### Design system refactor

**You own the visual contract. The system changes. The rendered UI does not.**

A visible change is a redesign. Name it and route it to **Feature design** (playbooks/feature-design.md). A new component is **Design system component** (playbooks/design-system-component.md).

1. Pin a visual baseline first. Capture Playwright `toHaveScreenshot` references per component, state, and viewport, all in one fixed environment, because baselines differ by browser and platform. No baseline, no refactor (**principle-prove-it-with-evidence**).
2. Audit token drift in the running app. Read the computed color, spacing, type, radius, and motion values of the rendered UI and list every value that is not a token. Most trace to a missing token or a decision nobody wrote down. Read the Figma variables and styles per references/figma.md and diff them against the code's tokens. Check Figma bindings with anthropic-skills:figma-lint-bindings if installed. With no Figma access, audit the rendered app alone (**principle-encode-decisions-in-the-system**).
3. Subtract before adding. Delete unused tokens and components and merge exact duplicates before you introduce anything new (**principle-as-little-design-as-possible**).
4. Consolidate without moving pixels. Map an off-system value to a token only when the two values match. Snapping to the nearest token changes pixels, which makes it a design decision. Record it as an open decision with both values, or route it to Feature design (**principle-propose-and-proceed**).
5. Deprecate through the lifecycle. Mark the replaced token or component deprecated (DTCG `$deprecated`, or the USWDS Deprecated status) with a removal date, migrate every usage, then delete it at zero usage (**principle-deprecate-through-a-lifecycle**).
6. Verify zero unintended pixel diff. Re-run the baseline in the same environment. Any nonzero diff fails unless a human approved that exact change. Never update the baseline to make a refactor pass (**principle-prove-it-with-evidence**).
7. Run **Design handoff** (playbooks/design-handoff.md) with the token changes, deprecations, and migration notes.

**Reply:** off-system values before and after, tokens added and removed, deprecations and their migrated usages, the diff result per component, and the open value decisions.

**Grounded in:** [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) (Apache-2.0), [DTCG Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/), [USWDS component lifecycle](https://designsystem.digital.gov/components/lifecycle/), [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), [Jeff Witters on off-system values](https://x.com/JeffWitters/status/2109729064206364748).
