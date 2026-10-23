# FROZEN r2 — partial result: every AME(4,6) state has at least 46 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`). r1 (d5b076ba146bb6ea6f6a8eb21dce948ade563f2cf1f2c808e84350d0002ffc83) is unchanged.
This is a **correction-only revision**: the theorem and its dependency chain are those of r1. §7 gives a disposition
for every review item, and Appendix A is explicitly NON-load-bearing.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written.
- Model reviews of r1, both ACCEPT-WITH-FIXES with no FATAL item:
  - Codex CLI gpt-6.1-sol: `review/ame46-lower46-codex-review-v1.note.md`;
  - Claude CLI claude-opus-5-5: `review/ame46-lower46-claude-review-v1.note.md`.
- Independent parent bindings P1–P4 have passed. They are pinned in §5 (Claude P5).
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The target is 59 versus 60; this file proves
  only the lower bound 46.
- **Builds on** `review/SUPPORT_LOWER42.r2.md` (1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418),
  cited as L42 with its line numbers (LF):
  - the AME definition (LF32–34);
  - the reshaping lemma (LF42–46);
  - the reduction to the computational basis (LF47–50);
  - the definitions of §0 (LF51–62), including e (LF54);
  - Lemmas 1–11, cited as L42-1 … L42-11, including L42-9 (e = 0);
  - the case arguments for t = 33–36 and the by-product corollary (LF202–204).
- **Cited theorem:** Tarry's theorem (no pair of orthogonal Latin squares of order 6), for t = 36 only, through L42.
  - The nonexistence of AME(4,2) is used for t = 32. Lemma 15 proves it in full by the standard Pauli-weight and
    spin-flip argument; that proof was supplied by the parent orchestrator and checked here.
  - The result is due to Higuchi–Sudbery (cited by Pandya LF46–47, ref. [10]), and no novelty is claimed for it.
- **Computer-assisted part:** five cases (t, e) ∈ {(30,0), (30,2), (30,3), (29,2), (28,0)} are excluded by an
  exhaustive enumeration (§3), with the outputs in §4.
  - **UNSAT basis.** The 18 pinned CNF/LRAT pairs were re-verified by the parent:
    - LRAT ids, hints and deletions are discarded;
    - the addition sequence is converted to DRAT additions and checked by the parent's pinned drat-trim in ASCII
      RUP-only mode (`-I -U`, so RAT is not used) against the original pinned CNFs;
    - all 18 VERIFIED (§5).
  - The worker's two LRAT checkers (C and Python) were written by the same author and share RUP semantics. They are
    reproducibility only and NOT load-bearing.
- No novelty or priority claim. Crowded field; a search miss is not novelty.

## Theorem

Let ψ ∈ (C^6)^{⊗4} be an AME(4,6) state, i.e. a state with every two-party reduced density matrix equal to I/36 (L42
LF32–34). Arbitrary complex amplitudes are allowed. For every product orthonormal basis, at least 46 of the 1296
coefficients of ψ are non-zero.

By the basis reduction (L42 LF47–50), it suffices to prove s ≥ 46 for every AME state in the computational basis.
Nothing below assumes real amplitudes or equal moduli.

## 1. Additional lemmas (written)

Notation is that of L42 §0: S, s, T, t, N, e, h = 36 − t, d_{i,a}, D_j^{(i,a)}, V_i, lines, components, e_K.
- s = t + |N| and e = s − (72 − t) (L42 LF53–54), so |N| = 2h + e.
- An element of N is called non-classical.
- A line is a **hole line** if it meets N. By L42-2(a) and L42-4, these are exactly the lines containing no classical
  officer.

**Lemma 12 (slices see whole value sets).** For every coordinate i, value a and partner j ≠ i, D_j^{(i,a)} ⊆ V_j.
Hence d_{i,a} ≤ |V_j|.
*Proof.* For b ∈ D_j^{(i,a)}, the line (x_i, x_j) = (a, b) contains elements y ∈ N (L42-8), and y_j = b. By
L42-8(c), b ∈ V_j. Also |D_j^{(i,a)}| = d_{i,a}. ∎

**Lemma 13 (t = 31 is impossible, for every e).**
*Proof.*
- h = 5. For each i, the positive deficits are ≥ 2 (L42-8(a)) and sum to 5 (L42-8(b)), so the profile is {5} or
  {3, 2}. In particular |V_j| ≤ 2 for all j, and some d_{1,a} ≥ 3.
- Lemma 12 gives |V_2| ≥ 3. Contradiction. ∎

