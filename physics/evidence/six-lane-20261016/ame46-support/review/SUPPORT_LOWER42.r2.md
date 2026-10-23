# FROZEN r2 — partial result: every AME(4,6) state has at least 42 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`, `evidence/SHA256SUMS.txt`). r2 supersedes r1 (`review/SUPPORT_LOWER42.r1.md`,
SHA-256 54880341b045b18fac6b60394c9ad12ae778de40945f2454fa04142c079bb2ad), which is kept unchanged. r2 is r1 plus
exactly the changes listed in §8.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written. r2 itself has not been reviewed.
- Reviews of r1 (parent-held, under `institute/runs/six-lane-2026-10-16/review/`):
  - Codex review, `ame46-lower42-codex-review-v1.note.md`: ACCEPT-WITH-FIXES, with no fatal or major finding. Its two
    minors are the false one-class symmetry sentence in §5 and the missing word "orthonormal". Both are fixed (§8).
  - The parent's independent checker passed, and the parent's replay of the pinned verifier was byte-identical.
  - Claude review, `ame46-lower42-claude-review-v1.note.md`: ACCEPT-WITH-FIXES, with no fatal finding and one major,
    M1: the same false symmetry sentence, together with the unproved invariance claim. Its minors m1–m5, verifier
    notes v1–v4 and editorial items e1–e3 are applied as listed in §8.
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The contract target is the minimum support:
  59 versus 60. This file proves only the lower bound 42.
- Pandya (pinned `sources/arxiv-2610.16673v1.layout.txt`, SHA-256 3a7d4fef…bae7, LF498–520) states 38 ≤ s_min ≤ 60
  and calls the gap open.
- One classical theorem is cited, not proved: there is no pair of orthogonal Latin squares of order six (G. Tarry, Le
  problème des 36 officiers, C. R. Assoc. Franç. Av. Sci. 1 (1900) 122 and 2 (1901) 170–203; short proof: D. R.
  Stinson, J. Combin. Theory Ser. A 36 (1984) 373–376). Neither reference is pinned in the lane. The pinned citation
  is Pandya LF42–46, refs [7–9]. The theorem is used only in the case t = 36.
- No novelty or priority claim is made. The field is crowded, and a search miss is not novelty.
- The written proofs (§§1–5) are separated from the executable finite facts (§6). All arithmetic is exact. Since r2,
  the proof no longer depends on the machine checks: two written representatives and a written symmetry reduction
  cover all ten sets of §4, and F1–F4 are reproducibility cross-checks.

## Theorem

Let |ψ⟩ ∈ (C^6)^{⊗4} be an AME(4,6) state, i.e. every two-party reduced density matrix equals I/36. For every
product orthonormal basis {|e^{(1)}_{x1}⟩ ⊗ |e^{(2)}_{x2}⟩ ⊗ |e^{(3)}_{x3}⟩ ⊗ |e^{(4)}_{x4}⟩}, at least 42 of the 1296
coefficients ⟨e_x|ψ⟩ are non-zero.

## 0. Definitions and the reduction to the computational basis

- [6] = {0, 1, …, 5}. A state is ψ = Σ_{x∈[6]^4} ψ_x |x⟩ with x = (x1, x2, x3, x4).
- The **support** is S = {x : ψ_x ≠ 0}, and s = |S|.
- **Reshapings.** For the three pairings π = (ab|cd) ∈ {12|34, 13|24, 14|23}, U_π is the 36×36 matrix with rows
  indexed by (x_a, x_b), columns by (x_c, x_d), and entries U_π[(x_a,x_b),(x_c,x_d)] = 6ψ_x.
- **AME ⇔ unitary reshapings.** For a pure state, ρ_ab = Tr_cd |ψ⟩⟨ψ| has entries
  (ρ_ab)_{(x_a x_b),(y_a y_b)} = Σ_{x_c,x_d} ψ_{x_a x_b x_c x_d} conj(ψ_{y_a y_b x_c x_d}), so ρ_ab = U_π U_π†/36.
  Similarly ρ_cd = (U_π† U_π)^T/36.
  - Hence all six two-party marginals equal I/36 iff U_π U_π† = U_π† U_π = I for the three pairings, i.e. iff all
    three U_π are unitary (also Pandya, proof of Lemma 1, LF248–253).
