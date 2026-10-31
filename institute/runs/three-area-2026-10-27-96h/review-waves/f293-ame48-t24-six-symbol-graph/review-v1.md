# Review f293-ame48-t24-six-symbol-graph — review-v1

- Reviewer: ReviewF293AME (disjoint same-harness written review; WRITTEN_ONLY).
- Packet: `literal-packet-v1.md`, SHA-256 `97a535094afd3f99929bdfd6d34d02a6adfd3cfdbbc9fdfec10bf6c42fceb1df`, 13746 bytes, 93 LF; read fully raw in five windows (1–20, 21–40, 41–60, 61–80, 81–93) including the ending; no elisions found; hash re-verified against freeze receipt `7c6cac89d3bc881761e2a947900e825826bdfbf7f01c47370be9a3c5b95a7e3a`.
- Source S1: `frontier-20261029-n48-t24-six-symbol-graph-obstruction-v1.md`, SHA-256 `af71caae6989f749b1e3ddf526194e058a55d00e8bc2aaef2aac866fe0120fd4`, COMPLETE_BODY, lines 1–91 (allowed lines equal). Line references below are S1 line numbers.
- Clocks: pre-body ACK 2026-10-30T03:49:40-0700 PDT; substantive checkpoint 2026-10-30T04:02:52-0700 PDT; review completion 2026-10-30T04:0X:00-0700 PDT (final value in reviewer-f293-closeout-v1.json).
- Controls were read STATUS ONLY; no mathematical input taken from them.

## Verdict

**Theorem at S1|7: SUPPORTED** at its stated conditional scope (N=48, t=24, fixed product basis, **assumed** no residual Hamming-distance-one pair). **Corollary at S1|89: SUPPORTED.** No FATAL, no MAJOR. Five MINOR presentational findings (m1–m5); none affects correctness. The reconstruction below is complete for every special case; no exact gap remains.

## Independent written reconstruction

### R1. Pair systems (S1|15) — SUPPORTED

For any 2|2 cut, the 36×36 flattening U=6ψ is unitary (two-party marginals of a normalized AME(4,6) are I/36). The 24 modulus-one entries sit in mutually distinct rows and columns (two in one row would force norm ≥ √2), and any singleton row/column must carry a modulus-one entry (unit norm); hence exactly 24 singleton rows and 24 singleton columns, one per P word. Deleting them leaves a 12×12 unitary U′ (the surviving rows have support inside the surviving columns, orthonormality restricts). E coefficients satisfy |c| ≤ 1/6 with |c| ≠ 1/6, so |c| < 1/6 strictly; hence U′ has no singleton row or column (a lone entry of a unitary row would have modulus 1). 24 nonzeros over 12 rows/columns of minimum degree 2 forces degree exactly 2 everywhere. Therefore each of the six pair-coordinate systems has exactly 12 E-carried pair values, each with exactly two E extensions, 24 P-carried singleton values, and no pair value shared by a P word and an E word. All sub-claims reconstruct.

### R2. Partner counts d_i(a) (S1|17) — SUPPORTED

Of the six pair values (a,x) in system (i,j), exactly p_i(a) are P-carried (distinct P words occupy distinct pair values) and the rest, 6−p_i(a), are E-carried; the E words with party-i symbol a have exactly one distinct j-symbol per E-carried value (a pair value fixes both coordinates), so the partner count is d_i(a) = 6−p_i(a), independent of j. If d_i(a)=1, all E words over the single E-carried value (a,x) would coincide at every party, contradicting that the value carries exactly two distinct E words (R1). Hence d_i(a) ≥ 2, and summing E-carried values over the pair system gives Σ_{a∈E_i} d_i(a) = 12. Reconstructs fully.

### R3. Fibers and rectangles under |E_A|=6 (S1|19) — SUPPORTED