**Lemma 14 (closure).** Let K be a connected component of a unitary matrix with k ≥ 2 rows. For 0 < k′ < k, no k′
rows of K are supported within k′ columns.
*Proof.*
- Such rows would be k′ orthonormal vectors in the k′-dimensional coordinate space of those columns, so they would
  span it.
- Every other row is orthogonal to them, so it vanishes on those columns.
- Then those k′ rows and k′ columns form a union of components, and K would be disconnected. ∎

Lemma 14 is used only by the filter in §3 step 4(a), which excluded nothing (m5).

**Lemma 15 (no AME(4,2); standard theorem, elementary proof).** No four-qubit pure state has all six two-qubit
marginals equal to I/4.
*Proof.*
- **Setup.** Let ρ = |ω⟩⟨ω| be such a state. Expand ρ = (1/16) Σ_P r_P P over the 256 Pauli strings
  P ∈ {I, X, Y, Z}^{⊗4}, with r_P = tr(ρP) ∈ R and r_{I⊗4} = 1. Let wt(P) be the number of non-identity factors, and
  A_w := Σ_{wt(P)=w} r_P².
- **A1 = A2 = 0.** A Pauli string of weight 1 or 2 acts on at most two qubits. So r_P = tr(ρ_ab P_ab) = tr(P_ab)/4 = 0.
- **A3 = 12.**
  - Each one-qubit marginal is I/2, the partial trace of a two-qubit marginal.
  - For the pure state ω, the marginal on three qubits {a, b, c} has the same non-zero spectrum as the marginal on the
    fourth qubit, namely {1/2, 1/2}. So tr ρ_abc² = 1/2.
  - Since ρ_abc = (1/8) Σ_Q r_{Q⊗I} Q over three-qubit Pauli strings Q, this gives (1/8) Σ_Q r_{Q⊗I}² = 1/2, i.e.
    Σ_Q r_{Q⊗I}² = 4.
  - The identity contributes 1, and weights 1 and 2 contribute 0. So the weight-3 strings supported on {a, b, c}
    contribute 3.
  - Each weight-3 string is supported on exactly one triple, so summing over the four triples gives A3 = 12.
- **A4 = 3.** tr ρ² = 1 gives Σ_P r_P² = 16, so A4 = 16 − 1 − 0 − 0 − 12 = 3.
- **Spin flip.** Let ρ̃ := Y^{⊗4} ρ̄ Y^{⊗4}, where ρ̄ is the entrywise complex conjugate in the computational basis.
  - **ρ̃ is positive semidefinite.** If ρ = Σ λ_k |v_k⟩⟨v_k| with λ_k ≥ 0, then ρ̄ = Σ λ_k |v̄_k⟩⟨v̄_k| is positive
    semidefinite. Y^{⊗4} is unitary and Hermitian, so ρ̃ = Y^{⊗4} ρ̄ (Y^{⊗4})† is too.
  - For single-qubit Paulis, Ī = I, X̄ = X, Ȳ = −Y, Z̄ = Z, and Y I Y = I, Y X Y = −X, Y(−Y)Y = −Y, Y Z Y = −Z. So
    Y^{⊗4} P̄ Y^{⊗4} = (−1)^{wt(P)} P.
  - Since r_P is real, ρ̃ = (1/16) Σ_P (−1)^{wt(P)} r_P P.
- **Contradiction.** Using tr(PQ) = 16 δ_{PQ},
  tr(ρ ρ̃) = (1/16) Σ_P (−1)^{wt(P)} r_P² = (A0 − A1 + A2 − A3 + A4)/16 = (1 − 0 + 0 − 12 + 3)/16 = −1/2.
  This is negative, but the trace of a product of two positive semidefinite matrices is non-negative. ∎

**Lemma 16 (t = 32 is impossible, for every e).**
*Proof.*
- **Profile.** h = 4. Each coordinate's positive deficits form the profile {4} or {2, 2}.
  - If coordinate i had {4}, with V_i = {a}, then Lemma 12 would give |V_j| ≥ d_{i,a} = 4 for j ≠ i. But |V_j| ≤ 2.
  - So |V_i| = 2 for all i, and N ⊆ V_1 × V_2 × V_3 × V_4 (L42-8(c)).
- **Hole lines of each pair {i, j}.**
  - The 32 officers occupy 32 distinct lines of the pair (L42-3), and a line without an officer meets N (L42-4). So
    the pair has 36 − 32 = 4 hole lines.
  - Their values form {(x_i, x_j) : x ∈ N} ⊆ V_i × V_j, a set of four cells. So the hole lines are exactly the four
    lines with values in V_i × V_j.
