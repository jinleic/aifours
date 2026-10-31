# An M↔adjacency-row bridge, exact target completeness, and a redistribution-invariance blocker

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Fri Oct 30 03:12:45 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Response to the future-only direction: one actual-array realizability constraint beyond count/degree identities, plus an exact blocker. All statements are all-variable over every T2(n) (n ≥ 3; T2(11) is the case of interest). No selected hypothetical array, search, solver, program, external model, held episode or unadopted packet is used. Inputs: the T1/T2 definitions and the f282-dispositioned boundary laws (outdeg_M = α₉, indeg_M = α₁). No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. The row-separation bridge between M and the adjacency structure

Write ρ(u,v) for the (unique) row containing the adjacency u→v. Rows are indexed by first symbol.

**Theorem A (all T2(n)).** For all symbols a ≠ c:

(a,c) ∈ M  ⟺  ρ(a,b) ≠ ρ(b,c) for every b ∉ {a,c}.                (1)

Moreover, when (a,c) ∉ M, the b with ρ(a,b) = ρ(b,c) is unique: it is the middle symbol of the unique row realizing the event (a,c).

*Proof.* (⇐) If (a,c) ∉ M, some row r has a at position i and c at i+2. Its middle symbol b = R_r(i+1) differs from both (rows are permutations), and row r contains the adjacencies a→b and b→c, so ρ(a,b) = r = ρ(b,c). Uniqueness: two such b would realize the event twice, violating T2. (⇒) Suppose ρ(a,b) = ρ(b,c) = r for some b ∉ {a,c}. In row r the adjacency a→b occupies positions (i, i+1) and b→c occupies (j, j+1); both contain b, so i+1 = j, whence a sits at i and c at i+2: row r realizes the event (a,c), contradicting (a,c) ∈ M. ∎

This is an exact equivalence, not an inequality: **the distance-two layer M is precisely the set of ordered pairs whose two-step adjacency paths never close within one row.** It converts each arc of M into n−2 row-inequalities on the D1 structure ρ (at n = 11, nine inequalities per arc). It involves symbol identities and row identities, not merely degrees. Its honest status: a bridge/reformulation of the T2 condition in D1 terms — by itself it neither excludes nor realizes anything; §4 states exactly what is missing.

*Remark.* For a mutual pair {x,y} ⊆ M, (1) applies in both directions: ρ(x,b) ≠ ρ(b,y) and ρ(y,b) ≠ ρ(b,x) for all b ∉ {x,y}. No contradiction is derivable from this alone (a fixed-point-free correspondence S∖{a} → S∖{c} mapping c ↦ a plainly exists).

## 2. Exact target completeness (uniform over all multiplicities)

**Theorem B (all T2(n)).** For every symbol a, let Miss(a) = {c : (a,c) ∈ M}, |Miss(a)| = α₉(a). The distance-two events sourced at a have target set **exactly** S ∖ ({a} ∪ Miss(a)), each target occurring once. Dually, the events targeting c have source set exactly S ∖ ({c} ∪ Miss⁻¹(c)), |Miss⁻¹(c)| = α₁(c).

*Proof.* Symbol a sources exactly n−1−α₉(a) events (f282-adopted position-window count), with pairwise distinct targets, none equal to a (rows are permutations) or in Miss(a) (definition). The set S∖({a}∪Miss(a)) has exactly n−1−α₉(a) elements, so the inclusion is an equality. The dual argument uses positions 0,1 as the non-receiving window. ∎

So every symbol reaches, at distance two, **all** symbols except itself and its missing targets — full-source and α₉ ≥ 2 symbols alike; completeness is not a special property of boundary cases. Combined with the f282 disposition: in the both-columns-permutation branch, every symbol misses exactly one target and one source; in every other branch, at least one symbol misses none (full source) or is missed by none (full target), and symbols with α₉ = v ≥ 2 miss exactly v targets and hit all others.

## 3. Redistribution invariance: a proved barrier for distance-function counting

**Theorem C (all T2(n)).** Let f : {1,…,n−1} → ℝ be arbitrary and d_r({x,y}) the row distance of {x,y} in row r. Then

Σ_{unordered pairs} Σ_r f(d_r({x,y})) = n · Σ_{d=1}^{n−1} (n−d) f(d),       (2)

the same constant for **every** T2(n) — independent of the array, of (k₀,k₁,k₂) and of all boundary data.

*Proof.* Exchange the summations: each row contributes Σ_{i<j} f(|i−j|) = Σ_d (n−d)f(d), identically for every row. ∎

Instances: f = id gives Σ_{pairs} T = 2420 at n = 11; f = d² gives 13310. In particular the class-conditional minima used in my earlier aggregate bounds cancel in k₀ identically (each pair has n row-distances and exactly two at d = 1 in every class), which explains why those aggregates never constrained anything. **Consequence (blocker):** no aggregate of row-distance functionals — nor any count derived from the f282 universal equations — can distinguish T2(11) arrays or their profiles. Any genuine realizability constraint must depend on symbol identities, row identities, or position coincidences (as Theorem A does), not on distance statistics alone. This is a proved statement about where such constraints cannot come from.

## 4. Exact remaining gap (first unproved steps)

1. **Bridge → inequality.** Theorem A gives n−2 row-inequalities per M-arc, but no counting consequence has been extracted: the first unproved step is to derive from (1) any inequality binding α₉, α₁, ρ-structure jointly, or to exclude some configuration (e.g., a mutual pair with additional structure) for actual arrays.
2. **Mixed columns.** Exactly one permutation boundary column remains unruled-out for actual arrays (f282 disposition); Theorem B now supplies the exact per-symbol completeness data any such construction/exclusion must satisfy.
3. Nothing here realizes or excludes any branch; no witness and no no-go. **Unrestricted T2(11) remains OPEN.**