- **Product orthonormal bases.** Let V_k be the unitary that maps the orthonormal basis vector |e^{(k)}_x⟩ to |x⟩.
  Then ⟨e_x|ψ⟩ is the x-coefficient of (V_1 ⊗ … ⊗ V_4)|ψ⟩,
  which is again AME, because local unitaries conjugate each marginal by a unitary. So it suffices to prove s ≥ 42 for
  every AME state in the computational basis.
- **Lines.** For a pair P = {i, j} of coordinates and z ∈ [6]², the P-line (P, z) is {x : (x_i, x_j) = z}. Each row
  and each column of each U_π is exactly one P-line, and each P-line is a row or column of exactly one U_π.
- **Classical officers.** T = {x ∈ S : |ψ_x| = 1/6}, with t = |T|. The non-classical support is N = S ∖ T.
- **Excess.** e := s − (72 − t).
- **Components.** For a unitary V, B(V) is the bipartite graph on the rows and columns of V, with an edge for each
  non-zero entry. A component K of a reshaping is a connected component of B(U_π). k_K is its number of rows, |K|
  its number of non-zero entries, and, when k_K ≥ 2, e_K := |K| − 2k_K.
- **Slices and deficits.** For a coordinate i and a value a:
  - t_{i,a} = |{y ∈ T : y_i = a}| and d_{i,a} = 6 − t_{i,a};
  - for j ≠ i, D_j^{(i,a)} = [6] ∖ {y_j : y ∈ T, y_i = a};
  - V_i = {a : d_{i,a} > 0};
  - h = 36 − t.

## 1. Lemmas (written proofs)

**Lemma 1 (norms).** For every P-line L, Σ_{x∈L} 36|ψ_x|² = 1.
*Proof.* Every row and column of a unitary matrix is a unit vector, and L is a row or column of some U_π. ∎

**Lemma 2 (classical officers).**
- (a) If x ∈ T, then no y ∈ S ∖ {x} agrees with x in two or more coordinates.
- (b) If a P-line meets S in a single element x, then x ∈ T.
*Proof.* (a) If y agrees with x on a pair P, then x and y lie in one P-line. By Lemma 1, 36|ψ_x|² + 36|ψ_y|² ≤ 1,
and 36|ψ_x|² = 1, so ψ_y = 0. (b) Lemma 1 for that line gives 36|ψ_x|² = 1. ∎

**Lemma 3 (code).** Two distinct classical officers agree in at most one coordinate. In particular they lie in
distinct lines, and t ≤ 36.
*Proof.* Lemma 2(a). ∎

**Lemma 4 (count).** s ≥ 72 − t, i.e. e ≥ 0. Every line containing no classical officer contains at least two
elements of S, all of them in N.
*Proof.* Fix U_12|34; each x ∈ S lies in exactly one of its rows.
- Each classical officer's row contains nothing else (Lemma 2(a)), and distinct classical officers lie in distinct
  rows (Lemma 3). This accounts for t rows.
- Any other row is non-empty (Lemma 1), has no single element (Lemma 2(b)), and contains no classical officer. So it
  contains at least two elements, all in N.
- Hence s ≥ t + 2(36 − t). The same argument applies to any line. ∎

**Lemma 5 (overlap).** If V is unitary and r ≠ r′ are rows, then the column supports of r and r′ do not meet in
exactly one column. The same holds for columns.
*Proof.* Otherwise the inner product of r and r′ would be a single non-zero product. ∎

