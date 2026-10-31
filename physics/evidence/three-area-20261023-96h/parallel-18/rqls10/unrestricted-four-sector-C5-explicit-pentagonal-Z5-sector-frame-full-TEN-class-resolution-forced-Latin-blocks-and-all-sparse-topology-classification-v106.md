# RQLS10 v106 — An explicit Z5-symmetric pentagonal C5 sector with full TEN-class resolution and forced block Latin mates; all-sparse topology classification

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 23:05:33 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. This is exact written Pauli/quaternion algebra only; it is not machine-, kernel- or formally checked. No scientific Eval, interpreter, CAS, program, enumeration, solver or replay was used.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Notation

This manuscript continues v105 for the all-sparse SIMPLE FIVE-CYCLE.
- Circuits C_i and vertices v_i = C_i ∩ C_{i+1} are indexed mod 5.
- R_i = 2P_{C_i} − I and Sigma_{v_i} = 2S_{v_i} − I.
- Work on C4 = K1 ⊗ K2.
  - K1 has Paulis σ_x, σ_y, σ_z and σ_z-basis |0>, |1>.
  - K2 has Paulis σ_1, σ_2, σ_3, with σ_k-eigenvectors |k±>.
- R_n(a) = exp(−i(a/2) n·σ) denotes the rotation by angle a about the axis n.

## 1. Data

- Let r_0 = (1/2)σ_z + (√3/2)σ_x.
- Let φ be the angle in (−π, −π/2) with cos φ = −2/3 and sin φ = −√5/3, so that φ/2 ∈ (−π/2, −π/4).
- Let V = R_z(φ) R_y(−π/3) on K1. Then V r_0 V* = σ_z, because R_y(−π/3) carries the Bloch vector (√3/2, 0, 1/2) to (0, 0, 1) and R_z fixes it.
- Let C = exp(−i(π/4) σ_z⊗σ_2) = |0><0| ⊗ R_2(π/2) + |1><1| ⊗ R_2(−π/2).
- Let U = C (V⊗I).
- Define R_i = U^i (r_0⊗I) U^{−i} and Sigma_{v_i} = U^i (I⊗σ_3) U^{−i}.

**Lemma PENT.** U^5 = −I. Hence the ten operators above are well defined mod 5.

*Proof.*
1. C and V⊗I commute with I⊗σ_2.
2. On K1⊗|2±> the operator C acts as exp(∓i(π/4)σ_z) = R_z(±π/2). So U acts as W_± = R_z(φ ± π/2) R_y(−π/3).
3. The scalar part of R_z(a)R_y(b) is cos(a/2)cos(b/2).
4. Put β = φ/2 + π/4 ∈ (−π/4, 0). Then cos 2β = −sin φ = √5/3, so cos β = (1+√5)/(2√3) and sin β = −(√5−1)/(2√3). Their squares are (3±√5)/6.
5. Hence the scalar part of W_+ is (√3/2)cos β = (1+√5)/4 = cos(π/5), and the scalar part of W_− is (√3/2)sin β = −(√5−1)/4 = cos(3π/5).
6. A unit quaternion cos(kπ/5) − i sin(kπ/5) m·σ has fifth power cos(kπ) I = −I for k = 1 and k = 3. ∎

## 2. Frame equations

**Explicit operators at i = 0.**
- R_1 = C(σ_z⊗I)C* = σ_z⊗I.
- {R_0, R_1} = 2(1/2)I = I. So the adjacent pairs are interior-isoclinic with λ = 1/2.
- C(I⊗σ_1)C* = −σ_z⊗σ_3, because R_2(±π/2) sends σ_1 to ∓σ_3.
- C(I⊗σ_3)C* = σ_z⊗σ_1, because R_2(±π/2) sends σ_3 to ±σ_1.
- Therefore Sigma_{v_1} = σ_z⊗σ_1.
- U(r_0⊗σ_1)U* = (σ_z⊗I)(−σ_z⊗σ_3) = −Sigma_{v_0}. Hence Sigma_{v_4} = U* Sigma_{v_0} U = −r_0⊗σ_1.

**Commutation and traces.** Sigma_{v_0} = I⊗σ_3 is traceless and commutes with R_0 and R_1, and tr(Sigma_{v_0} R_0) = tr(Sigma_{v_0} R_1) = 0. Conjugating by U^j gives the same statements for every j. So S_{v_j} is a rank-two projection commuting with P_{C_j} and P_{C_{j+1}}, with both traces equal to one. The v82 forward construction then makes all ten E4 rows and ten E4 columns orthonormal bases.

## 3. TEN classes (the all-adjacent pattern of v105 §4, now non-degenerate)

**Site operators.** M := R_1 Sigma_{v_1} = I⊗σ_1 = −R_0 Sigma_{v_4}.

