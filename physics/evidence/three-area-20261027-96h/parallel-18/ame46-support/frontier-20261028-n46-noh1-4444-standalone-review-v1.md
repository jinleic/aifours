# Standalone review packet: no distance-one residual pair and the N=46 (4,4,4,4) normal form

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 20:11:05 PDT 2026`; not an exact completion time. **WRITTEN mathematical candidate plus exact finite enumeration**, withheld pending independent attack; not formally verified, independently accepted, or novelty-cleared. The only external mathematical import is Tarry's classical theorem that no pair of orthogonal Latin squares of order six exists. This packet states its own conditional N=46,t=26 input and does not assume a prior global lower-bound disposition.

## 1. Exact input, claims, and boundaries

Assume a normalized complex AME(4,6) state ψ has support N=46 in a given product basis and exactly t=26 coefficients of modulus 1/6. Let P be those t positions and E the other 20. Assume, for the finite normal-form portion only, that each E coordinate alphabet has size 4.

**Candidate A.** No two E positions differ in exactly one of the four coordinates.

**Candidate B.** Under the four-alphabet assumption, E cannot have the required residual-unitary support. This is an exact finite exclusion conditional on Candidate A and the two programs specified below.

Together these candidates exclude only the stated `N=46,t=26,(4,4,4,4)` branch, subject to independent review. They do not establish that N=46 must have t=26, close the other alphabet profiles, prove a global ≥47 bound, provide an AME witness, or decide priority. The only deliberate loss of no-Hamming-one information in the enumeration is made explicit in §7.

## 2. Residual pair-projection facts derived from the input

For every pair of parties, its reduced state is `I_36/36`. Thus every complementary 2|2 flattening `U=6ψ` is a 36×36 unitary. A coefficient of modulus 1/6 exhausts the squared norm `1/36` of every row and column containing it. Therefore each P coefficient is isolated in every pair projection. The 26 P positions occupy 26 distinct singleton rows and columns of each U. After permuting/deleting them, the residual is a **10×10 unitary** on the E entries.

A singleton row or column in a unitary has entry of modulus 1, and the corresponding ψ coefficient would have modulus 1/6, hence would belong to P. Thus all residual rows and columns have at least two E entries. There are exactly 20 E entries and 10 residual rows, so each residual row has exactly two; likewise each column. Every one of the six coordinate-pair projections therefore has exactly 10 values, each with exactly two E extensions.

## 3. Propagating one distance-one pair

Suppose E contains the two words `(a,b,c,d_0)` and `(a,b,c,d_1)`, with `d_0≠d_1`. Denote the base triple by s=(a,b,c) and `D_0={d_0,d_1}`. Each base pair AB, AC or BC of s has already exhausted its two E extensions, so no other E triple may share any of those base pairs.

For each base coordinate, exactly one other base triple shares that coordinate with s and occurs at both D values. For example, in the AD|BC flattening, column `(a,d_0)` contains s and exactly one other E entry `(a,b′,c′,d_0)`. Column `(a,d_1)` contains s and one other E entry. Because unitary columns cannot overlap in exactly one nonzero row, their second BC row is also `(b′,c′)`; thus `(a,b′,c′,d_1)` exists. Pair saturation ensures b′≠b and c′≠c. The same argument applies to the other two base coordinates.

Close s under these three partner operations. The resulting finite set S has:

- both D_0 values over every triple in S;
- injective pair projections on the three base coordinates;
- exactly two triples using each base-coordinate value in S;
- a simple 3-regular graph on S, joining triples sharing one base coordinate.

The three partners of a triple are distinct: otherwise two different base coordinates would agree, violating pair injectivity. Set `m=|S|`.

## 4. Component isolation, phases, and the m=6/8/10 exclusions

In any cut, one side contains two base coordinates and the other contains D and the remaining base coordinate. A base/base pair used by S has its two E extensions already supplied by D_0. A base/D pair used by S also has its two E extensions supplied by the two triples sharing that base value. No E word outside `S×D_0` can use any of those rows or columns, and no P entry can share an E pair row. Hence `S×D_0` forms an isolated m×m unitary residual block in **all three** cuts; its complement is a `(10−m)×(10−m)` unitary residual block, also with every row and column of degree two.

The graph on S is bipartite. If s,s′ share a base coordinate, look at the cut with rows formed by that coordinate and D, and columns by the other two base coordinates. The two columns have the same two D supports. For their nonzero entries, let `r_s=u_{s,d_0}/u_{s,d_1}`. Orthogonality gives

`r_{s′}=−1/conjugate(r_s)`.

This involution has no fixed nonzero complex value, so an odd cycle is impossible. A simple 3-regular bipartite graph has at least three vertices on each side; its vertex count is even. Thus `m∈{6,8,10}`.

- **m=10.** Color S bipartitely and choose d_0 for one color and d_1 for the other. The ten selected words are pair-injective: base pairs are injective, and vertices sharing one base coordinate receive opposite D values. They share no coordinate pair with the 26 P words because P rows are isolated. The 36 words form OA(36,4,6,2), equivalent to a pair of orthogonal Latin squares of order six, contradicting Tarry's theorem.
- **m=8.** The complementary support has n′=2 pair values in every pair projection and at least two extensions per pair. For any one coordinate with r nonempty fibers, each fiber must vary in at least two of the other three coordinates; otherwise an occurring pair has only one extension. For each other coordinate, the number of varying fibers is at most `n′−r`, so `2r≤3(n′−r)` and r≤1. Every coordinate would be constant, contradicting projection size 2.
- **m=6.** The complement has n′=4. The same incidence inequality gives at most two values per coordinate; no coordinate is constant since every pair projection has size 4. Thus all four coordinates are binary, each pair projection is the full four-value product, and the complementary 4×4 residual block is unitary in all cuts. After normalizing it gives a four-qubit AME state, which is impossible by the self-contained spin-flip calculation below.

For the four-qubit contradiction, write `ρ=2^(−4)Σ_P r_P P` over four-qubit Paulis. Two-uniformity kills weights 1 and 2. Purity gives `Σ r_P²=16`. Each three-qubit marginal has purity 1/2, so its weight-3 terms have squared sum 3; over four triples the weight-3 sum is 12, and the weight-4 sum is `16−1−12=3`. The positive spin flip `ρ̃=Y^{⊗4}\barρ Y^{⊗4}` changes a Pauli of weight w by `(−1)^w`, implying `Tr(ρρ̃)=(1−12+3)/16=−1/2`, impossible. This excludes m=6 and completes Candidate A, conditional on no-OLS(6).

**Nonvacuity control.** A free six-row mixed-alphabet component can exist in isolation; the complement/P argument above is essential. `frontier-20261028-freefiber-component-control-v1.py`, SHA-256 `e302ae4688c473e53412e03cc938cd7d785f874257ef0c5b4a85a197c73b5d29`, constructs the six permutations of three symbols times a binary coordinate and checks all three exact `6×6` Grams; receipt SHA-256 `0ff419e62ac26185b580decb82d6e02efcac370a760660b12d036bdb485bef5e`. A single sign flip is rejected. This is a residual component only, not a full AME witness.

## 5. Exact four-alphabet degree normal form

For an active local symbol a, let d_i(a) be the number of its E-partner symbols at any one other party. It is independent of the other party: the number of P words using a is `6−d_i(a)` and their partner values are pairwise distinct. Every E fiber varies in at least two other coordinates, so all such degrees are at least two; the four degrees at each party sum to 10. The only possible multisets are

`X=(2,2,2,4)` and `Y=(2,2,3,3)`.

Let n_k count P words with k coordinates inside the four residual alphabets. The active and pair-active incidence counts are `4(6·4−10)=56` and `6(4·4−10)=36`, respectively; together with |P|=26 they give precisely

`(n_0,n_1,n_2,n_3,n_4)=(0,2,18,6,0),(0,1,21,3,1),(0,0,24,0,2)`.

For any active local symbol, if s,q,h count P occurrences with one, three, four active coordinates, subtracting its other-active incidences from its P occurrence count gives `s−q−2h=2d−6`. A degree-4 symbol requires at least two singleton-active P words; since there are at most two such words in total, and a singleton is active at only one party, at most one party has type X. Thus either all four parties are Y, or precisely one is X.

A degree-2 fiber has four E entries. Its three partner coordinates each use two values twice. Candidate A forbids Hamming-distance-one pairs, so the fiber is one of the two parity four-subsets of a binary 3-cube; all three of its pair projections are full 2×2 rectangles. A degree-3 six-point fiber uses three values twice in each partner coordinate and is pair-injective on those three coordinates; otherwise two words in the fixed local fiber would differ in only one coordinate. In the type-X case, its degree-4 eight-point fiber is pair-injective for the same reason, and each of its pair projections is a 2-regular 4×4 graph.

## 6. Explicit finite incidence and fiber normal form

Choose A to be a Y party in the all-Y case or the unique X party otherwise, and call the others B,C,D. At each Y party order its two degree-2 symbols as 0,1 and its two degree-3 symbols as 2,3. At X order its three degree-2 symbols as 0,1,2 and its degree-4 symbol as 3. For each A symbol, its A–B graph row is the set of B symbols used in that fiber.

There are 34 labeled Y–Y pair graphs. Up to permutations within A's low/high degree classes and within B's low/high degree classes, the following are the five complete representatives (each tuple lists the B symbols in A rows 0,1,2,3):

```
(01,23,023,123)
(02,03,123,123)
(02,13,023,123)
(02,23,013,123)
(23,23,012,013)
```

There are 15 labeled X–Y pair graphs; up to permutations of A's three low symbols and B's low/high classes, the two complete representatives are

```
(01,23,23,0123)
(02,13,23,0123)
```

After making the A–B representative choice, A–C and A–D graphs are allowed to be arbitrary labeled graphs from the same list. C and D have equal type, so their list indices may be ordered C≤D by a party swap. Hence there are `5·34·35/2=2,975` Y cases and `2·15·16/2=240` X cases. These numbers are explicitly checked by both independent programs; a review should independently reconstruct the relabeling/orbit completeness.

In Y, each high six-point fiber is, after relabeling its three symbols, a six-subset of `{0,1,2}^3` with each symbol appearing twice at each coordinate and all three pair projections injective. There are 144. The direct program constructs them as six-subsets; the independent replay constructs partial Latin tables. In X, the high fiber has eight pair-injective triples on four symbols, each symbol appearing twice in each coordinate.

For any pair among B,C,D, each A fiber contributes a pair-injective projected set: low parity fibers contribute a 2×2 rectangle, Y high fibers contribute six points, and an X high fiber contributes an eight-edge 2-regular pair graph. Since every global projected pair has multiplicity exactly two, the F₂ XOR of the four fiber projection sets is zero, and no pair cell occurs in all four fibers. These two conditions are together equivalent to global multiplicity 0 or 2, because each fiber contributes 0 or 1 to a pair cell.

## 7. Exact exhaustive outcomes and distance-one superset disclosure

**All Y.** Across all 2,975 incidence patterns, the XOR and no-fourfold condition retain exactly 10 pairs of high-fiber projection signatures. The two parity choices in each low fiber give 40 complete 20-point support candidates. The direct checker explicitly retains **all 40**, even though 30 of them contain a Hamming-distance-one pair **across** distinct A fibers. Those 30 cannot occur if Candidate A is valid, but are intentionally kept as a conservative superset rather than removed. All 40, including the remaining ten, exhibit a pair of rows or columns with exactly one common nonzero in **each** of the three cuts. Such a pair cannot be orthogonal.

**One X.** Across all 240 incidence patterns, the XOR and 2-regularity requirements retain 10 possible triples of high-fiber pair graphs. For each, the direct checker finds eight possible triples compatible with those graphs, but their pair projections have only six distinct edges each, so no pair-injective eight-word fiber exists. The independent replay uses an exact triangle-edge-cover recursion and finds no cover for all ten graph triples.

The complete normal-form claims and outcomes above are the finite-enumeration attack surface; no conclusion relies on the solver-status diagnostics previously reported for smaller subcases.

## 8. Frozen programs, receipts, and review instructions

- Direct balanced-subset program `frontier-20261028-n46-4444-noh1-enum-v1.py`, SHA-256 `96c519e0169380d333fd7a1414925e0decca2335c6cdf0ac4846c377e7d4ee4c`; receipt `frontier-20261028-n46-4444-noh1-enum-v1.json`, SHA-256 `45e5a0fbdb0b13dcd3f26905dde807b7067dc6ada115a965ed2e81cd66dbd21e`. The receipt includes all 40 all-Y supports, each overlap witness, all ten X high-graph triangle sets, and the 30 cross-fiber distance-one count.
- Independently structured partial-Latin and exact-edge-cover replay `frontier-20261028-n46-4444-noh1-latin-replay-v1.py`, SHA-256 `eb413c112a0398500f9642b9f39fb5ef20079f95aa09da29c95c27d298025425`; receipt SHA-256 `50a20186279163febfd47f586c37172d90ecd751a9cad19ddac4b7e7497ddd13`. It regenerates the incidence graphs and 144 six-point fibers by different constructions and reproduces the same 2,975/10/40 and 240/10/zero-cover outcomes.

Each program runs as `python3 -B <program.py> <new-output.json>` and refuses to overwrite an existing output. These are same-harness exact finite checks, not separate model-family reviews, formal proof, or independent acceptance. Review should attack the free-component propagation and **all-cut block isolation**, the complex ratio involution, the m=6/8/10 case split, the within-fiber consequence, orbit normalization, pair-projection completeness, and every overlap/edge-cover conclusion. In particular, the 30 distance-one supersets in §7 are disclosed, not presented as valid no-distance-one witnesses.
