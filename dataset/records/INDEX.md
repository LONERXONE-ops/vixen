# VIXEN Dataset Index

Score order: purpose / visual / discipline / usability / consistency / originality / accessibility (each 0-5). Rubric: `evaluation/concept-rubric.md` (v1.1).

## Batch 03 (schema v2.1)
| ID | Concept | Scores | Raw | Final | Ready | Critical | Schema |
|---|---|---|---|---|---|---|---|
| vixen-ui-020 | Marketplace landing hero: fanned artwork cards with floating @handle chips | 4/4/4/3/4/4/3 | 75.0 | 75.0 | B | - | 2.1 |
| vixen-ui-021 | Streetwear landing page with oversized headlines, cut-out hero and a 'rotate your phone' prompt | 4/4/3/2/4/4/1 | 64.0 | 64.0 | B | CF1? | 2.1 |
| vixen-ui-022 | Profile card with experience meter and social row (bar layout vs ring layout) | 4/4/4/3/4/4/4 | 77.0 | 77.0 | B | - | 2.1 |
| vixen-ui-023 | Talent card with 'Get in Touch' arrow bar: white card and full-bleed green gradient card | 4/4/4/3/4/3/2 | 71.0 | 71.0 | B | - | 2.1 |
| vixen-ui-024 | Mobile profile screen in dark and light themes with activity feed and avatar tab (Whop) | 4/4/4/4/5/3/3 | 78.0 | 78.0 | B | - | 2.1 |
| vixen-ui-025 | Freelancer cards with rating, earned and rate stats and a Get in Touch CTA (light and dark) | 4/4/3/4/5/3/3 | 74.0 | 74.0 | B | - | 2.1 |
| vixen-ui-026 | Soft UI component sheet: follow card, video card, product card, toggles, nav, search, progress ring | 4/4/3/3/5/3/2 | 69.0 | 69.0 | B | - | 2.1 |
| vixen-ui-027 | Free UI Cards (light variant): white header-image card and full-bleed red/blue card | 4/4/3/3/4/3/3 | 69.0 | 69.0 | B | - | 2.1 |
| vixen-ui-028 | 'Which is Better' card A/B test: photo-top card vs full-bleed photo card with overlay | 4/4/4/4/4/3/5 | 80.0 | 80.0 | A | - | 2.1 |
| vixen-ui-029 | Social profile concept with scenic blurred backdrop, glass stats panel and sticker-decorated avatar | 4/4/3/3/4/4/1 | 67.0 | 67.0 | B | CF1 | 2.1 |
| vixen-ui-030 | Free UI Cards series: header-art white card and full-bleed red/blue card (variant 3) | 4/4/3/3/4/3/3 | 69.0 | 69.0 | B | - | 2.1 |

## Batch 02 (schema v2.0, re-scored under rubric v1.1)
| ID | Concept | Scores | Raw | Final | Ready | Critical | Schema |
|---|---|---|---|---|---|---|---|
| vixen-ui-010 | Dark glass tab bar with raised glowing center action and green current-tab marker (crypto/finance) | 4/4/3/3/4/4/2 | 69.0 | 69.0 | B | - | 2.0 |
| vixen-ui-011 | Green glass sidebar where the active item merges into the content panel (collapsed and expanded) | 4/4/4/4/4/5/2 | 78.0 | 78.0 | B | - | 2.0 |
| vixen-ui-012 | Floating bottom bar with center + action in a smooth bump (light and dark) | 3/4/4/3/4/3/3 | 70.0 | 70.0 | B | - | 2.0 |
| vixen-ui-013 | Magnifying dock navigation presented as a website component (Osmo Nr. 003) | 4/3/3/2/4/4/3 | 64.0 | 64.0 | B | - | 2.0 |
| vixen-ui-014 | Profile card with gradient aura header and overlapping white panel | 4/4/4/4/4/3/4 | 78.0 | 78.0 | B | - | 2.0 |
| vixen-ui-015 | 'Free UI Cards': one profile structure in two skins (header image and full-bleed gradient) | 4/4/3/3/4/3/3 | 69.0 | 69.0 | B | - | 2.0 |
| vixen-ui-016 | 'What is Brick mode?': before/after lock screen explainer | 5/4/4/4/4/3/5 | 83.0 | 83.0 | A | - | 2.0 |
| vixen-ui-017 | AI image generation dashboard with content-derived orange accent | 4/4/4/4/3/4/1 | 72.0 | 69.0 | B | CF1? | 2.0 |
| vixen-ui-018 | Dark settings modal: menu column plus profile form with accent-outlined active item | 4/4/3/3/4/3/1 | 65.0 | 65.0 | B | - | 2.0 |
| vixen-ui-019 | Profile cards: solid card vs full-bleed photo with progressive blur | 4/4/4/3/5/4/3 | 77.0 | 77.0 | B | - | 2.0 |

`?` after a critical-failure code marks a borderline measurement (within 0.4 of the threshold). Contrast values are estimates from compressed images.

## Batch 01 (schema v1, pending upgrade)
vixen-ui-001 to vixen-ui-009 predate the rubric and have no scores, components, system links, build notes or `pattern` blocks, so they are not comparable with later batches yet.

## Families
- `families/profile-card.md`: draft synthesis of 9 profile/talent card records.

## Early observations (hypotheses; 21 scored records)
1. Accessibility is the weakest measured category: scores are 1 in 4 records, 2 in 4, 3 in 9, 4 in 2 and 5 in 2. 14 of 21 records have some primary or secondary text under 3:1 on the conservative measure.
2. Three records have a critical failure (vixen-ui-017, vixen-ui-021, vixen-ui-029); two reach readiness A (vixen-ui-016, vixen-ui-028).
3. Judged scores cluster at 3-4 and most records land in readiness B, which is expected when concepts are polished mockups with missing states.
4. Full-bleed gradient or photo skins are where small text most often fails (see the profile-card family).
5. Missing states are the most common usability gap: hover, focus, loading, error and 'already followed' states are rarely shown.

## Still needed from the collector
Creator and source for each concept; confirmation of the batch 01 groupings; any code or prototypes.
