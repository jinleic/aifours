# v18 manifest-scope erratum e1

```json
{
  "schema_version": 1,
  "observed_clock_before_creation": "2026-10-24T05:12:32-0700 PDT",
  "type": "MANIFEST_SCOPE_ERRATUM",
  "erratum_id": "v18-e1",
  "affects": "peer-review-wave-eighteen-v18.json",
  "affects_sha256": "3a38133485eae5493fc5e29a9ba87a3668cca7391758f810f67f2937532d3b3c",
  "discovered_by": "MathSemigroup actual ACK 2026-10-24T05:11:40-0700",
  "error": "The assignment scope text wrote active-sizes(4,4,4,5). That is the v4445 profile. The v4455 stratum has active sizes (4,4,5,5): exactly TWO four-value axes and TWO five-value axes, consistent with the candidate title, the two four-value axes P/Q in the placement-rigidity claims, both five-profile types, and lambda=1 kappa1=60/kappa2=49.",
  "correction": "Read every occurrence of active-sizes(4,4,4,5) in the v18 scope as active-sizes(4,4,5,5). All other scope terms are unchanged and unambiguous: h12/t24/e0/support48, every placement and arbitrary complex phases up to party permutation, GLOBAL necessary-structure + P/P-exclusion scope, the same six exclusions and non-claims. The original manifest is NOT edited; candidate bytes remain frozen at 47150687f15b8271fa153ea04be0eacc530a7f54713422fa55f423f4e8e07d78.",
  "binding": "This erratum is part of the v18 assignment; the reviewer proceeds under it. No mathematical verdict, source change or deadline change."
}
```

The single character-level correction: **active-sizes(4,4,5,5)**, not (4,4,4,5), throughout the v18 scope text. Discovered by the reviewer before any mathematical work; manifest left immutable.
