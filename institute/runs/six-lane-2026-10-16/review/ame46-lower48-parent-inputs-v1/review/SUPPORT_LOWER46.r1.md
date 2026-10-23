# FROZEN r1 — partial result: every AME(4,6) state has at least 46 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`, `evidence/SHA256SUMS.txt`). Corrections go to r2.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written and not yet independently reviewed.
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The target is 59 versus 60; this file proves
  only the lower bound 46.
- **Builds on** `review/SUPPORT_LOWER42.r2.md` (SHA-256 1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418):
  - its §0 definitions;
  - its Lemmas 1–11 (cited here as L42-1 … L42-11);
  - its case arguments for t = 33, 34, 35, 36.
  Those arguments are not repeated.
- **Cited theorem:** Tarry's theorem (no pair of orthogonal Latin squares of order 6), for t = 36 only, exactly as in
  LOWER42 r2. The nonexistence of AME(4,2) is used for t = 32. It is proved in full in §1 (Lemma 15) by the standard
  Pauli-weight and spin-flip argument; that proof was supplied by the parent orchestrator and checked here. The result
  is due to Higuchi–Sudbery (cited by Pandya LF46–47, ref. [10]), and no novelty is claimed for it.
- **Computer-assisted part:** five cases (t, e) ∈ {(30,0), (30,2), (30,3), (29,2), (28,0)} are excluded by an exact,
  exhaustive, certificate-producing procedure (§3). Its finite outputs are pinned in §5. Every UNSAT claim carries an
  LRAT proof, checked by two independently written checkers (§5).
- No novelty or priority claim. Crowded field; a search miss is not novelty.

## Theorem

Every AME(4,6) state has at least 46 non-zero coefficients in every product orthonormal basis.

## 1. Additional lemmas (written)

Notation is that of LOWER42 r2 §0: S, s, T, t, N, e, h = 36 − t, d_{i,a}, D_j^{(i,a)}, V_i, lines, components, e_K.
An element of N is called non-classical. A line is a **hole line** if it meets N; by L42-2(a) and L42-4 these are
exactly the lines containing no classical officer.

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

**Lemma 15 (no AME(4,2); standard theorem, elementary proof).** No four-qubit pure state has all six two-qubit
marginals equal to I/4.
*Proof.*
- Let ρ = |ω⟩⟨ω| be such a state. Expand ρ = (1/16) Σ_P r_P P over the 256 Pauli strings P ∈ {I, X, Y, Z}^{⊗4},
  with r_P = tr(ρP) ∈ R and r_{I⊗4} = 1. Let wt(P) be the number of non-identity factors, and
  A_w := Σ_{wt(P)=w} r_P².
- **A1 = A2 = 0.** A Pauli string of weight 1 or 2 acts on at most two qubits. So r_P = tr(ρ_ab P_ab) = tr(P_ab)/4 = 0.
- **A3 = 12.** Each one-qubit marginal is I/2, the partial trace of a two-qubit marginal. For the pure state ω, the
  marginal on three qubits {a, b, c} has the same non-zero spectrum as the marginal on the fourth qubit, namely
  {1/2, 1/2}. So tr ρ_abc² = 1/2.
  - Since ρ_abc = (1/8) Σ_Q r_{Q⊗I} Q over three-qubit Pauli strings Q, this gives (1/8) Σ_Q r_{Q⊗I}² = 1/2, i.e.
    Σ_Q r_{Q⊗I}² = 4.
  - The identity contributes 1, and weights 1 and 2 contribute 0. So the weight-3 strings supported on {a, b, c}
    contribute 3.
  - Each weight-3 string is supported on exactly one triple, so summing over the four triples gives A3 = 12.
