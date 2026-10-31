# RQLS10 v138 — BARBELL v98 frame, N-block family: forced row structure at Z, T1, T2, R1, R2 and a tight frame of eight singles in W(N@Z)

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:50:12 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact combinatorics and operator identities. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

Take the v98 BARBELL frame with any Latin completion L in the N-BLOCK FAMILY. By v137 §3 (Z-II), this means both NEITHER classes have type (Z, Z), so N occupies the 2×2 Latin block (Z; Xa, Ya). The v99 completion belongs to this family. We use the incidence table of v137 §1.

## 1. Theorem N-BLOCK FAMILY STRUCTURE

In every completion of the N-block family:

- **(a) Z rows.** z.1 places A1 and A3 in {Ba, Bb} and B2 and B4 in {Aa, Ab}. z.2 places A2 and A4 in {Ba, Bb} and B1 and B3 in {Aa, Ab}. So every A-class has exactly one Ba/Bb cell at Z, and every B-class has exactly one Aa/Ab cell at Z.
- **(b) T1.** The four cells of Aa ∪ Ab at T1 are:
  - N1 (t1.1) and N2 (t1.2);
  - one cell of B3 and one cell of B4, in different T1 rows.

  The other T1 cells of B3 and B4 lie in {Xc, Yb}, each in the row opposite its Aa/Ab cell.
- **(c) T2.** The same holds with N1 (t2.1), N2 (t2.2), B1 and B2. Their other T2 cells lie in {Xb, Yc}.
- **(d) R1 and R2.** The four cells of Ba ∪ Bb at R1 are N2 (r1.1), N1 (r1.2) and one cell each of A3 and A4, in different rows. The other R1 cells of A3 and A4 lie in {Xb, Yc}. At R2 the same holds with N2 (r2.1), N1 (r2.2), A1 and A2, whose other R2 cells lie in {Xc, Yb}.
- **(e) Columns Xa and Ya.** Xa at T1 ∪ T2 holds four A-cells, one per A-class. Ya at R1 ∪ R2 holds four B-cells, one per B-class.

Proof.
- **(a) and (e).** In each z-row, N fills Xa and Ya. The remaining columns follow from the v137 §1 lists. N's other G_X cells lie at T1 and T2 and avoid Xa, so they lie in Aa/Ab; its other G_Y cells lie at R1 and R2 and avoid Ya, so they lie in Ba/Bb. This gives (e).
- **(b).** By (a), B3 and B4 each have one Aa/Ab cell at Z. Their remaining Aa/Ab cell must lie at T1, since by v137 §1 B3 and B4 reach Aa/Ab only at Z and T1. Each T1 row contains exactly one N in Aa/Ab, so the two B-cells sit in different rows.
- **(c) and (d).** These are the mirror arguments. ∎

## 2. Theorem SINGLES TIGHT FRAME

Let S be the sum of the rank-one projections of eight cells:
- the four B-cells of Aa ∪ Ab at T1 ∪ T2;
- the four A-cells of Ba ∪ Bb at R1 ∪ R2.

Then S = 2P_{W(N@Z)}. In particular, all eight cells lie in the 4-dimensional block span W(N@Z) and form a tight frame with constant 2 there.

Proof.
1. **Row Z minus class N.** Row Z is P_{W(N@Z)} plus the eight Z-cells of Aa, Ab, Ba and Bb; these are B-cells and A-cells by §1(a). Class N is P_{W(N@Z)} plus its eight singles: the cells of Ba/Bb at R1, R2 and of Aa/Ab at T1, T2. Subtracting, (Z-cells of Aa, Ab, Ba, Bb) = (N-singles).
2. **Columns.** Columns Aa + Ab give (B-cells at Z) = 2I − (N-cells at T1, T2) − (B-cells at T1, T2). Columns Ba + Bb give (A-cells at Z) = 2I − (N-cells at R1, R2) − (A-cells at R1, R2).
3. **Conclusion.** Adding, 4I − 2·(N-singles) = S. The class-N identity gives (N-singles) = 2I − P_{W(N@Z)}. Positivity then places each cell in W(N@Z), as in v132 §1. ∎

This is the BARBELL analogue of the THETA(1,2,2) SS N-tight-frame (v133 §1).

## 3. Status

This is the forced row structure and an exact operator identity for the N-block family of the v98 BARBELL frame, which contains v99's completion. It is not a classification of the family: the T1/T2/R1/R2 sub-cases and the singles columns are not enumerated. No H6 existence or exclusion is claimed.

BARBELL H6 is OPEN for every frame and completion. So are:
- the THETA(1,2,2) SS residual and the other THETA patterns;
- C5 three-label patterns;
- dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v98/v99; v100/v102 N-FORCE; v107 BLOCK4 (the N block is an orthonormal 4-frame); v132 §1 positivity; v137; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S138. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
- the v80, v82 and v83 stray spaces;
- the park-v10 JSON parse-check disclosure;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
