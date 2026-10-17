# Word the prompt

A prompt states the user need and the check for done. The playbook supplies the steps, so a few plain sentences beat a spec.

## Put in

- **The need, not the solution.** "People can't find last month's failed payments" beats "add a filter button". design-mode reframes a solution anyway, so starting from the need saves a round.
- **Who it is for.** The users, their primary task, and the device or context they work in.
- **The done check.** It can pass or fail: "every state has a screenshot at 375 and 1280", "WCAG 2.2 AA with per-criterion evidence", "handoff package a developer can build from".
- **The proof to show.** Screenshot paths per state and viewport, computed contrast, a critique verdict, the state matrix.
- **What exists already.** A Figma link, the live URL, the design tokens or PRODUCT.md, past research, analytics. Each one saves a search and raises the evidence tier.
- **The real constraints.** The design system to stay inside, the conformance target, "don't touch production code", "read-only, don't change the design yet".

## Leave out

- **The how.** Say what to achieve and let the playbook find the way.
- **A list of skills or steps.** A hand-written order drops steps the playbook keeps. Name a skill only to override one choice, as in "use diverge with four variants".
- **Your favorite layout**, until the agent has framed the problem. A stated answer narrows the design space before it is explored.

## Ask for the right evidence

- An agent cannot recruit users. For a question only users can answer, ask for the study kit and expect a `pending: user evidence` gate, not a verdict.
- Send real study results back as raw data. The agent scores them with `sus.py` and synthesizes them. It never invents them.
- For "which of these is better", ask for a prototype or a diverge run with screenshots, then pick from the evidence.

## Follow up short

- "do it", "continue", and "keep going until done" are whole prompts once the chat holds the task.
- Start with "new task" when the subject changes.

## Before stepping away

- Say "going to bed" or "stepping away" so the agent stops asking. The Always-pause list still holds: it will not contact users, publish a library, or write to Figma without you.
- Write done as checks every iteration can run, and give `/loop` that predicate.
- Ask for a decision log with design-log, and for Pause safely if you might stop it midway.

## Steer in one line

- Restate the goal: "i asked for a heuristic review. don't redesign it yet."
- Name the principle: "apply design every state. show me empty, loading, and error."
- Ask for the tier: "label the evidence tier on every claim about users."
