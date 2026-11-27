# VIXEN tools

Python 3 with `numpy` and `Pillow` (`pip install numpy pillow`). These scripts make every record measurable and checkable the same way.

| File | Purpose |
|---|---|
| `contrast.py` | Measures text/icon contrast from boxes you define on each image (rubric v1.1). Writes `contrast_final.json` and an optional montage with the boxes drawn. |
| `evaluate.py` | Builds the `evaluation` block (scores, accessibility from measured contrast, critical failures, cap at 69, readiness). |
| `gen_example.py` | Template for generating schema-2.1 records. Copy it for each batch. |
| `validate_records.py` | Checks that every record is complete and internally consistent. Run before every delivery. |
| `example_boxes.json` | Example input for `contrast.py`. |

## Workflow for a new batch
1. For each image, decide the text and icon elements to measure and give each a role (`primary`, `secondary`, `icon`) and a pixel box. Write them in `boxes.json` (see `example_boxes.json`).
2. `python contrast.py boxes.json --out contrast_final.json --montage montage.png --sheet sheet`
3. **Open the contact sheets (`sheet-1.png`, ...) and the montage, and check that every box really contains its text** (the sheets show the actual crop with its measured values). In earlier batches several boxes missed their text (ratios near 1.0 or an impossible value are the usual sign). Fix the box and re-run. Measure text on gradients or photos one line at a time.
4. Copy `gen_example.py`, write one `rec(...)` call per concept (observed, interpretation, components, system, build, pattern, judged scores with evidence).
5. Every number written in prose (for example "about 2.8:1") must match `contrast_final.json`. Regenerate the prose if a measurement changes.
6. `python validate_records.py dataset/records` must report no errors, and every record must be at the current schema.
7. Zip `dataset/` and `evaluation/` and deliver.
