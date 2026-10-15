### Content design

**You own the words in the interface. If the copy has to explain the UI, fix the UI.**

1. Write the user need first. Name who it is, what they need to do, and why. No need, no content (**principle-user-outcome-first**).
2. Start with less. Add help text only where research or a task shows it is needed. Ask a question to establish eligibility instead of listing conditions.
3. Draft labels, questions, hints, and errors. Use design:ux-copy for draft variants if installed, and hold its output to these rules (**principle-minimize-cognitive-load**):
   - Every input has its own question, tied to it in the markup by a label or legend.
   - Key words come first. Drop filler words, and skip "please" and "thank you" by default.
   - Errors say what went wrong and how to fix it. No "sorry" and no jokes in validation errors.
   - Never point by colour, shape, size, or position ("the green button", "the menu on the left").
   - Link text makes sense read alone.
   - Sentence case. Short sentences, one idea each.
4. Run the plain-language check. Write for the named audience in their words. Spell out acronyms on each page that uses them.
5. Run the voice and tone check against the product's voice guide. If none exists, record a labeled default as an open decision. Voice stays constant. Tone fits the user's situation, so stressful or serious tasks get plain, calm copy.
6. Check that strings survive longer translations. Check right-to-left layout per the internationalization section of ../design-handbook/references/content.md. If comprehension matters, prepare a content test kit per **Usability test** (playbooks/usability-test.md) and record a pending gate.
7. Treat any hint that explains how the UI works as a design defect. Change the design here, or route it to **UX defect fix** (playbooks/ux-defect-fix.md) (**principle-fix-the-design-cause**).
8. Run **Design handoff** (playbooks/design-handoff.md).

**Reply:** the user need, the copy by screen and state, and the UI changes that replaced explanatory copy.

**Grounded in:** [GOV.UK Service Manual: Writing for user interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) (OGL v3.0, adapted), [GOV.UK: Understand content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/) (OGL v3.0), [Digital.gov plain language guides](https://digital.gov/guides/plain-language) (CC0 per the [site repository licence](https://github.com/GSA/digitalgov.gov/blob/main/LICENSE.md)), [W3C COGA](https://www.w3.org/TR/coga-usable/), [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/) (CC BY-NC 4.0, link only).
