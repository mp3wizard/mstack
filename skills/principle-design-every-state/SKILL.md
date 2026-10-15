---
name: principle-design-every-state
description: "Apply when specifying, building, or reviewing a screen or component. It is not designed until every data state, interaction state, worst-case content case, and breakpoint is specified."
disable-model-invocation: true
---

# Design Every State

The ideal mockup is one state out of many. The other states ship anyway, designed or not. A screen is designed when every state it can reach is specified.

Specify four sets before calling a screen done:

- **Data states.** Ideal, empty, partial, error, loading (Hurff's UI stack). Design the ideal first, then make the others lead toward it. Empty is the first-run screen, so give it a first action. Partial (one row, half a profile) still looks intentional. Error covers bad input, lost connection, missing permission, and combinations of them. Loading tells people what to expect.
- **Interaction states.** Default, hover, focus, active, selected, disabled, read-only, error, warning. Carbon's checklist requires hover, focus, selected, disabled, read-only, error, and warning in the spec, plus overflow, reflow, expansion, and scrolling behavior. W3C's designer tips add a distinct active style.
- **Worst-case content.** Long and unbreakable strings, missing fields, zero and huge counts, non-Latin scripts, right-to-left text, emoji, missing images. Fill the layout with real, representative content, the job Atomic Design gives its page stage. Label invented content per **principle-never-fabricate-user-evidence**. One artifact-level "Sample data" banner is enough, so per-item tags never distort the worst case. Render the worst case behind a toggle and screenshot it, the way the break-ui skill in emilkowalski/skills does.
- **Breakpoints.** Reflow at 320 CSS px wide with no two-dimensional scrolling is the floor (WCAG 1.4.10, AA). Screenshot each state at 1440, 768, and 375 px, the widths [OneRedOak's design-review agent](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) checks.

For right-to-left and other locales, set `dir` and `lang` on the root and mark inline changes of either. Never hard-code Western name, address, or date formats. Lay out with logical start and end instead of left and right, so the layout mirrors. That last rule is this plugin's own.

Write the matrix down. Rows are states, columns are viewports. Each cell holds a screenshot or `skip: <reason>`. An empty cell is an unspecified state, and the build will fill it with whatever default the code happens to have.

**Why:** A screen designed in only its ideal state leaves the other states to whoever writes the code, under deadline, with no spec. Hurff calls the result awkward UI. Carbon does not call a component stable until its spec covers the states.

## Misuse caveats

- Not every element has every state. A static label has no hover. Mark it `n/a` with a reason instead of inventing one.
- A state earns a cell when a user can reach it. Decorative variants are not states.

## Grounded in

- [The UI Stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/) (Scott Hurff, no open license), the five data states.
- [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), interaction states and behaviors in the spec.
- [Atomic Design, chapter 2](https://atomicdesign.bradfrost.com/chapter-2/) (Brad Frost, no open license), pages as the real-content stress test.
- [emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT), break-ui's worst-case data list.
- [W3C Internationalization quick tips](https://www.w3.org/International/quicktips/) (W3C Document License per [W3C intellectual rights](https://www.w3.org/copyright/intellectual-rights/)), language and its changes, dir=rtl on html, and local name, address, and date formats.
- [Authoring HTML, text direction](https://www.w3.org/International/techniques/authoring-html#direction) (W3C, the current page that replaces the outdated bidi techniques note), marking inline changes of direction.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (W3C Document License), 1.4.10 Reflow.