**Classes.** For s = ±, set A_0^s to be the four rays
- r_0+⊗|1s> and r_0−⊗|1s>, the C_0 cells at v_4, one in each row and one in each C_0 column;
- |0>⊗|1,−s> and |1>⊗|1,−s>, the C_1 cells at v_1, one in each row and one in each C_1 column.

Each A_0^s is an orthonormal basis, because the two pairs span complementary planes K1⊗|1s> and K1⊗|1,−s>. Define A_i^s = U^i A_0^s; U^i carries cells of (C_j, v_k) to cells of (C_{j+i}, v_{k+i}) and preserves the sign labels.

**Partition.** The ten classes use
- each row at v_j through its C_j cells (classes A_{j−1}^±) and its C_{j+1} cells (classes A_{j+1}^±);
- each column twice at each endpoint vertex, in different classes.

So the 40 cells are partitioned with distinct rows and columns in every class.

## 4. MAX40

All 40 rays are pairwise nonparallel, by the following checks.
- **Adjacent circuits.** {R_i, R_{i+1}} = I, so they have no common eigenvector.
- **Non-adjacent circuits.**
  - R_2 = UR_1U* = (1/2)σ_z⊗I + (−(√15/6)σ_x + (√3/3)σ_y)⊗σ_2. This uses C(σ_x⊗I)C* = σ_y⊗σ_2 and C(σ_y⊗I)C* = −σ_x⊗σ_2. Its square is (1/4 + 15/36 + 12/36)I = I.
  - {R_0, R_2} = (1/2)I − (√5/2) I⊗σ_2, with eigenvalues (1∓√5)/2. Neither equals ±2, so R_0 and R_2 have no common eigenvector. All non-adjacent pairs are conjugate to (R_0, R_2).
- **One circuit, two vertices.** The C_1 cells at v_0 are |0/1>⊗|3±>, and those at v_1 are |0/1>⊗|1±>. These are distinct; conjugation gives the same for every circuit.
- **One vertex.** Cells at the same vertex are orthogonal.

Remark: (1±√5)/2 are the pentagonal values 2cos(π/5) and 2cos(3π/5).

## 5. Latin mates are forced up to block orientation

Index the 2×2 blocks (v_j, c_k), where c_k is the column pair of C_k.
- **E4 blocks.** The block (v_j, c_j) holds A_{j−1}^± and the block (v_j, c_{j+1}) holds A_{j+1}^±. Each is a 2×2 Latin subsquare: the pairs {PS, P'S'} and {PS', P'S} are its two diagonals.
- **H6 rows and columns of A_i.** Class A_i needs H6 cells in rows v_i, v_{i+2}, v_{i+3} and in column pairs c_{i+2}, c_{i+3}, c_{i+4}.
  - Row v_{i+2} has H6 columns c_{i+4}, c_i, c_{i+1}. Its only admissible pair is therefore c_{i+4}.
  - Row v_{i+3} has H6 columns c_i, c_{i+1}, c_{i+2}. Its only admissible pair is therefore c_{i+2}.
  - The remaining rows v_i must use c_{i+3}.
- **Block square.** Hence EVERY Latin mate inflates the order-5 Latin square F(j,k) = j + g(k−j), where g(0..4) = (−1, 1, −2, 0, 2), using 2×2 Latin blocks. F is Latin: g is a bijection, and h(d) = g(d) − d takes the values (4, 0, 1, 2, 3).
- **Freedom.** Only the orientations of the fifteen H6 blocks are free.

## 6. H6 interface

Each row-pair v_i is squeezed by A_i^± in the v101 sense: the E4 columns of A_i equal those of v_i, and A_i has no E4 row at v_i. In EVERY Latin mate, both squeezing classes occupy the single block (v_i, c_{i+3}). This manuscript derives NO H6 consequence from these facts.

## 7. Corollary: all-sparse topology classification at sector level

Combine the following:
- v79/v81: at most three circuits and triple intersections are excluded;
- v82: the remaining topology list;
- v84: FIGURE-EIGHT is excluded;
- v93: THETA(1,1,3) is excluded.

Every all-sparse original MAX1 array in the v76 placement therefore has topology BARBELL(2,1,2), THETA(1,2,2) or C5, within the stated scopes of those imports. EACH of the three survivors admits explicit written sector data: an E4 frame, a TEN-class sector resolution, MAX40 and a Latin mate. These are given by S98/S99, S103 and S106 respectively. The all-sparse E4 sector question is thus settled at sector level; the H6 complement is not.

## 8. Scope

This is an explicit written sector candidate, not a 100-ray array. The C5 H6 sector, the H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN. This result supersedes nothing in v105, whose Clifford solution remains a MAX-failing degenerate case.

Imports: v82 forward construction and topology list; v86 Corollary R; v79/v81/v84/v93 exclusions as stated; v101 squeeze definition; elementary SU(2)/quaternion facts. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S106. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 pre-pin draft correction.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing was opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark. The metadata assembly is separately characterized; this is not a clean global execution/cognition census.
