# January 2026 Reconciliation Report

## Scope

This comparison focuses on January 2026 only.

- Source files:
  - `pbi.xlsx`
  - `synapse.xlsx`
- Scope limited to shared company codes present in both extracts for January 2026:
  - `EA01`
  - `EA11`
  - `EA12`
  - `EA18`
  - `EA22`
  - `EA37`
- Measures used for reconciliation:
  - `MTD&0T_FPIE&Actual`
  - `MTD&0T_FPIE&Budget`

Calculated columns that exist only in `pbi.xlsx` were excluded from the comparison.

## Normalization Applied

- Compared on `Reporting date = 2026-01`
- Treated blank and `NULL` values in account keys as equivalent
- Focused on shared business columns and the two measure columns only

## Executive Summary

At `company code + level 3 key`, January 2026 is largely reconciled.

- 4 company codes reconcile cleanly across all level 3 buckets:
  - `EA01`
  - `EA11`
  - `EA12`
  - `EA22`
- 2 company codes still have open differences:
  - `EA18`
  - `EA37`

After normalization, only 2 level 3 exceptions remain in total.

## Level 3 Reconciliation

This is the primary comparison view for sharing outcomes.

| Company Code | Level 3 Key | PBI Rows | Synapse Rows | Row Diff | PBI Actual | Synapse Actual | Actual Diff | PBI Budget | Synapse Budget | Budget Diff | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| EA18 | blank / NULL bucket | 178 | 183 | -5 | 2,063,746.08 | 2,274,090.12 | -210,344.04 | 1,515,111.07 | 1,515,111.07 | 0 | Investigate |
| EA37 | blank / NULL bucket | 151 | 169 | -18 | 579,579.69 | 2,379,865.35 | -1,800,285.66 | 0 | 0 | 0 | Investigate |

Interpretation:

- `Budget` reconciles for both remaining exceptions
- Remaining variance is entirely driven by `Actual`
- Both exceptions sit in the normalized blank / `NULL` level 3 bucket

## Matched Companies

The following company codes have no remaining January 2026 differences after normalization at the `company code + level 3 key` level:

- `EA01`
- `EA11`
- `EA12`
- `EA22`

## Level 4 Deep Dive

Level 4 is retained as a deeper investigation layer for the two open exceptions.

### EA18

| Level 4 Key | PBI Rows | Synapse Rows | Row Diff | PBI Actual | Synapse Actual | Actual Diff | PBI Budget | Synapse Budget | Budget Diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| KS00/24014290 | 0 | 1 | -1 | 0 | 210,344.04 | -210,344.04 | 0 | 0 | 0 |
| KS00/24014291 | 0 | 3 | -3 | 0 | 0 | 0 | 0 | 0 | 0 |
| KS00/24014292 | 0 | 1 | -1 | 0 | 0 | 0 | 0 | 0 | 0 |

EA18 deep-dive note:

- `Synapse` contains 5 extra rows not present in `PBI`
- Only `KS00/24014290` drives the `Actual` variance
- The other extra rows affect row count only

EA18 record view:

| Source | Reporting Date | Level 4 Key | Level 4 Name | Profit Center | Actual | Budget |
| --- | --- | --- | --- | --- | ---: | ---: |
| Synapse | 2026-01-01 | KS00/24014290 | OCBC SGD-368001-Main | CORPGG | 210,344.04 | 0 |
| Synapse | 2026-01-01 | KS00/24014291 | OCBC SGD-368001-Inc | CORPGG | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014291 | OCBC SGD-368001-Inc | RTCM00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014291 | OCBC SGD-368001-Inc | RTLL00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014292 | OCBC SGD-368001-Out | CORPGG | 0 | 0 |

PBI record view:

- No January 2026 records found in `PBI` for `KS00/24014290`, `KS00/24014291`, or `KS00/24014292`

### EA37

