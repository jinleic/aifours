# Quantum Mann dichotomy: L(K3,3,3) has no orthonormal representation in C^6, but L(K5,5,5) has an exact one in C^10

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the last pin before writing: Thu Oct 29 05:32:05 PDT 2026. Theorem A is a written proof. Theorem B is an explicit object verified by exact arithmetic in Z[zeta20]. Theorem C is an exact finite computer search, restricted to one stated ansatz. Nothing here constructs or excludes a maximal 1-RQLS(10); the original 100-ray target remains OPEN. No external model, network publication or novelty clearance was used. Novelty is unassessed.

## 0. Setting

An *orthonormal representation of L(K_{m,m,m}) in C^{2m}* means the following.
- Each edge e of the complete tripartite graph K_{m,m,m} (parts A, B, C) gets a unit vector psi_e.
- For every vertex v, the 2m vectors on the edges at v form an orthonormal basis.

The earlier packet `frontier-20261029-quantum-mann-kmmm-reformulation-v1.md` (SHA-256 `6f6a2dd8392ae8dccb8ca07384a7ad468d78765347d2105a0d4888f292cbe37e`) is the source of the setting. Suppose a 1-RQLS(2m) of any cardinality has a resolution Latin square with a Z2 quotient (four m x m subsquares; for example the cyclic labels Z_{2m}). Then the rows R0, the columns C0 and the labels T1 carry such a representation (the "parity core").

Classically (all vectors standard basis vectors) this is a proper 2m-edge-colouring of K_{m,m,m}. That is impossible for odd m, which is Mann's theorem. The frame identity gives Sum_{a in A} P_a = (m/2) I, where P_a is the projector onto the B-edges at a.

## 1. Theorem A (m = 3): impossible

**Theorem A.** L(K_{3,3,3}) has no orthonormal representation in C^6. Equivalently, there is no 27-ray, 9-context parity configuration in C^6 with K_{3,3,3} incidence.

**Lemma 1.** Let P1, P2, P3 be orthogonal projections with P1 + P2 + P3 = (3/2) I.
- Then P_i P_j P_i = P_i / 4 for i != j.
- All ranks equal some k, and dim H = 2k.
- Up to a unitary, H = C^2 (x) C^k and P_a = |u_a><u_a| (x) I, where u_a = (cos t_a, sin t_a) and t_a = 0, pi/3, 2pi/3.

*Proof.* Put S = P1 + P2 = (3/2)I - P3. Then S^2 = 9/4 - 2P3 = 2S - 3/4, so {P1, P2} = S - 3/4. Sandwiching by P1 gives P1 P2 P1 = P1/4. Taking traces equalises the ranks; trace of the sum gives dim H = 2k.

Now take an orthonormal basis f_j of ran P1 and write P2 f_j = f_j/4 + g_j with g_j orthogonal to ran P1. Then <g_i, g_j> = 3 delta_ij / 16. Put w_j = 4 g_j / sqrt 3. The map e1(x)e_j -> f_j, e2(x)e_j -> w_j is unitary. It carries P1 to |e1><e1| (x) I and P2 to |u_2><u_2| (x) I; this uses P2 w_j = sqrt3/4 f_j + 3/4 w_j. Then P3 = 3/2 - P1 - P2 becomes |u_3><u_3| (x) I. ∎

**Lemma 2.** Let a 3x3 array of unit vectors in C^3 have orthonormal rows and columns. Then it is, after one unitary and cellwise phases, a Latin square of basis vectors.

*Proof.* Take row 1 as the basis e_c. Row 2 then forms a unitary matrix with zero diagonal. Inner products of its columns force it to be a phased 3-cycle permutation matrix. Row 3 is forced cell by cell. ∎

**Proof of Theorem A.**

*Step 1 (structure from A).* By the frame identity, the three projectors P_a = Sum_b |psi_ab><psi_ab| satisfy Lemma 1, with k = 3. Write H = C^2 (x) K with K = C^3. Then psi_ab = u_a (x) x_ab and psi_ac = u_a^perp (x) y_ac. Each column {x_ab}_a is orthonormal because <u_a, u_a'> = ±1/2 is nonzero. The same holds for y.

*Step 2 (coordinates).* In the circular basis f_± = (1, ±i)/sqrt2, write w = f_+ (x) g + f_- (x) h, identified with (g, h) in K ⊕ K. Let xi_a = e^{-2i t_a}, so {xi_a} = {1, w, w^2}. Then:
- psi_ab is proportional to (xi_a x_ab, x_ab)/sqrt2;
- psi_ac is proportional to (-xi_a y_ac, y_ac)/sqrt2.