**Lemma 6 (components are unitary blocks).** Let K be a component of a unitary V. Then |rows(K)| = |cols(K)|,
V restricted to rows(K) × cols(K) is unitary, and every other entry in these rows and columns is 0.
*Proof.*
- The rows of K are orthonormal and supported in cols(K), so |rows(K)| ≤ |cols(K)|.
- Symmetrically, |cols(K)| ≤ |rows(K)|.
- So the restriction is square with orthonormal rows, hence unitary. ∎

**Lemma 7 (component sizes).** In each U_π:
- the components with one row are exactly the entries of classical officers;
- every other component K has k_K ≥ 2, every one of its rows has at least two entries, and e_K ≥ 0.
Moreover:
- (a) e_K = 0 iff k_K = 2; such a component is a 2×2 block with four non-zero entries;
- (b) e_K ≠ 1;
- (c) e = Σ_K e_K over the components with k_K ≥ 2.
*Proof.*
- A one-row component is an entry alone in its row (by Lemma 6 it also has a single column), hence classical
  (Lemma 2(b)).
- A classical officer is alone in its row and column (Lemma 2(a)), so it is a one-row component.
- In any other component, a row with a single entry would be a classical officer and form its own component. So rows
  have at least two entries, and |K| ≥ 2k_K.
- (a) Suppose all rows of K have exactly two entries, and let r have support {c, c′}. A row r′ meeting {c, c′} meets
  it in at least two columns (Lemma 5), so supp(r′) = {c, c′}. No row of K reaches a third column. So |cols(K)| = 2,
  hence k_K = 2 by Lemma 6, and the two rows have the same two columns. Conversely, k_K = 2 with at least two
  entries per row gives |K| = 4.
- (b) Suppose e_K = 1. Then one row r0 has three entries, with support C0, and all other rows have two.
  - A two-entry row meeting C0 lies in C0 (Lemma 5).
  - Let r be a two-entry row disjoint from C0. Every row meeting supp(r) has support exactly supp(r): two-entry rows by
    the argument of (a), and r0 does not meet supp(r). So such rows are not in K.
  - Hence cols(K) = C0, and k_K = 3 by Lemma 6. The other two rows have 2-subsets of C0 as supports; these meet, so
    by Lemma 5 they are equal.
  - The remaining column of C0 then has a single entry, in r0. By Lemma 2(b) that entry is classical, so by
    Lemma 2(a) r0 has no other entry. Contradiction.
- (c) S is the disjoint union of the components. The one-row components contribute t entries; the others contribute
  Σ (2k_K + e_K) = 2(36 − t) + Σ e_K. ∎

**Lemma 8 (slices).** Let x ∈ N with x_i = a. Then x_j ∈ D_j^{(i,a)} for every j ≠ i.
For b ∈ D_j^{(i,a)}, the {i,j}-line through (x_i, x_j) = (a, b) contains no classical officer and at least two
elements of N. Also |D_j^{(i,a)}| = d_{i,a}. Consequently:
- (a) d_{i,a} ≠ 1;
- (b) Σ_a d_{i,a} = h;
- (c) every x ∈ N has x_i ∈ V_i for every i.
*Proof.*
- If x_j = y_j for some y ∈ T with y_i = a, then x and y agree on {i, j}, contradicting Lemma 2(a). So x_j ∈ D.
- The classical officers with y_i = a have pairwise distinct j-coordinates (Lemma 3). So |D_j^{(i,a)}| = 6 − t_{i,a},
  and the line (a, b), b ∈ D, contains no classical officer. By Lemma 4 it contains at least two elements of N.
- (a) If d_{i,a} = 1, every x ∈ N with x_i = a has each x_j (j ≠ i) equal to the single element of D_j^{(i,a)}. So
  there is at most one such x, while the line (a, b) for that b contains at least two.
- (b) Σ_a t_{i,a} = t.
- (c) If d_{i,b} = 0, then D_j^{(i,b)} = ∅, so no x ∈ N has x_i = b. ∎

**Lemma 9 (e = 0).** If e = 0, every line containing no classical officer contains exactly two elements of S.
*Proof.* By Lemma 7(a) and (c), every component with k_K ≥ 2 is a 2×2 block with four entries. A line without a
classical officer is a row or column of such a block. ∎

