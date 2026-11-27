# VIXEN: Universal Design Intelligence

VIXEN is a design-intelligence system for AI agents. The goal is that an agent using VIXEN understands *why* designs work and can adapt those principles to a new project, instead of producing one generic style.

It is not a UI kit, a prompt pack or a screenshot gallery. It is an evidence base (a dataset of analyzed concept designs), a measurement and evaluation method, and, later, an installable Agent Skill built from that evidence.

> **Status: dataset phase, pre-release.** A first `SKILL.md` exists, but the skill has not been tested in any agent and the install command below is unverified. See [Roadmap](#roadmap).

## What exists today

| Part | State |
|---|---|
| Concept dataset (`dataset/records/`) | Batches 1 to 4 collected: 46 records, `vixen-ui-001` to `vixen-ui-046`. Records are being brought to one schema (see below). |
| Evaluation rubric (`evaluation/concept-rubric.md`) | v1.1, in use |
| Tools (`tools/`) | Contrast measurement, evaluation builder, record generator, validator |
| Family pages (`dataset/families/`) | Draft: profile / talent card |
| `SKILL.md` | First version, written from the dataset guidelines and rubric. Untested. |
| `core/`, `knowledge/`, `workflows/` | **Not written yet.** They will be derived from the dataset. |
| License | **Not chosen yet** (see [License](#license)) |

### Dataset schema status
| Records | Schema |
|---|---|
| `001` to `009` | v1 (no scores, no components) |
| `010` to `019` | v2.0 (scored) |
| `020` to `046` | v2.1 (current) |

The older records are being upgraded to schema 2.1. Run the validator for the exact current counts:

```
python tools/validate_records.py dataset/records
```

## How a record works

Each record turns one concept design into structured evidence:

- **measured**: palette and contrast ratios taken from the image
- **observed**: visible facts only
- **interpretation**: inferences, kept separate from facts
- **concept_work**: what makes it work, and what is missing
- **components** and **system**: the parts and how they connect
- **build**: effort (Low / Medium / High) and risks
- **pattern**: `use_when`, `avoid_when`, `must_preserve`, `free_to_vary`, `failure_modes`
- **evaluation**: scored with the rubric, with critical failures reported separately

Full schema and the agent decision protocol: [`dataset/dataset-guidelines.md`](dataset/dataset-guidelines.md).
Scoring rules: [`evaluation/concept-rubric.md`](evaluation/concept-rubric.md).

## Install (unverified)

The planned install command is:

```
npx skills add LONERXONE-ops/vixen
```

This has not been tested. If it fails, use the manual route below.

## Using the dataset manually

1. Clone the repository:
   ```
   git clone https://github.com/LONERXONE-ops/vixen.git
   ```
2. Point your agent at `dataset/dataset-guidelines.md` first, then let it search `dataset/records/` by each record's `pattern.use_when` and `pattern.avoid_when`.
3. For comparing several records of the same component, use `dataset/families/`.

The guidelines tell the agent to adapt patterns, never to copy a source design's surface (layout, art, logos).

## Using the tools

Requires Python 3 with `numpy` and `Pillow`:

```
pip install numpy pillow
```

| Tool | Purpose |
|---|---|
| `tools/contrast.py` | Measures text and icon contrast from boxes you define, and draws a verification montage |
| `tools/evaluate.py` | Builds the evaluation block (scores, accessibility rule, critical failures, readiness) |
| `tools/gen_example.py` | Template for generating records |
| `tools/validate_records.py` | Checks every record for completeness and consistency |

See [`tools/README.md`](tools/README.md) for details.

## Repository layout

```
dataset/
  dataset-guidelines.md      schema, agent protocol, learning loop
  records/                   one JSON record per concept, plus INDEX.md
  families/                  comparisons of records of the same component
  learning/                  template for logging real adaptations
evaluation/
  concept-rubric.md          scoring rubric
  CHANGELOG.md               rubric changes
tools/                       measurement, evaluation and validation scripts
SKILL.md                     agent skill entry point
CHANGELOG.md                 project changes
```

Source images are **not** stored in this repository (`raw-designs/`, `*.psd` and `*.fig` are git-ignored). Records hold analysis and, when known, a source link.

## Dataset integrity rules

- Observed facts are kept separate from interpretation. Design intent is never invented.
- `creator`, `source` and `publication_date` stay `null`, and `license` stays `"unknown"`, until evidence is supplied. Text visible in an image is recorded as `attribution_visible_in_image` and is not proof of authorship.
- Third-party content (logos, characters, photos, brand names) is listed in `contains_third_party_content`.
- Accessibility is measured from the image, never estimated. Contrast values within 0.4 of a threshold are flagged `near_threshold` and need checking in the source file.

## Roadmap

1. Repository and identity (done)
2. Dataset: collect and analyze concepts (in progress: 46 of a planned 100+)
3. Upgrade all records to schema 2.1
4. Derive `knowledge/` from the dataset (color, typography, composition, spacing, accessibility, design languages)
5. Derive `core/` (philosophy, reasoning, adaptation) and `workflows/`
6. Rewrite `SKILL.md` from `knowledge/` and `core/` and verify the install process
7. Test the skill across agents
8. First public release

## Contributing

Concepts are reviewed by a person before entering the dataset. A good candidate:

- shows an idea beyond a stock pattern
- shows more than one state or theme
- has a known creator and source
- belongs to a component family, so it can be compared with other records

Weaker or flawed concepts are welcome too, because the dataset should also teach what fails. When you submit a concept, include its creator and source if you know them.

## License

No license has been chosen yet. Until one is added, all rights are reserved by the repository owner. Analyzed concept designs remain the property of their creators and are not redistributed here.
