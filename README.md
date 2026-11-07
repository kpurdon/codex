# Personal Codex guidance

This checkout is the Codex home. Git tracks personal guidance, the default `config.toml`, and setup instructions; runtime state remains local and ignored. [Builder](https://github.com/semgrep/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance.

## Setup

From this checkout, ask Codex to "set up this Codex home" or invoke `$setup-codex`. The repository-local [setup skill](.agents/skills/setup-codex/SKILL.md) installs missing dependencies, prepares launchers that use the default config, and verifies readiness. It can be discovered before this checkout becomes the active home:

```sh
codex -C "$HOME/code/github.com/kpurdon/codex" 'Use $setup-codex to set up this Codex home.'
```

The intended `CODEX_HOME` is the main `kpurdon/codex` checkout. Codex reads [AGENTS.md](AGENTS.md) directly from that home. Use worktrees to edit tracked files while keeping the runtime pointed at the main checkout. Setup preserves existing state; moving an old home is a separate migration step.

## Personal settings

[config.toml](config.toml) holds the default model, reasoning, approval, subagent, terminal, and integration settings. Launch Codex without a profile flag:

```sh
codex
```

Codex [loads the user config by default](https://learn.chatgpt.com/docs/config-file/config-basic); trusted project configuration and command-line overrides can take precedence. Shell launchers such as `sgc` should use this default configuration too. Personal guidance prefers the authenticated `gh` CLI for GitHub work, with the connector available when explicitly requested or needed for access or capability.

When adopting this change in an existing home, back up the untracked `config.toml` and any locally modified `personal.config.toml` before updating the checkout. Reconcile their current settings into the tracked config, remove `--profile personal` from launchers, and retire the old profile only after preserving its local changes. The companion dotfiles change removes that flag from `sgc`. Verify the effective defaults in a fresh session after activation.

## Dependencies

The setup skill owns the [dependency inventory and verification](.agents/skills/setup-codex/SKILL.md#reconcile-dependencies): Builder, upstream gh-stack CLI, and its upstream skill. Add dependencies that setup must install there. The writing skill below is vendored in Git. Setup skips usable installations and reports sign-in or permission steps requiring your action. It runs on request, not on every startup.

Setup finishes with Builder's readiness checks and fresh-session verification where available. Installed packages, authenticated connections, and live handoff or deployment behavior are separate checks.

## Chrome validation

The personal [Chrome validation skill](skills/chrome-validation/SKILL.md) uses the installed Chrome client's `setupBrowserRuntime()` through `node_repl` for Chrome-based validation. This is the tested workaround for [openai/codex#57641](https://github.com/openai/codex/issues/57641), where `cua_repl` reports `The browser access host is unavailable`. The skill lives under `$CODEX_HOME/skills` for discovery across projects; after merging it into the active home, verify discovery in a fresh session. It requires the app-managed Chrome plugin and `node_repl`, and does not modify their authorization checks or configuration.

## Writing style

The [writing skill](skills/writing-clearly-and-concisely/SKILL.md) and its reference are tracked under `skills/`, so cloning this repository carries them to the new Codex home. No separate installation is needed. Keep this as the only installed copy; `npx skills` does not manage its updates.

Both files are unchanged from [obra/the-elements-of-style at `05fc4f0`](https://github.com/obra/the-elements-of-style/tree/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/skills/writing-clearly-and-concisely). Upstream identifies the 1918 Strunk text as public domain. To update, review and copy both files from a chosen upstream revision, then update this source link in the same PR.

## Local state

The tracked `config.toml` includes this machine's integration paths and app-managed settings; it is not a portable template. Clients may modify it, so inspect config diffs before committing and reconcile paths when using another machine. Never commit credentials. Memories, sessions, credentials, databases, and plugin caches remain ignored. The [Git allowlist](.gitignore) includes personal guidance, the default config, setup instructions, and the `setup-codex`, `chrome-validation`, and `writing-clearly-and-concisely` skills.

When migrating from an existing home, stop its clients and daemon and preserve a recoverable copy. Transfer runtime state without replacing this checkout's Git metadata or tracked guidance, and update shell, app, and configuration paths. Verify session resumption and required tools before removing the previous location.
