# RQLS10 v137 — BARBELL v98 frame, EVERY completion: the H6 incidence table, N-type count identities, and the Z-row configurations

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:45:40 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact combinatorics read off the hand-checked v99 §3 table (bracketed E4 entries only). Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Purpose

In the THETA(1,2,2) case, BLOCK-KILL (v132) needed the incidence structure of EVERY Latin completion (v111 FORCED-L). For BARBELL, v99 exhibits one completion, and v100/v102 force only the N classes. This manuscript fixes the completion-independent data for the v98 frame: which H6 cells each class may occupy. It also proves the first counting identities for every completion.

Notation follows v99 §4. The H6 row-pairs are R1, R2, Z, T1 and T2. The class H6 rows and columns are read off the bracketed E4 entries of v99 §3; they do not depend on L.

## 1. Lemma INCIDENCE (every completion L)

For each H6 row, the table lists the class → allowed columns map. An allowed column is one that is in both the row's H6 support and the class's H6 columns.

- **r1.1** (support Xb, Ya, Yb, Yc, Ba, Bb): N2 {Ya, Ba, Bb}; A3, A4 {Xb, Yc, Ba, Bb}; B1, B2 {Xb, Ya, Yb, Yc}; B3 {Ya, Yb, Yc}.
- **r1.2**: N1 {Ya, Ba, Bb}; A3, A4 {Xb, Yc, Ba, Bb}; B1, B2 {Xb, Ya, Yb, Yc}; B4 {Ya, Yb, Yc}.
- **r2.1** (support Xc, Ya, Yb, Yc, Ba, Bb): N2 {Ya, Ba, Bb}; A1, A2 {Xc, Yb, Ba, Bb}; B2 {Ya, Yb, Yc}; B3, B4 {Xc, Ya, Yb, Yc}.
- **r2.2**: N1 {Ya, Ba, Bb}; A1, A2 {Xc, Yb, Ba, Bb}; B1 {Ya, Yb, Yc}; B3, B4 {Xc, Ya, Yb, Yc}.
- **z.1** (support Xa, Aa, Ab, Ya, Ba, Bb): N1, N2 any; A1, A3 {Xa, Ba, Bb}; B2, B4 {Aa, Ab, Ya}.
- **z.2**: N1, N2 any; A2, A4 {Xa, Ba, Bb}; B1, B3 {Aa, Ab, Ya}.
- **t1.1** (support Xa, Xb, Xc, Aa, Ab, Yb): N1 {Xa, Aa, Ab}; A1, A2 {Xa, Xb, Xc, Yb}; A3 {Xa, Xb, Xc}; B3, B4 {Xc, Aa, Ab, Yb}.
- **t1.2**: N2 {Xa, Aa, Ab}; A1, A2 {Xa, Xb, Xc, Yb}; A4 {Xa, Xb, Xc}; B3, B4 {Xc, Aa, Ab, Yb}.
- **t2.1** (support Xa, Xb, Xc, Aa, Ab, Yc): N1 {Xa, Aa, Ab}; A2 {Xa, Xb, Xc}; A3, A4 {Xa, Xb, Xc, Yc}; B1, B2 {Xb, Aa, Ab, Yc}.
- **t2.2**: N2 {Xa, Aa, Ab}; A1 {Xa, Xb, Xc}; A3, A4 {Xa, Xb, Xc, Yc}; B1, B2 {Xb, Aa, Ab, Yc}.

Column hosts:
- Xa: N1, N2, A1–A4.
- Aa and Ab: N1, N2, B1–B4.
- Ya: N1, N2, B1–B4.
- Ba and Bb: N1, N2, A1–A4.
- Xb: A1–A4, B1, B2.
- Xc: A1–A4, B3, B4.
- Yb: A1, A2, B1–B4.
- Yc: A3, A4, B1–B4.

Proof. Each class's E4 rows and columns are its bracketed cells in v99 §3. The H6 supports are those of v99 §4, fixed by the placement (v102 §1). ∎

