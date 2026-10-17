# Set up mstack

## Install

The README's Install section has the two commands. Restart Claude Code afterwards so the skills and agents load.

Installing changes little on its own. Only `design-handbook` loads by itself, when you ask about a UX law, heuristic, or standard. Every other skill loads when you type it or when `/mstack:design-mode` runs it.

## Pick models (optional)

Run `/mstack:setup-mstack`. It asks for a budget, shows the model for each role, and writes `~/.mstack/models.md`. design-mode, critique, diverge, and design-reflect read that file before their own defaults. Without it, judgment work runs on `opus`, variants and kits on `sonnet`, and screenshot sweeps on `haiku`.

Roles and their meaning are in `skills/setup-mstack/SKILL.md`.

## Optional companions

These change how much mstack can do, not whether it runs:

- **A browser.** The built-in browser or the Playwright MCP lets the agent walk the live UI and screenshot every state. Without one, attach screenshots yourself.
- **Figma.** The Figma MCP or the Figma Console MCP lets it read a pasted figma.com link. Figma stays read-only unless you ask for a write. See `skills/design-mode/references/figma.md`.
- **Jev.** With `jev` on PATH and `TYPESAFE_API_KEY` set, design-mode gets a second opinion on routing and checks load-bearing claims. See `skills/design-mode/references/jev.md`.
- **codex-bridge.** Its second-opinion agent gives critique, diverge, design-log, and design-reflect a reviewer on a different model family.
- **Delegate skills** such as `impeccable`, `figma:*`, and `design:*` take the steps they fit. The table is `skills/design-mode/references/delegates.md`.

## First task

```
/mstack:design-mode audit the settings page against WCAG 2.2 AA and give me the evidence.
```

Next: [Route work through `/design-mode`](02-design-mode.md).
