# Hand off, check the build, and measure

## Design handoff

Every design-producing playbook ends here. The package covers the problem and outcome, the chosen design and the rejected alternatives, objects and flows, the state matrix with a screenshot per cell, every string by screen and state, every value by token name, behaviors and motion, accessibility, instrumentation events, acceptance criteria, the evidence pack, and the pending gates and open decisions.

A raw color or spacing value in the package is a defect. Sending the package, marking Figma frames ready for dev, or publishing a library waits for a human.

## Design QA

Compares the built UI with the design, from the rendered UI and not from reading code. It screenshots every state at 1440, 768, and 375 px, diffs against the baseline, loads worst-case content, spot-checks accessibility, runs rule checks, and sends the `mstack:ui-slop-sicko` agent after generic AI tells and visual bugs. That agent sees only the URL and viewports. Every finding gets the 0 to 4 severity.

## UX defect fix

A reported usability problem to reproduce on the real surface, trace to its design cause, and fix with before and after evidence. It fixes every screen that shares the same cause in one change. The before and after screenshots are tier 1. They show the defect is gone, not that users are now happier.

## Metric hillclimb

Sustained improvement of one UX metric, one change per round, with a pre-registered experiment and a decision log of every experiment kept, reverted, or inconclusive.

## Measure

Before build, a metrics plan with HEART goals, signals, and metrics, an event spec per signal, and a benchmark. After launch, a readout with baseline, current value, interval, sample size, and benchmark, then a maturity retro that turns recurring failures into system rules.

## Design system playbooks

**Design system component** takes a new component from evidence of need to definition of done. **Design system refactor** handles token drift, consolidation, and deprecation against a pinned visual baseline.

Files: `skills/design-mode/playbooks/design-handoff.md`, `design-qa.md`, `ux-defect-fix.md`, `metric-hillclimb.md`, `measure.md`, `design-system-component.md`, `design-system-refactor.md`.

Next: [Run long work and come back to it](07-long-runs.md).
