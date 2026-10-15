---
name: principle-fix-the-design-cause
description: "Apply when a user error, support complaint, or usability finding is reported. Treat it as a design defect, trace it to the first broken signifier, mapping, constraint, conceptual model, or copy, and fix it there instead of adding a tooltip or help text."
disable-model-invocation: true
---

# Fix the Design Cause

A user error is a design defect until shown otherwise. The symptom is where the user went wrong. The cause is the first place the design misled them. Fix the cause.

1. **Reproduce** on the real surface with the same task, data, and viewport. If it will not fire, tighten conditions (data, viewport, input method, slow network) until it does. Without a repro, the fix is a hypothesis and step 6 cannot claim it is fixed.
2. **Classify.** A slip means the user had the right goal and the action went wrong, often through inattention, a look-alike control, or a hidden mode. A mistake means the user acted on a wrong model of the system. **principle-design-for-error-and-reversal** lists the remedies for each.
3. **Trace.** Ask why at each step until you reach a design decision, not a user trait. The usual causes are a missing or weak signifier, a mapping that does not match the effect, a missing constraint, a conceptual model the UI never conveys, or copy that says the wrong thing.
4. **Fix it there.** Change the signifier, mapping, constraint, model, or words. Not the place the error surfaced.
5. **Fix the pattern.** Find every screen with the same cause and fix them all.
6. **Verify** by re-running the same task on the same surface. Show before and after evidence at the same state and viewport.

- Help text, a tooltip, or a longer error message is not a fix. Needing to explain the interface means the interface is broken.
- A better error message is still worth writing. It is the second fix, after the cause.
- "Users should read more carefully" is never a root cause.

**Why:** Blaming the user leaves the cause in place for the next one. A patch at the symptom adds reading load and hides the evidence of what is wrong.

## Grounded in

- [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) (Don Norman 2013, all rights reserved), chapter 5 treats human error as bad design, splits slips from mistakes, and traces errors to a root cause with five whys.
- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) (NN/g, all rights reserved, use with credit and link), H5 on slips vs mistakes and H9 on errors that explain the fix (IDs per `../critique/references/lenses.md`).
- [Writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) (Crown copyright, OGL v3), an interface that needs explaining needs fixing.
- [ISO 9241-110:2020](https://www.iso.org/standard/75258.html) (ISO, all rights reserved, cite clause names only), use error robustness (ISO110-6) as an interaction principle.
