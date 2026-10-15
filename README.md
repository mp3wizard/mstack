# mstack

The m is for mp3wizard, the way the p in pstack is for poteto.

poteto's [pstack](https://github.com/cursor/plugins/tree/main/pstack) method, applied to the design process.

pstack makes a coding agent work like a senior engineer. It routes each task to a playbook, copies the playbook's steps into the todo list, grounds every decision in a named principle, and proves the work on the real artifact. mstack keeps that method and swaps the grounding. Its playbooks follow the design phases of the SDLC, and its principles come from design handbooks: the GOV.UK Service Manual, the Design Council's Double Diamond, ISO 9241, WCAG 2.2, Nielsen Norman Group, the W3C design-token format, and more.

## Install

From a local clone:

```bash
claude plugin marketplace add /path/to/mstack
```

```bash
claude plugin install mstack@mstack
```

## Use

Start any rigorous design task with `/design-mode`:

```
/design-mode our checkout drop-off is high on mobile. figure out why and propose a fix.
```

```
/design-mode audit the settings page against WCAG 2.2 AA and give me the evidence.
```

```
/design-mode we need a date-range filter on the reports table. design it.
```

The router picks a playbook, opens a todo list with its steps, and runs the principles and skills each step needs. The reply names each principle that changed a decision and the heuristic, law, or WCAG criterion behind it.

## How it differs from pstack

Design frameworks gate on evidence from real users, and an agent cannot recruit participants. mstack splits evidence into three tiers:

1. **Inspection.** The agent runs it now: heuristic review, WCAG checks, computed contrast, screenshots, state coverage. Findings are hypotheses.
2. **Existing evidence.** Past research and analytics already in the project. Cited, never extended.
3. **New user evidence.** A human runs the study. The agent prepares the kit and analyzes the real results.

The agent never fabricates users, quotes, or results. When tier 3 is needed, it prepares the study, marks the gap as pending, and keeps working. Taste and brand calls go to a human as an evidence pack, not as a blocking question.

## What's inside

| Part | Contents |
|---|---|
| `skills/design-mode` | The router, 19 playbooks, and two scripts (`contrast.py`, `sus.py`) |
| `skills/principle-*` | 22 design principles, each with its sources and license |
| `skills/critique` | Multi-lens adversarial design review across models |
| `skills/diverge` | N design variants, a cross-judge, and a graft into one |
| `skills/design-handbook` | Reference: UX laws with their real scope, heuristics, WCAG 2.2, research numbers, process frameworks, design systems, ethics, AI features, content |
| `agents/design-agent` | Delegate for playbook steps |
| `agents/ui-slop-sicko` | Independent hunter that sees only the rendered UI |
| `docs/handbook-map.md` | Which handbooks replace pstack's, the full mapping, license tiers, and the folk claims the plugin corrects |
| `docs/sources.md` | Every source the research used, with its license |

## Recommended companion skills

The router delegates to these when they are installed and falls back to its own steps when they are not. The commands are the ones each project's README gave during research. They were not run for this README.

| Skill | Install |
|---|---|
| Impeccable | `/plugin marketplace add pbakaus/impeccable` then `/plugin install impeccable@impeccable` |
| Anthropic design plugin | `claude plugin marketplace add anthropics/knowledge-work-plugins` then `claude plugin install design@knowledge-work-plugins` |
| Figma | `claude plugin install figma@claude-plugins-official` |
| Vercel web-design-guidelines | `npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines` |
| Accessibility Agents | `/plugin marketplace add Community-Access/accessibility-agents` then `/plugin install accessibility-agents@community-access` |
| Web Quality Skills | `/plugin marketplace add addyosmani/web-quality-skills` then `/plugin install web-quality-skills@addy-web-quality-skills` |

For pstack itself on Claude Code, [`michael-denyer/pstack-claude`](https://github.com/michael-denyer/pstack-claude) is a maintained port.

## Development

```bash
python3 scripts/check-plugin.py
```

It fails when the router and the files disagree, when a path does not resolve, when a skill cites a URL from outside the research evidence, or when a skill repeats one of the folk claims encoded in its `FOLK` list (a subset of the Corrections table in `docs/handbook-map.md`). `scripts/gen-sources.py` regenerates `docs/sources.md` from `docs/research/findings.json`.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for pstack's license and the open-licensed guidance this plugin adapts.
