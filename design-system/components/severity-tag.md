# SeverityTag

Labels a single finding as a BLOCK (it must be fixed) or a FLAG (a risk the athlete can accept). Tags appear only in VerdictBanner's list of findings, one per finding, before the finding's title.

## Properties

| Property | Type | Values |
|---|---|---|
| `severity` | variant | `block`, `flag` |

There are no text properties. The word is fixed per variant. In code, any other `severity` value throws an error that names the two valid values.

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

- **Container:** a `<span>` that hugs its content (`inline-flex`). Fill `neutral/page/background`, the page color. Padding `space/xs` top and bottom, `space/sm` left and right. Corner radius `radius/sm`.
- **Word:** text style `label/large`: Barlow, 14/20, weight 500, letter spacing 0.1px. Color is the accent token below. These values are already in build-tokens.py. In Figma, the text style is `material-theme/label/large`.
- **No icon.** The component holds only the word. SeverityTag no longer uses VerdictIcon. Leave VerdictIcon.jsx as it is, because VerdictBanner still uses it.
- **Placement:** in VerdictBanner's list of findings, before each finding's title. VerdictBanner owns that layout: the tag column, how tags line up, and the space between them.

| Severity | Chip | Word |
|---|---|---|
| `block` | `neutral/page/background` | `verdict/block/accent` |
| `flag` | `neutral/page/background` | `verdict/findings/accent` |

`flag` uses the findings colors because flag findings are what produce a `findings` verdict.

| Token | Light | Dark |
|---|---|---|
| `neutral/page/background` | #FFFFFF | #111418 |
| `verdict/block/accent` | #900708 | #FFB4AA |
| `verdict/findings/accent` | #A14B00 | #FFAE66 |

The hex values are for checking only. Code uses the variables.

SeverityTag no longer uses `verdict/block/background` or `verdict/findings/background`. Don't delete them: VerdictBanner still uses them.

## Code names

Same rule as VerdictBanner: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front. Text styles drop the `material-theme` prefix.

- `neutral/page/background` → `--neutral-page-background`
- `verdict/block/accent` → `--verdict-block-accent`
- `verdict/findings/accent` → `--verdict-findings-accent`
- `label/large` → `--label-large-font-family`, `--label-large-font-size`, `--label-large-line-height`, `--label-large-font-weight`, `--label-large-letter-spacing`

## Rules

1. **Banner only.** Tags live only in VerdictBanner's list of findings, one per finding, before its title. A finding's own title in the body of the report carries no tag.
2. **The word always shows.** Color never carries meaning alone. The word is the meaning, so there's no icon.
3. **Tokens only, with no exceptions.** Without the icon, SeverityTag.css needs no pixel value. Remove SeverityTag's 12px allowance from check-tokens.py, including its line in the docstring. VerdictBanner's 22px allowance stays.
4. **A page-colored chip with a colored word.** Never fill the chip with a verdict tint, never make it solid, and never outline it on screen.
5. **Sentence case:** "Block" and "Flag," never all caps.
6. **Print always uses Light values.** tokens.css applies Dark values on screen only, so print gets the Light values with no extra code. Add a thin outline on all four sides in the accent color, as a backup in case a browser or printer drops the chip's fill. Use the CSS keyword `thin`, not 1px, because check-tokens.py rejects typed pixel values. No page-break rule is needed, because the tag is too small to split. Don't add `print-color-adjust` here: fills are handled for every component at once, in a later print pass.
7. **No other severities.** Clean, hold, and decline describe the whole report, so they belong to VerdictBanner, not to a tag.

## Right and wrong

- **Right:** "Block" in the block color on a page-colored chip, in the banner's list before the title of the finding that fails the gate.
- **Right:** "Flag" in the findings color on a page-colored chip, on a block banner or a findings banner.
- **Wrong:** a tag with an icon.
- **Wrong:** a tag filled with the block or findings tint.
- **Wrong:** a solid red "Block" or a solid orange "Flag."
- **Wrong:** a tag with a colored outline on screen.
- **Wrong:** a tag beside a finding's own title in the body of the report.
- **Wrong:** a red dot or colored text with no word.
- **Wrong:** a "Clean" or "Hold" tag.
- **Wrong:** a flag finding tagged in the block color.

## Accessibility

- The word is plain text, so screen readers read it. VerdictBanner's list decides how the tag and the title are read together.
- The word is 14px text, so it must meet WCAG AA contrast (4.5:1) against the chip in light and dark mode. Today: Block is 9.5:1 in light and 10.9:1 in dark, and Flag is 6.0:1 in light and 10.1:1 in dark. Recheck whenever a token changes.
- The chip stands apart from the banner's tint at about 1.1:1. That's allowed, because the chip only frames the word. The word carries the meaning.

## Demo

A page-colored chip disappears on the demo page, so show the tags where they live. Replace the current SeverityTag cases with two stand-in banner boxes, with the markup in demo/main.jsx and the styles in demo/demo.css: one filled with `verdict/block/background` holding a Block tag and a Flag tag, and one filled with `verdict/findings/background` holding a Flag tag. Give each box padding `space/lg` and radius `radius/md`. They stand in for VerdictBanner's list until its rework, and they are demo chrome, not part of SeverityTag.

## Why it looks this way

The tag's only job is to say which findings are blocks and which are flags, and the word does that. An icon would repeat the octagon already in the banner's headline and stack identical triangles down the list, and blocks always come first, so position helps too. The chip is the page color so the word lifts off the banner's tint without adding a new color.

Considered and ruled out:

- **Outlined tags.** They're crisp and look the same on paper, but the outline is the report's evidence device, and colored outlines read as clickable.
- **Solid tags.** A solid red "Block" competes with the headline, and solid orange flags look as urgent as the block.
- **Chips in the flag color.** The findings background and the block tint are nearly the same lightness (1.01 to 1), so flag chips vanish on a block banner.
