# LeetCode Repository Guide

Use this guide when you add a new LeetCode problem or replace an existing solution with a better one. The root `README.md` is displayed on the repository home page, so keep its existing generated structure intact.

## Current Structure

Each problem lives in its own folder at the repository root:

```text
0001-two-sum/
  0001-two-sum.py
  README.md
```

Follow this pattern:

- Folder name: `problem-number-problem-slug`, for example `0001-two-sum`.
- Solution file: same name as the folder, with the correct language extension, for example `0001-two-sum.py` or `0268-missing-number.java`.
- Problem README: `README.md` inside the problem folder. This usually contains the LeetCode problem statement.

## Replace an Existing Solution With an Optimal Solution

1. Open the problem folder you want to improve.
2. Edit only that problem's solution file, for example `0001-two-sum/0001-two-sum.py`.
3. Keep the LeetCode class and method signature valid. Do not rename `class Solution` or the required method unless LeetCode uses a different signature for that problem.
4. Test the solution on LeetCode or with local test cases.
5. Update `stats.json` automatically:

```powershell
python sync_stats.py --write
```

6. Do not change `solved`, `easy`, `medium`, or `hard` manually when you only replace an existing solution. The sync script keeps those counts unchanged unless problem entries change.

## Add a New Problem Solution

1. Create a new folder using the same naming pattern, for example `0002-add-two-numbers`.
2. Add the solution file inside that folder, for example `0002-add-two-numbers.py`.
3. Add the LeetCode problem statement as `0002-add-two-numbers/README.md`.
4. Add the problem link to every correct topic table in the root `README.md`.
5. Keep the root README topic marker comments exactly where they are. The start marker must stay directly before `# LeetCode Topics`, and the end marker must stay after the final topic table.
6. Preserve the topic table format:

```markdown
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/BibinSanju/LeetCode/tree/master/0001-two-sum) |
```

7. Update `stats.json` automatically:

```powershell
python sync_stats.py --write
```

If this is a new problem, the script prompts for difficulty. Enter `easy`, `medium`, or `hard`.

## How to Use sync_stats.py

Use `sync_stats.py` from the repository root to keep `stats.json` in sync with the problem folders.

Check only:

```powershell
python sync_stats.py --check
```

This reports outdated hashes, wrong solution keys, count mismatches, missing entries, or invalid difficulty values. It does not edit files and does not prompt for input.

Write fixes:

```powershell
python sync_stats.py --write
```

This updates `stats.json` in place. If a problem is new or has no valid difficulty, it asks:

```text
Difficulty for 0002-add-two-numbers (easy/medium/hard):
```

The script updates:

- Root README hash
- Problem solution hashes
- Problem README hashes
- Wrong solution file keys
- `easy`, `medium`, `hard`, and `solved` counts

It preserves this field unchanged:

```json
"stats.json": {
    "": "existing_hash_here"
}
```

A file cannot reliably contain its own current hash, so do not try to refresh the `stats.json` self-hash manually.

Manual hash command, if you ever need to inspect one value:

```powershell
git hash-object 0001-two-sum/0001-two-sum.py
```

## Validate Before Committing

Run these checks after editing files:

```powershell
python sync_stats.py --check
node -e "JSON.parse(require('fs').readFileSync('stats.json','utf8')); console.log('stats.json OK')"
git status --short
```

Also confirm:

- The root `README.md` still has one LeetCode topic start marker and one end marker.
- `solved` equals `easy + medium + hard`.
- When adding a new problem, the number of problem folders matches `solved`.
- `python sync_stats.py --check` reports `stats.json is up to date.`

## Quick Checklist

For an existing solution update:

1. Edit the solution file.
2. Test it.
3. Run `python sync_stats.py --write`.
4. Run `python sync_stats.py --check`.
5. Validate JSON and commit.

For a new problem:

1. Add the problem folder.
2. Add the solution file and problem `README.md`.
3. Add the problem to the correct root README topic tables.
4. Run `python sync_stats.py --write` and enter the difficulty.
5. Run `python sync_stats.py --check`.
6. Validate JSON, counts, folder count, and hashes.
