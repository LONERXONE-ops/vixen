#!/usr/bin/env python3
"""Example generator: builds ONE schema-2.1 record from measured contrast + judged scores.
Copy this file, replace the content, and add one rec(...) call per concept.
Run:  python contrast.py boxes.json --out contrast_final.json   (check the montage first)
      python gen_example.py contrast_final.json out_dir
"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import make, J
contrast = json.load(open(sys.argv[1])); out_dir = sys.argv[2]; os.makedirs(out_dir, exist_ok=True)
rec, J, R = make(19, contrast)          # base 19: key '03' -> id vixen-ui-022 ; for a new batch use (last_id, ...)
def comp(*a): return [dict(name=n, role=r, states_shown=s, connects_to=c) for n, r, s, c in a]
rec('03', title="EXAMPLE: profile card with experience meter", category="card / profile", source_files=["example/img-03"],
    attribution_visible_in_image=None, contains_third_party_content=None,
    palette=[["#F5F5F5","page"],["#000000","text (sampled)"]], roles="Neutral cards; color only in the metric.",
    observed=dict(layout="...", hierarchy="...", typography="...", iconography="...", materials="...", background="..."),
    interpretation=dict(aesthetic="...", implementation_notes=["..."], caveat="Inference."),
    concept_work=dict(essence="...", what_makes_it_work=["..."], gaps_to_make_it_work=["..."]),
    components=comp(("Header image","mood",["default"],["Avatar"]), ("Avatar","identity",["default"],["Header image"])),
    system=dict(shared_tokens=["large radius"], links=["Avatar overlaps the header."]),
    build=dict(effort="Low", approach=["Standard card"], risks=["..."]),
    pattern=dict(name="...", use_when=["..."], avoid_when=["..."], must_preserve=["..."], free_to_vary=["..."], adaptation_examples=["..."], failure_modes=["..."]),
    judged=J(4,4,4,3,4,4,["purpose evidence","visual evidence","discipline evidence","usability evidence","consistency evidence","originality evidence"]),
    cue=True,                                # is state/meaning carried by something besides color?
    # icon_only_nav=True / hover_only_labels=True cap accessibility at 3
    # cf=[dict(code="CF2", description="...", borderline=False, detail=["..."])]  # manual critical failures
    lessons=["..."], tags=["example"], open_questions=["Creator and source?"])
for r in R:
    json.dump(r, open(os.path.join(out_dir, r['id'] + '.json'), 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    e = r['evaluation']; print(r['id'], e['raw_total'], e['final_total'], e['readiness'])
