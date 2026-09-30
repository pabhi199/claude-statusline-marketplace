# Quick Statusline

A Claude Code statusline showing: model name, working directory, git branch, session cost, and session duration.

## Install

From inside Claude Code:

```
/plugin marketplace add pabhi199/claude-statusline-marketplace
/plugin install quick-statusline@abhishek-statusline-marketplace
```

## Activate

Claude Code plugins cannot wire up `statusLine` automatically — add this to your
`~/.claude/settings.json` (or project `.claude/settings.json`) yourself, once:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/plugins/marketplaces/abhishek-statusline-marketplace/plugins/quick-statusline/bin/statusline.py"
  }
}
```

`${CLAUDE_PLUGIN_ROOT}` does **not** resolve here — that placeholder only expands
inside hook commands, MCP/LSP server configs, monitor commands, and skill/agent
content (confirmed against the Claude Code plugin manifest docs). The main
`statusLine` setting isn't one of those, so plugins can never wire it up
automatically, and referencing `${CLAUDE_PLUGIN_ROOT}` in it silently fails
(no statusline shows, no error). Use the `~`-relative path above instead —
`~` expands to your home directory on every OS, and the marketplace-checkout
path stays stable across plugin version updates (unlike the versioned
`plugins/cache/.../<version>/` path).

Restart Claude Code (or start a new session) to see the statusline.

## Uninstall

```
/plugin uninstall quick-statusline@abhishek-statusline-marketplace
```

Then remove the `statusLine` entry from settings.json.
