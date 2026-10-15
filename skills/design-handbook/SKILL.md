---
name: design-handbook
description: "This skill should be used when a design question needs a sourced answer, such as 'what contrast ratio does WCAG 2.2 require', 'minimum target size', 'how many users for a usability test', 'what does a SUS of 68 mean', 'is the magic number seven real', 'which Nielsen heuristic does this break', 'how severe is this', or 'is this a dark pattern'. Holds UX laws in scope, heuristics, WCAG 2.2, research numbers, frameworks, design systems, ethics, AI, and content, with corrected folk claims."
---

# Design Handbook

The reference layer under design-mode. It holds what a design decision cites. It does not decide anything.

## How to use

1. Find the reference you need in the index below. Read that one file, not all of them.
2. Check the Corrections table before you repeat any number or law from memory.
3. Cite the item, then apply it inside its scope (**principle-cite-the-law-in-scope**).
4. When the handbook lacks something, say it is a known gap. Never fill it from memory.

## Citation rule

Name the source, the item ID, and the version or date. Use the IDs in [lenses.md](../critique/references/lenses.md), the plugin's one finding-ID scheme. Examples follow.

- WCAG 2.2 SC 2.5.8 Target Size (Minimum), AA.
- H6 Recognition rather than recall (Nielsen).
- ISO110-6 Use error robustness (ISO 9241-110:2020 clause 5.6).
- Fitts's law, Shannon formulation (MacKenzie).

