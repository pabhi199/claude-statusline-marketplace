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
    "command": "${CLAUDE_PLUGIN_ROOT}/bin/statusline.py"
  }
}
```

If `${CLAUDE_PLUGIN_ROOT}` doesn't resolve in your settings file, run `/plugin list`
to find the plugin's installed path and use the absolute path to
`bin/statusline.py` instead.

Restart Claude Code (or start a new session) to see the statusline.

## Uninstall

```
/plugin uninstall quick-statusline@abhishek-statusline-marketplace
```

Then remove the `statusLine` entry from settings.json.