Six symbols with degrees ≥ 2 summing to 12 force d_A(a)=2 each; each fiber E_a has 4 words (two E-carried (A,j) values × two extensions) using two values twice at each of B,C,D. No-distance-one makes each two-party projection of a fiber injective (agreement on A plus two of B,C,D would be distance 1), so 4 words fill the 2×2 rectangle over every pair from {B,C,D}; in particular the two words over a fixed (a,b) split the two C and two D values. Reconstructs.

### R4. Incidence graphs and (I) (S1|23–27) — SUPPORTED

G_j (j∈{B,C,D}): vertices = E symbols at j, one loopless edge per A fiber joining its two j-symbols; U_j is the 6×r_j edge–vertex incidence matrix; rows have weight 2 (R3), columns have weight d_j(b) ≥ 2 (R2). For j≠k, (U_j^T U_k)_{bc} counts A fibers whose rectangles contain the cell (b,c); by the rectangle bijection each containing fiber supplies exactly one word there, so this equals the number of E words at pair value (b,c), which is 0 or 2 by R1. This is (I); note it is exactly here that the no-h1 hypothesis enters the graph layer. Reducing mod 2 gives U_j^T U_k ≡ 0, i.e. pairwise orthogonality of the column spaces W_j ⊂ F₂⁶ (S1|29). Reconstructs.

### R5. Obstruction (O) (S1|33) — SUPPORTED

Let fibers a ≠ a′ share exactly one vertex in each of G_j, G_k, say shared j-symbol b₁ and k-symbol c₁; fibers a, a′ have j-symbols {b₁,b₂}, {b₁,b₂′} and k-symbols {c₁,c₂}, {c₁,c₂′} with b₂ ≠ b₂′, c₂ ≠ c₂′. Consider the (A,l)|(j,k) flattening, l the fourth party. The row of a word w of fiber a over (b₁,c₁) is the E-carried pair value (a, l_w): its two E words have j-symbols {b₁,b₂} and k-symbols {c₁,c₂} (fibers are bijective on (j,l) and (k,l) rectangles) and distinct (j,k) values, so the row is supported exactly on columns (b₁,c₁) and (b₂,c₂). Symmetrically the row of fiber a′'s word over (b₁,c₁) is supported on (b₁,c₁) and (b₂′,c₂′). The two unitary rows are distinct (different A symbols) and share exactly the one column (b₁,c₁) (b₂ ≠ b₁, b₂′), so their inner product is 36·c_w·conj(c_w′) ≠ 0, contradicting unitary orthogonality. Fully reconstructed.

### R6. Obstruction (Q) (S1|35) — SUPPORTED

If fibers a ≠ a′ have identical endpoint pairs {b₁,b₂}, {c₁,c₂}, {d₁,d₂} at B,C,D: within each of the three partner pair systems every cell of the common 2×2 rectangle receives one word from each fiber (two E words), saturating all cells since E-carried values carry at most two E words; all pair values involving A over these local alphabets are saturated inside the corresponding fiber. Any support word lying in the box {a,a′}×{b₁,b₂}×{c₁,c2}×{d₁,d₂} sits over saturated pair values in every pair system, hence is one of the 8 fiber words; conversely the 8 words occupy exactly these values. So every 2|2 flattening contains an isolated 4×4 block (saturated rows and columns) which, restricted, is unitary; the normalized 8-term restriction φ has Σ|c|² = 1/4 and two-party marginals I₄/4 in all six cuts, i.e. φ is AME(4,2). Reconstructs fully.

### R7. AME(4,2) nonexistence (S1|37) — SUPPORTED (finding m1: compression)

