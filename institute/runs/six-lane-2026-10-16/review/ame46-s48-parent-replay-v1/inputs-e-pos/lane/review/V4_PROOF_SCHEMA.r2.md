# Engine v4/v5: exact final-CNF and report schema for proof mode (r2)

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once.

**r2 corrects r1** (`review/V4_PROOF_SCHEMA.r1.md`, f558e75b6d7f87ea5db3f8025be8475694715d1f8e2f94f88673094936e0b986,
unchanged). Codex v5 delta review, MAJOR M1: r1 stated a single pair order (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
for all families, but the base hole indicators and the J linking use a different order. r2 states the exact order of
each family. No code, CNF or proof changes; the pinned code always produced the order below.

This file specifies, for independent regeneration and binding, the exact DIMACS text that engines v4
(`code/large_t_joint4.py`, 42d6e510582d8f5e46ed8b348c1fb57ed8d28e6a0fb4e1f77ac54242345426a9) and v5
(`code/large_t_joint5.py`, e57067c247d3e5c6ca8e7f28035a6d9ec45b1a77238fe8ccd5046eff7f0033f8; identical CNF, extra
assertions only) give the solver for a profile's final enumeration CNF. The v3 and v2 artifacts and the accepted
LOWER48 proof hashes are unaffected.

## 0. Conventions
- **Two pair orders, used by different families:**
  - `BPAIRS` = `ame_e0_cnf.PAIRS` = `large_t_e0.PAIRS` = [(0,1), (2,3), (0,2), (1,3), (0,3), (1,2)]
    (`code/ame_e0_cnf.py` line 22, 97e30ae4…8a26). Used by the base hole indicators (B1) and by the J linking.
  - `SPAIRS` = `itertools.combinations(range(4), 2)` = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
    (`code/profile_officer_cnf.py`, module constant `PAIRS`). Used only by the first loop of the officer CNF.
  - Reshapings: `RESHAPINGS` = [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))] (`ame_e0_cnf.py` line 23), used by the
    base overlap family (B4) in the orientations (rows, cols) and then (cols, rows).
- For a profile p = (p_0, p_1, p_2, p_3) of partitions, listed in `large_t_e0.profiles(h)` order:
  - V_i = [6 − |p_i|, …, 5] (increasing);
  - d_{i,a} = p_i[k] for the k-th element a of V_i;
  - points of Π V_i are in `itertools.product(V_0, V_1, V_2, V_3)` order.
- "new()" means the next unused variable index, starting after the current maximum.
- AMK(L, k) is the Sinz sequential counter of `ame_e0_cnf.CNF.at_most_k`
  (97e30ae4e825440653a50e3de84389b00122fa70d3bbddb42924ccdd6ed78a26, lines 48–68):
  - k ≥ |L|: nothing;
  - k = 0: units ¬l;
  - otherwise: s[i][j] for i < |L| − 1 and j < k, created row by row, then the clauses in the order of lines 58–68.
- EQK(L, k) := AMK(L, k) followed by AMK(¬L, |L| − k) (`large_t_e0.Small.eqk`, lines 82–84).

## 1. Variables, in order of creation
1. Point variables n_x, 1 … P, with P = Π|V_i|.
2. Base auxiliaries, created by `large_t_gen.SmallGen.build_gen(e, h)` (28c0c1f9…bcfd, lines 42–85) in its order:
   - B1: hole indicators hl(i,j,a,b), one new() each, for (i,j) in **BPAIRS**, a in V_i, b in V_j (`large_t_gen.py`
     lines 44–56);
   - B2: EQK counters, for i in 0..3, j in 0..3 with j ≠ i, a in V_i (lines 57–64; the indicator of the line (a, b)
     is hl at the sorted pair);
   - B3: the EQK counter for |N| = 2h + e (line 65);
   - B4: overlap auxiliaries, over RESHAPINGS × the two orientations (lines 66–85).
   Let nv0 be the variable count after build_gen.
3. Joint block J (`exp_joint.build_joint`, 97024d63…1bca, lines 22–43). The officer CNF F = `profile_officer_cnf.build(p)`
   (802af4fe…cce9, lines 24–59) has its own variables:
   - officer point variables 1 … 1296 for y ∈ [6]⁴ in `itertools.product(range(6), repeat=4)` order;
   - then its auxiliaries.
   Every literal ℓ of F is shifted to sign(ℓ)(|ℓ| + nv0). So the officer variable of y is o_y = nv0 + 1 + index(y).
4. W (triangles) adds no variables.
5. Lex chains: fresh variables per generator, in generator order (§4).
Blocking clauses add no variables.

