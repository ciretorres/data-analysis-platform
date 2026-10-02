---
description: Group changes into semantic commits and push
---

Group all current changes into meaningful semantic commits and push the current branch.

Optional context for commit messages: `$ARGUMENTS``

Rules:

- First inspect the full repository state:
    - `git status --short`
    - `git diff --stat`
    - `git diff`
    - `git log --oneline-10`
- Indentify related file groups by intent: feature, fix, refactor, tests, docs, chore, release, or config.
- Create multiple commits when there are independent changes. Do not mix unrelated changes in the same commit.
- Write all commit messages in Spanish.
- If `$ARGUMENTS`is not empty, use it as context to adjust commit messages, but do not force that text if it does not accurrately describe the changes.
- Use clear, semantic, concise commit messahes that follow the repo's recent style.
- Before committing, check for sensitive or suspicious files (`.env`, tokens, credential, keys, secrets). If any appear, stop and ask.
- Include new, modified, and deleted files that belong to each group.
- Do not revert existing changes.
- Do not use `--no-verify`.
- Do not amend commits.
- Do not force push.

Flow:

1. Show the proposed commit plan with the files included in each commit.
2. If the grouping is clear, continue. If there is real ambiguity, as before commiting.
3. For each group:
    - Add only the files for that group with `git add <files>`.
    - Create the commits with a semantic message.
4. Once all commit have been created, ask me if I wanna make the `git push` manually or I want you to run it.
5. When finised, summarize the commits created and the branch that was pushed if it applies.