Full reconstruction of the stated elementary argument. Write ρ = |φ⟩⟨φ| = (1/16)Σ_P β_P P with β_P = Tr(ρP) real over four-qubit Paulis, A_k = Σ_{wt(P)=k} β_P²; A₀ = β_I² = 1. Purity: Σ_k A_k = 16. Maximally mixed one- and two-party marginals give A₁ = A₂ = 0. For each triple, the three-party marginal has purity 1/2 (Schmidt coefficients of the complementary I/2 marginal), and its Pauli expansion gives 1 + (weight-3 sum over that triple) = 4, so each triple contributes 3; the four weight-3 classes are disjoint, A₃ = 12, and A₄ = 16−1−12 = 3. Spin-flip ρ̃ = Y^{⊗4}ρ*Y^{⊗4} is positive semidefinite; single-qubit conjugation I↦I, X,Y,Z ↦ −X,−Y,−Z (Y* = −Y) flips each Pauli's coefficient by (−1)^{wt(P)}, so Tr(ρρ̃) = (A₀−A₁+A₂−A₃+A₄)/16 = (1−12+3)/16 = −1/2 < 0, contradicting positivity of ρ,ρ̃ ⪰ 0. Every numeric identity in the packet line reconstructs; the alternating-sign mechanism and "positive = positive semidefinite" are compressed in the text (m1), not erroneous.

### R8. Rank lemma and the all-ranks-≥3 case (S1|41–47) — SUPPORTED

For loopless G_j with minimum degree ≥ 2 (hence no isolated vertices), ker(U_j^T) = vertex labelings constant on connected components, so dim W_j = r_j − c_j with every component ≥ 2 vertices. If all three ranks ≥ 3, pairwise orthogonality (W_k ⊆ W_j^⊥, dim W_j^⊥ = 6 − dim W_j) forces all ranks = 3; then W_C = W_B^⊥ = W_D and W_C is self-orthogonal of dimension 3 in F₂⁶, hence self-dual, and all three spaces equal one self-dual W. Classification (S1|45), reconstructed in full: all words even weight (w·w = 0), so 𝟙 ∈ W = W^⊥; a nonword-of-weight-6 nonzero w has weight 2 or 4, and w+𝟙 converts 4 to 2; permuting, W ∋ e₁+e₂ and every vector of W has equal first two coordinates; the projection to the last four coordinates is a self-dual dimension-2 subspace (v·u = v′·u′), whose two non-𝟙 nonzero words have weight 2; clearing the first two coordinates by e₁+e₂ as needed and summing with the all-ones lift exhibits the third pair; the three weight-2 words are pairwise disjoint (the two four-coordinate pairs are complementary) and linearly independent, so W is exactly the span of three disjoint pair indicators. Then every column of every U_j is constant on each pair, the two edge labels of a pair have identical endpoints in all three graphs, and (Q) forbids this. All steps reconstruct (finding m2: the closing sentence "the sum with all-ones gives the remaining disjoint weight-2 pair" is compressed but valid as reconstructed).

### R9. r=2 case (S1|51–53) — SUPPORTED

If r_j = 2, all six edges join the two vertices; the 12 E-carried pair values of any partner system satisfy 12 ≤ 2·r_k, so r_k = r_l = 6. Total degree 12 over 6 vertices of degree ≥ 2 forces all degrees 2; at most three components and rank = r − c ≥ 3; pairwise orthogonality of the two partner spaces pins both ranks at exactly 3, hence c = 3, each component two vertices joined by two parallel edges. The column space is then the span of the three component edge-pair indicators — self-dual; the second partner's space lies in it with equal dimension, hence equals it, so edges of a pair have identical endpoints there; endpoints in G_j are trivially identical, and within each partner the two parallel edges of a component share endpoints. Any pair of edge labels in one component has identical endpoints in all three graphs: (Q) contradiction. Reconstructs.

### R10. r=3 case (S1|57–73) — SUPPORTED

By (I) against G_j's columns, every column of U_k or U_l induces degrees 0 or 2 on the 3 vertices of G_j; nonempty such edge sets are exactly 2-cycles (two parallel edges) or triangles (one edge per vertex pair), so all column sizes are 2 or 3 and 3r ≥ 12 gives r_k, r_l ≥ 4.

