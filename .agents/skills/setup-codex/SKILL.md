---
name: setup-codex
description: Use when asked to set up, repair, or verify this personal Codex home, including its dependencies.
---

# Set up this Codex home

Run Codex setup commands with `CODEX_HOME` set to the main checkout.

Check readiness read-only and honor intentional disables during setup.

## Reconcile dependencies

Install missing dependencies and verify they work.

| Dependency | Setup and verification |
| --- | --- |
| Builder | `builder@kpurdon-builder` from `kpurdon/builder`. |
| dispatcher | `dispatcher@kpurdon-dispatcher` from `kpurdon/dispatcher`, when requested. |
| Upstream gh-stack | The `github/gh-stack` extension and its upstream `gh-stack` skill. |

## Verify readiness

Verify the active home and skill discovery from a fresh session outside the checkout.
