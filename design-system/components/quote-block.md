# QuoteBlock

One exact excerpt from the athlete's plan, shown as evidence. Anything inside a QuoteBlock is the plan's own words and can be checked against the plan.

## Properties

| Property | Type | Values |
|---|---|---|
| `quote` | text | One excerpt from the plan, word for word, with no quotation marks around it. |

There are no variants. The block looks the same in every finding.

In code:

```jsx
<QuoteBlock quote="Do not make up a missed long run by jumping ahead. Repeat the previous successful distance and continue from there." />
```

In a report, the excerpt is the quote in the finding's "Your plan says" line. check_contract.py already verifies those quotes against the plan's evidence file, so pass the quote through exactly as the report prints it, without the report's surrounding quotation marks.

The Figma component (QuoteBlock, in the "Taper Editor Design system" file) uses the same property name.

One difference between Figma and code: in Figma, the quotation marks are typed as part of the text, because Figma can't add them. In code, the component adds them. Never include the surrounding quotation marks in the `quote` prop.

## When to use it

| Content | What to do |
|---|---|
| One whole line or sentence from the plan | One QuoteBlock. |
| Several separate lines from the plan | One QuoteBlock per line, stacked. Don't join them with "·" or any other separator. |
| The editor's words between two excerpts ("and later:") | Plain text between the blocks. Never inside a block. |
| A few quoted words inside the editor's own sentence | Plain text in quotation marks. No QuoteBlock. |

## Anatomy

- **Container:** a `<blockquote>`. Background `neutral/container/background`. Padding `space/lg` on all four sides. Corner radius `radius/md`. It fills the width of its parent, and its height follows the text. Reset the browser's default blockquote margin to 0.
- **Text:** a `<p>` inside the blockquote, with margin 0. Text style `body/large`: Barlow, 16/24, weight 400, letter spacing 0.5px. Color `neutral/container/text`. These type values are already in build-tokens.py for VerdictBanner. Use the same ones.
- **Quotation marks:** a left curly mark (U+201C) before the excerpt and a right curly mark (U+201D) after it. In code, write them as real characters in the same `<p>` as the excerpt, not as CSS generated content, so they print, copy, and read aloud with the text. They use the same style and color as the excerpt.
- **Spacing around the block:** none. QuoteBlock has no outer margin. Its parent (FindingCard) sets the space between blocks and around them.

| Token | Light | Dark |
|---|---|---|
| `neutral/container/background` | points to Schemes/Surface Container High | #282A2E, copied from Surface Container High's Dark value |
| `neutral/container/text` | points to Schemes/On Surface | #E3E2E8, copied from On Surface's Dark value |

The `neutral` collection follows the same pattern as `verdict`: Light points to material-theme, and Dark is copied by hand. If the theme changes, update the two Dark values by hand.

## Code names

Same rule as VerdictBanner: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front.

- `neutral/container/background` → `--neutral-container-background`
- `neutral/container/text` → `--neutral-container-text`

## Rules

1. **The plan's words only.** Nothing the editor wrote goes inside a QuoteBlock: no labels, no bridging words, no commentary.
2. **Word for word.** The component never changes the excerpt. It doesn't trim it, fix it, change its case, or add an ellipsis. Marks that are already part of the excerpt, such as "…" and "[joint]", pass through as written.
3. **The plan's punctuation stays.** The design system's "no em dashes" rule covers what we write. It doesn't reach inside a quote. If the plan used an em dash, the quote shows it.
4. **One excerpt per block.** Two excerpts are two blocks.
5. **Never cut off.** Long excerpts wrap. No truncation, no line clamp, no scrolling. Use `overflow-wrap: break-word` so a long unbroken string can't overflow the block.
6. **Tokens only.** Use the variables named above. Never type a hex color or a pixel value.
7. **No left accent stripe, and no outline on screen.** The soft surface and the quotation marks do the work.
8. **Always neutral.** Never use verdict colors. The block looks the same in a block finding and a flag finding.
9. **No italics.** The marks and the surface already say "this is a quote."
10. **No label inside.** "Your plan says" belongs to FindingCard.
11. **Print always uses Light values,** with a thin outline on all four sides in the Light value of `neutral/container/text`, because browsers drop background colors when printing. Add `break-inside: avoid` so a block doesn't split across two pages. In code, use the CSS keyword thin, not 1px, because check-tokens.py rejects typed pixel values.

## Right and wrong

- **Right:** one line from the plan, word for word, in curly quotation marks on the neutral surface.
- **Right:** two excerpts as two stacked blocks, with "and later:" as plain text between them.
- **Wrong:** a quote with a colored stripe down the left side.
- **Wrong:** "and later:" or "Your plan says" inside the block.
- **Wrong:** a quote tinted red because its finding is a block.
- **Wrong:** a long quote cut off with "…" by the component.
- **Wrong:** a block wrapped around three quoted words from the middle of the editor's sentence.

## Accessibility

- The `<blockquote>` element tells screen readers this is quoted text. The quotation marks are real characters, so they are read and copied with the excerpt.
- `neutral/container/text` on `neutral/container/background` must meet WCAG AA contrast (4.5:1) in light and dark mode. Recheck whenever a token changes.

## Why it looks this way

The quote is evidence. The athlete should be able to see at a glance which words are their plan's and which are the editor's, and trust that the plan's words were not touched. A quiet neutral surface sets the evidence apart without judging it. The verdict colors stay with the verdict.
