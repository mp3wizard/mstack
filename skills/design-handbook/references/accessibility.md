# Accessibility

The accessibility gate. WCAG and the WAI pages are W3C documents that allow no derivative text, so everything below is our paraphrase with criterion IDs. Read the criterion itself before ruling on a borderline case. Your checks are inspection (tier 1). Testing with disabled and assistive-technology users is tier 3.

Time-sensitive facts here (edition dates, legal references, draft status) are as of 2026-10-15. Other files point here instead of restating them.

Contents. Which edition, New in 2.2, Contrast, Target size, Other criteria the playbooks test, Legal targets, WCAG 3 is a draft, Evaluation method, Beyond the testable criteria.

## Which edition

- Cite WCAG 2.2, the W3C Recommendation republished 12 Dec 2024. It republishes the 5 Oct 2023 Recommendation, so the 2024 date is the one to cite. [Source](https://www.w3.org/TR/WCAG22/).
- 2.2 adds nine success criteria to 2.1 and removes 4.1.1 Parsing as obsolete. Never report a 4.1.1 failure against 2.2. [Source](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/).
- Content that conforms to 2.2 also conforms to 2.1 and 2.0. So 2.2 AA covers the WCAG part of every legal target below, except 4.1.1. A legal target pinned to 2.0 or 2.1 still records 4.1.1 per that edition's current W3C note.
- Default target is WCAG 2.2 AA. Add AAA criteria only when the project names them.

## New in 2.2

| SC | Name | Level | In our words |
|---|---|---|---|
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Sticky headers, cookie banners, and chat widgets never hide the whole focused item. |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | No part of the focused item is hidden by author content. |
| 2.4.13 | Focus Appearance | AAA | The focus indicator meets a minimum area and a 3:1 change of contrast. |
| 2.5.7 | Dragging Movements | AA | Every drag has a single-pointer alternative, unless dragging is essential. |
| 2.5.8 | Target Size (Minimum) | AA | Pointer targets are at least 24 by 24 CSS px, or a named exception applies. |
| 3.2.6 | Consistent Help | A | Help that repeats across pages keeps the same relative order. |
| 3.3.7 | Redundant Entry | A | Data given earlier in the same process is prefilled or offered for selection, not asked for again. Exceptions are re-entry that is essential, re-entry required for security, and earlier data that is no longer valid. |
| 3.3.8 | Accessible Authentication (Minimum) | AA | No sign-in step needs a memory, transcription, or puzzle test, unless one of four exceptions holds. An alternative method exists, a mechanism helps (paste and password managers work), the test is recognizing objects, or the test is identifying personal content the user supplied. |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | As 3.3.8, minus the object and content recognition exceptions. |

Six of the nine sit at A or AA. [Source](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/).

## Contrast

| SC | Level | Text | Large text | Covers |
|---|---|---|---|---|
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 | 3:1 | Text and images of text |
| 1.4.6 Contrast (Enhanced) | AAA | 7:1 | 4.5:1 | Text and images of text |
| 1.4.11 Non-text Contrast | AA | 3:1 | n/a | Component boundaries, state indicators, and meaningful graphics against adjacent colors |

- Large-scale text is at least 18 pt, or 14 pt bold, or the equivalent for CJK fonts.
- Inactive, decorative, and logotype text are exempt from 1.4.3 and 1.4.6.
- The ratio is (L1 + 0.05) / (L2 + 0.05), where L1 is the relative luminance of the lighter color.
- Relative luminance is L = 0.2126 R + 0.7152 G + 0.0722 B on linearized sRGB channels. Scale each channel c to 0..1. Linearize it as c / 12.92 when c ≤ 0.04045, else ((c + 0.055) / 1.055) ^ 2.4. Older copies use 0.03928 as the cutoff, which makes no practical difference.
- Run design-mode's `../../design-mode/scripts/contrast.py <fg> <bg>`, with the absolute path built from this skill's base directory. It prints the ratio and pass or fail for 1.4.3, 1.4.6, and 1.4.11. Run it on the color pair of every interaction state in principle-design-every-state.
- 1.4.1 Use of Color, A. Color is never the only carrier of meaning. Pair it with text, shape, or pattern.

[Source](https://www.w3.org/TR/WCAG22/).

## Target size

| SC | Level | Minimum | Exceptions |
|---|---|---|---|
| 2.5.8 Target Size (Minimum) | AA | 24 by 24 CSS px | Spacing, equivalent control, inline, user agent control, essential |
| 2.5.5 Target Size (Enhanced) | AAA | 44 by 44 CSS px | Equivalent control, inline, user agent control, essential |

- The spacing exception lets a smaller target pass when 24 px circles centred on each small target overlap no other target or circle. Read Understanding 2.5.8 for the geometry. [Source](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
- 2.5.5 is AAA in both 2.1 and 2.2. Some checklists list it as AA, including the quick reference in design:accessibility-review. That label is wrong. It is AAA. Take every level from WCAG itself. [Source](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html).
- Native platforms set their own sizes. See design-systems.md.

## Other criteria the playbooks test

[Source](https://www.w3.org/TR/WCAG22/).

- **1.4.10 Reflow, AA.** Content works at 320 CSS px wide without scrolling in two directions, except content that is two-dimensional by nature.
- **4.1.2 Name, Role, Value, A.** Every component exposes a programmatic name, role, and state.
- **2.2.2 Pause, Stop, Hide, A.** Two cases, both starting on their own beside other content. Moving, blinking, or scrolling content that lasts more than five seconds needs a way to pause, stop, or hide it. Auto-updating content, such as a ticker or live feed, needs a way to pause, stop, or hide it or to set its update frequency, with no time threshold. Both are exempt when the movement or update is essential.
- **2.3.3 Animation from Interactions, AAA.** Covers motion the user's own action triggers. Honor `prefers-reduced-motion` (technique C39) by default even when the target is AA. It is cheap and spares people with vestibular disorders. [Source](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).

## Legal targets

| Where | Instrument | WCAG reference today | Notes |
|---|---|---|---|
| EU, products and consumer services | European Accessibility Act, Directive (EU) 2019/882 | EN 301 549 V3.2.1, which applies WCAG 2.1 AA | Covers listed products placed on the market and consumer services provided after 28 June 2025. Microenterprises providing services are exempt. |
| EU, public sector | Web Accessibility Directive | EN 301 549 V3.2.1 (WCAG 2.1 AA) | Same legal reference as the EAA. |
| EU, next | EN 301 549 V4.1.1 (Sep 2026) | WCAG 2.2 | Published, not yet cited in the Official Journal, so not yet the legal reference. Drops 4.1.1. Adds a clause map to the EAA. |
| US federal | Revised Section 508 Standards (36 CFR Part 1194) | WCAG 2.0 A and AA, incorporated by reference | Non-web documents and software are exempt from 2.4.1, 2.4.5, 3.2.3, and 3.2.4. Adds functional performance criteria. |
| UK public sector | GOV.UK Service Manual | WCAG 2.2 AA as a minimum | Also requires working with common assistive technologies, disabled people in research, an audit before public beta, and a published accessibility statement. GOV.UK says meeting this also meets the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018. |

- Each instrument adds requirements beyond WCAG (functional performance, hardware, statements). List them separately from the WCAG results.
- Name the instrument and its version. The legal verdict belongs to counsel (**principle-cite-the-law-in-scope**).
- The UK row contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Sources. [EAA](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng), [AccessibleEU on EN 301 549 V4.1.1](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en), [EN 301 549 V4.1.1](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf), [US Access Board](https://www.access-board.gov/ict/), [GOV.UK, Making your service accessible](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction).

## WCAG 3 is a draft

- WCAG 3.0 is a W3C Working Draft dated 10 Sep 2026, not a Recommendation. [Source](https://www.w3.org/TR/wcag-3.0/).
- W3C expects it to take a few more years. WCAG 3 is not meant to replace WCAG 2, and W3C does not plan to deprecate WCAG 2 until several years after WCAG 3 becomes final. [Source](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/).
- The draft leaves its contrast algorithm undetermined. APCA is not the WCAG 3 algorithm. Gate on the WCAG 2.x ratios above and show APCA as an advisory column at most.
- APCA's reference code is all rights reserved and its name is a restricted trademark. Never vendor it. [Source](https://github.com/Myndex/SAPC-APCA).
- Use the draft for direction only. Never fail a design against it.

## Evaluation method

**WCAG-EM 2.** Published 23 Jul 2026. Unlike version 1 it covers apps and other digital products, not only websites. [Source](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/).

1. Define the scope. What is in, the goal, and the target level.
2. Explore the product. Key views, functions, content types, and the technologies relied on.
3. Select a representative sample. Mix a structured sample with random views when testing everything is not feasible.
4. Evaluate the sample. Pass or fail per criterion, with the steps taken.
5. Report. Aggregate the results into evaluation statements.

**ACT Rules.** Shared test rules that map WCAG 2.2 and ARIA requirements to applicability, expectations, and test cases. A working group either approved a rule or it is still proposed. ACT rules are informative and not required for conformance. This plugin treats a hit from an approved rule as a failure (house policy). A hit from a proposed or unmapped rule needs manual confirmation. A confirmed failure of an in-scope criterion blocks whatever its ACT status. Cite the tool's rule ID behind each automated finding, plus the ACT rule ID when one maps. [Source](https://www.w3.org/WAI/standards-guidelines/act/rules/).

**axe-core.** Deque's open-source rules engine, MPL-2.0. Use it for the automated slice through Playwright MCP or the built-in browser. Its README says it finds on average 57% of WCAG issues automatically and marks uncertain results incomplete for manual review. Alt-text quality, focus-order sense, and cognitive load stay manual checks. [Source](https://github.com/dequelabs/axe-core). GOV.UK asks for automated, manual, and assistive-technology testing together, because automation alone misses issues ([GOV.UK, Testing for accessibility](https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility)).

**ARIA Authoring Practices Guide (APG).** Keyboard and role, state, and property models for about 30 widget patterns (accordion, combobox, dialog, menu, tabs, tree, grid, and more). Declaring a role commits you to that widget's full keyboard and state behavior. Wrong ARIA misleads assistive-technology users more than missing ARIA does. So use the native HTML element first, and check every custom widget against its APG pattern. [Source](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), [patterns](https://www.w3.org/WAI/ARIA/apg/).

**Designer first pass.** WAI's designing tips cover what a designer owns before code exists. Contrast, color never alone, identifiable controls with visible focus, consistent navigation, visible labels next to fields, noticeable feedback, headings and spacing, and planned media alternatives. [Source](https://www.w3.org/WAI/tips/designing/).

## Beyond the testable criteria

**COGA.** *Making Content Usable for People with Cognitive and Learning Disabilities* goes past WCAG's testable criteria with user stories, personas, and patterns. [Source](https://www.w3.org/TR/coga-usable/). WCAG 2.2 added cognitive-focused criteria such as 3.2.6 Consistent Help, 3.3.7 Redundant Entry, and 3.3.8 Accessible Authentication ([What's new in 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)). Its eight objectives, by name, follow.

1. Help users understand what things are and how to use them.
2. Help users find what they need.
3. Use clear and understandable content.
4. Help users avoid mistakes and know how to correct them.
5. Help users focus.
6. Ensure processes do not rely on memory.
7. Provide help and support.
8. Support adaptation and personalization.

**W3C Accessibility Maturity Model.** A Group Note since 4 Nov 2025. It rates an organization, not a product, so use it in the **Measure** maturity retro (../../design-mode/playbooks/measure.md). Seven dimensions are Communications, Oversight and Culture, ICT Development Life Cycle, Knowledge and Skills, Personnel, Procurement, and Support. Each moves through Inactive, Launch, Integrate, and Optimize, and every level claim needs proof points. [Source](https://www.w3.org/TR/maturity-model/).
