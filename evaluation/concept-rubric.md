# VIXEN Concept Evaluation Rubric (v1.0)

Every concept record is scored with this rubric so scores are comparable across records and across batches. It keeps the seven categories and weights from the project handoff. What this document adds is precise anchors, a split between measured and judged scores, and mechanical rules for critical failures.

## 1. Two kinds of score

- **Measured**: computed from numbers taken from the image (contrast ratios) by a fixed rule. Anyone repeating the measurement should get the same score.
- **Judged**: assigned by the evaluator against written anchors, and must cite observed evidence from the image. A judged score with no evidence is invalid.

Interpretation (what the designer intended, how it was built) is never scored. Only what is visible in the material is scored.

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

**Readiness** (from the final total): **A** = 80 or more, ship with minor adjustments. **B** = 60-79, needs the specific fixes listed. **C** = below 60, needs rethinking.

## 3. Anchors for judged categories

General scale: **0** absent or broken. **1** major problems. **2** noticeable problems. **3** competent and conventional. **4** strong, minor issues. **5** exemplary, hard to improve. A 5 requires that the evaluator cannot name a meaningful improvement; most records should land at 3-4.

| Category | What a 5 looks like | What a 3 looks like | What a 1 looks like |
|---|---|---|---|
| Purpose and requirements | Purpose and audience obvious in seconds; every element serves it | Purpose clear, some elements generic | Purpose unclear or contradicted by content |
| Visual quality and composition | Clear hierarchy, balanced spacing, harmonious color, refined detail | Orderly but unremarkable, or one weak area | Cluttered, unbalanced or crude |
| Discipline-specific correctness | Follows or deliberately and successfully improves the conventions of its sub-discipline; labels and semantics correct | Mostly conventional with a minor misuse or ambiguity | Violates core conventions or misleads |
| Usability and functionality | Affordances clear and the states needed to use it are shown (active, hover/focus, collapsed, loading, error where relevant) | Main path clear, key states missing | Users could not tell what to do |
| Consistency and coherence | Spacing, radii, icon weight, type and color roles consistent; content matches the design | Small inconsistencies | Components feel unrelated |
| Originality and creative direction | A distinct idea that also serves the purpose | Familiar pattern executed well | Template-like, or novelty that harms function |

Novelty without function scores no higher than 3 on originality.

### Discipline checks used for "discipline-specific correctness"
- **Navigation**: current location identifiable; labels or recognizable icons; groups logical; collapsed state defined.
- **Forms/settings**: visible labels (not placeholder-only); label and placeholder agree; one primary action; destructive actions distinguished.
- **Cards**: information order matches user need; one dominant action; stat labels unambiguous.
- **Dashboards/tools**: controls ordered by workflow; async states shown.
- **Explainers**: comparisons use equal framing.
Add checks as new disciplines enter the dataset.

## 4. Accessibility (measured)

Scope is limited to contrast and non-color cues, because those can be measured from an image. Touch-target size, motion, keyboard and screen-reader support cannot be assessed from a static image and are not scored.

Text roles: **primary** = text needed to complete a task (nav labels, button labels, names, form labels). **secondary** = supporting text (captions, timestamps, helper text, placeholders, stat labels). **icon** = non-text UI icons.

Let `P` = lowest primary-text ratio, `S` = lowest secondary-text ratio, `I` = lowest icon ratio (items not present are skipped). `Cue` = whether state or meaning is carried by something besides color (shape, fill, label, position).

| Score | Rule |
|---|---|
| 5 | P >= 4.5 and S >= 4.5 and I >= 3 and Cue |
| 4 | P >= 4.5 and S >= 3 and I >= 3 and Cue |
| 3 | P >= 4.5 but S < 3, or I < 3, or no Cue |
| 2 | 3 <= P < 4.5 |
| 1 | P < 3 |

Special cases: if no text is present, score from icons: 4 if I >= 3 and Cue, else 3 or lower. Navigation that is icon-only, or whose labels appear only on hover, is capped at 3.

**Measurement method**: for each text element, take a box around it; background = dominant color in the box; foreground = mean of the most distant ~4% of pixels; ratio = WCAG relative-luminance contrast. Because images are compressed and thin text is anti-aliased, measured ratios tend to be slightly low. Any value within 0.3 of a threshold (3.0 or 4.5) is flagged `near_threshold` and must be re-checked against the source file or code before being treated as a failure.

## 5. Critical failures

Reported separately from the score. Any critical failure caps the final total at 69.

| Code | Condition | How determined |
|---|---|---|
| CF1 | A primary text or label measures below 3:1 contrast | Measured (flag `borderline` if within 0.4 of 3.0) |
| CF2 | The primary action is not distinguishable from secondary elements | Judged |
| CF3 | Core content is contradicted or misleading (not merely ambiguous) | Judged |
| CF4 | The current state or location cannot be identified in a navigation component | Judged |

## 6. Scope and limits

- Scores describe the concept **as presented**. States, motion and behavior that are not shown are not scored as present, and not assumed absent in the idea itself.
- A score is a calibrated judgment, not an objective measurement of artistic merit. Its value comes from consistency across records.
- When a rubric rule changes, bump `rubric_version` and re-score affected records. Never mix versions in comparisons.

## 7. Calibration

Keep three anchor records per sub-discipline (a low, a middle and a high scorer) and re-read them before scoring a new batch. If a new record seems to deserve a 5 in a category, compare it directly with the existing 4s first.
