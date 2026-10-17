# mstack

The m is for mp3wizard, the way the p in pstack is for poteto.

poteto's [pstack](https://github.com/cursor/plugins/tree/main/pstack) method, applied to the design process.

pstack makes a coding agent work like a senior engineer. It routes each task to a playbook, copies the playbook's steps into the todo list, grounds every decision in a named principle, and proves the work on the real artifact. mstack keeps that method and swaps the grounding. Its playbooks follow the design phases of the SDLC, and its principles come from design handbooks: the GOV.UK Service Manual, the Design Council's Double Diamond, ISO 9241, WCAG 2.2, Nielsen Norman Group, the W3C design-token format, and more.

## Install

From GitHub. The repo is its own marketplace, so there is nothing to register.

```bash
claude plugin marketplace add mp3wizard/mstack
```

```bash
claude plugin install mstack@mstack
```

Restart Claude Code afterwards so the skills and agents load.

To work on it locally, clone the repo and add the clone as the marketplace:

```bash
claude plugin marketplace add /path/to/mstack
```

## Use

Start any rigorous design task with `/mstack:design-mode` followed by the task:

```
/mstack:design-mode our checkout drop-off is high on mobile. figure out why and propose a fix.
```

```
/mstack:design-mode audit the settings page against WCAG 2.2 AA and give me the evidence.
```

```
/mstack:design-mode we need a date-range filter on the reports table. design it.
```

The router picks a playbook, opens a todo list with its steps, and runs the principles and skills each step needs. The reply names each principle that changed a decision and the heuristic, law, or WCAG criterion behind it.

### Pick a playbook by task

| Task | Playbook |
|---|---|
| A new problem space, not sure what to build | Discovery |
| How does this page work, or why was it designed this way | Investigation |
| Design a new flow | Feature design |
| Try an idea you will throw away | Prototype |
| Inspect a UI against heuristics | Heuristic review |
| Prepare a test or interviews with real users | Usability test, Interview study |
| Check accessibility | Accessibility audit |
| Check for dark patterns | Deceptive pattern audit |
| Fix a reported UX problem | UX defect fix |
| Compare the built UI with the design | Design QA |
| Hand the design to developers | Design handoff |

The router lists all 19 playbooks. Naming one in your request works too.

### Things to know

- **No invented users.** When a task needs real users, such as a SUS score, the agent prepares the study kit for a human to run and records the gap as pending. It never makes up numbers. Send the raw answers back and it scores them.
- **Taste and brand calls.** The agent picks a labeled default, keeps working, and hands you the evidence to decide later. It does not stop to ask mid-task.
- **Other skills help when installed.** `impeccable`, `figma:*`, and `design:*` get the steps they fit. Without them the agent follows the playbook's own steps.
- **Ask for a source directly.** A question like "what contrast does WCAG 2.2 require" or "how many users is enough" is answered by the `design-handbook` skill with its source, and common myths such as 7±2 are corrected.

### Reading Figma files

Paste a figma.com link into the task. design-mode reads the file through whichever Figma server is connected, and uses both when one read needs what each holds:

- **Figma MCP** (Figma's official server) for deep reads of a few frames: screenshots, layout and styles for a spec, the variables a node uses, Code Connect, and design-system search.
- **Figma Console MCP** (through its Desktop Bridge plugin) for file-wide reads: every variable and style, annotations, comments, version history, lint and audits, FigJam boards, and the current selection.

Figma stays read-only unless you ask for a write. If neither server is connected, export the frames and attach them. The routing table is `skills/design-mode/references/figma.md`.

### Jev judgments (optional)

When the `jev` command is on PATH (it ships with the research-team plugin and needs `TYPESAFE_API_KEY`), design-mode uses TypeSafe's Jev model as a check beside its own reading in four places:

- **Routing.** `scripts/route.py` ranks the playbooks for an unclear task and names one only when it clearly leads. Close calls go back to the router.
- **Claim checks.** Each load-bearing number, WCAG criterion, or law definition is checked with `jev check` against the handbook reference before the reply goes out.
- **Critique ranking.** Long finding lists from the critique skill are ranked against the agreed objectives with `jev rank`. Nothing is dropped.
- **Source triage.** Research hits are ranked before reading, and each claim taken from a new source is checked against its text.

Jev calls send text to api.typesafe.ai, so mstack never sends links, Figma file keys, client names, or participant data. Without `jev`, these steps are skipped and the reply says so. Details are in `skills/design-mode/references/jev.md`.

### Scripts you can run yourself

```bash
python3 skills/design-mode/scripts/contrast.py "#767676" "#ffffff"
```

```bash
python3 skills/design-mode/scripts/sus.py "5,1,5,1,5,1,5,1,5,1" "4,2,4,2,4,2,4,2,4,2"
```

```bash
python3 skills/design-mode/scripts/route.py --task "why do people abandon the signup form"
```

`contrast.py` prints the WCAG contrast ratio and pass or fail for 1.4.3, 1.4.6, and 1.4.11. It accepts hex, `rgb()`, and `rgba()`. `sus.py` scores the System Usability Scale per respondent and prints the mean with a 95% interval against the 68 benchmark. `route.py` asks Jev which playbook fits a task and names one only when it clearly leads. It needs `jev` (see above). All three have a `--self-test` flag.

## How it differs from pstack

Design frameworks gate on evidence from real users, and an agent cannot recruit participants. mstack splits evidence into three tiers:

1. **Inspection.** The agent runs it now: heuristic review, WCAG checks, computed contrast, screenshots, state coverage. Findings are hypotheses.
2. **Existing evidence.** Past research and analytics already in the project. Cited, never extended.
3. **New user evidence.** A human runs the study. The agent prepares the kit and analyzes the real results.

The agent never fabricates users, quotes, or results. When tier 3 is needed, it prepares the study, marks the gap as pending, and keeps working. Taste and brand calls go to a human as an evidence pack, not as a blocking question.

## What's inside

| Part | Contents |
|---|---|
| `skills/design-mode` | The router, 19 playbooks, and three scripts (`contrast.py`, `sus.py`, `route.py`) |
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
