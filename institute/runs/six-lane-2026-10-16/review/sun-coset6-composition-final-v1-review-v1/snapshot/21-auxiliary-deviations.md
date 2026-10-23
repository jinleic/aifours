# Parent timestamp and auxiliary-check clarifications, v1

Host clock: 2026-10-18T12:03:00-0700.

## Timestamp corrections (original files unchanged)

The parent wrote two estimated future time phrases. They are inaccurate and must not be used as execution evidence:

- `olson-zs-v2-parent-verdict-v1.md` says “after 11:50 PDT”; recorded filesystem birth and modification times are 2026-10-18 11:45:17 PDT.
- `pa19-m1-retry543-end-notice-v1.md` says “after 11:56 PDT”, with a live-check label “about 11:55”; its recorded birth and modification times are 2026-10-18 11:53:49 PDT. The preceding process observation occurred before that write; its exact clock time was not captured. Do not assign it an exact timestamp.

These are filesystem timestamps read by the parent, not reconstructed execution timestamps. Retry543's audited native completion remains 10:58:27.899 PDT; its clean-settlement receipt and the subsequent zero-PA19-native process observation are unchanged. The M2H pilot PRE-EXEC and fresh prelaunch process checks independently re-establish the operational release.

## k6 auxiliary parent checks

- `check_sun_k6_parent_v1.py` used NumPy integer arrays for independent universe/orbit reconstruction. This does **not** meet transition43's standard-library-only restriction and is disclosed as an auxiliary-check deviation. The separate-author primary checker must be standard-library-only (or a source-hashed compiled helper as authorized by the contract). Do not substitute the auxiliary result for that obligation.
- Its header says RPLP uses integer arithmetic after common-denominator scaling; the actual implementation uses Python `Fraction` throughout. All comparisons are exact, with no floating-point proof decisions.
- The auxiliary parser is written for these four pinned certificate files, not certified as a general fail-closed untrusted-input parser. The separate checker must validate schemas, type set, domains, distinctness, rational entries, keys and coverage explicitly.
- During pre-execution editing, one patch targeted the wrong lines; the malformed draft was repaired before its first execution. No run used that malformed draft. The first executed source hash is in the auxiliary receipt.
- Three exploratory mutation expectations were ill-posed: moving an RLP witness to another genuinely killing vertex; increasing a multiplier within available Farkas slack; and increasing a zero-valued tight-to-zero Farkas column by 0.001. Their unexpected accepts are preserved in `sun-coset6-parent-partial-check-v1/MUTATIONS-v1.json`. Corrected mutations (a non-killing vertex; a column increased to 1.001) were rejected. They are not counted as three detector failures.

## Metadata evidence

```json
[
  {
    "file": "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zs-v2-parent-verdict-v1.md",
    "sha256": "2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734",
    "birth_at_pt": "2026-10-18T11:45:17.961355-07:00",
    "mtime_at_pt": "2026-10-18T11:45:17.961478-07:00"
  },
  {
    "file": "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m1-retry543-end-notice-v1.md",
    "sha256": "7cd962a6591806b86c8df24454c3aa3bc3a4417c3e0ee2ef0511521d8eeef385",
    "birth_at_pt": "2026-10-18T11:53:49.358234-07:00",
    "mtime_at_pt": "2026-10-18T11:53:49.358336-07:00"
  }
]
```