- **6.1 (r_k = 4), S1|61–65 — SUPPORTED.** Four column sizes ≤ 3 summing to 12 are all triangles; each edge label lies in exactly two U_k columns. A 2-cycle column of U_l and any triangle of U_k containing one of its two parallel edges meet in exactly one label (a triangle takes one edge per parallel class), violating (I); such a triangle exists because each label of the 2-cycle lies in two all-triangle U_k columns. So U_l is all triangles and r_l = 4. Each of G_j's three parallel classes receives 4 occurrences (one per U_k triangle) and each label occurs twice, so each class has exactly two labels; label the two edges of each class 0/1 so triangles are binary triples. Against any fixed U_l triangle, (I) allows 0 or 2 agreements, i.e. odd Hamming distance, so the four U_k triples share one parity; each bit value occurs twice per coordinate (each label in two columns). The balanced four-multiset of one parity is unique — the complete parity class, each triple once (reconstructed by solving the three balance equations: n₀ = 1 forces all multiplicities 1). Two edges from different classes share exactly one vertex of G_j; the complete class realizes each two-bit choice exactly once, so the corresponding two rows of U_k lie together in exactly one column, i.e. the two edges share exactly one vertex of G_k. (O) contradiction. Reconstructs; the balanced-multiset uniqueness check is correct.
- **6.2 (r_k, r_l ≥ 5), S1|69–73 — SUPPORTED.** Sizes 2/3 summing to 12 give: r=6 → no triangles; r=5 → exactly two triangle columns. If U_l has a triangle T: a U_k 2-cycle containing a label of T meets T in exactly one label (forbidden); each of T's three labels occurs in exactly two U_k columns, all therefore triangle columns — impossible at r_k=6 (none exist), and at r_k=5 the two triangle columns must both equal T (6 occurrences fill both 3-slot columns), giving column intersection 3 against (I). Symmetrically neither partner has a triangle column, so both have r=6 with all columns 2-cycles. Two 2-element column supports of U_k are equal or disjoint by (I); if two distinct supports met in one label, a U_l column through that label (exists, two per label) would have to equal both — impossible; so the distinct supports are three disjoint pairs each repeated twice (each label in exactly two columns), and the same argument forces the U_l supports to be the same three pairs. A pair is a 2-cycle of G_j, and its two labels occur together in exactly the two columns of that support in each partner, so they have identical endpoints in G_j, G_k, G_l: (Q) contradiction. Reconstructs (finding m5: the phrase "pair capacity" at S1|57 is nonstandard for 3r ≥ 12, clear in context).

### R11. Rank-2 / four-vertex case (S1|77–83) — SUPPORTED

After R9 and R10 all graphs have r ≥ 4. If some rank is < 3: rank = r − c with c ≤ r/2 (components ≥ 2 vertices) gives r ≤ 4, hence r = 4, c = 2, rank = 2; in particular ranks 0 and 1 are excluded by the same component bound (c = r or r−1 exceeds r/2). Each component is two vertices joined by parallel edges (degrees ≥ 2), with edge sets P, Q partitioning the six labels, |P|,|Q| ≥ 2. G_j's columns are 𝟙_P, 𝟙_Q (duplicated), so by (I) every column of U_k, U_l meets each of P, Q in 0 or 2 labels: P and Q each form a 2-regular subgraph of both other graphs (S1|79).

- |P| = 2 (or |Q| = 2), S1|81: a 2-edge loopless 2-regular graph is two parallel edges, so the two labels have identical endpoints in both other graphs and in G_j (same component): (Q). SUPPORTED.
- |P| = |Q| = 3, S1|83: in each other graph P and Q form triangles. Their vertex sets cannot coincide, else every further vertex (r ≥ 4 guarantees one exists) would have degree 0 < 2; so some P-triangle vertex v of G_k is not a Q-triangle vertex, and its column is a 2-subset S ⊂ P. The three P-triangle vertices of G_l carry three distinct 2-subsets of P (triangle incidences); intersecting their full columns with S sees only P labels, two 2-subsets of a 3-set meet in 1 or 2, and (I) forbids 0 and 1, forcing each of the three distinct subsets to equal S — contradiction. SUPPORTED, including the vertex-set distinctness step.

