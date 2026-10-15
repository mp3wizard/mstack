### Accessibility audit

**You own the conformance evidence. Automation alone never ships (principle-accessible-by-default).**

Steps follow the five WCAG-EM 2 steps (scope, explore, sample, evaluate, report). Your checks are tier 1. Testing with disabled and assistive-technology users is tier 3.

1. Scope. Pin the standard and level. Default to WCAG 2.2 AA. If a law sets the target, name the instrument and its version (**principle-cite-the-law-in-scope**). Gate on the pinned legal target and the current WCAG edition. Their current status lives in the handbook's accessibility reference (../design-handbook/references/accessibility.md). Laws add requirements beyond WCAG, so list those separately. Skip 4.1.1 Parsing when the target is WCAG 2.2. When the legal target pins 2.0 or 2.1, record 4.1.1 per that edition's current W3C note.
2. Explore and sample. List the key views, flows, components, and states. Pick a structured sample and add a few random views.
3. Run the automated pass on every sampled view and state. Delegate it to Community-Access accessibility-agents (not installed by default, and it adds an edit-gate hook, so read it first) or design:accessibility-review, if installed. That skill's quick reference lists 2.5.5 as AA, but 2.5.5 Target Size (Enhanced) is AAA, so take every level from WCAG 2.2 itself. Without either, run axe-core through Playwright MCP or the built-in browser. Cite the tool's rule ID, plus the ACT rule ID when one maps. ACT rules are informative, and W3C marks each one approved or proposed. This playbook treats a hit from an approved rule as a failure. A hit from a proposed or unmapped rule needs manual confirmation. A confirmed failure of an in-scope criterion blocks whatever its ACT status.
4. Run the manual passes on the same sample, each with a screenshot, DOM excerpt, or recording. This list is the minimum. Step 5 covers every AA criterion.
   - Keyboard only. Every control is reachable and operable, focus order follows meaning, focus stays visible. 2.1.2 No Keyboard Trap holds everywhere.
   - 2.4.11 Focus Not Obscured (Minimum). No focused item is fully hidden by sticky headers, banners, or chat widgets.
   - 2.5.8 Target Size (Minimum). Pointer targets are at least 24 by 24 CSS px, or a named exception applies (spacing, equivalent, inline, user agent, essential).
   - 2.5.7 Dragging Movements. Every drag has a single-pointer alternative unless dragging is essential.
   - 1.4.10 Reflow. Content works at 320 CSS px wide without two-dimensional scrolling.
   - 1.4.4 Resize Text. Text zoomed to 200% loses no content or function.
   - 1.4.12 Text Spacing. Overriding line, paragraph, letter, and word spacing loses no content.
   - 1.4.13 Content on Hover or Focus. Tooltips and popovers are dismissible, hoverable, and persistent.
   - 3.3.7 Redundant Entry and 3.3.8 Accessible Authentication (Minimum). Check every multi-step form and every sign-in, with the exceptions in the handbook reference.
   - Contrast. Run `scripts/contrast.py <fg> <bg>` on every text and UI color pair (1.4.3 text 4.5:1, large text 3:1, 1.4.11 non-text 3:1). APCA may appear as an advisory column only.
   - Accessibility tree (4.1.2). Every control exposes name, role, and value. Check custom widgets against the matching APG pattern. Prefer native HTML to ARIA. A real screen-reader pass is a human step. Record it as `pending: user evidence for <question>`.
5. Evaluate. Record pass, fail, or not applicable per success criterion in scope, with the evidence path. A criterion with no evidence is untested, not passed (**principle-prove-it-with-evidence**).
6. Report. Findings by criterion with level, evidence, and fix, then a WCAG-EM 2 evaluation statement scoped to the sample. It is not a conformance claim. Mark it draft, pending human sign-off. Send what needs assistive-technology users to a **Usability test** (playbooks/usability-test.md).
7. Pause before sharing the report outside the session (see Autonomy in the router).

**Reply:** the target and why, the sample, failures by criterion with level and evidence, automated vs manual split, untested criteria, the draft evaluation statement, and what still needs disabled users.

**Grounded in:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [What's new in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [WCAG-EM 2](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/), [ACT Rules](https://www.w3.org/WAI/standards-guidelines/act/rules/), [GOV.UK: Making your service accessible](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction) (OGL v3.0).
