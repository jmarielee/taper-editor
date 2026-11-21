# RaceWeekLoad

The checker's evidence for the race-week load check, shown as two comparisons: the average training a day, and the biggest training day, each for race week against the stretch before it. Every number in it comes from the checker's receipt, not from the editor.

It uses one small part of its own, ComparisonBadge, described below.

## Properties

| Property | Type | Values |
|---|---|---|
| `raceWeekAverage` | text | Race week's average training a day, as the receipt prints it. Example: "47.1" |
| `beforeAverage` | text | The average a day before race week, as the receipt prints it. Example: "45.7" |
| `raceWeekBiggestDay` | text | Race week's biggest training day, as the receipt prints it. Example: "90" |
| `beforeBiggestDay` | text | The biggest training day before race week, as the receipt prints it. Example: "75" |

Each value is the number only, as text. The component adds " min" after it. A value must be digits with an optional decimal part, such as "47.1" or "90". Anything else is an error, the same way an unknown variant is in SeverityTag and VerdictBanner.

In code:

```jsx
<RaceWeekLoad
  raceWeekAverage="47.1"
  beforeAverage="45.7"
  raceWeekBiggestDay="90"
  beforeBiggestDay="75"
/>
```

The Figma component (RaceWeekLoad, in the "Taper Editor Design system" file) uses the same four property names. Two differences between Figma and code:

- In Figma, each text property includes the unit ("47.1 min"), because Figma can't add it. In code, the component adds " min". Never include the unit in the code props.
- In Figma, each badge's result is set by hand through the nested instance properties `averageResult` and `biggestDayResult`. In code, the component works out each badge from the numbers, so there is no prop for it.

## Where the numbers come from

Every value comes from the race-week lines of the checker's receipt in `runs/`. For example, `runs/2026-07-19-trap-plan-run.txt` has:

```
[RAMP] preceding daily avg = 45.7 min over 7 days; race-week daily avg = 47.1 min
[RAMP] preceding max day = 75 min; race-week max training day = 90 min
```

| Prop | Receipt value |
|---|---|
| `raceWeekAverage` | `race-week daily avg` |
| `beforeAverage` | `preceding daily avg` |
| `raceWeekBiggestDay` | `race-week max training day` |
| `beforeBiggestDay` | `preceding max day` |

Copy each number exactly as the receipt prints it. Never round it, pad it, or take it from the report's prose. Reports round in their sentences ("47" and "46"), and the component must show the receipt, not the sentence.

## When to use it

| Situation | What to do |
|---|---|
| The receipt has both race-week lines | Show one RaceWeekLoad. |
| The race-week check is on hold (the race's role isn't declared yet) | Don't show it until the athlete answers. Its badges would read as a ruling the editor hasn't made yet. |
| The receipt has no race-week lines, or the checker couldn't run | Don't show it. Never fill it in from the report's prose. |
| The report declines the plan as out of scope | Don't show it. |
| The report doubts the count, for example because distances counted as zero minutes | Still show it. The finding's text explains the doubt. The component shows the count, not a judgment of it. |

The parent decides where it goes: inside the race-week finding when the check fails, or in the report's summary when it passes. The sentence around it must not repeat these numbers, because the component now carries them.

## Anatomy

The whole component is a vertical stack with a gap of `space/sm`: the header, then the box. It fills the width of its parent. The Figma component is 496 wide only to show it.

**Header:** a row with a gap of `space/sm`, centered vertically. If the header runs out of room, it wraps, and the source moves to the next line with its border.

- **Name:** `Race-week load`. Text style `label/large`, color `neutral/container/text`.
- **Source:** `Counted by the checker`. Text style `body/medium`, color `neutral/container/text-muted`. It has a thin border on its left side in `neutral/container/divider`, with `space/sm` padding between the border and the text. That border is the divider between the two halves. In code, it's a CSS border, not a typed character, so screen readers don't announce it.

**Box:** background `neutral/container/background`, corner radius `radius/md`. Padding `space/lg` left and right, `space/xs` top and bottom. It holds two groups, stacked with no gap.

**Group:** a vertical stack with no gap: the group label, two number rows, then the result row.

- **Group label:** `Average training a day` for the first group, `Biggest training day` for the second. Text style `body/medium`, color `neutral/container/text-muted`. The first group has `space/md` padding above its label. The second has `space/xl`, and that larger space is what separates the two groups.
- **Number row:** a row with the label on the left and the value on the right, pushed apart. Padding `space/sm` top and bottom, none on the sides. A thin bottom border in `neutral/container/divider`. The first row's label is `Race week`, and the second's is `Before race week`.
  - **Label:** text style `body/large`, color `neutral/container/text`.
  - **Value:** the number plus " min." Text style `title/medium`, color `neutral/container/text`.
- **Result row:** `Race week is` on the left and a ComparisonBadge on the right, pushed apart and centered vertically. Padding `space/sm` top and bottom, no border. The label uses `body/large` and `neutral/container/text`.

Every row has a gap of `space/sm` between its two sides, so they can't touch on a narrow screen.

Set the browser's default margins on `figure`, `dl`, `dd`, and `p` to 0.

### ComparisonBadge

A small pill holding one word that describes how race week compares.

| Property | Type | Values |
|---|---|---|
| `result` | variant | `lighter`, `heavier`, `same` |

- **Container:** a `<span>`, padding `space/xs` top and bottom, `space/sm` left and right, corner radius `radius/sm`.
- **Label:** text style `label/large`. The word is fixed per variant. There is no icon.

