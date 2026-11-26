#!/usr/bin/env python3
"""Check that every record in dataset/records is complete and internally consistent.
Run this BEFORE delivering any zip:  python tools/validate_records.py dataset/records
Exit code 1 if any record has errors. Schema v1 records are reported as 'needs upgrade'."""
import sys, json, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate import _acc, W, RUBRIC_VERSION
CURRENT_SCHEMA = "2.1"
REQ = {
 "2.0": ["id","title","type","discipline","category","source_files","creator","source","license","attribution_status","measured","observed","interpretation","concept_work","pattern","evaluation","lessons","tags"],
 "2.1": ["components","system","build","related_optional"],
}
def required(ver):
    r = list(REQ["2.0"])
    if ver == "2.1": r += ["components","system","build"]
    return r
def check(rec):
    errs = []; ver = rec.get("schema_version", "1.0")
    if ver == "1.0": return ver, ["schema v1: no evaluation/pattern/components; needs upgrade"]
    for f in required(ver):
        if f not in rec: errs.append(f"missing field: {f}")
    ev = rec.get("evaluation")
    if ev:
        if ev.get("rubric_version") != RUBRIC_VERSION: errs.append(f"rubric_version {ev.get('rubric_version')} != {RUBRIC_VERSION}")
        sc = ev.get("scores", {})
        if set(sc) != set(W): errs.append("scores must contain exactly the 7 categories")
        else:
            pts = round(sum(v["points"] for v in sc.values()), 1)
            if abs(pts - ev["raw_total"]) > 0.11: errs.append(f"raw_total {ev['raw_total']} != sum of points {pts}")
            for c, v in sc.items():
                if v["weight"] != W[c]: errs.append(f"{c}: weight {v['weight']} != {W[c]}")
                if abs(round(v["score"] / 5 * W[c], 1) - v["points"]) > 0.11: errs.append(f"{c}: points do not match score")
                if c != "accessibility" and not v.get("evidence"): errs.append(f"{c}: judged score without evidence")
            cf = ev.get("critical_failures", [])
            exp = min(ev["raw_total"], 69.0) if cf else ev["raw_total"]
            if abs(exp - ev["final_total"]) > 0.11: errs.append(f"final_total {ev['final_total']} != expected {exp}")
            band = "A" if ev["final_total"] >= 80 else ("B" if ev["final_total"] >= 60 else "C")
            if band != ev["readiness"]: errs.append(f"readiness {ev['readiness']} != {band}")
            samples = rec.get("measured", {}).get("contrast_samples", [])
            if samples:
                a = _acc(samples, True, False, False, "ratio_low")[0]
                stored = sc["accessibility"]["score"]
                if stored > a and not any("Capped" in e or "cue" in e for e in sc["accessibility"]["evidence"]):
                    errs.append(f"accessibility {stored} higher than recomputed {a}")
                bad = [s for s in samples if s["role"] == "primary" and s["ratio"] < 3.0]
                if bool(bad) != any(c.get("code") == "CF1" for c in cf): errs.append("CF1 flag does not match samples")
    return ver, errs
if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "dataset/records"
    bad = 0; rows = []
    for f in sorted(glob.glob(os.path.join(d, "vixen-*.json"))):
        rec = json.load(open(f, encoding="utf-8")); ver, errs = check(rec)
        rows.append((rec.get("id", f), ver, errs))
        if errs and ver != "1.0": bad += 1
    for i, ver, errs in rows:
        status = "OK" if not errs else ("UPGRADE" if ver == "1.0" else "ERROR")
        print(f"{i}  schema {ver:<4} {status}" + ("" if not errs else "  - " + "; ".join(errs)))
    n_cur = sum(1 for _, v, e in rows if v == CURRENT_SCHEMA and not e)
    print(f"\n{len(rows)} records; {n_cur} fully valid at schema {CURRENT_SCHEMA}; "
          f"{sum(1 for _,v,_ in rows if v=='1.0')} at v1.0; {sum(1 for _,v,_ in rows if v=='2.0')} at v2.0; {bad} with errors")
    sys.exit(1 if bad else 0)