## 2. Clause order
1. **Base:** the clauses of build_gen, in its order.
2. **J, the officer CNF F**, in its order, shifted by nv0:
   - for (j,k) in **SPAIRS**, b in 0..5, c in 0..5: L = officer variables of the line (x_j, x_k) = (b, c), in product
     order. If b ∈ V_j and c ∈ V_k: AMK(L, 1). Otherwise: the clause L, then AMK(L, 1);
   - for j in 0..3, k in 0..3 with k ≠ j, a in V_j (increasing):
     - for b in V_k (increasing): a new indicator v, the clause (¬v ∨ L_{ab}), then (¬ℓ ∨ v) for each ℓ ∈ L_{ab};
     - then AMK(inds, |V_k| − d_{j,a}) and AMK(¬inds, d_{j,a}).
3. **J, linking:** for (i,j) in **BPAIRS**, a in V_i, b in V_j, with h = hl(i,j,a,b) and Λ the officer variables of the
   line (x_i, x_j) = (a, b) in product order: the clauses (¬h ∨ ¬o) for o ∈ Λ in order, then (h ∨ Λ).
4. **W (e = 0 only;** `exp_triangle.triangle_clauses`, 4a7aed55…eb37, lines 30–58): for i in 0..3, with others
   (c1, c2, c3) = the other coordinates in increasing order, for a < a′ in V_i (combinations order), and with
   Z = product of V_{c1}, V_{c2}, V_{c3} in product order:
   - for z1 in Z, z2 in Z with z2[c1] = z1[c1], z2[c2] ≠ z1[c2], z2[c3] ≠ z1[c3]:
     - for z3 in Z with z3[c2] = z2[c2], z3[c3] = z1[c3], z3[c1] ≠ z1[c1]: the clause
       (¬n_{(a;z1)} ∨ ¬n_{(a′;z1)} ∨ ¬n_{(a;z2)} ∨ ¬n_{(a′;z2)} ∨ ¬n_{(a;z3)} ∨ ¬n_{(a′;z3)}).
   - For profile {6,6}{2⁶}³ at t = 24 this gives 108,000 clauses.
5. **Lex-leader** for each generator g in `large_t_lex.generators(S)` order (cde05b00…12b8):
   - first, coordinate swaps (i, i+1), for i = 0, 1, 2 with p_i = p_{i+1};
   - then, for i = 0..3, the d-classes of V_i in order of first occurrence, and in each class the adjacent pairs (a, b)
     in increasing order: the value transposition a ↔ b on coordinate i.
   For each g, go through the points x of Π V_i in product order with y = g(x), skipping x = y. Let k count the
   non-fixed positions, with x = n_x and y = n_{g(x)}.
   - k = 1: (¬x ∨ y); q1 = new(); (¬x ∨ ¬y ∨ q1), (x ∨ y ∨ q1), (¬q1 ∨ ¬x ∨ y), (¬q1 ∨ x ∨ ¬y). This is the q0 = true
     substitution, with the tautological clause dropped.
   - k > 1: (¬q_{k−1} ∨ ¬x ∨ y); q_k = new(); (¬q_k ∨ q_{k−1}), (¬q_{k−1} ∨ ¬x ∨ ¬y ∨ q_k), (¬q_{k−1} ∨ x ∨ y ∨ q_k),
     (¬q_k ∨ ¬x ∨ y), (¬q_k ∨ x ∨ ¬y).
6. **Blocking:** for each recorded solution, in report order, the clause (∨ ¬n_x) over its points in product order.
   The report lists each N as 4-digit strings in product order.

The DIMACS header is `p cnf <max variable> <number of clauses>`, with one clause per line ending in ` 0`
(`large_t_lex.dimacs`). The report records `final_cnf_sha256`, the SHA-256 of this exact text.

## 3. Report fields used for binding (`evidence/large_t_joint4_t<t>_e<e>.json` in proof mode)
- Per profile:
  - `index`, `profile`, `lemma17_f`;
  - `status` ∈ {EXCLUDED-BY-LEMMA, EMPTY, ENUMERATED, UNKNOWN};
  - `triangle_clauses`, `generators`, `solutions`;
  - `final_cnf_sha256`;
  - `final_proof`: gzip LRAT path, `proof_gz_sha256`, and the worker checker results, which are same-author and not
    load-bearing;
  - `reps`: for each solution, N (4-digit strings), `components_ok`, `moduli_certificate` if one was used,
    `phase_certificate` and `phase_certificate_compact` (w, k, corners) with the verifier result, `excluded`, and for
    a candidate `T`, `theta` and `exact_unitarity`.
- Top level: `engine`, `mode`, `joint`, `triangles`, `caps`, `guard_tripped`, `outcome`.
- A partial run, with `--profiles`, is labelled PARTIAL and is never a certificate.

## 4. What a binding should establish
- The final CNF's regenerated text has SHA-256 equal to `final_cnf_sha256`.
- The addition-only RUP replay of the gzip LRAT stream against that text verifies.
- Every recorded N is excluded by a parent-checked certificate, with the closure criteria of LOWER48 r2 §3.
- Profile completeness for h holds, and the Lemma 17 exclusions are recomputed.
- Lemmas 19 and 20 and the realizable-support completeness argument (`review/ENGINE_V4.r1.md` §§3–5) pass hostile
  review.
