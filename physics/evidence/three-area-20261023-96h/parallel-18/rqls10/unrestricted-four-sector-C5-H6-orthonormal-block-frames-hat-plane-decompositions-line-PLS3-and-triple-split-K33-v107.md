# RQLS10 v107 — C5 H6: every Latin block is an orthonormal 4-frame; complementary hat planes decompose along all fifteen lines; line arrays are PLS3; triple splits force K33

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 23:20:43 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra and combinatorics only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

Take the C5 sector of v106 with ANY Latin mate. By v106 §5, every mate is the block inflation of the order-5 square F. H6 is the complementary sector, isometric to C6, and MAX means its sixty rays are pairwise distinct. The H6 cells form fifteen 2×2 blocks beta = (v_j, c_k) with k − j ∈ {2, 3, 4}; block beta holds the class pair A_{F(j,k)}^±.

There are fifteen LINES, each consisting of three blocks:
- **row-pair line j:** (v_j, c_{j+2}), (v_j, c_{j+3}), (v_j, c_{j+4});
- **column-pair line k:** (v_{k+1}, c_k), (v_{k+2}, c_k), (v_{k+3}, c_k);
- **class-pair line i:** (v_i, c_{i+3}), (v_{i+2}, c_{i+4}), (v_{i+3}, c_{i+2}).

Write the cells of a block as p = (v.1, c^a), q = (v.1, c^b), r = (v.2, c^a) and t = (v.2, c^b).

## 1. Lemma BLOCK4

In every block, p, q, r and t are pairwise orthogonal.
- p ⊥ q and r ⊥ t (rows).
- p ⊥ r and q ⊥ t (columns).
- The two classes of a 2×2 Latin block occupy its two diagonals, so p ⊥ t and q ⊥ r.

Hence W_beta = span(p, q, r, t) is four-dimensional. Let the HAT plane be Ŵ_beta = W_beta^⊥, of dimension two. In particular, the two column planes of a block, Π^a = span(p, r) and Π^b = span(q, t), are orthogonal, and W_beta = Π^a ⊕ Π^b.

## 2. Lemma HAT

Along each of the fifteen lines, the three hat planes are mutually orthogonal and sum to I.

Proof. For a row-pair line, P_{W} summed over its three blocks equals the sum of the projections onto the six row-1 cells and the six row-2 cells, which is 2I. Hence the three rank-two projections P_Ŵ sum to 3I − 2I = I, so they are orthogonal. Column-pair lines work the same way, using columns a and b. Class-pair lines work the same way, using A_i^+ and A_i^−, whose six H6 cells are orthonormal bases of H6.

## 3. Lemma PLS-LINE

On each line, the following 3×3 arrays of planes have every row and column summing to I, so v100 PLS3 applies and each is Classical or K33:
- row-pair line: rows D = span(p, q), E = span(r, t) and Ŵ; the columns are the three blocks;
- column-pair line: rows Π^a, Π^b and Ŵ;
- class-pair line: rows K^+, K^− (the two diagonals) and Ŵ.

Each column of such an array sums to P_W + P_Ŵ = I. Each row of the array is a line orthonormal basis, or it is the hat row of §2.

Fact used below: for orthogonal Latin squares of order three, two cells in different rows and different columns share exactly one coordinate. Indeed, up to isotopy L1 = r + c and L2 = r + 2c, and Δr is always Δc or 2Δc. Hence, in the K33 case, such entries meet in exactly one K33 line.

## 4. Lemma TRIPLE (row-pair splits)

At v_i the squeezed block is kappa0 = (v_i, c_{i+3}) (v106 §6).

(i) An orthogonal triple split at v_i exists iff some column plane Π_x of one of the other two blocks equals Ŵ_{kappa0}. In that case the split is {c_{i+3}^a, c_{i+3}^b, x} | {x̄, both columns of the third block}, and the plane of x̄ (x's partner column) equals the third block's hat plane.

Proof of (i). By v101 SQUEEZE, applicable because A_i^± squeeze v_i, T ⊇ {c_{i+3}^a, c_{i+3}^b}. These two planes are orthogonal by BLOCK4. So T is orthogonal iff Π_x ⊥ W_{kappa0}, i.e. Π_x = Ŵ_{kappa0}. The complement follows from W_{block(x)} = Π_x ⊕ Π_x̄ and HAT.

(ii) If v_i has an orthogonal triple split, its row-pair array is K33, not Classical. Moreover, the two cells of column x at v_i are K33 lines.

Proof of (ii).
- Classical case. Ŵ_{kappa0} ∈ {D_{kappa1}, E_{kappa1}}, where kappa1 is x's block. Π_x contains one cell of D_{kappa1} and one of E_{kappa1}, so the containment Π_x = Ŵ_{kappa0} forces a unit vector to be orthogonal to itself.
- K33 case. By the Fact, Ŵ_{kappa0} ∩ D_{kappa1} and Ŵ_{kappa0} ∩ E_{kappa1} are single K33 lines. They contain x's row-1 and row-2 cells respectively.

## 5. Consequences and frontier

C5 H6 is now equivalent to the following data:
- fifteen orthonormal 4-frames in C6;
- their hat planes, decomposing along all fifteen lines;
- forty-five PLS3 line arrays, each Classical or K33;
- class-diagonal compatibility and MAX.

Every split row-pair is K33 with K33-line cells in its x column. No existence and no exclusion of a C5 H6 sector is claimed. The H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v106 forced block Latin mates and squeeze interface; v101 SQUEEZE; v100 PLS3; elementary linear algebra; orthogonal Latin squares of order 3 up to isotopy. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S107. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 pre-pin draft correction.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
