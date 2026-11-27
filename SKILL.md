---
name: vixen
description: Design intelligence for building or editing interfaces and visual concepts. Use when creating or redesigning UI (navigation, cards, profile screens, landing pages, dashboards, onboarding, widgets) and you want to pick patterns by need, adapt them to the project instead of copying a style, and check the result for contrast and usability. Draws on a dataset of analyzed concept designs with measured contrast, scores and failure modes.
---

# VIXEN

VIXEN gives you an evidence base of analyzed concept designs and a method for using it. The goal is a result that fits this project, not a copy of a reference.

## Scope today
The dataset covers UI concepts: navigation, cards and profiles, landing and hero pages, dashboards, onboarding, widgets, product pages. If the request is outside that (print, 3D, motion), say the dataset has no records for it and work from general design judgment.

## Method

1. **Classify the request.** What is being built, for whom, under what constraints (platform, brand, content, audience, light or dark). Do not choose a style yet.
2. **Retrieve by need, not by look.** Read `dataset/records/INDEX.md`, then open only the records whose `pattern.use_when` matches the need and whose `pattern.avoid_when` does not. For several records of one component, check `dataset/families/`.
3. **Compare candidates.** Weigh each record's `evaluation`, `failure_modes` and `build.effort` before committing to one.
4. **Adapt, do not copy.** Keep the pattern's `must_preserve` items and the `system.links` that make its components work together. Change `free_to_vary` items to fit the brand and content. Never reproduce a source design's layout, art, logos or characters.
5. **Build from one set of tokens.** Use the record's `system.shared_tokens` idea: one accent role, one radius scale, one type pairing, so every part looks like one product.
6. **Self-evaluate** with `evaluation/concept-rubric.md`. Check contrast on every text line, including secondary text on photos and gradients. Fix any critical failure before delivering.
7. **Log real adaptations** in `dataset/learning/adaptation-log.jsonl` (template in `dataset/learning/README.md`) when the project allows it.

Do not narrate these steps to the user. Show the result and the reasons that matter.

## Rules that apply to every output

- Primary text needs 4.5:1 contrast. Secondary text and icons need at least 3:1. Do not carry state or meaning by color alone.
- Icon-only navigation, or labels visible only on hover, is an accessibility weakness. Add labels or a visible active state.
- One dominant action per view. Two equal-weight primary actions is a failure the dataset records repeatedly.
- Put the unit inside each stat value ("$50/hr", "12 yrs"). Ambiguous stat labels cost points in the dataset.
- Proofread all visible text. Typos and mismatched content recur across records.
- Text over photos or gradients needs a scrim or a solid panel.
- Show the states the component needs (active, collapsed, hover, focus, loading, error), not only the default.
- Overlap and breakout effects must never cover text.

## Using the records honestly

- A record describes a concept as presented in a static image. Behavior, motion and states that were not shown were not scored.
- Scores are calibrated judgments, except accessibility, which is measured. Contrast values flagged `near_threshold` need checking in the real implementation.
- Family pages are drafts until reviewed. Treat their guidance as hypotheses.
- `creator`, `source` and `license` are unknown for every record. Do not attribute a record to anyone.
- Records `001` to `019` may be at an older schema and may lack scores or components. Check `schema_version` before relying on a field.

## Files

- `dataset/dataset-guidelines.md`: schema and the full agent protocol
- `dataset/records/`: one JSON record per concept, with `INDEX.md`
- `dataset/families/`: comparisons of records of the same component
- `evaluation/concept-rubric.md`: scoring rules, accessibility rule, critical failures
- `tools/contrast.py`: measure contrast from boxes drawn on an image (needs Python, `numpy`, `Pillow`)
- `dataset/learning/`: adaptation log template

Load files on demand. Do not read the whole dataset.
