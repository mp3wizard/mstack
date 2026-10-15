# UX laws with their real scope

[Laws of UX](https://lawsofux.com/) by Jon Yablonski indexes 30 entries. It is licensed CC BY-NC-ND 4.0, so this file restates each entry in our own words and goes back to the original source where the research found one. Link Laws of UX. Never paste its text.

Evidence strength uses four labels. **Strong** means a quantitative model or meta-analysis, inside its scope. **Moderate** means one founding study or a secondary reproduction. **Unchecked** means the research found no primary source. **Aphorism** means it is not an empirical claim.

## Contents

- [Fitts's law](#fittss-law)
- [Hick's law (Hick-Hyman)](#hicks-law-hick-hyman)
- [Miller's law and working-memory capacity](#millers-law-and-working-memory-capacity)
- [Doherty threshold](#doherty-threshold)
- [Aesthetic-usability effect](#aesthetic-usability-effect)
- [Choice overload](#choice-overload), near zero on average
- [Postel's law](#postels-law-the-robustness-principle), with the RFC 9413 caveat
- [Gestalt grouping](#gestalt-grouping)
- [Entries without a checked primary source](#entries-without-a-checked-primary-source)
- [Aphorisms](#aphorisms)

## Fitts's law

- **Origin.** Fitts 1954, motor control. It measures the time of a rapid aimed movement to a target of width W at distance (amplitude) A.
- **Form.** HCI uses the Shannon formulation, MT = a + b log2(A/W + 1). The constants a and b come from a least-squares regression for each device and task. Fitts's original index, log2(2A/W), fits data worse and can go negative. Throughput, in bits per second, is the measure for comparing devices.
- **Supports.** Sizing and placing pointer targets. Larger and nearer targets are faster, with logarithmic returns. Screen edges act as very large targets (Tognazzini).
- **Misuse.** It predicts movement time only, not decision or reading time. It sets no accessibility floor. That floor is WCAG 2.2 SC 2.5.8 (see accessibility.md).
- **Evidence.** Strong for pointing tasks.
- **Source.** [MacKenzie, Fitts' law (HHCI 2018)](https://www.yorku.ca/mack/hhci2018.html).

## Hick's law (Hick-Hyman)

- **Origin.** Hick 1952, choice reaction time. People responded to one of up to 10 stimuli, and information was gained at a roughly constant rate of about 5 bits per second. Hyman extended it in a separate 1953 paper. They were not a joint team.
- **Form.** t = c + k log b, for b equally likely alternatives. Practice lowers the slope k.
- **Supports.** Estimating decision time where people map clearly distinct, well-learned stimuli to assigned responses. Landauer and Nachbar fit ordered touch-menu selection as Hick-Hyman decision time plus Fitts movement time.
- **Misuse.** It is not a menu-length cap. Menu selection can be driven by visual scan-and-match, and scanning a randomly ordered list grows roughly linearly with its length. Their menus were ordered alphabetically or numerically.
- **Evidence.** Strong inside its lab scope. Weak as a menu design rule.
- **Source.** [Hick 1952](https://cir.nii.ac.jp/crid/1361418518753603072), [Landauer and Nachbar 1985](https://dl.acm.org/doi/10.1145/1165385.317470).

## Miller's law and working-memory capacity

Laws of UX also lists chunking, cognitive load, and working memory. They rest on the same evidence.

- **Origin.** Miller 1956 concerns absolute judgment and immediate memory span. Cowan 2010 separates a central working-memory store of about 3 to 5 meaningful chunks in young adults from span measures that depend on the task.
- **Supports.** When a task truly needs items held in mind (a code carried between screens, options compared across pages), keep them to a few chunks or keep them on screen.
- **Misuse.** The 7 ± 2 figure is not the current estimate (Cowan), and it never capped menus. Menus, tabs, and nav lists rely on recognition, so people scan them instead of memorizing them.
- **Evidence.** Strong for the capacity estimate. The design inference is indirect.
- **Source.** [Cowan 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/), [NN/g on short-term memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/).

## Doherty threshold

- **Origin.** Doherty and Thadhani, IBM, 1982. It measured programmer transactions per hour against system response time. At 3 s response a programmer completed about 180 transactions an hour. At 0.3 s the count was 371. Gains rose steeply once response fell below 1 s. It challenged the older view that waits up to 2 s were acceptable.
- **Supports.** Aim for sub-second response. Acknowledge input at once when work takes longer (Nielsen H1).
- **Misuse.** The 400 ms figure is a later popularization that the reproduced text does not support, so say sub-second. The data are 1982 programmer transactions, so applying them to other users is an inference.
- **Evidence.** Moderate. The research read a blog reproduction of the IBM text. The original report was not fetched.
- **Source.** [Doherty and Thadhani 1982, reproduction](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html).

## Aesthetic-usability effect

- **Origin.** Kurosu and Kashimura 1995, Hitachi Design Center. 252 participants rated 26 ATM layouts for ease of use and for appeal. Appeal correlated more strongly with perceived ease of use than with actual ease of use.
- **Supports.** Planning tests. Visual polish shapes first judgments of ease.
- **Misuse.** It does not say attractive designs are more usable. It is about perceived usability. A polished prototype can hide problems, so probe behind praise and weight observed task success over ratings.
- **Evidence.** Moderate. One founding study, summarized by NN/g.
- **Source.** [NN/g, The aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/).

## Choice overload

- **Origin.** Consumer psychology. Scheibehenne, Greifeneder and Todd 2010 pooled 63 conditions from 50 experiments (N = 5,036) on whether larger option sets hurt choosing. The mean effect was virtually zero, with large variance between studies. No sufficient conditions for the effect were found.
- **Supports.** Testing option-set size in its real context.
- **Misuse.** Fewer options are not reliably better. Do not cut options on this law alone.
- **Evidence.** Strong that the average effect is near zero. Weak as a general rule.
- **Source.** [Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1827647).

## Postel's law (the robustness principle)

- **Origin.** Internet protocol design, not human behavior. Send strictly, accept tolerantly.
- **Supports.** Accepting varied input formats (dates, phone numbers) and normalizing them, with a helpful error for what cannot be parsed.
- **Misuse.** RFC 9413 (IAB, 2023, informational) says some tolerant readings harm interoperability over time. Silent leniency can entrench bad input.
- **Evidence.** Engineering guidance, not a behavioral finding.
- **Source.** [RFC 9413, Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413.txt).

## Gestalt grouping

Laws of UX lists proximity, similarity, Prägnanz, common region, and uniform connectedness.

- **Origin.** Perceptual psychology. Wagemans et al. 2012 review 100 years of work on perceptual grouping and figure-ground.
- **Classical principles.** Proximity, similarity, common fate, good continuation, closure, symmetry, and parallelism. Prägnanz was the classical umbrella idea, kept deliberately vague. It holds that we see the simplest organization a scene can support.
- **Later additions.** Synchrony, common region, element connectedness, and uniform connectedness were described after the classical set.
- **Supports.** Grouping and separation in layout, and figure-ground for layering.
- **Misuse.** Do not present the later principles as original Gestalt laws. Check grouping on the rendered layout, not on the intent.
- **Evidence.** Strong as perception science. Layout rules drawn from it are inference.
- **Source.** [Wagemans et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/).

## Entries without a checked primary source

The research found only the Laws of UX entry for these. Origin was not researched. Use them as prompts for a critique, never as evidence.

| Entry | In our words | Evidence |
|---|---|---|
| Jakob's law | People expect a product to behave like the others they already use. | Practitioner heuristic, unchecked. |
| Tesler's law | Some complexity cannot be removed. Decide whether the system or the user carries it. | Practitioner heuristic, unchecked. |
| Mental model | People act on a simplified picture of how the system works. | Unchecked here. Norman's conceptual model is in heuristics.md. |
| Paradox of the active user | People start using software at once instead of reading instructions. | Unchecked. |
| Goal-gradient effect | Motivation rises as people sense the end is near. | Unchecked. |
| Peak-end rule | People judge a past experience mostly by its most intense moment and its ending. | Unchecked. |
| Serial position effect | Items at the start and end of a sequence are recalled best. | Unchecked. |
| Von Restorff effect | The item that differs from its neighbors is noticed and remembered. | Unchecked. |
| Zeigarnik effect | Interrupted tasks are recalled better than finished ones. | Weak. Replication status not researched. |
| Selective attention | People attend to what serves their current goal and skip the rest. | Unchecked. |
| Flow | Absorbed focus, helped by balanced challenge and immediate feedback. | Unchecked. |
| Cognitive bias | Systematic reasoning errors shape how people judge options. | Unchecked. |

## Aphorisms

These are rules of thumb, not empirical laws of design. Never cite one as evidence.

| Entry | In our words |
|---|---|
| Pareto principle | A minority of causes often produces most of the effects. |
| Parkinson's law | Work expands to fill the time it is given. |
| Occam's razor | When options perform equally, prefer the one with fewer assumptions or parts. |