*Step 3 (graph subspaces).* Let G(U) = {(Uv, v)} for a unitary U. Its projector is (1/2)[[I, U], [U*, I]], and G(U)^perp = G(-U). Define K_b = Sum_a xi_a |x_ab><x_ab| and L_c = Sum_a xi_a |y_ac><y_ac|. Both have spectrum {1, w, w^2}, so det K_b = det L_c = 1. Then:
- Sum_a |psi_ab><psi_ab| = proj G(K_b);
- Sum_a |psi_ac><psi_ac| = proj G(-L_c).

Since E_b and E_c are orthonormal bases, psi_bc lies in G(-K_b) ∩ G(L_c). Hence psi_bc = (-K_b eta_bc, eta_bc)/sqrt2 with -K_b eta_bc = L_c eta_bc. Orthonormality transfers: eta is an orthonormal-row/column 3x3 array. So is kappa_bc := K_b eta_bc, because K_b and -L_c are unitary. This gives K_b = Sum_c |kappa_bc><eta_bc| and L_c = -Sum_b |kappa_bc><eta_bc|.

*Step 4 (Lemma 2).* Write eta_bc = phi_bc e_{lambda(b,c)} and kappa_bc = phi'_bc e'_{mu(b,c)}, with Latin squares lambda and mu. Let W = Sum |e'_j><e_j| and theta_bc = phi'_bc conj(phi_bc). Then K_b = W Sum_c theta_bc E_{mu(b,c), lambda(b,c)}.

*Step 5 (row completeness).* Rows of x are complete, so Sum_b K_b = Sum_a xi_a I = 0. Hence S := Sum_{b,c} theta_bc E_{mu(b,c), lambda(b,c)} = 0.

Fix j. The three cells with lambda = j would land in some positions (mu, j). Any position holding a single cell gives a nonzero unimodular entry of S. So all three cells share one mu-value. Therefore mu = pi∘lambda for a permutation pi.

This gives K_b = U Theta_b and L_c = -U Theta^c, with U = W P_pi. The diagonal matrices Theta_b and Theta^c carry the entries theta_bc of row b and of column c.

*Step 6 (determinant parity).* Take determinants and multiply:
- over b: 1 = Prod_b det K_b = (det U)^3 Prod_{b,c} theta_bc;
- over c: 1 = Prod_c det L_c = (-1)^9 (det U)^3 Prod_{b,c} theta_bc.

These two equations contradict each other. ∎

The final contradiction is a quantum version of Mann's parity count: the sign (-1)^{m·m} with m = 3. The m = 3 proof relies on two rigidity facts, Lemmas 1 and 2, which have no analogue at m = 5.

**Corollary A.** Let L be a Latin square of order 6 with a Z2 quotient (for example cyclic Z6). Then L has no quantum orthogonal mate. That is, no 6x6 array of unit vectors in C^6 has rows, columns and L-classes that are all orthonormal bases, at any cardinality. In fact the nine contexts R0 ∪ C0 ∪ T1 alone are already impossible.

*Comparison (not used in the proof).* For full order-6 arrays, Ball–Simoens (arXiv:2603.02334) prove a broader non-existence: the theorem quoted there excludes unentangled mutually orthogonal quantum Latin squares of order six. Theorem A concerns only the 9-context sub-configuration.

## 2. Theorem B (m = 5): an exact construction exists

**Theorem B.** L(K_{5,5,5}) has an orthonormal representation in C^10. Its properties:
- all 75 rays are pairwise non-parallel;
- all vectors are flat with entries zeta20^e / sqrt10;
- the 75 rank-one projectors have trivial commutant (computed numerically), i.e. the configuration is orthogonally irreducible.

*Construction.*
- Characters: c_j in Z5^2 are taken from the list T = [(0,0), (0,1), (1,0), (1,3), (2,2), (2,4), (3,1), (3,4), (4,2), (4,3)].
- For quadrant q in {AB, AC, BC} and x = (s,t) in Z5^2, set psi_q(x)_j = zeta5^{<c_j,x>} zeta20^{PHI2[q][j]} / sqrt10.
- PHI2[AB] = (-35, -25, -25, -15, -20, -10, -15, -5, -10, 0); PHI2[AC] = (-10, -10, -10, -5, 0, 5, -10, 0, 0, 0); PHI2[BC] = 0.
- Incidence: AB-cell x is edge A_s–B_t; AC-cell x is edge A_s–C_{s+t}; BC-cell x is edge B_t–C_{s+t}.

*Why it works.* T takes each value of alpha, beta and alpha - beta exactly twice. That gives orthogonality inside one quadrant. Across quadrants, orthogonality reduces to an integer phase system mod 2pi, which the stated phases solve exactly.