- **A4 = 3.** tr ρ² = 1 gives Σ_P r_P² = 16, so A4 = 16 − 1 − 0 − 0 − 12 = 3.
- **Spin flip.** Let ρ̃ := Y^{⊗4} ρ̄ Y^{⊗4}, where ρ̄ is the entrywise complex conjugate in the computational basis.
  ρ̄ and ρ̃ are positive semidefinite.
  - For single-qubit Paulis, Ī = I, X̄ = X, Ȳ = −Y, Z̄ = Z, and Y I Y = I, Y X Y = −X, Y(−Y)Y = −Y, Y Z Y = −Z. So
    Y^{⊗4} P̄ Y^{⊗4} = (−1)^{wt(P)} P.
  - Since r_P is real, ρ̃ = (1/16) Σ_P (−1)^{wt(P)} r_P P.
- **Contradiction.** Using tr(PQ) = 16 δ_{PQ},
  tr(ρ ρ̃) = (1/16) Σ_P (−1)^{wt(P)} r_P² = (A0 − A1 + A2 − A3 + A4)/16 = (1 − 0 + 0 − 12 + 3)/16 = −1/2.
  This is negative, but the trace of a product of two positive semidefinite matrices is non-negative. ∎

**Lemma 16 (t = 32 is impossible, for every e).**
*Proof.*
- h = 4. Each coordinate's positive deficits form the profile {4} or {2, 2}.
  - If coordinate i had {4}, with V_i = {a}, then Lemma 12 would give |V_j| ≥ d_{i,a} = 4 for j ≠ i. But |V_j| ≤ 2.
  - So |V_i| = 2 for all i, and N ⊆ V_1 × V_2 × V_3 × V_4 (L42-8(c)).
- Hole lines of each pair {i, j}:
  - The pair has 36 − t = 4 hole lines (L42-3: the 32 officers occupy 32 lines of the pair, and a line without an
    officer meets N).
  - Their values form {(x_i, x_j) : x ∈ N} ⊆ V_i × V_j, a set of four cells. So the hole lines are exactly the four
    lines with values in V_i × V_j.
- Unitary 4×4 blocks:
  - In U_12|34, every non-classical component (L42-6) has its rows in V_1 × V_2 and its columns in V_3 × V_4.
  - These four rows and four columns carry no classical entry (L42-2(a)).
  - So the 4×4 submatrix on (V_1 × V_2) × (V_3 × V_4) is the direct sum of the non-classical components, which is
    unitary. The same holds for U_13|24 and U_14|23.
- Reduction to four qubits:
  - Identify V_i with {0, 1} and let ω := 3ψ|_{ΠV_i}. Summing L42-1 over the four hole rows of U_12|34 gives
    Σ_{x∈N} 36|ψ_x|² = 4, so ‖ω‖ = 1.
  - The reshapings of 2ω are the three unitary 4×4 submatrices. By the computation of LOWER42 r2 §0 for d = 2, every
    two-qubit marginal of ω equals I/4. This contradicts Lemma 15. ∎

## 2. Proof of the Theorem (case table)

Suppose ψ is AME(4,6) with s ≤ 45. By L42-4, t ≥ 72 − 45 = 27, and e = s − 72 + t.

| t | allowed e (from s ≤ 45) | status | reason |
|---|---|---|---|
| 36 | — | impossible | Tarry (LOWER42 r2 §2) |
| 33, 34, 35 | any | impossible | LOWER42 r2 §2 and its corollary |
| 32 | any | impossible | Lemma 16 (with Lemma 15) |
| 31 | any | impossible | Lemma 13 |
| 30 | 0, 1, 2, 3 | impossible | e = 1: L42-7(b), (c). e ∈ {0, 2, 3}: §3 certificates |
| 29 | 0, 1, 2 | impossible | e = 0: t odd (LOWER42 r2 corollary). e = 1: L42-7. e = 2: §3 certificate |
| 28 | 0, 1 | impossible | e = 1: L42-7. e = 0: §3 certificate |
| 27 | 0 | impossible | t odd with e = 0 |

Every row is impossible, so s ≥ 46. ∎

## 3. The exhaustive procedure for one pair (t, e)

Fix (t, e) and suppose ψ is an AME state with these parameters. The code is `code/large_t_gen.py` with helpers from
`code/large_t_e0.py`, `code/ame_e0_cnf.py` and `code/phase_check.py`; §5 pins the SHA-256 values.

