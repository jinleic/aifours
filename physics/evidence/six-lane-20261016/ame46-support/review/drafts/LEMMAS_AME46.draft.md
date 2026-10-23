# DRAFT (not frozen): lemmas for the minimum support of AME(4,6) states

Lane `physics/evidence/six-lane-20261016/ame46-support`. Worker-written and unreviewed. Notation is that of README §0.2.

Sources: Pandya arXiv:2610.16673v1, pinned as `sources/arxiv-2610.16673v1.layout.txt` (SHA-256 3a7d4fef…bae7).
Line numbers (LF) refer to that layout.

## 0. Setting

- ψ = Σ_x ψ_x |x⟩, x ∈ [6]^4. For a pairing π = (ab|cd), U_π[(x_a,x_b),(x_c,x_d)] = 6ψ_x.
- For a pure state, ρ_ab = U_π U_π†/36 and ρ_cd = (U_π†U_π)^T/36. Hence ψ is AME(4,6), i.e. all six two-party
  marginals equal I/36, iff U_π U_π† = U_π†U_π = I for the three pairings, i.e. iff all three U_π are unitary
  (Pandya, proof of Lemma 1, LF248–253).
- Local unitaries preserve the AME property. So it suffices to bound |S|, S = supp ψ, for an arbitrary AME state in
  the computational basis.
- A P-line is the set of x with x_P = z, for P a pair of coordinates and z ∈ [6]². Every P-line is a row or a column
  of exactly one U_π, and every row or column is a P-line.

## 1. Basic lemmas

**Lemma 1 (norms).** For every P-line L, Σ_{x∈L} 36|ψ_x|² = 1.
*Proof.* Rows and columns of a unitary matrix are unit vectors. ∎

**Lemma 2 (classical officers).** Let x ∈ S.
- (a) If |ψ_x| = 1/6, then no other y ∈ S agrees with x in two or more coordinates.
- (b) If some P-line meets S only in x, then |ψ_x| = 1/6.
*Proof.* (a) If y ≠ x agrees with x on a pair P, then x and y lie in a common P-line. By Lemma 1,
36|ψ_x|² + 36|ψ_y|² ≤ 1, so ψ_y = 0. (b) This is Lemma 1 for that line. ∎

**Lemma 3 (code).** Any two classical officers agree in at most one coordinate.
*Proof.* Lemma 2(a). ∎

**Lemma 4 (count).** s ≥ 72 − t. The number e := s − (72 − t) ≥ 0 does not depend on the reshaping.
*Proof.* Fix U_12|34.
- Each x ∈ S lies in exactly one row.
- A row containing a classical officer contains nothing else (Lemma 2(a)). By Lemma 3, distinct classical officers
  lie in distinct rows, so these rows number t.
- Every other row is non-empty (Lemma 1) and contains no single element (Lemma 2(b)), so it has at least two.
- Hence s ≥ t + 2(36 − t). The quantities s and t do not depend on the reshaping. ∎

**Lemma 5 (overlap).** If V is unitary and r ≠ r′ are rows, then |supp(r) ∩ supp(r′)| ≠ 1. The same holds for
columns.
*Proof.* If the supports met in exactly one column, the inner product of r and r′ would be a single non-zero
product, contradicting orthogonality. ∎

**Lemma 6 (components).** Let V be an n×n unitary matrix and B(V) the bipartite graph on rows ∪ columns whose edges
are the non-zero entries. Every connected component K of B(V) has as many rows as columns. V restricted to
rows(K) × cols(K) is unitary, and every other entry in these rows and columns is zero.
*Proof.*
- The rows of K are orthonormal and supported in cols(K), so |rows(K)| ≤ |cols(K)|.
- Symmetrically, the columns of K give |cols(K)| ≤ |rows(K)|.
- The restricted matrix therefore has orthonormal rows and is square, hence unitary. ∎

**Lemma 7 (component sizes).** In each U_π:
- the 1×1 components are exactly the entries of the classical officers;
- every other component K has k ≥ 2 rows, every one of its rows and columns has at least two entries, and it has
  |K| = 2k + e_K entries with e_K ≥ 0.
Moreover:
- (a) e_K = 0 iff k = 2, and then K is a full 2×2 block;
- (b) e_K ≠ 1;
- (c) e = Σ_K e_K, summed over the components with k ≥ 2.
*Proof.*
- A 1×1 component is an entry alone in its row; by Lemma 2(b) it is a classical officer. A classical officer's row
  and column contain nothing else (Lemma 2(a)), so it forms a 1×1 component.
