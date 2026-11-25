# Learning log

Agents append one JSON line per real adaptation to `adaptation-log.jsonl`. Keep entries factual and short.

```json
{
  "date": "YYYY-MM-DD",
  "task": "short description of what was built",
  "context": {"domain": "", "audience": "", "constraints": []},
  "patterns_used": ["vixen-ui-011"],
  "preserved": ["items from must_preserve that were kept"],
  "changed": ["items from free_to_vary that were changed, and why"],
  "evaluation": {"rubric_version": "1.0", "final_total": 0, "critical_failures": []},
  "what_worked": [],
  "what_failed": [],
  "lesson": "one sentence a future agent can act on",
  "promote": false
}
```

Do not log private user data or proprietary content. A lesson is only promoted into the dataset or knowledge files after review.
