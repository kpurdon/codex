# Personal Codex guidance

This checkout is the Codex home. Git tracks personal guidance, a portable settings profile, and setup instructions; machine configuration and runtime state remain local and ignored. [Builder](https://github.com/semgrep/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance.

## Setup

From this checkout, ask Codex to "set up this Codex home" or invoke `$setup-codex`. The repository-local [setup skill](.agents/skills/setup-codex/SKILL.md) installs missing dependencies, prepares profile-aware launchers, and verifies readiness. It can be discovered before this checkout becomes the active home:

```sh
codex -C "$HOME/code/github.com/kpurdon/codex" 'Use $setup-codex to set up this Codex home.'
```

The intended `CODEX_HOME` is the main `kpurdon/codex` checkout. Codex reads [AGENTS.md](AGENTS.md) directly from that home. Use worktrees to edit tracked files while keeping the runtime pointed at the main checkout. Setup preserves existing state; moving an old home is a separate migration step.

## Personal settings

[personal.config.toml](personal.config.toml) preserves model, reasoning, approval, subagent, and terminal preferences. Select it explicitly:

```sh
codex --profile personal
```

The [profile](https://learn.chatgpt.com/docs/config-file/config-advanced#profiles) overlays local `config.toml`; trusted project configuration and command-line overrides take precedence. Its presence alone does not activate it. Shell launchers such as `sgc` should pass `--profile personal` when adopting this setup. Desktop settings remain local unless the client explicitly selects this profile.

## Dependencies

The setup skill owns the [dependency inventory and verification](.agents/skills/setup-codex/SKILL.md#reconcile-dependencies): Builder, upstream gh-stack CLI, and its upstream skill. Add explicitly selected dependencies there rather than copying installed packages into Git. Setup skips usable installations and reports sign-in or permission steps requiring your action. It runs on request, not on every startup.

Setup finishes with Builder's readiness checks and fresh-session verification where available. Installed packages, authenticated connections, and live handoff or deployment behavior are separate checks.

## Local state

Keep machine-specific paths, integrations, trust records, and app-managed settings in this checkout's ignored `config.toml`. Memories, sessions, credentials, databases, and plugin caches also live here without being committed. The [Git allowlist](.gitignore) includes personal guidance, the profile, setup instructions, and the `setup-codex` skill.

When migrating from an existing home, stop its clients and daemon and preserve a recoverable copy. Transfer runtime state without replacing this checkout's Git metadata or tracked guidance, and update shell, app, and configuration paths. Verify session resumption and required tools before removing the previous location.
