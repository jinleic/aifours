# v28-B: independent written reconstruction of the MOQLS joint-residual mechanism

Actual returned `/bin/date` before this output: **Sun Oct 25 03:47:48 PDT 2026**. Reviewer MathResearch96h, math-1. Source read in full, including raw LF26–30: `physics/evidence/three-area-20261023-96h/parallel-18/moqls8/joint-residual-transversal-mechanism-v1.md`, SHA256 `8d2ab33eff4381be7f8e8bab97ce47df69fa83cbc686fe89c4143bfdfa6a3245`, 207 LF. Assignment: `peer-review-wave-eighteen-v28.json`, v28-B.

## Overall verdict and limits

**0 FATAL / 0 MAJOR / 0 MINOR at the stated mechanism-correctness scope.** The quaternion control, its exact selected-square parameters, the two-sided transition calculation, the rook-graph/no-transversal obstruction, and the conditional classical/quantum completion interface reconstruct correctly. Every finite arithmetic check listed below used integers and `fractions.Fraction` in the owner's persistent eval kernel; no floats or native scientific process. This is **WRITTEN-checked-in-kernel**, where “kernel” means the arithmetic session, NOT a proof-assistant kernel.

The review DOES NOT promote the control to a q3 witness. It has **no classical mate**, so it cannot be a five-MOQLS family with two classical members. There is no q3 exclusion, q1/q2 result, formal proof, independent executable finite-object certification, cross-vendor review, novelty clearance, or new admission/GO. Historical timestamps, author no-execution assertions, and source-reading claims are not independently recoverable from mathematics; they are not newly attested here.

## 1. Explicit dependency boundaries

### B0 — physical definition, source LF16,20,26,38–59

**0F/0M/0m.** Import only the ordinary product-cell MOQLS definition: each square has unit vectors forming row/column ONBs; different squares have their 64 same-cell tensor products forming an ONB. For cells x≠y this gives `<Q_i(x),Q_i(y)><Q_j(x),Q_j(y)>=0`, and summing the 64 product projectors gives the tensor identity. Conversely 64 pairwise orthonormal product vectors in dimension64 are complete. These are direct finite-dimensional consequences, not an uninspected theorem from the linked paper. The review made no web/source-access assertion.

### B1 — previous physical q3 reduction, source LF11–30

**0F/0M/0m at the import boundary, not a re-review of the imported proofs.** Read the complete 27-LF parent disposition `wave-v20-q3-component-parent-v1.md`. Its accepted statement and remaining cases are exactly the two joint residuals copied here: f4/r4/b8..10 and f5/r3/b7..9. The source explicitly retains all64 cells and all five squares.

Named inherited inputs remain MATCH/ISOLATE2 (source pin `34e5eca0a0d7ebac81b67c39cde758591513c79bf848d3bf9263c27126d1855d`), degree3/S3 with mandatory adjoint correction (`4e49d97cb3e2b813a07c23bfbafe789bc5b510f17e32e8fa5553b423c5197a22`, `36d3dba2fb62059e3acc5a0ee185fa2545b2bb31d373733272e4172e5db0ac11`), and the whole-component reduction (`8fbd48630a85b4976ccb841924d429a96f5e091b61c7aaacdd5b87087f2897da`) at the earlier parent verdict, not newly independently reconstructed here. None is needed to verify the explicit control or its lack of a classical mate. In particular the control is NOT asserted to meet their full-five-family premises. No b5/b7 minimal-cone conclusion is extended to the higher-span residuals.

## 2. Reconstruction of the exact completion interface

### B2 — one classical mate, LF34–46: 0F/0M/0m

For a classical Latin square C, its symbol classes T_k each have eight cells, one in every row and column. The Q1/C products for T_k lie in the orthogonal sector `C^8 tensor span{|k>}`. Completeness of all64 products is therefore equivalent to Q1's eight vectors on each T_k being an ONB.

The fixed rays are orthogonal axes, and all remaining vectors lie in their orthogonal complement A. Such an ONB must use each fixed axis once: omission prevents spanning that one-dimensional summand, repetition violates orthogonality. The remaining r vectors must be pairwise orthogonal A-rays and hence an A-ONB. Distinct actual occurrences, not free graph vertices, must satisfy the row/column transversal constraint. Conversely a partition with precisely these properties defines a Latin square by its eight labels and makes all64 products an ONB. This proves BOTH directions, with no hidden occurrence-to-ray injectivity assumption.