- **Unitary 4×4 blocks.**
  - In U_12|34, every non-classical component (L42-6) has its rows in V_1 × V_2 and its columns in V_3 × V_4.
  - These four rows and four columns carry no classical entry (L42-2(a)).
  - So the 4×4 submatrix on (V_1 × V_2) × (V_3 × V_4) is the direct sum of the non-classical components, which is
    unitary. The same holds for U_13|24 and U_14|23, for every e.
- **Reduction to four qubits.**
  - Identify V_i with {0, 1} and let ω := 3ψ|_{ΠV_i}.
  - Summing L42-1 over the four hole rows of U_12|34 gives Σ_{x∈N} 36|ψ_x|² = 4, so ‖ω‖² = 9 · 4/36 = 1.
  - Let M_π be the reshaping of 2ω for the pairing π = (ab|cd), with M_π[(x_a,x_b),(x_c,x_d)] = 2ω_x. Then M_π is
    the unitary 4×4 block above, since 2ω_x = 6ψ_x.
  - As in L42 LF42–44 with d = 2: ρ_ab = M_π M_π†/4 = I/4 and ρ_cd = (M_π† M_π)^T/4 = I/4.
  - So every two-qubit marginal of ω equals I/4, contradicting Lemma 15. ∎

## 2. Proof of the Theorem (case table)

Suppose ψ is AME(4,6) with s ≤ 45. By L42-4, t ≥ 72 − 45 = 27, and e = s − 72 + t.

| t | allowed e (from s ≤ 45) | status | reason |
|---|---|---|---|
| 36 | — | impossible | Tarry (L42 §2) |
| 33, 34, 35 | any | impossible | L42 §2 and its corollary (L42 LF202–204) |
| 32 | any | impossible | Lemma 16 (with Lemma 15) |
| 31 | any | impossible | Lemma 13 |
| 30 | 0, 1, 2, 3 | impossible | e = 1: L42-7(b), (c). e ∈ {0, 2, 3}: §3 and §4 |
| 29 | 0, 1, 2 | impossible | e = 0: t odd (L42 LF202–204). e = 1: L42-7. e = 2: §3 and §4 |
| 28 | 0, 1 | impossible | e = 1: L42-7. e = 0: §3 and §4 |
| 27 | 0 | impossible | t odd with e = 0 (L42 LF202–204) |

Every row is impossible, so s ≥ 46. ∎

## 3. The exhaustive procedure for one pair (t, e)

Fix (t, e) and suppose ψ is an AME state with these parameters. The code is the frozen engine `code/large_t_gen.py`,
with helpers from `code/large_t_e0.py` and `code/ame_e0_cnf.py`; §5 pins the full SHA-256 values.

### 1. Profiles (written derivation; Claude m1)

For each coordinate, the positive deficits form a partition of h into parts ≥ 2 (L42-8(a), (b)). Its largest part is
at most min_{j≠i} |V_j| (Lemma 12), hence at most 4 here.
- **h = 6.** A partition of 6 into parts ≥ 2 has at most 3 parts, so every part is ≤ 3. That excludes {6} and {4,2},
  leaving {3,3} and {2,2,2}. A {3,3} coordinate forces the other three to have ≥ 3 parts, i.e. to be {2,2,2}. This
  gives exactly {3,3}{2,2,2}³ and {2,2,2}⁴.
- **h = 7.** A partition of 7 into parts ≥ 2 has at most 3 parts, so every part is ≤ 3. The only partition of 7 into
  parts in {2, 3} is {3,2,2}. This gives {3,2,2}⁴.
- **h = 8.** A partition of 8 into parts ≥ 2 has at most 4 parts, so every part is ≤ 4. That excludes {8}, {6,2} and
  {5,3}.
  - {4,4} or {4,2,2} forces the other three to be {2,2,2,2}, the only partition with 4 parts.
  - {3,3,2} forces each of the others to be {3,3,2} or {2,2,2,2}.
  - This gives seven profiles, exactly those of §4.

The code's `profiles` lists the same 2, 1 and 7 profiles, and the parent's independent enumeration agrees (§5, P1).

**Normalization.** Local permutation unitaries map AME states to AME states (L42 LF47–50). A party permutation also
maps AME states to AME states, because it permutes the six two-party marginals. Both preserve s, t and e, and act on
points as in L42-11. So we may assume:
- the coordinates carry the partitions in the code's order;
- V_i = {6 − |V_i|, …, 5};
- the parts are assigned to the values of V_i in non-increasing order.

