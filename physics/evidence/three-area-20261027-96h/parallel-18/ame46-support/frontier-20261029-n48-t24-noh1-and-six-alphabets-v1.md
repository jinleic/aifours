# Partial zero-excess support48 result: no distance-one residual pairs and no three six-symbol residual alphabets

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 10:24:12 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified or novelty-cleared. This is a partial result for exact `(N,t)=(48,24)`, not a global support49 theorem or an exclusion of support48. Its only external mathematical import is the explicitly named no-OLS(6) theorem. The f127 no-Hamming-one result at N46 is **not** applied outside its scope; the argument is re-derived here.

## 1. Input and claims

Assume a normalized complex AME(4,6) state in a product basis has support N=48, exactly t=24 coefficients of modulus1/6 (P), and other support E of size24. The24 maximal entries are singleton rows and columns in every cut, leaving a12×12 residual unitary with24 entries. Every residual row and column therefore has degree2, and every one of the six E pair projections has12 values, each with two extensions.

Candidate claims, conditional on no-OLS(6):

1. E contains no two words differing in exactly one coordinate.
2. At most two parties can have all six local symbols present in E. In particular the residual profiles `(2,6,6,6)`, `(3,6,6,6)`, `(4,6,6,6)`, `(5,6,6,6)` and `(6,6,6,6)` are impossible. Since pair capacity12 forces any size2 alphabet to have three size6 partners, no residual size2 alphabet can occur.

Other residual profiles, N48 with other maximal-coefficient counts, and the actual support minimum remain unresolved here.

## 2. A six-row residual component admits a classical selection

We first prove a source-free component lemma. Let a nonzero tensor T have, in every cut, a6×6 unitary flattening on its occurring row/column pair values, with12 nonzero entries. Then each pair projection has six values, each with two extensions. For a symbol a, `|T_a|=2|π_j(T_a)|` for all other coordinates j, so the partner degree d(a) is j-independent. It is≥2 and sums to6, hence every local alphabet has size at most3. Pair capacity6 implies the profile is3333 or2333 up to order.

### All ternary is impossible

Each local degree is2 and every symbol fiber contains four words, balanced twice on two values of each other coordinate. Pair incidence on two ternary alphabets is a2-regular3×3 graph, i.e. the complement of a matching. Normalize the matchings from A to the other parties to be diagonal. In A fiber g, each other coordinate uses the two values other than g.

For a pair j,k among the other three parties, a fiber's pair projection is either a full2×2 square or a perfect correlation with two values repeated twice. A fiber is correlated on at most one pair: two correlations would make all three coordinates functions of one binary value, leaving at most two words. The three potential squares omit different symbols and pairwise intersect in one point. Two full squares would already give seven projected values, not six; hence every pair needs at least two correlated fibers. Three pairs require six correlations, but three fibers supply at most three. Contradiction.

### One binary alphabet gives a free fiber

Let B be binary and A,C,D ternary. Normalize A–C and A–D as above. For the C,D projection, at least two A fibers are correlated. Each such fiber contains its two C,D values at both B values, saturating the allowed pair multiplicity2. The four C,D values from two correlated fibers are disjoint. The third fiber cannot have a full four-value C,D projection, because then it would need four new values and make at least eight, not six. Hence all three fibers are correlated and

`T support = S × {b_0,b_1}`,

where S is a six-element set of triples on A,C,D, every coordinate value occurs twice, and all three base pair projections are injective.

Join two S triples when they share one base coordinate. This is a simple cubic graph. The corresponding columns of the appropriate unitary flattening have the same two B supports. For their nonzero ratios r_s, orthogonality gives `r_{s′}=−1/conjugate(r_s)`. This fixed-point-free involution forbids odd cycles, so the graph is bipartite. Choosing b_0 or b_1 by the bipartition selects six support words that are pair-injective on all four coordinates.

Thus **every possible six-row unitary component of this type has a six-word pair-injective selection**. The exact twelve-entry positive component already checked in `frontier-20261029-freefiber-component-control-v1.json`, SHA-256 `0ff419e62ac26185b580decb82d6e02efcac370a760660b12d036bdb485bef5e`, realizes this mixed case; it is not an AME(4,6) witness.

