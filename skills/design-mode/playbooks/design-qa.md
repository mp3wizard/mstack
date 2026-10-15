### Design QA

**You own the verdict on the built UI. The design is the spec. The verdict comes from the rendered UI, not from reading code.**

1. Load the spec. Use the handoff package, or the Figma frames marked ready for dev through figma:figma-spec if installed. Its state matrix and acceptance criteria are your checklist (**principle-design-every-state**).
2. Open the running UI in the built-in browser, the Playwright MCP, or the **run** skill. Walk the main flow before reading any code, and read the console (**principle-prove-it-with-evidence**).
3. Screenshot every state at 1440, 768, and 375 px wide (**principle-design-every-state**).
4. Diff each screenshot (**principle-prove-it-with-evidence**). Against a Playwright `toHaveScreenshot` baseline captured in the same environment, any nonzero diff fails. Against Figma the renderers differ, so compare measured properties (computed tokens, spacing, sizes, type) and a side-by-side overlay with a stated tolerance. Never update a baseline to pass.
5. Load worst-case content. Long strings, many items, missing images, the empty, partial, error, and loading states, and reflow at 320 CSS px (SC 1.4.10) (**principle-design-every-state**).
6. Spot-check accessibility (**principle-accessible-by-default**). Tab through the flow and confirm focus is never fully hidden (SC 2.4.11, AA). Compute contrast with `scripts/contrast.py` (SC 1.4.3, 1.4.11). Confirm targets reach 24 by 24 CSS px or meet an exception (SC 2.5.8, AA), and that reduced motion is honored. Full conformance is **Accessibility audit** (playbooks/accessibility-audit.md).
7. Run the rule checks (**principle-follow-conventions**). Use Vercel web-design-guidelines for file and line findings if installed, or impeccable:impeccable audit if installed. A clean detector run is evidence, not proof. With neither, check keyboard, focus, targets, forms, and motion against the Vercel guidelines yourself.
8. Spawn an Agent with `subagent_type: "design-stack:ui-slop-sicko"` and give it only the URL and the viewports. It hunts generic AI tells and visual bugs on its own. Confirm each of its findings on a screenshot yourself (**principle-prove-it-with-evidence**).
9. Triage every finding on the 0 to 4 scale in ../design-handbook/references/heuristics.md, labeled Blocker (4), High (3), Medium (2), or Nit (1), each with a screenshot. Write the problem and its impact on the user, not the CSS fix (**principle-user-outcome-first**).
10. Write the QA report in the project. Pause before sharing the report outside the session (see Autonomy in the router).

**Reply:** pass or fail, the report path, the diff result per state and viewport, findings by triage with screenshots, the accessibility spot checks, and what you did not check.

**Grounded in:** [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) (Apache-2.0), [OneRedOak design-review](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) (MIT, adapted to WCAG 2.2), [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines), [Carbon component checklist](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist) (IBM, Apache-2.0 via the carbon-website repo, paraphrased), [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