- In any other component, a row with one entry would be a classical officer, hence a 1×1 component. So rows (and
  columns) have at least two entries.
- (a) Suppose every row of K has exactly two entries, and take a row r with support {c, c′}. Any row r′ meeting
  {c, c′} meets it in at least two columns (Lemma 5), so supp(r′) = {c, c′}. Thus no row of K reaches a column
  outside {c, c′}, so k = 2. The converse is immediate.
- (b) Suppose e_K = 1. Then all rows have two entries except one row r0, with support C0 of size 3.
  - A two-entry row meeting C0 lies inside C0 (Lemma 5).
  - Let r be a two-entry row disjoint from C0. Every row meeting supp(r) has support supp(r): for two-entry rows
    this is the argument of (a), and r0 does not meet supp(r). So such rows are not in r0's component.
  - Hence cols(K) = C0 and k = 3. The two other rows have 2-subsets of C0 as supports, and these intersect. By
    Lemma 5 they are equal, say {c, c′}.
  - The third column c″ of C0 then has a single entry, in row r0. By Lemma 2(b) that entry is classical, so by
    Lemma 2(a) its row r0 has no other entry. This contradicts |C0| = 3.
- (c) Sum the entries over all components. ∎

**Lemma 8 (scout lead, now proved).** If s ≤ 59, then t ≥ 14 and e ≤ t − 13.
*Proof.*
- e ≤ t − 13 is s ≤ 59 rewritten, and s ≥ 72 − t gives t ≥ 13.
- If t = 13, then e = 0. By Lemma 7, every non-classical component of U_12|34 is a 2×2 block, so 36 − 13 = 23 would
  be even. Contradiction. ∎

**Lemma 9 (slices).** For a coordinate i and a value a, let t_{i,a} = |{x ∈ T : x_i = a}| and d_{i,a} = 6 − t_{i,a}.
For j ≠ i, let D_j^{(i,a)} = [6] ∖ {y_j : y ∈ T, y_i = a}; it has size d_{i,a} by Lemma 3.
- Every x ∈ N with x_i = a has x_j ∈ D_j^{(i,a)} for all j ≠ i.
- For every b ∈ D_j^{(i,a)}, the {i,j}-line with value (a, b) contains at least two elements of N.
Consequently:
- (a) d_{i,a} ≠ 1;
- (b) Σ_a d_{i,a} = h := 36 − t;
- (c) if d_{i,b} = 0, no element of N has x_i = b; in particular, if only one value a has d_{i,a} > 0, then every
  element of N has x_i = a.
*Proof.*
- If x_j = y_j for some y ∈ T with y_i = a, then x and y agree on {i, j}, contradicting Lemma 2(a).
- The {i,j}-line with value (a, b), b ∈ D_j^{(i,a)}, contains no classical officer. It is non-empty (Lemma 1) and
  has no single element (Lemma 2(b)).
- (a) If d_{i,a} = 1, every element of N with x_i = a has all its coordinates determined, so there is at most one
  such element. But the line (a, b), b ∈ D_j^{(i,a)}, contains at least two. Contradiction.
- (b) Σ_a t_{i,a} = t.
- (c) D_j^{(i,b)} = ∅. ∎

**Lemma 10 (hole bound).** |N| = 2h + e ≤ h².
*Proof.* Every element of N lies in a non-classical row and a non-classical column of U_12|34. There are h of
each. ∎

**Lemma 11 (e = 0 line structure).** If e = 0, every non-classical line contains exactly two elements of S, both
non-classical. Within slice (i, a), the value x_j (j ≠ i) takes each element of D_j^{(i,a)} exactly twice. So
|{x ∈ N : x_i = a}| = 2 d_{i,a}.
*Proof.* With e = 0, Lemma 7 makes every non-classical component a full 2×2 block, so each non-classical row and
column has exactly two entries. Every line of every reshaping is such a row or column. Count the slice through the
lines (a, b), b ∈ D_j^{(i,a)} (Lemma 9). ∎

## 2. Large-t exclusions (partial lower bound)

**Theorem A (draft).** Every AME(4,6) state has s ≥ 43 — *pending the (t, e) = (30, 0) analysis*. Proved so far:
s ≥ 41.

