# Candidate support48/t24 bridge: no residual party can use all six symbols

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 11:00:37 PDT 2026`; not an exact completion time. **WRITTEN reduction plus exact finite incidence certificates**, not independently reviewed, adopted, formally verified or novelty-cleared. This is a partial N48/t24 result, not an exclusion of support48 or a global support49 theorem.

## 1. Exact input and prerequisite

Assume a normalized complex AME(4,6) state has `N=48`, exactly `t=24` coefficients of modulus1/6 (P), and other support E of size24. Every2|2 flattening `U=6ψ` is unitary. Removing the24 singleton P rows/columns leaves a12×12 residual unitary with24 entries, so every one of the six E pair projections has12 values, each with exactly two E extensions.

This packet uses the exact-scope **N48/t24 no-distance-one candidate** in `frontier-20261029-n48-t24-noh1-and-six-alphabets-v1.md`, SHA-256 `6bbe85a8b1bec38ef5984d32408c52479ec58edeb3502398d87ab1f7e04a7c96`. That proof re-derives n12 propagation and the m6 complement selection; it is separately unreviewed and conditional on no-OLS(6). The recorded N46 f127 lemma is **not** applied outside its scope. No other classical import, no SAT certificate, no phase solver and no held material is used.

**Candidate conclusion:** no E coordinate alphabet has size6. Since a size2 alphabet would require each other size to be6 (`2r≥12`), residual alphabets must all have sizes3,4 or5. This does not resolve those profiles.

## 2. Six parity fibers and incidence matrices

Suppose A has six E values. For any E symbol a at any party, exact pair multiplicity2 gives `|E_a|=2d(a)`, where d(a) is its number of partner values at any other party, independent of the partner. d≥2, and the six A degrees sum to12, so all are2.

Every A fiber has four E words, balanced twice on two values at each other coordinate. The no-distance-one prerequisite leaves only the two parity subsets of that binary3-cube. Therefore every A fiber projects onto the full2×2 rectangle on any pair of the three other coordinates.

For j=B,C,D, let U_j be its6×r_j incidence matrix: the row indexed by A=a has ones on the two j values used in that parity fiber. Every row has weight2, every used column has weight≥2 and all column weights sum to12. The columns' labels may be independently permuted without changing the problem.

For any pair j,k≠A and symbols b,c, the number of E words with `(x_j,x_k)=(b,c)` is the integer intersection of the two column supports in U_j,U_k. By exact pair multiplicity, every such intersection has size0 or2. This is an **integer** condition, not just evenness over F₂.

Every pair product `r_j r_k≥12`; with local dimensions≤6, there are17 sorted triples of partner sizes in the range2,…,6.

## 3. A complete small incidence classification

A column of U_j is a nonempty six-bit mask of weight≥2. Since column labels are irrelevant, U_j is a sorted **multiset** of r_j masks whose per-bit coverage is exactly2. Repeated masks are retained as distinct local symbols. All such matrices have been completely enumerated by two distinct constructions:

- producer: enumerate the possible sorted column-weight profiles summing to12; choose mask multisets of each weight; retain per-bit coverage2;
- replay: partition the12 labeled edge-end stubs into vertices, rejecting loops and singleton vertices. The two stubs of fiber g cannot belong to the same vertex. Sort/deduplicate the resulting column multisets. This independent construction visits667,951 nodes and recovers exactly the same whole families.

Family counts for r=2,3,4,5,6 are respectively **1,115,1150,1295,130**. The producer checks compatibility by a precomputed allowed-column-mask test; the replay independently uses exact numpy int64 integer matrix products, whose sums are at most6. Every compatible triple is included and has one of two directly verifiable structural certificates:

1. **COMMON_ROW_PAIRING:** the six fibers split into three pairs, and in every one of U_B,U_C,U_D the two rows in each pair are identical.
2. **TWO_SINGLETON_INTERSECTIONS:** some two distinct A fibers have row-set intersection of cardinality1 at two distinct partner coordinates.

No compatible triple is left unclassified. Complete counts, with columns relabeled only (A fibers remain labeled):

| partner sizes | common pairing | two singleton intersections |
|---|---:|---:|
| 2,6,6 |15|0|
| 3,4,4 |0|30|
| 3,4,5 |0|0|
| 3,4,6 |0|0|
| 3,5,5 |0|0|
| 3,5,6 |0|0|
| 3,6,6 |60|0|
| 4,4,4 |90|0|
| 4,4,5 |90|0|
| 4,4,6 |180|0|
| 4,5,5 |90|0|
| 4,5,6 |135|0|
| 4,6,6 |105|0|
| 5,5,5 |90|0|
| 5,5,6 |90|0|
| 5,6,6 |45|0|
| 6,6,6 |15|0|

Total: **1,035** compatible triples, with1,005 common pairings and30 singleton-intersection cases. The proof after this finite classification uses actual same-tensor complex unitarity.

## 4. Singleton intersections force a unique row overlap

Let A fibers g,h have singleton intersection in the two partner coordinates C,D. Their C,D rectangles intersect in exactly one coordinate pair `(c*,d*)`. Since each fiber is a parity four-subset, its C,D projection is full and contains exactly one word above that pair. Let the remaining B values of these words be b_g,b_h; they **need not be equal**.

The two AB rows `(g,b_g)` and `(h,b_h)` are distinct. They both contain the CD column `(c*,d*)`. Every column in either row belongs to its fiber's C,D rectangle, whose mutual intersection is exactly that one pair. Thus the rows share exactly one nonzero column, impossible for orthogonal rows of a unitary. This excludes every certificate of type2, independently of the two parity signs.

## 5. A common pairing forces a forbidden binary component

Take any paired fibers g,h with identical B,C,D row sets. Their eight E words use two local values at **each** of A,B,C,D. At each pair among B,C,D, the common2×2 rectangle has one occurrence in each parity fiber, hence exactly two in this eight-word group. These projected values are saturated: no E word outside the group can share them. Pair projections involving A are likewise confined to the group by A's two fiber labels. No maximal P word shares an E pair.

Therefore the group's support is an isolated4×4 unitary block in every cut. This argument does **not** assume different groups' individual B,C,D symbol sets are disjoint. They may overlap at one coordinate; saturation of every pair rectangle is what gives the required all-cut isolation.

After normalizing the group state, every two-qubit marginal is `I_4/4`, giving AME(4,2), impossible. For completeness, Pauli weights1,2 vanish; each triple's purity1/2 makes the total weight3 squared sum12, and global purity makes the weight4 sum3. The positive spin flip would have overlap `(1−12+3)/16=−1/2` with the pure state. This excludes every common-pairing certificate.

Thus every compatible incidence triple is inconsistent with the original tensor's unitarity. A six-symbol residual party cannot occur, conditional on the stated no-distance-one prerequisite and the finite classification's correctness/coverage.

## 6. Frozen finite evidence and corruption controls

Producer `frontier-20261029-sixfiber-incidence-classifier-v1.py`, SHA-256 `d3c0ad7c6a929d20a48a3a59d13f31a70097e2d0e7c5a9675d8d4b5938b7a8af`; candidate/certificate record `frontier-20261029-sixfiber-incidence-classifier-v1.json`, SHA-256 `4e1978e3cebdc6b9ac3cde46cba81bf1cc51f7aae4244e22d09d37dd2260853d` (47,539LF,612,054bytes). It includes every incidence class and every compatible-triple certificate.

Independent12-stub/matrix-product replay `frontier-20261029-sixfiber-incidence-replay-v1.py`, SHA-256 `e114c2e6f091e5380310b4543af1d6f8c1fca3eb47c57f17079bfc676d3a1bd5`; receipt SHA-256 `42b001d09005930265ddb5e9ec94ab4387644612dd0a151c7ed3a7031165df6c`. It checks complete family equality, exact compatible-triple coverage, all1,035 literal certificates, and four intended mutation rejections: duplicate fiber in a pairing, identical fibers in a purported singleton case, unknown certificate kind, and missing triple.

These are same-harness exact finite computations, not independent-model-family/human review or formal proof. Independent review should reconstruct the no-distance-one input at its exact scope; why every size6 A fiber is parity/full; arbitrary column relabeling and duplicate-column handling; completeness of both matrix enumerations; the integer0/2 condition; and the actual unitary contradictions in §§4–5.

## 7. A separate elementary reduction among the remaining smaller alphabets

With no residual size6 or2 alphabet, sizes lie in3,…,5 and each pair product is at least12. General maximal-word activity counting gives `6Σr_i−Σ_{i<j}r_i r_j≤0` at t24,n12; this eliminates3444 and3445. Profile3455 is also impossible without a no-distance-one or finite-classification input:

- P active incidences total54, pair-active incidences35, and |P|=24 give `n_0+n_3+3n_4=5`.
- Its size3 and size4 parties have `3·4−12=0` jointly active P words, so n_4=0 and n_3≤5.
- At either size5 party,18 P words are active, while its sum of joint active counts is `(15−12)+(20−12)+(25−12)=24`. With no quadruple words, this gives `q_i−s_i=6`, so at least6 triple-active P words contain that party, contradiction.

The separate r4444 actual-phase packet (SHA-256 `f3d90e07304746c57c7a985893255b03e678e230713f6d6a8a4fb1643ad673b9`) is not adopted here. If it and this packet's prerequisites were independently accepted, the unresolved N48/t24 profiles would be3555,4445,4455,4555,5555. No exclusion of those five or of the other t cases at N48 is claimed.
