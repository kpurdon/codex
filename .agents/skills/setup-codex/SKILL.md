---
name: setup-codex
description: Set up or repair this personal Codex home and verify readiness.
---

# Set up this Codex home

Use the main checkout as `CODEX_HOME` and scope Codex commands to it with `env CODEX_HOME="$target_home" codex ...`.

Inspect readiness read-only, and during setup preserve existing settings, credentials, sessions, local changes, and intentional disables.

## Reconcile dependencies

Install missing dependencies through their existing owner and verify identity, enablement, and any required authentication.

| Dependency | Setup and verification |
| --- | --- |
| Builder | Register `kpurdon/builder` with `codex plugin marketplace add`, install `builder@kpurdon-builder` with `codex plugin add`, and verify with `codex plugin list --marketplace kpurdon-builder --json` and Builder’s readiness skill. |
| dispatcher | When requested, register `kpurdon/dispatcher`, install `dispatcher@kpurdon-dispatcher`, and verify registry help, discovery of `dispatch` and `tabs`, and capabilities on the selected backend. |
| Existing iTerm2 plugin | Keep it active until an authorized migration verifies dispatcher in fresh sessions. |
| Upstream gh-stack | Install with `gh extension install github/gh-stack` and install the upstream skill through `gh skill install` or the skill installer, then verify help and discovery. |
| Locked skills | Restore with `npx --yes skills@1.7.6 experimental_install --frozen-lockfile` in the main checkout and create missing `skills/<name>` → `../.agents/skills/<name>` links. |

## Configure launchers

Use the tracked default `config.toml`, point launchers at the main checkout, and reconcile legacy profile settings before removing `--profile personal`.

Edit managed shell configuration at its source, and get separate authority to migrate state from or disrupt an existing home.

## Verify readiness

Check launcher syntax and verify the effective home, defaults, and skill discovery in a fresh session outside the checkout, reporting any pending restart or unverified capability.

For native Chrome, verify discovery and the installed Chrome and `node_repl` prerequisites of the [Chrome validation skill](../../../skills/chrome-validation/SKILL.md).