*Proof of s ≥ 41.* Suppose s ≤ 40. Then t ≥ 32 by Lemma 4.
- **t = 36.** Every line contains a classical officer, so N = ∅ and S = T is a set of 36 codewords meeting every
  line once. This is a pair of orthogonal Latin squares of order six, which does not exist (Tarry; cited through
  Pandya LF45, refs [7–9]). [cited]
- **t = 35.** h = 1, but every positive d_{i,a} is at least 2 (Lemma 9(a)), so Σ_a d_{i,a} = 1 is impossible.
- **t ∈ {33, 34}.** h ∈ {3, 2}. Every positive d_{i,a} is at least 2 and they sum to h ≤ 3, so each coordinate
  has a single value with positive deficit. By Lemma 9(c), all elements of N then agree in every coordinate,
  so |N| ≤ 1. But h > 0, so there is a non-classical line, which contains at least two elements of N
  (Lemma 4). Contradiction.
- **t = 32, so s = 40 + e ≤ 40 and e = 0.** Here h = 4, and each coordinate's positive deficits are {4} or {2, 2}.
  - Suppose coordinate i has profile {4}, with value a. Then N ⊆ {x_i = a} (Lemma 9(c)). For j ≠ i, the four
    lines (a, b), b ∈ D_j^{(i,a)}, each contain elements of N, so x_j takes four values on N. But coordinate j
    allows at most two values (Lemma 9(c)). Contradiction.
  - Hence every coordinate has profile {2, 2}, so N ⊆ V_1 × V_2 × V_3 × V_4 with |V_i| = 2.
  - The h = 4 hole cells of each pair (i, j) are exactly V_i × V_j, each containing exactly two elements of N
    (Lemma 11). So N is an OA(8, 4, 2, 2) on the subcube.
  - By the Fourier lemma (§3), N = {x : Σ_{i∈U} x_i ≡ c (mod 2)} with |U| ∈ {3, 4}.
  - Each of these ten sets has an inconsistent 2×2-block phase system (§4): a three-block obstruction, verified
    exactly by `code/phase_check.py`.
  Hence s ≥ 41. ∎

*s = 41 is impossible.* It would need t = 31 with e = 0, but 36 − 31 = 5 is odd (Lemma 7(a)); or t = 32 with e = 1,
excluded by Lemma 7(b) and (c); or t ≥ 33, excluded above. So s ≥ 42.

*s = 42* needs one of:
- (t, e) = (30, 0) — open in this draft;
- (31, 1) — excluded by Lemma 7;
- (32, 2) — excluded: h = 4, so U_12|34 would have a single connected 4×4 non-classical component with 10 entries;
  §5 shows this is impossible;
- t ≥ 33 — excluded.

## 3. Fourier lemma (OA(8,4,2,2) as subsets of {0,1}^4)

If N ⊆ {0,1}^4, |N| = 8, has all six 2-dimensional marginals uniform (two points per cell), then
N = {x : Σ_{i∈U} x_i ≡ c} for some U with |U| ∈ {3, 4} and some c.

*Proof.*
- Let g = 2·1_N − 1, a ±1-valued function. Uniform 1- and 2-marginals mean ĝ(u) = 0 for 1 ≤ |u| ≤ 2, and |N| = 8
  means ĝ(0) = 0. So g = Σ_{u∈F} ĝ(u)χ_u with F ⊆ {u : |u| ≥ 3} (four vectors of weight 3 and 1111).
- g² ≡ 1 gives Σ_{u,v∈F} ĝ(u)ĝ(v)χ_{u⊕v} = 1.
- For distinct u, v ∈ F the sums u ⊕ v are pairwise distinct and non-zero: the six sums of two weight-3 vectors are
  the six weight-2 vectors, and the four sums with 1111 are the four weight-1 vectors.
- So for each pair u ≠ v the coefficient of χ_{u⊕v} is 2ĝ(u)ĝ(v) = 0. Hence at most one ĝ(u) ≠ 0, and g = ±χ_u. ∎

## 4. Phase obstructions for 2×2 blocks (used as clauses)

In a 2×2 component with rows r, r′ and columns c, c′, unitarity is equivalent to:
- the moduli conditions; and
- φ_rc − φ_rc′ − φ_r′c + φ_r′c′ ≡ π (mod 2π) (Pandya, Lemma 1, LF234–275).
Swapping r with r′, or c with c′, negates the left side, which leaves the congruence unchanged.

