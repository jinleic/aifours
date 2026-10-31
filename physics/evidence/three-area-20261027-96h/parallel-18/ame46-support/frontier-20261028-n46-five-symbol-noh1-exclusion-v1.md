# Candidate exclusion of every five-symbol residual profile at support 46

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 20:06:26 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, accepted, formally verified, or novelty-cleared. It depends on `frontier-20261028-n46-residual-no-hamming1-v1.md`, SHA-256 `98bb82499cda7135db96de89b6a7fb9901274c892af3fd125ac7a9d446992b0d`, and the pinned N=46 residual/lower-bound dependencies named there. The classical no-OLS(6) theorem is inherited. No global ≥47 result is adopted here.

## 1. Claim and setup

In the conditional `N=46,t=26,n=10,|E|=20` case, no residual coordinate can have five values. Every pair projection of E has ten values, each with exactly two E extensions. If a residual coordinate A has five values, the incidence lemma forces every A-fiber to have at least four E entries, so all five have exactly four. Each of the other three coordinates takes two values twice in every A fiber. By the no-Hamming-one dependency, each fiber is a binary parity set; its projection onto **every** pair of the other three coordinates is the full 2×2 rectangle.

For any other coordinate j, form the 5×r_j F₂ incidence matrix U_j whose g-th row indicates the two j symbols used in A fiber g. Each pair projection of E has even multiplicity, and every fiber projection is full, so for distinct j,k

`U_j^T U_k=0` over F₂.                                             (1)

All local residual alphabet sizes are between 2 and 5, and every pair product is at least 10. The five-valued cases considered below cover all possibilities.

For an active symbol a at any party, its residual partner degree d(a) is independent of the other party: `6−d(a)` maximal P words use a, and their partner symbols are pairwise distinct. The fiber varies in at least two coordinates, so d(a)≥2; the degrees sum to n=10. The incidence matrix U_j is the vertex-edge incidence matrix of a loopless multigraph on r_j symbols with five edges, one edge for each A fiber. Its F₂ rank is `r_j−(# connected components)`.

## 2. Incidence ranks for five and four symbols

For r_j=5, every symbol has degree two. The graph is either one 5-cycle (incidence rank 4) or a double-edge component plus a 3-cycle (rank 3). In the rank-3 case the kernel of U_j^T, as a subspace of the five fiber indices, is spanned by the indicators `p,q` of the disjoint 2-fiber and 3-fiber components.

For r_j=4, the only possible degree multisets are

`X=(2,2,2,4)` and `Y=(2,2,3,3)`.                                  (2)

An X graph is connected: a disconnected component containing its unique degree-4 vertex would need another vertex of degree four or a loop. Hence X has rank 3. A Y graph has rank 2 or 3. If it has rank 2, it is disconnected into a double-edge component and a triple-edge component; its four column membership vectors are `p,p,q,q` for disjoint fiber sets of sizes 2 and 3. Consequently the all-ones vector lies in its column space. Every Y graph has `U_Y^T 1≠0`, since exactly its two degree-3 columns have odd sums.

The elementary rank inequality `rank(U^T V)≥rank(U)+rank(V)−5` yields:

- two five-symbol incidences cannot satisfy (1), since both ranks are at least 3;
- two X incidences cannot satisfy (1), since each has rank 3;
- two Y incidences cannot satisfy (1): if both have rank 3 their product has positive rank; if one has rank 2, its column space contains 1, while the other Y matrix has `U_Y^T 1≠0`.

## 3. At least three five-symbol alphabets

If there are three or four size-5 parties, choose A and two other size-5 parties j,k. Equation (1) requires the product of their incidence matrices to be zero, contrary to the first bullet in §2. This excludes `(2,5,5,5)`, `(3,5,5,5)`, `(4,5,5,5)`, and `(5,5,5,5)` without any P-word counting or phase choices.

## 4. Exactly one five-symbol alphabet

Choose A as the unique size-5 party. Since pair alphabet products must be at least ten, the remaining profiles are `(4,4,4,5)` or `(3,4,4,5)`.

For `(4,4,4,5)`, the three 4-symbol incidences are each X or Y. By the pigeonhole principle two have the same type, contradicting one of the last two bullets in §2.

For `(3,4,4,5)`, choose the size-3 party B and size-4 parties C,D. A residual symbol at C or D has degree at most three toward B, and its four degrees are at least two and sum to ten. Both degree multisets are therefore Y. Their zero product (1) is impossible by §2.

## 5. Exactly two five-symbol alphabets

Choose the two size-5 parties A,B. The other parties are either `(4,4)` or `(3,4)`; two size-3 alphabets cannot have ten projected pairs. Choose C of size 4 and let D be the other party.

Equation `U_B^T U_C=0`, together with `rank U_B≥3` and `rank U_C≥2`, forces ranks 3 and 2. The B graph is a 4+6-cycle graph. Let p,q be the indicators of its disjoint 2-fiber and 3-fiber components. Its transpose kernel is their two-dimensional span. Every column of U_C lies in this kernel; it is nonzero and has weight at most four, since its degree toward D cannot exceed D's alphabet size. Thus every C-symbol membership vector is p or q, never `p+q=1`. Every A fiber uses two C symbols, so exactly two C symbols belong to each disjoint fiber group.

If D has size 3, every column of U_D also lies in the same kernel and has weight at most four because C has size 4. Thus each of D's symbols belongs entirely to the p group or the q group. Each group needs two distinct D symbols, requiring at least four symbols, a contradiction.

If D has size 4, the same kernel argument splits its symbols into two disjoint pairs aligned with p,q. In the p group, A,B,C,D each have two local values and there are eight E terms. Every pair projection has four group values, each with two E extensions, so the corresponding four residual-unitary rows are orthonormal and supported only within the group. After normalizing the group state, its three two-qubit marginals on A,B,C are `I_4/4`, while D has dimension two. This is impossible: for any three-qubit state with all two-qubit marginals `I_4/4`, its Pauli expansion contains only the identity and weight-3 terms, so spin flip gives `ρ̃=I_8/4−ρ≥0`; hence every eigenvalue of ρ is at most 1/4 and `rank ρ≥4`. A two-dimensional D cannot purify it.

All profiles with a size-5 residual alphabet are excluded, conditional on the no-Hamming-one prerequisite and the written argument.

## 6. Exact controls and limits

`frontier-20261028-n46-fivefiber-orthogonality-v1.py`, SHA-256 `ef8d368fbca44bf133756946649c638e793d6e4a31abb74a817f8f93c2a6efff`; receipt `frontier-20261028-n46-fivefiber-orthogonality-v1.json`, SHA-256 `ddc0347c41fcd968d7d5af5f28bce408c8c9b5bf450d6832ea2bde73b9270de9`, checks all 180 normalized X graphs, 310 Y graphs, and 2,040 five-symbol 2-regular graphs. It finds zero X/X or Y/Y zero products, verifies all 600 possible rank-(3,2) five/four zero products have the stated aligned kernel partition, and finds zero allowed three-symbol allocations. This is a finite F₂ control, not a substitute for the written rank proof or independent review.

The exact rank-four 2-uniform three-qubit positive control and rank-three mutation are pinned in `frontier-20261028-three-qubit-shadow-control-v1.json`, SHA-256 `2db5eeabadae4bcee850cd0078622e49777bfadeb4a2f478c3ac8940bb685f96`.

With the separately written `(3,4,4,4)` active-count exclusion, this would leave only `(4,4,4,4)`, addressed by a separate finite-support candidate. No lower bound 47 is accepted by this packet, and every dependency remains subject to scientific review.