### 2. The base CNF on Π V_i (Claude M1: exact clause families)

There is one variable n_x per point x ∈ Π V_i, numbered in `itertools.product` order. `large_t_e0.Small.__init__`
(`code/large_t_e0.py` lines 61–70) adds no clauses. `large_t_gen.SmallGen.build_gen` (`code/large_t_gen.py` lines
42–85) adds exactly four families:
- **F1 (lines 44–56), lines 0 or ≥ 2.** For each pair i < j and (a, b) ∈ V_i × V_j, a hole-line indicator v with
  v → ∨(points of the line) and point → v, plus, for each point x of the line, x → ∨(other points of the line). So a
  line meets N in 0 or ≥ 2 points (L42-2(a), L42-4).
- **F2 (lines 57–64), hole counts.** For each ordered pair (i, j) and a ∈ V_i, exactly d_{i,a} of the indicators
  (a, b), b ∈ V_j, are true. Sequential-counter `eqk` from `large_t_e0.py` lines 75–84 is used, via
  `ame_e0_cnf.CNF.at_most_k`. Necessity: the lines (a, b) with b ∈ D_j^{(i,a)} meet N (L42-8), and these b lie in V_j
  (Lemma 12). Every other line through x_i = a holds an officer, hence no point of N (L42-2(a)).
- **F3 (line 65), cardinality.** Exactly 2h + e points; |N| = 2h + e as noted in §1.
- **F4 (lines 66–85), combinatorial orthogonality.** For each of the three reshapings, in both orientations (rows
  versus columns and columns versus rows): if rows r1 ≠ r2 share a column of N, they share a second one (L42-5).
  Auxiliaries a_c → n(r1,c) ∧ n(r2,c) are used.

There is **no** exactly-two family, phase family or symmetry-breaking family. Those exist only in
`large_t_e0.Small.build`, which is used solely by the e = 0 consistency run below. Every true N satisfies F1–F4, with
the indicator and auxiliary values it determines (the necessary-constraint extension).

Controls:
- the parent's e > 0 positive control `review/ame46-e-positive-control-v1/result.json`: a real (27,2) support planted
  in `build_gen(e = 2)` is SAT, and removing one point is UNSAT;
- Pandya's e = 0 support (`evidence/engine_control.json`).

### 3. Complete enumeration and orbit transfer (Claude M2, m7)

**Groups.** G is the group generated by local value permutations of each coordinate and by party permutations. H ⊆ G
fixes the normal form: coordinate permutations preserving the assigned partitions, and permutations of each V_i that
preserve d.

**Enumeration.** The code repeats: solve, then add one blocking clause ∨_{x∈X} ¬n_x for every image X of the solution
under H. Every blocking clause is all-negative with exactly 2h + e literals, so under F3 it excludes exactly the
support X. The loop stops at UNSAT.

**State-level orbit transfer.** Suppose ψ is an AME state whose non-classical support is N(ψ) = g(N0), for a listed
representative N0 and some g ∈ G. Applying the corresponding local permutation unitaries and party permutation gives
an AME state with non-classical support N0. The checks in step 4 are necessary conditions on N alone. So excluding N0
excludes every G-image of it, and membership in H is irrelevant to completeness.

**Completeness.** By the necessary-constraint extension, a true N satisfies the base CNF. The final UNSAT then forces N
to be a blocked support, i.e. an image of a listed representative, and that representative is excluded. The parent's
binding (§5, P3) independently verifies two things:
- the blocking clauses are exactly the H-orbit unions of the 28 listed representatives. There are 164,752 images:
  144, 78,192, 21,600, 16 and 64,800 for (30,0){3,3}, (28,0){4,4}, {4,2,2}, {3,3,2}⁴ and {2,2,2,2}⁴;
- an independent C enumerator of all N satisfying F1–F4 reproduces these orbit unions, which is a CNF-independent
  coverage route.

### 4. Exclusion of each representative N0

Each check is a necessary condition for realizability. The first failure is recorded.
- **(a) Components** (L42-6, L42-7, Lemma 14). Valid, but it excluded nothing (m5).
- **(b) Moduli** (exactly verified Stiemke vector).
  - Some m > 0 has every hole-line sum equal to 1 (A m = b): m_x = 36|ψ_x|² satisfies this, by L42-1 and because hole
    lines hold no officer.
  - Exclusion would need an exactly verified rational w with Aᵀw ≥ 0, bᵀw ≤ 0 and (Aᵀw ≠ 0 or bᵀw < 0).
  - The executed path, `moduli_certificate`, finds candidates by a floating LP and verifies them exactly.
  - The routine `moduli_lp` (sympy `lpmax`, `code/large_t_gen.py` lines 112–136) and the docstring lines 13–18 that
    describe it are obsolete and were never called. The frozen bytes are unchanged.
  - Moduli excluded nothing (m5).
