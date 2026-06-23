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
from urllib.parse import quote


VALID_DIFFICULTIES = {"easy", "medium", "hard"}
PROBLEM_FOLDER_RE = re.compile(r"^\d{4}-.+")
README_TOPICS_START = "<!---LeetCode Topics Start-->"
README_TOPICS_END = "<!---LeetCode Topics End-->"
README_CATEGORIES_START = "<!---Algorithm Categories Start-->"
README_CATEGORIES_END = "<!---Algorithm Categories End-->"
TOPIC_ROW_RE = re.compile(r"^\| \[(?P<label>[^\]]+)\]\((?P<url>[^)]+)\) \|$")
GITHUB_TREE_URL = "https://github.com/BibinSanju/LeetCode/tree/master"
ALGORITHM_CATEGORIES = (
    "Hash Map and Frequency",
    "Two Pointers",
    "Sliding Window",
    "Prefix Sum and Difference Array",
    "Stack and Monotonic Stack",
    "Binary Search",
    "Linked List",
    "Trees and BST",
    "Heap and Priority Queue",
    "Backtracking",
    "Intervals",
    "Graph DFS and BFS",
    "Topological Sort and Dependency Graphs",
    "Union Find - Disjoint Set Union",
    "Greedy",
    "Dynamic Programming",
    "Trie",
    "Bit Manipulation",
    "Shortest Path and Weighted Graph",
    "Basic Array and String",
)
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
    problem_dirs: list[Path] = []
    category_names = set(ALGORITHM_CATEGORIES)

    for path in repo_root.iterdir():
        if not path.is_dir():
            continue

        if PROBLEM_FOLDER_RE.match(path.name):
            problem_dirs.append(path)
            continue

        if path.name in category_names:
            problem_dirs.extend(
                child
                for child in path.iterdir()
                if child.is_dir() and PROBLEM_FOLDER_RE.match(child.name)
            )

    seen: dict[str, Path] = {}
    duplicates: list[str] = []
    for problem_dir in problem_dirs:
        existing = seen.get(problem_dir.name)
        if existing is None:
            seen[problem_dir.name] = problem_dir
        else:
            duplicates.append(
                f"{problem_dir.name} ({relative_to_repo(repo_root, existing)}, "
                f"{relative_to_repo(repo_root, problem_dir)})"
            )

    if duplicates:
        raise StatsError(f"duplicate problem folders found: {', '.join(duplicates)}")

    return sorted(
        problem_dirs,
        key=lambda path: (problem_sort_key(path.name), relative_to_repo(repo_root, path)),
    )


def find_problem_dir(repo_root: Path, problem_name: str) -> Path | None:
    for problem_dir in problem_folders(repo_root):
        if problem_dir.name == problem_name:
            return problem_dir
    return None


def problem_algorithm(repo_root: Path, problem_dir: Path) -> str | None:
    parent = problem_dir.parent
    if parent == repo_root:
        return None
    if parent.parent == repo_root and parent.name in ALGORITHM_CATEGORIES:
        return parent.name
    return None


def problem_sort_key(problem_name: str) -> tuple[int, str]:
    match = re.match(r"^(\d+)", problem_name)
    if match:
        return int(match.group(1)), problem_name
    return sys.maxsize, problem_name


def github_tree_url(repo_root: Path, path: Path) -> str:
    encoded_path = "/".join(
        quote(part, safe="") for part in relative_to_repo(repo_root, path).split("/")
    )
    return f"{GITHUB_TREE_URL}/{encoded_path}"


def problem_category_row(repo_root: Path, problem_dir: Path) -> str:
    return f"| [{problem_dir.name}]({github_tree_url(repo_root, problem_dir)}) |"


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


def normalize_topics(topics: list[str] | None) -> list[str]:
    if topics is None:
        return []

    normalized: list[str] = []
    seen: set[str] = set()
    for topic in topics:
        clean_topic = topic.strip()
        if not clean_topic:
            raise StatsError("topic names cannot be empty")
        if clean_topic not in seen:
            normalized.append(clean_topic)
            seen.add(clean_topic)
    return normalized