### B3 — two classical mates, LF48–50: 0F/0M/0m

Their product vectors are the 64 basis tensors `|k> tensor |l>`. They are an ONB exactly when every ordered symbol pair occurs once, equivalently `|T_k intersect U_l|=1` for all k,l. Row/column transversality supplies the other pairs in the four-net. This supplies neither quantum mate.

### B4 — remaining quantum mates, LF52–59: 0F/0M/0m

Decompose the full product space as the orthogonal direct sum of the f fixed-ray sectors (each dimension8) and `A tensor C^8` (dimension8r). Q1/Q_u product completeness is equivalent to an eight-vector Q_u ONB on EACH fixed matching and an 8r-vector product ONB on Z. The dimensions sum to64, and every cell lies in exactly one sector. No projected vector is mislabeled an ONB. The classical-mate products are exactly the full net-symbol-line ONBs of Q_u, in addition to its ordinary row/column ONBs. The independent Q2/Q3 product ONB remains mandatory across ALL cells. Thus the displayed gluing conditions are jointly necessary and sufficient when supplied as full arrays; they are not a construction.

## 3. Quaternion algebra reconstructed

### B5 — oriented basis and Q4, LF65–93: 0F/0M/0m

For the integer imaginary rows v1=(-10,2,11), v2=(10,-5,10), v3=(5,14,2), the squared norms are225 and pairwise dots zero. Their cross product is v1×v2=(75,210,30)=15v3. Consequently `(v1/15)×(v2/15)=v3/15`, not an orientation reversal. With imaginary quaternion multiplication `xy=-x·y+x×y`, the normalized a1,a2,a3 obey exactly `a1 a2=a3`, `a2 a3=a1`, `a3 a1=a2`, and `a_i^2=-1`.

Left/right multiplication by a unit quaternion preserves norm and thus inner product by real polarization. For fixed i, the four a_i e_j are an ONB; for fixed j, the four a_i e_j are also an ONB because 1,a1,a2,a3 is an ONB. All vectors are real, so these are also complex ONBs.

### B6 — full Q8 and multiplicities, LF95–117: 0F/0M/0m

Each actual row has one Q4 row in its diagonal block and four different g-axes in its other block; the two summands A,F are orthogonal. Columns work identically. Thus the formula supplies all64 unit vectors and a genuine QLS8.

For imaginary a=(a,b,c), the vectors `a e0`, `a e1`, `a e2`, `a e3` have their sole zero coordinate at 0,1,2,3, respectively, since all three coefficients are nonzero. For a fixed column the three noncoordinate vectors are orthogonal; across columns their distinct supports preclude parallelism. The four coordinate rays are separate. Hence Q4 has exactly16 rays, each occurring twice in Q8. Each F-axis occurs four times in each of two off-diagonal blocks, hence eight times. Exactly four rays have multiplicity8; no others were omitted. The 16 three-coordinate/coordinate A-rays connect the support graph on all four A coordinates. The whole QLS uses20 distinct rays and is nonclassical in the selected-square sense.

### B7 — projector span b=10, LF119–149: 0F/0M/0m

Reality bounds the projector span above by `dim_R Sym_4=10`. To show no annihilator remains, coordinate projectors first force diag(K)=0. Column0 produces rows (-20,-110,22), (-50,100,-50), (70,10,28) on (K12,K13,K23). Their sum is zero and the first two are independent. Solving gives `(-11,7,25)t`.

The formulas `a e1=(-a,0,c,-b)` and `a e2=(-b,-c,0,a)` send the same coefficient system to `(K03,-K02,-K23)` and `(-K03,-K13,K01)`. The first gives s=-t, K03=11t, K02=7t. The second gives u=t from K03, while -K13=7u and K13=7t force 14t=0. Therefore K=0, proving b=10 over real symmetric matrices. Imaginary skew-Hermitian directions are irrelevant: b is the real span of these real projectors, not the entire16-dimensional Hermitian space. The f orthogonal F-axis projectors add four dimensions, giving a=14.