**TBL (three-block lemma).** Let a, h ∈ [6]^4 differ in all four coordinates. Put
- D12 = {(a1,a2,h3,h4), (h1,h2,a3,a4)},
- D13 = {(a1,h2,a3,h4), (h1,a2,h3,a4)},
- D14 = {(a1,h2,h3,a4), (h1,a2,a3,h4)}.
The eight points {a, h} ∪ D12 ∪ D13 ∪ D14 form one of the two "even codes" of the subcube Π{a_i, h_i}. No AME state
can have three of the four antipodal pairs {a,h}, D12, D13, D14 inside 2×2 components that are formed as follows.
Take {a,h} ∪ D12 ∪ D13, with the blocks
- β1 = {a, (a1,a2,h3,h4), (h1,h2,a3,a4), h} in 12|34,
- β2 = {a, (a1,h2,a3,h4), (h1,a2,h3,a4), h} in 13|24,
- β3 = D12 ∪ D13 in 14|23.
Then β1 − β2 + β3 = 0 on the phases, while the right-hand sides add to 3π ≢ 0. The other three choices of three
pairs work the same way: the three blocks are the rectangles that the six points span in the three reshapings.
In the e = 0 model, the presence of the six points as N-elements forces exactly these blocks (exact-two lines and
Lemma 5). So the clause is ¬n over the six points.

**TWIN (twin triangle).** Fix a twin coordinate i (others j < k < l) and values d ≠ d′. For α ≠ α′, β ≠ β′,
γ ≠ γ′, consider the three twin pairs over p = (α, β, γ), q = (α′, β′, γ), r = (α′, β, γ′) in coordinates (j, k, l),
with x_i ∈ {d, d′}.
- In the e = 0 model, the six points force three 2×2 blocks: {p, q} in the reshaping pairing i with l, {p, r} in the
  one pairing i with k, and {q, r} in the one pairing i with j.
- Each block gives D_u − D_v ≡ π, where D_u = φ_(u,d) − φ_(u,d′).
- Summing around the triangle gives 0 ≡ 3π. Contradiction.

Both families were checked against Pandya's pattern: the e = 0 CNF with that pattern fixed is satisfiable (kissat,
10:47:57).

## 5. A connected 4×4 unitary component has at least 11 entries

Suppose it had 10. Rows have at least two entries, so the row-degree sequence is (2,2,3,3) or (2,2,2,4).
- **(2,2,2,4).** By Lemma 5, two distinct 2-subsets of the four columns must be disjoint. So the three two-entry rows
  use supports from a complementary pair {A, A^c}.
  - Using only A leaves the columns of A^c with only the full row, which forces a single-entry column, i.e. a
    classical officer (Lemma 2(b)). Contradiction.
  - Using A twice and A^c once: a column of A has rows {full row, r1, r3} and a column of A^c has rows
    {full row, r2}. They meet only in the full row, contradicting Lemma 5 for columns.
- **(2,2,3,3).** A two-entry row meets each three-entry row in at least one column, hence (Lemma 5) in at least two.
  So both two-entry rows equal r3 ∩ r4, a 2-set A. Then r3 = A ∪ {c3} and r4 = A ∪ {c4}.
  - If c3 = c4, the fourth column is empty.
  - Otherwise column c3 has the single entry in row r3, which is therefore classical (Lemma 2), contradicting
    |r3| = 3.
So such a component has at least 11 entries (e_K ≥ 3).

## 6. Symmetry reductions used by the SAT models

- **(SB1)** If t ≥ 1, apply local relabelings sending some classical officer to 0000.
- **(SB2, parameter τ)** Let τ* = max_{i,a} t_{i,a}.
  - Permute coordinates and relabel coordinate 1 so that t_{1,0} = τ*.
  - The τ* classical officers with x1 = 0 have pairwise distinct x2, x3 and x4 (Lemma 3). Relabel coordinates 2, 3
    and 4 so that they become (0, m, m, m), m < τ*.
  - All slice counts are then ≤ τ*.
  - Since t ≥ 13, τ* ≥ ⌈t/6⌉ ≥ 3. Also τ* ≤ 6 and τ* ≠ 5 (Lemma 9(a)). So the three instances τ ∈ {3, 4, 6} cover
    every AME state with t ≥ 13.
  - All maps used are elements of G, which preserves AME, s, t and every model constraint.