- **(c) 2×2 phases** (L42-10). This excluded 24 representatives.
  - The engine checked consistency over R/2πZ by an exact Hermite reduction, but **stored only booleans**. The r1
    phrases "certificate-producing", "re-verified" and "verified integer certificate" therefore described unrecorded
    run-time artifacts; they are withdrawn (Claude M3).
  - The load-bearing certificates are the parent's: 24 ±1 certificates reconstructed by a read-only audit, bound to
    the exact engine representatives, and machine-checked by the parent's checker (§5, P4). Its criteria:
    - the four corners lie in N0;
    - in the stated reshaping, the block's two rows and two columns each contain exactly two N0-points;
    - the + signs sit on one diagonal;
    - the signed sum of the forms is the zero form;
    - the number of terms, counted with multiplicity, is odd.
  - The lane's own certificates (`evidence/lower46_phase_certificates.json`, 24/24) are same-author reproductions
    and are not load-bearing.
- **(d) Classical completion.** This excluded 4 representatives: (30,0) ×1, (28,0){4,4} ×2 and (28,0){3,3,2}⁴ ×1.
  - The CNF asks for a set T that avoids every hole line and meets every other line exactly once (L42-1, L42-3,
    L42-2(a)).
  - The parent regenerated the 4 completion CNFs from N0 without worker code, byte-identically. Their encoding
    soundness is in §5 (P2, P4), and their UNSAT is among the 18 RUP-verified pairs.

**Conclusion.** Every profile's final UNSAT is RUP-verified, and every representative is excluded. So no AME state has
these (t, e).

**e = 0 consistency run (Claude m4).** `code/large_t_e0.py` is a same-code consistency run with zero evidential
weight:
- it shares `ame_e0_cnf.py` and `phase_check.py` with the main engine;
- it adds the exactly-two family (L42-9), and was run without its CNF-level phase families;
- it excluded its (28,0) representatives with the same per-representative exact phase check and completion check, not
  with CNF phase clauses;
- its proofs are not among the 18.

## 4. Results of the procedure

Frozen engine `code/large_t_gen.py`, run 2026-10-17 12:25:16–12:32:52 PDT. Reasons are per orbit representative, and
orbit sizes are under H. "Final UNSAT" means the profile's last CNF, with all orbits blocked, is UNSAT. It is
RUP-verified by the parent (§5).

