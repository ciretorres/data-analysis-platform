---
description: Group changes into semantic commits and offer to push
---

Group all current changes into meaningful semantic commits and offer to push the current branch.

Optional context for commit messages: `$ARGUMENTS`

Rules:

- First inspect the full repository state:
  - `git status --short`
  - `git diff --stat`
  - `git diff`
  - `git log --oneline -10`
- Identify related file groups by intent: feature, fix, refactor, tests, docs, chore, release, or config.
- Create multiple commits when there are independent changes. Do not mix unrelated changes in the same commit.
- Write all commit messages in Spanish.
- If `$ARGUMENTS` is not empty, use it as context to adjust commit messages, but do not force that text if it does not accurately describe the changes.
- Use clear, semantic, concise commit messages that follow the repository’s recent style.
- Before committing, check for sensitive or suspicious files (`.env`, tokens, credentials, keys, or secrets). If any appear, stop and ask.
- Include new, modified, and deleted files that belong to each group.
- Do not revert existing changes.
- Do not use `--no-verify`.
- Do not amend commits.
- Do not force push.
- Update `changelog.md` with the changes that will be included in the planned commits:
  - First, review its current format and style.
  - Do not invent changes or include commit hashes or numbers that do not exist yet.
  - Include `changelog.md` in the appropriate commit. If it does not clearly fit another group, create a separate documentation commit for it.
  - Do not overwrite or remove existing changelog content unrelated to this update.

Flow:

1. Inspect the repository and identify the groups of changes.
2. Prepare an initial commit plan listing the files in each group.
3. Update `changelog.md` to reflect the changes in that plan.
4. Show the final commit plan, including the proposed `changelog.md` changes and the files included in each commit.
5. If the grouping is clear, continue. If there is real ambiguity, ask before making changes or commits.
6. For each group:
   - Add only the files for that group with `git add <files>`.
   - Create the commit with a semantic message in Spanish.
7. Once all commits have been created, ask me whether I want to run `git push` or do it manually.
8. When finished, summarize the commits created and, if a push was performed, the branch that was pushed.
