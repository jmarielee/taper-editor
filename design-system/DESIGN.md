# Taper Editor design system

The design system behind Taper Editor's reports. A report reads top to bottom as verdict, evidence, decision: the banner says whether the plan passes, each finding shows the plan's own words and the checker's numbers, and the report ends with the decisions that belong to the athlete. Every rule here serves that order and the editor's promise: it checks the plan, it never rewrites it, and the athlete decides.

It's written for two readers: designers and developers, and AI agents that build or fill in reports. An agent should be able to build from these docs alone, and the system checks its work instead of trusting it.

Updated November 23, 2026. Settled decisions come from the design decision list. Component docs in `components/` hold the details for each piece.

## How it's built

1. **Figma first.** Every component is designed in the "Taper Editor Design system" Figma file with variables and component properties. Property names and values are identical in Figma and code.
2. **One doc per component.** Each component gets a doc in `components/`: its properties, anatomy, tokens, rules, accessibility, and demo cases.
3. **Code from the doc.** Claude Code builds each component in a fresh session, from its doc alone. It reports what it found unclear or had to guess, and the doc gets fixed, not just the code.
4. **Check against Figma.** The Vite demo (`npm run dev`) shows every component, with a button to switch between light and dark mode. It's compared with Figma before each commit.
5. **Tokens only.** `build-tokens.py` turns the Figma variable exports in `tokens/` into `build/tokens.css`. `check-tokens.py` fails the build on any hex color or pixel value in `react/`, with one exception: the 22px VerdictBanner icon width.

## Working with AI agents

An agent that builds or fills in a report follows the same rules as a person, but the system doesn't rely on it reading carefully. Every rule an agent could break has a check.

| Rule for agents | What enforces it |
|---|---|
| Read this file, then the doc for each component you use. The docs are the spec. | Each doc is tested by an agent: Claude Code builds the component from the doc alone, and whatever it had to guess becomes a doc fix. |
| Use tokens only. Never type a hex color or a pixel value. | `check-tokens.py` fails on any hex or px value in `react/`. |
| Copy words, never write them. Finding titles, plan quotes, and checker numbers come exactly from the report and its receipt. | check_contract.py verifies the report's quotes and its four parts. Components show numbers as given and never round them. |
| Pass only the values a component accepts. | Components with fixed values (VerdictBanner, SeverityTag, ComparisonBadge, RaceWeekLoad) throw an Error that names the problem. Fix the input. Never catch the error to get past it. |
| Use the same names as Figma. | Property names and values are identical in Figma and code, so a Figma frame maps straight to props. |
| Don't guess silently. | When a doc doesn't say, the agent lists the gap under "Unclear or guessed," and the doc gets fixed. |

**From report to components.** An agent turns a report into components like this:

| In the report | Component |
|---|---|
| The overall verdict | VerdictBanner. Any block finding makes it `block`, only flags make it `findings`, and no findings makes it `clean`. `hold` and `decline` come from the editor. |
| One finding | VerdictBanner's message, which is the finding's title. |
| Two or more findings | VerdictBanner's list: each finding's severity and its title, word for word, blocks first. |
| BLOCK or FLAG on a finding | SeverityTag, only inside VerdictBanner's list. |
| "Your plan says" | QuoteBlock, one per excerpt, without the report's surrounding quotation marks. |
| Race-week load | RaceWeekLoad, with the numbers exactly as the receipt prints them. |
| Lighter, heavier, or the same | ComparisonBadge. |

## Standing rules

These apply to every component and every report.

- Tokens only.
- Color never carries meaning alone. A word always says it too.
- No left accent stripes.
- Print always uses Light values.
- The octagon means block. The triangle means findings or flag.
- Sentence case everywhere.
- The verdict is "clean," never "pass."
- Checker numbers are shown exactly as the receipt prints them, never rounded.
- One device per job: space separates, thin lines guide the eye, and color appears only where it means something.
- Italic means a note.
- The editor never prescribes training or rewrites the plan. "Your call" hands back a question (rules.md, check_contract.py).
- No em dashes in anything the design system writes. Quoted plan text keeps its own punctuation.