1. **Profiles.**
   - For each coordinate, the positive deficits form a partition of h into parts ≥ 2 (L42-8(a), (b)), with largest
     part ≤ min_{j≠i} |V_j| (Lemma 12).
   - The code lists all such 4-tuples of partitions up to the order of the coordinates (`profiles`: multisets of
     partitions, filtered by Lemma 12).
   - Local permutation unitaries and party permutations map AME states to AME states with the same s, t and e
     (LOWER42 r2 §0). Their action on points is that of L42-11. So we may assume:
     - the coordinates carry the partitions in the code's order;
     - V_i = {6 − |V_i|, …, 5};
     - the parts are assigned to the values of V_i in non-increasing order.
2. **N-only CNF on Π V_i.** Variables n_x for x ∈ Π V_i. The constraints, each a consequence of the lemmas:
   - every line meets N in 0 or ≥ 2 points (L42-2(a), L42-4);
   - for each ordered pair (i, j) and a ∈ V_i, exactly d_{i,a} of the lines (a, b), b ∈ V_j, meet N. The lines
     b ∈ D_j^{(i,a)} meet N (L42-8). Every other line through x_i = a contains a classical officer, hence no point of
     N (L42-2(a));
   - |N| = 2h + e (L42-7(c));
   - combinatorial orthogonality for the rows and for the columns of each reshaping (L42-5). Rows and columns
     outside the hole lines do not interact with N.
   The indicator of the true N satisfies the CNF, with suitable auxiliary values.
3. **Complete enumeration up to symmetry.**
   - H is the group of coordinate permutations preserving the assigned partitions, combined with permutations of
     each V_i preserving d. Each element of H extends to an element of G (identity outside V_i), maps CNF solutions
     to CNF solutions, and preserves every check in step 4.
   - The code repeats: solve, then add one blocking clause ¬(all points of the image) for every image of the
     solution under H. Every solution has exactly 2h + e points, so each clause blocks exactly one solution.
   - It stops at UNSAT, whose LRAT proof is checked. Hence every solution lies in the H-orbit of a listed
     representative.
4. **Exact certificates per representative N0.** Each of the following is a necessary condition for realizability.
   The first that fails is recorded:
   - (a) **components:** every component of each reshaping restricted to N0 is square with ≥ 2 rows, every row and
     column has ≥ 2 entries, e_K ≠ 1, and no k′ rows are supported within k′ columns (L42-6, L42-7, Lemma 14);
   - (b) **moduli:** some m > 0 has every hole-line sum equal to 1 (A m = b, with A the hole-line/point incidence
     matrix and b = 1). m_x = 36|ψ_x|² > 0 satisfies this, by L42-1 and because hole lines contain no officer and
     N ⊆ S.
     - Exclusion only by an exactly verified rational vector w with Aᵀw ≥ 0, bᵀw ≤ 0 and (Aᵀw ≠ 0 or bᵀw < 0).
       Soundness: if Aᵀw ≠ 0 then mᵀAᵀw > 0 ≥ bᵀw = mᵀAᵀw; if Aᵀw = 0 then bᵀw = 0, contradicting bᵀw < 0.
     - Candidates come from a floating LP (scipy HiGHS) and are rationalised. If exact verification fails, nothing is
       excluded.
     - An earlier exact-LP attempt with sympy 1.14 `lpmax` gave a wrong optimum on a test LP. It is not used anywhere.
   - (c) **2×2 phases:** the congruences of L42-10 on the 2×2 components are consistent over R/2πZ. Decided by an
     exact integer Hermite reduction; an obstruction is an integer left-kernel vector with odd coordinate sum,
     re-verified;
   - (d) **classical completion:** some set T avoids every hole line and meets every other line exactly once. A
     non-hole line is non-empty (L42-1), contains no point of N, and contains at most one officer (L42-3). This is a
     CNF, solved by CaDiCaL 3.0.1 with an LRAT proof, which is checked.
   A representative is excluded if (a), (b) or (c) fails, or if (d) is UNSAT with a checked proof. Exclusion
   transfers to its whole orbit (step 3).
