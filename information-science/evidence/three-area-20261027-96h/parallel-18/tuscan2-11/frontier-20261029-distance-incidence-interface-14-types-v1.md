# The distance-two incidence interface: per-type profiles for the 14-way M-branch of T2(11)

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 20:22:35 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** It develops the 14-way branch of the f279-frozen M-dichotomy as an exact search interface. All statements are all-variable and quantified over every original T2(n) / T2(11); the finite computations cited are **labelled diagnostics** on pinned, previously verified squares. No selected hypothetical square, search, SAT, DRAT, program, external model, review return or held material is used. No formal/kernel, human, independent-model, novelty or parent-adoption claim. The f279 review is pending; this packet depends on its Theorem 1 (boundary law of M) only as a **named unreviewed import**, restated here with its two-line proof so the interface stands alone modulo that proof.

## 1. Framework: distance-two incidence of unordered pairs

Let A be a T2(n). Each symbol occurs exactly once per row, so for every unordered symbol pair {x,y} and every row r there is a well-defined row distance d_r({x,y}) ∈ {1,…,n−1}. Let

n₂({x,y}) = #{rows r : d_r({x,y}) = 2}.

An occurrence with x before y is the ordered event (x,y). T2 injectivity gives:

**Lemma 1.** For each unordered pair, n₂ ≤ 2, and n₂ = 2 only with one occurrence in each direction (two distinct rows; both directions in one row is positionally impossible, since it would need x at i and i+2−2 = j+2 and y at i+2 and j, forcing i = i+4). Define
- k₀ = #{pairs : n₂ = 0}, k₁ = #{pairs : n₂ = 1}, k₂ = #{pairs : n₂ = 2}.

**Theorem 2 (profile identities, all T2(n)).** k₁ + 2k₂ = n(n−2) (count ordered events); 2k₀ + k₁ = n (count the n missing ordered pairs, i.e. the arcs of M, by mutuality: a mutual unordered pair carries 2 arcs of M, an asymmetric one carries 1); hence k₂ = n(n−1)/2 − n + k₀ and **k₁ ≡ n (mod 2)**. In particular **k₁ is odd at every odd n, including 11.**

*Proof of the M-arc count.* (x,y) ∈ M iff the ordered event (x,y) never occurs iff the pair {x,y} has n₂ ≤ 1 with x's direction absent; summing arcs of M over unordered pairs counts mutual pairs twice and asymmetric pairs once. ∎

**Import (f279 Theorem 1, unreviewed, proof recalled).** outdeg_M(x) = α₉(x) (penultimate-column count), indeg_M(x) = α₁(x), |M| = n. Proof: x sits at positions ≤ n−3 in exactly n−1−α₉(x) rows, each yielding one outgoing event with distinct targets. ∎

## 2. Case (A): the profile is determined by the number of 2-cycles of M

Suppose case (A) of the dichotomy: the penultimate column is a permutation, so M is a fixed-point-free permutation of the n symbols. Then the mutual pairs of M are exactly its 2-cycles. Writing t = number of 2-cycles in the cycle decomposition of M:

**Theorem 3 (all T2(n), case A).** k₀ = t, k₁ = n − 2t, k₂ = n(n−1)/2 − n + t. The distance-two incidence profile of the whole array is determined by t alone; the remaining cycle-length structure of M does not enter (k₀,k₁,k₂).

**At n = 11** the 14 dichotomy types collapse to **five** interface profiles:

| cycle types of M (t = #2-cycles) | k₀ | k₁ | k₂ |
|---|---|---|---|
| 11; 8+3; 7+4; 6+5; 5+3+3; 4+4+3 (t=0) | 0 | 11 | 44 |
| 9+2; 6+3+2; 5+4+2; 3+3+3+2 (t=1) | 1 | 9 | 45 |
| 7+2+2; 4+3+2+2 (t=2) | 2 | 7 | 46 |
| 5+2+2+2 (t=3) | 3 | 5 | 47 |
| 3+2+2+2+2 (t=4) | 4 | 3 | 48 |

Readings, all forced: e.g. a T2(11) whose M is an 11-cycle must have **every** unordered pair at distance two in at least one direction (k₀=0), exactly 11 pairs in only one direction, and 44 pairs in both; a T2(11) with M of type 3+2+2+2+2 has exactly 4 pairs never at distance two and only 3 asymmetric ones.

**Sub-branch (A1: M = E⁻¹).** If additionally M equals the inverse of the last-column permutation E — the circular-completion condition — then the profile attaches to E: k₀ = #2-cycles of E. This is the 2-perfect-circular case; its symmetry classes are governed by the adopted f204 scope (Aut ∈ {1,2,3,6} for such extensions). No case of it is excluded here.

## 3. Case (B): what remains forced

If the penultimate column is not a permutation, M is a general directed multigraph-free digraph on n vertices with |M| = n arcs, out-degrees α₉ and in-degrees α₁ (import). Theorem 2 still forces 2k₀ + k₁ = n with **k₁ odd** at n = 11; now k₀ counts mutual pairs of a non-permutation digraph and is not determined by a cycle count. Full-source symbols (α₉(x) = 0 ⇒ all outgoing pairs present) and full-target symbols (α₁(x) = 0) exist whenever any α₉, α₁ exceeds 1.

## 4. Diagnostics (labelled; pinned squares only)

Recomputed this session from the pinned, twice-verified rows (T2(21) from the adopted f187 file; even-order squares from the adopted f187 item-3 enumerations):

| square | case | k₀ | k₁ | k₂ | checks |
|---|---|---|---|---|---|
| T2(4) | A (M = (2,2), t=2) | 2 | 0 | 4 | 2k₀+k₁=4 ✓; k₁+2k₂=8 ✓ |
| T2(6) | A (M = three 2-cycles, t=3) | 3 | 0 | 12 | 6 ✓; 30 ✓ |
| six T2(8) | B (outdeg profiles [3,3,1,1] or [2,2,2,2]) | 0 | 8 | 20 | 8 ✓; 48 ✓; k₁ even (n even) ✓ |
| T2(21) | A (M = three 7-cycles, t=0) | 0 | 21 | 189 | 21 ✓; 399 ✓ |

The n=21 row realizes the t=0 profile exactly as Theorem 3 predicts (k₁ = 21, k₂ = 189). The n=4, n=6 rows realize the t = C(n,2) extreme (M all 2-cycles). All six T2(8) squares have k₀ = 0 — no mutual missing pair — an empirical observation in case (B), not a theorem.

## 5. Interface use and residual

Any future frozen search over T2(11) may branch on the dichotomy and impose the exact profile (k₀,k₁,k₂) per type, or in case (B) the odd-k₁ law plus boundary degree sequences. What is proved here: the identities of Theorem 2 for every T2(n); the determination by t in case (A) with the five-profile table at n = 11. What is **not** proved: realizability or exclusion of any profile or type, any constraint beyond these counts, any witness. This is an interface, not an obstruction; **T2(11) remains OPEN**.