## 2. Lemma N-TYPE COUNTS (every completion)

By v102 §3, each NEITHER class N has exactly three G_X cells and three G_Y cells:
- its G_X cells sit at its T1 row, its T2 row and one z-row, and they lie one each in Xa, Aa and Ab;
- its G_Y cells sit at its R1 row, its R2 row and the other z-row, and they lie one each in Ya, Ba and Bb.

Define:
- X-type(N) ∈ {Z, T1, T2}: the row-pair of N's Xa cell;
- Y-type(N) ∈ {Z, R1, R2}: the row-pair of N's Ya cell.

Then:
- **(a)** The number of B3/B4 cells of Aa ∪ Ab at Z equals #{N : X-type ≠ T1}.
- **(b)** The number of B1/B2 cells of Aa ∪ Ab at Z equals #{N : X-type ≠ T2}.
- **(c)** The number of N-cells of Aa ∪ Ab at Z equals #{N : X-type ≠ Z}.
- **(d)** Mirror for A: the A3/A4 cells of Ba ∪ Bb at Z number #{N : Y-type ≠ R1}, and the A1/A2 cells number #{N : Y-type ≠ R2}.
- **(e)** Each of B3 and B4 has at least one Aa/Ab cell at T1. Each of B1 and B2 has at least one at T2. Each of A3 and A4 has at least one Ba/Bb cell at R1. Each of A1 and A2 has at least one at R2.

Proof of (a). The four cells of Aa ∪ Ab at T1 belong to N1 (t1.1), N2 (t1.2), B3 and B4 (§1). The N contributes there iff its Xa is not at T1. B3 and B4 have four Aa/Ab cells in total, and these lie at Z or T1 (§1). Subtracting gives (a).

The other parts are identical. For (e): B3 has only one Z row (z.2), so at most one of its two Aa/Ab cells is at Z. ∎

## 3. Lemma Z-ROW CONFIGURATIONS (every completion)

In row z.1, the classes A1 and A3 occupy two of {Xa, Ba, Bb} and B2 and B4 occupy two of {Aa, Ab, Ya}. So exactly one N lies in {Xa, Ba, Bb} and the other in {Aa, Ab, Ya}. The same holds in z.2 with A2, A4, B1, B3.

Hence exactly one of the following holds:
- **(Z-I)** One N has its two Z cells in {Xa, Ba, Bb}: Xa (X-type Z) and Ba or Bb (Y-type ≠ Z). The other has its two Z cells in {Aa, Ab, Ya}: Aa or Ab (X-type ≠ Z) and Ya (Y-type Z).
- **(Z-II)** Each N has one Z cell in each group. Then each N is either:
  - of type (Z, Z), with cells Xa and Ya; or
  - of type (≠Z, ≠Z), with cells Ba/Bb and Aa/Ab.

  If both N are of type (Z, Z), then N occupies a 2×2 Latin block (Z; Xa, Ya). This is the v99 completion.

Proof. Each N has one G_X and one G_Y cell among the two z-rows (v102 §3). The groups are {Xa} ∪ {Ba, Bb} and {Aa, Ab} ∪ {Ya}, and G_X ∩ {Xa, Ba, Bb} = {Xa}. The cases follow. ∎

## 4. Status

These are completion-independent incidence lemmas for the v98 BARBELL frame: the first step toward a FORCED-L-type classification, which BALANCE-type arguments (v132) would need. No H6 existence or exclusion is claimed, and the classification of completions is NOT completed.

BARBELL H6 is OPEN for every frame. So are:
- the THETA(1,2,2) S103 SS residual and the other THETA patterns;
- C5 three-label patterns;
- dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v98/v99 §3–§4 table and supports; v100 N-FORCE; v102 §1–§3. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S137. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114, S130 and S136 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v77 stray-space and characterization typos;
- the v78 checkpoint typo;
- the v80 and v82 stray spaces;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