5. **Conclusion.** If every profile's final UNSAT is certified and every representative is excluded, then no AME
   state has these (t, e).

**e = 0 cross-check engine.** `code/large_t_e0.py` adds the e = 0 consequence that every hole line has exactly two
points (L42-9) and drops the global cardinality. It is run without phase clauses for (30, 0) and (28, 0), and agrees.

**Controls.**
- `code/engine_control.py`: Pandya's N (t = 12, e = 0, relabelled into the engines' normal form) satisfies the CNFs of
  both engines, and one mutated point makes both UNSAT (`evidence/engine_control.json`, all_required_true).
- `code/moduli_cert_tests.py`: the moduli verifier rejects a w with Aᵀw = 0 and bᵀw = 0 (intended-reason negative),
  rejects bᵀw > 0, and rejects a negative entry of Aᵀw. It accepts true certificates for an infeasible toy, and finds
  no certificate for feasible patterns (`evidence/moduli_cert_tests.json`).
- `code/lrat_soundness_tests.py`: the parent's negatives N1–N4 and positive P1, plus N5–N7 and P2, give the expected
  outcome for both LRAT checkers (`evidence/lrat_soundness_tests.json`).

## 4. Results of the procedure

Final engine `code/large_t_gen.py` (SHA-256 28c0c1f9…bcfd), run 12:25:16–12:32:52 PDT. Reasons per orbit
representative; orbit sizes are under H. "Final enumeration UNSAT" means the profile's last CNF, with all orbits
blocked, is UNSAT with a checked LRAT proof.

