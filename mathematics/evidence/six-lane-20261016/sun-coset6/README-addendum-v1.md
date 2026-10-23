# sun-coset6 README addendum v1: run record (host-clock times; every artefact frozen with chmod a-w)

## Freezes, in order

| time (PDT) | artefact | sha256 |
|---|---|---|
| 11:08:42 | README.md, rules-k6-v1.md | 10fc493e…e2bf, 3b135fea…b187 |
| 11:12:19 | rules-k6-v2.md (hereditary Sun), code/core56_engine_v2.py, evidence/engine-v1-to-v2.diff | b45049a0…fa6, f9b83731…8ee5, 4312a5c6…6d90 |
| 11:33:27 | rules-k6-v3.md (XE, N2-6, RPLP, certificate formats), code/core56_engine_v3.py | e25af84f…7130, 01f0de4c…d0cd |
| 11:36:08 | CERT-FORMAT-k6-v1.md | 45f5d73c…68e2 |
| 11:38:24 | proof-k6-lemmas-v1.md, rules-k6-erratum-v1.md | 1fded4df…7573, e3c5e22d…99e7dc |
| 11:46:52 | proof-k6-v1.md (conditional candidate structure) | b8ac51a1…ecd6 |

Engine v1 is code/core56_engine_v1.py (2dbc9d02…73b7). Its chmod a-w ran just before the `date` printed 11:10:27 in the bg_2236 command output.

## Counted runs

| run | engine | rules | result |
|---|---|---|---|
| engine-v1-core34 | v1 | T, K, RLP, P | 111 orbits, 0 survivors (control) |
| engine-v1-core45 | v1 | T, K, RLP, P | 21,150 orbits, 0 survivors (control) |
| engine-v1-core56 | v1 | rules-k6-v1 | 61,124 leaf orbits, **425 survivors** |
| engine-v2-core56 | v2 | + hereditary Sun | 61,124 leaf orbits, **263 survivors**, all of type (0,1,1) or (0,2,1) |
| engine-v3-core56 | v3 | + XE, N2-6, RPLP | 61,124 leaf orbits, **0 survivors**; certificates per CERT-FORMAT-k6-v1 |
| checkB-v1-run1 | same-author self-check | v2 rules | lane SELF-REPORT only; not independent |
| controls-k6-v1-run1, engine-v2-core45, engine-v2-core34 | see the controls script | — | sanity checks only, never gate evidence |

## Control results (sanity only; never gate; same-author code; run 11:48–11:49)

- **C1: reproduction with engine v2 (hereditary rules T, K, RLP, P).**
  - core45: 21,150 orbits, 0 survivors.
  - core34: 111 orbits, 0 survivors.
- **C2: realisable families** (controls-k6-v1-run1). 180 disjoint-coset families with indices 5r_i (r_i pairwise coprime, k ≤ 5) were drawn in Z5, A5 and S5 with seed 20261018. Running the k-generic rules T, K, RLP, P and FH5 on exact data killed none of them.
- **C3: selected mutations** (controls-k6-v2-run1). For each certificate type (K, RLP, PB, FH5, N26, RPLP), the first certified orbit's witness verifies. One single-label mutation then breaks it:
  - K: α(1,2) 1→2;
  - RLP: α(0,3) 2→1;
  - PB: α(0,1) 4→1;
  - FH5: α(0,1) 1→2;
  - N26: α(0,1) 2→1;
  - RPLP: α(0,5) 4→2.

  The K, RLP, PB and FH5 mutants are not T-consistent; the N26 and RPLP mutants are. controls_k6_v1 had required the mutants to be T-consistent and so found no breaking mutation for K or FH5.
- **Hashes:** `evidence/controls-k6.sha256`.

Hashes of the counted-run outputs are in `evidence/engine-v3-run.sha256`.

## Exploratory cells (EXPLORATORY; never counted)

Eval-kernel cells were used at three points:
- **Before the freeze.** Calibration; see README §4.
- **Between 11:20 and 11:30.** Analysis of the 263 v2 survivors. The cells tried a float version of the joint LP, which removed 253 of them. They also checked that a vertex N2-6 argument removes 108, and that the union of the two removes all 263.
- **11:25–11:30.** Smoke tests of engine v3 on 15 survivors.

None of these cells wrote a file, and none is evidence.

## Procedure notes

**Same-author verifier, never run.** A verifier, core56_checkB_v2.py, was written by the lane author. Following the parent's instruction that a separate author must write the independent checker, it was retired unrun to archive/retired-v1/.

**Unused copy.** An unused copy of engine v2 was retired to the same folder.

**Status.** The k6 result is a candidate. No theorem is claimed and no novelty is claimed. See proof-k6-v1.md for the conditions.
