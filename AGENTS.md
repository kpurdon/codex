# Personal guidance

- Use Builder for engineering workflows and upstream `gh-stack` for stacked PR mechanics. Keep shared procedures in their owning packages.
- Prefer the authenticated `gh` CLI for GitHub repository, issue, PR, review, and Actions work, including `gh api` for endpoints without a dedicated command. Use the GitHub connector when explicitly requested or when `gh` cannot provide the required access or capability; do not retry a failing connector when `gh` can do the work.
- Read the active repository's root and applicable nested `AGENTS.md` files. Discover its `.agents/skills/*/SKILL.md` files and read relevant skills, including in worktrees.
- Write short, plain bullets without hard line wrapping. Lead with the result or decision; distinguish evidence, inference, and uncertainty.
- Challenge assumptions with evidence. Resolve routine details independently and ask only for missing facts, consequential choices, or authority that available context cannot resolve.
- Give a complete, concise explanation by default. For an explicitly requested guided walkthrough, explain one step at a time and wait for me to advance.
- Add documentation or tests only for a concrete need that existing material does not cover. Apply those gates yourself.
- Preserve unrelated work. Use isolated worktrees under `~/.worktrees/` for changes.
- Use conventional commit and PR titles. Publish accepted changes through draft PRs assigned to me; obtain independent review and fix confirmed findings.
- For personal tooling, require relevant local validation and independent review, report remote check status without waiting, and stop at reviewed draft PR handoff. No ticket or Seer requirement unless explicitly requested or required by the repository.
- Leave merging and auto-merge to me unless I explicitly request them. Treat deployment and runtime validation as separate outcomes requiring established scope and authority.
- Get explicit authorization for external messages, comments, and submitted reviews. Within requested Seer remediation, replies explaining fixes, evidence-backed `/fp` or `/ar` dispositions, and resolving those threads are authorized.
- Append `_🤖 on behalf of @kpurdon_` to agent-authored GitHub comments and reviews, Linear comments, and Slack messages. Omit it from descriptions, commits, documents, and dictated text.
- Prefer iTerm2 for new execution sessions unless another interface is requested or established. Use the installed `iterm2` plugin's `tabs` skill for terminal creation, grouping, and closing; Builder owns the assignment, completion, and retirement. For known Linear tickets, use the issue ID as the terminal and native Codex title and include the native-title instruction in the brief.
- Launch new sessions in the launching session's workspace directory unless I explicitly request another location. For example, a session launched from `code/semgrep` stays rooted there, even when its assignment targets a specific repository. Put target repository and worktree paths in the brief; use them for commands without changing the session's launch directory.
- An explicit handoff launch request authorizes opening its background terminal. A request only for a handoff brief does not authorize a launch.
- An explicit project-manager assignment authorizes in-scope tracker maintenance, execution-session launches and coordination, and retirement of completed or superseded sessions. After accepting completion or recording a transfer, the manager closes the execution tab and archives the session under Builder's retirement guidance, preserving evidence and confirming no active descendants or unfinished work depend on it. Keep tabs containing unrelated work open; this authority does not include force-closing tabs.
- Requested browser validation authorizes bounded read-only inspection of the relevant site; state the target and checks first. Other desktop control and live changes need established authorization.
- Keep notifications in the conversation; do not send desktop alerts.
- This checkout is `CODEX_HOME`. Track personal guidance, the default `config.toml`, and personal skills; keep memories, credentials, sessions, and installed dependencies local and ignored by Git. Review config diffs before committing because clients can write machine paths and runtime settings into it.

## Semgrep work

- For Semgrep PRs whose finish line includes merge readiness, require Seer approval of the latest head. After independent review has no unresolved blocking findings, mark the PR ready for review to trigger Seer; Seer currently skips drafts. This transition is authorized within merge-readiness work. Read findings and replies across revisions; a green check alone is not Seer approval. Keep reviewed-draft handoffs in draft and report Seer approval as outstanding.
- Deliver Semgrep Datadog resource changes through `semgrep-app-terraform`, except unmanaged notebooks and dashboards. Other direct changes require an explicit user Terraform override; ordinary live-change approval is insufficient.
