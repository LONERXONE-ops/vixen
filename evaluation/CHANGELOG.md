# Rubric changelog

## v1.1
- Contrast measurement now reports `ratio_low` (conservative) and `ratio` (best estimate). v1.0 used a single value that tended to understate contrast for small text on colored backgrounds.
- Accessibility scores use `ratio_low`; CF1 uses `ratio`. A `cf1_watchlist` records primary text that is below 3:1 conservatively but above it by best estimate.
- Gradient and photo backgrounds are measured per text line.
- Re-scored batch 02 under v1.1. Changes: vixen-ui-019 accessibility 4 -> 3 (the first line of the right bio sits on a mid-grey blurred area at about 2.7-3.1:1), final 79 -> 77; vixen-ui-017 CF1 is now flagged borderline (white on orange about 2.8:1); vixen-ui-018 CF1 moved to the watchlist (primary labels about 2.8-3.3:1). All other batch 02 scores are unchanged.

## v1.0
- Initial rubric (batch 02).
