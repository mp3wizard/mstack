# Design and prototype

## Feature design

For a new or changed flow. The order is fixed: model the objects before any screen, map the flows across them, then inventory a state matrix of every screen by state. States are the UI Stack's ideal, empty, partial, error, and loading, plus each component's interaction states. Then it diverges on the riskiest screen, converges against written criteria, designs every screen with a screenshot per matrix cell and viewport, runs critique on the whole flow, and writes the spec. It ends in Design handoff.

An empty matrix cell is a gap, not a pass. A combination that cannot happen gets `n/a: <reason>`.

## Prototype

A throwaway to settle one design decision by observing it instead of asking. It names the assumption under test and the result that would change the decision, picks the lowest fidelity that answers it, and builds the variants through the diverge skill. Prototype code never becomes production. What it shows is inspection evidence, labeled as a hypothesis, until real users try it.

```
/mstack:design-mode prototype two ways to show bulk selection in the inbox and tell me which one to build.
```

## The diverge skill

`/mstack:diverge` builds N variants in parallel, each in its own directory, with one variant required to reject the look the brief would get by default. A judge on another model scores them against a rubric by label only, picks a base, and grafts the best of the rest into it. Prototype, Feature design, and Design sprint all call it.

## Design sprint

A time-boxed sprint from mapping the problem to a prototype and a ready-to-run test kit. It needs one critical question and a named human decider. The agent never simulates the test-day interviews. It prepares the kit and records the test as a pending gate.

## Content design

Labels, questions, hints, errors, and flows of words. Any interface copy in another playbook follows its rules.

Files: `skills/design-mode/playbooks/feature-design.md`, `prototype.md`, `design-sprint.md`, `content-design.md`, and `skills/diverge/SKILL.md`.

Next: [Evaluate a design](05-evaluate.md).
