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
| iTerm2 tabs | Register `kpurdon/iterm2` with `codex plugin marketplace add kpurdon/iterm2`; install `codex plugin add iterm2@kpurdon-iterm2` only when missing. Requires macOS, `uv`, and iTerm2 with its Python API enabled and tab-group support. | Verify `iterm2@kpurdon-iterm2` is installed and enabled, then use its `tabs` skill for a read-only destination inventory. Check fresh-session skill discovery separately; do not launch a tab for readiness inspection. |
| gh-stack CLI | Authenticated GitHub CLI; `gh extension install github/gh-stack` when absent. | Check extension provenance and `gh stack --help`. |
| gh-stack skill | Install directly from `github/gh-stack`, using `gh skill install` with a supported Codex user target or the available Codex skill-installer for upstream `skills/gh-stack`. Inspect installer help first. | Confirm the skill comes from upstream and is discoverable for the target home, not only the current working directory. |
| Locked external skills | From `$target_home`, run `npx --yes skills@1.7.6 experimental_install --frozen-lockfile` using the tracked `skills-lock.json`. Node/npm come from the machine's package manager. | Require restore success and an unchanged lockfile; verify the discovery links below. |
| Automatic task titles | The tracked `$target_home/bin/codex-task-title` uses `uv`, authenticated `codex`, and the shared local daemon; see [activation and scope](../../../README.md#automatic-task-titles). | Check the helper and both configured hooks. Leave hook trust to the user's `/hooks` review; report runtime naming as unverified until a prompt and completed turn exercise it. |

- For source conflicts, preserve the installed item and resolve the conflict before installation. Recheck the resulting state after every install; command success alone is insufficient.
- For additional selected plugins, resolve their exact source and identifier using the available plugin-management tools or native marketplace commands. Install through that supported path and follow its authentication flow. Keep app-bundled and workspace-managed plugins under their owning client/account; do not recreate them from local cache directories or broaden workspace permissions.
- When an installation result is uncertain, read state before retrying. Report unresolved failures with the dependency, observed error, and next action; do not loop or silently substitute another tool.

## Configure launchers

- Use the tracked `config.toml` as the default user configuration; preserve machine-specific integrations and app-managed fields. Reconcile existing settings before replacing an untracked config. Do not create a personal overlay or add a profile selector.
- When migrating from `personal.config.toml`, preserve a recoverable copy of both files and reconcile any local profile changes into `config.toml` before retiring the profile. Remove launcher profile flags as part of the same activation; an obsolete local overlay can still override the default settings.
- Locate the actual shell configuration and follow symlinks to their owner. Set `CODEX_HOME` to the resolved main checkout and remove `--profile personal` from existing Codex launchers such as `sgc`, preserving their working directory and argument forwarding. Avoid duplicate exports or wrappers on reruns.
- For versioned dotfiles, prepare changes in an isolated worktree and deliver through the normal PR workflow; do not edit through live symlinks or merge on the user's behalf. For unversioned configuration, preserve a recoverable original and change only the relevant settings. Keep activation pending while an old-home migration or source change is outstanding.

## Verify and hand off

- For each skill in `skills-lock.json`, verify `$target_home/.agents/skills/<name>/SKILL.md` exists and create the relative symlink `$target_home/skills/<name>` → `../.agents/skills/<name>` when absent. Preserve conflicting files or links and resolve them before replacement. Restore skips existing skill directories; use `--force --frozen-lockfile` only for an intentional reinstall after preserving local edits. Check discovery outside this repository after activation.
- Verify the personal [Chrome validation skill](../../../skills/chrome-validation/SKILL.md) exists at `$target_home/skills/chrome-validation/SKILL.md`. Its runtime prerequisites are the app-managed Chrome plugin and the `node_repl` tool. Preserve their owning client's setup; report missing prerequisites without copying cached packages or changing authorization checks. Verify global skill discovery in a fresh session outside this repository after activation; run live browser validation only when requested.
- Verify dependency identity, installation, enablement, and any required account connection separately. Use a small relevant read for connected tools; an installed plugin alone does not establish working authentication.
- Check shell syntax and launcher definitions without starting interactive sessions. Once changes are activated, verify the selected home and default settings in a fresh launch without a profile flag, skill discovery, and Builder's installed setup/readiness skill. If this requires a user restart or unavailable client control, leave that check explicitly pending.
- Run Builder's readiness checks from its installed package and verify the separate iTerm2 integration when selected. These checks do not authorize launching sessions or deployment probes. Report those separately if requested.
- Return a short account of what was already ready, what changed, and what remains blocked or unverified. Keep install/enablement, authentication, default configuration loading, and fresh-session readiness distinct. Do not claim the environment is ready while a required item remains pending.
