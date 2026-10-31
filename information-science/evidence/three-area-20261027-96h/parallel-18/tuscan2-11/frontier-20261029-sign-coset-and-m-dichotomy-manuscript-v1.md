# Row-sign coset structure, the missing-pair boundary law, and the M-dichotomy for T2(11)

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 20:06:35 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Self-contained; it supersedes and folds in both prior packets of this thread and their corrections (§7). The theorems are written and all-variable. The finite computations cited are **labelled diagnostics** recomputed this session from pinned, twice-verified rows. No search, SAT, DRAT, scientific program, external model, review return or held material is an input. No formal/kernel, human, independent-model, novelty or parent-adoption claim.

**Named imports (adopted scopes only):**
- f187 item 1: the pinned order-21 square is a genuine linear T2 (used only as a diagnostic source of rows).
- f175 Theorem A (adopted): every T1(p), p an odd prime, has trivial symbol-automorphism group.
- f187 item 3 (adopted): normalized counts T2(3..8) = 0,1,0,1,0,6 (diagnostic provenance for the eight even-order squares).

## 1. Setup

A **T1(n)** array is n permutation rows of S={0,…,n−1} whose n(n−1) directed adjacencies (consecutive ordered pairs) are pairwise distinct. A **T2(n)** array is a T1(n) whose n(n−2) directed distance-two pairs (x_i,x_{i+2}) are also pairwise distinct. Two standard consequences, proved here: each symbol is **first** in exactly one row and **last** in exactly one row (its n−1 outgoing adjacencies need n−1 distinct rows, since a symbol has one successor slot per row; dually for incoming). Hence the first and last columns are permutations.

