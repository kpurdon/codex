# Personal guidance

- Reconnect existing integrations as needed using the same account and permissions.
- Use isolated worktrees for changes.
- Prefer direct commands for routine shell work.
- When you need me to act, tell me exactly what to do and include only what I need to do it.
- Use conventional commit messages and PR titles, and assign PRs to me.
- Obtain independent review before handoff, using a reviewer subagent when needed, and fix confirmed findings.
- Require explicit approval for merges, auto-merge, and external communications, with separate authority for deployment and runtime validation.
- Append `_🤖 on behalf of <my handle on that service>_` to agent-authored GitHub comments and reviews, Linear comments, and Slack messages.

## Semgrep work

- For merge readiness, mark drafts ready after independent review and address Seer feedback until Seer approves the latest head. During requested remediation, you may reply with fixes or evidence-backed `/fp` or `/ar` and resolve addressed threads.
- Use `semgrep-app-terraform` for Datadog changes, except to create unmanaged dashboards and notebooks or when I explicitly authorize a Terraform override.
