from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


VALID_DIFFICULTIES = {"easy", "medium", "hard"}
PROBLEM_FOLDER_RE = re.compile(r"^\d{4}-.+")
SOLUTION_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".cxx",
    ".go",
    ".java",
    ".js",
    ".kt",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".scala",
    ".sql",
    ".swift",
    ".ts",
}


class StatsError(Exception):
    pass


def relative_to_repo(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def git_hash_object(repo_root: Path, path: Path) -> str:
    result = subprocess.run(
        ["git", "hash-object", relative_to_repo(repo_root, path)],
        cwd=repo_root,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise StatsError(f"git hash-object failed for {path}: {message}")
    return result.stdout.strip()


def load_stats(stats_path: Path) -> dict[str, Any]:
    try:
        with stats_path.open("r", encoding="utf-8") as handle:
            stats = json.load(handle)
    except FileNotFoundError as exc:
        raise StatsError("stats.json was not found") from exc
    except json.JSONDecodeError as exc:
        raise StatsError(f"stats.json is not valid JSON: {exc}") from exc

    leetcode = stats.get("leetcode")
    if not isinstance(leetcode, dict):
        raise StatsError('stats.json must contain an object at key "leetcode"')
    shas = leetcode.get("shas")
    if not isinstance(shas, dict):
        raise StatsError('stats.json must contain an object at key "leetcode.shas"')
    return stats


def write_stats(stats_path: Path, stats: dict[str, Any]) -> None:
    with stats_path.open("w", encoding="utf-8") as handle:
        json.dump(stats, handle, indent=4)
        handle.write("\n")


def problem_folders(repo_root: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in repo_root.iterdir()
            if path.is_dir() and PROBLEM_FOLDER_RE.match(path.name)
        ),
        key=lambda path: path.name,
    )


def find_solution_file(problem_dir: Path) -> Path:
    candidates = sorted(
        (
            path
            for path in problem_dir.iterdir()
            if path.is_file() and path.suffix.lower() in SOLUTION_EXTENSIONS
        ),
        key=lambda path: path.name,
    )
    preferred = [path for path in candidates if path.stem == problem_dir.name]

    if len(preferred) == 1:
        return preferred[0]
    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        raise StatsError(f"{problem_dir.name}: no solution file found")

    names = ", ".join(path.name for path in candidates)
    raise StatsError(
        f"{problem_dir.name}: multiple solution files found ({names}); "
        "keep one solution file or name the primary file after the folder"
    )


def prompt_difficulty(problem_name: str) -> str:
    while True:
        try:
            value = input(f"Difficulty for {problem_name} (easy/medium/hard): ")
        except EOFError as exc:
            raise StatsError(
                f"{problem_name}: difficulty is required, but input was not available"
            ) from exc

        difficulty = value.strip().lower()
        if difficulty in VALID_DIFFICULTIES:
            return difficulty
        print("Please enter easy, medium, or hard.")


def get_difficulty(
    problem_name: str,
    entry: dict[str, Any],
    *,
    prompt_when_missing: bool,
) -> tuple[str | None, list[str]]:
    changes: list[str] = []
    current = entry.get("difficulty")
    difficulty = current.strip().lower() if isinstance(current, str) else ""

    if difficulty in VALID_DIFFICULTIES:
        if current != difficulty:
            changes.append(f"{problem_name}: normalize difficulty to {difficulty}")
        return difficulty, changes

    if prompt_when_missing:
        difficulty = prompt_difficulty(problem_name)
        changes.append(f"{problem_name}: set difficulty to {difficulty}")
        return difficulty, changes

    changes.append(
        f"{problem_name}: missing or invalid difficulty; run --write and enter one"
    )
    return None, changes


def entry_matches(entry: Any, expected: dict[str, str]) -> bool:
    return isinstance(entry, dict) and entry == expected


def set_if_changed(
    container: dict[str, Any],
    key: str,
    value: Any,
    label: str,
    changes: list[str],
) -> None:
    if container.get(key) != value:
        changes.append(label)
        container[key] = value


def build_expected_stats(
    repo_root: Path,
    stats: dict[str, Any],
    *,
    prompt_for_difficulty: bool,
) -> tuple[dict[str, Any], list[str]]:
    expected = copy.deepcopy(stats)
    leetcode = expected["leetcode"]
    shas = leetcode["shas"]
    changes: list[str] = []
    counts: Counter[str] = Counter()
    seen_problem_names: set[str] = set()

    for problem_dir in problem_folders(repo_root):
        problem_name = problem_dir.name
        seen_problem_names.add(problem_name)

        old_entry = shas.get(problem_name)
        entry = old_entry if isinstance(old_entry, dict) else {}
        solution_file = find_solution_file(problem_dir)
        readme_file = problem_dir / "README.md"
        if not readme_file.is_file():
            raise StatsError(f"{problem_name}: README.md was not found")

        difficulty, difficulty_changes = get_difficulty(
            problem_name,
            entry,
            prompt_when_missing=prompt_for_difficulty,
        )
        changes.extend(difficulty_changes)
        if difficulty is None:
            continue

        counts[difficulty] += 1
        expected_entry = {
            solution_file.name: git_hash_object(repo_root, solution_file),
            "README.md": git_hash_object(repo_root, readme_file),
            "difficulty": difficulty,
        }

        if not entry_matches(old_entry, expected_entry):
            if old_entry is None:
                changes.append(f"{problem_name}: add stats entry")
            else:
                old_solution_keys = [
                    key
                    for key in entry
                    if key not in {"README.md", "difficulty"}
                ]
                if old_solution_keys != [solution_file.name]:
                    changes.append(
                        f"{problem_name}: use solution key {solution_file.name}"
                    )
                elif entry.get(solution_file.name) != expected_entry[solution_file.name]:
                    changes.append(f"{problem_name}: update solution hash")

                if entry.get("README.md") != expected_entry["README.md"]:
                    changes.append(f"{problem_name}: update README.md hash")
                if entry.get("difficulty") != expected_entry["difficulty"]:
                    changes.append(f"{problem_name}: update difficulty")

            shas[problem_name] = expected_entry

    stale_problem_keys = sorted(
        key
        for key in shas
        if PROBLEM_FOLDER_RE.match(key) and key not in seen_problem_names
    )
    for key in stale_problem_keys:
        changes.append(f"{key}: remove stale stats entry")
        del shas[key]

    root_readme = repo_root / "README.md"
    if root_readme.is_file():
        root_readme_entry = shas.get("README.md")
        if not isinstance(root_readme_entry, dict):
            root_readme_entry = {}
            shas["README.md"] = root_readme_entry
        root_hash = git_hash_object(repo_root, root_readme)
        if root_readme_entry.get("") != root_hash:
            changes.append("README.md: update root hash")
            root_readme_entry[""] = root_hash

    set_if_changed(leetcode, "easy", counts["easy"], "easy: update count", changes)
    set_if_changed(leetcode, "medium", counts["medium"], "medium: update count", changes)
    set_if_changed(leetcode, "hard", counts["hard"], "hard: update count", changes)
    set_if_changed(
        leetcode,
        "solved",
        sum(counts.values()),
        "solved: update count",
        changes,
    )

    return expected, changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check or update LeetCode stats.json hashes and counts."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check",
        action="store_true",
        help="report required stats.json changes without editing",
    )
    mode.add_argument(
        "--write",
        action="store_true",
        help="update stats.json in place; prompts for missing difficulty values",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    stats_path = repo_root / "stats.json"

    try:
        current = load_stats(stats_path)
        expected, changes = build_expected_stats(
            repo_root,
            current,
            prompt_for_difficulty=args.write,
        )
    except StatsError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    if args.check:
        if changes:
            print("stats.json needs updates:")
            for change in changes:
                print(f"- {change}")
            return 1
        print("stats.json is up to date.")
        return 0

    if changes:
        write_stats(stats_path, expected)
        print(f"Updated stats.json ({len(changes)} change(s)):")
        for change in changes:
            print(f"- {change}")
    else:
        print("stats.json is already up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
