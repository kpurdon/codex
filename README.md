# Personal Codex guidance

This checkout is the Codex home. Git tracks personal guidance, the default `config.toml`, and setup instructions; runtime state remains local and ignored. [Builder](https://github.com/kpurdon/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance. [Personal guidance](AGENTS.md#semgrep-work) adds Semgrep's Seer and Datadog requirements.

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

## Session titles

T3 owns title generation and title controls for its threads. Standalone Codex uses its built-in naming. Personal guidance prefers `ISSUE-123: PR #456: Short description` when setting a title, omitting unknown identifiers and preserving established context unless the work's scope materially changes.

## Dependencies

The setup skill owns the [dependency inventory and verification](.agents/skills/setup-codex/SKILL.md#reconcile-dependencies): Builder, dispatcher, upstream gh-stack CLI, and its upstream skill. dispatcher provides initiative-scoped iTerm2/T3 session operations and retains the iTerm `tabs` helper. Keep the existing iTerm2 plugin and running sessions until an explicit migration verifies dispatcher in fresh sessions. Add dependencies that setup must install to the inventory. External skills managed by the Skills CLI are recorded in [skills-lock.json](skills-lock.json). Setup skips usable installations and reports sign-in or permission steps requiring your action. It runs on request, not on every startup.

Setup finishes with Builder's readiness checks and fresh-session verification where available. Installed packages, authenticated connections, and live handoff or deployment behavior are separate checks.

Broad PM/discovery sessions normally start at the Semgrep parent workspace. Once affected repositories are known, independent implementation sessions can start in their isolated worktrees. dispatcher records initiative membership separately from launch directories and UI groups, using the ignored `$CODEX_HOME/dispatcher/registry.sqlite3`. Builder's local project record references that inventory rather than duplicating it. Existing sessions remain unmanaged until explicitly adopted or transferred. New initiatives follow an explicit interface choice, then verified origin, with T3 as the fallback when origin is unknown. Existing initiatives retain their recorded backend. Launches, connected tools, and native title behavior need runtime evidence before claiming readiness.

## Chrome validation

Ordinary browser validation in T3 uses its native preview and fallback rules. The personal [Chrome validation skill](skills/chrome-validation/SKILL.md) covers explicit native Chrome/profile/tab/group requests and host-approved Chrome fallbacks. It uses the installed Chrome client's `setupBrowserRuntime()` through `node_repl`, including the workaround for [openai/codex#57641](https://github.com/openai/codex/issues/57641). The skill lives under `$CODEX_HOME/skills` for discovery across projects; after merging it into the active home, verify discovery in a fresh session. It requires the app-managed Chrome plugin and `node_repl`, and does not modify their authorization checks or configuration.

## External skills

[skills-lock.json](skills-lock.json) records the source revision and content hash for external skills, starting with `writing-clearly-and-concisely` from `obra/the-elements-of-style`. Git tracks the lockfile; downloaded files and local discovery links stay ignored.

From the main Codex home, restore with the pinned Skills CLI:

```sh
npx --yes skills@1.7.6 experimental_install --frozen-lockfile
```

The CLI restores into `.agents/skills/`. Setup creates a relative link for each locked skill under `skills/`, making it available across projects through this Codex home. For the writing skill, when the destination is absent:

```sh
ln -s ../.agents/skills/writing-clearly-and-concisely skills/writing-clearly-and-concisely
```

To add or update a dependency, run `npx --yes skills@1.7.6 add` with an explicit GitHub `/tree/<commit>/<skill-path>` URL, `--agent codex`, and `--yes`. Review the generated lockfile's `ref` and hash, then commit it. Restore is experimental; keep the CLI version pinned and verify a clean restore when changing dependencies or the CLI version.

## Local state

The tracked `config.toml` includes this machine's integration paths and app-managed settings; it is not a portable template. Clients may modify it, so inspect config diffs before committing and reconcile paths when using another machine. Never commit credentials. Memories, sessions, credentials, databases, and plugin caches remain ignored. The [Git allowlist](.gitignore) includes personal guidance, the default config, setup instructions, and the `setup-codex` and `chrome-validation` skills, and the external skill lockfile.

When migrating from an existing home, stop its clients and daemon and preserve a recoverable copy. Transfer runtime state without replacing this checkout's Git metadata or tracked guidance, and update shell, app, and configuration paths. Verify session resumption and required tools before removing the previous location.
