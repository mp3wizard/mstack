---
name: principle-cite-the-law-in-scope
description: "Apply when you justify a design decision or invoke a UX law, heuristic, or standard. Name the heuristic, law, or criterion ID and version that changed the decision, state the law's original scope, and never repeat its folk form."
disable-model-invocation: true
---

# Cite the Law in Scope

Every design decision names the heuristic, law, or criterion ID that changed it, with its version. Use the IDs in `../critique/references/lenses.md`, for example H5, WCAG 2.2 SC 2.5.8 (AA), or ISO110-6. A decision with no citation is taste. Say so when it is.

Before invoking a UX law, state three things:

- its original domain (choice reaction, memory span, pointing, network protocols),
- the quantity it measured (reaction time, items held, movement time),
- the conditions (number of alternatives, stimulus type, who took part).

If your case falls outside them, the law is a metaphor. Do not present it as evidence.

Never repeat the folk form. Use the corrected one.

| Folk form | Say instead |
|---|---|
| Miller's 7±2 caps a menu | Not a menu rule. Cowan puts central working memory near 3 to 5 chunks, and menus rely on recognition. |
| The Doherty threshold is 400 ms | Aim for sub-second. The 1982 IBM text argues for sub-second response, and 400 ms is a later popularization. |
| Hick's law limits menu length | Hick 1952 measured choice reaction time with up to 10 alternatives. Menu selection can be bound by visual scanning instead. |
| More options cause choice overload | The meta-analytic mean effect is near zero with high variance. Test it in context. |
| Pretty designs are more usable | Attractiveness lifts perceived ease of use more than measured ease, and polish can mask problems in tests. |
| Postel's law as a UX rule | It comes from protocol design, and RFC 9413 warns that tolerant acceptance can harm interoperability. |
| SC 2.5.5 (44 × 44) is AA | 2.5.5 Target Size (Enhanced) is AAA. 2.5.8 Target Size (Minimum) is AA, 24 × 24 CSS px with exceptions. |
| APCA is the WCAG 3 contrast method | The WCAG 3 draft leaves the algorithm undetermined. APCA is advisory only. Gate on WCAG 2.x ratios. |

Research-number folk forms (5 users, SUS, sample sizes, HEART, ODI) are corrected in **principle-explain-the-metric**. Folk forms about WCAG edition dates and legal targets (EN 301 549, Section 508) change over time. Their current corrections live only in `../design-handbook/references/accessibility.md` and the Corrections table in `../design-handbook/SKILL.md`.

- **Normative over draft.** Gate on the pinned legal target and the current normative WCAG edition. Drafts such as the WCAG 3 Working Draft and the W3C Web Sustainability Guidelines are advisory.
- **Flag stale versions.** Move WCAG 2.1 targets to 2.2 and unversioned token files to DTCG 2025.10. When a law pins an older version, name both the legal floor and the current standard.
- **Laws of UX is an index.** Follow it to the primary source and write the scope in your own words. Never copy its one-liners.

**Why:** A cited rule can be checked. A folk rule sounds authoritative and is wrong in ways nobody notices until the design fails.

## Grounded in

- [Cowan 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/) (PMC author manuscript), [Short-term memory and web usability](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) (NN/g, all rights reserved), and [Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1827647) (Journal of Consumer Research), working-memory capacity, no 7-item menu cap, and the near-zero choice-overload effect.
- [Hick 1952](https://cir.nii.ac.jp/crid/1361418518753603072) (Quarterly Journal of Experimental Psychology) and [Landauer and Nachbar 1985](https://dl.acm.org/doi/10.1145/1165385.317470) (ACM), Hick's original measure and its scope for menus.
- [Doherty and Thadhani 1982, reproduction](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html) (© IBM, all rights reserved, reproduced with permission on Jim Elliott's blog) and [Aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/) (NN/g, all rights reserved), the sub-second argument and perceived vs measured usability.
- [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413.txt) (IETF Trust, BCP 78), the costs of the robustness principle.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WCAG 3.0 Working Draft](https://www.w3.org/TR/wcag-3.0/) (W3C Document License, cite and paraphrase), [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) (W3C Software and Document License), [EN 301 549 update](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en) (AccessibleEU), and [Section 508](https://www.access-board.gov/ict/) (US Access Board, US government work), criterion levels, draft status, and legal references.
- [Laws of UX](https://lawsofux.com/) (Jon Yablonski, CC BY-NC-ND 4.0, link only), an index of 30 laws, some stated in folk form.
