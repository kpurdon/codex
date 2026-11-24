# Personal guidance

- Use Builder for engineering workflows and upstream `gh-stack` for stacked PRs.
- Prefer authenticated `gh` for GitHub unless I request the connector or `gh` lacks access or capability.
- Refresh existing connections within authorized scope, keeping the same account and permissions.
- Read applicable repository guidance and skills, use isolated worktrees under `~/.worktrees/`, and preserve unrelated changes.
- Prefer direct repository commands and use scripts when they simplify shared state, cleanup, or error handling.
- Lead with the result and any action I need to take, report material changes, and use guided walkthroughs only on request.
- Keep task records private and findings in the conversation unless I request an artifact or repository policy requires one.
- Add tests or documentation for concrete gaps and keep task plans, inventories, runbooks, and session notes out of tracked docs unless requested or required.
- Use conventional titles and publish accepted changes as drafts assigned to me.
- Obtain independent review before handoff, using a reviewer subagent when needed, and fix confirmed findings.
- For personal tooling, validate locally and hand off a reviewed draft with the current remote check status.
- Require explicit authority for merges, auto-merge, external messages, comments, and submitted reviews, and establish authority for deployment and runtime validation separately.
- Sign agent-authored GitHub comments and reviews, Linear comments, and Slack messages with `_🤖 on behalf of @kpurdon_`.
- Use dispatcher for initiative membership and session mechanics, keeping `iterm2` available until its replacement is verified.
- An explicit PM assignment authorizes in-scope tracker maintenance and management of its recorded sessions.
- Use the requested or recorded session interface, then the verified origin for a new initiative, with T3 as the fallback.
- Use native title controls and preserve established context, adding known ticket and PR IDs.
- Inspect requested browser targets read-only unless authorized to make changes, using T3 preview by default and the personal Chrome skill for explicit native Chrome requests.
- Keep notifications in the conversation.

## Semgrep work

- Start broad discovery in the Semgrep workspace and independent implementation in repository worktrees, keeping coupled work with its owner.
- Observe Kargo through the configured MCP and use the configured Argo CD integration for workload evidence.
- Default to merge readiness with independent review, required CI, and approval from Seer on the latest head, marking ready after independent review clears to trigger Seer.
- In requested Seer remediation, reply with fixes or evidence-backed `/fp` or `/ar` dispositions and resolve the addressed threads.
- Deliver Datadog resource changes through `semgrep-app-terraform`, with direct changes limited to unmanaged notebooks and dashboards or an explicit Terraform override.
