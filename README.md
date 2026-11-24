# Personal Codex home

The main checkout is `CODEX_HOME`. It holds [personal guidance](AGENTS.md), the default [config.toml](config.toml), and personal skills. [Dotfiles](https://github.com/kpurdon/dotfiles) configure the shell and launchers.

## Setup

Ask Codex to set up this home or invoke [`$setup-codex`](.agents/skills/setup-codex/SKILL.md) to install missing dependencies and verify readiness.

```sh
codex -C "$HOME/code/github.com/kpurdon/codex" 'Use $setup-codex to set up this Codex home.'
```

Use [`$chrome-validation`](skills/chrome-validation/SKILL.md) for native Chrome validation.

## Local state

Credentials, sessions, memories, and installed dependencies are ignored. Use worktrees to edit tracked files and review config diffs before committing because clients can update machine-specific settings.
