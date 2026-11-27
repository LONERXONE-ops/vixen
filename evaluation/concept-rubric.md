# VIXEN Concept Evaluation Rubric (v1.1)

Every concept record is scored with this rubric so scores are comparable across records and batches. It keeps the seven categories and weights from the project handoff. It adds precise anchors, a split between measured and judged scores, and mechanical rules for critical failures.

## 1. Two kinds of score
- **Measured**: computed from numbers taken from the image (contrast ratios) by a fixed rule.
- **Judged**: assigned against written anchors and must cite observed evidence. A judged score with no evidence is invalid.

Interpretation (designer intent, how it was built) is never scored. Only what is visible is scored.

## 2. Formula
Each category is scored 0-5. Points = (score / 5) x weight. Raw total = sum of points (0-100).

| Category | Weight | Basis |
|---|---|---|
| Purpose and requirements | 15 | judged |
| Visual quality and composition | 20 | judged |
| Discipline-specific correctness | 20 | judged |
| Usability and functionality | 15 | judged |
| Consistency and coherence | 10 | judged |
| Originality and creative direction | 10 | judged |
| Accessibility and inclusivity | 10 | **measured** |

**Final total** = raw total, capped at 69 if any critical failure is present (section 5).
**Readiness**: **A** = 80 or more, ship with minor adjustments. **B** = 60-79, needs the specific fixes listed. **C** = below 60, rethink.

## 3. Anchors for judged categories
General scale: **0** absent or broken. **1** major problems. **2** noticeable problems. **3** competent and conventional. **4** strong, minor issues. **5** exemplary, hard to improve. A 5 requires that the evaluator cannot name a meaningful improvement; most records should land at 3-4.

| Category | What a 5 looks like | What a 3 looks like | What a 1 looks like |
|---|---|---|---|
| Purpose and requirements | Purpose and audience obvious in seconds; every element serves it | Purpose clear, some elements generic | Purpose unclear or contradicted by content |
| Visual quality and composition | Clear hierarchy, balanced spacing, harmonious color, refined detail | Orderly but unremarkable, or one weak area | Cluttered, unbalanced or crude |
| Discipline-specific correctness | Follows, or deliberately and successfully improves, the conventions of its sub-discipline; labels and semantics correct | Mostly conventional with a minor misuse or ambiguity | Violates core conventions or misleads |
| Usability and functionality | Affordances clear and the states needed to use it are shown (active, hover/focus, collapsed, loading, error where relevant) | Main path clear, key states missing | Users could not tell what to do |
| Consistency and coherence | Spacing, radii, icon weight, type and color roles consistent; content matches the design | Small inconsistencies | Components feel unrelated |
| Originality and creative direction | A distinct idea that also serves the purpose | Familiar pattern executed well | Template-like, or novelty that harms function |

Novelty without function scores no higher than 3 on originality.

### Discipline checks for "discipline-specific correctness"
- **Navigation**: current location identifiable; labels or recognizable icons; logical groups; collapsed state defined.
- **Forms/settings**: visible labels (not placeholder-only); label and placeholder agree; one primary action; destructive actions distinguished.
- **Cards**: information order matches user need; one dominant action; stat labels unambiguous (unit inside the value); text in core labels correct.
- **Dashboards/tools**: controls ordered by workflow; async states shown.
- **Landing pages**: responds to the viewport; headline states the offer; one primary action.
- **Explainers/comparisons**: equal framing; one variable changed.
Add checks as new disciplines enter the dataset.

## 4. Accessibility (measured)
Scope: contrast and non-color cues only. Touch-target size, motion, keyboard and screen-reader support cannot be assessed from a static image and are not scored.

Roles: **primary** = text needed to complete a task (nav labels, button labels, names, form labels). **secondary** = supporting text (captions, timestamps, helper text, placeholders, stat labels, handles). **icon** = non-text UI icons.

Let `P` = lowest primary-text ratio, `S` = lowest secondary-text ratio, `I` = lowest icon ratio (absent items are skipped), using `ratio_low`. `Cue` = state or meaning is carried by something besides color.

| Score | Rule |
|---|---|
| 5 | P >= 4.5 and S >= 4.5 and I >= 3 and Cue |
| 4 | P >= 4.5 and S >= 3 and I >= 3 and Cue |
| 3 | P >= 4.5 but S < 3, or I < 3, or no Cue |
| 2 | 3 <= P < 4.5 |
| 1 | P < 3 |

If no text is present, score from icons: 4 if I >= 3 and Cue, otherwise 3 or lower. Navigation that is icon-only, or whose labels appear only on hover, is capped at 3.

### Measurement method (v1.1)
- Draw a box around each text element; background = dominant color in the box.
- `ratio_low` (conservative) = contrast using the mean of the most distant ~4% of pixels as the text color.
- `ratio` (best estimate) = contrast using the mean of the most distant ~1.5%. If the text sits on a saturated background (HSV saturation >= 0.4) and its peak pixels (the most distant ~0.5%, at least 3 pixels) appear near-white (all channels >= 170) or near-black (all <= 60), the text is assumed to be pure white or black, because anti-aliasing of small text otherwise understates contrast. In that case `ratio_low` equals `ratio`.
- Gradient and photo backgrounds are measured one text line at a time.
- Scores use `ratio_low`. A score is reported with a note when the best estimate would give a different score.
- Values within 0.4 of a threshold (3.0 or 4.5) are `near_threshold` and must be re-checked in the source file or code before being treated as failures.

## 5. Critical failures
Reported separately from the score. Any critical failure caps the final total at 69.

| Code | Condition | How determined |
|---|---|---|
| CF1 | A primary text or label has a best-estimate contrast below 3:1 | Measured. Flagged `borderline` if all offending values are within 0.4 of 3.0 |
| CF2 | The primary action is not distinguishable from secondary elements | Judged |
| CF3 | Core content is contradicted or misleading (not merely ambiguous) | Judged |
| CF4 | The current state or location cannot be identified in a navigation component | Judged |

Primary text whose conservative value is below 3 but whose best estimate is 3 or more goes on a `cf1_watchlist` (no cap).

## 6. Scope and limits
- Scores describe the concept **as presented** in a static image. States, motion and behavior that are not shown are not scored as present.
- A score is a calibrated judgment, not an objective measure of artistic merit. Its value comes from consistency across records.
- When a rule changes, bump `rubric_version` and re-score affected records. Never mix versions in comparisons.

## 7. Calibration
Keep three anchor records per sub-discipline (low, middle, high) and re-read them before scoring a new batch. If a record seems to deserve a 5 in a category, compare it with the existing 4s first.