## 4. All transition supports and the no-mate theorem

### B8 — degree3 in both orientations, LF151–167: 0F/0M/0m

Distinct Q4 rows have transition matrix from multiplication by `bar(a_i)a_l=±a_m`. It is imaginary with all three coordinates nonzero; its real4-by4 multiplication matrix has precisely one zero in every row and column. Distinct Q4 columns instead use the coordinate imaginary unit in the rotated basis; its three coordinates are one R column, again all nonzero. Equal bases are monomial.

For a row/column transition, the common vector isolates one entry of modulus1. For all remaining entries i≠l,k≠j, cyclicity of the real part transforms

`Re(bar(e_k) bar(a_i) a_l e_j)`

into the signed coordinate pairing of `bar(a_i)a_l=±a_m` with `e_j bar(e_k)=±e_p`. Both m and p run bijectively over1,2,3. The remaining block is thus a signed/permuted R with all nine entries nonzero. No support4 entry is hidden. In Q8, every actual line is one such A-basis plus a permutation of the four F-axes; this description is independent of whether the lines' ACTUAL intersection is an A- or F-cell. All transitions therefore retain both row and column degree≤3.

### B9 — orthogonality graph and exhaustive no-transversal argument, LF169–182: 0F/0M/0m

Pairs in a common Q4 row/column are orthogonal. A pair sharing neither has the nonzero residual overlap just computed. The graph on the16 distinct A-rays is exactly the rook graph. Any clique with two entries in one row must remain in that row: a third entry outside it would need both of their distinct columns. If no row contains two, every pair shares a column and the clique lies in that column. Thus the only4-cliques are the four rows and four columns, with no other real or complex A-ONB assembled from actual rays.

A row-clique's four rays have their eight total occurrences in only two ACTUAL Q8 rows. Selecting one occurrence of each of four rays cannot be a transversal, since only two row slots are available. The column-clique argument uses only two actual columns. Therefore no candidate classical symbol class exists, a stronger conclusion than failure to partition all64 cells. The control admits no classical mate. Phases do not alter ray orthogonality or these occurrence constraints.

### B10 — logical control flow and finiteness, LF184–207: 0F/0M/0m

The rejected strategy was selected-square-only impossibility from f4/r4/b≤10, multiplicity gap, and all actual degree3 transitions. Q8 meets these selected hypotheses, so it refutes that strategy without meeting the full physical q3 premises. The occurrence-sensitive transversal mechanism correctly rejects Q8. Nothing in the proof classifies all actual r4/b8..10 configurations or r3/b7..9 configurations. Section8 therefore accurately identifies two STILL UNPROVED obligations: two classical resolutions, then the two complete quantum mates. Finite enumeration for ONE explicit graph never becomes finiteness or a classification of the whole continuous residual.

## 5. Declared exact arithmetic checks

One owner-eval cell constructed quaternion multiplication from the four bilinear coordinate formulas using `fractions.Fraction`. It asserted all of the following, all successfully:

- Orthonormality of (1,a1,a2,a3) and the three oriented quaternion multiplication identities.
- All eight Q4 row/column ONBs (their full4-by4 Gram identities).
- Both row and column support degrees≤3 for all28 distinct pairs of those eight bases.
- Exactly16 Q4 rank-one projectors; for all120 pairs of ray labels, zero overlap iff the labels share a row or column.
- Projector rank exactly10 by exact rational Gaussian elimination on the16 flattened4-by4 projectors.
- All sixteen Q8 row/column ONBs (their full8-by8 Gram identities), and both support-degree bounds for all120 distinct pairs of actual line bases.
- Exact Q8 ray multiplicity distribution: sixteen rays of multiplicity2 and four of multiplicity8.
- All `binomial(16,4)=1820` four-subsets of A-ray labels, yielding exactly eight orthogonal4-cliques, each a row or column. This finite check supplements, and is not substituted for, the uniform rook-graph proof above.

No floating arithmetic, tolerance, external library rank, scientific child process, native solver, network request, model CLI or nested agent was used. This one Fraction implementation is NOT independent triple finite-witness verification and is not a full MOQLS checker. The mathematical review is complete at its frozen scope; the parent's q3 ineligibility decision is unchanged.
