---
name: principle-prove-it-with-evidence
description: "Apply before declaring any design, build, or fix done. Verify against the real rendered artifact, per state and viewport in a fixed environment, and treat a passing lint, detector, or AI review as necessary but not sufficient."
disable-model-invocation: true
---

# Prove It With Evidence

Verify against the real artifact. Not a description of it, not a proxy, not a tool's verdict.

- **Live environment first.** Open the running UI and drive the flow before you read code or design files.
- **Every state, every viewport.** Capture each state at each target width (for example 1440, 768, and 375 px). One happy-path screenshot proves one state.
- **Fixed environment.** Generate and compare pixel baselines in the same browser, OS, and container. Rendering differs across platforms, so a cross-environment diff is noise.
- **Diff, do not eyeball.** Prove parity with a pixel diff against a pinned baseline. Prove a number by computing it, for example contrast with `../design-mode/scripts/contrast.py`, its absolute path built from this skill's base directory.
- **Tools are necessary, not sufficient.** A clean lint, detector, Figma check, or AI review shows only that it found nothing it looks for. Inspect the rendered UI as well.
- **Match the claim to its tier.** Inspection (tier 1) can support "likely problem" or "meets SC 1.4.3". Only new user evidence (tier 3) supports "users can do this". Label the tier behind each claim.
- **Suspect the observation first.** When a check fails, rule out a wrong viewport, a stale build, a cached screenshot, or a different environment before blaming the design.
- **Keep the artifacts.** Screenshots, diff images, and script output go where a reviewer can reopen or rerun them.

**Why:** Unverified design work has unknown quality. Agents have reported finished UI as fine while text clipped on mobile and focus was invisible. Only the rendered artifact shows that.

## Grounded in

- [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) (Microsoft, Apache-2.0), baseline on first run, per-platform snapshots, and the same-environment rule.
- [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), built to spec down to the pixel and a visual-regression test on the default story.
- [OneRedOak design-review agent](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) (MIT), live environment first, three viewports, screenshot-backed findings. It pins WCAG 2.1 AA, so cite 2.2.
- [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0), its README treats a clean detector run as evidence, not proof.
- [ISO 9241-210:2019](https://www.iso.org/standard/77520.html) (ISO, all rights reserved, cite clause names only), 7.5.4 user-based testing and 7.5.5 inspection-based evaluation as separate routes.
- [@educalvolpz](https://x.com/educalvolpz/status/2110038211678355706) on X (author's copyright, link only), agents called UI finished despite clipped text and invisible focus until a separate visual-bug reviewer was added.
