# Content

Interface copy, content design, plain language, voice and tone, charts, and internationalization. If the copy has to explain the interface, fix the interface (**principle-fix-the-design-cause**). Whether real users understand the words is tier 3 evidence. Prepare the content test and let a human run it.

## Writing for user interfaces (GOV.UK)

OGL v3.0, adapted here with attribution. [Source](https://www.gov.uk/service-manual/design/writing-for-user-interfaces).

- **Clarity first.** Use your users' words to cut cognitive load. Specialists prefer clear language too. Name the service in users' terms so they can find it and know what it does.
- **Start with less.** People scan, more so in a transactional service. Add help text only where research shows a need. Ask questions to establish eligibility instead of listing conditions up front.
- **Fix the interface.** Needing to explain how the interface works means the interface is wrong.
- **Short and direct.** Short sentences, one idea each. Important words first. Write "Total cost", not "This is the total cost". Write "Wrong password", not "You have entered the wrong password". Drop "now" unless the user really chooses between now and later.
- **Tone.** Approachable and helpful, not overly familiar. Say sorry only when something serious breaks, such as the whole service. Never say sorry in validation errors. "Please", "please note", and "thank you" are usually unneeded. No jokes in errors, because people often use these services under stress. Copy nobody notices is usually doing its job.
- **Exclude no one.** Never rely on shape, size, colour, or location alone ("click the green button", "the menu on the left"). Link text makes sense read alone, so "click here" fails.
- **Structure.** Headings describe the text that follows and are not part of it. One `h1` per page, saying what the page does. The `title` is based on the `h1`.
- **Inputs.** Every field has its own question tied to it in the markup, by a label or a visually hidden legend.
- **Pronouns.** The service is "we" and the user is "you". When the user speaks, use "I", "me", and "my". Use "they" instead of "he or she".
- **Style.** Sentence case except proper nouns. Headings and labels carry no full stop. Other copy is full sentences. Simple contractions such as "you're" are fine. Avoid negative contractions such as "can't" and forms like "should've", which some people misread. Write "for example", not "eg" or "ie". Spell acronyms out on every page that uses them.
- **URLs and legal text.** URLs are readable and never carry personal data such as a name or date of birth, so it stays out of analytics. Privacy notices and declarations are as plain as everything else.

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Content design (GOV.UK)

OGL v3.0. The method that coined the term. Write the user need before any content. Then choose the amount, format, and place that meet it most simply. That can mean publishing less, splitting a page, changing format, removing duplicates, or publishing somewhere else. Content stays current, or is kept on purpose as a record. [Source](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/).

Contains public sector information licensed under the Open Government Licence v3.0.

## Plain language (Digital.gov)

CC0 and US public domain (per the [site repository licence](https://github.com/GSA/digitalgov.gov/blob/main/LICENSE.md)). The federal plain-language guides that carried forward plainlanguage.gov content. Four guides cover the principles, writing for understanding, design for understanding, and testing for understanding. The Plain Writing Act of 2010 requires public content to be written for its specific audience. [Source](https://digital.gov/guides/plain-language).

- **Missing guidelines.** The Digital.gov guides are not the Federal Plain Language Guidelines. Those vanished when plainlanguage.gov came down, and the old link now lands on Digital.gov. The Center for Plain Language reposted the last version. Cite that repost or an archived copy, never a dead .gov URL. [Source](https://centerforplainlanguage.org/the-federal-plain-language-guidelines-are-missing/).

## Voice and tone (Mailchimp)

CC BY-NC 4.0, so link only and never blend its text into this plugin. Use it as a reference for a voice-and-tone rubric. Its central split is a voice that stays constant and a tone that shifts with the reader's situation. It also has sections on writing for accessibility and for translation. [Source](https://styleguide.mailchimp.com/).

## Charts (UK Government Analysis Function)

OGL v3.0 for most text, adaptable with attribution. Delegate chart building to the dataviz skill if installed, and review its output against this list. [Source](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).

- Pick the chart from the relationship the data shows (part to whole, change over time, ranking, and so on).
- A pie chart gets five categories at most. Use bars beyond five, or when the values are close.
- Start bar chart axes at zero. If zero hides the story, switch chart type (a dot plot, for example) instead of breaking the axis. When an axis does not start at zero, say so plainly.
- Label series directly instead of using a legend. A legend matched by colour alone fails WCAG 1.4.1. When a legend is unavoidable, match its order and orientation to the data and say so above the chart.
- No 3D shapes and no boxes around legends.
- Put a text description in the page body directly under the chart, and mark the chart image as decorative.
- Name the specific data source and link straight to it, not to a homepage.

Contains public sector information licensed under the Open Government Licence v3.0. [Terms](https://analysisfunction.civilservice.gov.uk/terms-of-use/).

## Internationalization and right-to-left (W3C)

W3C Document License (per [W3C intellectual rights](https://www.w3.org/copyright/intellectual-rights/)), so paraphrase. [Quick tips](https://www.w3.org/International/quicktips/), [handling direction in HTML](https://www.w3.org/International/techniques/authoring-html#direction).

- Use UTF-8 for content, forms, servers, and databases, and declare it.
- Declare the page language and mark every change of language inside it.
- Support local formats for names, addresses, dates, and times. Never hard-code one country's form layout.
- Keep text simple and concise. Avoid composing sentences from separate strings, since word order changes in translation.
- Check images, animations, and examples for translatability and cultural bias. Text inside images is hard to translate.
- Give each page clearly visible navigation to its localized versions, labeled in the target language.
- For right-to-left text, set `dir="rtl"` on the `html` element. Set `dir` again only where the base direction changes. Isolate inline phrases that run in the opposite direction (`bdi`, or `dir` on a tightly wrapping element).

House rules, not W3C text.

- Use CSS logical properties (start and end) instead of left and right so the layout mirrors.
- Leave room for strings to grow in translation. Test each layout with the longest expected string, not the source language.
- Carbon's component definition of done requires strings parameterized for i18n (IBM, Apache-2.0 via the carbon-website repo, paraphrased). See design-systems.md.
