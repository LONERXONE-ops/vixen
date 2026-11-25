# VIXEN Dataset Index

Order of scores: purpose / visual / discipline / usability / consistency / originality / accessibility (each 0-5). Rubric: `evaluation/concept-rubric.md`.

## Batch 02 (schema v2, evaluated)
| ID | Concept | Scores | Raw | Final | Ready | Critical |
|---|---|---|---|---|---|---|
| vixen-ui-010 | Dark glass tab bar with raised glowing center action and green current-tab marker (crypto/finance) | 4/4/3/3/4/4/2 | 69.0 | 69.0 | B | - |
| vixen-ui-011 | Green glass sidebar where the active item merges into the content panel (collapsed and expanded) | 4/4/4/4/4/5/2 | 78.0 | 78.0 | B | - |
| vixen-ui-012 | Floating bottom bar with center + action in a smooth bump (light and dark) | 3/4/4/3/4/3/3 | 70.0 | 70.0 | B | - |
| vixen-ui-013 | Magnifying dock navigation presented as a website component (Osmo Nr. 003) | 4/3/3/2/4/4/3 | 64.0 | 64.0 | B | - |
| vixen-ui-014 | Profile card with gradient aura header and overlapping white panel | 4/4/4/4/4/3/4 | 78.0 | 78.0 | B | - |
| vixen-ui-015 | 'Free UI Cards': one profile structure in two skins (header image and full-bleed gradient) | 4/4/3/3/4/3/3 | 69.0 | 69.0 | B | - |
| vixen-ui-016 | 'What is Brick mode?': before/after lock screen explainer | 5/4/4/4/4/3/5 | 83.0 | 83.0 | A | - |
| vixen-ui-017 | AI image generation dashboard with content-derived orange accent | 4/4/4/4/3/4/1 | 72.0 | 69.0 | B | CF1 |
| vixen-ui-018 | Dark settings modal: menu column plus profile form with accent-outlined active item | 4/4/3/3/4/3/1 | 65.0 | 65.0 | B | CF1? |
| vixen-ui-019 | Profile cards: solid card vs full-bleed photo with progressive blur | 4/4/4/3/5/4/4 | 79.0 | 79.0 | B | - |

`?` after a code would mean the failure is borderline (within measurement error). Contrast values are estimates from compressed images.

## Batch 01 (schema v1, pending re-evaluation)
vixen-ui-001 to vixen-ui-009 were analyzed before the rubric existed. They have no scores and no `pattern` block yet, so they are not comparable with batch 02 until upgraded.

## Early observations (hypotheses, n=10 evaluated)
1. Accessibility is the weakest measured category. Four of 10 records have some text under 3:1 (vixen-ui-013, 015, 017, 018), and two of those have a primary label under 3:1 (CF1: vixen-ui-017, vixen-ui-018, the latter borderline).
2. Only one record reaches readiness A (vixen-ui-016, an explainer with high measured contrast and one unambiguous purpose). The highest originality score (5) went to vixen-ui-011, where the active item fuses with the content surface, but its inactive labels measure about 3.2:1.
3. Several concepts paired with a single accent color used for only one or two roles (010, 012, 017).
4. Glass and photo-overlay concepts lose points on text contrast over variable backgrounds (010, 015, 019).
5. Label/placeholder and stat-label semantics errors appear in finished-looking concepts (015, 018), so correctness checks cannot be skipped because a design looks polished.

## Still needed from the collector
Creator and source for each concept; confirmation of batch 01 groupings; any code or prototypes.
