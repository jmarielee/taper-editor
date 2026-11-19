# SeverityTag

Labels a single finding as a BLOCK (it must be fixed) or a FLAG (a risk the athlete can accept). A report can mix both, so each finding carries its own tag.

## Properties

| Property | Type | Values |
|---|---|---|
| `severity` | variant | `block`, `flag` |

There are no text properties. The word is fixed per variant.

In code:

```jsx
<SeverityTag severity="flag" />
```

The Figma component (SeverityTag, in the "Taper Editor Design system" file) uses the same property name and the same two lowercase values.

## Which severity to use

| Severity | When | Word |
|---|---|---|
| `block` | The finding fails the gate. The plan can't pass until it's fixed. | Block |
| `flag` | The finding carries a risk the athlete can choose to accept. | Flag |

The report's verdict follows from its findings: any `block` finding makes the verdict `block`; only `flag` findings make it `findings`; no findings makes it `clean`.

## Anatomy

- **Container:** a `<span>`, laid out horizontally (`inline-flex`), centered vertically, hugging its content. Background from the tokens below. Padding `space/xs` top and bottom, `space/sm` left and right. Corner radius `radius/sm`.
- **Placement:** on the same line as the finding's title, before it, with a gap of `space/md`. FindingCard owns this layout.
- **Icon:** the same glyph as the matching VerdictBanner icon: the octagon for `block`, the triangle for `flag`. Every shape is drawn 12px wide, with its height following the shape, so the octagon and the triangle match in width (this matches Figma). In code, use the same tightly cropped viewBoxes as VerdictBanner, at a width of 12px. Centered vertically with the label, with no optical nudge at this size. Color is the accent token below. `aria-hidden="true"`. In code, use the shared VerdictIcon component, so each icon is defined once.
- **Label:** text style `label/large`: Barlow, 14/20, weight 500, letter spacing 0.1px (Material's defaults). Color is the accent token below. Typography isn't exported from Figma yet, so these values live in build-tokens.py, as VerdictBanner's do. The page loads Barlow at weights 400 and 500, so the browser doesn't fake the medium weight.
- **Gap** between icon and label: `space/xs`.

| Severity | Background | Icon and label |
|---|---|---|
| `block` | `verdict/block/background` | `verdict/block/accent` |
| `flag` | `verdict/findings/background` | `verdict/findings/accent` |

`flag` uses the findings colors because flag findings are what produce a `findings` verdict.

## Code names

Same rule as VerdictBanner: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front.

- `verdict/findings/accent` → `--verdict-findings-accent`
- Text style `label/large` → `--label-large-font-family`, `-font-size`, `-line-height`, `-font-weight`, `-letter-spacing`

## Rules

1. **One tag per finding,** placed before the finding's title.
2. **Color never carries meaning alone.** Always the icon and the word.
3. **Tokens only.** The one allowed exception is the 12px icon width.
4. **Shapes are reserved.** The octagon means block, and the triangle means findings or flag, in both VerdictBanner and SeverityTag. Don't use either shape for anything else.
5. **Sentence case:** "Block" and "Flag," never all caps.
6. **Print always uses Light values,** with a thin outline on all four sides in the accent color, because browsers drop background colors when printing. No page-break rule is needed; the tag is too small to split. In code, use the CSS keyword thin, not 1px, because check-tokens.py rejects typed pixel values.
7. **No other severities.** Clean, hold, and decline describe the whole report, so they belong to VerdictBanner, not to a tag.

## Right and wrong

- **Right:** "Block" with the octagon, before the title of the finding that fails the gate.
- **Wrong:** a red dot or colored text with no icon or word.
- **Wrong:** a "Clean" or "Hold" tag on a finding.
- **Wrong:** a flag finding tagged in red. Flag uses the findings colors.

## Accessibility

- The icon is decorative. The word carries the meaning for screen readers.
- The label is 14px text, so it must meet WCAG AA contrast (4.5:1) against its background in light and dark mode. Recheck whenever a token changes.
