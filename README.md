# Personal Codex guidance

Personal preferences for Codex. [Builder](https://github.com/semgrep/builder) owns the engineering workflows; [GitHub's gh-stack](https://github.com/github/gh-stack) supplies stacked PR tools and guidance.

## Setup

Keep this checkout separate from the Codex runtime home. Install [AGENTS.md](AGENTS.md) as `$CODEX_HOME/AGENTS.md` (normally `~/.codex/AGENTS.md`) after reviewing and preserving any existing guidance. A symlink can keep the installed guidance synchronized with this checkout.

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

Maintain model, approval, UI, and machine-specific settings in the runtime home's `config.toml`. Keep memories, sessions, credentials, databases, plugin caches, and hook trust records there too. This repository does not manage or version them.

Before relocating an existing runtime home, stop its clients and daemon, preserve a recoverable copy, and update shell and app references. Verify session resumption and required tools before removing the previous location.