| Level 4 Key | PBI Rows | Synapse Rows | Row Diff | PBI Actual | Synapse Actual | Actual Diff | PBI Budget | Synapse Budget | Budget Diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| KS00/24014280 | 0 | 3 | -3 | 0 | 1,623,265.28 | -1,623,265.28 | 0 | 0 | 0 |
| KS00/24014285 | 0 | 2 | -2 | 0 | 189,006.46 | -189,006.46 | 0 | 0 | 0 |
| KS00/24014281 | 0 | 5 | -5 | 0 | -10,572.27 | 10,572.27 | 0 | 0 | 0 |
| KS00/24014282 | 0 | 5 | -5 | 0 | -1,413.81 | 1,413.81 | 0 | 0 | 0 |
| KS00/24014286 | 0 | 3 | -3 | 0 | 0 | 0 | 0 | 0 | 0 |

EA37 deep-dive note:

- `Synapse` contains 18 extra rows not present in `PBI`
- The largest `Actual` drivers are `KS00/24014280` and `KS00/24014285`
- The remaining listed accounts are smaller `Actual` differences or row-count-only differences

EA37 record view:

| Source | Reporting Date | Level 4 Key | Level 4 Name | Profit Center | Actual | Budget |
| --- | --- | --- | --- | --- | ---: | ---: |
| Synapse | 2026-01-01 | KS00/24014280 | OCBC-SGD-767001-Main | CORPGG | 1,623,265.28 | 0 |
| Synapse | 2026-01-01 | KS00/24014280 | OCBC-SGD-767001-Main | RTLL00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014280 | OCBC-SGD-767001-Main | RTMC00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014281 | OCBC-SGD-767001-Inc | CORPGG | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014281 | OCBC-SGD-767001-Inc | RTCM00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014281 | OCBC-SGD-767001-Inc | RTCP00 | -10,572.27 | 0 |
| Synapse | 2026-01-01 | KS00/24014281 | OCBC-SGD-767001-Inc | RTLL00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014281 | OCBC-SGD-767001-Inc | RTMC00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014282 | OCBC-SGD-767001-Out | CORPGG | -1,413.81 | 0 |
| Synapse | 2026-01-01 | KS00/24014282 | OCBC-SGD-767001-Out | RTCM00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014282 | OCBC-SGD-767001-Out | RTCP00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014282 | OCBC-SGD-767001-Out | RTLL00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014282 | OCBC-SGD-767001-Out | RTMC00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014285 | OCBC-SGD-141001-Main | CORPGG | 189,006.46 | 0 |
| Synapse | 2026-01-01 | KS00/24014285 | OCBC-SGD-141001-Main | RTLL00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014286 | OCBC-SGD-141001-Inc | CORPGG | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014286 | OCBC-SGD-141001-Inc | RTCM00 | 0 | 0 |
| Synapse | 2026-01-01 | KS00/24014286 | OCBC-SGD-141001-Inc | RTLL00 | 0 | 0 |

PBI record view:

- No January 2026 records found in `PBI` for `KS00/24014280`, `KS00/24014281`, `KS00/24014282`, `KS00/24014285`, or `KS00/24014286`

## Overall Conclusion

For January 2026, the reconciliation result is:

- clean at `company code + level 3 key` for `EA01`, `EA11`, `EA12`, and `EA22`
- open only for `EA18` and `EA37`
- `Budget` fully aligned for the remaining exceptions
- unresolved differences driven by extra `Synapse` rows affecting `Actual`

## Suggested Follow-Up

1. Validate whether level 4 accounts `KS00/24014290`, `KS00/24014291`, `KS00/24014292` should exist for `EA18` in January 2026.
2. Validate whether level 4 accounts `KS00/24014280`, `KS00/24014285`, `KS00/24014281`, `KS00/24014282`, `KS00/24014286` should exist for `EA37` in January 2026.
3. Confirm whether these rows are expected in Synapse only, or whether PBI is filtering/excluding them.
4. If needed, trace these account keys back to the source query or transformation rules used by both extracts.