| Result | Word | Background | Text |
|---|---|---|---|
| `lighter` | Lighter | `verdict/clean/background` | `verdict/clean/accent` |
| `heavier` | Heavier | `verdict/block/background` | `verdict/block/accent` |
| `same` | Same | `neutral/container/badge/background` | `neutral/container/text` |

### How the badge is chosen

In code, the component compares the two values in each group as numbers, so "45" and "45.0" count as equal:

- Race week lower: `lighter`.
- Race week higher: `heavier`.
- Exactly equal: `same`.

The word always describes the numbers beside it, so it can never contradict them. It doesn't state a verdict. The checker treats ties differently on each measure (a tied average fails, and a tied biggest day passes), and that's why a tie gets the neutral "Same": the VerdictBanner above it already says whether the plan passed.

## Tokens

The `neutral` collection follows the same pattern as `verdict`: Light points to material-theme, and Dark is copied by hand. If the theme changes, update the Dark values by hand.

| Token | Light | Dark |
|---|---|---|
| `neutral/container/background` | points to Schemes/Surface Container High | #282A2E, copied from Surface Container High's Dark value |
| `neutral/container/text` | points to Schemes/On Surface | #E3E2E8, copied from On Surface's Dark value |
| `neutral/container/text-muted` | points to Schemes/On Surface Variant | #C4C6D2, copied from On Surface Variant's Dark value |
| `neutral/container/divider` | points to Schemes/Outline Variant | #434750, copied from Outline Variant's Dark value |
| `neutral/container/badge/background` | points to Schemes/Surface Container Highest | #333539, copied from Surface Container Highest's Dark value |

Text styles, with Material's defaults. Typography isn't exported from Figma yet, so these values live in build-tokens.py, as the other styles do.

- `body/large`: Barlow, 16/24, weight 400, letter spacing 0.5px.
- `body/medium`: Barlow, 14/20, weight 400, letter spacing 0.25px.
- `title/medium`: Barlow, 16/24, weight 500, letter spacing 0.15px.
- `label/large`: Barlow, 14/20, weight 500, letter spacing 0.1px.

## Code names

Same rule as VerdictBanner: slashes and spaces become hyphens, everything is lowercase, and the collection name goes in front.

- `neutral/container/text-muted` → `--neutral-container-text-muted`
- `neutral/container/divider` → `--neutral-container-divider`
- `neutral/container/badge/background` → `--neutral-container-badge-background`
- Text style `title/medium` → `--title-medium-font-family`, `-font-size`, `-line-height`, `-font-weight`, `-letter-spacing`

## Rules

1. **Receipt numbers only.** Every value comes from the receipt's race-week lines, copied exactly. Never from the report's prose, and never estimated.
2. **Never reformatted.** The component doesn't round, pad, or change a value. It only adds " min."
3. **The badge is worked out, never passed in.** It comes from comparing the two numbers beside it.
4. **Fixed text.** The header, group labels, and row labels are fixed words, in sentence case. None of them are props.
5. **One device per job.** Space separates the two groups. Thin lines help the eye travel from a label to its number. The badge is the only color. Don't add stripes, bands, extra lines, or an outline on screen.
6. **Evidence sits on the quiet surface.** The box uses the same surface as QuoteBlock, because both show evidence: QuoteBlock shows the plan's words, and this shows the checker's counts.
7. **Verdict colors only where they mean the same thing.** "Heavier" in block colors and "Lighter" in clean colors is allowed, because a heavier race week is exactly what blocks a plan and a lighter one is what lets it pass. The badge never has an icon, and the triangle never appears here, because this check never produces a flag.
8. **Color never carries meaning alone.** The word in the badge always carries it.
9. **Tokens only.** Use the variables named above. Never type a hex color or a pixel value. Borders use the CSS keyword thin, not 1px, because check-tokens.py rejects typed pixel values.
10. **No overall tally.** Don't add a line like "2 of 2 lighter." The VerdictBanner already gives the overall result.
11. **Print always uses Light values.** Browsers drop background colors when printing, so in print the box gets a thin outline on all four sides in the Light value of `neutral/container/text`, and each badge gets a thin outline in its own text color. Add `break-inside: avoid` to the whole component so it doesn't split across two pages. Row lines and the header divider keep their Light color in print. They are faint on paper, and that is intended: they guide the eye but carry no meaning.

## Right and wrong

- **Right:** 47.1 and 45.7, copied from the receipt, with "Heavier" in block colors beside them.
- **Wrong:** 47 and 46, taken from the report's sentence.
- **Wrong:** a badge that says "Heavier" when the race-week number is the lower one.
- **Wrong:** a gray band behind each group label, or an extra line under it.
- **Wrong:** an icon inside the badge.
- **Wrong:** RaceWeekLoad shown in a report whose race-week check is on hold.

## Accessibility

- Wrap the component in a `<figure>`, with the header as its `<figcaption>`, so a screen reader announces "Race-week load, Counted by the checker" before the numbers.
- Write each group as a description list (`<dl>`), with each row's label as a `<dt>` and its value or badge as a `<dd>`. Give the list `aria-labelledby` pointing to its group label.
- Every text and background pair must meet WCAG AA contrast (4.5:1) in light and dark mode, including each badge's text on its background. Recheck whenever a token changes.

## Why it looks this way

The athlete doesn't need to understand the math. They need to see which numbers were counted, not guessed, and whether race week came out lighter. So the numbers are pulled out of the sentence into plain pairs, each pair ends in one word, and one line at the top says who counted them. The layout stays quiet so the numbers are the first thing the eye lands on.
