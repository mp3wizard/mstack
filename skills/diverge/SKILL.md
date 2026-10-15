---
name: diverge
description: "Explore N design variants of a screen, flow, or component. Cross-judges them on another model, picks a base by rubric, and grafts the best of the rest into it."
disable-model-invocation: true
---

# Diverge

Sibling skills live at `../<name>/SKILL.md` from this file (design-mode, critique, principle-<slug>). Build absolute paths from this skill's base directory.

Open a todo list with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

Go wide first, then converge on evidence (**principle-diverge-then-converge**). The variants exist to make a design decision cheaply. They are not the build.

## Phase A, Frame

Every variant gets the same brief, so the brief is the contract.

1. State the artifact. Which screen, flow, or component, in which format (HTML page, Figma frame), at the lowest fidelity that settles the question (**principle-riskiest-assumption-first**).
2. Ground the brief. Give it the users, the primary task, real or worst-case content, and the product's design tokens or PRODUCT.md. Put the tokens before the page description. Fixed lists of AI-design tells go stale as models change, and product tokens matter more ([@tiennguyendev](https://x.com/tiennguyendev/status/2104745477308604733)).
3. Derive the rubric. Write 3 to 6 gradeable criteria tied to the objective, such as steps to finish the primary task, every screen state designed, only system tokens used, 1.4.3 contrast and 2.5.8 target size met, layout holding at 320 px. Variants see the brief, not the rubric.
4. Name the default. Without direction a model drifts to the most common look in its training data ([Anthropic](https://claude.com/resources/articles/improving-frontend-design-through-skills)). The [frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) lists five such clusters, including the uniform rounded-card SaaS kit and generic template chrome. Write one line naming the look this brief would get by default. At least one variant must reject it explicitly. The others may use it only where the brief calls for it.
5. Pick N (default 3) and give each variant a distinct direction, for example system-native, rejects the default in a named way, density-first. Three samples of one direction is not divergence.
6. Give each variant its own output dir, `/tmp/diverge-<slug>/variant-<n>/`. No two variants write to the same file.

## Phase B, Fan out

Spawn all N in a single message with the Agent tool, `subagent_type: "design-stack:design-agent"`. Each gets the absolute path of design-mode's SKILL.md (`../design-mode/SKILL.md` from this skill's base directory), the brief, its direction, its output dir, and the grounding files by path. Each returns the artifact, a screenshot of every state at each viewport, and a short rationale naming the alternatives it considered and rejected.

Mix `opus` and `sonnet` when the call is judgment-heavy. One model N times is fine when the work is generation-bound. Each variant may use **frontend-design:frontend-design** for its token plan and build, if installed.

If `design-stack:design-agent` fails to spawn, use `general-purpose` with the same prompt plus an instruction to read design-mode's SKILL.md first, and say so. If a variant produces nothing, continue with N-1 and note the dropout.

## Phase C, Cross-judge

After every variant finishes, spawn one judge on a model other than the one that built most variants. Prefer the **codex-bridge:codex-second-opinion** agent when installed, since it is a different model family. Otherwise use `general-purpose` on `opus` or `sonnet`, whichever built fewer variants.

The judge sees the rubric and the variants by label only (Variant 1, 2, 3), with no direction names. It scores each criterion per variant, cites the screenshot behind each score, and recommends a base. It must not edit files. It runs while you read.

## Phase D, Pick a base

When the variants are HTML, put them behind one switcher page (buttons or a keypress) at `/tmp/diverge-<slug>/index.html`, so you and the owner can flip between them.

Open every variant's screenshots, every state and viewport, before picking. Score each criterion yourself, then compare with the judge. Agreement confirms the base. Disagreement means a bias or an ambiguous rubric, so read both rationales before deciding.

Break ties toward the variant that needs the fewest new components and tokens (**principle-as-little-design-as-possible**, **principle-encode-decisions-in-the-system**).

A tie that only taste or brand can break becomes an open decision with an evidence pack. Include the screenshots per state and viewport, the rubric scores, and your recommendation. Continue on your recommended base and list the open decision in the final reply (**principle-propose-and-proceed**). Use AskUserQuestion at most once, as the last action, and never under a session override such as "don't stop".

## Phase E, Graft

Walk each losing variant once more for what is worth porting. Expect one or two things per variant, not most of it. Rebuild each graft by hand inside the base, in the base's tokens and patterns, so the result reads as one design. Never paste a fragment that brings its own spacing, color, or component.

If the variants converge on one shape, that is strong agreement. Note it and ship the consensus with no graft. If they diverge wildly with no clear winner, Phase A was under-specified. Reframe and re-run instead of averaging.

## Phase F, Verify

Verify the result on the rendered artifact (**principle-prove-it-with-evidence**). Screenshot every state (**principle-design-every-state**) at 375, 768, and 1440 px (the OneRedOak design-review widths), plus 320 px for reflow (WCAG 1.4.10). Re-score the rubric. Compute contrast with design-mode's script (`../design-mode/scripts/contrast.py`). Run the critique skill (`../critique/SKILL.md`) before the result ships.

If verification finds a problem, either Phase A was wrong (reframe and re-run) or a variant held the answer and the graft missed it (back to Phase E). Don't paper over it.

Which variant users prefer is a tier 3 question. The rubric and the judge are inspection. Never report that users prefer a variant. When preference matters, prepare the test kit through **Usability test** (`../design-mode/playbooks/usability-test.md`).

## Outputs

One synthesized artifact, with a short note. The note names the base and why, the default look and the variant that rejected it, the judge's verdict, and each graft with its source variant. It also lists what was rejected and why, any convergence or dropouts, open decisions, the verification screenshots by path, and the scratch dir.

## Grounded in

- [Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) (Design Council, CC BY 4.0), diverge to generate several answers, then converge by testing and dropping the ones that fail.
- [Improving frontend design through Skills](https://claude.com/resources/articles/improving-frontend-design-through-skills) (Anthropic, license unknown), why unguided output converges on one generic look.
- [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (Anthropic, Apache-2.0, paraphrased), the default clusters and reviewing a plan against them before building.
- [@tiennguyendev](https://x.com/tiennguyendev/status/2104745477308604733) (X post, community signal), tells drift and product tokens before the brief fix it.
- [emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT), several variants of one UI piece behind a switcher.
- [design-review agent](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) (OneRedOak, MIT), review at 375, 768, and 1440 px.
