# RQLS10 v104 — THETA(1,2,2) H6: EVERY row-pair is squeezed; for the v103 Latin square, forced triple splits and an all-triple no-go

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 22:46:33 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra and combinatorics only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Setting

The E4 frame, the classes and the Latin square L are those of v103. H6 is the complementary sector; MAX means its sixty rays are pairwise distinct.

H6 supports by row-pair:
- v1: Xb', Yb', a1, a2, b1, b2
- v2: Xc', Ya', Yb', Yc', b1, b2
- v3: Xa', Xb', Xc', Yc', b1, b2
- v4: Xa', Ya', Yb', Yc', a1, a2
- v5: Xa', Xb', Xc', Ya', a1, a2

For a row-pair v, write d_k = cell (v.1, k) and e_k = cell (v.2, k). An orthogonal triple split at v is a partition of its six columns into T | T' whose planes span(d_k, e_k) are mutually orthogonal within each triple.

## 2. Theorem ALL-SQUEEZED (every completion L)

A class sigma SQUEEZES row-pair v if its E4 columns are exactly v's E4 columns and none of its E4 rows lies in v. In THETA(1,2,2) every row-pair is squeezed by two classes, read off from v103 §4:

| Row-pair | E4 columns | Squeezing classes | Their E4 rows |
|---|---|---|---|
| v1 | Xa', Xc', Ya', Yc' | N1, N2 | v2, v3, v4, v5 |
| v2 | Xa', Xb', a1, a2 | P1, P2 | v1, v4 and both v3 rows |
| v3 | Ya', Yb', a1, a2 | U1, U2 | v1, v5 and both v2 rows |
| v4 | Xb', Xc', b1, b2 | Q1, Q2 | v2, v1 and both v5 rows |
| v5 | Yb', Yc', b1, b2 | V1, V2 | v3, v1 and both v4 rows |

Each squeezing class therefore has one H6 cell in each row of v, and its other four H6 cells lie in v's H6 columns. The v101 SQUEEZE lemma and forced forms apply verbatim: v replaces Z, and sigma replaces N1.
- Every orthogonal triple split at v contains sigma's two v-columns m1 (row v.1) and m2 (row v.2) in one triple.
- If that triple is {m1, m2, m'}, then sigma's cell in column m' equals alpha d_{m2} + beta e_{m1} with alpha·beta ≠ 0.

These statements are independent of L. In BARBELL, by contrast, only Z is squeezed.

## 3. Forced triples for the v103 L

Reading L (v103 §5) gives the v-columns of each squeezing class:
- v1: N1 at (Xb', Yb'), N2 at (Yb', Xb').
- v2: P1 at (Yc', b1), P2 at (b2, Yc').
- v3: U1 at (b1, Xc'), U2 at (Xc', b2).
- v4: Q1 at (Ya', a2), Q2 at (a1, Ya').
- v5: V1 at (a1, Xa'), V2 at (Xa', a2).

Hence every orthogonal triple split is FORCED to be:
- v2: {Yc', b1, b2} | {Xc', Ya', Yb'}
- v3: {Xc', b1, b2} | {Xa', Xb', Yc'}
- v4: {Ya', a1, a2} | {Xa', Yb', Yc'}
- v5: {Xa', a1, a2} | {Xb', Xc', Ya'}
- v1: {Xb', Yb', x} | rest, with x ∈ {a1, a2, b1, b2}

## 4. Theorem ALL-TRIPLE NO-GO (v103 L)

No MAX H6 sector for this L has orthogonal triple splits at all five row-pairs. More precisely:
- if v1 splits with x ∈ {a1, a2}, then v2 or v3 has no orthogonal triple split;
- if v1 splits with x ∈ {b1, b2}, then v4 or v5 has none.

Proof, case x ∈ {a1, a2}. Then b1 and b2 lie in a common triple at v1, v2 and v3, with third columns a_other, Yc' and Xc' respectively. Because the b1 and b2 columns each sum to I, the third planes also sum to I. So the 3×3 array (v1, v2, v3) × (b1, b2, third) is a plane Latin array, and v100 PLS3 makes it Classical or K33.
- P1's forced form gives (v1.2, b2) = alpha (v2.1, b1) + beta (v2.2, Yc'), with alpha·beta ≠ 0.
- Classical case: (v1.2, b2) would have nonzero parts in two orthogonal planes of the decomposition while lying in a single one, which is impossible.
- K33 case: write the v2 planes as b1 = (p',q'), Yc' = (p'',q''), b2 = (p''',q'''). Then b2 at v1 is (p',q'') or (p'',q'); up to the x/y symmetry take (p',q''). Containment forces (v2.1, b1) = x_{p'} and (v2.2, Yc') = y_{q''}.
- P2's form gives (v1.1, b1) = alpha' (v2.1, Yc') + beta' (v2.2, b2). This forces every v2 T-cell to be a K33 line, and fixes the v1 and v3 rows:
  - v1: b2 = (p',q''), b1 = (p'',q'''), a_other = (p''',q');
  - v3: b1 = (p''',q''), b2 = (p'',q'), Xc' = (p',q''').
- U1's form gives (v1.1, b2) = alpha'' (v3.1, Xc') + beta'' (v3.2, b1). Containment in x_{p'} ⊕ y_{q''} forces (v3.1, Xc') = x_{p'} = (v2.1, b1). Two distinct cells then carry one ray, contradicting MAX.

Case x ∈ {b1, b2} is the same argument on the block (v1, v4, v5) × (a1, a2, third), using Q1, Q2 and V1:
- Q1 and Q2 make every v4 T-cell a K33 line, (v4.1, ·) = x's and (v4.2, ·) = y's, with (v4.2, a1) = y_{q'''}.
- V1's form then forces (v5.1, Xa') = y_{q'''} = (v4.2, a1), again a repeat.

## 5. Status and frontier

For this L, every MAX H6 must contain a row-pair, among v2/v3 or v4/v5 according to v1's split (or v1 itself), whose six planes admit NO orthogonal triple split. This parallels BARBELL's Z-SPLIT (v101/v102). The surviving H6 frontier for this L consists of non-triple ("dense") row-pairs. Other completions L have other forced triples; the §2 squeeze holds for all L, but the §4 no-go is proved only for this L.

H6 existence for THETA(1,2,2) and BARBELL remains OPEN, and no general no-go is claimed. C5, dense E4 frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v103 frame, classes and L; v101 SQUEEZE and forced forms; v100 PLS3 and Lemma U6; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S104, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the v29 and v40 parallel-intent minors, the v30 dangling-reference defect, the v34 capture retry, the S98 zero-credit mental-decimal disclosure, the v46 parallel post-cell capture disclosure and the S103 pre-pin draft correction.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
