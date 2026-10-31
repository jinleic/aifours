# Validated exact SAT model for Tuscan-2 squares, complete cube splitting, and campaign status

Native `/bin/date` observed before writing: **Wed Oct 28 19:33:57 PDT 2026**. **WRITTEN lemmas + exact computation.** This packet documents a validated encoding and the current bounded search status for the original target T2(11); no T2(11) witness and no T2(11) nonexistence is claimed. Results for orders 4–9 are calibrations of the method on adjacent orders, explicitly not substitutes for the target. UNSAT statuses are **unverified** unless a DRAT check is cited; UNKNOWN is never exclusion.

## 1. Model and three normalization lemmas

`frontier-20261028-tuscan2-channel-sat-v1.py` (SHA-256 `2c675e63cc0bab9e9b8fd6358ca12defcaedd25903cc9f5cdfcea1e69cdf2b1e`) encodes linear rows with position variables x[r][c][v], successor variables s[r][a][b], distance-two variables t[r][a][b], exact channelling between them, per-row exactly-one successor/predecessor and distance-two successor/predecessor constraints, the redundant implications s(a,b)∧s(b,c)→t(a,c), D1 exactly-once and D2 at-most-once per ordered pair. No Latin-column or circular constraint is used.

**Lemma 1 (unique endpoints).** In any T1(n) array, every symbol a is last in exactly one row and first in exactly one row: a occurs once per row and has an outgoing D1 event in every row where it is not last; D1 exactness gives exactly n−1 outgoing events, so it is last in exactly one row; symmetrically for first.

**Lemma 2 (normalization).** Relabelling symbols and permuting rows preserve the T2 property. Relabel so a chosen row is 0,1,…,n−1 and sort rows by their (distinct, Lemma 1) first symbols. Thus every T2(n) array has a normalized copy with row 0 = identity and row r starting with r. The model fixes these unit facts, and adds the redundant (Lemma 1) last-column permutation constraint.

**Lemma 3 (reversal cut).** For a normalized array A, reverse every row and relabel x↦n−1−x. Row 0 becomes the identity again, rows can be re-sorted by start, and the result A* is normalized; global reversal maps D1 and D2 events bijectively ((a,b)↦(b,a)) so A* is T2 iff A is. Its end permutation is E*=cE^{−1}c with c(x)=n−1−x. A↦A* is an involution, so requiring E ≤lex E* (non-strict, ties kept) retains at least one member of every pair and preserves satisfiability. The model optionally encodes this cut; a separately written in-kernel Z3 projection audit matched the cut on 100 random end permutations and an actual table (`frontier-20261028-reversal-cut-audit-v1.json`, SHA-256 `7b0dcc254d21d86fdfc0368c6964a238f24c789945111ea5035e0027e0712900`).

**Lemma 4 (complete second-row cubes).** In a normalized T2 array, row 1 starts with 1, contains none of row 0's D1 events (i,i+1) or D2 events (i,i+2), and does not end with n−1. `frontier-20261028-cube-driver-v1.py` (SHA-256 `97238728a0eee7208e75bacb21bfd69ef2537d910c4755058e86c9a14d3f1d48`) enumerates exactly all permutations with these necessary properties (120, 807, 6,298, 55,668, 549,012 for n=7,…,11), so every normalized solution lies in exactly one cube. Each cube adds the n unit facts for row 1.

## 2. Calibration against known counts (Handbook Table 62.26: standard-form T2 counts 1,1,0,6 for n=4,6,7,8)

| n | Result | Evidence |
|---|---|---|
| 4, 6 | SAT; independent general checker confirms T2 | runs `frontier-20261028-channel-n4/n6-run-01.json` |
| 7 | UNSAT in 1 s, **DRAT VERIFIED** by owned drat-trim (built from source SHA-256 `d834b649…a0c2ee`); all 120 cubes also UNSAT (≤70 ms each) | CNF `6f651d2f…bb61`, proof `ca19eb62…559c`, checker log `984feb90…a0924`; cubes `frontier-20261028-cubes-n7-all.jsonl` `add94c15…11bb` |
| 8 | SAT in 58 s; blocking-clause enumeration of the uncut model gives **exactly 6** normalized squares, then UNSAT (unverified); the 807-cube run gives exactly 6 SAT cubes and the **same 6 arrays** | `frontier-20261028-channel-n8-enumeration.json` `5a77f081…ff00`; `frontier-20261028-cubes-n8-all.jsonl` `93a2fa3d…2fb9` |

The n=8 agreement of two independent methods with the published count 6 is strong evidence that the model neither over- nor under-constrains. A simulated annealing search over unconstrained rows (`frontier-20261028-tuscan2-anneal-v1.cpp`, SHA-256 `145fed19…7770`) also found an independently checked T2(8) in 27.5 s.

## 3. Status for n=9 (calibration) and the target n=11

- **n=9:** one 30-minute Kissat run UNKNOWN (`frontier-20261028-channel-n9-kissat-s1.json` `3206a0dc…a612ba74`); a 25-minute annealing run reached D1 excess 2, D2 excess 0 (`frontier-20261028-anneal-n9-run-01.json` `0f8db604…ba2e`), not a square. A 20-cube sample of the complete 6,298-cube split was entirely UNSAT (17–104 s each; `frontier-20261028-cubes-n9-sample-000.jsonl` `e6ca37b0…4d96`); a probe cube proof (33.7 MB) was DRAT VERIFIED with check time ≈ solve time. A full cube campaign is running; until every cube is resolved and verified, T2(9) remains open here.
- **n=11 (target):** four ~58-minute runs (Kissat with/without reversal cut, Kissat `--sat`, CaDiCaL) are all UNKNOWN (`…n11-kissat-s1.json` `7ea97adb…29ce`, `…n11-kissat-s2.json` `0faa8af4…786e`, `…n11-kissat-sat-s3.json` `6fb51571…4c4f`, `…n11-cadical-s1.json` `1c451742…920e`). The complete n=11 second-row split has 549,012 cubes; exhaustive treatment is not feasible in this round at the measured n=9 per-cube cost. Structured sub-routes tried: Vatican T2(10) plus symbol insertion UNSAT in 95 ms (unverified, `frontier-20261028-insert-vatican-run-01.json` `e6609e2b…4a99`); symmetric circular 11×12 types q=3 with 5/8/11 fixed rows and q=2 with 7/9/11 fixed rows UNSAT (unverified), the other types UNKNOWN; regular circular actions excluded by the corrected written theorem (erratum `6e64aa10…1c2c`).

Interpretation: by heuristic configuration counting, T2(11) solutions, if they exist, are extremely sparse among T1(11) arrays; the absence of a witness in these bounded runs is not evidence of nonexistence. No novelty or formal/kernel claim is made.
