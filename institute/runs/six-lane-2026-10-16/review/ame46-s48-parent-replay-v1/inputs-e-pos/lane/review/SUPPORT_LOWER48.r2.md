# FROZEN r2 — partial result: every AME(4,6) state has at least 48 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`). r1 (0457570502535eb3bb6aaa8002f81ca640451c8364079c9e0f4cc9413fb49f95) is unchanged.
This is a correction revision: the search, the CNFs, the proof streams, the certificates and the theorem are those of
r1. §7 gives a disposition for every review item.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written.
- Model reviews of r1, both ACCEPT-WITH-FIXES with no FATAL item and the same MAJOR item (fixed in §3):
  - Codex CLI gpt-6.1-sol: `review/ame46-lower48-codex-review-v1.note.md`;
  - Claude CLI claude-opus-5-5: `review/ame46-lower48-claude-review-v1.note.md`.
- The parent's independent replay of the load-bearing computation PASSED (§5).
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The target is 59 versus 60; this file proves
  only the lower bound 48.
- **Builds on:**
  - `review/SUPPORT_LOWER42.r2.md` (1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418), cited as L42
    with line numbers LF: the definitions of §0, Lemmas 1–11 (L42-1 … L42-11), the cases t = 33–36 and the corollary
    (LF202–204);
  - `review/SUPPORT_LOWER46.r2.md` (fac5242b90554de86cd6bd8e17fb2a6800fbd4a3e71d2e4a99f154d5a216f35b), cited as L46:
    its Theorem s ≥ 46, Lemmas 12–16 (L46-12 … L46-16), §3 steps 1, 2 and 4 (normalization, the base CNF families
    F1–F4, the exclusion checks), and its evidence record. Its narrowed load-bearing content is stated in §4.