## 3. Propagating a distance-one pair at n=12

Suppose E has two words differing only in D, over a base triple s and two values D_0={d_0,d_1}. Since all pair multiplicities are exactly2, the common base pairs are saturated. In a cut with rows formed by a shared base coordinate and D, the two columns through s share one row; unitary orthogonality forces their second row to coincide. This propagates the same free D pair along all three base-coordinate partner operations.

Their closure S is a simple cubic graph of triples, each base value appearing twice and each base pair injective. The tensor on `S×D_0` is an isolated m×m residual unitary block in all three cuts: every used base/base and base/D pair has its two extensions already supplied, so no E entry outside this component can share such a pair. The phase ratio involution makes S bipartite; hence m is even and m≥6. Since m≤12,

`m∈{6,8,10,12}`.

- m12: selecting the free D coordinate by the bipartition gives12 pair-injective words. They share no pair with the24 P words; together they form OA(36,4,6,2), forbidden by the imported no-OLS(6) theorem.
- m10: the complementary residual has pair projection size2 and multiplicity2. Its local degree identity gives alphabets of size at most1, contradicting size2 pair projections.
- m8: the complementary residual has size4 and multiplicity2. Its local alphabets have size≤2; every pair has four values, so all alphabets are binary and the normalized complementary tensor is AME(4,2), impossible by the Pauli spin-flip argument below.
- m6: the complement is a six-row unitary component of the kind in §2. It has a six-word pair-injective selection; the original free component also has a six-word selection. Their pair projections are disjoint in every cut. Together with24 P words they form OA(36,4,6,2), forbidden by no-OLS(6).

No m remains. This proves claim1, not by invoking the different f127 scope but by the explicit n12 complement analysis.

For the self-contained four-qubit contradiction: two-uniformity kills Pauli weights1,2; each triple marginal's purity1/2 gives total weight3 squared sum12, and full purity gives weight4 sum3. The positive spin flip has impossible overlap `(1−12+3)/16=−1/2` with the pure state.

## 4. Three six-symbol alphabets force binary components

Assume A,B,C all have residual alphabet size6. Their local partner degrees sum to12 and are≥2, hence all are2. Every A fiber is a balanced four-word binary cube subset in the other three coordinates. Claim1 excludes cylinder subsets with distance-one pairs, leaving parity subsets; their other-coordinate pair projections are all full.

For j=B,C,D, let U_j be the6×r_j incidence matrix of the two values used in each A fiber. Pair multiplicity2 implies `U_j^T U_k=0` over F₂. For j=B,C, the incidence graph on six symbols is2-regular. Its F₂ rank is at least3; equality holds only for three disjoint double-edge components. Orthogonality over the six-dimensional fiber space forces both ranks to be3. Thus the A fibers partition into three pairs, and B,C each split into three disjoint two-symbol sets on those pairs.

For completeness, the partitions coincide: the column space W_B is spanned by the three disjoint pair indicators, so it is self-orthogonal of dimension3 and `W_B^⊥=W_B`. Every weight-two column of U_C lies in W_B, hence is exactly one pair indicator. For D, every column of U_D also lies in W_B and is a union of whole pairs. Therefore both A fibers in any pair use the same two D values (those D values may recur in other pairs).

Each pair group contains eight E words and has two local values at A,B,C,D. It is isolated in every cut: each side contains at least one of A,B,C, whose group symbols are disjoint from those in the other groups, so no outside word shares its row or column. The corresponding4×4 block is unitary in each cut. After normalization it would be AME(4,2), again impossible. This proves claim2.

## 5. Limits

The component-selection lemma is written complex unitarity, not a finite enumeration or a classical input. The no-OLS(6) import appears only when selected words complete the24 original maximal words to36. The no-distance-one proof and the three-six-symbol exclusion need independent reconstruction before any adoption.

The residual profiles without three size6 alphabets remain open. In particular this packet does not exclude the full zero-excess N48/t24 case, other t values at N48, or produce a smaller-support tensor.