**Lemma 10 (block congruence).** Let K be a 2×2 component of U_π, with rows r ≠ r′, columns c ≠ c′, four non-zero
entries, and φ_{rc} := arg U_π[r, c]. Then
  φ_{rc} − φ_{rc′} − φ_{r′c} + φ_{r′c′} ≡ π (mod 2π).
*Proof.* By Lemma 6, rows r and r′ are orthogonal and supported on {c, c′}:
U[r,c] conj(U[r′,c]) + U[r,c′] conj(U[r′,c′]) = 0. Both terms are non-zero, so their arguments differ by π:
(φ_{rc} − φ_{r′c}) − (φ_{rc′} − φ_{r′c′}) ≡ π. ∎
Swapping r with r′, or c with c′, negates the left side, and the congruence is unchanged because −π ≡ π.
Since U_π[r, c] = 6ψ_x for the point x in row r and column c, φ_rc = arg ψ_x =: φ_x does not depend on π. So the
congruences of different reshapings are linear forms in the same unknowns φ_x, x ∈ N.

**Lemma 11 (symmetries).** Let g act on points by (g·x)_{σ(i)} = β_i(x_i), where σ is a permutation of the four
parties and β_1, …, β_4 are bijections of [6]. Let N be a set of points.
- (a) g maps each P-line to a σ(P)-line. The pairing {P, P^c} goes to the pairing {σ(P), σ(P^c)}, possibly with
  rows and columns interchanged.
- (b) g maps the connected components of the support graph of N in reshaping π onto those of g(N) in the image
  reshaping.
- (c) Let a 2×2 component have rows r, r′ and columns c, c′. Transporting its Lemma 10 form by x ↦ g·x gives plus or
  minus the Lemma 10 form of the image component.
Consequently, three components (one per reshaping) whose signed forms sum to the zero form are mapped to three
components of g(N) with the same property, and the signed right sides still sum to an odd multiple of π.
*Proof.*
- (a) The P-line through x is mapped to the σ(P)-line through g·x. The two pairs of a pairing are mapped to the two
  pairs of one pairing.
- (b) Two points share a row or column iff their images do, by (a).
- (c) The four points rc, rc′, r′c, r′c′ go to the four points of the image component, and the checkerboard pattern
  (same row, same column, diagonal) is preserved. The Lemma 10 form gives sign +1 to the diagonal pair {rc, r′c′}
  and −1 to the other pair. Interchanging rows and columns keeps the two diagonals. Swapping the order of the rows or
  of the columns interchanges them, which negates the form. ∎

## 2. Proof of the Theorem

Suppose ψ is AME(4,6) with s ≤ 41. By Lemma 4, t ≥ 72 − s ≥ 31, and t ≤ 36 by Lemma 3.