Link the source this handbook gives. Inspection findings name the heuristic or criterion they break and stay labeled as hypotheses until users confirm them. Rate severity on the one 0 to 4 scale in [references/heuristics.md](references/heuristics.md#severity-ratings).

## License tiers

- **A. Adapt with attribution.** OGL v3, CC BY 4.0, CC0 or US public domain, Apache-2.0, MIT (GOV.UK, Design Council, 18F, USWDS, Digital.gov). Adapt the text and keep an attribution line.
- **Carbon** (IBM, Apache-2.0 via the carbon-website repo, paraphrased). No Carbon text is adapted here. Adapting it later means shipping the Apache-2.0 license and notice.
- **B. Quote with notice, never adapt.** W3C TR (WCAG 2.2, WCAG 3 draft), WAI pages, DTCG, Inclusive Design Principles. Paraphrase, cite criterion IDs, quote only short spans with the source named.
- **C. Link and paraphrase only.** All rights reserved, unknown, or no-derivatives (NN/g, Laws of UX, Rams via Vitsoe, Norman, ISO, Apple HIG, Krug, MeasuringU, deceptive.design). Own words only. An unknown license counts as C.
- **D. NonCommercial, link only.** IDEO.org Field Guide, d.school Bootleg, Google PAIR, Mailchimp. Never blend their text into this plugin.
- Names of heuristics, criteria, and laws may be listed with credit. Their explanations may not be copied.
- Laws of UX and NN/g one-liners are the easiest to copy by accident. Rewrite them.

## Corrections

These folk claims came back contradicted or unsupported against the primary source. State the corrected form. Dated rows are as of 2026-10-15. This table and [references/accessibility.md](references/accessibility.md) are the only places that hold dated regulatory facts. Other files point here.

| Folk claim | Corrected form | Source |
|---|---|---|
| Keep menus to 7 ± 2 items (Miller). | Miller 1956 is about absolute judgment and immediate memory span. Cowan puts central working-memory capacity near 3 to 5 chunks. Menus rely on recognition, not recall, so they have no 7-item cap. | [Cowan 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/), [NN/g](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) |
| The Doherty threshold is 400 ms. | The 1982 IBM text argues for sub-second response. The 400 ms figure is a later popularization. | [Doherty and Thadhani 1982, reproduction](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html) |
| Hick's law limits menu length. | Hick 1952 measured choice reaction time with up to 10 alternatives. Menu selection can be bound by visual scan instead of choice. | [Hick 1952](https://cir.nii.ac.jp/crid/1361418518753603072), [Landauer and Nachbar 1985](https://dl.acm.org/doi/10.1145/1165385.317470) |
| More options always cause choice overload. | A meta-analysis of 63 conditions from 50 experiments found a mean effect of virtually zero, with large variance. | [Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1827647) |
| Pretty designs are more usable. | Aesthetic appeal tracks perceived ease of use more than measured ease. Polished prototypes inflate ratings. | [NN/g](https://www.nngroup.com/articles/aesthetic-usability-effect/) |
| Be liberal in what you accept (Postel) is a UX rule. | It is a networking robustness principle. RFC 9413 warns that some readings of it harm interoperability over time. | [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413.txt) |
| 5 users find 85% of problems. | 85% is an average that assumes λ ≈ 0.31 and one homogeneous group. Single 5-user samples found 55% to 99%. Full coverage needs about 15 users. | [Nielsen and Landauer 1993](https://dl.acm.org/doi/10.1145/169059.169166), [Faulkner 2003](https://link.springer.com/article/10.3758/BF03195514), [Spool and Schroeder 2001](https://dl.acm.org/doi/10.1145/634067.634236) |
| NN/g recommends 20 users for quantitative studies. | That was the 2006 advice. The current figure is 40. | [NN/g 2006](https://www.nngroup.com/articles/quantitative-studies-how-many-users/), [NN/g 2021](https://www.nngroup.com/articles/summary-quant-sample-sizes/) |
| A SUS of 68 means 68 percent usable. | 68 is the average, about the 50th percentile. SUS scores are not percentages. | [MeasuringU](https://measuringu.com/sus/) |
| HEART means tracking all five categories. | Rodden et al. say to choose the categories explicitly, per product or feature. | [Rodden et al. 2010](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) |
| ODI opportunity = importance - satisfaction. | Opportunity = importance + max(0, importance - satisfaction). | [Strategyn](https://strategyn.com/outcome-driven-innovation/) |
| An expert review can replace usability testing. | Heuristic evaluation complements user research and cannot replace it. One evaluator finds about 35% of problems on average, so use 3 to 5. Parallel model passes are not independent evaluators. Never claim a coverage percentage. | [NN/g method](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/), [NN/g theory](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/) |
| WCAG 2.5.5 (44 × 44) is a AA criterion. | 2.5.5 Target Size (Enhanced) is AAA. WCAG 2.2 adds 2.5.8 Target Size (Minimum) at AA, 24 by 24 CSS px, with exceptions. | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) |
| APCA is the WCAG 3 contrast algorithm. | The WCAG 3 Working Draft (10 Sep 2026) leaves the contrast algorithm undetermined. Gate on WCAG 2.x ratios. APCA is an advisory column at most. | [WCAG 3.0 WD](https://www.w3.org/TR/wcag-3.0/) |
| WCAG 2.2 dates from October 2023. | The current edition is the republication of 12 Dec 2024. Cite that one. 4.1.1 Parsing is removed in 2.2. | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [What's new in 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) |
| EN 301 549 already requires WCAG 2.2 in the EU. | V4.1.1 (Sep 2026) adopts WCAG 2.2 but is not yet cited in the Official Journal. The legal reference stays V3.2.1 (WCAG 2.1 AA). | [AccessibleEU](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en) |
| Section 508 tracks current WCAG. | The Revised 508 Standards incorporate WCAG 2.0 Level A and AA. | [US Access Board](https://www.access-board.gov/ict/) |

## References

| File | Holds |
|---|---|
| [references/ux-laws.md](references/ux-laws.md) | Each Laws of UX entry with its origin, measured quantity, design use, misuse caveat, and evidence strength. |
| [references/heuristics.md](references/heuristics.md) | Nielsen's 10, ISO 9241-110:2020, Shneiderman's 8, Norman's concepts, Tognazzini, Rams, the one severity scale (0 to 4, usability and harm anchors), cognitive walkthrough. |
| [references/research-numbers.md](references/research-numbers.md) | Sample sizes, SUS, SEQ, UMUX-LITE, HEART, ODI, experiment checks, triangulation. |
| [references/accessibility.md](references/accessibility.md) | WCAG 2.2 criteria and levels, evaluation method, legal references. |
| [references/process-frameworks.md](references/process-frameworks.md) | Design-process frameworks across the SDLC. |
| [references/design-systems.md](references/design-systems.md) | Tokens, component definition of done, lifecycle and deprecation, visual regression. |
| [references/ethics-and-ai.md](references/ethics-and-ai.md) | Deceptive patterns and their regulation, AI-feature guidance. |
| [references/content.md](references/content.md) | Content design and plain language. |

## Known gaps

The research could not ground these. Say so instead of guessing.

- Zeigarnik effect replication status. Treat it as weak evidence.
- ISO 9241-11:2018 usability definition and the body of ISO 9241-210 clause 7.4.5. Paywalled, not read.
- RITE method. Not fetched.
- Forms design depth, DesignOps, and service design method libraries.
- Typography and color theory beyond tokens.
- Australian Digital Service Standard criteria.
- The FTC click-to-cancel rule's legal status. Do not cite it.