| (t, e) | profile (deficit partitions per coordinate) | orbits (sizes) | exclusion reasons | final enumeration UNSAT LRAT-checked |
|---|---|---|---|---|
| (30, 0) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 2 (108, 36) | 2×2 phase obstruction ×1; completion UNSAT ×1 | yes |
| (30, 0) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 2) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 2) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 3) | {3,3} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (30, 3) | {2,2,2} {2,2,2} {2,2,2} {2,2,2} | 0 | — | yes |
| (29, 2) | {3,2,2} {3,2,2} {3,2,2} {3,2,2} | 0 | — | yes |
| (28, 0) | {4,4} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 14 | 2×2 phase obstruction ×12; completion UNSAT ×2 | yes |
| (28, 0) | {4,2,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 7 | 2×2 phase obstruction ×7 | yes |
| (28, 0) | {3,3,2} {3,3,2} {3,3,2} {3,3,2} | 1 (16) | completion UNSAT ×1 | yes |
| (28, 0) | {3,3,2} {3,3,2} {3,3,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {3,3,2} {3,3,2} {2,2,2,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {3,3,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 0 | — | yes |
| (28, 0) | {2,2,2,2} {2,2,2,2} {2,2,2,2} {2,2,2,2} | 4 | 2×2 phase obstruction ×4 | yes |

The (28, 0) orbit sizes, in the report, are:
- profile {4,4}: 2592, 10368, 20736, 13824, 10368, 5184, 5184, 1728, 2592, 2592, 1296, 432, 864, 432;
- profile {4,2,2}: 2592, 5184, 1728, 5184, 5184, 864, 864;
- profile {2,2,2,2}⁴: 10368, 31104, 20736, 2592.

No representative was excluded by components or by moduli. Every exclusion is either an exact 2×2 phase obstruction
(verified integer certificate) or a completion UNSAT with a checked LRAT proof. All five cases are excluded. The e = 0
cross-check engine agrees on (30, 0) and (28, 0).

## 5. Executable record

All paths are relative to the lane `physics/evidence/six-lane-20261016/ame46-support/`.

- **Engine.**
  - Command per case: `cd code && OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B large_t_gen.py --t T --e E`
    (Python 3.13.9, scipy 1.18.1, numpy 2.5.4; CaDiCaL 3.0.1).
  - Code SHA-256 values:
    - `large_t_gen.py` 28c0c1f9e32089d0080869689be6ea7fd3dd93ae5239cf0c7131cf4c4607bcfd;
    - `large_t_e0.py` 67033dcfc2e41d29f73c235ac422857be33f684135102e7c5739b303a755466c;
    - `ame_e0_cnf.py` 97e30ae4e825440653a50e3de84389b00122fa70d3bbddb42924ccdd6ed78a26;
    - `phase_check.py` 0c591d1b1188a536c88831fb632f92b78b5f771c473d2d2f6fdff99ca728f693.
- **Reports.**
  - `evidence/large_t_gen_t30_e0.json` 5b586a2d6ed1af70000962b77d783ff675321ed2679be519cf7c2588c7413922;
  - `evidence/large_t_gen_t30_e2.json` 8b3f3fc6c9491d5d21d7f9d1a377703ca7493e5954267f1ef484f28c918e0770;
  - `evidence/large_t_gen_t30_e3.json` 05d5089abd3e6798f72182932c63935f99b73c92a47ce319031823ccb1a20985;
  - `evidence/large_t_gen_t29_e2.json` 478d8d8c139f5bd24677123055e0806822eb2e83efb20f70790e4c929a75692f;
  - `evidence/large_t_gen_t28_e0.json` 267294dd07ef0f3423a4cfc02ddc8c5f3271a57f1f1b51c4ace4707af54e8c74.
- **Receipt.** `code/lower46_receipt.py` (11ffd3d4c3f6f95bf78765d4641103293eb8fbd7b720c125251aeff991d5a725) →
  `evidence/lower46_receipt.json` (05729155a438f04e4b34ca977ec9cdd07268609bbb5fd86b9e983b14981bf3fe). Run at
  12:40:16–12:44:04 PDT; all_required_true = true.
  - It pins all 18 CNF/LRAT pairs: each profile's final enumeration UNSAT, plus each completion UNSAT. The raw
    proofs are kept in `explore/large_t_gen/`, and their SHA-256 values are in the receipt.
  - All 18 are verified by `code/lratcheck` (C; source `lratcheck.c` e9da1fa8…5159, binary b4e14cd9…3470) and by
    `code/lratcheck_py.py` (7bc9cff7…7edd) in skip mode.
- **Satisfied hints.**
  - CaDiCaL emitted 6 hints that were already satisfied at the point of use, 3 in each of two proofs:
    `t28_e0_3-3-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat` and `t28_e0_2-2-2-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat`. Both
    checkers count these identically.
  - These two proofs fail the strict Python mode, which rejects any satisfied hint. The other 16 pass strict mode.
  - Skipping a satisfied hint is sound: it assigns nothing, and it never ends a check. Success requires a later
    falsified hint, i.e. an actual conflict.
- **Checker soundness tests.** `code/lrat_soundness_tests.py` (fb0fd942…9458) →
  `evidence/lrat_soundness_tests.json` (e9e064668fb666c40bbcfd72f82d6fa9cd752e181b43a45b13472dc199354230). Negatives
  N1–N7 fail and positives P1, P2 verify in both checkers; P2 fails strict mode, as intended.
- **Controls.**
  - `evidence/engine_control.json` (9b6a3f21d87eac276e0d8fd1bd6f514877df3961806e02e0c3052d0365118500): Pandya's N
    is accepted by both engines, and the mutation is rejected.
  - `evidence/moduli_cert_tests.json` (9b6827482565cfb99bb985d64d4e75b9f6df8e94e0ed36fe36be1790cd3fca91): the
    intended-reason negatives are rejected and the true certificates accepted.
- **e = 0 cross-check.** `evidence/large_t_e0_t30_nophase.json` (cd272534…418d) and
  `evidence/large_t_e0_t28_nophase.json` (a21179bd…dded): both excluded, with all LRAT checks verified.
- **Not part of this proof.** Earlier engine runs made with older code (the sympy LP, now removed; the strict
  checker), and the batch outputs for other (t, e).

## 6. Not claimed

- Nothing about 59 versus 60 beyond the bound 46.
- No unverified SAT result is used. Runs with UNKNOWN or without proofs, and the t = 14 explorations, are not part of
  this proof.
- No novelty or priority claim. Lemma 15 is a standard theorem with a standard proof.
