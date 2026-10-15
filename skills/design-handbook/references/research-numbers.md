# Research numbers

Every number here carries its source. A number from inspection is a hypothesis. A number from users is evidence. Never invent either.

## Qualitative usability tests

- **The model.** Nielsen and Landauer 1993 fit problem discovery across 11 studies as found = N(1 - (1 - λ)^n). N counts all the problems, n the participants, and λ the chance one participant hits an average problem. The mean λ was about 0.31. [Source](https://dl.acm.org/doi/10.1145/169059.169166).
- **Where 85% comes from.** With λ = 0.31, five users find 1 - 0.69^5, about 85% on average, for one homogeneous group.
- **λ varies by product and task.** Nielsen's own Guerrilla HCI case fit λ = 0.26. [Source](https://www.nngroup.com/articles/guerrilla-hci/).
- **Open web tasks have low λ.** Spool and Schroeder found four production sites needed far more than 5 users to reach 85%, because open-ended tasks lower λ. [Source](https://dl.acm.org/doi/10.1145/634067.634236).
- **Samples vary.** Faulkner tested 60 users. Random sets of 5 found between about 55% and 99% of the problems. Add participants when a miss is costly. [Source](https://link.springer.com/article/10.3758/BF03195514).
- **Rule.** Run about 5 per round for one homogeneous group, fix, then test again. Spend a 15-user budget on 3 rounds of 5, since each redesign needs its own test. [Source](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/).
- **Full coverage.** Finding essentially all problems in one group needs about 15 users.
- **Distinct groups.** For two groups, 3 to 4 users each. For three or more groups, at least 3 each.
- **Stopping.** Track new problems per session. Stop a round when the curve flattens.

## Quantitative usability studies

- NN/g recommends 40 participants for most quantitative studies, sized for about a 15% margin of error at 95% confidence. [Source](https://www.nngroup.com/articles/summary-quant-sample-sizes/). Its 2006 advice was 20. [Source](https://www.nngroup.com/articles/quantitative-studies-how-many-users/).
- House guidance. Read a UX number against a comparison, such as an earlier version, a competitor, or a published norm.

## Card sorting

- Run 15 or more users per sort. Results from 5 users correlate about 0.75 with the eventual result. 15 users reach about 0.90. 30 users reach about 0.95, worth it only for a large, well-funded project. [Source](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/).
- Run at least 15 users per distinct user group. [Source](https://www.nngroup.com/articles/how-many-test-users/).
- A card sort is generative. Test the resulting structure with users afterwards.

## Heuristic evaluation

- Use 3 to 5 evaluators, each working alone before the findings are merged. [Source](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/).
- One evaluator found about 35% of the problems on average, across six projects. [Source](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/).
- The 3-to-5 advice comes from the same discovery model as the user-test numbers.
- Parallel model passes share training and prompts. They are not independent evaluators. Never claim a coverage percentage for them.
- Heuristic evaluation complements user testing. It never replaces it. Rate severity on the one 0 to 4 scale in [heuristics.md](heuristics.md#severity-ratings).

## System Usability Scale (SUS)

Created by John Brooke in 1986. [Source](https://measuringu.com/sus/).

- **Instrument.** 10 items on a 5-point agreement scale, alternating positive and negative.
- **Scoring.** Odd items score the answer minus 1. Even items score 5 minus the answer. Multiply the sum by 2.5 for a 0 to 100 range. [../../design-mode/scripts/sus.py](../../design-mode/scripts/sus.py) does this and prints the mean with its 95% t interval. Build its absolute path from this skill's base directory.
- **Benchmark.** The mean across about 500 studies is 68, about the 50th percentile. Above about 80.3 is roughly the top 10%. A SUS score is not a percentage. Report a percentile rank or grade.
- **Precision.** Small samples give unstable means. Report the confidence interval.
- **Not diagnostic.** SUS correlates only modestly with task performance (r about 0.24). A low score says something is wrong, not what. Pair it with observed sessions.

## Single Ease Question (SEQ)

Sauro and Dumas, CHI 2009. [Source](https://measuringu.com/evolution-of-seq/).

- One 7-point ease rating, asked right after each task.
- The average is about 5.5, the 50th percentile. Early benchmarks suggested about 5.
- An average SEQ goes with about 71% task completion.
- Ease and success are separate. Report both.

## UMUX-LITE and UX-Lite

Lewis, Utesch and Maher, CHI 2013. [Source](https://dl.acm.org/doi/10.1145/2470654.2481287).

- Two items. One asks whether the system's capabilities meet the user's needs, one asks whether it is easy to use.
- Reliability was about 0.82 to 0.83. Correlation with SUS was about 0.81.
- Apply the published regression before comparing with SUS norms such as 68.
- It suits in-product intercepts where 10 items is too many. MeasuringU's UX-Lite adapts it to 5-point items.

## HEART

Rodden, Hutchinson and Fu, CHI 2010. [Source](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/).

- **Categories.** Happiness, Engagement, Adoption, Retention, Task success.
- **Choose explicitly.** Decide which categories apply at product or feature level. Tracking all five is not required.
- **Goals, signals, metrics.** Agree the goals first, then the signals that would show success, then the metrics. Do not start from whatever is already logged.
- **Fit.** Engagement may not make sense for a tool people must use.

## ODI opportunity score

Outcome-Driven Innovation, Strategyn. [Source](https://strategyn.com/outcome-driven-innovation/).

- opportunity = importance + max(0, importance - satisfaction)
- It surfaces outcomes that are important and underserved. An outcome already satisfied beyond its importance gains nothing from the second term.

## Experiment checks

Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (2020). [Source](https://experimentguide.com/).

- **OEC.** Agree one overall evaluation criterion before launch, one that predicts long-term value. Profit is a poor OEC, because short-term moves such as raising prices can lift it now and hurt it later.
- **Sample ratio mismatch.** If the observed traffic split differs significantly from the designed split, distrust the result until the cause is found. About 6% of experiments at Microsoft showed one. [Source](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf).
- **Twyman's law.** Any figure that looks interesting or different is usually wrong. Double-check the data and run validity tests, such as an SRM check, before celebrating.
- **Guardrails.** Track guardrail metrics that protect key business goals while you move the OEC. The research did not read the book's guardrail section, so define them per experiment.
- **Base rate.** Only about one in three Microsoft ideas moved the metric it targeted. In well-optimized domains such as Bing and Google, about 10% to 20% did. Expect most changes to fail.

## Triangulation

[Source](https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/), [methods](https://www.nngroup.com/articles/which-ux-research-methods/), NN/g research-method guidance.

- Treat a finding as established only when an independent source or method agrees.
- Pair behavioral with attitudinal data, and qualitative with quantitative. SUS plus an observed task failure is one such pair.
- Pick methods on two axes. What people do versus what they say. Why and how versus how many.
