# VIXEN Dataset Guidelines (schema v2.1)

## Purpose of the dataset
The dataset is not a gallery to imitate. It is the evidence base from which an agent chooses, combines and adapts design patterns for a new project. Each record turns one concept design into: what it is, how it was measured, how it scored, what is worth preserving, how its components connect, how hard it is to build, and how it can change.

## What an agent does differently with VIXEN
1. **Classify the request** (what is being built, for whom, under what constraints). Do not pick a style yet.
2. **Retrieve by need, not by look.** Match the request against each record's `pattern.use_when` and `pattern.avoid_when`; use `dataset/families/` to compare several records of the same component.
3. **Compare candidates** using their evaluations, `failure_modes` and `build` effort before committing.
4. **Adapt, do not copy.** Keep each pattern's `must_preserve` items and the `system.links` that make components work together; change `free_to_vary` items to fit the brand, content and constraints. Never reproduce a source design's surface (layout, art, logos).
5. **Build every component from the same tokens** (`system.shared_tokens`), so the parts look and behave like one product.
6. **Self-evaluate** with `evaluation/concept-rubric.md`, including measured contrast, and fix critical failures.
7. **Log** what was used, adapted and learned (see `dataset/learning/`).

## Record schema v2.1
```
schema_version, id, title, type ("concept"), discipline, category, source_files
creator, source, publication_date, license, attribution_status
attribution_visible_in_image      # text seen in the image; not proof of authorship
contains_third_party_content      # logos, photos, art that cannot be redistributed
measured:
  palette_method, palette, color_roles
  contrast_method, contrast_samples[ {element, role, fg, bg, ratio, ratio_low, fg_assumed, near_threshold} ]
observed:        # visible facts only
interpretation:  # inference, kept separate; includes implementation notes
concept_work:    # essence, what_makes_it_work[], gaps_to_make_it_work[]
components[]:    # {name, role, states_shown[], connects_to[]}
system:          # shared_tokens[], links[]  (how the components are connected)
build:           # effort (Low/Medium/High), approach[], risks[]
pattern:         # name, use_when[], avoid_when[], must_preserve[], free_to_vary[], adaptation_examples[], failure_modes[]
evaluation:      # see evaluation/concept-rubric.md
related[]:       # {id, relation} links between records
lessons[], tags[], open_questions[]
```
Schema v2.0 (batch 02) lacks `components`, `system`, `build` and `related`; batch 01 is v1. Both will be upgraded.

### Build effort scale
- **Low**: standard HTML/CSS (flex or grid, gradients, shadows, standard components).
- **Medium**: custom shapes, masks or layered gradients, scripted animation, or state logic across components.
- **High**: real-time effects (refraction, heavy backdrop blur, WebGL), native-only APIs, or heavy dependence on photographic assets.

### What "connected" means
A concept is only workable if its parts form a system. Record the `components`, what each links to (`connects_to`), the tokens they share, and the links between them (for example one accent color that always means "current", or one metric shown in two components). A component list without links is incomplete.

## Rules
- `observed` holds only what is visible. Anything inferred (how it was built, intent) goes in `interpretation`.
- `creator`, `source`, `publication_date` stay `null` and `license` stays `"unknown"` until supplied with evidence. Visible text goes in `attribution_visible_in_image` and is not treated as confirmed authorship. Upload file names are not evidence of content or authorship.
- Do not store source images in the repository. Records hold analysis and a source link.
- Every judged score needs cited evidence. Colors are sampled from pixels where possible; mark anything judged by eye as approximate. Typeface names are guesses unless the creator states them.

## Selection criteria for new entries
Prefer concepts that (a) show an idea beyond a stock pattern, (b) show more than one state or theme, (c) have a known creator and source, (d) include code or implementation notes, (e) belong to a component family so records can be compared. Include some weaker or flawed concepts on purpose, so the dataset also teaches what fails.

## Families
Records of the same component are compared in `dataset/families/`. A family page lists the invariants, the variations, the measured failures and a draft of defaults. Family guidance is a draft until it has enough records and has been reviewed.

## Learning loop (what "adapts and learns" means here)
An installed skill cannot change a model's weights. What changes is the shared knowledge in this repository.
1. When an agent adapts a pattern for a real project it appends an entry to `dataset/learning/adaptation-log.jsonl` (template in `dataset/learning/README.md`).
2. When several entries agree on a lesson, the owner promotes it into a record's `failure_modes`, a family page or a `knowledge/` file.
3. A new adaptation that scores well and differs meaningfully from its source can be added as a record (type `adaptation`).
4. Promotion is reviewed by a person, so the dataset does not drift or amplify mistakes.