def problem_topic_row(problem_name: str) -> str:
    return f"| [{problem_name}]({GITHUB_TREE_URL}/{problem_name}) |"


def problem_name_from_topic_row(match: re.Match[str]) -> str:
    url = match.group("url")
    github_tree_prefix = f"{GITHUB_TREE_URL}/"
    if url.startswith(github_tree_prefix):
        return url[len(github_tree_prefix) :]
    return match.group("label")


def split_topic_sections(
    block: list[str],
) -> tuple[list[str], list[dict[str, Any]]]:
    intro: list[str] = []
    sections: list[dict[str, Any]] = []
    index = 0

    while index < len(block) and not block[index].startswith("## "):
        intro.append(block[index])
        index += 1

    while index < len(block):
        heading = block[index]
        if not heading.startswith("## "):
            raise StatsError(f"unexpected line in README topics block: {heading}")

        topic = heading[3:].strip()
        if not topic:
            raise StatsError("README topic heading cannot be empty")

        index += 1
        table_lines: list[str] = []
        while index < len(block) and not block[index].startswith("## "):
            table_lines.append(block[index])
            index += 1

        non_empty_lines = [line for line in table_lines if line.strip()]
        if len(non_empty_lines) < 2:
            raise StatsError(f"{topic}: topic table is missing its header")
        if non_empty_lines[0] != "|  |" or non_empty_lines[1] != "| ------- |":
            raise StatsError(f"{topic}: topic table header is not in the expected format")

        rows: list[tuple[str, str]] = []
        for row in non_empty_lines[2:]:
            match = TOPIC_ROW_RE.match(row)
            if not match:
                raise StatsError(f"{topic}: invalid topic row: {row}")
            rows.append((problem_name_from_topic_row(match), row))

        sections.append({"topic": topic, "rows": rows})

    return intro, sections


def render_topic_sections(
    intro: list[str],
    sections: list[dict[str, Any]],
) -> list[str]:
    lines = intro[:]
    for section in sections:
        sorted_rows = sorted(section["rows"], key=lambda row: problem_sort_key(row[0]))
        lines.extend([f"## {section['topic']}", "|  |", "| ------- |"])
        lines.extend(row_line for _, row_line in sorted_rows)
    return lines


