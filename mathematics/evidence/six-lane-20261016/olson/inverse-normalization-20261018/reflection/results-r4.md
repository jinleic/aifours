# Results r4: final continuation package of the reflection desk, after host clock 2026-10-18T12:27:47-0700

Owner OlsonReflectionRigidity.  This updates results-r3.md (8e464d54...476a), which is kept unchanged and whose Secs. A-F stay
valid.  The additions follow.  Finite aids are not premises.

## Additions since results-r3

1. **Lemma EDGE** (proof-B0Sedge-r2.md; written and unreviewed; r1 was an unsent draft).
   - B = 0 has no avoider with kappa = (p + 1)/2 and R in {2p - 2, 2p - 1}.
   - Consequence: B0S-CJ''' holds under R >= 4 kappa - 4 alone, and the hypothesis 2 kappa <= p - 1 of REFL-B0 can be dropped.
   - This closes gap (b), pending review.
2. **REFL-B0-r3** (proof-REFL-B0-r3.md).  A wording-only revision of r2: "no imposed bound o_F <= p"; o_F = 2p - R + 2 kappa.
   r2's review is ongoing, and Main will bind r3 by reconciliation.
3. **notes-gapA-r2.md.**
   - E17: in the gap-(a) cell (29, 7, 29), no random all-ones arrangement has (2HA), yet every interval-feasible leaf has J = 0
     and c = 0.
   - Lemma HOT: J >= 1 forces a light interval with c >= 1.  If J = 1 there is a single hot spot, and every interval avoiding it
     has c = 0.
4. **notes-B1-cfunc-r1.md.**  The B >= 1 c-function: index E = D + B, non-additive, with pair indices summing to 2R - B.  The
   no-small-pair case of (B_B) needs 2R >= 2p + B - 1.  MXG's uses of k <= p are the real obstruction.

## Open gaps (B = 0, k >= p + 1), final

(a) Numerical Corollary-2 failures under R >= 4 kappa - 4: Delta >= 2, p < kappa + 5 Delta - 5,
    (p + 10)/6 < kappa < (2p + 5)/7.  E17 suggests interval-level SIGMA still holds there.
(b) Closed by Lemma EDGE, pending review.
(c) Deep IIIa: 2 kappa < R <= 4 kappa - 5.
(d) IIIb: R <= 2 kappa, i.e. k >= 2p.
Untouched: B >= 1 with k >= p + 1.

## Hashes of the added files (sha256)

* proof-B0Sedge-r1.md  893c04ff677a24b002e4507f2d26d0388f226789aab14b7e89b97991e16ffa35
* proof-B0Sedge-r2.md  ac2de0d299849aa50e733fbe01deb2448bfa19f8e67f33137daa0a2459a70ba3
* proof-REFL-B0-r3.md  c05eb38386e8e1a239f6abf51875f3fcc02c1ce2304cf14063be9d95bd412272
* notes-B1-cfunc-r1.md  781bfee8ec92417ce5e19785d9dc2c966edd4483123148436f7be8805fcdb3e3
* notes-gapA-r1.md  20daf0dbc507ad7dc6a1292cb5ff9b3fcabb069690452693274d12c4c83feb0f
* notes-gapA-r2.md  b32df386154980708ff9342691d2832dc3387a9287f1602f2aead939c96f8f89
* plan-E17.md  5ecd3f202486f2bf60f0eb2187523f5c044a4f697e48245c4167721cf6bbbd4d
* code/e17_gap_a_probe.py  36b8e20af797ce4b9167e980e5452e45827607c3c5bf633c755c92ab8a6234ff
* code/e17_gap_a_probe_v2.py  b53299fdfdd0afee56ec42c01a0bcca620f0d4f5ee5bb84f8e47ec18f4a6fde3
* out/e17_gap_a_probe.json  14dcab390373949b723c59cecb24d1939ef1be471350c6cd6c38618d18f30e34
* results-r3.md  8e464d54c43fb5a4eef913a7be9bd504953d0bf2456fb84c1106b9254e79476a