- **Cited theorem:** Tarry (t = 36 only), through L42.
- **New written lemmas:** Lemma 17 (officer counting) and Lemma 18 (a binary code; the argument is the parent
  orchestrator's). Both are load-bearing here.
- **Computer-assisted part:** six cases, (26,0), (27,2), (28,2), (28,3), (30,4) and (30,5), run under engine v2
  `code/large_t_lex.py` (cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8).
  - The engine-v2 runs for (29,3) and (29,4) are cross-checks only, because Lemma 17 excludes t = 29 in writing.
  - The UNSAT basis is the parent's addition-only RUP replay of the 37 load-bearing final CNFs (§5).
  - The worker's two LRAT checkers are separately implemented by the same author, so they give reproducibility only.
- No novelty or priority claim. Crowded field; a search miss is not novelty.

## Theorem

Let ψ ∈ (C^6)^{⊗4} be an AME(4,6) state (L42 LF32–34); arbitrary complex amplitudes are allowed. For every product
orthonormal basis, at least 48 of the 1296 coefficients of ψ are non-zero.

By the basis reduction (L42 LF47–50), local unitaries preserve the AME property, so it suffices to treat the
computational basis. Nothing below assumes real amplitudes or equal moduli.

## 1. Two written lemmas on the officers

Notation is that of L42 §0 and L46 §1:
- T is the set of classical officers, |T| = t, and h = 36 − t;
- N is the non-classical support, with |N| = 2h + e;
- V_i is the set of values of coordinate i with positive deficit, and d_{i,a} = 6 − t_{i,a} is the deficit of a,
  where t_{i,a} = |{y ∈ T : y_i = a}| (L42 LF59).

The partition of h formed by the d_{i,a}, a ∈ V_i, is coordinate i's profile part.

**Officer facts.**
- (O1) A line meeting N contains no officer (L42-2(a), L42-4).
- (O2) Every other line contains exactly one officer: it is non-empty (L42-1), contains no point of N, and has at most
  one officer (L42-3).
- (O3) For i ≠ j and a ∈ V_i, the lines (x_i, x_j) = (a, b) that meet N are exactly those with b ∈ D_j^{(i,a)}. There
  are d_{i,a} of them (L42-8), and D_j^{(i,a)} ⊆ V_j (L46-12). For a ∉ V_i no line (a, b) meets N, since N ⊆ Π V_i
  (L42-8(c)).
- (O4) Σ_{a∈V_i} d_{i,a} = h for every i (L42-8(b)).

**Lemma 17 (officer counting).** For x ∈ T let c(x) := #{i : x_i ∈ V_i} ∈ {0, …, 4}, and let v_i = |V_i|. Then
- κ0 := Σ_{x∈T} 1 = t;
- κ1 := Σ_{x∈T} c(x) = 6 Σ_i v_i − 4h;
- κ2 := Σ_{x∈T} C(c(x), 2) = e2(v) − 6h, where e2(v) = Σ_{i<j} v_i v_j.
For every integer α,

  f(α) := κ2 − α κ1 + C(α+1, 2) κ0 = Σ_{x∈T} (c(x) − α)(c(x) − α − 1)/2 ≥ 0.

In closed form, f(α) = e2(v) − 6h − α(6 Σ v_i − 4h) + C(α+1, 2) t. A profile with f(α) < 0 for some integer α is
impossible, for every e.

*Proof.*
- **κ1.** Σ_x c(x) = Σ_i Σ_{a∈V_i} t_{i,a} = Σ_i Σ_{a∈V_i} (6 − d_{i,a}) = 6 Σ v_i − 4h, by the definition of d_{i,a}
  and (O4).
- **κ2.** C(c(x), 2) counts the pairs i < j with x_i ∈ V_i and x_j ∈ V_j. So κ2 = Σ_{i<j} |T ∩ {x_i ∈ V_i, x_j ∈ V_j}|.
  - For fixed i < j, each such officer lies on exactly one line in V_i × V_j.
  - By (O3) and (O4), exactly h of these v_i v_j lines meet N and hold no officer (O1). Each of the others holds
    exactly one (O2).
  - So the count is v_i v_j − h.
- **Non-negativity.** For integers k and α, (k − α)(k − α − 1) ≥ 0, because no integer lies strictly between α and
  α + 1. Expanding gives (k − α)(k − α − 1)/2 = C(k, 2) − αk + C(α+1, 2). Summing over x ∈ T with k = c(x) proves
  f(α) ≥ 0. ∎

Since c(x) ∈ [0, 4], each summand is monotone in α outside [0, 4]. So α ∈ {0, …, 4} already gives every exclusion the
lemma can give. α = 1 is the Bonferroni inequality, which the parent derived independently.

**Lemma 18 (a binary code; argument due to the parent orchestrator).** For t = 28, the profile
{4,4}{2,2,2,2}{2,2,2,2}{2,2,2,2} is impossible for every e.
*Proof.* Order the coordinates so that coordinate 1 has {4,4}, with V_1 = {a1, a2} and v_j = 4 for j = 2, 3, 4.
- For a ∈ V_1 and j ≠ 1, (O3) gives D_j^{(1,a)} ⊆ V_j with d_{1,a} = 4 = v_j elements, so D_j^{(1,a)} = V_j. Every
  line (a, b) with b ∈ V_j meets N and holds no officer (O1).
- Exactly t_{1,a} = 6 − 4 = 2 officers have x_1 = a. Each has x_j ∈ [6] ∖ V_j, a 2-element set, for j = 2, 3, 4.
- The four officers with x_1 ∈ V_1 are therefore words over four 2-letter alphabets. Two officers agreeing in two
  coordinates would share a line, contrary to L42-3. So any two of them differ in at least 3 coordinates, and the six
  pairwise distances sum to at least 18.
- Each coordinate separates at most 2 · 2 = 4 of the 6 pairs, so the sum is at most 16. Contradiction. ∎

**Profiles excluded in writing** (values f(0..4); every other profile at t = 26..30 has all f ≥ 0):
- **t = 29: every e.** Parts are ≥ 2 and sum to 7 (L42-8(a), (b)), so each coordinate has at most 3 parts. By L46-12
  every part is at most 3. So every coordinate is {3,2,2}, the only partition of 7 into parts in {2, 3}. For
  {3,2,2}⁴, v = (3,3,3,3), κ1 = 44, κ2 = 12 and f = (12, −3, 11, 54, 126).
- **t = 30:** {3,3}{2,2,2}³ has v = (2,3,3,3) and f = (9, −3, 15, 63, 141).
- **t = 28:** {3,3,2}⁴ has f = (6, −6, 10, 54, 126). {3,3,2}³{2,2,2,2} has f = (15, −3, 7, 45, 111). Lemma 18 excludes
  {4,4}{2,2,2,2}³, where f(1) = 0.
- **t = 27:** {3,3,3}⁴ has f(1) = −9, {3,3,3}³{3,2,2,2} has f(1) = −6, and {3,3,3}²{3,2,2,2}² has f(1) = −2.
- **t = 26:** {5,5}{2,2,2,2,2}³ has v = (2,5,5,5), κ1 = 62, κ2 = 45 and f = (45, 9, −1, 15, 57).
  - A two-line alternative: the two officers with x_1 ∈ V_1 both have x_j equal to the single element of [6] ∖ V_j
    for j = 2, 3, 4 (as in Lemma 18). So they agree in three coordinates, contrary to L42-3.

## 2. The cases for s ≤ 47

By L42 §0, s = 72 − t + e, and e ≥ 0 by L42-4. So s ≤ 47 forces t ≥ 25 and e ≤ t − 25. L46 already excludes
s ≤ 45. The new pairs are the 23 with s ∈ {46, 47}: e = t − 26 for t = 26..36, and e = t − 25 for t = 25..36.

| t | e range (s ≤ 47) | how excluded |
|---|---|---|
| 36 | — | Tarry (L42) |
| 33–35 | all e | L42 corollary (LF202–204) |
| 32 | all e | L46-16 |
| 31 | all e | L46-13 |
| 30 | 0 ≤ e ≤ 5 | e = 1: L42-7(b),(c). e = 0, 2, 3: L46. e = 4, 5: §3 and §4 |
| 29 | all e | Lemma 17 (§1) |
| 28 | 0 ≤ e ≤ 3 | e = 0: L46. e = 1: L42-7. e = 2, 3: §3 and §4 |
| 27 | 0 ≤ e ≤ 2 | e = 0: t odd (L42 corollary). e = 1: L42-7. e = 2: §3 and §4 |
| 26 | 0 ≤ e ≤ 1 | e = 0: §3 and §4. e = 1: L42-7 |
| 25 | e = 0 | t odd (corollary) |

Every row is impossible, so s ≥ 48. ∎

## 3. Engine v2: what the computation proves

### Normalization (L46 §3 step 1)

- A permutation matrix on one party permutes coefficients. So it maps an AME state to an AME state, preserves s, t and
  e, and relabels deficits.
- A permutation σ of the parties permutes the six two-party marginals, so it also maps AME states to AME states.
- Under the combined map, d_{σ(i), β_i(a)} = d_{i,a}, where β_i is the value permutation on party i.
- So we may assume the profile is in normal form: V_i = {6 − v_i, …, 5}, parts assigned in non-increasing order, and
  coordinates in the code's order.

### The final CNF of a profile

There is one variable n_x per point x ∈ Π V_i, numbered 1, 2, … in `itertools.product` order. This is the shared
point order. The base auxiliaries and then the lex chain variables are numbered after the point variables, in order of
creation. Blocking clauses add no variables.
- **Base clauses.** The families F1–F4 of L46 §3 step 2, from `large_t_gen.SmallGen.build_gen` (lines 42–85).
- **Generators Γ** (`code/large_t_lex.py`, function `generators`):
  - adjacent transpositions (a, a′) of values inside one d-class of one V_i (equal deficits), the identity elsewhere;
  - adjacent transpositions (i, i+1) of coordinates with equal profile parts.
  - Every generator is an involution.
- **Lex-leader clauses for a generator g** (`add_lex_leader`, lines 225–239). Write X for the assignment of the point
  variables, and (g·X)_p := X_{g(p)}.
  - Go through the points p_1, p_2, … in the shared order, skipping fixed points (g(p) = p).
  - At the k-th non-fixed position, with x = n_{p_k} and y = n_{g(p_k)}, the code adds:
    - the comparison clause (¬q_{k−1} ∨ ¬x ∨ y), or (¬x ∨ y) when k = 1;
    - a fresh chain variable q_k with q_k ↔ (q_{k−1} ∧ (x ↔ y)), i.e. q_k ↔ (x ↔ y) when k = 1. In clauses:
      (¬q_k ∨ q_{k−1}), (¬q_{k−1} ∨ ¬x ∨ ¬y ∨ q_k), (¬q_{k−1} ∨ x ∨ y ∨ q_k), (¬q_k ∨ ¬x ∨ y) and (¬q_k ∨ x ∨ ¬y).
      For k = 1 the q_{k−1} literals are omitted.
  - The chain variables are fresh for each generator and disjoint from the base auxiliaries.
- **Blocking clauses.** One per recorded solution Y, in report order: ∨_{x∈Y} ¬n_x, with |Y| = 2h + e.
- **Composition.** The final CNF is exactly base ∧ Lex_Γ ∧ the blocking clauses of all recorded solutions. The receipt
  regenerates it and records its SHA-256, and the parent regenerated it independently with matching SHA-256 (§5).

### The properties used (Claude P1–P5)

- **P1 (base soundness; L46 §3 step 2).** The non-classical support of every normalized AME state with parameters
  (t, e, profile) extends to a model of the base clauses.
- **P2 (lex soundness).** Let ≤ be the lexicographic order on point assignments in the shared order, with
  false < true. For every g ∈ Γ and every X with X ≤ g·X, setting q_k := [X and g·X agree on the first k non-fixed
  positions] satisfies all of g's clauses.
  - *Proof.* The chain definitions hold by construction. For a comparison clause, if q_{k−1} holds, position k is
    either still equal or the first difference, and X ≤ g·X forces n_{p_k} = false or n_{g(p_k)} = true there. ∎
- **P3 (blocking).** Under F3 (|N| = 2h + e), a base model falsifies ∨_{x∈Y} ¬n_x only if its support contains Y,
  i.e. equals Y.
- **P4 (composition).** As stated above.
- **P5 (generators).** Each g ∈ Γ is a permutation matrix on one party within a d-class, or a swap of two parties
  that carry the same partition.

### Completeness (replaces r1's syntactic-symmetry argument)

Fix (t, e) and a profile p. Let ψ be an AME(4,6) state with these parameters, normalized as above, with
non-classical support N ⊆ Π V_i.
- Each g ∈ Γ is a permutation matrix on one party or a swap of two parties carrying the same partition. So g·ψ is
  AME with the same s, t, e, V_i and d_{i,·}, and its non-classical support is g(N). Hence every member of H·N
  (H = ⟨Γ⟩) is the support of a normalized AME state with parameters (t, e, p).
- Let X* be the ≤-least member of H·N. X* extends to base auxiliaries by P1. Since X* ≤ g·X* for every g ∈ Γ, it also
  extends to the fresh lex auxiliaries by P2.
- If X* were not a recorded solution, it would satisfy every blocking clause (P3), and the final CNF (P4) would be
  satisfiable, contrary to its checked UNSAT. So X* is a recorded solution.
- Being a true support, X* satisfies every necessary condition of L46 §3 step 4. That contradicts its recorded
  exclusion.

This needs neither syntactic CNF symmetry, nor exact encodings, nor H-invariance of the checks. r1's claim that each
generator, with renamed auxiliaries, maps the clause set onto itself is false: the sequential-counter auxiliaries
depend on input order. Codex gave a counterexample: in the (30,4) base CNF of profile {2,2,2}⁴, generator 3 swaps
3333 and 4333 (variables 1 and 28), whose positive and negative occurrence counts are (103, 61) and (168, 77). The
claim is withdrawn here and in `review/ENGINE_V2_GUARD.erratum-1.md`.

### Phase certificates are closed components (Claude m2)

L42-10 applies to 2×2 components. Every stored certificate is checked by `code/phase_cert.py` (lines 72 and 75): each
corner's row and column in the stated reshaping contains exactly two points of N, so the block is a closed component.
The parent's replay checks the same closure for the 137 load-bearing certificates.

At e = 0, closure is automatic anyway:
- a solution has 2h points;
- for each pair, exactly h lines meet it, by (O3) and (O4), each in at least 2 points;
- so every hole line holds exactly two points.

All 137 load-bearing certificates are in (26,0), where e = 0.

### Guard

None of the RSS watchdog (6 GiB, SIGTERM only), the exact-byte disk accounting, the solution cap or the per-call time
limits tripped in the eight runs. The parent confirmed this from the reports (§5).

## 4. Results and load-bearing computation

Runs used CPython 3.13.9 and CaDiCaL 3.0.1 (SHA-256 601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa),
on 2026-10-17 PDT. In profiles, 2⁴ means {2,2,2,2} and 2⁵ means {2,2,2,2,2}.

### All 51 profiles

**(26,0)**, run 13:24:12–13:43:48: 25 profiles, 1695 solutions.
- Excluded in writing: {5,5}{2⁵}³ (Lemma 17). It held 1558 solutions: 1482 phase, 76 completion.
- With solutions, all phase-excluded:
  - {5,3,2}{2⁵}³: 51;
  - {4,4,2}{3,3,2,2}{2⁵}²: 29;
  - {4,2,2,2}³{3,3,2,2}: 10;
  - {4,2,2,2}²{3,3,2,2}{2⁵}: 16;
  - {4,2,2,2}{3,3,2,2}{2⁵}²: 16;
  - {3,3,2,2}{2⁵}³: 15.
- Without solutions:
  - {4,4,2}{3,3,2,2}³, {4,4,2}{3,3,2,2}²{2⁵}, {4,4,2}{2⁵}³;
  - {4,3,3}{3,3,2,2}³, {4,3,3}{3,3,2,2}²{2⁵}, {4,3,3}{3,3,2,2}{2⁵}², {4,3,3}{2⁵}³;
  - {4,2,2,2}⁴, {4,2,2,2}³{2⁵}, {4,2,2,2}²{3,3,2,2}², {4,2,2,2}²{2⁵}²;
  - {4,2,2,2}{3,3,2,2}³, {4,2,2,2}{3,3,2,2}²{2⁵}, {4,2,2,2}{2⁵}³;
  - {3,3,2,2}⁴, {3,3,2,2}³{2⁵}, {3,3,2,2}²{2⁵}², {2⁵}⁴.

**(27,2)**, 13:02:08–13:02:20: 6 profiles.
- Excluded in writing (Lemma 17): {3,3,3}⁴, which held all 28 solutions (20 components, 4 moduli, 4 completion);
  {3,3,3}³{3,2,2,2}; {3,3,3}²{3,2,2,2}².
- No solutions: {4,3,2}{3,2,2,2}³, {3,3,3}{3,2,2,2}³, {3,2,2,2}⁴.

**(28,2)**, 13:02:04–13:02:07, and **(28,3)**, 13:02:20–13:02:24: 7 profiles each, no solutions.
- Excluded in writing: {4,4}{2⁴}³ (Lemma 18), {3,3,2}⁴ and {3,3,2}³{2⁴} (Lemma 17).
- Remaining: {4,2,2}{2⁴}³, {3,3,2}²{2⁴}², {3,3,2}{2⁴}³, {2⁴}⁴.

**(29,3)** and **(29,4)**: {3,2,2}⁴, no solutions. These are cross-checks; Lemma 17 excludes the profile.

**(30,4)**, 13:02:03–13:02:04, and **(30,5)**, 13:02:07–13:02:08: 2 profiles each, no solutions.
- {3,3}{2,2,2}³ is excluded in writing (Lemma 17). {2,2,2}⁴ remains.

### The 37 load-bearing final UNSATs

The streams are in `explore/large_t_lex/`. Both hashes are SHA-256: the gzip stream, and the regenerated final CNF.

| case | profile | stream | stream SHA-256 | final CNF SHA-256 |
|---|---|---|---|---|
| (30,4) | {2,2,2}⁴ | t30_e4_2-2-2_2-2-2_2-2-2_2-2-2.final.lrat.gz | c533799470b0d1dc95c86423490191a32c08b5f022981d04fe7c42ebe600fe73 | 0e34ac7d90dbbaa0987e50eb1092630256e8a2023ce8e1ba0b0ed05f6b9db67a |
| (30,5) | {2,2,2}⁴ | t30_e5_2-2-2_2-2-2_2-2-2_2-2-2.final.lrat.gz | ea2448d21b8492a9074d0be77940bc63e427614ef2b992b5f5138a3e83ff605b | e3330f637a44934ce44ef8d1616a797d7e534fe867e02d5f52dbbbedc0c267d0 |
| (28,2) | {4,2,2}{2⁴}³ | t28_e2_4-2-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | 53d5b820cca1ab64fc598a5b84a31c87b9cd775af132e0e4a4ca2c76e222a44c | eeb21bc06d76dea07e2b35308ebfa5b7595d34ea5c7a8c2234585eb8a8939220 |
| (28,2) | {3,3,2}²{2⁴}² | t28_e2_3-3-2_3-3-2_2-2-2-2_2-2-2-2.final.lrat.gz | 1bb26362111190008b9b8979598be3b442d0b234aa05fd8dae245700f34037f4 | 495da7c3228fe929d1ef95e3afe1feedba522d3ff8f097f408190a721fdcb4d9 |
| (28,2) | {3,3,2}{2⁴}³ | t28_e2_3-3-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | a880487064271901659ea8633c4d9a3676a1efc63577f872b52be9c758987ad9 | ad04a115e7606e6fa0caaea94ef2bfc8ed4aaf5443af4f03949c8cd1f814c3f2 |
| (28,2) | {2⁴}⁴ | t28_e2_2-2-2-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | 952a9944b85db0284b52b18f4c35af2d11ba686117d81c5de1e140f212fcbf09 | cb25ff6a46176c42f07e695c43eb6dd3fdc921ec2b6113a377ef5f83f8ef4792 |
| (28,3) | {4,2,2}{2⁴}³ | t28_e3_4-2-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | d4bf98b6989c6a07992e4d699339ffd3f3a2221468a02774a734b8141b5dce35 | 522c0fde27409ed5567419e75645f7a15e5ede77fc9280efb37bbd96b9ad8ed9 |
| (28,3) | {3,3,2}²{2⁴}² | t28_e3_3-3-2_3-3-2_2-2-2-2_2-2-2-2.final.lrat.gz | 4030575aaa306f5128f1ca0d74f7f3fce580b8e9f77a9bbf0465118a4876a036 | cf461aa5840b282c3d0139117405ac8482bc3fde4de48e5668d66a5fc5eab863 |
| (28,3) | {3,3,2}{2⁴}³ | t28_e3_3-3-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | aeb76f2ee861dce40afc1e46dc4a057b0ad7f7c0e714f642c2202f2fa5ef6258 | c4473e522b3728b0f43c8b4624e7cce2e8b46ef29fa5935d6c4b44b092cdd435 |
| (28,3) | {2⁴}⁴ | t28_e3_2-2-2-2_2-2-2-2_2-2-2-2_2-2-2-2.final.lrat.gz | 6dbfde118e8f2d143d89b0c4c9618718a5b8685967c295b9d4483125de6f9440 | ea31afe83d7e0bbe4e05c0e30ed0e261b397c4ef281ceea9abbf1810cfa3771c |
| (27,2) | {4,3,2}{3,2,2,2}³ | t27_e2_4-3-2_3-2-2-2_3-2-2-2_3-2-2-2.final.lrat.gz | 352389bf80adc0a0bd54e5b45bf0fd7e2397f870979f634106b6399e5b5cd67d | 1517e725b748eeda72f3d2da98dae35363832e9bab45e8d4452ad648352ed564 |
| (27,2) | {3,3,3}{3,2,2,2}³ | t27_e2_3-3-3_3-2-2-2_3-2-2-2_3-2-2-2.final.lrat.gz | 01740aaf8739c7df0ec91a402cb092706a43d25a4714c7e82218fc014e72c45d | 965bea115a9abdcee7dc9e5ce78f8c84c1be6f80fe5f73f29ed634e799252bbd |
| (27,2) | {3,2,2,2}⁴ | t27_e2_3-2-2-2_3-2-2-2_3-2-2-2_3-2-2-2.final.lrat.gz | d1e700a609bfc84344b8f5779bf7c14fba6575613846768b6012b8b0a171854f | 8f59ddf394d7ef8875ffda2e91efd9537d098534366670b392c06868a2cf2476 |
| (26,0) | {5,3,2}{2⁵}³ | t26_e0_5-3-2_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 3026022a96f3a3aabcc38b161273b320dbf5321dccd7c006e9a3ce93da4929f2 | 8acdbfda1b999f7fcd1ca74b40b4fc31d57b1535eb30f724b151398add5c77e4 |
| (26,0) | {4,4,2}{3,3,2,2}³ | t26_e0_4-4-2_3-3-2-2_3-3-2-2_3-3-2-2.final.lrat.gz | e061431004efa30c8464aefcf38554aa11feef76c9b53f365c5d463d224e8ab4 | 4ad4bcf3cf5f448677e6bcf688dffa2bb793bd20d8da91b739444127250a080e |
| (26,0) | {4,4,2}{3,3,2,2}²{2⁵} | t26_e0_4-4-2_3-3-2-2_3-3-2-2_2-2-2-2-2.final.lrat.gz | 724f3dacc3efd57571a8a19755b501da1cc97b1f0b9ee0d903e9a15b9d63e6dd | ce465df9a5bd5f1a41d751d4aa5a3ca0c6c91d4401d49f5713d3c05f4971ebd5 |
| (26,0) | {4,4,2}{3,3,2,2}{2⁵}² | t26_e0_4-4-2_3-3-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | dd38747a1126058ae9c713bc5955941a3c3d4907b0dd8d6a83d02df0035458c8 | b16969d97b4fb2d7a0f6d095295fc28a0ff97afd3477a231d4a65513b07cc1a2 |
| (26,0) | {4,4,2}{2⁵}³ | t26_e0_4-4-2_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 636029a912ece6829a9169bbe3eeb3939b032d93d87ec7298cc3ac8726a03085 | 38ed013aa2f1b843969294c6a565e818446cb136faf0fa3baf7d6753152a2817 |
| (26,0) | {4,3,3}{3,3,2,2}³ | t26_e0_4-3-3_3-3-2-2_3-3-2-2_3-3-2-2.final.lrat.gz | 3bc22f145cfe1bd0c3e8e61c0d08d96890ab5dec5684a02e0cc4b23855e58e7d | d520a690af015a772ea08ebe531943b882f42c6323692b04cce4d8b92da90b7a |
| (26,0) | {4,3,3}{3,3,2,2}²{2⁵} | t26_e0_4-3-3_3-3-2-2_3-3-2-2_2-2-2-2-2.final.lrat.gz | 150272f297c695b891354e8921f1b69e4ee47850fd1b2e4fa4a5d4a90a6b932d | 389d6144ff6d724e59e34174be5f79c146dfb14940a5b817a39b257b20e58200 |
| (26,0) | {4,3,3}{3,3,2,2}{2⁵}² | t26_e0_4-3-3_3-3-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 821aabc8014f525529540670c6a3ab1b1842ca641f300130405a3def68b37972 | 580870f34c0a321dddfc19d30fc14f75fb404b5ba662b0ddda091fb821a48c68 |
| (26,0) | {4,3,3}{2⁵}³ | t26_e0_4-3-3_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | c85443540fd2111a203a2f2762fb9f1114e89833fd07635b219855fd58226da9 | f2211919c43cac2e6c88f213c96eabf2c6817458a61f974b602a53a4bb83901f |
| (26,0) | {4,2,2,2}⁴ | t26_e0_4-2-2-2_4-2-2-2_4-2-2-2_4-2-2-2.final.lrat.gz | b1dbd0f91dc9460f3633b8c309f7c89b4dfe3a13fc277a81e03f54cfec04506d | 945ce756a3a98672ce5a33500c921e3acf6085d8b14201d12b66310c1259f545 |
| (26,0) | {4,2,2,2}³{3,3,2,2} | t26_e0_4-2-2-2_4-2-2-2_4-2-2-2_3-3-2-2.final.lrat.gz | 282fd067b0d7e60f48963eeeed1399a3eb76f13211777f28fddbf23d8a63560a | b1a76f36ec8ff1c6ab80e7b32cadc76c91f084c06175c5ee2565609f102a0404 |
| (26,0) | {4,2,2,2}³{2⁵} | t26_e0_4-2-2-2_4-2-2-2_4-2-2-2_2-2-2-2-2.final.lrat.gz | b03d44ce745a186b4111f199d7e0c644b72acf2b03c3f61494a5047804241e42 | b8332f1e08aa9d72ba8d3b7ee537c5f9ef18a84d94203e3371163ebb007dbe91 |
| (26,0) | {4,2,2,2}²{3,3,2,2}² | t26_e0_4-2-2-2_4-2-2-2_3-3-2-2_3-3-2-2.final.lrat.gz | 90a150ecb9c9bf6ede4dbdbf9d4df1a8e9417cdb9337f896bed1da8d78a68f8b | 279edf2441a67f0ec5ed179592aa7d2e7efcddbc2574887b01c1fcb7fe7e80e9 |
| (26,0) | {4,2,2,2}²{3,3,2,2}{2⁵} | t26_e0_4-2-2-2_4-2-2-2_3-3-2-2_2-2-2-2-2.final.lrat.gz | 8b11abf1292206bfdc8294936ccdc643ff2ad60d47af8e93533c0c95be16608e | 6f1ac3aef62dc9c12504e43a36cf87aa7a62c4e0d84ba19b06031bcdb13f05cf |
| (26,0) | {4,2,2,2}²{2⁵}² | t26_e0_4-2-2-2_4-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 411670225055cfec6cba03e1fd2cc8018bdb09c2c5207423d15b2b76bc0cbf30 | 1dd56f089672bb647c76e2965515c75865bcf3d1209a2e40613c47776a09080f |
| (26,0) | {4,2,2,2}{3,3,2,2}³ | t26_e0_4-2-2-2_3-3-2-2_3-3-2-2_3-3-2-2.final.lrat.gz | c35b5fbaebc5bde9a420bf0840813c23a48ad8eaec606c6fb165e70adbdd791c | 293ef8aec4267288f4f48fad72bc24692301826545c81db1ac136fa8251e1515 |
| (26,0) | {4,2,2,2}{3,3,2,2}²{2⁵} | t26_e0_4-2-2-2_3-3-2-2_3-3-2-2_2-2-2-2-2.final.lrat.gz | 59261c331bd8f89294d9005b0b996d7809b774e2b13c3839751a50661aa16283 | 7e8eb049f7d3bcb73b69a9b9abde061f22e716fde0b1ebf17c1ed586d4e2c47c |
| (26,0) | {4,2,2,2}{3,3,2,2}{2⁵}² | t26_e0_4-2-2-2_3-3-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 0835d3bf6cc0e6e946561761f4cd6fdbdce5355bd9ef2bda34de64142bb160b9 | 59ceeccdf57676044e53d78dc0fde93b1ec976ffb9512e36872ad559b7c197bd |
| (26,0) | {4,2,2,2}{2⁵}³ | t26_e0_4-2-2-2_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | aeeaea4f3f676910b8be37a43ecf81af208464652b055bf12f2c05b22c407b02 | 87fa9eeae3b5c0c1df890382169fc049b93462f74e1678bd746ec5268d946fff |
| (26,0) | {3,3,2,2}⁴ | t26_e0_3-3-2-2_3-3-2-2_3-3-2-2_3-3-2-2.final.lrat.gz | 1762f111ffb14114765d498b29fbfcf3a790bde9e360d1d6462851e5b5a37a0e | 74d4d4c6494c33a3046d04783515704eebc5f67d2bc7b37b8b6448541168d8ff |
| (26,0) | {3,3,2,2}³{2⁵} | t26_e0_3-3-2-2_3-3-2-2_3-3-2-2_2-2-2-2-2.final.lrat.gz | 1395e7681ca6a82b5e27f5375010818da21b7c7b1c97fa6ec9c20f461d4ee91b | ab053108568c224296e364a03c49c64fe4f07db27f1da4e4f9c99a3a12333c5e |
| (26,0) | {3,3,2,2}²{2⁵}² | t26_e0_3-3-2-2_3-3-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 551dc4fc65ae39f80bb26e2258d0cebaeb4a7d46ba8e02f7ccffd51f036a135b | 6b1f22b3b9ccf8e7c4638273212013b4f043fd63d38829a523ab3a3e1cdc959d |
| (26,0) | {3,3,2,2}{2⁵}³ | t26_e0_3-3-2-2_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 5168c510d89f0bc0a515745ad0f2f2183986328964caa328682d3616c685cba6 | 0f0b13399b1aaf0b54b2d23c858196558de570bbb9b8fffc413ad2457e90e7c9 |
| (26,0) | {2⁵}⁴ | t26_e0_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2_2-2-2-2-2.final.lrat.gz | 2f2da9286a36a9042367c0c2e8138208c26a66eaf063e717a8962651c65d5576 | 3ebdc5323f5a351da34021e19acf9abe06179796edd7fdb4c3f8bcbb96a9b686 |

The (26,0) stream for {4,2,2,2}²{3,3,2,2}² contains 3 hints already satisfied when used, so it passes the worker's
Python checker only in skip mode. The parent's RUP replay covers it.

**Load-bearing phase certificates:** the 137 of (26,0) listed above (51 + 29 + 10 + 16 + 16 + 15). No completion,
moduli or components exclusion of the new cases is load-bearing.

### Narrowed import from LOWER46 (Claude m6)

With Lemmas 17 and 18, the load-bearing computation of L46 shrinks to:
- 7 final UNSATs: {2,2,2}⁴ at (30,0), (30,2) and (30,3); and at (28,0), {4,2,2}{2⁴}³, {3,3,2}²{2⁴}², {3,3,2}{2⁴}³
  and {2⁴}⁴;
- 11 phase obstructions: 7 in (28,0) {4,2,2}{2⁴}³ and 4 in (28,0) {2⁴}⁴;
- no completion UNSATs.

All of these are among the parent-verified items pinned in L46 r2 §5.

## 5. Executable record

All lane paths are relative to `physics/evidence/six-lane-20261016/ame46-support/`. Parent paths are relative to
`institute/runs/six-lane-2026-10-16/review/`. All runs are on 2026-10-17, PDT.

**Load-bearing (independent of the worker's checkers)**
- **Parent replay:** `ame46-lower48-parent-replay-v1/result.json`
  (464a121a5870f73a16269012783e990ae927b9dfcaaefcf70f76e753a283dbcf), run 14:01:54–14:02:18, PASS. It covers:
  - the 8 reports, all complete and untripped;
  - independent profile completeness for each h;
  - the written exclusions, recomputed;
  - exactly the 37 load-bearing final CNFs, regenerated with matching SHA-256 (the satisfied-hint stream included) and
    RUP-verified from the gzip LRAT addition sequences only, by the parent's pinned drat-trim with `-I -U`;
  - the 137 load-bearing compact phase certificates, independently checked: closure, zero weighted form, odd weight
    sum;
  - 6 gzip-pipeline controls.

**Worker inputs**
- **Engine v2:** `code/large_t_lex.py` (cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8).
  - Command per case: `cd code && OMP_NUM_THREADS=1 ../../depolarizing/env/bin/python -B large_t_lex.py --t T --e E --proof`.
  - It imports `large_t_gen.py` (28c0c1f9…bcfd), `large_t_e0.py` (67033dcf…466c), `phase_check.py` (0c591d1b…f693)
    and `ame_e0_cnf.py` (97e30ae4…8a26). The full SHA-256 values are in L46 r2 §5.
- **Interpreter:** CPython 3.13.9 at
  `/opt/homebrew/Cellar/python@3.13/3.13.9_1/Frameworks/Python.framework/Versions/3.13/bin/python3.13` (SHA-256
  50018add1e0d9b253f6466d9de81ea2aaea7ef4bd664db219e2d16cfe66e395b).
- **Guard:**
  - spec `review/ENGINE_V2_GUARD.r1.md` (d5733a7366c6d7fb3c197829ed6232abcb74c27f7250fa556cc59f34a3a273fd);
  - erratum `review/ENGINE_V2_GUARD.erratum-1.md` (6cb1fd8c4b86410af253d99b5a05b9d05ff8bb443ebe1d1e1586f0f55166ab65);
  - smoke `evidence/guard_smoke.json` (3c4ea4e6ad2346f358378c264994093e2dc1f58f4d288c3b927978cbf8c9db46).
- **Reports** (SHA-256):
  - t26_e0 7aafcb4a02498fa67fff4cad8d4865d835cdbf650aaa105c3593fa883fc6edb0;
  - t27_e2 4e5166da4a97f71e314be5125b6c21ffe63fef6be0c8ffd76d0df0dfb93a60a8;
  - t28_e2 bdfef2eb0943508cf798c658e9f679e10cde86b24a7ae6ab3bf5f1a0f4104d3e;
  - t28_e3 2ecf727263513498dde48aa0c57ae821d021282f47b83b49d49e429fb5a1966e;
  - t29_e3 d406a95d96d789a0f019d5ff7173250b8415f192b2f940773fd9a087d307d0e5;
  - t29_e4 3483bf4e403596d1685a6dff83a0de95e79c177a17c0d483f8faead13a22f01c;
  - t30_e4 147ea683c9c6cbe8010b246e6eab4949b8de2b3055dc96daff4fc3ee71c04901;
  - t30_e5 e334872ab1c02a29fa72b331dce91d7824ed2caa44db9fb7dd6add6846ad0c37.
  All files are `evidence/large_t_lex_t<t>_e<e>.json`.
- **Worker receipt** (reproducibility): `code/v2_receipt_r2.py`
  (328bf36b2dae8b42a53183d6751baaa73e284b4b13f592973a0c08df0e0e81ec) produced `evidence/v2_receipt_r2.json`
  (bf05ec215313eedd490293d1a04a7ca8ed073da30b58e5831587e497caada5fa), run 13:44:00–13:45:04.
  - It holds 131 streams, 1619 stored phase certificates (±1 and compact forms) and 80 completion records.
  - The certificate verifier is `code/phase_cert.py` (fbe3ab68899fec97486f1ce126749e820087d09fe5f12f2773199306883cb54e).
    It is separate from `phase_check.py` but has the same author. Its 5 negative controls were rejected.
- **Proof streams:** the gzip streams in `explore/large_t_lex/`, with the 37 load-bearing ones listed in §4. CNFs are
  not stored; they are regenerated from the profile, the pinned code and the report's solution order.

**Model reviews of r1**
- Codex: `ame46-lower48-codex-review-v1.note.md`, 24715d22af86cd6bc49abd6944106e4788c6fd401732d23d1f68d5422800214b.
- Claude: `ame46-lower48-claude-review-v1.note.md`, 9070080d21659fc5434db4e3ca2c8ea2d0b4977c4010fef79623634334594d58.

## 6. Not claimed

- Nothing about 59 versus 60 beyond the bound 48. This is a lower bound, not the minimum. With Pandya's upper bound 60,
  which is not re-reviewed here, the range is 48..60.
- Exploration runs, UNKNOWN runs and older-code batch outputs are not part of this proof.
- No novelty or priority claim. Lemma 18's argument is the parent orchestrator's, and the α = 1 case of Lemma 17 was
  derived independently by the parent.

## 7. Review dispositions (changes from r1)

**Codex.**
- MAJOR (false clause-set symmetry): fixed. §3 now uses the realizable-support completeness argument, and the guard
  erratum covers ENGINE_V2_GUARD §3 and the v2 docstring.
- MINOR (checker independence in the v2 docstring line 16 and the guard spec line 22): erratum E2. The header here
  uses "separately implemented by the same author".
- Note (no Lemma 18 flag in the receipt): §4 lists every written exclusion explicitly.

**Claude.**
- M1 (same symmetry error): fixed with Claude's completeness paragraph and properties P1–P5 (§3).
  - Claude also observes that L46 r1 LF142–143 rest on the same claim. L46 r2 withdraws them and argues through true
    supports.
- m1: the lex-leader clause schema, the blocking form, the final-CNF composition and a proof of P2 are now in §3.
- m2: phase closure is stated. `phase_cert.py` checks it, the parent's replay checks it, and it is automatic at
  e = 0 (§3).
- m3: the product-basis reduction sentence (Theorem) and the party-permutation sentence (§3 normalization) are added.
- m4: the reason that t = 29 has only {3,2,2}⁴ is given (§1). All 51 profiles are listed, and the 37 load-bearing
  final UNSATs are named with stream and CNF SHA-256 values (§4).
- m5: L46 r2 is pinned (fac5242b…f35b), replacing the reference to a "forthcoming" r2.
- m6: the narrowed L46 import is stated: 7 final UNSATs, 11 phase obstructions, no completion (§4).
- m7: editorial fixes.
  - The certificate reference is now §4 or §5.
  - Only six cases are counted as computer-assisted.
  - Notation: the officer facts are now (O1)–(O4), the counts κ0–κ2, the chain variables q_k, and group elements g.
  - The redundant line argument is replaced by the definition t_{i,a} = 6 − d_{i,a}.
  - Evenness is not used.
  - e ≥ 0 is cited from L42-4.
  - The closed form, the α-range remark and the two-line {5,5}{2⁵}³ argument are added.

The search, the CNFs, the proof streams, the certificates and the theorem are unchanged from r1.
