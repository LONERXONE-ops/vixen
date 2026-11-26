# Family: profile / talent card

Status: **draft**, derived from 9 records (batches 02 and 03). Treat as hypotheses until more records are added and the owner has reviewed them.

## Records in the family
| ID | Skins | Stats | Primary action | Final | Access. | Ready |
|---|---|---|---|---|---|---|
| vixen-ui-014 | white card, gradient aura header | none (tags and bio only) | black 'Follow' pill + 2 icon buttons | 78.0 | 4 | B |
| vixen-ui-015 | dark card with header image; full-bleed red/blue | Rating / $160 hours / 24 Month (ambiguous) | white 'Get In Touch' bar on both skins | 69.0 | 3 | B |
| vixen-ui-019 | solid card with photo top; full-bleed photo with progressive blur | two counts with icons only (no text labels) | 'Follow +' pill, dark then white | 77.0 | 3 | B |
| vixen-ui-022 | header photo; centered layout with ring | Likes / Posts / Views | 'Follow +' pill or '+' circle | 77.0 | 4 | B |
| vixen-ui-023 | white with green banner; full-bleed green gradient | Rating / Posts / Followers | Follow pill AND 'Get in Touch' bar (two actions) | 71.0 | 2 | B |
| vixen-ui-025 | light and dark themes with banner art | rating ('raiting') / earned / rate, units in values | 'Get in Touch' bar, black then white | 74.0 | 3 | B |
| vixen-ui-027 | white with header image; full-bleed red/blue | Rating / $160 hours / 24 Month (ambiguous) | 'Get In Touch' bar, black then white | 69.0 | 3 | B |
| vixen-ui-028 | photo-top; full-bleed photo with dark overlay | Rating / Earned / Rate, units in values | 'Get In Touch' bar, black then white (+ bookmark button) | 80.0 | 5 | A |
| vixen-ui-030 | white with header art; full-bleed red/blue | Rating / $150 hours / 24 Month (ambiguous) | 'Get In Touch' bar, black then pale | 69.0 | 3 | B |

Related profile *screens* (not cards): vixen-ui-024, vixen-ui-029.
Same series: vixen-ui-015 and vixen-ui-027 credit '@Spline'; vixen-ui-030 matches the style but shows no credit.

## Invariants (present in nearly every record)
- An avatar that overlaps the header or banner edge.
- Name with a role or bio line; trust markers (verified badge, online dot) in some records.
- One primary action: 'Follow' for social profiles, 'Get in Touch' for hire cards.
- A header treatment that gives personality: gradient aura (014), blurred image (015), photo (019, 022, 028), mesh gradient (023), translucent shapes (025), abstract art (030).

## Variations and what the measurements show
1. **Stat labels.** Records whose values carry the unit inside the value ('$50/hr', '$53K earned', '$45k+ Earned') read unambiguously (025, 028). Records that print '$160' above 'hours' or '24' above 'Month' do not (015, 027, 030). The unambiguous records finished at 74 and 80; the ambiguous ones at 69 each. This is an observation, not a tested cause.
2. **Full-bleed skins and small text.** Five of the six full-bleed gradient or photo skins had some label measuring below 3.5:1 (015, 019, 023, 027, 030). The exception, 028 variant B, places a dark gradient overlay under all text and measures about 11:1 or higher.
3. **Light-grey role text on white** measured about 2.1:1 in 027 and 030.
4. **Call to action.** Where two skins exist, the CTA flips between a dark fill on light surfaces and a light fill on dark or gradient surfaces (019, 023, 025, 027, 028, 030). In 015 it stays white on both. Only 023 shows two heavy actions on one card (Follow and Get in Touch), which the evaluation scored lower on usability.
5. **Typos in core data.** 025 repeats 'raiting' in two cards, a content error that cost discipline points.
6. **A/B comparison.** 028 changes four variables at once (photo treatment, text color, CTA color, bookmark placement), so the comparison cannot say which change matters.

## Draft defaults for a talent card (to be validated)
- Put the unit inside each stat value ('$50/hr', '12 yrs'), and proofread labels.
- Keep one dominant action; place secondary actions (bookmark) beside it or on the media.
- For a full-bleed photo or gradient skin, place text on a dark scrim or a solid inset panel, then check every text line (primary and secondary) for contrast.
- Keep secondary text (role, handle) at 4.5:1 or above on its surface.
- Derive both skins from one token set so the structure, spacing and CTA position do not change.
- Show hover, focus, 'already following' and loading states; none of the records do.

## Build notes
Effort is Low to Medium in this family: a card grid, a stat row, token-based skins and, for glass skins, backdrop blur. Photo-led skins add image weight and blur cost (vixen-ui-019, 028 B, 029).