## Color

The page is white, the brand owns navy, and finish yellow has exactly two jobs.

| Role | Token | Light | Dark | Notes |
|---|---|---|---|---|
| Page | `page/background` | #FFFFFF | #111418 | The page, the tag chips, and the evidence boxes. |
| Text | `container/text` | #181C21 | #E0E2E9 | Main text. |
| Muted text | `container/text-muted` | #42474F | #C2C7D1 | Gray labels and notes. |
| Lines | `container/divider` | #D5D9E0 | #3A404B | Typed from the settled report. |
| Box outlines | `container/outline` | points to divider | points to divider | Outlines always match the dividers. |
| Finding chip | `chip/background` | #ECEEF4 | #272A2F | The "Finding 1 of 4" chip. |
| Print lines | `print/line` | #9AA1AD | #9AA1AD | Print only, as tested on paper. |
| Build weeks | `chart/build-weeks` | #5E7FB8 | #5E7FB8 | Brand collection. |
| Race week | `chart/race-week` | #123A7A | #AEC6FF | Brand collection. |
| Race day | `race-day/highlight` | #FAE8B0 | #54481F | Finish yellow mixed onto the page ahead of time. |

- **Navy (#123A7A) belongs to the brand.** Its jobs are the masthead band and the race-week bar. The hold verdict borrows it.
- **Finish yellow (#F2C230) has two jobs:** the 6px line under the masthead and the race-day highlight. It's never a verdict color. `race-day/highlight` is yellow pre-mixed onto the page (38% on white, 30% on #111418), because `build-tokens.py` rejects transparent colors.
- **Verdict colors:** each of the five verdicts has a background, an accent, and a text color. The banner is the only tinted surface on the page. The tints stand apart from white by hue, not lightness.
- **Neutrals are cool blue-gray,** not Material's default lavender.
- **The brand collection is typed by hand,** so a Material Theme Builder update can't move it.

## Type

Two families, five sizes, and italic only for notes. Always use the material-theme text styles, never the M3 library.

| Style | Font | Size / line | Letter spacing | Used for |
|---|---|---|---|---|
| `headline/medium` | Barlow Condensed Regular | 28/36 | 0 | Report title, banner headline, finding titles |
| No style yet | Barlow Condensed Regular | 24 | | Masthead, "Where this leaves you," part titles in the race-week box |
| `body/large` | Barlow Regular | 16/24 | 0.5 | Body text, banner message and list titles, each finding's question |
| `title/medium` | Barlow Medium | 16/24 | 0.15 | Terms in a paragraph, comparison labels, the plan's words in a quote box |
| `label/large` | Barlow Medium | 14/20 | 0.1 | Labels, tags, the finding chip, chart numbers, box tag lines |
| `body/medium` | Barlow Regular | 14/20 | 0.25 | Small text such as the check date and chart labels |
| `body/small-italic` | Barlow Italic | 12/16 | 0.4 | Notes only |

- A term is set in medium weight, with an italic note under its paragraph that defines it.
- Barlow italic loads at 400 and 500, so the browser never fakes the slant.

## Space and shape

Space separates sections. There are no horizontal rules between them.

| Token | Value | Main uses |
|---|---|---|
| `space/xs` | 4 | Banner headline to its message or list, chip padding |
| `space/sm` | 8 | Finding chip to title, paragraph to its note, the banner icon's optical nudge |
| `space/md` | 12 | Banner icon to headline, tag to title, between banner list lines, part label to a quote box |
| `space/lg` | 16 | Banner and quote box padding, between paragraphs |
| `space/xl` | 24 | Race-week box padding, banner to the first part in a one-finding report |
| `space/2xl` | 32 | Above every part label, between the parts of the race-week box |
| `space/3xl` | 48 | Between findings and report sections |
| `radius/xs` | 4 | Tops of chart bars |
| `radius/sm` | 8 | Chips and tags |
| `radius/md` | 12 | Banner and boxes |

## Report structure

1. **Masthead:** a navy band with "The Taper Editor" and a 6px finish-yellow line under it.
2. **Report header:** the title and "Checked [date]."
3. **VerdictBanner.**
4. **Findings,** each with its number on a chip, its title, then four parts in order: "Your plan says," "The problem," "What it costs you," and "Your call." Each part starts with a small gray label. The markdown keeps its bold labels so check_contract.py can read them. In a one-finding report, the banner carries the finding, so there's no chip or title.
5. **Where this leaves you:** where things stand, the athlete's decisions as a numbered list, then the two paths for each severity, shown once.

## Components

| Component | Status | Doc |
|---|---|---|
| VerdictBanner | Built: headline and message. The findings list is designed in Figma, with code next. | `components/verdict-banner.md` |
| SeverityTag | Built. A word on a page-colored chip, no icon. | `components/severity-tag.md` |
| QuoteBlock | Built. White with a thin outline, the plan's words in medium weight. | `components/quote-block.md` |
| ComparisonBadge | Built. Lighter uses the clean colors, Heavier the block colors, always with the word. | |
| RaceWeekLoad | Built, rework planned. It gains the weekly chart, the day strip, and the regrouped comparisons once checker.py prints weekly totals. | `components/race-week-load.md` |

**VerdictBanner's list,** for reports with two or more findings: the headline, then each finding's title word for word, in the report's order, so blocks come first. A banner shows the message or the list, never both. Each line has a SeverityTag and its title. The tags fill a shared column, so Block and Flag chips are the same width. **Each title takes its tag's color:** Block titles use the block accent and Flag titles use the findings accent, because a block should read as a block at a glance. In Figma, the list is a slot with FindingLine as its preferred instance. Figma's "Flag non-preferred instances" setting is a hint, not a lock.

**Still to build:** term definition, question prompt ("Your call"), finding card, report heading and summary, the date table, and number rows. Then CLAUDE.md and an agent test that builds a full report from a real report in the repo.

## Print

Tested on Letter paper in Chrome with Pam's report and the trap plan report.

- Print styles force Light values, whatever the computer's own setting.
- Fills always print (`print-color-adjust: exact`).
- Boxes, the banner, tables, rows, and "Where this leaves you" never split across pages.
- Print at 90%, with 0.5 in margins at the top and 0.6 in at the sides and bottom.
- Every page has a footer with the report name and check date on the left and "Page 2 of 5" on the right.
- Lines and outlines print in `print/line`, because the screen's light gray can break up on an office laser printer.

## Keeping Figma and tokens in sync

Material Theme Builder generates the material-theme collection. It needs care on every update:

- **Check the fonts after every Update.** Update resets the material-theme text styles to Roboto. The five in use are set back to: headline/medium Barlow Condensed Regular 28/36, 0; body/large Barlow Regular 16/24, 0.5; body/medium Barlow Regular 14/20, 0.25; title/medium Barlow Medium 16/24, 0.15; label/large Barlow Medium 14/20, 0.1. The other styles are unused.
- **Color match stays on.** With it off, Update rebuilds Primary, Error, and Clean, and the navy and yellow leave the theme.
- **The neutral keys are bright blues on purpose.** With Color match on, the plugin weakens Neutral to one-eighth strength and Neutral Variant to one-eighth plus 4. The keys Neutral #1E7BC6 and Neutral Variant #4A7AB0 give Surface Container #ECEEF4 and On Surface Variant #42474F, the report's grays.
- **body/small-italic is added by hand,** not by the plugin, so an update won't recreate it.
- **The divider is typed from the settled report,** not linked to Outline Variant, which was visibly darker.
- **Three verdict Dark values are copied by hand** (block, clean, and hold accents), because Figma exports cross-collection links using the other collection's first mode. If the theme changes, update them.
- **Save a Figma version before any re-export.**

## Open items

- The two flag paths' sentences ("Accept the risk," "Change it") are still drafts.
- The masthead's navy and finish-yellow tokens, including dark mode, are decided with the report heading.
- checker.py needs weekly totals, with each week's uncounted sessions, before the RaceWeekLoad rework.
