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
4. Update the root `README.md` topic tables and `stats.json` together:

```powershell
python sync_stats.py --write --problem 0002-add-two-numbers --difficulty medium --topics "Linked List" Math Recursion
```

Use `easy`, `medium`, or `hard` for `--difficulty`. Quote topic names that contain spaces, such as `"Two Pointers"` or `"Linked List"`.

## How to Use sync_stats.py

Use `sync_stats.py` from the repository root to keep `stats.json` in sync with the problem folders. It can also update the root `README.md` topic tables when you pass a problem, difficulty, and topics.

Check only:

```powershell
python sync_stats.py --check
```

This reports outdated hashes, wrong solution keys, count mismatches, missing entries, or invalid difficulty values. It does not edit files and does not prompt for input.

Write hash/stat fixes only:

```powershell
python sync_stats.py --write
```

This updates `stats.json` in place. If a problem is new or has no valid difficulty, it asks:

```text
Difficulty for 0002-add-two-numbers (easy/medium/hard):
```

Update one problem's root README topics and stats together:

```powershell
python sync_stats.py --write --problem 0189-rotate-array --difficulty medium --topics Array Math "Two Pointers"
```

This command:

- Adds the problem to only the topics you list.
- Removes the problem from old or wrong topic sections.
- Creates a new topic section when you pass a topic that does not exist yet.
- Removes an empty topic section after moving the problem out of it.
- Sorts each topic table by problem number.
- Refreshes the root README hash, problem hashes, difficulty, and counts in `stats.json`.

If you pass the wrong topics, rerun the same command with the correct `--topics`. The script removes stale topic rows automatically.

The script updates:

- Root README hash
- Root README topic tables when `--problem`, `--difficulty`, and `--topics` are passed
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

## Local LeetCode Browser Automation

The `extension/` folder contains a local Chrome/Edge extension that can save an accepted LeetCode solution into this repository. It talks to the local Python helper in `automation/local_leetcode_server.py`.

Start the helper from the repository root:

```powershell
python automation/local_leetcode_server.py
```

The helper prints a local token. Keep that terminal open, then load the extension:

1. Open Chrome or Edge extension management.
2. Enable developer mode.
3. Choose "Load unpacked".
4. Select this repository's `extension` folder.
5. Open the extension popup and paste the token from the helper.

On a LeetCode problem page:

1. Submit until the result is accepted.
2. Write or paste your approach notes in LeetCode Notes when possible.
3. Click `Save to Local Repo`.
4. If notes cannot be read, type or paste them in the local editor.
5. Review the preview. If the folder already exists, confirm overwrite.
6. Click `Save and commit`.

The helper writes the problem folder, canonicalizes `README.md`, runs the combined `sync_stats.py` command, validates with `python sync_stats.py --check`, stages only the problem folder plus root `README.md` and `stats.json`, and commits with the Time/Space message shown in the editor.

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
3. Run `python sync_stats.py --write --problem <problem-folder> --difficulty <easy|medium|hard> --topics <topic> ...`.
4. Run `python sync_stats.py --check`.
5. Validate JSON, counts, folder count, root README topics, and hashes.
