---
name: critique
description: "Multi-lens, multi-model design critique of screens, a flow, a URL, or Figma frames. Findings cite the heuristic and WCAG IDs in lenses.md, carry evidence, and get a 0-4 severity. Does not apply changes."
disable-model-invocation: true
---

# Critique

Sibling skills live at `../<name>/SKILL.md` from this file (design-mode, diverge, design-handbook, principle-<slug>). Build absolute paths from this skill's base directory.

Spawn one independent reviewer per lens to check a design against its objectives. The signal comes from separate lenses and different models, not from personas. The deliverable is a synthesized verdict. Do NOT auto-apply changes.

Every finding is an inspection hypothesis (evidence tier 1). It predicts a problem a user may hit. It does not prove one. Only user evidence does (**principle-observe-behavior-over-opinion**, **principle-never-fabricate-user-evidence**). Inspection complements testing and never replaces it.

## Step 1, Scope

Name the surface: screens, a flow, a live URL, or Figma frames. Name the viewports and the states in scope.

Capture the evidence before any reviewer runs. Reviewers judge files, not memories.

- Live UI. Drive it with the built-in browser, the Playwright MCP, or the **run** skill. Screenshot each screen at 375, 768 and 1440 px wide, plus 320 px when reflow is in scope. Save a DOM and accessibility snapshot next to each screenshot.
- Figma. Pull each frame with the Figma MCP screenshot tool. Read the Dev Mode spec for tokens and states if one exists.
- States. Capture the screen states and the interaction states in **principle-design-every-state** that the flow reaches. Tab through once and screenshot the focus path.
- Save everything to one evidence dir, `/tmp/critique-<slug>/`, with names that say screen, state and viewport.

A state you cannot reach is a gap. List it. No reviewer guesses how it looks.

## Step 2, Intent

State in one paragraph the objective the design must meet, who the users are, their primary tasks, and the constraints (platform, design system, brand, legal). Pull it from the brief, PRODUCT.md, the ticket, or discovery notes.

Critique checks the design against agreed objectives, never against taste. If objectives or users are missing, propose them from what you have, label them assumed at the top of the output, and proceed (**principle-propose-and-proceed**). A product call no artifact can answer becomes an open decision with its evidence, listed in the output. Use AskUserQuestion at most once, as the last action, and never under a session override such as "don't stop".

## Step 3, Spawn reviewers

Launch every reviewer in a single message with the Agent tool. One seat per lens in `references/lenses.md`.

| Seat | Lens | Agent | Model |
|------|------|-------|-------|
| A | Heuristics | `general-purpose` | `opus` |
| B | Accessibility | `general-purpose` | `sonnet` |
| C | Cognition and laws in scope | `general-purpose` | `opus` |
| D | Conventions and system consistency | `general-purpose` | `sonnet` |
| E | Content | `general-purpose` | `sonnet` |
| F | Ethics and deceptive patterns | `general-purpose` | `opus` |
| G | All lenses | `codex-bridge:codex-second-opinion` | its own |

Seat G is the only seat on a different model family. Opus and sonnet are one family. When the codex-bridge plugin is missing, drop seat G and say the review ran on one model family. Codex starts with no context, so pass it the full prompt as files: the evidence dir, the DOM snapshots, and all of `references/lenses.md`. Tell it to run Codex with the evidence dir as `-C`, so that directory is Codex's working directory and sandbox root.

Copy design-mode's contrast script (`../design-mode/scripts/contrast.py` from this skill's base directory) into the evidence dir, so every seat, seat G included, can reach it. Fill `references/reviewer-prompt.md` for each seat with the intent, the evidence paths, the gaps, that seat's lens section, the absolute path of that copy, and the absolute path of `../design-handbook/references/heuristics.md` for the severity scale. Pass paths, not pasted images. Tell each seat not to edit files.

If the Agent tool rejects a model, run that seat on the parent model and say so. If six seats cost too much, merge into three: heuristics with cognition, accessibility with conventions, content with ethics. Keep at least two models. Say which lenses merged.

