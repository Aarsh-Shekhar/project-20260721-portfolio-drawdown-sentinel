# Data Quality Guardrail

Domain: finance

This note records an implementation detail for Portfolio Drawdown Sentinel. The current operating
threshold is `0.42` and review should happen within `12` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
