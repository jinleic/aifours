# Middle-uniformity, the position census with a proved boundary inequality, and the double realization of α_{n−2}

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Fri Oct 30 03:44:33 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** One bounded delivery of all-variable consequences of the row/ρ conditions, separate from the frozen f292 input (`frontier-20261030-closing-pairs-derangements-and-failed-inequality-v1.md`, SHA `77e61e00…65e9`, untouched). No selected hypothetical array, program, search, solver, kernel cell or external model. Finite checks cited only as labelled diagnostics on pinned/adopted squares. No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. Middle-uniformity (all T1(n))

**Theorem 1.** In every T1(n), each symbol is the **middle** of exactly n−2 consecutive triples (distance-two events). With T2, the n−2 sources and the n−2 targets of those events are each pairwise distinct.

*Proof.* The middle of the event at positions (i, i+1, i+2) sits at position i+1 ∈ {1,…,n−2}. Symbol b occupies position 0 in exactly one row and position n−1 in exactly one row (first/last columns are permutations), hence positions 1..n−2 in exactly n−2 rows, and in each such row it middles the unique triple through its position. Distinctness under T2: two events with middle b share the source only if two rows contain the same adjacency into b (excluded by D1), and share the target dually. ∎

So middles are distributed perfectly uniformly even though sources and targets are not (they follow α_{n−2} and α₁). Σ_b (n−2) = n(n−2) events ✓.

## 2. Position census and a proved boundary inequality (all T1(n))

For symbol a, classify each of the n rows by a's role at its position: source (positions 0..n−3), middle (1..n−2), target (2..n−1). By position:

| position | role | # rows |
|---|---|---|
| 0 | source only | 1 |
| 1 | source ∧ middle | α₁(a) |
| 2..n−3 | all three | n−4−α₁(a)−α_{n−2}(a) |
| n−2 | middle ∧ target | α_{n−2}(a) |
| n−1 | target only | 1 |

**Corollary 2 (proved inequality, all T1(n)).** For every symbol a:

α₁(a) + α_{n−2}(a) ≤ n−4.                                        (1)

At n = 11: a symbol cannot be second and penultimate more than 7 times in total (each at most 7 given the other ≥ 1... the inequality itself allows 0). This is a genuine realizability constraint on the boundary column pair beyond the sums Σα = n: e.g. at n = 11 no symbol may satisfy α₁(a) = α_{n−2}(a) = 5.

## 3. Double realization of α_{n−2} and of α₁ (all T2(n))

Let ρ(u,v) be the row of adjacency u→v and λ(b) the row where b is last.

**Theorem 3.** For every a: the two sets
- Miss(a) = {c : (a,c) ∈ M} (missing distance-two targets), and
- U(a) = {b : ρ(a,b) = λ(b)} (symbols whose adjacency from a sits in the row ending at b)

have the **same cardinality** α_{n−2}(a). Dually, Miss⁻¹(a) = {b : (b,a) ∈ M} and V(a) = {b : F(b) = a} (symbols whose row opens into a) both have cardinality α₁(a). Note U(a) is defined by an adjacency-row condition, Miss(a) by event absence — they are different sets of the same size.

*Proof.* b ↦ λ(b) bijects U(a) with {rows r whose penultimate symbol is a} (r = λ(b) ends at b and contains a→b, so a is r's penultimate), giving |U(a)| = α_{n−2}(a); the boundary law gives |Miss(a)| = α_{n−2}(a). The dual is the same with row openings. ∎

Diagnostic (labelled, pinned T2(4) by hand): Miss(3) = {0} while U(3) = {1} — disjoint sets of equal size 1. So neither inclusion holds in general; |Miss(a) ∩ U(a)| is a genuinely open structural parameter, unconstrained by current tools (it enters nowhere in the count identities).

## 4. Exact obstruction report (the natural inequality that resists proof)

**Candidate (C):** k₀ ≤ #{2-cycles of E} (mutual M-pairs are at most the transpositions of the endpoint permutation). Diagnostics (labelled, pinned/adopted): equality holds in T2(4) (2 = 2), T2(6) (3 = 3) and T2(21) (0 = 0); the six T2(8) satisfy 0 ≤ 4. But the three equalities arise by three different mechanisms (M = C at n = 4, 6; group-right-multiplication at n = 21), so the pattern is confounded by provenance.

**Where the proof fails.** The ψ/π machinery of the frozen packet converts membership of a *closing* pair in M into derangement-ness of an explicit permutation π_c; it provides no mechanism connecting a *mutual* pair {x,y} ⊆ M to E's cycle type. Concretely, from (x,y), (y,x) ∈ M one obtains that ψ_{x,y} and ψ_{y,x} are fixed-point-free correspondences; if additionally E(x) = y these become derangement permutations π-y... but nothing forces or forbids E(x) = y. The first unproved step is any relation between the fixed-point structure of ψ on mutual pairs and the cycle structure of E. No conjecture here is promoted to a claim.

## 5. Residual

Theorems 1 and 3 and inequality (1) are proved for all arrays; they constrain realizability (the census is exact, not a relabeling of M = C) but exclude nothing by themselves. All boundary types and mixed column cases remain live; no witness, no no-go; **unrestricted T2(11) remains OPEN.**
