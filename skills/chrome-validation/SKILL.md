---
name: chrome-validation
description: Validate websites and tab groups in the user's native Google Chrome through the installed Chrome client in node_repl. Use for Chrome-based browser validation, including when cua_repl reports that the browser access host is unavailable.
---

# Chrome validation

Use the installed Chrome client's `setupBrowserRuntime()` in `node_repl` for Chrome validation. This personal workaround addresses the `cua_repl` initialization failure `The browser access host is unavailable`, tracked in [openai/codex#57641](https://github.com/openai/codex/issues/57641). The [reported alternate initialization](https://github.com/openai/codex/issues/57641#issuecomment-6701344387) worked locally on 2026-11-07 for navigation, page reads, tab-group membership, collapse/expand, and cleanup. It does not repair `cua_repl`.

Use this route directly while the workaround is needed; do not repeat the known failing bootstrap on every validation request. When reassessing it after an app/plugin update or a confirmed upstream fix, retest the normal route before retiring this skill. An issue being closed alone is not local acceptance evidence.

## Connect

- State the target site and checks. Use the browser/profile the user requested and keep inspection within that scope. A validation request does not authorize live product changes.
- Reuse existing runtime, browser, and tab bindings within a `node_repl` session. Otherwise discover the `node_repl` JavaScript tool and resolve the active `CODEX_HOME` from the environment or host configuration. This checkout uses a custom home; do not assume `~/.codex` or point runtime setup at a review worktree.
- Confirm `<CODEX_HOME>/plugins/cache/openai-bundled/chrome/latest/scripts/browser-client.mjs` exists. Use the installed `latest` link rather than a version-pinned cache path. If the tool or client is unavailable, report that prerequisite; do not install or patch the runtime as part of validation.
- Run the following in `node_repl`, replacing the home placeholder with the resolved absolute path. `process` is not available there; resolve the home before this call. Do not run the browser client in a shell or import a separate browser controller.

```js
var chromeCodexHome = "/absolute/path/to/active/CODEX_HOME";
var { pathToFileURL } = await import("node:url");
var { setupBrowserRuntime } = await import(pathToFileURL(
  `${chromeCodexHome}/plugins/cache/openai-bundled/chrome/latest/scripts/browser-client.mjs`
).href);
var chromeAgent = await setupBrowserRuntime();
var chromeCandidates = (await chromeAgent.browsers.list()).filter(
  browser => browser.type === "extension" && browser.name === "Chrome"
);
nodeRepl.write(chromeCandidates);
```

Select the matching profile from this live list. If several match and the request does not identify one, ask which profile to use. If none match, report Chrome as unavailable. Never substitute another browser or assume a persistent browser ID.

For a single matching profile:

```js
if (chromeCandidates.length !== 1) throw new Error("Select the requested Chrome profile first");
var chromeBrowser = await chromeAgent.browsers.get(chromeCandidates[0].id);
nodeRepl.write(await chromeBrowser.documentation());
```

Read the returned documentation before using browser controls, and say which Chrome profile connected. Name the session before creating or claiming tabs:

```js
await chromeBrowser.nameSession("🧪 Chrome validation");
```

## Validate and leave the intended state

- Use the connected runtime's documented APIs and current page observations. Ground clicks in a fresh accessibility state, and verify the resulting page or state after interaction.
- For an existing user tab, follow the runtime's `user.openTabs()` and `user.claimTab()` instructions. For a new validation page, use `tabs.new()` and `tab.goto()`; choose URLs from the user's target or observed links.
- For requested tab-group validation, read the `management` capability documentation. Inspect the created tabs' actual group IDs and query group membership; a session name alone does not prove grouping. Only exercise collapse/expand or other group changes on the requested group or disposable test group. Keep unrelated tabs and groups intact.
- Close disposable tabs and verify cleanup. When the user asks to keep the group/pages open, mark each intended tab with `markDeliverable()` before ending the turn; otherwise agent-created tabs can disappear at turn cleanup. Use `markHandoff()` only for unfinished work awaiting user action.
- Report the checks that passed, limitations, and what remains open. A successful connection alone is not proof of navigation, interaction, or tab-group support.
- If the alternate path fails or rejects an operation, report the blocker. Do not strip `require-browser-access.mjs`, modify `BROWSER_USE_ACCESS_*`, fabricate session identity, or change browser security settings to make validation pass.
