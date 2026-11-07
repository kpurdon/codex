# Personal Codex guidance

This checkout is the Codex home. Git tracks personal guidance and setup instructions; runtime configuration and state remain local and ignored. [Builder](https://github.com/semgrep/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance.

## Setup

Set `CODEX_HOME` to the main checkout before starting Codex or installing its dependencies:

```sh
export CODEX_HOME="$HOME/code/github.com/kpurdon/codex"
```

Codex reads [AGENTS.md](AGENTS.md) directly from this home. Use worktrees to edit the tracked files while keeping the runtime pointed at the main checkout.

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

Start a fresh conversation, verify the skills are discoverable, and run Builder's setup action to check available capabilities. Installation and readiness checks do not establish live handoff or deployment behavior.

## Local state

Maintain model, approval, UI, and machine-specific settings in this checkout's ignored `config.toml`. Memories, sessions, credentials, databases, plugin caches, and hook trust records also live here without being committed. The [Git allowlist](.gitignore) tracks only `AGENTS.md`, `README.md`, and `.gitignore`.

When migrating from an existing home, stop its clients and daemon and preserve a recoverable copy. Transfer runtime state without replacing this checkout's Git metadata or tracked guidance, and update shell, app, and configuration paths. Verify session resumption and required tools before removing the previous location.
