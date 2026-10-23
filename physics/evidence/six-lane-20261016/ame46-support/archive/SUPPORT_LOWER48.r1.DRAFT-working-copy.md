# FROZEN r1 — partial result: every AME(4,6) state has at least 48 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`, `evidence/SHA256SUMS.txt`). Corrections go to r2.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written and not yet independently reviewed.
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The target is 59 versus 60; this file proves
  only the lower bound 48.
- **Builds on:**
  - `review/SUPPORT_LOWER42.r2.md` (1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418): §0
    definitions, Lemmas 1–11 (cited as L42-1 … L42-11), the cases t = 33–36 and the by-product corollary;
  - `review/SUPPORT_LOWER46.r1.md` (d5b076ba146bb6ea6f6a8eb21dce948ade563f2cf1f2c808e84350d0002ffc83): its Theorem
    (s ≥ 46), Lemmas 12–16 (cited as L46-12 … L46-16), and the exhaustive procedure of its §3 (steps 1, 2 and 4).
  - LOWER46 r1's wording on checker independence, moduli and certificate storage is corrected in the forthcoming
    LOWER46 r2. This file uses the corrected wording and does not rely on the contested phrases.
- **Cited theorem:** Tarry (t = 36 only), via LOWER42 r2 and LOWER46 r1.
- **New written lemmas:** Lemma 17 (officer counting) and Lemma 18 (a binary code; the argument is the parent
  orchestrator's). Both are load-bearing here.
- **Computer-assisted part:** eight cases (26,0), (27,2), (28,2), (28,3), (29,3), (29,4), (30,4), (30,5), run under
  engine v2 `code/large_t_lex.py` (cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8). Its scope and
  resource guard are frozen in `review/ENGINE_V2_GUARD.r1.md`
  (d5733a7366c6d7fb3c197829ed6232abcb74c27f7250fa556cc59f34a3a273fd).
  - Every UNSAT used carries a gzip-compressed text LRAT proof. The two LRAT checkers that accept them were both
    written by this worker, so their agreement is reproducibility, not independent validation.
  - Every phase exclusion has a stored explicit certificate (§5). Independent re-checking by the parent is pending.
- No novelty or priority claim. Crowded field; a search miss is not novelty.

## Theorem

Every AME(4,6) state has at least 48 non-zero coefficients in every product orthonormal basis.

## 1. Two written lemmas on the officers

Notation is that of LOWER42 r2 §0 and LOWER46 r1 §1. T is the set of classical officers, |T| = t, h = 36 − t, N the
set of non-classical support points, and |N| = 2h + e. V_i is the set of values of coordinate i with positive
deficit, and d_{i,a} the deficit of a ∈ V_i. The partition of h formed by the d_{i,a} is coordinate i's **profile
part**.

**Facts used.**
- (F1) A line meeting N contains no officer (L42-2(a), L42-4).
- (F2) Every other line contains exactly one officer: it is non-empty (L42-1), contains no point of N, and has at
  most one officer (L42-3).
- (F3) For i ≠ j and a ∈ V_i, the lines (x_i, x_j) = (a, b) meeting N are exactly those with b ∈ D_j^{(i,a)}, with
  |D_j^{(i,a)}| = d_{i,a} (L42-8). Moreover D_j^{(i,a)} ⊆ V_j (L46-12). For a ∉ V_i no line (a, b) meets N
  (L42-8(c): N ⊆ Π V_i).
- (F4) Σ_{a∈V_i} d_{i,a} = h for every i (L42-8(b)).

**Lemma 17 (officer counting).** For x ∈ T let c(x) := #{i : x_i ∈ V_i} ∈ {0, 1, 2, 3, 4}. Then
- σ0 := Σ_{x∈T} 1 = t;
- σ1 := Σ_{x∈T} c(x) = 6 Σ_i |V_i| − 4h;
- σ2 := Σ_{x∈T} C(c(x), 2) = e2(|V_1|, |V_2|, |V_3|, |V_4|) − 6h, where e2(v) = Σ_{i<j} v_i v_j.
Consequently, for every integer α,

  f(α) := σ2 − α σ1 + C(α+1, 2) σ0 = Σ_{x∈T} (c(x) − α)(c(x) − α − 1)/2 ≥ 0.

So a deficit profile with f(α) < 0 for some integer α is impossible, for every e.

*Proof.*
- **σ1.** Σ_x c(x) = Σ_i Σ_{a∈V_i} |T ∩ {x_i = a}|. Fix i, a ∈ V_i and a partner j ≠ i. Each officer with x_i = a
  lies on exactly one of the six lines (a, b), b ∈ {0, …, 5}. By (F3), d_{i,a} of these meet N and hold no officer
  (F1), and each of the other 6 − d_{i,a} holds exactly one (F2). So |T ∩ {x_i = a}| = 6 − d_{i,a}. Summing over
  a ∈ V_i with (F4) gives 6|V_i| − h, and summing over i gives 6 Σ|V_i| − 4h.
- **σ2.** C(c(x), 2) is the number of pairs i < j with x_i ∈ V_i and x_j ∈ V_j. So σ2 = Σ_{i<j} |T ∩ {x_i ∈ V_i,
  x_j ∈ V_j}|. For fixed i < j, each such officer lies on exactly one line (x_i, x_j) ∈ V_i × V_j. By (F3) and (F4)
  exactly h of these |V_i||V_j| lines meet N, and each of the others holds exactly one officer (F1, F2). So the count
  is |V_i||V_j| − h, and σ2 = e2(|V|) − 6h.
- **Integrality.** For integers k and α, (k − α)(k − α − 1) is a product of two consecutive integers. It is even and
  non-negative, because no integer lies strictly between α and α + 1. Expanding gives (k − α)(k − α − 1)/2 =
  C(k, 2) − α k + C(α+1, 2), with C(k, 2) = k(k − 1)/2. Summing over x ∈ T with k = c(x) gives f(α) ≥ 0. ∎

α = 1 is the inequality σ0 − σ1 + σ2 ≥ 0, which the parent orchestrator derived independently. α = 2 is needed for
(26,0) below. The values f(0), …, f(4) are computed exactly from the profile alone.

**Lemma 18 (a binary code; argument due to the parent orchestrator).** For t = 28 the profile
{4,4}{2,2,2,2}{2,2,2,2}{2,2,2,2}, in any coordinate order, is impossible for every e.
*Proof.* Order the coordinates so that coordinate 1 has the part {4,4}.
- So V_1 = {a1, a2} with d_{1,a1} = d_{1,a2} = 4, and |V_j| = 4 for j = 2, 3, 4.
- For a ∈ V_1 and j ≠ 1, (F3) gives D_j^{(1,a)} ⊆ V_j with |D_j^{(1,a)}| = 4 = |V_j|, so D_j^{(1,a)} = V_j. Every line
  (a, b) with b ∈ V_j meets N and holds no officer (F1).
- By the σ1 computation, exactly 6 − 4 = 2 officers have x_1 = a. Each of them has x_j ∉ V_j for j = 2, 3, 4, i.e. x_j
  lies in a 2-element set.
- So the four officers with x_1 ∈ V_1 are words of a product of four 2-element alphabets. Two officers agreeing in
  two coordinates would lie on a common line, which L42-3 forbids. So any two of the four words differ in at least
  3 coordinates, and the six pairwise distances sum to at least 18.
- A coordinate with a 2-element alphabet separates at most 2 · 2 = 4 of the 6 pairs of four words, so the distances
  sum to at most 4 · 4 = 16. Contradiction. ∎

**Profiles excluded in writing** (values f(0), …, f(4); a negative entry excludes the profile):
- t = 29: the only profile {3,2,2}⁴ has f = (12, −3, 11, 54, 126). So t = 29 is impossible for every e.
- t = 30: {3,3}{2,2,2}³ has f = (9, −3, 15, 63, 141).
- t = 28: {3,3,2}⁴ has f = (6, −6, 10, 54, 126) and {3,3,2}³{2,2,2,2} has f = (15, −3, 7, 45, 111). Lemma 18
  excludes {4,4}{2,2,2,2}³.
- t = 27: {3,3,3}⁴ (f(1) = −9), {3,3,3}³{3,2,2,2} (−6) and {3,3,3}²{3,2,2,2}² (−2).
- t = 26: {5,5}{2,2,2,2,2}³ has f = (45, 9, −1, 15, 57). Here |V| = (2, 5, 5, 5), σ1 = 62, σ2 = 45, and
  f(2) = 45 − 124 + 78 = −1.

## 2. The cases for s ≤ 47

By L42 §0, s = 72 − t + e with e ≥ 0. So s ≤ 47 forces t ≥ 25 and e ≤ t − 25. LOWER46 r1 already excludes s ≤ 45.
The new values are s ∈ {46, 47}, i.e. e = t − 26 or e = t − 25.

| t | e range (s ≤ 47) | how excluded |
|---|---|---|
| 36 | — | Tarry (LOWER42 r2) |
| 33–35 | all e | LOWER42 r2 corollary |
| 32 | all e | L46-16 |
| 31 | all e | L46-13 |
| 30 | 0 ≤ e ≤ 5 | e = 1: L42-7(b),(c). e = 0, 2, 3: LOWER46 r1 (s ≤ 45). e = 4, 5: §3 |
| 29 | all e | Lemma 17 (single profile, f(1) = −3) |
| 28 | 0 ≤ e ≤ 3 | e = 0: LOWER46 r1. e = 1: L42-7. e = 2, 3: §3 |
| 27 | 0 ≤ e ≤ 2 | e = 0: t odd (LOWER42 r2 corollary). e = 1: L42-7. e = 2: §3 |
| 26 | 0 ≤ e ≤ 1 | e = 0: §3. e = 1: L42-7 |
| 25 | e = 0 | t odd (corollary) |

Every row is impossible, so s ≥ 48. ∎

## 3. Engine v2: scope, completeness and results

The per-profile CNF and the per-solution exact checks are those of LOWER46 r1 §3, steps 1, 2 and 4, imported unchanged
from the frozen engine `code/large_t_gen.py` (28c0c1f9e32089d0080869689be6ea7fd3dd93ae5239cf0c7131cf4c4607bcfd).
Engine v2 changes only the enumeration (step 3) and the I/O. The full specification is `review/ENGINE_V2_GUARD.r1.md`;
the load-bearing points follow.

**Variables and their order.** A profile's CNF has one Boolean variable per point of V_1 × V_2 × V_3 × V_4, with
V_i = {6 − |p_i|, …, 5} in normal form. Points are ordered lexicographically (`itertools.product` order). That is the
shared variable order of every lex-leader constraint. Auxiliary variables are numbered after the point variables.

**Generators Γ.**
- adjacent transpositions (a, a′) of values inside one d-class of one V_i (equal deficits);
- adjacent transpositions (i, i+1) of coordinates with equal profile parts. Profiles are listed in canonical order,
  so equal parts are contiguous.

**Each generator is a symmetry of the CNF.** It permutes the point variables, and renaming the auxiliary variables
accordingly maps the clause set onto itself:
- line indicators and their definitions are uniform over values;
- each hole-count constraint (exactly d_{i,a} of the lines (a, b), b ∈ V_j, meet N) maps to one with the same
  right-hand side, because transposed values have equal deficits and transposed coordinates have equal deficit maps;
- the cardinality |N| = 2h + e is invariant;
- the overlap constraints are imposed in both orientations of all three reshapings, and a coordinate transposition
  permutes the reshapings and their row and column roles.
Hence the set Sol of point assignments that extend to a model is invariant under H = ⟨Γ⟩.

**Completeness.**
- Let X ∈ Sol and let X* be the lexicographically least element of its H-orbit. Then X* ≤_lex g(X*) for every g ∈ H,
  in particular for every g ∈ Γ. So X* satisfies the lex-leader constraints, with the chain auxiliaries e_k set to
  "the prefixes agree up to position k".
- v2 blocks each found solution individually. The final CNF (CNF ∧ Lex_Γ ∧ all blocking clauses) is UNSAT with a
  checked LRAT proof. So X* is a found solution, and X = h(X*) for some h ∈ H.
- The per-solution checks are invariant under H (LOWER46 r1 §3). So excluding every found solution excludes Sol.

**Guard.** The RSS watchdog (6 GiB, SIGTERM only), exact-byte disk accounting, the solution cap and the per-call time
limits were in place. None tripped in the runs used here.

**Results.** All runs used `../../depolarizing/env/bin/python` (CPython 3.13.9) and CaDiCaL 3.0.1
(`/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical`, SHA-256 601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa),
on 2026-10-17 PDT.

| case | run | profiles | solutions | exclusion reasons | written profile exclusions |
|---|---|---|---|---|---|
| (26,0) | 13:24:12–13:43:48 | 25 | 1695 | phase 1619; completion UNSAT 76 (all in {5,5}{2⁵}³) | {5,5}{2⁵}³ (Lemma 17, α = 2) |
| (27,2) | 13:02:08–13:02:20 | 6 | 28, all in {3,3,3}⁴ | components 20; moduli 4; completion UNSAT 4 | {3,3,3}⁴, {3,3,3}³{3,2,2,2}, {3,3,3}²{3,2,2,2}² (Lemma 17) |
| (28,2) | 13:02:04–13:02:07 | 7 | 0 | — | {3,3,2}⁴, {3,3,2}³{2⁴} (Lemma 17); {4,4}{2⁴}³ (Lemma 18) |
| (28,3) | 13:02:20–13:02:24 | 7 | 0 | — | as for (28,2) |
| (29,3) | 13:02:03 | 1 | 0 | — | {3,2,2}⁴ (Lemma 17) |
| (29,4) | 13:02:07 | 1 | 0 | — | {3,2,2}⁴ (Lemma 17) |
| (30,4) | 13:02:03–13:02:04 | 2 | 0 | — | {3,3}{2,2,2}³ (Lemma 17) |
| (30,5) | 13:02:07–13:02:08 | 2 | 0 | — | {3,3}{2,2,2}³ (Lemma 17) |

In (26,0), the profiles with solutions outside {5,5}{2⁵}³ are all excluded by phase certificates:
- {5,3,2}{2⁵}³: 51;
- {4,4,2}{3,3,2,2}{2⁵}²: 29;
- {4,2,2,2}³{3,3,2,2}: 10;
- {4,2,2,2}²{3,3,2,2}{2⁵}: 16;
- {4,2,2,2}{3,3,2,2}{2⁵}²: 16;
- {3,3,2,2}{2⁵}³: 15.

These 137 phase certificates are load-bearing.

**Dependency on computation.**
- The final enumeration UNSATs of every profile not excluded in writing: 24 in (26,0); 3 in (27,2), namely
  {4,3,2}{3,2,2,2}³, {3,3,3}{3,2,2,2}³ and {3,2,2,2}⁴; 4 each in (28,2) and (28,3); 1 each in (30,4) and (30,5).
  These are 37 final UNSATs.
- The 137 phase certificates listed above.
- The cases imported from LOWER46 r1.
No completion proof, moduli certificate or components exclusion is needed. All of them are kept as evidence, and all
were verified.

## 4. Executable record

All paths are relative to the lane `physics/evidence/six-lane-20261016/ame46-support/`.

- **Engine v2:** `code/large_t_lex.py` (cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8). Command per
  case: `cd code && OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B large_t_lex.py --t T --e E --proof`.
  - It imports `large_t_gen.py` (28c0c1f9…bcfd), `large_t_e0.py` (67033dcf…466c), `phase_check.py` (0c591d1b…f693)
    and `ame_e0_cnf.py` (97e30ae4…8a26).
  - Guard spec: `review/ENGINE_V2_GUARD.r1.md` (d5733a73…73fd). Guard smoke: `evidence/guard_smoke.json`
    (3c4ea4e6ad2346f358378c264994093e2dc1f58f4d288c3b927978cbf8c9db46), S1–S9 all as expected.
- **Reports** (SHA-256):
  - `evidence/large_t_lex_t26_e0.json` 7aafcb4a02498fa67fff4cad8d4865d835cdbf650aaa105c3593fa883fc6edb0;
  - `evidence/large_t_lex_t27_e2.json` 4e5166da4a97f71e314be5125b6c21ffe63fef6be0c8ffd76d0df0dfb93a60a8;
  - `evidence/large_t_lex_t28_e2.json` bdfef2eb0943508cf798c658e9f679e10cde86b24a7ae6ab3bf5f1a0f4104d3e;
  - `evidence/large_t_lex_t28_e3.json` 2ecf727263513498dde48aa0c57ae821d021282f47b83b49d49e429fb5a1966e;
  - `evidence/large_t_lex_t29_e3.json` d406a95d96d789a0f019d5ff7173250b8415f192b2f940773fd9a087d307d0e5;
  - `evidence/large_t_lex_t29_e4.json` 3483bf4e403596d1685a6dff83a0de95e79c177a17c0d483f8faead13a22f01c;
  - `evidence/large_t_lex_t30_e4.json` 147ea683c9c6cbe8010b246e6eab4949b8de2b3055dc96daff4fc3ee71c04901;
  - `evidence/large_t_lex_t30_e5.json` e334872ab1c02a29fa72b331dce91d7824ed2caa44db9fb7dd6add6846ad0c37.
- **Receipt:** `code/v2_receipt_r2.py` (328bf36b2dae8b42a53183d6751baaa73e284b4b13f592973a0c08df0e0e81ec) →
  `evidence/v2_receipt_r2.json` (bf05ec215313eedd490293d1a04a7ca8ed073da30b58e5831587e497caada5fa). Run 13:44:00–13:45:04
  PDT; all_required_true = true. Stdout: `explore/v2_receipt_r2.stdout.txt` (4b33bae5…3592). For each report it does
  the following:
  - It checks the header (engine v2, proof mode, EXCLUDED, no guard trip).
  - It regenerates in memory the exact final CNF of each profile (base CNF, lex-leader constraints, blocking clauses
    in report order) and records its SHA-256.
  - It checks each gzip LRAT stream with the C checker and with the Python checker in skip mode, through a FIFO and
    a pipe, and runs the Python strict mode for information. No uncompressed proof is stored.
  - It recomputes every solution's exclusion: components; moduli (the Stiemke vector is stored); phase (the explicit
    certificate is stored in repeated ±1 form and in compact (w, k, corners) form, and verified by
    `code/phase_cert.py`, fbe3ab68…b54e, whose verifier does not use `phase_check.py`); or completion (N, the
    completion-CNF SHA-256 and the stream SHA-256 are stored).
  - It asserts that the blocking clauses are exactly the re-excluded solutions.
  - It records Lemma 17's f(0..4) for each profile.
