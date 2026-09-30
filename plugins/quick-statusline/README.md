# Quick Statusline

A Claude Code statusline plugin.

## What it does

Adds a status bar at the bottom of Claude Code showing, on one line:

- Current model name
- Working directory (shortened with `~`)
- Git branch (if the working directory is inside a git repo)
- Session cost so far (USD)
- Session duration

It reads the JSON Claude Code feeds it on stdin (model, cwd, cost, etc.) and prints
a formatted, color-coded line — see `bin/statusline.py`.

## Install

From inside Claude Code:

```
/plugin marketplace add pabhi199/claude-statusline-marketplace
/plugin install quick-statusline@abhishek-statusline-marketplace
```

This downloads the plugin and enables it — but **the statusline will not appear
yet**. See below.

## Activate (required manual step)

Add this to your `~/.claude/settings.json` (global) or project `.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/plugins/marketplaces/abhishek-statusline-marketplace/plugins/quick-statusline/bin/statusline.py"
  }
}
```

Then **restart Claude Code** (`/exit`, then run `claude` again — or open a new session).

### Why this step can't be automated

Claude Code plugins are not allowed to set the main `statusLine` setting for
you. Per the plugin system's design, when a plugin is enabled, only two keys
from its own config carry over into your settings automatically: `agent` and
`subagentStatusLine`. `statusLine` (the one that actually renders the bar at
the bottom of the screen) is deliberately excluded — every statusline plugin,
including this one, requires the user to add that block by hand, once.

Don't use `${CLAUDE_PLUGIN_ROOT}` in the `command` value — it looks like the
"proper" way to reference a plugin's own files, but that placeholder only
expands inside hook commands, MCP/LSP server configs, monitor commands, and
skill/agent content. `statusLine` isn't one of those, so it silently fails
(no error, no statusline) if you try it there. The `~`-relative path above
is the form that actually works — `~` expands to your home directory on
every OS, and the marketplace-checkout path it points to stays the same
across plugin version updates, unlike the versioned
`plugins/cache/.../<version>/...` path.

### Why the restart is required

Claude Code reads `statusLine` from settings once at session start. It
doesn't hot-reload settings.json mid-session, so a change only takes effect
in a new session — hence `/exit` + relaunch (or opening a fresh session)
after editing the config.

## Verify it's working

Test the script directly, independent of Claude Code, by feeding it sample input:

```bash
echo '{"model":{"display_name":"Sonnet 5"},"cwd":"'"$HOME"'","cost":{"total_cost_usd":0.05,"total_duration_ms":90000}}' \
  | ~/.claude/plugins/marketplaces/abhishek-statusline-marketplace/plugins/quick-statusline/bin/statusline.py
```

If that prints a colored status line, the script itself is fine and any
remaining issue is in `settings.json` (wrong path, JSON typo, or the session
hasn't restarted yet).

## Uninstall

```
/plugin uninstall quick-statusline@abhishek-statusline-marketplace
```

Then remove the `statusLine` entry from `settings.json` and restart.
