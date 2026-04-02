# Jan 2026 Reconciliation Summary

January 2026 was reconciled between `pbi.xlsx` and `synapse.xlsx` at the shared company scope.

## Result

- Fully matched: `EA01`, `EA11`, `EA12`, `EA22`
- Exceptions remain: `EA18`, `EA37`

## Exception Summary

| Company | Row Diff | Actual Diff | Budget Diff | Comment |
| --- | ---: | ---: | ---: | --- |
| EA18 | -5 | -210,344.04 | 0 | Extra rows exist in Synapse only |
| EA37 | -18 | -1,800,285.66 | 0 | Extra rows exist in Synapse only |

## Key Detail

The remaining differences are not broad data quality issues. They are concentrated in a small set of level 4 keys that appear in `synapse.xlsx` but do not appear in `pbi.xlsx`.

- `EA18`: `KS00/24014290`, `KS00/24014291`, `KS00/24014292`
- `EA37`: `KS00/24014280`, `KS00/24014281`, `KS00/24014282`, `KS00/24014285`, `KS00/24014286`

## Interpretation

- `Budget` is fully aligned for the open exceptions.
- The variance is driven by `Actual` only.
- These keys recur across multiple months in Synapse and are absent from PBI, which suggests a systematic inclusion or exclusion difference between the two pipelines rather than a one-off January issue.

## Next Step

Validate these exact keys in `brnz.sapbw_zsfiva02_q005` for January 2026 to determine whether the difference originates in the Synapse source extract or in the downstream transformation.
