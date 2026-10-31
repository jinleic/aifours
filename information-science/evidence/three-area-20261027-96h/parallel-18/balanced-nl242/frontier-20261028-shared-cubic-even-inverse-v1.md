# info-6 frontier: fixed shared-cubic even inverse search

Owner InfoBalancedNL242-2-2. Native `/bin/date` before this record: **2026-10-29T03:38:36-0700**. This records one bounded exploratory solver attempt and a successful positive control for its encoding. It is **not** a no-go, target witness, global search, independent review, novelty claim or formal verification.

## Fixed problem

Take the even mod4 residue array g from the pinned shared-cubic formal non-witness. For each nonzero residue, choose the bit b in `k=2g−8b`; residue zero is fixed at k=0. The checker imposes exactly:

* every reduced character-moment equation equivalent to `Walsh(k)≡0 mod128` (93 equations for masks of degree at most three, after eliminating higher-degree equations identically);
* exactly eight magnitude-2 even values, as in that D12/m118 placement;
* even first sum zero.

It does not impose ternary inverse magnitudes beyond divisibility, the odd half, all correlations or the original Boolean caller. The 8,000 ms Z3 run returned **UNKNOWN** after 8.015 s. No exclusion or witness follows. The fixed g is a selected formal object and its UNKNOWN status does not bear on other g, placements, ranks, or the unrestricted target.

## Positive control for the encoding

The separately pinned eight-variable actual balanced ternary half from the full-rank support-floor packet has 62 nonzero inverse values and even half peak 6. The control checker derives its g and bits, verifies all 256 inverse values are 0 or ±128, verifies the full mod64 identity `Walsh(g)−4Walsh(b)`, and verifies the exact 93 reduced moment equations. This shows the encoding accepts a real inverse-compatible half. It is not a nine-variable function or target witness.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-shared-cubic-even-inverse.py` | `b0a52810f0a28e2c41944a411984a8bbe2fc0ee61d554ed6f1afc7adbe9addb7` | 52 | bounded selected-object solver |
| `frontier-20261028-shared-cubic-even-inverse-result.json` | `bc259d9790b4de4b7aa341c7fec35e2a0baba090dd7e662cfad27a307970affb` | 7 | UNKNOWN receipt |
| `frontier-20261028-even-inverse-moment-control.py` | `58c067d8bb98cecedcf39268b498bbbedf52640692bf8ff23d9f84cb7d075c2a` | 47 | encoding positive control |
| `frontier-20261028-even-inverse-moment-control-result.json` | `231b832d4f197a245efce7e1400b5ec0343f762b41e652d09c91624cc3dd2a96` | 10 | positive-control receipt |
| `frontier-20261028-rank2-shared-cubic-placement-result.json` | `7581458a93462f424a4c6f77f468c1b43c84fedce63399790be0df474692400f` | 562 | source formal non-witness |
| `frontier-20261028-fullrank-support-floor-check-result.json` | `5786202aa785762d79e48b69d2f6fb0df4f3ae0fe3a444ffdf2edf86867089c8` | 612 | actual ternary half control source |

**END.**
