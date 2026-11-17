---
name: setup-codex
description: Set up or repair this personal Codex home by installing missing dependencies, configuring default-config launchers, and verifying readiness. Use for a request to set up this Codex environment; creating or reviewing this skill does not run setup.
---

# Set up this Codex home

Carry a setup request through installation and verification. Follow the repository's [personal guidance](../../../AGENTS.md). A request only to inspect readiness stays read-only.

## Establish the target

- Resolve the main `kpurdon/codex` checkout from the request and Git worktree metadata. Use that checkout as the target home; a review worktree is only a source for edits. Confirm its `AGENTS.md` and `config.toml` exist before configuring launchers.
- Inspect the effective `CODEX_HOME`, existing configuration, installed dependencies, and shell startup links. Preserve user settings, credentials, sessions, unrelated tools, and dirty work. Never print or commit credentials. Preserve existing app-managed configuration and review generated paths before committing config changes.
- Scope every Codex installation and inventory command to the target with `env CODEX_HOME="$target_home" codex ...`. Use the default configuration without `--profile personal`.
- If another home contains existing runtime state, prepare the target without changing the running session or activating new launchers. Report migration and restart as pending. Moving credentials/databases, stopping daemons, deleting the old home, or installing startup hooks needs an explicit migration or automation request; ordinary setup does not include those actions.

## Reconcile dependencies

- Use the inventory below plus dependencies explicitly selected by the user. Installed unrelated plugins are not requests to reproduce them. Inspect current native help and state before changing anything; a failed lookup or denied access does not mean a dependency is absent.
- Install missing prerequisites needed by this inventory through the machine's existing package manager. Dotfiles owns executable installation and shell configuration; preserve its conventions and avoid a whole-machine upgrade. If sign-in, permission, or a consequential source choice blocks a step, request that specific action and continue independent work.
- Skip items already present and usable. Do not upgrade, reinstall, or overwrite an intentional disable on every run. Diagnose unusable versions and changed sources before repair; resolve an intentional disable with the user when it prevents the requested setup.

| Dependency | Source and installation | Verification |
| --- | --- | --- |
| Builder | Register `kpurdon/builder` with `codex plugin marketplace add kpurdon/builder`; install `codex plugin add builder@kpurdon-builder` only when missing. | Inspect the marketplace source and `codex plugin list --marketplace kpurdon-builder --json`; require the exact installed plugin with `enabled: true`. |
| dispatcher | Register `kpurdon/dispatcher` with `codex plugin marketplace add kpurdon/dispatcher`; install `codex plugin add dispatcher@kpurdon-dispatcher` when requested and missing. It includes `dispatch` and the compatible `tabs` skill. The registry uses Python 3.10+; iTerm2 needs macOS, `uv`, and its enabled Python API. T3 uses injected tools or a configured MCP connection. | Verify the plugin is enabled, run the bundled registry's `--help`, and check native capabilities for the selected backend. Require fresh-session discovery of both skills. CLI presence alone does not establish T3 retirement support. Do not launch or adopt sessions for readiness inspection. |
| Existing iTerm2 installation | Preserve `iterm2@kpurdon-iterm2` and its running sessions during dispatcher preparation. Keep its source unchanged until dispatcher is available. | Use its `tabs` skill for read-only destination inspection. After dispatcher discovery and selected-backend readiness are verified, disable the old plugin only as part of an authorized migration; do not uninstall it or close active sessions. |
| gh-stack CLI | Authenticated GitHub CLI; `gh extension install github/gh-stack` when absent. | Check extension provenance and `gh stack --help`. |
| gh-stack skill | Install directly from `github/gh-stack`, using `gh skill install` with a supported Codex user target or the available Codex skill-installer for upstream `skills/gh-stack`. Inspect installer help first. | Confirm the skill comes from upstream and is discoverable for the target home, not only the current working directory. |
| Locked external skills | From `$target_home`, run `npx --yes skills@1.7.6 experimental_install --frozen-lockfile` using the tracked `skills-lock.json`. Node/npm come from the machine's package manager. | Require restore success and an unchanged lockfile; verify the discovery links below. |

- For source conflicts, preserve the installed item and resolve the conflict before installation. Recheck the resulting state after every install; command success alone is insufficient.
- dispatcher runtime state uses `$CODEX_HOME/dispatcher/registry.sqlite3`, outside tracked files. Project records reference this single registry and their stable initiative IDs. Do not populate it by adopting existing terminals, guessing PM ownership, or scanning all sessions. Installing dispatcher and transferring management of a running initiative are separate actions.
- For additional selected plugins, resolve their exact source and identifier using the available plugin-management tools or native marketplace commands. Install through that supported path and follow its authentication flow. Keep app-bundled and workspace-managed plugins under their owning client/account; do not recreate them from local cache directories or broaden workspace permissions.
- When an installation result is uncertain, read state before retrying. Report unresolved failures with the dependency, observed error, and next action; do not loop or silently substitute another tool.

## Configure launchers

- Use the tracked `config.toml` as the default user configuration; preserve machine-specific integrations and app-managed fields. Reconcile existing settings before replacing an untracked config. Do not create a personal overlay or add a profile selector.
- When migrating from `personal.config.toml`, preserve a recoverable copy of both files and reconcile any local profile changes into `config.toml` before retiring the profile. Remove launcher profile flags as part of the same activation; an obsolete local overlay can still override the default settings.
- Locate the actual shell configuration and follow symlinks to their owner. Set `CODEX_HOME` to the resolved main checkout and remove `--profile personal` from existing Codex launchers such as `sgc`, preserving their working directory and argument forwarding. Avoid duplicate exports or wrappers on reruns.
- For versioned dotfiles, prepare changes in an isolated worktree and deliver through the normal PR workflow; do not edit through live symlinks or merge on the user's behalf. For unversioned configuration, preserve a recoverable original and change only the relevant settings. Keep activation pending while an old-home migration or source change is outstanding.

## Verify and hand off

- For each skill in `skills-lock.json`, verify `$target_home/.agents/skills/<name>/SKILL.md` exists and create the relative symlink `$target_home/skills/<name>` → `../.agents/skills/<name>` when absent. Preserve conflicting files or links and resolve them before replacement. Restore skips existing skill directories; use `--force --frozen-lockfile` only for an intentional reinstall after preserving local edits. Check discovery outside this repository after activation.
- For ordinary browser validation in T3, follow its native preview and fallback rules. Verify the personal [Chrome validation skill](../../../skills/chrome-validation/SKILL.md) for explicit native Chrome/profile/tab/group requests or a host-approved fallback. Its runtime prerequisites are the app-managed Chrome plugin and the `node_repl` tool. Preserve their owning client's setup; report missing prerequisites without copying cached packages or changing authorization checks. Verify global skill discovery in a fresh session outside this repository after activation; run live browser validation only when requested.
- Verify dependency identity, installation, enablement, and any required account connection separately. Use a small relevant read for connected tools; an installed plugin alone does not establish working authentication.
- Check shell syntax and launcher definitions without starting interactive sessions. Once changes are activated, verify the selected home and default settings in a fresh launch without a profile flag, skill discovery, and Builder's installed setup/readiness skill. If this requires a user restart or unavailable client control, leave that check explicitly pending.
- Run Builder's readiness checks from its installed package and verify the separate iTerm2 integration when selected. These checks do not authorize launching sessions or deployment probes. Report those separately if requested.
- Return a short account of what was already ready, what changed, and what remains blocked or unverified. Keep install/enablement, authentication, default configuration loading, and fresh-session readiness distinct. Do not claim the environment is ready while a required item remains pending.