- **t = 36.** The 36 classical officers lie in 36 distinct rows of U_12|34 (Lemma 3), so every row contains one. A
  row containing a classical officer contains nothing else (Lemma 2(a)), so S = T and N = ∅.
  - Every P-line is non-empty (Lemma 1) and contains at most one point of T (Lemma 3). So T is a set of 36 points of
    [6]^4 meeting every P-line exactly once.
  - Setting L1(x1, x2) = x3 and L2(x1, x2) = x4 for (x1, x2, x3, x4) ∈ T defines two Latin squares of order six:
    each line through (x1, x3), (x2, x3), (x1, x4) or (x2, x4) is met once. They are orthogonal, because each line
    through (x3, x4) is met once.
  - No such pair exists (Tarry's theorem; cited through Pandya LF42–46, refs [7–9]). **[cited]**
- **t = 35.** h = 1. By Lemma 8(b), Σ_a d_{1,a} = 1, so some d_{1,a} = 1, contradicting Lemma 8(a).
- **t ∈ {33, 34}.** h ∈ {2, 3}.
  - For each i the positive deficits d_{i,a} are at least 2 (Lemma 8(a)) and sum to h ≤ 3 (Lemma 8(b)), so V_i is a
    single value.
  - By Lemma 8(c), all elements of N agree in every coordinate, so |N| ≤ 1.
  - But h > 0 lines lack a classical officer, and each contains at least two elements of N (Lemma 4).
    Contradiction.
- **t = 31.** Then e = s − 41 ≤ 0, so e = 0. By Lemma 7(a) and (c), the 36 − 31 = 5 non-classical rows of U_12|34
  are partitioned into 2×2 components, and 5 is odd. Contradiction.
- **t = 32.** Then e = s − 40 ≤ 1. Lemma 7(b) and (c) exclude e = 1, so e = 0 and h = 4. §3 shows that N is, up to
  relabelling, one of ten explicit 8-point sets in a 2^4 subcube. §4 shows that for each of them the congruences of
  Lemma 10 are inconsistent. Contradiction.

Every case is impossible, so s ≥ 42. ∎

**Corollary (by-product).** The arguments for t ∈ {33, 34, 35} do not use s ≤ 41. So no AME(4,6) state has
t ∈ {33, 34, 35}, and with Tarry's theorem t ≤ 32 for every AME(4,6) state. Moreover, e = 0 forces t to be even
(Lemma 7(a), (c): 36 − t non-classical rows are paired into 2×2 components).

## 3. The case t = 32, e = 0: reduction to an OA(8, 4, 2, 2)

- **Step 1: |V_i| = 2 for every i.**
  - The positive deficits d_{i,a} are at least 2 (Lemma 8(a)) and sum to 4, so each coordinate has the profile {4} or
    {2, 2}.
  - Suppose coordinate i has the profile {4}, with V_i = {a}. Then N ⊆ {x_i = a} (Lemma 8(c)). For j ≠ i, the four
    lines (a, b), b ∈ D_j^{(i,a)}, each contain elements of N (Lemma 8), so x_j takes four distinct values on N.
  - By Lemma 8(c) these values lie in V_j, but |V_j| ≤ 2 under either profile. Contradiction.
  - So V_i = {a_i, b_i} for every i, and N ⊆ V_1 × V_2 × V_3 × V_4 (Lemma 8(c)).
- **Step 2: all 2-marginals are uniform.**
  - Fix a pair {i, j}. The lines of that pair which lack a classical officer number 36 − t = 4 (Lemma 3: the t
    classical officers lie in t distinct lines).
  - These lines are exactly the lines meeting N: lines lacking an officer meet N by Lemma 4, and a line containing an
    officer meets no element of N by Lemma 2(a).
  - Hence {(x_i, x_j) : x ∈ N} is a 4-element subset of V_i × V_j, so it equals V_i × V_j. By Lemma 9 each of these
    four lines contains exactly two elements of N.
- **Conclusion.** Identify V_i with {0, 1} by a_i ↦ 0 and b_i ↦ 1. Then N becomes an 8-point subset of {0,1}^4 whose
  six 2-dimensional marginals are uniform, i.e. an orthogonal array OA(8, 4, 2, 2).

**Classification (written proof).** An 8-point set N ⊆ {0,1}^4 with all six 2-marginals uniform equals
{x : Σ_{i∈U} x_i ≡ c (mod 2)} for some U with |U| ∈ {3, 4} and some c ∈ {0, 1}. There are ten such sets.
*Proof.*
- Let g = 2·1_N − 1, a ±1-valued function, and ĝ(u) = 2^{−4} Σ_x g(x)(−1)^{u·x}.
- |N| = 8 gives ĝ(0) = 0. Uniform 2-marginals imply uniform 1-marginals (four points per value). For |u| ∈ {1, 2}
  they give Σ_x 1_N(x)(−1)^{u·x} = 0, and Σ_x (−1)^{u·x} = 0, so ĝ(u) = 0.
- Hence g = Σ_{u∈F} ĝ(u)χ_u, with χ_u(x) = (−1)^{u·x} and F = {1110, 1101, 1011, 0111, 1111}.
- Since g² ≡ 1, the coefficient of χ_w in g² vanishes for every w ≠ 0. For distinct u, v ∈ F the sums u ⊕ v are
  pairwise distinct and non-zero: two weight-3 vectors give the six weight-2 vectors, and a weight-3 vector with 1111
  gives the four weight-1 vectors.
- So the coefficient of χ_{u⊕v} in g² is 2ĝ(u)ĝ(v) = 0 for all distinct u, v ∈ F. At most one ĝ(u) is non-zero, and
  Parseval (Σ ĝ(u)² = 1) gives g = ±χ_u. That is the stated form. ∎
Executable cross-check: fact F1 (§6) enumerates all C(16, 8) = 12870 subsets.

## 4. Phase obstruction for the ten sets (t = 32, e = 0)

Fix one of the ten sets, embedded in the subcube Π_i {a_i, b_i}.
- **Blocks.** By Lemma 9 and Lemma 7(a), the non-classical components of each U_π are 2×2 blocks with four entries.
  By Lemma 2(a), no line through a point of N contains a classical officer. So the components of B(U_π) that meet N
  are exactly the components of the support graph of N alone, and they are determined by N. For the two written
  representatives below they are listed explicitly.
- **Obstruction.** By Lemma 10, each block gives a congruence with right side π. It is enough to find three blocks,
  one in each reshaping, and signs ε ∈ {±1} whose signed left sides add to the zero linear form. Adding the three
  congruences then gives 0 ≡ (1 + ε2 + ε3)π (mod 2π), and 1 + ε2 + ε3 is odd. Contradiction.

**Written instance (even code, U = {1,2,3,4}, c = 0, in {4,5}^4).** Write a = 4444, b = 4455, c = 4545, d = 4554,
e = 5445, f = 5454, g = 5544, h = 5555.
- 12|34 has the blocks {a, b, g, h} and {c, d, e, f}. The block {a, b, g, h} has rows (4,4), (5,5) and columns (4,4),
  (5,5), so Lemma 10 gives φ_a − φ_b − φ_g + φ_h ≡ π.
- 13|24 has the block {a, c, f, h}, with rows (x1, x3) = (4,4), (5,5) and columns (x2, x4) = (4,4), (5,5):
  φ_a − φ_c − φ_f + φ_h ≡ π.
- 14|23 has the block {b, c, f, g}, with rows (x1, x4) = (4,5), (5,4) and columns (x2, x3) = (4,5), (5,4). Here b and
  g are diagonal: φ_b − φ_c − φ_f + φ_g ≡ π.
- (first) − (second) + (third) = 0 identically, while the right sides add to π − π + π = π ≢ 0.

**Written instance 2 (U = {1,2,3}, c = 0, in {4,5}^4).** Here N = {x : x1 + x2 + x3 ≡ 0} with 4 ↦ 0 and 5 ↦ 1.
Write a = 4444, b = 4445, c = 4554, d = 4555, e = 5454, f = 5455, g = 5544, h = 5545.
- 12|34 has the blocks {a, b, g, h} and {c, d, e, f}. The block {a, b, g, h} has rows (4,4), (5,5) and columns (4,4),
  (4,5): φ_a − φ_b − φ_g + φ_h ≡ π.
- 13|24 has the block {a, b, e, f}, with rows (x1, x3) = (4,4), (5,5) and columns (x2, x4) = (4,4), (4,5):
  φ_a − φ_b − φ_e + φ_f ≡ π.
- 14|23 has the block {e, f, g, h}, with rows (x1, x4) = (5,4), (5,5) and columns (x2, x3) = (4,5), (5,4). Here e and
  h are diagonal: φ_e − φ_f − φ_g + φ_h ≡ π.
- (first) − (second) − (third) = 0 identically, while the right sides add to π − π − π = −π ≢ 0 (mod 2π).
- In each reshaping, the remaining four points of N form the second block. They are not needed.

**Symmetry reduction (written).** The relabellings used are coordinate permutations and, in each coordinate, the swap
a_i ↔ b_i. By Lemma 11(c), an obstruction for one set gives an obstruction for its image.
- A coordinate permutation σ maps {Σ_{i∈U} x_i ≡ c} to {Σ_{i∈σ(U)} x_i ≡ c}. The swap in coordinate i maps it to the
  set with the same U and with c replaced by c + [i ∈ U].
- Hence the ten sets fall into exactly two classes: the two sets with |U| = 4, which are images of instance 1, and the
  eight sets with |U| = 3, which are images of instance 2. The size |U| is invariant (it is the Fourier support of
  §3), so there is no third class and the two classes are distinct.
- Any subcube Π{a_i, b_i} is mapped onto {4,5}^4 by a value relabelling (Lemma 11 with suitable β_i).

Cross-checks (not load-bearing):
- r1's facts F2–F4 (§6) recheck all ten sets and all 50625 subcubes.
- F4 is logically redundant. Components and Lemma 10 forms depend only on which coordinates of points agree, every
  coordinatewise injection preserves that, and a change of orientation only flips signs (Lemma 11).
- The r2 verifier (§6) re-derives the two written instances literally. It also checks the two orbits, and Lemma 11
  on all 384 × 10 group-element/set pairs.

**Remark (bridge to AME(4,2); not used).**
- In the case t = 32, e = 0, the non-classical rows and columns of U_12|34 are V_1 × V_2 and V_3 × V_4. By Lemma 6
  the 4×4 submatrix there is unitary, and likewise for the other two reshapings.
- Also Σ_{x∈N} 36|ψ_x|² = 4 (sum Lemma 1 over the four non-classical rows). So ω := 3·ψ|_{ΠV_i}, viewed as a
  four-qubit state, has reshapings 2ω = 6ψ|_{ΠV_i} that are unitary in all three pairings. That is an AME(4,2) state.
- AME(4,2) states do not exist (Higuchi–Sudbery, cited by Pandya LF46–47, ref. [10]), which would give an alternative
  proof of this case.
- The proof above does not use this citation. Its phase obstruction is the explicit mechanism.

## 5. What is cited and what is computed

- **Cited:** Tarry's theorem (case t = 36). It is pinned only through Pandya's text; primary references are given in
  the status block. The AME(4,2) theorem in the §4 remark is not used.
- **Written:** Lemmas 1–11, §2 with its corollary, §3 (including the Fourier classification), and in §4 the two
  written instances and the symmetry reduction. These cover all ten sets of §4.
- **Executable finite facts (§6):** reproducibility cross-checks only; the proof does not depend on them. They are
  the r1 verifier's F1–F4 and the r2 verifier's W, SYM and F1. r1's sentence claiming that the nine unwritten sets
  are images of the single weight-4 instance was false. The ten sets form two classes, and both now have written
  representatives.

## 6. Executable finite facts: replay record

- **Script:** `code/verify_lower42.py`, SHA-256 9106089aa5fa28edad039579c74e3fd2ea999a4226bbf2592827c72970af182b.
  Python standard library only, exact integers.
- **Command:** `cd code && /usr/bin/python3 -B verify_lower42.py` (Python 3.9.6). Exit status 0 iff all facts hold.
- **Run:** 11:49:48–11:50:18 PDT, 2026-10-17. Outputs:
  - `evidence/verify_lower42.json`, SHA-256 caee2f5e1c7a081869ad2b292912fd6d7b3bd120c3ca55eb0afee13744e11eaa;
  - `evidence/verify_lower42.stdout.txt`, SHA-256 e62cb4ee62867b45f7db03b043dbac10c9efefaf5ba32a40e058c16895f600cc.
- **Results:** all_required_true = true.
  - F1: exactly 10 of the 12870 8-subsets have uniform 2-marginals, and they are the ten parity sets.
  - F2: each set gives two 2×2 blocks in each reshaping.
  - F3: a verified signed three-block obstruction for each set; the coefficient vectors are listed in the JSON.
  - F4: all 50625 subcubes pass.
- No other input is needed. The pinned Pandya layout is needed only for the citations.
- Notes on the r1 verifier (Claude review). The r1 verifier is unchanged, and none of these notes affects its
  successful run:
  - v1: `verify_combination` repeats the summation on the same data, and its parity test is vacuous (1 + ε2 + ε3 is
    always odd).
  - v2: after a failure the per-set report would raise a TypeError. The exit status would still be 1.
  - v3: byte-identical replay is meaningful only under Python 3.9.6, since the JSON records the Python version.
  - v4: "no real or complex solution" should read "no assignment of phases".
- **r2 cross-check verifier:** `code/verify_lower42_r2.py`, SHA-256
  9be67daf0668eb4a20dcdf4ad366f8c9f1369275531a7e9a815bca64242b4125. It is a new file; the r1 verifier is unchanged.
  - Run 12:07:01–12:07:02 PDT under Python 3.9.6, all_required_true = true.
  - Outputs: `evidence/verify_lower42_r2.json` (54ed974b47a16cee23b6ce9acef258557db24ac8d9b6641b5b687acb8be275b8) and
    `evidence/verify_lower42_r2.stdout.txt` (7c2b479b1c6d8c09923b6443855c019da306f55488c2cdaf1ad8d2a96d5f9264).
  - W: both written instances are reproduced literally. The blocks are components, the forms are the Lemma 10
    forms, the signed sums are the zero form, and the right sides are odd.
  - SYM: the orbits have sizes 2 and 8, are disjoint, and together give the ten parity sets. Lemma 11 holds on all
    3840 cases.
  - F1 is repeated.
  - It uses independent code paths for components and form summation, it does not repeat F4, and it states that
    no assignment of phases exists.

## 7. Not claimed

- Nothing here bears on the contract target (59 versus 60) beyond the lower bound 42.
- No SAT result is used. In particular, the unverified t = 30 UNSAT and the t = 14 UNKNOWN runs recorded in the lane
  README are not part of this proof.
- No novelty or priority claim is made.

## 8. Changes from r1

Apart from the title, supersession and status lines, r2 differs from r1 only as follows. The sources are the Codex
review (`ame46-lower42-codex-review-v1.note.md`), the Claude review (`ame46-lower42-claude-review-v1.note.md`) and
the parent's notes.
1. Theorem and §0 (Codex minor, Claude m4): "product basis" is now "product orthonormal basis", and §0 calls V_k a
   unitary.
2. Claude M1(1): new Lemma 11 (symmetries), with proof.
3. Claude M1(2) and the parent's note: a second written representative in §4 (U = {1,2,3}, c = 0), with blocks and
   the combination B12 − B13 − B14 = 0 with right side −π. A written symmetry reduction, using Lemma 11, shows that the
   ten sets form exactly two classes, each the image of one written representative.
4. §5 (Codex minor, Claude M1, e3): r1's false one-class sentence is replaced. The dependence statements are
   updated, and F1–F4 are now cross-checks.
5. Claude m1: Lemma 7 cites Lemma 6 for one-row components and for k_K = 2, and says "same two columns".
6. Claude m2: after Lemma 10, φ_rc = arg ψ_x does not depend on the reshaping.
7. Claude m3: §4 explains why the blocks are determined by N.
8. Claude m5: F4 is described as logically redundant.
9. Claude v1–v4: notes on the r1 verifier in §6, and a new cross-check verifier `code/verify_lower42_r2.py`. The r1
   verifier is unchanged.
10. Claude e1: the four-qubit state in the §4 remark is renamed ω. Claude e2: primary references for Tarry's theorem.
11. Claude by-product: a corollary after §2 (t ∈ {33, 34, 35} is impossible for every AME(4,6) state; with Tarry,
    t ≤ 32; e = 0 forces even t).
No mathematical conclusion changed.
