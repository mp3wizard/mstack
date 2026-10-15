---
name: principle-explain-the-metric
description: "Apply before you report, compare, or act on a UX number, such as a SUS or SEQ score, a success rate, a count of findings, or an experiment result. Never report it alone. Give its benchmark, interval, sample size, and method, and rule out that it measured something else."
disable-model-invocation: true
---

# Explain the Metric

A UX number reported alone means nothing. Every number carries its benchmark, its interval, its n, and how it was collected.

- **Benchmark.** Compare against a norm, a prior version, or a competitor. A SUS score of 68 is about average, near the 50th percentile across roughly 500 studies. SUS scores are not percentages. The average SEQ is about 5.5 on its 7-point scale.
- **Interval and n.** Report the confidence interval and n with every mean. Small samples give unstable means. Score SUS with `../design-mode/scripts/sus.py` (absolute path built from this skill's base directory), which prints n, the mean, and its 95% interval.
- **Size the sample to the question.**
  - Qualitative rounds take about 5 users for one homogeneous group, then iterate. With two distinct groups, use 3 to 4 each. With three or more, at least 3 each.
  - The 85% figure for 5 users is an average that assumes λ ≈ 0.31 in one homogeneous group. Single 5-user samples found 55% to 99% of problems. Never promise coverage.
  - Quantitative benchmarks take about 40 users, for roughly a 15% margin of error at 95% confidence.
  - Card sorts take about 15 users per user group.
- **Severity, not count.** Rank problems on the 0 to 4 scale defined in `../design-handbook/references/heuristics.md`, in a separate pass after the findings list exists. Average about three independent raters. Parallel model passes are not independent raters. Mark any frequency judgment "estimated, no tier 2 data" unless analytics back it. A tally of findings is not a ranking.
- **Triangulate.** Pair what people did with what they said. SUS says something is wrong, not what. SEQ ease correlates with task success but does not replace it, so report success and ease separately.
- **Name the framework's real rule.** HEART does not require all five categories, so choose them explicitly from goals to signals to metrics. An ODI opportunity score is importance + max(0, importance - satisfaction).
- **Experiments.** Agree one overall evaluation criterion before launch. Check for sample ratio mismatch before reading any result. About 6% of Microsoft experiments had one. Apply Twyman's law. A figure that looks interesting or different is usually wrong, so double-check it and run validity tests before trusting it. Most ideas fail (about a third helped at Microsoft, 10 to 20% in mature domains), so a win needs scrutiny.

**Why:** A bare number invites the wrong reading. A SUS of 68 reads like a failing grade. "5 users" reads like a guarantee. The benchmark, interval, and n make the number usable.

## Grounded in

- [SUS](https://measuringu.com/sus/) and [SEQ norms](https://measuringu.com/evolution-of-seq/) (MeasuringU, all rights reserved), SUS average and percentile, intervals, not diagnostic, SEQ average, and ease correlating with success.
- [Why you only need to test with 5 users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), [quantitative sample sizes](https://www.nngroup.com/articles/summary-quant-sample-sizes/), [card sort sizing](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/), and [how many test users](https://www.nngroup.com/articles/how-many-test-users/) (NN/g, all rights reserved), round sizes, per-group quotas, 40 for quantitative, 15 for card sorts, and 15 per user group.
- [Nielsen and Landauer 1993](https://dl.acm.org/doi/10.1145/169059.169166) (ACM) and [Faulkner 2003](https://link.springer.com/article/10.3758/BF03195514) (Springer), the discovery curve, λ as a project average, and the 55% to 99% spread.
- [Severity ratings](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) (NN/g, all rights reserved), the 0 to 4 scale and averaging raters.
- [HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) (Rodden et al., CHI 2010) and [ODI](https://strategyn.com/outcome-driven-innovation/) (Strategyn, all rights reserved), choosing categories and the opportunity formula.
- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) (Kohavi, Tang and Xu, Cambridge University Press) and [the SRM study](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf) (KDD 2019), the OEC, SRM, Twyman's law, and base rates.
