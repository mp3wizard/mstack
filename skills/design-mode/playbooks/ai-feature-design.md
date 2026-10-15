### AI feature design

**You own whether AI belongs here and how the feature behaves when the AI is wrong.**

Use it for any AI or agentic feature, including one queued by **Discovery** (playbooks/discovery.md).

1. Ask first whether AI is needed. Name the user problem, a non-AI alternative, and whether people want this task automated at all. Google's People + AI Guidebook covers this question. Link it and never adapt its text. The answer is tier 3 evidence about behavior, such as how people do the task today, their workarounds, and what they already hand off. Cite tier 2 or prepare a kit per **Interview study** (playbooks/interview-study.md). Never assume the answer.
2. If AI stays, fetch the guideline list from the HAX Toolkit first, since this plugin links it and holds no guideline text. Walk Microsoft's 18 Guidelines for Human-AI Interaction one by one in the HAX Design Library or Workbook. Record a decision or `N/A: <rationale>` for each. The guidelines fall into four phases:
   - **Initially.** Set expectations for what the system can do and how well.
   - **During interaction.** Fit the user's context and social norms. Show what matters for the task at hand.
   - **When wrong.** Make outputs quick to dismiss and correct. Explain why the system acted as it did.
   - **Over time.** Learn from behavior with care, change cautiously, and tell users what changed.
3. Specify onboarding. State capabilities and limits in plain language. Back any accuracy or quality claim with a measured number and its source (**principle-explain-the-metric**). Never overstate the model (**principle-honest-design**).
4. Specify explanation. Decide what the user sees about why an output appeared, and where.
5. Specify feedback controls. Decide how the user rates or corrects an output, and what that changes.
6. Specify graceful failure. Wrong, empty, slow, and unavailable outputs each get a designed state (**principle-design-every-state**). Fill the states with real model outputs, wrong ones included. Where none exist yet, mark the state pending real outputs. Never invent representative outputs or an accuracy figure.
7. Specify dismiss, correct, and undo for every AI output and action. An agentic action with side effects gets a confirmation before it runs and a reversal path after (**principle-design-for-error-and-reversal**, **principle-honest-design**).
8. Run the **critique** skill with the guideline record attached. Its findings are inspection hypotheses.
9. Run **Design handoff** (playbooks/design-handoff.md). Put the guideline record in the spec.

**Reply:** whether AI is needed and why, the guideline record by phase with each decision or N/A rationale, the onboarding, explanation, feedback, failure, and undo specs, pending gates, and open decisions.

**Grounded in:** [Microsoft HAX Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/), [Guidelines for Human-AI Interaction (Microsoft Research, CHI 2019)](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/), [Google PAIR People + AI Guidebook](https://pair.withgoogle.com/guidebook/).
