### Measure

**You own the definition of success and an honest readout of it.**

Before build it produces a metrics plan. After launch it produces a readout and a retro. Define success up front and publish the data, as GOV.UK Service Standard point 10 asks.

1. Before build. Write goals, then signals, then metrics, with HEART. Choose the categories that serve the goal and say why the rest are out, since HEART does not ask for all five. Add the GOV.UK service measures that apply: digital take-up, user satisfaction, completion rate, cost per transaction (**principle-user-outcome-first**, **principle-explain-the-metric**).
2. Before build. Write the event spec per signal (name, properties, trigger) for the handoff. Verify that each event fires on staging before launch. A metric with no firing event is a gap in the plan (**principle-prove-it-with-evidence**).
3. Before build. Set the benchmark. Read a UX number against a comparison, such as an earlier version, a competitor, or a published norm. Score SUS with `scripts/sus.py`. Its average of 68 sits near the 50th percentile, and the score is not a percentage. A quantitative benchmark needs about 40 participants. Write the kit per **Usability test** (playbooks/usability-test.md). A human runs it (**principle-never-fabricate-user-evidence**).
4. After launch. Read out each metric with baseline, current value, interval, sample size, and benchmark. Check the instrumentation before you believe a surprise (**principle-explain-the-metric**).
5. After launch. Propose retiring what users no longer use. GOV.UK retires a service that users no longer need. Applying that to a single feature is our inference, so say so. Removal is a human call, so record it as an open decision (**principle-as-little-design-as-possible**, **principle-deprecate-through-a-lifecycle**).
6. After launch. Run a maturity retro. List the failures that recurred across this work and earlier evidence packs. Turn each into a system rule, such as a token, a component, a lint, or a checklist item (**principle-encode-decisions-in-the-system**). Place the team on the NN/g UX maturity stages and the W3C Accessibility Maturity Model only with proof points. Write "unknown" where none exist.
7. Write the metrics plan or the readout as a report. Pause before sharing the report outside the session (see Autonomy in the router).

**Reply:** before build, the HEART table (goal, signal, metric, benchmark) and the event spec with its staging status. After launch, each metric with its interval and benchmark, the features proposed for retirement as open decisions, and each recurring failure with the system rule that now prevents it.

**Grounded in:** [Rodden, Hutchinson and Fu: HEART (CHI 2010)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/), [GOV.UK Service Standard](https://www.gov.uk/service-manual/service-standard) (OGL v3.0, adapted), [MeasuringU: SUS](https://measuringu.com/sus/), [NN/g: Quantitative sample sizes](https://www.nngroup.com/articles/summary-quant-sample-sizes/), [NN/g: The 6 levels of UX maturity](https://www.nngroup.com/articles/ux-maturity-model/), [W3C Accessibility Maturity Model](https://www.w3.org/TR/maturity-model/).
