# Design systems

Tokens, the component definition of done, contribution and lifecycle, platform targets, and visual-regression evidence. A value outside the system is drift until someone decides otherwise (**principle-encode-decisions-in-the-system**).

## Contents

- [Design tokens (DTCG 2025.10)](#design-tokens-dtcg-202510)
- [Token layers (Fluent 2)](#token-layers-fluent-2)
- [Component definition of done (Carbon)](#component-definition-of-done-carbon)
- [Contribution gate (GOV.UK Design System)](#contribution-gate-govuk-design-system)
- [Lifecycle and maturity (USWDS)](#lifecycle-and-maturity-uswds)
- [Atomic Design](#atomic-design)
- [UI stack states](#ui-stack-states)
- [Platform targets](#platform-targets)
- [Visual regression (Playwright)](#visual-regression-playwright)
- [Web Interface Guidelines (Vercel)](#web-interface-guidelines-vercel)

## Design tokens (DTCG 2025.10)

W3C Design Tokens Community Group. The spec text is under the W3C Community Final Specification Agreement, so paraphrase it and cite sections.

- **Status.** 2025.10 is the first stable version, published 28 Oct 2025. Its header reads Final Community Group Report. Its status section says it was published as a Candidate Recommendation and is considered stable. It is not a W3C Standard and not on the Standards Track. [Source](https://www.designtokens.org/tr/2025.10/format/), [announcement](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/).
- **Modules.** Format, Color (modern color spaces such as Display P3 and OKLCH), and Resolver (themes and modes without duplicate files).
- **Drafts.** An editor's draft dated 2026-09-08 exists. Pin 2025.10 until a newer stable version ships. [Source](https://www.designtokens.org/tr/drafts/format/).
- **Token.** A named JSON object with `$value`, plus optional `$type`, `$description`, `$extensions`, and `$deprecated`.
- **Groups.** Groups nest tokens, pass `$type` down, and can extend other groups. An extension cycle is an error.
- **Aliases.** Curly-brace paths reference other tokens. Tools must also support JSON Pointer references.
- **Types.** Primitives are color, dimension, fontFamily, fontWeight, duration, cubicBezier, and number. Composites are strokeStyle, border, transition, shadow, gradient, and typography.
- **Files.** Media type `application/design-tokens+json` (`application/json` is allowed). Extension `.tokens` or `.tokens.json`.
- **Tools.** Style Dictionary, Tokens Studio, and Terrazzo are reference implementations.

## Token layers (Fluent 2)

Microsoft. The site text falls under the Microsoft Terms of Use, so paraphrase. Global tokens hold raw, context-agnostic values for color, type, radius, stroke, and animation. Alias tokens sit on top, add semantic meaning, and are named by function. Fluent's tokens support light, dark, high-contrast, and branded theming. [Source](https://fluent2.microsoft.design/design-tokens). This plugin's own rule is that components consume aliases, never globals or raw values.

## Component definition of done (Carbon)

IBM Carbon component checklist (IBM, Apache-2.0 via the carbon-website repo, paraphrased). [Source](https://www.carbondesignsystem.com/getting-started/contributing/component-checklist).

- **Status ladder.** Draft, Preview candidate, Preview, Stable. Each step demands more completeness across spec, code, tests, and kit.
- **Spec tokens.** Color, type, and spacing come only from existing tokens. An untokenized value is a defect.
- **Spec states.** The interaction states in **principle-design-every-state**.
- **Spec behaviors.** Responsiveness, overflow and reflow, expansion, and scrolling.
- **Spec accessibility.** Text at 4.5:1 (disabled excepted), interactive non-text at 3:1, and a documented focus order.
- **Built to spec.** Every specified interaction works, and the build matches the spec.
- **Code.** No magic numbers, strings parameterized for i18n, works down to about 320 px, typed props, and codemods with breaking changes.
- **Tests.** Unit coverage of at least 80%. At least one Percy visual-regression test on the default story. IBM Equal Access checks on default and complex states. A manual pass with JAWS, VoiceOver, and NVDA.
- **Kit.** The Figma component follows naming and construction conventions, matches the spec, and is published to the library.
- **Carbon MCP.** Serves current Carbon docs, tokens, components, and code to agents, instead of training-data memory. [Source](https://www.carbondesignsystem.com/getting-started/carbon-mcp/overview).

## Contribution gate (GOV.UK Design System)

OGL v3.0, adaptable with attribution. A new component or pattern gets in only with evidence. The proposal brings the user need and examples in use, not a polished design or code ([propose a component or pattern](https://design-system.service.gov.uk/community/propose-a-component-or-pattern/)). [Source](https://design-system.service.gov.uk/community/contribution-criteria/).

- **Useful.** Evidence that many teams or services would use it, such as existing implementations.
- **Unique.** It does not duplicate an existing component. A replacement shows evidence it is better.
- **Usable.** Shown to work for users.
- **Consistent.** Fits the existing styles.
- **Versatile.** Works across contexts.

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Lifecycle and maturity (USWDS)

CC0 and US public domain. The design-system form of migrating callers before deleting an API (**principle-deprecate-through-a-lifecycle**). [Source](https://designsystem.digital.gov/components/lifecycle/).

1. **Proposal.** Public discussion and a formal proposal, with at least 45 days for community comment.
2. **Development.** An assigned team designs, builds, tests, and documents it. Alpha and beta releases can happen here.
3. **Released.** Public and documented. It can start as experimental (early access) and becomes stable once it passes all tests and is fully documented. A released component that fails accessibility, usability, or development requirements is flagged "use with caution" before any deprecation.
4. **Deprecated.** Still in the code base, no longer updated, and consumers are advised to remove it.

The maturity model runs from Level 1 (adopt the principles) to Level 2 (follow the UX guidance) to Level 3 (use the USWDS code, tokens and components). The five principles are start with real user needs, earn trust, embrace accessibility, promote continuity, and listen. A missing component is built from tokens and contributed back with research. [Source](https://designsystem.digital.gov/maturity-model/).

## Atomic Design

Brad Frost. Free to read, no open license, so link only. Five stages are atoms, molecules, organisms, templates, and pages. The useful split is the last one. Templates show content structure. Pages fill templates with real, representative content (long names, missing images) to see whether the system holds. [Source](https://atomicdesign.bradfrost.com/chapter-2/).

## UI stack states

Scott Hurff. No open license, so paraphrase. A screen can be in up to five states, ideal, empty, error, partial, and loading. Design the ideal first, then each other state on purpose. Error covers combined failures too. Carbon's list covers component states. The UI stack covers screen states. Spec both (**principle-design-every-state**). [Source](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/).

## Platform targets

| Platform | Source | Target | Status |
|---|---|---|---|
| Web | WCAG 2.2 SC 2.5.8 | 24 by 24 CSS px at AA, with exceptions | Normative |
| Web | WCAG 2.2 SC 2.5.5 | 44 by 44 CSS px, AAA only | Normative at AAA |
| Web | Vercel Web Interface Guidelines | Hit area at least 24 px, at least 44 px on mobile. Expand the hit area when the visual is smaller. | Guidance |
| iOS, iPadOS | Apple HIG | 44 by 44 pt default, 28 by 28 pt minimum | Checked |
| macOS | Apple HIG | 28 by 28 pt default, 20 by 20 pt minimum | As recorded, unchecked |
| tvOS | Apple HIG | 66 by 66 pt default, 56 by 56 pt minimum | As recorded, unchecked |
| visionOS | Apple HIG | 60 by 60 pt default, 28 by 28 pt minimum | As recorded, unchecked |
| watchOS | Apple HIG | 44 by 44 pt default, 28 by 28 pt minimum | As recorded, unchecked |
| Android | Material Design 3 | Touch 48 by 48 dp (about 9 mm), pointer 44 by 44 dp, about 8 dp between targets | Checked |

- Apple's terms make HIG all rights reserved and forbid scraping. Link it and paraphrase, never bundle or fetch it at runtime. [Source](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- Material 3 guideline text has no license we could find. Paraphrase it. [Source](https://m3.material.io/foundations/designing/structure).
- Check a native app against its own platform first, then WCAG.

## Visual regression (Playwright)

Apache-2.0. `toHaveScreenshot()` writes a reference image on the first run and diffs later runs against it. Snapshot names carry browser and platform, because rendering and fonts differ between them. Generate and compare baselines in the same environment (one CI container, for example), or the diffs are false. A clean diff proves parity with the baseline. It does not prove usability. [Source](https://playwright.dev/docs/test-snapshots).

## Web Interface Guidelines (Vercel)

MIT, adaptable with attribution. A living, mostly framework-agnostic ruleset in eight sections (Interactions, Animations, Layout, Content, Forms, Performance, Design, Copywriting). AGENTS.md restates it as MUST, SHOULD, and NEVER rules. command.md is a review prompt that reports by file and line. [Source](https://github.com/vercel-labs/web-interface-guidelines), [AGENTS.md](https://github.com/vercel-labs/web-interface-guidelines/blob/main/AGENTS.md).

- Full keyboard support per the APG. A visible `:focus-visible` ring that sticky UI never covers. No outline removal without a replacement.
- Mobile inputs at least 16 px, so iOS does not zoom on focus.
- Never disable zoom. The README offers a `maximum-scale` workaround, but AGENTS.md forbids it. Follow AGENTS.md.
- Honor `prefers-reduced-motion`. Animate transform and opacity. Never `transition: all`. Keep animations interruptible.
- Put state in the URL (filters, tabs, pagination, expanded panels) so share, refresh, and back work.
- Keep button labels while loading. Delay loaders and give them a minimum duration so they do not flicker. Roll back or offer undo when an optimistic update fails.
- Never block paste. Validate after typing. Show errors inline and move focus to the first one. Set the right `autocomplete`, `type`, and `inputmode`.
- Destructive actions get a confirmation or an undo window.
- Delegate to Vercel's web-design-guidelines skill if installed. It fetches the latest rules before each review. Without it, check against this list.

Adapted from Vercel Web Interface Guidelines, MIT License, Copyright (c) 2025 Vercel Labs.
