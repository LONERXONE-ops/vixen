# VIXEN Dataset Index

Batch 01: 10 images, 9 concepts (img-05 and img-08 grouped as one concept in two themes; unconfirmed).

| ID | Concept | Category | Attribution |
|---|---|---|---|
| vixen-ui-001 | Glass launcher menu over dark bloom wallpaper | app menu | needed |
| vixen-ui-002 | Black pill bottom nav, expanding active label | tab bar | needed |
| vixen-ui-003 | Nav active-state variant matrix (12) | component taxonomy | needed |
| vixen-ui-004 | Social video tab bar, raised circular tab | tab bar | needed |
| vixen-ui-005 | Collapsible workspace sidebar, light + dark | sidebar | needed |
| vixen-ui-006 | Dark glass sidebar, blue glow, hover tooltips | sidebar | needed |
| vixen-ui-007 | Three tab bar treatments on magenta | tab bar | needed |
| vixen-ui-008 | Liquid-glass pill nav (cropped) | floating nav | needed |
| vixen-ui-009 | Edge-docked AI usage meter widget | widget | needed |

## Method notes
- Colors: sampled from the supplied images (median-cut quantization and saturated-pixel medians). Approximate because the images are compressed; items marked "approx" were not sampled.
- Typefaces are guesses from letterforms and are not confirmed.
- `observed` = visible in the image. `interpretation` = Claude's inference, including all implementation notes. Never treat interpretation as the creator's intent.
- `creator`, `source`, `publication_date` are null and `license` is "unknown" until supplied.

## Early patterns (hypotheses from n=9, to be tested as the dataset grows)
1. **Navigation dominates this batch.** 7 of 9 concepts are navigation (tab bars and sidebars).
2. **Active-state signaling is the central design question.** Techniques seen: filled-vs-outline icon, label reveal, pill/tile fill, underline, raised circle, notch, edge marker, color change. The strongest concepts stack two or more cues.
3. **Glass is paired with a controlled backdrop.** Every glass concept uses a deliberately chosen wallpaper (bloom shapes or photos). None of them show glass over arbitrary content.
4. **One accent color is a recurring discipline.** Concepts 001, 002, 003 are achromatic; 006 has only blue; 007 only magenta.
5. **Collapsed/compact states are shown in the stronger sidebar concepts** (005, 006).
6. **Recurring gaps** (what stops a concept from shipping): text contrast on glass/pale surfaces, hidden-label discoverability, reduced-motion handling, small touch targets, and performance of blur/refraction.

## Still needed from the collector
- Creator name and source link for each concept.
- Confirm whether img-05 and img-08 are the same concept.
- Code, CSS or prototypes where they exist.
- Whether you want the dataset to include the 'concept_work' fields for every record (current format) or a leaner schema.
