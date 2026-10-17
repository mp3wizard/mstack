# Principles and evidence tiers

## Evidence tiers

Design frameworks gate on evidence from real users, and an agent cannot recruit them. mstack keeps both truths with three tiers:

| Tier | Produced by | Examples | Proves usability? |
|---|---|---|---|
| 1. Inspection | The agent, now | Heuristic review, WCAG checks, computed contrast, screenshots, state coverage | No. Findings are hypotheses. |
| 2. Existing evidence | Already in the project | Past research, analytics, support tickets, recorded sessions | Partly. Cited, never extended. |
| 3. New user evidence | A human runs it | Usability rounds, interviews, card sorts, experiments | Yes. |

When tier 3 is needed, the agent prepares the study kit, adds a `pending: user evidence for <question>` item, and keeps working. Simulated or AI participants are never tier 3.

## Principles

Each principle is a one-rule skill that design-mode reads in full before applying it, then cites in its reply with the heuristic, law, or criterion behind it. There are 22, in seven groups:

- **Framing.** frame-the-problem, user-outcome-first, riskiest-assumption-first, diverge-then-converge, as-little-design-as-possible.
- **Structure.** model-the-objects, design-every-state, minimize-cognitive-load.
- **Interaction.** signify-and-give-feedback, follow-conventions, design-for-error-and-reversal.
- **Inclusion and ethics.** accessible-by-default, honest-design.
- **Systems.** encode-decisions-in-the-system, deprecate-through-a-lifecycle.
- **Evidence.** prove-it-with-evidence, never-fabricate-user-evidence, observe-behavior-over-opinion, explain-the-metric, cite-the-law-in-scope, fix-the-design-cause.
- **Delegation.** propose-and-proceed.

Each lives at `skills/principle-<name>/SKILL.md`, and the router's Principles section says when each applies.

## Steer with a name

You rarely invoke a principle. Name it in a one-line steer instead, and the agent applies the rule it already read:

```
apply design every state. show me empty, loading, and error at 375.
```

```
cite the law in scope. what did Hick's law actually measure?
```

## Laws and myths

The `design-handbook` skill holds the references: UX laws with their real scope, heuristics, WCAG 2.2, research numbers, process frameworks, design systems, ethics, AI features, and content. design-mode checks each load-bearing number or criterion against it before the reply goes out. `docs/handbook-map.md` lists the folk claims mstack corrects, and `scripts/check-plugin.py` fails when a skill repeats one.

Next: [Make it yours](09-make-it-yours.md).
