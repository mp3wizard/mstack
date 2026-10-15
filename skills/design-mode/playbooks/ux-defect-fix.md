### UX defect fix

**You own the fix and its proof. The report names a symptom. The cause is in the design.**

Use it for one reported usability problem. A metric that needs sustained work goes to **Metric hillclimb** (playbooks/metric-hillclimb.md).

1. Read the report as tier 2 evidence. Cite the ticket, recording, or analytics line. Do not stretch it into claims it does not make (**principle-never-fabricate-user-evidence**).
2. Reproduce it yourself on the real surface. Run the same task with the same data, viewport, and input method in the built-in browser, the Playwright MCP, or the **run** skill. Screenshot each step. Without a repro, tighten the conditions (data, viewport, input method, slow network) until it fires. Record what you tried and how your setup differs from the reporter's. If it still will not fire, the fix ships as a hypothesis and step 8 cannot claim it is fixed (**principle-prove-it-with-evidence**).
3. Classify the error (**principle-cite-the-law-in-scope**, H5 in ../critique/references/lenses.md). A slip is a lapse of attention. The user had the right goal and did something else. A mistake means the user's idea of how the product works is wrong, so the plan was wrong from the start. Slips point at signifiers, mapping, constraints, and defaults. Mistakes point at the conceptual model, memory burden, and copy.
4. Trace the design cause (**principle-fix-the-design-cause**). Keep asking why until you reach the first broken signifier, mapping, constraint, feedback, model, or line of copy. "User error" is never the answer.
5. When the complaint is slowness, double submits, or "nothing happened", time the response on the real surface. Aim for sub-second. Where a wait is real, show status at once, keep the control's label while it loads, and delay the spinner so it never flickers (**principle-signify-and-give-feedback**, H1).
6. Fix it at the cause. Change the signifier, mapping, constraint, feedback, or copy, and nothing the evidence does not justify. Reuse system tokens and components (**principle-as-little-design-as-possible**). Copy changes follow **Content design** (playbooks/content-design.md).
7. Search for every screen with the same cause and fix them in the same change.
8. Re-run the same task on the same surface. Attach before and after screenshots, or before and after timings for latency. Label the result tier 1. It shows the defect no longer reproduces for you, not that users now succeed (**principle-prove-it-with-evidence**).
9. If the fix needs user validation, prepare the kit per **Usability test** (playbooks/usability-test.md), add `pending: user evidence for <question>` to the todo list, and keep going (**principle-propose-and-proceed**).
10. Run **Design handoff** (playbooks/design-handoff.md).

**Reply:** what users hit and where the report came from, the error class, and the design cause. Then the fix, the sibling screens it covered, and before and after evidence from the same task. Name any pending user-evidence gate.

**Grounded in:** [Norman, The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/), [NN/g: 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [Doherty and Thadhani 1982 (reproduction)](https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html), [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) (MIT, adapted).
