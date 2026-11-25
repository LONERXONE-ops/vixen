# VIXEN Dataset Guidelines (schema v2)

## Purpose of the dataset
The dataset is not a gallery to imitate. It is the evidence base from which an agent chooses, combines and adapts design patterns for a new project. Each record turns one concept design into: what it is, how it was measured, how it scored, what is worth preserving, and how it can change.

## What an agent does differently with VIXEN
1. **Classify the request** (what is being built, for whom, under what constraints). Do not pick a style yet.
2. **Retrieve by need, not by look.** Match the request against each record's `pattern.use_when` and `pattern.avoid_when`. Select 2-4 candidate patterns from different records.
3. **Compare candidates** using their evaluations and `failure_modes` before committing.
4. **Adapt, do not copy.** Keep each pattern's `must_preserve` items; change `free_to_vary` items to fit the brand, content and constraints. Never reproduce a source design's surface (layout, art, logos).
5. **Self-evaluate** the result with `evaluation/concept-rubric.md`, including measured contrast, and fix critical failures.
6. **Log** what was used, what was adapted and what happened (see `dataset/learning/`).

## Record schema v2
```
id, title, type ("concept"), discipline, category, source_files
creator, source, publication_date, license, attribution_status
attribution_visible_in_image      # text seen in the image; not proof of authorship
contains_third_party_content      # logos, photos, art that cannot be redistributed
measured:
  palette_method, palette, color_roles
  contrast_method, contrast_samples[ {element, role, fg, bg, ratio, near_threshold} ]
observed:        # visible facts only
  layout, hierarchy, typography, iconography, materials, background
interpretation:  # inference, clearly separated; includes implementation notes
  aesthetic, implementation_notes[], caveat
concept_work:
  essence, what_makes_it_work[], gaps_to_make_it_work[]
pattern:         # the agent-facing, reusable part
  name, use_when[], avoid_when[], must_preserve[], free_to_vary[],
  adaptation_examples[], failure_modes[]
evaluation:      # see evaluation/concept-rubric.md
  rubric_version, scores{category: {score, weight, points, evidence[], basis}},
  raw_total, critical_failures[], final_total, cap_applied, readiness, scope
lessons[], tags[], open_questions[]
```

## Rules
- `observed` holds only what is visible. Everything inferred (how it was built, intent) goes in `interpretation` and is never presented as the creator's intent.
- `creator`, `source`, `publication_date` stay `null` and `license` stays `"unknown"` until supplied with evidence. Text visible in the image goes in `attribution_visible_in_image` and is not treated as confirmed authorship.
- Do not store the source images in the repository. Records hold analysis and a source link.
- Every judged score needs at least one piece of cited evidence.
- Colors are sampled from pixels where possible; mark anything judged by eye as approximate.
- Typeface names are guesses unless the creator or source states them.

## Selection criteria for new entries
Prefer concepts that: (a) show a clear idea beyond a stock pattern, (b) show more than one state or theme, (c) have a known creator and source, (d) include code or implementation notes. Include a few weaker or flawed concepts on purpose, so the dataset also teaches what fails.

## Learning loop (what "adapts and learns" means here)
An installed skill cannot change a model's weights. What can change is the shared knowledge in this repository.
1. Each time an agent adapts a pattern for a real project, it appends an entry to `dataset/learning/adaptation-log.jsonl` (template in `dataset/learning/README.md`).
2. When several log entries agree on a lesson (for example "pattern X fails below 4.5:1 on photos"), the owner promotes it into the record's `failure_modes` or into a `knowledge/` file.
3. A new adaptation that scores well and differs meaningfully from its source can be added as its own record (type `adaptation`).
4. Promotion is reviewed by a person, so the dataset does not drift or amplify mistakes.