def update_root_readme_topics(
    repo_root: Path,
    problem_name: str,
    topics: list[str],
) -> list[str]:
    readme_path = repo_root / "README.md"
    if not readme_path.is_file():
        raise StatsError("README.md was not found")

    problem_dir = repo_root / problem_name
    if not problem_dir.is_dir() or not PROBLEM_FOLDER_RE.match(problem_name):
        raise StatsError(f"{problem_name}: problem folder was not found")

    desired_topics = normalize_topics(topics)
    if not desired_topics:
        raise StatsError("at least one topic is required")

    original_text = readme_path.read_text(encoding="utf-8")
    lines = original_text.splitlines()

    start_indexes = [i for i, line in enumerate(lines) if line == README_TOPICS_START]
    end_indexes = [i for i, line in enumerate(lines) if line == README_TOPICS_END]
    if len(start_indexes) != 1 or len(end_indexes) != 1:
        raise StatsError("README.md must have exactly one LeetCode topics start marker and one end marker")

    start_index = start_indexes[0]
    end_index = end_indexes[0]
    if start_index >= end_index:
        raise StatsError("README.md LeetCode topics markers are out of order")

    intro, sections = split_topic_sections(lines[start_index + 1 : end_index])
    topic_names = [section["topic"] for section in sections]
    duplicate_topics = sorted(
        topic for topic in set(topic_names) if topic_names.count(topic) > 1
    )
    if duplicate_topics:
        raise StatsError(f"README.md has duplicate topic sections: {', '.join(duplicate_topics)}")

    desired_topic_set = set(desired_topics)
    target_row = problem_topic_row(problem_name)
    changes: list[str] = []

    for section in sections:
        topic = section["topic"]
        old_rows = section["rows"]
        matching_rows = [row_line for row_problem, row_line in old_rows if row_problem == problem_name]
        rows_without_problem = [
            (row_problem, row_line)
            for row_problem, row_line in old_rows
            if row_problem != problem_name
        ]

        if topic in desired_topic_set:
            section["rows"] = rows_without_problem + [(problem_name, target_row)]
            if not matching_rows:
                changes.append(f"README.md: add {problem_name} to {topic}")
            elif len(matching_rows) != 1 or matching_rows[0] != target_row:
                changes.append(f"README.md: update {problem_name} in {topic}")
        else:
            section["rows"] = rows_without_problem
            if matching_rows:
                changes.append(f"README.md: remove {problem_name} from {topic}")

    existing_topics = {section["topic"] for section in sections}
    for topic in desired_topics:
        if topic not in existing_topics:
            sections.append({"topic": topic, "rows": [(problem_name, target_row)]})
            existing_topics.add(topic)
            changes.append(f"README.md: create topic {topic} with {problem_name}")

    non_empty_sections: list[dict[str, Any]] = []
    for section in sections:
        if section["rows"]:
            non_empty_sections.append(section)
        else:
            changes.append(f"README.md: remove empty topic {section['topic']}")

    new_lines = (
        lines[: start_index + 1]
        + render_topic_sections(intro, non_empty_sections)
        + lines[end_index:]
    )
    new_text = "\n".join(new_lines) + "\n"

    if new_text != original_text:
        if not changes:
            changes.append("README.md: sort topic rows")
        readme_path.write_text(new_text, encoding="utf-8")

    return changes


def algorithm_category_block(repo_root: Path, problem_dirs: list[Path]) -> list[str]:
    rows_by_category: dict[str, list[Path]] = {
        category: [] for category in ALGORITHM_CATEGORIES
    }
    uncategorized: list[Path] = []

    for problem_dir in problem_dirs:
        category = problem_algorithm(repo_root, problem_dir)
        if category is None:
            uncategorized.append(problem_dir)
        else:
            rows_by_category[category].append(problem_dir)

    lines = [README_CATEGORIES_START, "# Algorithm Categories"]
    for category in ALGORITHM_CATEGORIES:
        rows = sorted(
            rows_by_category[category],
            key=lambda path: problem_sort_key(path.name),
        )
        lines.extend([f"## {category}", "| Problem |", "| ------- |"])
        lines.extend(problem_category_row(repo_root, problem_dir) for problem_dir in rows)

    if uncategorized:
        lines.extend(["## Uncategorized", "| Problem |", "| ------- |"])
        lines.extend(
            problem_category_row(repo_root, problem_dir)
            for problem_dir in sorted(
                uncategorized,
                key=lambda path: problem_sort_key(path.name),
            )
        )

    lines.append(README_CATEGORIES_END)
    return lines


def readme_category_marker_indexes(lines: list[str]) -> tuple[int, int] | None:
    marker_pairs = (
        (README_CATEGORIES_START, README_CATEGORIES_END),
        (README_TOPICS_START, README_TOPICS_END),
    )

    for start_marker, end_marker in marker_pairs:
        start_indexes = [i for i, line in enumerate(lines) if line == start_marker]
        end_indexes = [i for i, line in enumerate(lines) if line == end_marker]
        if len(start_indexes) > 1 or len(end_indexes) > 1:
            raise StatsError(
                f"README.md must not have duplicate {start_marker} or {end_marker} markers"
            )
        if start_indexes or end_indexes:
            if len(start_indexes) != 1 or len(end_indexes) != 1:
                raise StatsError(
                    f"README.md must have matching {start_marker} and {end_marker} markers"
                )
            start_index = start_indexes[0]
            end_index = end_indexes[0]
            if start_index >= end_index:
                raise StatsError("README.md algorithm category markers are out of order")
            return start_index, end_index

    return None