**Position windows.** In a row of length n, positions i=0,…,n−3 start a distance-two window; positions n−2 (penultimate) and n−1 (last) do not. *(This window fact is the correction of the earlier packet's error: a penultimate symbol never sources a distance-two pair.)*

For a T2(n), let **M** be the set of ordered pairs (x,y), x≠y, that never occur at distance two. Let α₉(x) = number of rows with x penultimate, α₁(x) = number with x second.

## 2. Boundary law of M (all T2(n); corrected)

**Theorem 1.** outdeg_M(x) = α₉(x) and indeg_M(x) = α₁(x) for every x; |M| = n; Σα₉ = Σα₁ = n.

*Proof.* Symbol x sits at one position in each of the n rows. It is last in exactly one row and penultimate in α₉(x) rows, so it sits at positions ≤ n−3 in exactly n−1−α₉(x) rows, each giving one distance-two event with source x. Two such events have distinct targets (a repeated pair (x,·) would violate T2). So x realizes exactly n−1−α₉(x) of its n−1 possible outgoing pairs, missing α₉(x). The dual argument counts incoming pairs with positions 0,1 non-receiving. Each row contributes one penultimate and one second symbol, giving the sums. ∎

Nothing forces α₉ or α₁ to be permutations; at n=8 the pinned T2(8) squares have non-permutation boundary columns (diagnostic; also implied by the adopted f187 item 3 refutations).

## 3. Row-sign coset theorem under symbol symmetry

For a row R (a sequence enumerating S), let sgn(R) be its sign as a permutation. A subgroup G ≤ Sym(S) is a **symbol symmetry** of the array if the positionwise image gR of every row is again a row.

**Lemma 2 (freeness).** gR = R implies g = id. *Proof.* R contains every symbol; g fixes each entry. ∎ So every row orbit under G has size |G|, and |G| divides n.

**Theorem 3 (coset structure).** sgn(gR) = sgn(g)·sgn(R). Hence within a row orbit, the multiset of row signs is sgn(R₀)·{sgn(g) : g ∈ G} — a coset of the image of the sign homomorphism on G. Consequently:
1. If G ≤ A_n, each orbit is sign-constant.
2. If G acts transitively (|G| = n), the whole array has a single sign class iff G ≤ A_n; otherwise the sign homomorphism is onto {±1}, exactly half of G is odd, and the split is exactly **[n/2, n/2]**.
3. If |G| is odd, every element of G has odd order, all its cycles have odd length, and it is even; so G ≤ A_n.

*Proof.* (gR)(i) = g(R(i)) says gR = g∘R as maps position→symbol, and sign is multiplicative. The orbit of R₀ is {gR₀ : g ∈ G} with signs sgn(g)sgn(R₀); freeness makes g ↦ gR₀ a bijection, so the sign multiset is the stated coset. The rest is the homomorphism theorem; for (3), a cycle of odd length ℓ has sign (−1)^{ℓ−1} = +1. ∎

## 4. Applications: theorem or coincidence? (diagnostics labelled)

Diagnostics recomputed this session from the pinned rows (T2(21) from the f187-adopted file; the eight even-order squares from the f187 item-3 enumerations):

| array | symbol symmetry (diagnostic) | forced by Thm 3 | observed split |
|---|---|---|---|
| T2(4) | Z₄, contains odd 4-cycles | **[2,2]** (transitive, ⊄A₄) | [2,2] ✓ theorem |
| T2(6) | Z₆, contains odd 6-cycles | **[3,3]** (transitive, ⊄A₆) | [3,3] ✓ theorem |
| T2(8), 4 squares | Z₂ = ⟨even (2,2,2,2)⟩ | orbits size 2, sign-constant: split may be any [2k, 8−2k] | [4,4] — allowed, **not forced** |
| T2(8), 2 squares | Z₄ = ⟨even (4,4)⟩ (two 4-cycles: sign +1) | two orbits size 4, sign-constant: [8] or [4,4] | [8] — allowed, **not forced** |
| T2(21) | transitive G₂₁ of odd order 21 | **[21]** (Thm 3.3 + transitivity) | [21] ✓ theorem |

**Conclusion.** The sign-class observation is a **theorem** exactly when a transitive symbol symmetry exists: forced [2,2], [3,3], [21] at n=4,6,21. At n=8 the observed patterns are consistent with, but not implied by, the (necessarily even) symmetries — an empirical regularity of the six known squares, not a law.

**At n = 11 the mechanism is vacuous.** By the adopted f175 Theorem A, every T1(11) — hence every T2(11) — has trivial symbol-automorphism group: G = 1, no orbits, no coset constraint. Therefore no symmetry-based sign obstruction can exist at order 11; the sign multiset of a hypothetical T2(11) is unconstrained by this route (one global parity fact: row 0 can be normalized to the identity, but no constraint on the remaining ten signs is known).

## 5. The M-boundary dichotomy at n = 11

**Theorem 4.** For every T2(11), exactly one of the following holds for the penultimate column:
- **(A) Permutation case.** α₉(x) = 1 for all x. Then by Theorem 1, M is the digraph of a **fixed-point-free permutation** of the 11 symbols (all in/out-degrees 1; no loop, since a distance-two pair has distinct symbols). Its cycle type is one of the **14** partitions of 11 into parts ≥ 2: 11; 9+2; 8+3; 7+4; 7+2+2; 6+5; 6+3+2; 5+4+2; 5+3+3; 5+2+2+2; 4+4+3; 4+3+2+2; 3+3+3+2; 3+2+2+2+2.
- **(B) Full-source case.** Some symbol y has α₉(y) = 0. Then y misses no outgoing pair: **every** ordered pair (y,z), z≠y, occurs exactly once at distance two; y is last in exactly one row and occupies positions 0..8 in each of the other ten rows, realizing ten distinct targets.

The identical dichotomy holds independently for the second column and in-degrees (full-target symbols).

*Proof.* Case distinction on whether all α₉(x) = 1. In (A), Theorem 1 gives a 1-in-1-out loopless digraph on 11 vertices with 11 arcs, i.e., a permutation digraph without fixed points; its cycle types are the partitions of 11 with no part 1 (14 of them, listed exhaustively). In (B), α₉(y) = 0 gives outdeg_M(y) = 0 by Theorem 1, so all ten outgoing pairs occur; the position count is §1's window fact. ∎

This is a **search reduction, not an obstruction**: any future frozen search may branch on the 14 permutation types of case (A) or on the full-source structure of case (B). No case is excluded here.

## 6. Corrected reversal-map statement (supersedes the earlier "bijection")

For any T1(n) and unordered symbol pair {x,y}, the two directed adjacencies lie in **two distinct rows** (a symbol has one successor slot). The map {x,y} ↦ {row(x→y), row(y→x)} into unordered row pairs is therefore well defined, and the reversal multigraph H on the n rows is (n−1)-regular with C(n,2) edges — but it is **not injective in general**:

- Diagnostic (this session, pinned rows): distinct images / total pairs and max multiplicity: T2(4) 2/6 (mult 3); T2(6) 3/15 (mult 5); T2(8) 12–16/28 (mult 3); T2(21) 147/210 (mult 3).

So the "reversal bijection" retained by my first erratum is **false**; only the distinctness of the two rows and the H degree/edge counts survive. At n = 11 the multiplicity profile of H is unknown (no T2(11) is known).

## 7. Supersession (errata folded in)

1. `frontier-20261029-reversal-multigraph-and-missing-pair-structure-v1.md` (SHA `abfc0a0b…f82635`): the permutation claim, the forced boundary columns, Corollary 4.1 and the six-type list are withdrawn by its erratum (`6be892b1…34f8f`), which is itself superseded by §6 (the "bijection" survivor is false; the correct count of derangement types is 14, not 6).
2. This manuscript is the single current statement of the thread: Theorems 1, 3, 4 and the corrected reversal facts of §6.

## 8. Residual — no obstruction reached

What is proved: the boundary law of M; the coset theorem for row signs under symbol symmetry, with forced splits exactly in the transitive cases; its **vacuity at n = 11** (no symmetry exists there); the 14-type derangement/full-source dichotomy for M; and the non-injectivity of the reversal map (diagnostic). What is **not** proved: any constraint binding a hypothetical T2(11) beyond case-splitting on Theorem 4; realizability or exclusion of any dichotomy case; any witness. The sign-class route is provably unusable as an obstruction at order 11. **T2(11) remains OPEN.**
