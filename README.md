# Personal Codex guidance

This checkout is the Codex home. Git tracks personal guidance, a portable settings profile, and setup instructions; machine configuration and runtime state remain local and ignored. [Builder](https://github.com/semgrep/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance.

## Setup

Set `CODEX_HOME` to the main checkout before starting Codex or installing its dependencies:

```sh
export CODEX_HOME="$HOME/code/github.com/kpurdon/codex"
```

Codex reads [AGENTS.md](AGENTS.md) directly from this home. Use worktrees to edit the tracked files while keeping the runtime pointed at the main checkout.

## Personal settings

[personal.config.toml](personal.config.toml) preserves model, reasoning, approval, subagent, and terminal preferences. Select it explicitly:

```sh
codex --profile personal
```

The [profile](https://learn.chatgpt.com/docs/config-file/config-advanced#profiles) overlays local `config.toml`; trusted project configuration and command-line overrides take precedence. Its presence alone does not activate it. Shell launchers such as `sgc` should pass `--profile personal` when adopting this setup. Desktop settings remain local unless the client explicitly selects this profile.

## Dependencies

Install Builder following its [setup instructions](https://github.com/semgrep/builder#install):

```sh
codex plugin marketplace add semgrep/builder
codex plugin add builder@semgrep-builder
```

Install gh-stack and its skill directly from [upstream](https://github.com/github/gh-stack#installation), using an authenticated GitHub CLI with `gh skill` support:

```sh
gh extension install github/gh-stack
gh skill install github/gh-stack
```

Verify Builder's installed entry has `enabled: true`, then check gh-stack:

```sh
codex plugin list --marketplace semgrep-builder --json
gh stack --help
```

Keep installation commands here as the dependency inventory; do not commit installed copies or cache paths. Additional plugins need their stable marketplace source and plugin selector recorded here. App-bundled and workspace-managed plugins depend on the client and signed-in workspace; configure those through the plugin browser and verify them after sign-in. Connected services still require authentication.

Start a fresh conversation with the personal profile, verify the skills are discoverable, and run Builder's setup action to check available capabilities. Installation and readiness checks do not establish live handoff or deployment behavior.

## Local state

Keep machine-specific paths, integrations, trust records, and app-managed settings in this checkout's ignored `config.toml`. Memories, sessions, credentials, databases, and plugin caches also live here without being committed. The [Git allowlist](.gitignore) tracks only `AGENTS.md`, `README.md`, `personal.config.toml`, and `.gitignore`.

When migrating from an existing home, stop its clients and daemon and preserve a recoverable copy. Transfer runtime state without replacing this checkout's Git metadata or tracked guidance, and update shell, app, and configuration paths. Verify session resumption and required tools before removing the previous location.
