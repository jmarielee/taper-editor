# QuoteBlock

One exact excerpt from the athlete's plan, shown as evidence. Anything inside a QuoteBlock is the plan's own words and can be checked against the plan.

## Properties

| Property | Type | Values |
|---|---|---|
| `quote` | text | One excerpt from the plan, word for word, with no quotation marks around it. |

There are no variants and no other slots. The block looks the same in every finding.

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
| Several separate excerpts, even when the report's markdown joins them on one line with "...", "·", or bridging words | One QuoteBlock per excerpt, stacked. Drop a bare separator like "..." or "·" between them. |
| The editor's words between two excerpts ("and later:") | Plain body text (`body/large`) between the blocks. Never inside a block. |
| A few quoted words inside the editor's own sentence, like "Run 5 miles" | Plain text in quotation marks, in the sentence's regular weight. No QuoteBlock. |
| A note that defines a term | Outside the block, under the editor's paragraph that uses the term. That's the term definition piece (step 5), not part of QuoteBlock. |

## Anatomy

- **Container:** a `<blockquote>`. Fill `neutral/page/background`. A thin outline on all four sides in `neutral/container/outline`. Padding `space/lg` on all four sides. Corner radius `radius/md`. It fills the width of its parent, and its height follows the text. Reset the browser's default blockquote margin to 0.
  - In code, draw the outline as a border: `border: thin solid var(--neutral-container-outline)`. Use a border, not an outline, so the line takes up space. That matches Figma, where the stroke is weight 1, Inside, and included in the auto layout. In both, the text sits 1 + 16 in from the edge.
- **Text:** a `<p>` inside the blockquote, with margin 0. Text style `title/medium`: Barlow, 16/24, weight 500, letter spacing 0.15px. Color `neutral/container/text`. These values are already in build-tokens.py, and RaceWeekLoad's comparison labels use the same style. In Figma, the text style is `material-theme/title/medium`.
- **Quotation marks:** a left curly mark (U+201C) before the excerpt and a right curly mark (U+201D) after it. In code, write them as real characters in the same `<p>` as the excerpt, not as CSS generated content, so they print, copy, and read aloud with the text. They use the same style and color as the excerpt.
- **Spacing around the block:** none. QuoteBlock has no outer margin. Its parent (FindingCard) sets the space between blocks and around them.

| Token | Used for | Light | Dark |
|---|---|---|---|
| `neutral/page/background` | Fill | points to Schemes/Surface Container Lowest (#FFFFFF) | #111418, typed |
| `neutral/container/outline` | Outline on screen | points to `neutral/container/divider` (#D5D9E0) | points to `neutral/container/divider` (#3A404B) |
| `neutral/container/text` | Text and quotation marks | points to Schemes/On Surface (#181C21) | #E0E2E9, typed |
| `neutral/print/line` | Outline in print | #9AA1AD, typed | #9AA1AD, typed. Never used, because print always uses Light. Figma needs a value in every mode. |

The hex values are for checking only. Code uses the variables.

QuoteBlock no longer uses `neutral/container/background`. Don't delete that token: RaceWeekLoad still uses it. RaceWeekLoad moves to the white, outlined surface in its own rework, so don't change it now.

## Code names

Same rule as VerdictBanner: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front. Text styles drop the `material-theme` prefix.

- `neutral/page/background` → `--neutral-page-background`
- `neutral/container/outline` → `--neutral-container-outline`
- `neutral/container/text` → `--neutral-container-text`
- `neutral/print/line` → `--neutral-print-line`
- `title/medium` → `--title-medium-font-family`, `--title-medium-font-size`, `--title-medium-line-height`, `--title-medium-font-weight`, `--title-medium-letter-spacing`

## Rules

1. **The plan's words only.** Nothing the editor wrote goes inside a QuoteBlock: no labels, no bridging words, no commentary, no notes. A note that defines a term goes outside the block, under the editor's paragraph that uses the term.
2. **Word for word.** The component never changes the excerpt. It doesn't trim it, fix it, change its case, or add an ellipsis. Marks that are already part of the excerpt, such as "…" and "[joint]", pass through as written.
3. **The plan's punctuation stays.** The design system's "no em dashes" rule covers what we write. It doesn't reach inside a quote. If the plan used an em dash, the quote shows it.
4. **One excerpt per block.** Two excerpts are two blocks, even when the report's markdown puts them on one line.
5. **Never cut off.** Long excerpts wrap. No truncation, no line clamp, no scrolling. Use `overflow-wrap: break-word` so a long unbroken string can't overflow the block.
6. **Tokens only.** Use the variables named above. Never type a hex color or a pixel value. Use the CSS keyword `thin` for the line, not 1px, because check-tokens.py rejects typed pixel values.
7. **One edge: the thin outline.** A thin line on all four sides, on screen and in print. No left accent stripe, no shadow, no gray fill.
8. **Always neutral.** Never use verdict colors for the text, the outline, or the fill. The block looks the same in a block finding and a flag finding.
9. **No italics.** Italic means a note, and notes don't go in the box.
10. **No label inside.** "Your plan says" belongs to FindingCard.
11. **Print always uses Light values.** tokens.css applies Dark values on screen only, so print gets the Light values with no extra code. In print, only the outline's color changes: it switches to `neutral/print/line`, because the screen's light gray can break up on an office laser printer. The line stays `thin`, and the fill stays the page color, which is white on paper, so nothing is lost when a browser drops background colors. Add `break-inside: avoid` so a block doesn't split across two pages.

## Right and wrong

- **Right:** one line from the plan, word for word, in curly quotation marks, in medium weight, on the page color with a thin cool-gray outline.
- **Right:** two excerpts as two stacked blocks, with "and later:" as plain text between them.
- **Wrong:** a box with a gray fill.
- **Wrong:** an italic note inside the box.
- **Wrong:** two excerpts in one block, joined with "...".
- **Wrong:** a quote with a colored stripe down the left side.
- **Wrong:** "and later:" or "Your plan says" inside the block.
- **Wrong:** a quote, outline, or fill in a verdict color because its finding is a block.
- **Wrong:** a long quote cut off with "…" by the component.
- **Wrong:** a block wrapped around three quoted words from the middle of the editor's sentence.
- **Wrong:** plan words quoted inside the editor's paragraph set in medium weight.

## Accessibility

- The `<blockquote>` element tells screen readers this is quoted text. The quotation marks are real characters, so they are read and copied with the excerpt.
- `neutral/container/text` on `neutral/page/background` must meet WCAG AA contrast (4.5:1) in light and dark mode. Today it's 17.1:1 in light and 14.3:1 in dark. Recheck whenever a token changes.
- The outline is 1.4:1 against the page in light and 1.8:1 in dark. That's below the 3:1 that WCAG asks of graphics that carry meaning, and that's allowed here, because the outline only groups the quote. The `<blockquote>`, the curly marks, and the medium weight say "quote" without it.

## Demo

Keep the demo's three QuoteBlock cases: one quote, a long quote that wraps, and two quotes stacked with "and later:" between them. Leave the demo's page colors in demo.css as they are. They're demo chrome, and the report page gets its own tokens in step 5.

## Why it looks this way

The quote is evidence. The athlete should be able to see at a glance which words are their plan's and which are the editor's, and trust that the plan's words were not touched. The box uses the report's evidence surface, white with a thin cool-gray outline, which the race-week box also uses after its rework. Medium weight makes the quote the anchor of each finding for a reader who skims. It stays in the main text color, never a verdict color, so the plan's words stay calm and separate from the verdict's alarm. It isn't larger, because the next size up is 24 condensed, which would make the plan's words look like the editor's finding titles.