| (t, e) | profile (deficit partitions per coordinate) | orbits (sizes) | exclusion reasons | final UNSAT |
|---|---|---|---|---|
| (30, 0) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 2 (108, 36) | 2×2 phase ×1; completion UNSAT ×1 | yes |
| (30, 0) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 2) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 2) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 3) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 3) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (29, 2) | {3,2,2} {3,2,2} {3,2,2} {3,2,2} | 0 | — | yes |
| (28, 0) | {4,4} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 14 | 2×2 phase ×12; completion UNSAT ×2 | yes |
| (28, 0) | {4,2,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 7 | 2×2 phase ×7 | yes |
| (28, 0) | {3,3,2} {3,3,2} {3,3,2} {3,3,2} | 1 (16) | completion UNSAT ×1 | yes |
| (28, 0) | {3,3,2} {3,3,2} {3,3,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {3,3,2} {3,3,2} {2,2,2,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {3,3,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {2,2,2,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 4 | 2×2 phase ×4 | yes |

The (28, 0) orbit sizes are:
- {4,4}: 2592, 10368, 20736, 13824, 10368, 5184, 5184, 1728, 2592, 2592, 1296, 432, 864, 432 (sum 78,192);
- {4,2,2}: 2592, 5184, 1728, 5184, 5184, 864, 864 (sum 21,600);
- {2,2,2,2}⁴: 10368, 31104, 20736, 2592 (sum 64,800).

No representative was excluded by components or by moduli. All five cases are excluded.

## 5. Executable record (Claude P5, m6)

All lane paths are relative to `physics/evidence/six-lane-20261016/ame46-support/`. Parent paths are relative to
`institute/runs/six-lane-2026-10-16/review/` and are read-only here. All runs are on 2026-10-17, PDT.

**Load-bearing (independent of the worker's checkers)**
- **P5/M4: UNSAT of the 18 pinned CNFs.** `ame46-lower46-parent-inputs-v1/addition-replay-result.json`
  (e616298744a44be43727fddbe9b3bb0a68b446df0c40bc16b9695a16cc69d230), run 12:56:04–13:00:32: 18 pairs, 18 VERIFIED,
  verdict PASS.
  - drat-trim checker binary SHA-256 a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37, flags `-I -U`
    (ASCII, RUP only; RAT not used).
  - Converter `lrat_additions_to_drat.py` (e13ff89105eee2c87bf06e17a210fc989c82fa2df8688ffb6760d8040147965f): LRAT
    ids, hints and deletions are discarded.
  - Driver `recheck_additions.py` (10a572658f54a7b57de02458893ba2fce7aa84693df1c0a32022ff00b711e24d).
  - Pipeline controls: `conversion-smoke-result.json`
    (aa20532b03c569336c4712022e6090b46c9d42738b94966537bb54d2d487c64d). Three bogus empty-clause SAT cases are NOT
    VERIFIED; genuine conflict, satisfied-hint and deletion cases are VERIFIED.
  - The per-pair CNF and proof SHA-256 values and the VERIFIED lines are in `addition-replay-v1/p*.json`. They match
    `evidence/lower46_receipt.json`.
- **P1/P3: profiles, base-CNF identity and blocking orbits.**
  - `ame46-lower46-parent-binding-v1/binding-result.json`
    (6589167609d6478d300371e6de388adcabe3a8d6e053ab157388d1cb0b4febf9).
  - `enum-runs.json` (229f4d7edf8a121ce54879c04acd2a7cb39640c18ec1b48a48d97b772b469f4d): the independent C enumerator.
  - `controls-result.json` (7b425d47bdeb7693789db7c92332cbd7bb5131e4b42945ac185c65a6fd04d3d7).
  - Parent replay `ame46-lower46-binding-parent-replay-v1.json`
    (6a967c71384897004d3f900b5ac0dddb5d16130959f058704e2a71d70671aa37): PASS on all 14 profiles, all 28
    representatives and 164,752 images.
- **P2: completion CNFs.** `ame46-lower46-completion-binding-result-v1.json`
  (96d55f3c1c797b20143027855ba6f5dafa4de8ab008588ed13535748258642b7): the 4 CNFs were regenerated from N0 without
  worker code and are byte-identical, PASS.
- **P2: e > 0 positive control.** `ame46-e-positive-control-v1/result.json`
  (09c0844b5c4f4c206648d9b3d9de2f8f0cd262f744e142cb4fb1b715b36879c0): PASS.
- **P4/M3: phase certificates.** `ame46-lower46-parent-phase-check-v1/`:
  - table `certificates-from-audit.md`: 537a788e37259de937d96dc97911c3bea6ae7879cf85ff423d4b14cc8ee319dd;
  - checker `phase_cert_check.py`: 45ca5b278df787a831189cf74ddc9707fa4a739e32acd0a46e43ef619281176a;
  - result `result.json`: 38f35f244bbcbbc568a4a2fbcf8282dbdc82d56ee77f6881b923cc693784fea1. 24/24 PASS, bound to the
    exact engine representatives, and 7 negative controls rejected.

**Worker inputs, pinned in full**
- **Engine:** `code/large_t_gen.py` 28c0c1f9e32089d0080869689be6ea7fd3dd93ae5239cf0c7131cf4c4607bcfd;
  `code/large_t_e0.py` 67033dcfc2e41d29f73c235ac422857be33f684135102e7c5739b303a755466c; `code/ame_e0_cnf.py`
  97e30ae4e825440653a50e3de84389b00122fa70d3bbddb42924ccdd6ed78a26; `code/phase_check.py`
  0c591d1b1188a536c88831fb632f92b78b5f771c473d2d2f6fdff99ca728f693.
  - Command: `cd code && OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B large_t_gen.py --t T --e E`.
- **Interpreter.**
  - `../../depolarizing/env/bin/python` is a symlink, in another lane's venv (uv 0.9.8, no lockfile), to
    `/opt/homebrew/Cellar/python@3.13/3.13.9_1/Frameworks/Python.framework/Versions/3.13/bin/python3.13`. Its binary
    SHA-256 is 50018add1e0d9b253f6466d9de81ea2aaea7ef4bd664db219e2d16cfe66e395b, and `sys.version` is
    `3.13.9 (main, Oct 14 2025, 13:52:31) [Clang 17.0.0 (clang-1700.3.19.1)]`. scipy 1.18.1 and numpy 2.5.4 were used
    only by the unused moduli candidate search.
  - `code/lower46_receipt.py` ran under `/usr/bin/python3`, i.e.
    `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/bin/python3.9`. Its SHA-256
    is 4c0dd940cd1e299dab25441c4e7a468e11dcf771f77e82207479fc2fc7df6a60, and the version is 3.9.6.
- **CaDiCaL:** `/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical`, version 3.0.1, SHA-256
  601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa. Build: Apple clang 21.0.0, `-Wall -Wextra -O3
  -DNDEBUG -DNCLOSEFROM`, Sun Jul 19 15:40:55 UTC 2026, Darwin arm64.
- **Reports:**
  - `evidence/large_t_gen_t30_e0.json` 5b586a2d6ed1af70000962b77d783ff675321ed2679be519cf7c2588c7413922;
  - `evidence/large_t_gen_t30_e2.json` 8b3f3fc6c9491d5d21d7f9d1a377703ca7493e5954267f1ef484f28c918e0770;
  - `evidence/large_t_gen_t30_e3.json` 05d5089abd3e6798f72182932c63935f99b73c92a47ce319031823ccb1a20985;
  - `evidence/large_t_gen_t29_e2.json` 478d8d8c139f5bd24677123055e0806822eb2e83efb20f70790e4c929a75692f;
  - `evidence/large_t_gen_t28_e0.json` 267294dd07ef0f3423a4cfc02ddc8c5f3271a57f1f1b51c4ace4707af54e8c74.
- **Worker receipt:** `code/lower46_receipt.py` (11ffd3d4c3f6f95bf78765d4641103293eb8fbd7b720c125251aeff991d5a725)
  produced `evidence/lower46_receipt.json` (05729155a438f04e4b34ca977ec9cdd07268609bbb5fd86b9e983b14981bf3fe), run
  12:40:16–12:44:04.
  - It pins the 18 CNF/LRAT pairs. The raw proofs are in `explore/large_t_gen/`.
  - Its lines 67–70 contain stale keys (`moduli_ok`, `moduli_lp_max_eps`) on a branch that is never taken. The
    recorded reasons are correct. The receipt is not regenerated, because the parent's replay supersedes it (m5).

**Not load-bearing** (reproducibility only)
- The worker's LRAT checkers `code/lratcheck` (C; binary b4e14cd923e94f07fbbff5cf4a3e3cff617b13f8db33d3428d64a04a23813470,
  source e9da1fa8cfe3804d04378fb625b9ce116d00f085b9e8f0cb6bca3b3814fe5159) and `code/lratcheck_py.py`
  (7bc9cff72805842a711385e2dbdcdf39305efd13788d079ccdacc61938bc7edd). Both are by the same author.
  - Their satisfied-hint handling is sound but moot. Six satisfied hints occur in two (28,0) proofs, which fail the
    Python strict mode.
  - `evidence/lrat_soundness_tests.json` (e9e064668fb666c40bbcfd72f82d6fa9cd752e181b43a45b13472dc199354230).
- The lane's phase certificates: `code/lower46_phase_certs.py`
  (b09526e84f959d8748fff337f614e476d1d9a9d70e622f9d5f4e57e1de7d56ea) using `code/phase_cert.py`
  (fbe3ab68899fec97486f1ce126749e820087d09fe5f12f2773199306883cb54e) produced
  `evidence/lower46_phase_certificates.json` (94dc8db5b6e06d22999fc618e7f89abc145c679cc1b21f5b94b3173eb547cd63),
  24/24.
- Controls: `evidence/engine_control.json` (9b6a3f21d87eac276e0d8fd1bd6f514877df3961806e02e0c3052d0365118500) and
  `evidence/moduli_cert_tests.json` (9b6827482565cfb99bb985d64d4e75b9f6df8e94e0ed36fe36be1790cd3fca91).
- The e = 0 consistency run: `evidence/large_t_e0_t30_nophase.json` and `evidence/large_t_e0_t28_nophase.json`.

## 6. Not claimed

- Nothing about 59 versus 60 beyond the bound 46. Combined with Pandya's upper bound 60, which is not re-reviewed
  here, the range is 46..60.
- No unverified SAT result is used. UNKNOWN runs, runs without proofs and the t = 14 explorations are not part of this
  proof.
- No novelty or priority claim. Lemma 15 is a standard theorem with a standard proof.

## 7. Review dispositions (changes from r1)

Codex (`review/ame46-lower46-codex-review-v1.note.md`, 8fa1e871be5e10c9a428742cb9d08c1bfabae9e3b8e96d1c0779489734dd4a13):
- MINOR 1 (checker independence): fixed in the header and §5. The parent's RUP replay is cited.
- MINOR 2 (certificates discarded): fixed in §3 step 4(c) and §5. The parent's table, checker and result are pinned.
- MINOR 3 (stale moduli description): fixed in §3 step 4(b). The routine is marked obsolete and never called.

Claude (`review/ame46-lower46-claude-review-v1.note.md`, bce81129783f15b34cc73fbab1f9a88bd5dc0dfa474efff7dd1bd4c2b4138748):
- **M1** (clause content): fixed in §3 step 2.
  - The four families F1–F4 are listed with code line references.
  - There is no exactly-two, phase or symmetry family, and `Small.__init__` adds nothing.
  - The e > 0 planted positive control and the parent's independent binding and enumeration are pinned.
- **M2** (blocking clauses): fixed in §3 step 3. The parent's binding verifies the blocking clauses as exact orbit
  unions (164,752 images, matching the orbit sums), with an independent C enumerator.
- **M3** (phase record): fixed in §3 step 4(c). The engine claims are withdrawn as unrecorded. The parent's bound
  certificates and checker criteria are stated and pinned.
- **M4** (UNSAT basis): fixed in the header and §5.
  - The basis is the parent's addition-only RUP replay (drat-trim SHA, flags `-I -U`, per-pair SHAs and VERIFIED).
  - The worker checkers and the satisfied-hint text are demoted to non-load-bearing.
  - "independently written" is deleted.
- **m1:** the written profile derivation is inserted (§3 step 1).
- **m2:** citations fixed:
  - L42 LF42–50, LF202–204 and L42-9 are added;
  - in Lemma 16, "a line without an officer meets N" is L42-4;
  - the case table cites LF202–204;
  - party permutations permute the six two-party marginals;
  - |N| = 2h + e follows from L42 LF53–54.
- **m3:** the Theorem states complex amplitudes and cites L42 LF32–34 and LF47–50.
- **m4:** the e = 0 run is relabelled a same-code consistency run, with its exclusion mechanism stated.
- **m5:** filters (a) and (b) excluded nothing and are not part of the proof. The dead moduli code is marked never
  called. The stale receipt keys are explained but not regenerated, because the frozen bytes stay and the parent's
  replay supersedes the receipt.
- **m6:** absolute interpreter paths, `sys.version`, binary SHA-256 values, the CaDiCaL SHA and build options, full
  SHA-256 values and dates are recorded. The venv belongs to another lane and has no lockfile; that is recorded, not
  fixed.
- **m7:** the state-level orbit transfer is used, and G is defined. H-membership is irrelevant.
- **m8:** Lemma 15 now justifies that ρ̃ is positive semidefinite, and Lemma 16 writes out ρ_ab and ρ_cd.

Claude's LOWER48 review (M1 note, `review/ame46-lower48-claude-review-v1.note.md`) observes that r1 LF142–143 assert
H maps CNF solutions to CNF solutions and preserves every check. That rests on the same unproved syntactic symmetry,
and it is withdrawn. §3 step 3 now argues through true supports, which needs neither property: a blocked true N
equals h(Y) for a representative Y, and Y = h⁻¹(N) is itself a true support.

Parent: Appendix A is NON-load-bearing, and the dependency chain is identical to r1.

No mathematical conclusion changed. The frozen code and evidence bytes of r1 are unchanged.

## Appendix A (NON-load-bearing): written exclusions of the completion representatives

This appendix is not part of the proof above; the dependency chain of the theorem is exactly that of r1. It records
that the four completion representatives are also excluded by written arguments, proved in
`review/SUPPORT_LOWER48.r1.md` §1 (0457570502535eb3bb6aaa8002f81ca640451c8364079c9e0f4cc9413fb49f95):
- (30,0), profile {3,3}{2,2,2}³: LOWER48 Lemma 17 (officer counting) gives f(1) = 9 − 42 + 30 = −3;
- (28,0), profile {3,3,2}⁴: f(1) = 6 − 40 + 28 = −6;
- (28,0), profile {4,4}{2,2,2,2}³, two representatives: LOWER48 Lemma 18, the parent orchestrator's binary-code
  argument.
The Codex reviewer of r1 recovered the same three exclusions independently.
