---
name: setup-codex
description: Set up or repair this personal Codex home by installing missing dependencies, configuring profile-aware launchers, and verifying readiness. Use for a request to set up this Codex environment; creating or reviewing this skill does not run setup.
---

# Set up this Codex home

Carry a setup request through installation and verification. Follow the repository's [personal guidance](../../../AGENTS.md). A request only to inspect readiness stays read-only.

## Establish the target

- Resolve the main `kpurdon/codex` checkout from the request and Git worktree metadata. Use that checkout as the target home; a review worktree is only a source for edits. Confirm its `AGENTS.md` and `personal.config.toml` exist before configuring launchers.
- Inspect the effective `CODEX_HOME`, existing configuration, installed dependencies, and shell startup links. Preserve user settings, credentials, sessions, unrelated tools, and dirty work. Never print credentials or copy app-generated cache paths into tracked files.
- Scope every Codex installation and inventory command to the target with `env CODEX_HOME="$target_home" codex ...`. Profile flags belong on supported runtime commands; do not pass `--profile` to plugin commands.
- If another home contains existing runtime state, prepare the target without changing the running session or activating new launchers. Report migration and restart as pending. Moving credentials/databases, stopping daemons, deleting the old home, or installing startup hooks needs an explicit migration or automation request; ordinary setup does not include those actions.

## Reconcile dependencies

- Use the inventory below plus dependencies explicitly selected by the user. Installed unrelated plugins are not requests to reproduce them. Inspect current native help and state before changing anything; a failed lookup or denied access does not mean a dependency is absent.
- Install missing prerequisites needed by this inventory through the machine's existing package manager. Dotfiles owns executable installation and shell configuration; preserve its conventions and avoid a whole-machine upgrade. If sign-in, permission, or a consequential source choice blocks a step, request that specific action and continue independent work.
- Skip items already present and usable. Do not upgrade, reinstall, or overwrite an intentional disable on every run. Diagnose unusable versions and changed sources before repair; resolve an intentional disable with the user when it prevents the requested setup.

| Dependency | Source and installation | Verification |
| --- | --- | --- |
| Builder | Register `semgrep/builder` with `codex plugin marketplace add semgrep/builder`; install `codex plugin add builder@semgrep-builder` only when missing. | Inspect the marketplace source and `codex plugin list --marketplace semgrep-builder --json`; require the exact installed plugin with `enabled: true`. |
| gh-stack CLI | Authenticated GitHub CLI; `gh extension install github/gh-stack` when absent. | Check extension provenance and `gh stack --help`. |
| gh-stack skill | Install directly from `github/gh-stack`, using `gh skill install` with a supported Codex user target or the available Codex skill-installer for upstream `skills/gh-stack`. Inspect installer help first. | Confirm the skill comes from upstream and is discoverable for the target home, not only the current working directory. |

- If a marketplace name or installed item resolves to another source, preserve it and resolve the conflict before installation. Recheck the resulting state after every install; command success alone is insufficient.
- For additional selected plugins, resolve their exact source and identifier using the available plugin-management tools or native marketplace commands. Install through that supported path and follow its authentication flow. Keep app-bundled and workspace-managed plugins under their owning client/account; do not recreate them from local cache directories or broaden workspace permissions.
- When an installation result is uncertain, read state before retrying. Report unresolved failures with the dependency, observed error, and next action; do not loop or silently substitute another tool.

## Configure launchers

- Use the tracked `personal.config.toml` as an overlay on the target's local `config.toml`; preserve machine-specific integrations and app-managed fields. Select it with `codex --profile personal`. Do not replace the base config or use the obsolete `profile = "personal"` selector.
- Locate the actual shell configuration and follow symlinks to their owner. Set `CODEX_HOME` to the resolved main checkout and make existing Codex launchers such as `sgc` pass `--profile personal`, preserving their working directory and argument forwarding. Avoid duplicate exports or wrappers on reruns.
- For versioned dotfiles, prepare changes in an isolated worktree and deliver through the normal PR workflow; do not edit through live symlinks or merge on the user's behalf. For unversioned configuration, preserve a recoverable original and change only the relevant settings. Keep activation pending while an old-home migration or source change is outstanding.

## Verify and hand off

- Verify dependency identity, installation, enablement, and any required account connection separately. Use a small relevant read for connected tools; an installed plugin alone does not establish working authentication.
- Check shell syntax and launcher definitions without starting interactive sessions. Once changes are activated, verify the selected home and profile in a fresh launch, skill discovery, and Builder's installed setup/readiness skill. If this requires a user restart or unavailable client control, leave that check explicitly pending.
- Run Builder's readiness checks from its installed package; they do not authorize launching iTerm sessions or deployment probes. Report those separately if requested.
- Return a short account of what was already ready, what changed, and what remains blocked or unverified. Keep install/enablement, authentication, profile selection, and fresh-session readiness distinct. Do not claim the environment is ready while a required item remains pending.