*Exact certificate.*
- Script `frontier-20261029-k555-exact-construction-v1.py`, SHA-256 `86dac5a94b33798703ecb3ee17004a0a7a9276cbf471753b127cc7cdd8ac9f5f`. It reduces modulo Phi20 = x^8 - x^6 + x^4 - x^2 + 1.
- It checks all 675 within-context pairs exactly orthogonal and all 75 rays exactly pairwise non-parallel. The total number of exactly orthogonal pairs is 825.
- Result `frontier-20261029-k555-exact-construction-v1.json`. **Provenance disclosure:** the first run at 05:29:32 PDT wrote bytes with SHA `74ea6f49aa784bc8436d7a289f35e53789823cfdf70055932747c4fbe79ff045`. An unintended identical re-execution (an in-kernel `runpy` load at 05:29:45) regenerated the file. The current bytes have SHA `4de4f0e3cbd47825d423d00ed741a1aeb46729b1ee8c52945d94a65e07d1aa65`, and only `clock_finish` differs.
- A floating-point cross-check gave a maximum basis error of 2.0e-15. The numerical commutant dimension is 1.

*Discovery path.* A covariant search was run under G = Z5^2 ⋊ Z3, which acts regularly on the 75 edges.
- Heisenberg-type projective representations gave only nonzero minima (0.0122 / 0.00575 / 0.0872 / 0.00182).
- 12 of 360 linear 3+3+3+1 representations gave zero residual.
- Calibration controls: the same code finds K2,2,2 and K4,4,4 immediately.
- The exact flat-diagonal reformulation then gives the cyclotomic phases above.

**Consequence.** Theorems A and B together form a genuine quantum Mann *dichotomy*. At m = 3 the classical parity obstruction survives quantization; at m = 5 it does not. The parity core of a Z2-quotient-labelled 1-RQLS(10) is therefore realizable, and realizable irreducibly. This differs from the reducible 4+6 cores analysed earlier. A no-go for cyclic-label 1-RQLS(10) cannot come from the 75-ray core alone.

## 3. Theorem C (computer-assisted, exact, restricted ansatz): no completion in the flat Z5^2-diagonal ansatz

*Ansatz.* A Z2-quotient 1-RQLS(10) of any cardinality has four quadrants Q_ij = R_i x C_j. Assume each quadrant is indexed by x in Z5^2 with flat vectors psi_q(x)_j = zeta5^{<c_j,x>} e^{i phi_{q,j}} / sqrt10, using one common character multiset T. Assume each of the six basis types is a pair of cosets of one line with an offset.

**Theorem C.** In this ansatz no full Z2-quotient 1-RQLS(10) exists.

For flat vectors, orthonormality is equivalent to two conditions:
- uniformity of T along each line used;
- one torus phase equation per frequency pair.

The torus system is solvable iff y·rhs = 0 mod 10 for an integer basis y of the left kernel.

Normalisations (WLOG):
- by GL(2,5), the K-part lines are (0,1), (1,0), (1,4);
- by quadrant re-indexing, the K-part offsets are 0;
- T is taken up to translation.

Search results:
- Admissible T: 220 in total, 16 up to translation.
- Only 4 of the 16 have a solvable K-part.
- Tested: every completion line triple and every Q11 offset pair. That is 13,600 cases, of which 3,325 have uniform T.
- **0 are solvable.**
- Numerical corroboration (in-kernel, not pinned): torus Levenberg–Marquardt on 25 sampled uniform cases gave minima of at least 1.958, while the K-part control reaches 0.

*Certificate.*
- Script `frontier-20261029-flat-diagonal-z5sq-completion-search-v1.py`, SHA-256 `585c04b8f2db270157301008919963b2802e0906d6b3c53247053dcb51b7a12a`.
- Result `frontier-20261029-flat-diagonal-z5sq-completion-search-v1.json`. **Provenance disclosure:** the first run at 05:31:35 wrote SHA `1180a694c0c7e5884bbfd3935c5fa8c0bb0662f55b183a50df3820440cf6a533`. An unintended in-kernel `runpy` load at 05:31:53 regenerated it. The current SHA is `931e2694cbbab17f92b55951f68ceda24522f899753a743adb4f872ecea01a84`, and only `clock_finish` differs.

**Direct check on the found object.** For the covariant K5,5,5 solutions, the 150 extra orthogonal pairs form exactly the transversal partitions that a completion needs. Every pairwise intersection of the R1/C1/T0 complements is exactly 1-dimensional, which forces the Q11 vectors. The forced Q11 rows, columns and label classes are orthonormal. However, those vectors miss their label complements: the best residual over the sampled continuous family is about 0.2254.

## 4. Remaining gap

Completion of an (irreducible) K5,5,5 core to all 100 cells is open beyond the stated ansatz. Open directions include:
- non-flat diagonal weights;
- Heisenberg or other non-diagonal actions;
- symmetry-breaking families.

Label squares without a Z2 quotient have no parity core and are untouched here. So are all other 1-RQLS(10) routes. Independent review is requested of:
- the written proof of Theorem A, especially Steps 3–6;
- the exact certificate of Theorem B;
- the integer-kernel criterion and the WLOG reductions of Theorem C.