Delegates, when installed, run as extra seats. Treat each as one more reviewer, never as the verdict.

- **impeccable:impeccable** critique scores Nielsen's ten heuristics. Its detector output is evidence, not proof. Still look at the screenshots.
- **design:design-critique** gives a second structured pass.
- **design:accessibility-review** targets WCAG 2.1 AA, and its quick reference wrongly lists 2.5.5 as AA (2.5.5 is AAA). Cite levels from WCAG 2.2 directly.

## Step 4, Synthesize

Parse every finding. Merge findings that describe the same problem in different words. Record which seats and models raised each.

- Agreement across same-family seats is corroboration, not independent confirmation. Agreement between seat G and a lens seat crosses model families and ranks highest. Report agreement only as seat counts, never as evaluator counts.
- A finding from one seat is read and weighted lower. Mark its severity single-rater.
- When several seats rated the same finding, report the spread and the mean, labeled "model-panel mean, not independent raters". Where severity decides the next step, the human designer rates it.
- Open the evidence behind every finding headed for Act on. Look at the screenshot region. Check the DOM. Recompute any contrast claim with that same script. Evidence that does not show the problem sends the finding to Dismissed.

NN/g's method uses three to five independent human evaluators, and a lone evaluator finds about 35% of problems on average. Parallel model passes are not independent evaluators. Never state a coverage percentage.

## Step 5, Lead judgment

You are the lead designer, not an aggregator. Put every finding in one bucket, with the seats that raised it and a one-line reason.

- **Act on**. A real problem against the stated objective, visible in the evidence. Severity 3 or 4, any WCAG 2.2 A or AA failure, or a deceptive pattern. It would block a ship.
- **Consider**. Legitimate, but unclear it outweighs the cost now. Worth the owner's attention.
- **Noted**. Valid and not actionable now. Cosmetic, AAA-only, or outside scope.
- **Dismissed**. Wrong, missing context, unsupported by the evidence, or taste with no user impact. Give the reason.

Filter hard. A preference that names no user impact and no ID is dismissed. A pattern the design system uses everywhere is not a defect of this screen. Raise it against the system. More than five Act on items below severity 3 means you are not filtering. Severity 3 or 4 findings, A or AA failures, and deceptive patterns always stay.

A finding that only user behavior can confirm becomes a pending gate. Name the **Usability test** (../design-mode/playbooks/usability-test.md) task that would confirm it.

## Output format

### Intent
> [The paragraph from Step 2. Mark assumed objectives.]

### Evidence
[Evidence dir path. Screens, states and viewports captured. Gaps.]

### Reviewers
- Seat [label], [lens]: [model], [N findings] (one bullet per seat)

### Act on
[Each with the problem as user impact, the ID, the evidence path and region, severity (model-panel mean with spread, or single-rater), seats that raised it.]

### Consider
[Each with the problem, the ID, the seats, and the tradeoff.]

### Noted
[Brief list.]

### Dismissed
[Each with its reason.]

### Agreement map
[Where seats and model families agreed and split, and what that says.]

### Open decisions
[Product, taste, or brand calls left to the owner, each with its evidence and your recommendation.]

### Pending gates
[Findings that need tier 3 evidence, and the test task for each. Every finding above stays a hypothesis until then.]

## Grounded in

- [Design Critiques](https://www.nngroup.com/articles/design-critiques/) (NN/g, all rights reserved), critique against agreed objectives, not taste.
- [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) (NN/g, all rights reserved), independent evaluators, then merge, and inspection never replaces testing.
- [Theory of Heuristic Evaluations](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/) (NN/g, all rights reserved), the single-evaluator 35% average and the three-to-five recommendation.
- [Severity Ratings](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) (NN/g, all rights reserved), the 0-4 scale and averaging raters.
- [design-review agent](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) (OneRedOak, MIT), live environment first, three viewports, problems over prescriptions.
- [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0), detector output is evidence, not proof.