def update_root_readme_categories(
    repo_root: Path,
    problem_dirs: list[Path],
    *,
    write: bool,
) -> list[str]:
    readme_path = repo_root / "README.md"
    if not readme_path.is_file():
        raise StatsError("README.md was not found")

    original_text = readme_path.read_text(encoding="utf-8")
    lines = original_text.splitlines()
    marker_indexes = readme_category_marker_indexes(lines)
    replacement = algorithm_category_block(repo_root, problem_dirs)

    if marker_indexes is None:
        prefix = lines
        if prefix and prefix[-1].strip():
            prefix = prefix + [""]
        new_lines = prefix + replacement
    else:
        start_index, end_index = marker_indexes
        new_lines = lines[:start_index] + replacement + lines[end_index + 1 :]

    new_text = "\n".join(new_lines) + "\n"
    if new_text == original_text:
        return []

    if write:
        readme_path.write_text(new_text, encoding="utf-8")

    return ["README.md: update algorithm categories"]


def build_expected_stats(
    repo_root: Path,
    stats: dict[str, Any],
    *,
    prompt_for_difficulty: bool,
    difficulty_overrides: dict[str, str] | None = None,
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

        if difficulty_overrides and problem_name in difficulty_overrides:
            difficulty = difficulty_overrides[problem_name]
        else:
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
        description="Check or update LeetCode stats.json hashes, counts, and algorithm README links.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python sync_stats.py --check\n"
            "  python sync_stats.py --write\n"
            "  python sync_stats.py --write --problem 0189-rotate-array --difficulty medium "
            "--algorithm \"Two Pointers\""
        ),
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
        help="update stats.json in place; prompts for missing difficulty values unless --difficulty is provided for --problem",
    )
    parser.add_argument(
        "--problem",
        help="problem folder to update, for example 0189-rotate-array",
    )
    parser.add_argument(
        "--difficulty",
        choices=sorted(VALID_DIFFICULTIES),
        help="difficulty to store for --problem",
    )
    parser.add_argument(
        "--algorithm",
        choices=ALGORITHM_CATEGORIES,
        help="primary algorithm folder for --problem; quote names with spaces",
    )
    parser.add_argument(
        "--topics",
        nargs="+",
        help=argparse.SUPPRESS,
    )

    args = parser.parse_args()
    if args.topics is not None:
        parser.error("--topics is no longer used; pass --algorithm instead")

    problem_args = [
        args.problem is not None,
        args.difficulty is not None,
        args.algorithm is not None,
    ]
    if any(problem_args):
        if not args.write:
            parser.error("--problem, --difficulty, and --algorithm can only be used with --write")
        if not all(problem_args):
            parser.error("--problem, --difficulty, and --algorithm must be used together")
    return args


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    stats_path = repo_root / "stats.json"

    try:
        problem_dirs = problem_folders(repo_root)
        readme_changes: list[str] = []
        difficulty_overrides: dict[str, str] | None = None
        if args.problem:
            problem_dir = find_problem_dir(repo_root, args.problem)
            if problem_dir is None:
                raise StatsError(f"{args.problem}: problem folder was not found")
            actual_algorithm = problem_algorithm(repo_root, problem_dir)
            if actual_algorithm != args.algorithm:
                raise StatsError(
                    f"{args.problem}: expected algorithm folder {args.algorithm}, "
                    f"found {actual_algorithm or 'repo root'}"
                )
            difficulty_overrides = {args.problem: args.difficulty}

        readme_changes = update_root_readme_categories(
            repo_root,
            problem_dirs,
            write=args.write,
        )
        current = load_stats(stats_path)
        expected, changes = build_expected_stats(
            repo_root,
            current,
            prompt_for_difficulty=args.write,
            difficulty_overrides=difficulty_overrides,
        )
        changes = readme_changes + changes
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
        target = "README.md and stats.json" if readme_changes else "stats.json"
        print(f"Updated {target} ({len(changes)} change(s)):")
        for change in changes:
            print(f"- {change}")
    else:
        print("stats.json is already up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
