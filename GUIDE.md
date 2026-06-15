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
5. Generate the new hash for the changed solution file:

```powershell
git hash-object 0001-two-sum/0001-two-sum.py
```

6. In `stats.json`, update only that solution file's hash:

```json
"0001-two-sum": {
    "0001-two-sum.py": "new_hash_here",
    "README.md": "existing_readme_hash_here",
    "difficulty": "easy"
}
```

7. Do not change `solved`, `easy`, `medium`, or `hard` when you only replace an existing solution.

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

7. Update `stats.json`:
   - Increase `solved` by `1`.
   - Increase exactly one difficulty count: `easy`, `medium`, or `hard`.
   - Add a new entry under `stats.leetcode.shas` for the new problem folder.

Example new problem entry:

```json
"0002-add-two-numbers": {
    "0002-add-two-numbers.py": "solution_file_hash_here",
    "README.md": "problem_readme_hash_here",
    "difficulty": "medium"
}
```

## How to Update stats.json

`stats.json` stores Git blob hashes. Generate them with `git hash-object`.

Useful commands:

```powershell
git hash-object 0001-two-sum/0001-two-sum.py
git hash-object 0001-two-sum/README.md
git hash-object README.md
```

Update these fields only when the related file changes:

- Root README hash: `stats.leetcode.shas["README.md"][""]`
- Problem solution hash: `stats.leetcode.shas["problem-folder"]["solution-file"]`
- Problem README hash: `stats.leetcode.shas["problem-folder"]["README.md"]`
- Problem difficulty: `stats.leetcode.shas["problem-folder"]["difficulty"]`

Leave this field unchanged:

```json
"stats.json": {
    "": "existing_hash_here"
}
```

A file cannot reliably contain its own current hash, so do not try to refresh the `stats.json` self-hash manually.

## Validate Before Committing

Run these checks after editing files:

```powershell
node -e "JSON.parse(require('fs').readFileSync('stats.json','utf8')); console.log('stats.json OK')"
git status --short
```

Also confirm:

- The root `README.md` still has one LeetCode topic start marker and one end marker.
- `solved` equals `easy + medium + hard`.
- When adding a new problem, the number of problem folders matches `solved`.
- Any changed solution, problem README, or root README hash in `stats.json` matches `git hash-object`.

## Quick Checklist

For an existing solution update:

1. Edit the solution file.
2. Test it.
3. Run `git hash-object` on the solution file.
4. Update that solution hash in `stats.json`.
5. Validate JSON and counts.

For a new problem:

1. Add the problem folder.
2. Add the solution file and problem `README.md`.
3. Add the problem to the correct root README topic tables.
4. Update counts and hashes in `stats.json`.
5. Validate JSON, counts, folder count, and hashes.
