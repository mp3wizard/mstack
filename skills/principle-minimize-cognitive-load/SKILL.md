---
name: principle-minimize-cognitive-load
description: "Apply when a flow asks people to remember, re-enter, compare, or decode information. Keep the memory on the screen, not in the user's head."
disable-model-invocation: true
---

# Minimize Cognitive Load

Every item a user has to hold in mind is a chance to drop it. Put what they need on the screen, where the decision happens.

- **Recognition over recall.** Keep options, earlier answers, and the facts a step needs visible ([Nielsen H6](https://www.nngroup.com/articles/ten-usability-heuristics/)). Never make people carry information from one screen to the next.
- **Never ask twice.** Information the user already gave in the same process is filled in for them or offered for selection (WCAG 3.3.7 Redundant Entry, Level A). The exceptions are re-entry that is essential, re-entry required for security, and earlier data that is no longer valid.
- **Keep help where it was.** Help that repeats across pages stays in the same relative order (WCAG 3.2.6 Consistent Help, Level A).
- **Chunk what must be held.** When a task truly depends on memory, plan for about 3 to 5 meaningful chunks (Cowan 2010).
- **Put core content first.** Lead with the main task ([Inclusive Design Principles](https://inclusivedesignprinciples.info/)). Move secondary options behind a control that is easy to find.
- **Write plainly.** Write for the specific reader, in their words (Digital.gov plain language, Nielsen H2).
- **Remove what competes.** Cut information that pulls attention from the task (Nielsen H8). This is about relevance, not a mandate for flat style.

COGA extends this past WCAG. Its objectives include clear content, help to focus, and processes that do not rely on memory. Use it whenever the audience includes people with cognitive and learning disabilities.

**Why:** Working memory is small. Cowan puts its central capacity at about 3 to 5 meaningful items in young adults. Anything beyond that has to live on the screen.

## Misuse caveats

- Miller's 7±2 is not a menu rule. Menus work by recognition, so a longer menu needs no 7-item cap (NN/g).
- Hick's law measured choice reaction time with up to ten alternatives. Menu selection time can be driven by visual search instead, so Hick alone cannot set a menu length (Landauer and Nachbar 1985). See **principle-cite-the-law-in-scope**.
- Fewer options is not automatically better. A meta-analysis of choice overload found a mean effect near zero with high variance ([Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1827647)). Cut options for task fit, not to hit a number.
- Hiding things can backfire. Tognazzini warns that hiding complexity tends to increase it. Hide only what this task does not need, and keep it findable.

## Grounded in

- [Short-Term Memory and Web Usability](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) (NN/g, all rights reserved), recognition over memorizing, no 7-item cap.
- [The Magical Mystery Four](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/) (Nelson Cowan 2010, license unknown), the 3 to 5 chunk estimate.
- [What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) (W3C, cite and link), 3.3.7 and 3.2.6 and their levels.
- [COGA, Making Content Usable](https://www.w3.org/TR/coga-usable/) (W3C), cognitive accessibility objectives.
- [Digital.gov plain language guides](https://digital.gov/guides/plain-language) (CC0 per the [site repository license](https://github.com/GSA/digitalgov.gov/blob/main/LICENSE.md)), writing for the intended reader.
- [Landauer and Nachbar 1985](https://dl.acm.org/doi/10.1145/1165385.317470) (ACM, license unknown), the scope of Hick's law in menus.
