# RQLS10 v108 — C5 with the all-adjacent class pattern has NO MAX H6: hat-triangle rigidity, purity, and a complete no-go

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 23:30:10 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra and combinatorics only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Scope

Consider the all-sparse SIMPLE FIVE-CYCLE placement of v82 whose TEN-class resolution is the ALL-ADJACENT pattern: two classes A_i^± with labels {C_i, C_{i+1}} for each i. The S106 sector is one such frame, but the theorem quantifies over EVERY E4 frame with this pattern and EVERY Latin mate. Other C5 class patterns (non-adjacent pairs, or three-label classes) are NOT covered.

By v106 §5, every mate is a block inflation of F. The fifteen H6 blocks are (j, d), meaning row-pair v_j and column pair c_{j+d} for d ∈ {2, 3, 4}. Block (j, d) holds A_{j+g(d)}^±, with g(2) = 3, g(3) = 0, g(4) = 2 (mod 5). The fifteen lines are:
- row line R_j = {(j,2), (j,3), (j,4)};
- column line C_k = {(k+1,4), (k+2,3), (k+3,2)};
- class line S_i = {(i,3), (i+2,2), (i+3,4)}.

H_{j,d} denotes the hat plane of block (j, d) (v107 §1). By v107 HAT, the three hats on each line are mutually orthogonal and sum to I.

## 1. Lemma TRIANGLE (hat rigidity)

For every j: H_{j+3,4} = H_{j,4} and H_{j+2,2} = H_{j,2}.

Proof.
- Block (j+3, 4) lies in column line C_{j+2}, together with (j,2), and in class line S_j, together with (j,3). Hence H_{j+3,4} ⊥ H_{j,2} and H_{j+3,4} ⊥ H_{j,3}, so H_{j+3,4} ⊂ (H_{j,2} ⊕ H_{j,3})^⊥ = H_{j,4} by R_j. Both planes have dimension two.
- Block (j+2, 2) lies in class line S_j, together with (j,3), and in column line C_{j+4}, together with (j,4). Hence H_{j+2,2} ⊂ (H_{j,3} ⊕ H_{j,4})^⊥ = H_{j,2}.

Since 3 and 2 generate Z5, H_{j,4} =: Q_4 and H_{j,2} =: Q_2 are independent of j. Then H_{j,3} = (Q_2 ⊕ Q_4)^⊥ =: Q_3 is constant too. ALL fifteen hats therefore lie in the single orthogonal decomposition C6 = Q_2 ⊕ Q_3 ⊕ Q_4, with H_{j,d} = Q_d.

## 2. Lemma PURITY

Every H6 cell lies in a single Q_d.

Proof. Fix a block (j, d), so that W = Q_{d'} ⊕ Q_{d''}. Its row-line array and its column-line array are PLS3 (v107). Their hat rows consist of the three distinct members Q_2, Q_3, Q_4.

Every non-hat entry X of either array, at this block, has one of two forms:
- **Classical case:** X is one of Q_{d'} or Q_{d''}, because {A, B, C} = {Q_2, Q_3, Q_4}.
- **K33 case:** each Q is spanned by two K33 lines, so X is a SPLIT plane: a line of Q_{d'} plus a line of Q_{d''}. Both lines cannot lie in one Q, since two distinct array cells never carry the same index pair.

A cell, say p = D ∩ Π^a, is one-dimensional because p, q, r, t are orthonormal (v107 BLOCK4). The four cases are:
- **full ∩ full:** equal or orthogonal, which is impossible;
- **full ∩ split:** the split plane's line in that Q;
- **split ∩ full:** the same;
- **split ∩ split:** exactly one of the two component lines must agree, otherwise the intersection is zero or D = Π^a.

In every possible case the cell is a line inside one Q_d.

## 3. Theorem C5-ADJ-NO-GO

No original MAX1 array has the all-sparse C5 placement with the all-adjacent class pattern.

Proof. By PURITY, each H6 row consists of six pure cells forming an orthonormal basis of Q_2 ⊕ Q_3 ⊕ Q_4. It therefore contains exactly two cells in each Q_d, and they form an orthonormal basis of that plane. The same holds for each H6 column.

Take any H6 cell x ∈ Q_d. Its row contains a cell y ∈ Q_d with y ⊥ x, and its column contains a cell z ∈ Q_d with z ⊥ x. Since Q_d is two-dimensional, y and z are both the unique ray x^⊥. They occupy different positions (y is off x's column, z is off x's row), which contradicts MAX.

In particular, the explicit S106 sector admits no completion to an original 100-ray array, for any H6 and any Latin mate.

## 4. Status

C5 survives at most through class patterns that contain non-adjacent pairs {C_i, C_{i+2}} or three-label classes. Their existence is OPEN and is not addressed here.

S106 remains a valid explicit SECTOR-level candidate, i.e. E4 plus resolution plus Latin mate. Its §7 sector-level classification is unchanged, but this theorem shows that the all-adjacent route cannot be completed.

The H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v106 forced block Latin mates (all-adjacent pattern); v107 BLOCK4/HAT/PLS-LINE; v100 PLS3; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S108. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 pre-pin draft correction;
- the v53 two-replace ceiling disclosure.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing was opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark. The metadata assembly is separately characterized; this is not a clean global execution/cognition census.
