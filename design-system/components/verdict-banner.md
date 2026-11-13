# VerdictBanner

The overall result for one Taper Editor report. It tells the athlete, in one glance, whether their taper plan passes, fails, needs a look, or needs an answer first.

## Properties

| Property | Type | Values |
|---|---|---|
| `verdict` | variant | `block`, `clean`, `findings`, `hold`, `decline` |
| `headline` | text | Verdict word, a colon, then a short phrase. Example: "Blocked: this plan fails" |
| `message` | text | One plain sentence. For `hold`, the message is the question. |

In code:

```jsx
<VerdictBanner
  verdict="hold"
  headline="On hold: one question first"
  message="Is your July 12 race the goal, or training for something else?"
/>
```

The Figma component (VerdictBanner, in the "Taper Editor Design system" file) uses the same three property names and the same five lowercase values. Keep them identical in both places.

## Which verdict to use

| Verdict | When | Headline starts with |
|---|---|---|
| `block` | The plan fails. At least one finding is a BLOCK. | Blocked: |
| `findings` | The plan passes, but one or more FLAG findings carry risk the athlete can accept. | Findings: |
| `clean` | The plan passes with no findings. | Clean: |
| `hold` | The editor needs one answer before it can judge the plan. | On hold: |
| `decline` | The input is outside scope (not an AI-generated running or triathlon plan). | Not reviewed: |

These match the checker's overall verdicts (CLEAN, FINDINGS, HOLD, BLOCK) plus DECLINE from the scope rules. Name the verdict `clean`, never "pass."

## Anatomy

- **Container:** a `<section>`. Background `verdict/{verdict}/background`, padding `space/lg`, corner radius `radius/md`.
- **Icon:** Material Symbols, filled, weight 400. Every shape is drawn 22px wide, with its height following the shape, so all five icons match in width (this matches Figma). In code, crop each icon's viewBox tightly to its shape and set the width to 22px. Color `verdict/{verdict}/accent`, `aria-hidden="true"`. Sits left of the text with a gap of `space/md`. Top padding `space/sm`: this is an optical alignment to the headline's letters, set by eye in Figma. It is intentionally not centered on the headline's line box.
- **Headline:** an `<h2>`. Text style `headline/medium`: Barlow Condensed, 28/36, weight 400. Color `verdict/{verdict}/accent`. The report's own title is the `<h1>`.
- **Message:** a `<p>`. Text style `body/large`: Barlow, 16/24, weight 400. Color `verdict/{verdict}/text`. Gap from the headline: `space/xs`.
- **Letter spacing:** 0 for `headline/medium` and 0.5px for `body/large` (Material's defaults, confirmed in the Figma styles). Typography isn't exported from Figma yet, so these values live in build-tokens.py for now. When Figma exports them, remove them from the script so they're defined in one place.
- **Font fallbacks:** Barlow Condensed, then Arial Narrow, then sans-serif. Barlow, then system-ui, then sans-serif.

| Verdict | Icon (Material Symbols, filled) | Accent, Light | Accent, Dark |
|---|---|---|---|
| `block` | `report` (octagon) | points to Schemes/Error | #FFB4AA, copied from Error's Dark value |
| `findings` | `warning` (triangle) | #A14B00, typed | #FFAE66, typed |
| `clean` | `check_circle` | points to Extended Colors/Clean | #95D68F, copied from Clean's Dark value |
| `hold` | `help` | points to Schemes/Primary | #AEC6FF, copied from Primary's Dark value |
| `decline` | `do_not_disturb_on` | #434750, typed | #C4C6D2, typed |

The three copied Dark values exist because Figma exports cross-collection links using the other collection's first mode. If the theme changes, update those three by hand. The `findings` and `decline` accents are typed in both modes, so nothing goes stale. The `decline` values match material-theme's On Surface Variant.

## Code names

CSS variable names come from the Figma variable path: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front unless Figma's code syntax says otherwise.

- `verdict/block/accent` → `--verdict-block-accent`
- `space/lg` → `--space-lg`
- `radius/md` → `--radius-md`
- `Extended Colors/Clean` → `--material-theme-extended-colors-clean`
- Text style `headline/medium` → `--headline-medium-font-family`, `-font-size`, `-line-height`, `-font-weight`, `-letter-spacing`

## Rules

1. **One per report, at the top.** Every report has exactly one VerdictBanner, before any findings.
2. **Color never carries meaning alone.** Every banner shows the icon, the verdict word in the headline, and the message. Reports are read on phones, laptops, and paper, sometimes printed in black and white.
3. **Tokens only.** Use the variables named above. Never type a hex color or a pixel value, except the 22px icon width.
4. **No left accent stripes, and no outline on screen.** The soft tint, icon, and words do the work.
5. **Print always uses Light values**, even if the page is in dark mode, because paper is white. Browsers drop background colors when printing, so in print the banner gets a 1px outline on all four sides in the Light accent color.
6. **Shapes are reserved.** The octagon means block, and the triangle means findings, here and in SeverityTag (where it marks a flag). Don't use either shape for anything else.
7. **Finish yellow is never a verdict color.** It belongs to the brand (the finish band and the main button).
8. **Sentence case.** No all-caps headlines.
9. **Hold asks one question.** The message for `hold` is a single question, never a statement or a list.
10. **No new verdicts.** Don't invent a sixth variant or reuse verdict colors for decoration.

## Right and wrong

- **Right:** a `block` banner with the octagon, "Blocked: this plan fails," and one sentence explaining why.
- **Wrong:** a red text line with no icon. Color alone carries the meaning.
- **Wrong:** a tinted box with a colored stripe down the left side.
- **Wrong:** a `clean` banner on a report that has FLAG findings. Use `findings`.
- **Wrong:** calling the verdict "PASS." Its name is `clean`. Saying a plan "passes" in a sentence is fine.

## Accessibility

- The icon is decorative. The verdict word in the headline carries the meaning for screen readers.
- Every text and background pair, including the accent-colored headline, should meet WCAG AA contrast (4.5:1) in both light and dark mode. Recheck whenever a token changes.

## Why it looks this way

The report should feel like a coach who's on your side: calm, but honest. A soft tint keeps the tone calm, and the blunt headline ("This plan fails") carries the seriousness, so the banner never needs a red wall to be taken seriously. The palette is inspired by the Boston Marathon's blue and yellow, with a condensed, race-bib headline style.