- **Receipt totals.**
  - 131 proof streams (51 final, 80 completion), 44,680,286 compressed bytes, all verified by both checkers.
  - 130 pass strict mode. The exception is
    `explore/large_t_lex/t26_e0_4-2-2-2_4-2-2-2_3-3-2-2_3-3-2-2.final.lrat.gz`, which has 3 hints already satisfied at
    use, counted identically by both checkers. Skipping such a hint is sound (LOWER46 r1 §5).
  - 1619 phase certificates, all verified, each with an odd weight sum. Moduli 4, components 20, completion 80.
  - Negative controls of the certificate verifier, all rejected for the intended reason: drop an entry (even
    count); flip a sign (non-zero sum); duplicate an entry (even count); change the reshaping (not a rectangle);
    corner outside N.
- **Proof streams:** `explore/large_t_lex/<tag>.final.lrat.gz` and `<tag>_sol<k>_completion.lrat.gz`. Their paths and
  SHA-256 values are in the receipt. CNFs are not stored; they are regenerated deterministically from the profile,
  the pinned code and the report's solution list.
- **Interpreter:** CPython 3.13.9 for the engine and the receipt.

## 5. Not claimed

- Nothing about 59 versus 60 beyond the bound 48.
- Exploration runs, UNKNOWN runs and older-code batch outputs are not part of this proof.
- No novelty or priority claim. Lemma 18's argument is the parent orchestrator's. The α = 1 case of Lemma 17 was
  derived independently by the parent.
