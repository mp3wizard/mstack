---
name: design-help
description: "Guides users through mstack: setup, starting a task with /design-mode, picking a playbook, skill, or principle for a design situation, and fixing a run that went wrong. Answers with a prompt the user can send and the file the answer came from. Type /design-help with a question."
disable-model-invocation: true
---

# Design help

Answer the user's question about mstack, hand them a prompt they can send, and point to the file the answer came from. For a help question, do not start the work. The user asked how, and a design-mode run spends real tokens on subagents and review panels, so let them send the prompt.

A message that asks for work, such as "use mstack to audit this page", is not a help question. Read the **design-mode** skill (`../design-mode/SKILL.md`) and do the work under it.

This file maps questions to the skills and guide pages that hold the answers. Those files own the details. Read the file you route to before you quote it, and trust it when it disagrees with this map. Paths are relative to this skill's directory. The same paths exist in the mstack repo on GitHub, which the user can open.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which playbook checks contrast?", goes straight to its section. If the need is still unclear, ask one AskUserQuestion with these options, then answer only the section they pick:

- Get set up
- Start a task or pick a playbook or skill
- Fix a run that went wrong
- Make mstack my own

Check the state that changes the answer, and mention it only when it does:

- No `~/.mstack/models.md` means **setup-mstack** has not run, so every role uses its default model. Mention it when the question is about cost, speed, or which models run.
- No `jev` on PATH means routing second opinions and claim checks are skipped (`../design-mode/references/jev.md`).
- No Figma MCP and no Figma Console MCP means Figma links cannot be read, so the user exports frames instead (`../design-mode/references/figma.md`).

## Get set up

1. Install the plugin and restart Claude Code. The README's Install section has the two commands.
2. Optionally run `/mstack:setup-mstack` to pick a model per role and a reasoning budget.
3. Start a real task with `/mstack:design-mode`, the task, and how to tell it is done.

Installing changes little until the user invokes a skill. Only **design-handbook** loads on its own, when a question asks about a UX law, heuristic, or standard. Every other mstack skill loads only when typed or when design-mode runs it. Guide page 1 (`../../docs/guide/01-setup.md`) has the details.

If cost is the worry, say where the tokens go: critique runs seven seats plus any installed delegates, diverge builds N variants plus a judge, and design-reflect runs four agents. A smaller budget or `haiku` for delegates in `/mstack:setup-mstack`, fewer diverge variants, or the merged three-seat critique all spend less. Save design-mode for work that needs rigor.

## Start a design task

`/mstack:design-mode` matches the task to a playbook, copies its steps into the todo list, and runs the principles and skills each step needs. A good prompt states the user need, who it is for, and how to tell it is done. It does not list skills or steps. Read `references/prompting.md` before you help word one. Guide page 2 (`../../docs/guide/02-design-mode.md`) has examples.

Say "new task" mid-chat to make design-mode match a fresh playbook. Its playbook steps already spawn `mstack:design-agent`. To get the same grounding from a subagent of your own, spawn it with `subagent_type: "mstack:design-agent"`. The bare name errors.

## Pick a playbook or skill

The default answer is `/mstack:design-mode`, which runs the others when its steps need them. Name a skill directly when the user wants more or less of something than a playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any design task with rigor | `/mstack:design-mode` (`../design-mode/SKILL.md`) |
| Have several models review a design and rate the problems | `/mstack:critique` (`../critique/SKILL.md`) |
| Explore several design variants and merge the best into one | `/mstack:diverge` (`../diverge/SKILL.md`) |
| Look up a UX law, heuristic, WCAG criterion, or research number with its real scope | `/mstack:design-handbook` (`../design-handbook/SKILL.md`) |
| Keep a decision log during a long run and audit it afterward | `/mstack:design-log` (`../design-log/SKILL.md`) |
| Turn what a session taught into edits to the mstack skills | `/mstack:design-reflect` (`../design-reflect/SKILL.md`) |
| Pick a model for each role and a reasoning budget | `/mstack:setup-mstack` (`../setup-mstack/SKILL.md`) |
| Find their way around mstack | `/mstack:design-help` |

If a skill directory next to this one is missing from the table, read its frontmatter and route by its description. The `principle-*` directories are covered below.

Close calls:

- **critique** reviews one design against its objectives. **diverge** builds several and picks one. The Heuristic review playbook is a full inspection with severity ratings, and it runs critique-style lenses itself.
- **design-handbook** answers a question about a law or standard. It does not review a design.
- **design-log** keeps the trail during the work. **design-reflect** looks back after the work and proposes skill edits.

## Playbooks and principles

Playbooks are step lists inside design-mode, not skills, so they have no slash command. Describing the task picks one, and naming it works too, as in "run a heuristic review of the settings page". The Playbooks section of `../design-mode/SKILL.md` lists every playbook and when it applies. These phrases pick the plan, pause, and resume playbooks:

- "pause safely" runs Pause safely (`../design-mode/playbooks/pause-safely.md`).
- "pick up where the last session stopped" runs Session pickup (`../design-mode/playbooks/session-pickup.md`).
- A task no playbook fits runs Bespoke run (`../design-mode/playbooks/bespoke-run.md`).

Principles are one-rule skills that design-mode reads and cites in its replies. The user rarely invokes one. They steer with the name instead, as in "apply design every state. show me the empty and error states." Guide page 8 (`../../docs/guide/08-principles-and-evidence.md`) lists them with the evidence tiers.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The reply describes screenshots instead of showing them | Ask for the screenshot paths per state and viewport. That is **principle-prove-it-with-evidence**. |
| The reply quotes users or gives a usability score nobody measured | Say "label the evidence tier". Only a human-run study is tier 3 (**principle-never-fabricate-user-evidence**). |
| The agent stopped to ask about layout or flow | Say "prototype it and let the result decide" (**principle-propose-and-proceed**). |
| A contrast claim looks eyeballed | Ask for `contrast.py` output (`../design-mode/scripts/contrast.py`). |
| A Figma link was ignored | Neither Figma server is connected. See `../design-mode/references/figma.md`, or attach exported frames. |
| A new model choice had no effect | design-mode reads `~/.mstack/models.md` once per session. Start a new chat, or ask it to re-read the file. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A long run lost the thread after a restart | Ask for Session pickup. Next time, ask for a decision log with **design-log** before stepping away. |
| A question got treated as the next step of the last task | Say "new task". |

For a run that drifts, `references/prompting.md` has one-line steers. Guide page 10 (`../../docs/guide/10-recipes-and-pitfalls.md`) has more pitfalls and the recipes.

## Make mstack my own

- `/mstack:design-reflect` after a session turns its lessons into skill edits the user approves.
- `/mstack:setup-mstack` picks the models and budget.
- Edit a skill in your clone and run `python3 ../../scripts/check-plugin.py`. It fails when the router and the files disagree or a skill repeats a known UX myth.

Guide page 9 (`../../docs/guide/09-make-it-yours.md`) covers each of these.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from `references/recipes.md` when one fits, then the path of the file it came from. Keep it short unless the user asked for the whole map.

Adapted from pstack's poteto-help skill (see NOTICE.md).