Finding m3: the sentence "If a rank is below 3, it must be 2" (S1|77) is justified only implicitly by the component bound c ≤ r/2 from S1|41; the exclusion of rank ≤ 1 is immediate from it but unstated.

### R12. Exhaustion and conclusion (S1|85) — SUPPORTED

Case tree: either all three ranks ≥ 3 (→ R8 contradiction) or some rank ≤ 2; a rank-deficient graph has r ∈ {2,3} (→ R9, R10 contradictions) or r ≥ 4 (→ R11, rank ≤ 2 forces rank = 2, r = 4, contradiction). No residual party has six E symbols. The tree is exhaustive; no case omitted.

### R13. Alphabet corollary (S1|89) — SUPPORTED (finding m4: size-1 exclusion implicit)

12 ≤ |E_i|·|E_j| ≤ 6|E_i| gives |E_i| ≥ 2 for every party. If |E_i| = 2, the 12 E-carried pair values force |E_j| = 6 for every partner, contradicting the theorem just proved; |E_i| = 6 is the theorem's conclusion. Hence |E_i| ∈ {3,4,5}. The packet states the size-2 elimination explicitly; the size-1 elimination is the same one-line count left implicit (m4). The boundary sentence (no actual support-48 tensor, no N ≥ 49 claim) is accurate.

## Import and scope audit

- **No f127 import**: the no-distance-one property is used only as the explicit hypothesis of S1|7, entering at S1|19 (fiber injectivity) and through it at (I)/(O)/(Q); S1|9 correctly disclaims the f127 lemma (different N,t scope) and the separate unreviewed candidate `6bbe85a8…` is referenced but not used. VERIFIED.
- **No OLS(6) claim or use** anywhere in S1|1–91. VERIFIED.
- **No ≥ 49 or all-support claim**: S1|11 and S1|89 explicitly disclaim; nothing in the proof asserts more than the conditional theorem. VERIFIED.
- **AME(4,2) nonexistence is proved internally** (S1|37), not imported. VERIFIED.
- No held payloads, prior review bodies, sibling material or author code were opened; controls were status-only.

## Findings

- FATAL: none.
- MAJOR: none.
- MINOR:
  - m1 (S1|37): the alternating-sign mechanism of the spin-flip overlap (each non-identity Pauli factor flips sign under Y·(·)*·Y, giving A₀−A₁+A₂−A₃+A₄) and "positive" meaning positive semidefinite are compressed; the stated numbers are correct.
  - m2 (S1|45): the closing construction sentence for the third disjoint pair is compressed; valid as reconstructed in R8.
  - m3 (S1|77): "must be 2" relies implicitly on c ≤ r/2 from S1|41 (which also excludes rank ≤ 1); immediate but unstated.
  - m4 (S1|89): the size-1 alphabet exclusion is implicit in the same 12 ≤ |E_i||E_j| count; conclusion unaffected.
  - m5 (S1|57): "pair capacity" is nonstandard phrasing for 3r ≥ 12; meaning unambiguous.

## Bottom line

Complete symbolic reconstruction achieved for every claim and every special case (r = 2, 3 with 6.1/6.2, rank-2/r = 4 with |P| ∈ {2,3}; all-ranks-≥3 self-dual case). The conditional theorem (S1|7) and the alphabet-size corollary (S1|89) are SUPPORTED at exactly the stated import boundary — N=48, t=24, fixed product basis, **assumed** no residual distance-one pair — with no additional imports and no scope extension. No selected configurations, code, interpreters, solvers, enumerations or replays were used at any point; all verification above is written derivation from the packet text.
