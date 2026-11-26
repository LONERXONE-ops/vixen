"""VIXEN evaluation builder (rubric v1.1).
Builds the `evaluation` block and `measured.contrast_samples` for a record from contrast samples and judged scores.
Used by generator scripts: rec,J,R = make(base_id, contrast_json) ; see tools/README.md for a full example.
"""
import json
W = {"purpose":15,"visual":20,"discipline":20,"usability":15,"consistency":10,"originality":10,"accessibility":10}
RUBRIC_VERSION="1.1"
CMETHOD = ("Estimated from compressed images. Background = dominant color in a box around the text. ratio_low = conservative estimate (mean of the most distant ~4% of pixels). "
           "ratio = best estimate (mean of the most distant ~1.5% of pixels; for text on a saturated background that appears near-white or near-black, the text is assumed pure white or black, because anti-aliasing of small text otherwise understates the contrast). "
           "Accessibility scores use ratio_low; critical failure CF1 uses ratio. Gradient or photo backgrounds are measured one text line at a time. Values within 0.4 of a threshold are borderline and should be verified in the source file.")
PMETHOD = "Median-cut quantization of the supplied image plus saturated-pixel hue medians. Approximate (JPEG). Items marked 'approx' were judged by eye."

def _acc(samples, cue, icon_only_nav, hover_only_labels, key):
    prim=[s[key] for s in samples if s['role']=='primary']; sec=[s[key] for s in samples if s['role']=='secondary']; ico=[s[key] for s in samples if s['role']=='icon']
    pm=min(prim) if prim else None; sm=min(sec) if sec else None; im=min(ico) if ico else None
    if pm is None: sc = 4 if (im is not None and im>=3 and cue) else (3 if (im is not None and im>=3) else 2)
    elif pm<3: sc=1
    elif pm<4.5: sc=2
    else:
        ok_i=(im is None or im>=3)
        if (sm is None or sm>=4.5) and ok_i and cue: sc=5
        elif (sm is None or sm>=3) and ok_i and cue: sc=4
        else: sc=3
    capped=False
    if (icon_only_nav or hover_only_labels) and sc>3: sc=3; capped=True
    return sc,pm,sm,im,capped

def build_eval(samples_raw, judged, cue, cf_manual=(), icon_only_nav=False, hover_only_labels=False):
    samples=[]
    for s in samples_raw:
        s=dict(s); s['near_threshold']=any(abs(s['ratio']-t)<=0.4 for t in (3.0,4.5)); s.pop('old_ratio',None); samples.append(s)
    a,pm,sm,im,capped=_acc(samples,cue,icon_only_nav,hover_only_labels,'ratio_low')
    a_est=_acc(samples,cue,icon_only_nav,hover_only_labels,'ratio')[0]
    f=lambda v:'n/a' if v is None else v
    aev=f"Scored on conservative values: primary text min {f(pm)}:1; secondary text min {f(sm)}:1; icon min {f(im)}:1; non-color state cue: {cue}."
    if capped: aev+=" Capped at 3: meaning depends on icon recognition or hover-only labels."
    if a_est!=a: aev+=f" Using best-estimate values the score would be {a_est}; the measurement is within error of a threshold."
    scores={}
    for cat,(sc,ev) in judged.items():
        scores[cat]=dict(score=sc,weight=W[cat],points=round(sc/5*W[cat],1),evidence=[ev] if isinstance(ev,str) else ev,basis="judged")
    scores["accessibility"]=dict(score=a,weight=10,points=round(a/5*10,1),evidence=[aev],basis="computed from measured contrast + cue flag (scope: contrast and non-color cues only; touch targets, motion and screen-reader support cannot be assessed from a static image)")
    raw=round(sum(v['points'] for v in scores.values()),1)
    cfs=[]
    bad=[s for s in samples if s['role']=='primary' and s['ratio']<3.0]
    if bad:
        cfs.append(dict(code="CF1",description="A primary text/label measures below 3:1 contrast (best estimate)",borderline=all(s['ratio']>=2.6 for s in bad),detail=[f"{s['element']}: {s['ratio_low']}-{s['ratio']}:1" for s in bad]))
    watch=[s for s in samples if s['role']=='primary' and s['ratio_low']<3.0<=s['ratio']]
    for c in cf_manual: cfs.append(c)
    total=min(raw,69.0) if cfs else raw
    ready="A" if total>=80 else ("B" if total>=60 else "C")
    ev=dict(rubric_version=RUBRIC_VERSION,scores=scores,raw_total=raw,critical_failures=cfs,cf1_watchlist=[f"{s['element']}: {s['ratio_low']}-{s['ratio']}:1 (conservative value below 3, best estimate above)" for s in watch],
        final_total=total,cap_applied=bool(cfs) and raw>69,readiness=ready,
        readiness_key="A = ship with minor adjustments (>=80, no critical failure); B = needs specific fixes (60-79); C = rethink (<60)",
        scope="Scored as presented in a static image. States, motion and behavior that are not shown are not scored as present.")
    return ev,samples

def J(p,v,d,u,c,o,ev):
    return {"purpose":(p,ev[0]),"visual":(v,ev[1]),"discipline":(d,ev[2]),"usability":(u,ev[3]),"consistency":(c,ev[4]),"originality":(o,ev[5])}

def make(base, contrast):
    R=[]
    def rec(key, **kw):
        kw['id']=f"vixen-ui-{base+int(key):03d}"
        kw.update(schema_version=kw.pop('schema_version','2.1'),type="concept",discipline="ui-design",creator=None,source=None,publication_date=None,license="unknown",attribution_status="needs-user-input")
        ev,samples=build_eval(contrast[key], kw.pop('judged'), kw.pop('cue'), kw.pop('cf',()), kw.pop('icon_only_nav',False), kw.pop('hover_only_labels',False))
        pal=kw.pop('palette'); roles=kw.pop('roles')
        kw['measured']=dict(palette_method=PMETHOD,palette=pal,color_roles=roles,contrast_method=CMETHOD,contrast_samples=samples)
        kw['evaluation']=ev; R.append(kw)
    return rec,J,R
