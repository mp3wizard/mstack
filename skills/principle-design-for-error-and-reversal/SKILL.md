---
name: principle-design-for-error-and-reversal
description: "Apply when designing input, validation, destructive actions, or any flow where people can go wrong. Make errors hard to make, easy to understand, and cheap to reverse."
disable-model-invocation: true
---

# Design for Error and Reversal

People will make errors. Design so the error is hard to make, plain when it happens, and cheap to undo.

- **Prevent first.** Remove the conditions that cause errors before writing a message for them (Nielsen H5, Shneiderman rule 5). Constrain input to valid values and choose defaults that are safe and easy to replace (Tognazzini).
- **Fix the kind of error you have.** Slips and mistakes need different fixes (NN/g on H5, Norman ch. 5). An inattentive slip is blocked by a constraint. A mistake follows a wrong mental model, so change what the screen tells people about how the system works.
- **Say what happened and how to fix it.** Name the cause in the user's words, put the message next to what failed, and give the next step (Nielsen H9). No apologies and no jokes in validation errors (GOV.UK).
- **Prefer undo to a confirmation dialog.** Undo at a sensible granularity lets people explore without fear (Shneiderman rule 6, Nielsen H3). Keep confirmation for actions that truly cannot be reversed, and name the consequence in it.
- **Give every destructive action a way back.** Delete goes to a recoverable state first. An optimistic update that fails rolls back visibly or offers undo ([Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines)).
- **Never lose the user's work.** Save as they go and restore state after a failure (Tognazzini).
- **Accept varied formats, never guess.** Take a card number with spaces or a pasted phone number with dashes. When input has two plausible readings, ask with a specific error instead of picking one. RFC 9413 records that silent leniency entrenches bad input over time.
- **Getting out is as easy as getting in.** Cancel, unsubscribe, and account deletion follow **principle-honest-design**.

**Why:** Norman treats "human error" as a symptom of design and traces it to a root cause instead of blaming the user. ISO 9241-110 makes use error robustness (avoid, tolerate, recover) one of its seven interaction principles. A flow that blames the user for a predictable slip has a design defect. Find it with **principle-fix-the-design-cause**.

## Misuse caveats

- Undo does not replace a confirmation where reversal is impossible, such as a payment sent or a message delivered.
- Postel's robustness principle comes from network protocols. Cite it for input handling only with the RFC 9413 caveat (**principle-cite-the-law-in-scope**).

## Grounded in

- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) (NN/g, all rights reserved, use with credit and link), H3, H5, H9 and slips vs mistakes.
- [Eight Golden Rules](https://www.cs.umd.edu/users/ben/goldenrules.html) (Ben Shneiderman, license unknown), rules 5 and 6.
- [First Principles of Interaction Design](https://asktog.com/atc/principles-of-interaction-design/) (Bruce Tognazzini, personal-use copies only), defaults and protecting work.
- [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) (Don Norman, all rights reserved), error as a design root cause.
- [GOV.UK writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) (Crown copyright, OGL v3), error message tone.
- [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413.txt) (IETF Trust, BCP 78), the costs of tolerant acceptance.
