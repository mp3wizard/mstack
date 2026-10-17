# Route work through `/design-mode`

`/mstack:design-mode` is the router. It reads your task, picks a playbook, copies that playbook's steps into the todo list verbatim, and runs the principles and skills each step names. A step it skips stays in the list as `skip: <reason>`.

## Write the prompt

State the user need, who it is for, and how to tell it is done. Do not list skills or steps, because a hand-written order drops steps the playbook would keep. `skills/design-help/references/prompting.md` has the full advice.

```
/mstack:design-mode finance users can't find last month's failed payments on the reports page. design a fix. done means every state has a screenshot at 375 and 1280.
```

## What the router does on its own

- **Reframes a solution as a need.** "Add a filter button" becomes a user problem first (principle-frame-the-problem).
- **Answers its own empirical questions.** If a prototype, an inspection, or a measurement could settle a fork, it runs one instead of asking you. Taste, brand, product strategy, and risk acceptance stay yours. It proceeds on a labeled default and lists the call as an open decision.
- **Labels the evidence tier** on every claim about users. See [page 8](08-principles-and-evidence.md).
- **Asks Jev for a second opinion** when a task matches no playbook clearly, and keeps the last word itself.

## The playbooks

The router lists 22 playbooks in seven groups: discover and define, design and prototype, evaluate, improve, systemize, hand off and measure, and plan, pause, and resume. Naming one in your prompt picks it directly. The full list with one line each is the Playbooks section of `skills/design-mode/SKILL.md`.

When no playbook fits, the router runs **Bespoke run**, which borrows the nearest playbooks' steps and designs only the gaps.

## Autonomy

Reversible work proceeds without asking: prototypes, screenshots, critiques, drafts, study kits, local design-system branches. The agent always pauses before anything outward or irreversible: contacting users or stakeholders, publishing a shared library, deleting or overwriting design files, merging, and any legal, compliance, or accessibility sign-off.

## The reply

Every playbook ends with a reply that names each principle that changed a decision, the heuristic or criterion behind it, and the evidence for each claim. Claims about users carry their tier.

Next: [Discover and investigate](03-discover-and-investigate.md).
