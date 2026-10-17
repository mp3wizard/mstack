# Evaluate a design

Evaluation playbooks end in a report and pause before the report leaves the session.

## The critique skill

`/mstack:critique` checks a design against agreed objectives, never against taste. It spawns one reviewer per lens: heuristics, accessibility, cognition and laws in scope, conventions and consistency, content, and ethics, plus seat G on the codex-bridge agent for a different model family when installed. Findings cite heuristic or WCAG IDs, carry evidence, and get a 0 to 4 severity. It does not apply changes.

Parallel model passes are not independent evaluators, so critique reports agreement as seat counts and never states a coverage percentage.

## Heuristic review

A full inspection of an existing or proposed UI with independent lenses and severity ratings. Its output is tier 1: hypotheses, not proof of usability.

## Accessibility audit

WCAG 2.2 conformance with per-criterion evidence, defaulting to AA unless a law sets another target. It runs an automated pass and then manual passes on a structured sample. A criterion with no evidence is untested, not passed. The report is an evaluation statement scoped to the sample, not a conformance claim.

```
/mstack:design-mode audit the checkout at [url] against WCAG 2.2 AA. per-criterion evidence. report only.
```

Contrast is always computed with `scripts/contrast.py`, never eyeballed.

## Deceptive pattern audit

Consent, checkout, cancellation, and data flows checked for manipulation. design-mode runs it whenever a task touches sign-up, checkout, consent, cancellation, personal data, children, or an AI feature.

## Studies a human runs

**Usability test** and **Interview study** produce a study kit: research questions, a recruit spec, tasks, a facilitator script, consent, observer sheets, and an analysis template. A human recruits and runs the sessions. The agent never simulates a participant, a quote, a rating, or a task result. When you send back the raw data, it removes identifying details, scores SUS with `scripts/sus.py`, and synthesizes the round.

Files: `skills/critique/SKILL.md` and `skills/design-mode/playbooks/heuristic-review.md`, `accessibility-audit.md`, `deceptive-pattern-audit.md`, `usability-test.md`, `interview-study.md`.

Next: [Hand off, check the build, and measure](06-handoff-qa-measure.md).
