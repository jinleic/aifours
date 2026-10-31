# w18-physics-5-v1-v2 — complete written review at the exact Gram/scalar-overlap scope

Reviewer **MathOlson-2-2**. Author **PhysicsRQLS10-2**.
Actual returned `/bin/date` before this write: **Tue Oct 27 15:10:13 PDT 2026**.

## 1. Verdict, read frontier and exposure

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**
**Finding counts: 0 FATAL / 0 MAJOR / 0 MINOR.**

This verdict covers the full complex original-object Gram equivalence for every n≥3; the simultaneous actual-projector row/column/transversal kernel and span bounds; and the universally feasible FORMAL matrix M_* for every n≥4 and EVERY Latin incidence L, including the aggregate-bound/equality statement.
It does NOT cover physical feasibility of M_*, existence of an order10 witness, a universal no-go, any old sector classification or a worldwide priority/openness claim.

I read the complete frozen manifest FIRST, then ALL268 literal packet LF in raw1–175 and176–268, including ALL original LF and endings of context35, v1/S2 117 and v2/S3 104.
No verdict preceded complete packet intake.
No other source, old body, author communication, external model or scientific program was used.
Only THIS required output file was written for the review, as the manifest requires; no separate review ACK/checkpoint or shared-source edit was made.

Manifest SHA256 `89c16144896646bd544ab75c876b9edd96f666218c4a0473cca49b5ac0d44a59`.
Literal part SHA256 `8a8a881282dd975ac788753247cb8df529669f3ee274e6450180a2a74c1c5943`,268LF/30450B; observed live hash matches the supplied pin.
Author v1 SHA256 `bd44c7c95d646f130c00307212fdea16a8281518d5dd732d096660bf740d018d`,117LF.
Author v2 SHA256 `859d494ae5dc62fd006d5552d59b91786b37f0ea8919f552678fb8f76afe89b5`,104LF.
These author bindings are the frozen source identities supplied in the manifest/packet, not an extra read of original files outside the allowed packet.

I have substantial earlier RQLS/complex-Gram/QLS and cross-domain source/review exposure from the predecessor round. This is NOT blind or a clean-cognition/no-influence certificate.
No old result, review verdict, S73–S138 material, selected-probe output or private method guide is a premise of this reconstruction. The mathematical arguments below use only the current supplied definitions and explicitly elementary finite-dimensional linear algebra.
My own Olson S1 work is paused for this priority review; none of its mathematical claims is used here.

## 2. Original object, Latin labels and the primary-definition cut

The supplied registered target is a QLS(10) of100 pairwise nonparallel rays, with one resolution into ten ONB transversals.
For general n, a cell is an ACTUAL label x=(i,j) in X=[n]×[n], N=n². Each row and column is an ONB in C^n.
One resolution partitions all N cells into n blocks of n cells, each meeting every row/column exactly once and itself an ONB.
Labelling those blocks by L∈[n] gives an incidence Latin square: each L label occurs once per row and once per column.
This labels the actual resolution; it does not make any quantum entry a computational-basis state or fix a classical array ansatz.
Conversely such an L gives the correct incidence sets of a possible resolution, but their quantum ONB property must still be supplied by actual Gram orthogonality.

Within a parallel class, blocks partition X. Between two different classes, any two blocks intersect in exactly ONE cell:
row/column is the grid property; row/L and column/L are the two Latin incidence conditions.
Two DISTINCT cells therefore cannot share two block types.
This all-L fact is the load-bearing incidence input for both papers.

The v1 literal quoted primary definitions at S2 LF19–33 agree with this registered t=1 object: the between-resolution intersection condition is vacuous for t=1, and n disjoint n-cell transversals cover n² cells.
The supplied quoted Theorem1.3 at S2 LF39 explicitly excludes10. Its logical content therefore does NOT supply an order10 construction.
That is not a proof of nonexistence, worldwide current openness or novelty.

**Named source-verification boundary:** I did NOT open arXiv:2608.29201v2, its original HTML/PDF or any source outside this packet. Primary quote fidelity/version coverage, the unquoted full Theorem1.4 and any later literature are NOT independently reconstructed here.
The author records a restricted primary read and supplies quotes; this review tests their stated logical consequences, not that external read's authenticity.
The ordinary Gram/scalar theorems below do not depend on a primary construction or on the historical status of the target, so this boundary does not become an unpaid mathematical premise of those theorems.

## 3. Exact complex Gram caller — forward

References: S2 LF51–66.
Assume an ACTUAL maximal-cardinality1-resolvable QLS(n), n≥3, and choose arbitrary unit representatives ψ_x of its rays.
Let V be the n×N matrix of those columns and let G=V*V.
Then G is Hermitian, G_xx=1 and every distinct pair in a common row, column or L-transversal has G_xy=0.
All these are statements about the SAME N actual vectors and the SAME L, not separately fitted Gram blocks.

Each row of the array contributes an ONB, hence the sum of its rank-one projectors is I_n.
Summing the n rows gives

`VV*=sum_x ψ_xψ_x*=nI_n`.

Therefore

`G²=V*(VV*)V=nV*V=nG`.

For unit vectors, the complex Cauchy–Schwarz equality condition is exactly parallelism up to a scalar of modulus1.
Distinct rays therefore imply `|G_xy|<1` for EVERY distinct cell pair, including pairs already prescribed zero.
No real-valuedness, common phase, symmetry, sparse support, distinguished seed or sector decomposition was used.

## 4. Exact complex Gram caller — converse and all hidden feasibility conditions

Assume an incidence Latin L and a matrix G with the four displayed conditions at S2 LF55–58.
Hermitian spectral decomposition and G²=nG imply every eigenvalue λ satisfies λ²=nλ; thus λ∈{0,n}.
Since n>0, G is automatically PSD; this is not an additional assumed physical lift.
Its trace is N=n² from the diagonal, so its rank is trace(G)/n=n.

Hermitian spectral factorization gives an ACTUAL n×N complex V with G=V*V.
Its columns have squared norms G_xx=1.
In any row, column or L-block, the n×n principal Gram matrix is EXACTLY I_n: diagonal1 and all other entries prescribed zero.
Thus the SAME n columns in that block are n orthonormal vectors in C^n and hence form a COMPLETE ONB.
The L-blocks are already the n disjoint row/column transversals of the actual cell labels.
Consequently the recovered vectors form a QLS(n) with the stated resolution.
The strict off-diagonal modulus excludes every pair of parallel unit columns, so its cardinality is N up to global phase.

There is no missing tight-frame constraint: the n positive eigenvalues of G are all n, so VV* also has all n eigenvalues equal n and equals nI; the row ONBs give the same conclusion directly.
Zero overlaps and the repeated eigenvalue n cause no degeneracy in this argument.
A diagonal phase conjugation D*GD corresponds to rephasing the unit column representatives and changes neither the rays, L nor any squared overlap.
A global unitary on V leaves G unchanged.
The caller therefore retains the full complex phase freedom and all original occurrence labels.

**Converse scope:** this is an actual Hermitian G theorem, not a theorem about an arbitrary scalar M. G²=nG, the PSD consequence and the strict off-diagonal condition are essential. None is replaced by scalar entrywise bounds.

## 5. Actual-projector overlap Gram, basis sums and the shared kernel

References: S2 LF70–97 and S3 LF17–24.
For the SAME actual vectors define P_x=ψ_xψ_x*.
These are Hermitian positive rank-one projectors with trace1, and

`tr(P_xP_y)=|ψ_x*ψ_y|²=|G_xy|²`.

Treat Herm_n as a REAL inner-product space with inner product tr(AB).
The overlap matrix M is the real Hilbert–Schmidt Gram matrix of the P_x, hence real symmetric PSD; its diagonal is1 and every prescribed pair has overlap0.
For unit distinct rays all other overlaps lie in[0,1), with zero allowed. No lower positivity assumption is added for actual nonforced pairs.

For ANY actual ONB block B, `sum_(y∈B)P_y=I_n`.
Thus for every cell x,

`(M b_B)_x=tr(P_x sum_(y∈B)P_y)=tr(P_x)=1`.

This holds for EVERY row, column and transversal block using the SAME projectors.
Summing the n blocks of one class gives M1=n1.
With u_B=b_B−(1/n)1,

`M u_B=1−(1/n)n1=0`.

Equivalently the map T:R^N→Herm_n, `T(c)=sum_x c_xP_x`, annihilates u_B, since T(b_B)=I and T(1)=nI. M=T*T, so this is an actual linear relation among physical projectors, not only a scalar row-count assertion.

## 6. All three centred spaces and the exact projector-span rank bound

For blocks B,C of size n,

`<u_B,u_C>=|B∩C|−1`.

Within one class this is nδ_(B,C)−1. The n×n Gram matrix is nI−J: it has its sole zero direction along the all-one coefficient vector and is n times identity on the coefficient zero-sum space.
Consequently the centred block space in that class has dimension n−1 and its indicators sum to zero.
Every u_B is orthogonal to 1 because it has coordinate sum n−N/n=0.
Between different classes, |B∩C|=1, so the two centred spaces are orthogonal.

Their orthogonal direct sum W has dimension EXACTLY3(n−1), and W⊆ker M.
Rank-nullity therefore gives

`rank M ≤ N−3(n−1)=n²−3n+3`.

Since M is a real Gram matrix of the P_x, its rank is precisely the dimension of their REAL linear span.
That span contains I from any actual ONB block.
Put Q_x=P_x−I/n. Each Q_x is traceless and belongs to the same span; conversely each P_x is I/n+Q_x.
The decomposition

`span_R{P_x} = R I ⊕ span_R{Q_x}`

is direct and orthogonal because tr(Q_x)=0.
Thus the traceless span has dimension rank(M)−1, at most n²−3n+2.
This does not bound the NUMBER of distinct rays; a finite set can contain many distinct points in a low-dimensional linear span.
No common invariant sector, repeated ray, irreducibility classification or nonexistence theorem follows merely from this rank bound.

## 7. Full formal incidence spectral decomposition for EVERY L

References: S3 LF28–54.
Let B be the3n×N REAL block-incidence matrix, with ALL rows, columns and L-blocks represented; J=11^T on R^N.
Let P_1=J/n², the orthogonal projection onto the all-one line, and let P_W project onto the three-centred-space direct sum.
Define U=(span{1}⊕W)^⊥.
Its dimension is

`N−1−3(n−1)=(n−1)(n−2)`.

For one parallel class A, its incidence outer-product sum
`C_A=sum_(D∈A) b_D b_D^T`
acts as n times the identity on the span of its disjoint block indicators and vanishes on the orthogonal complement.
That span is the orthogonal sum of the all-one line and its own centred class space.
Hence `C_A=nP_1+nP_WA`.
Summing the three classes, whose centred spaces are orthogonal, yields the exact full-matrix identity

`B^T B=3nP_1+nP_W`.

It acts as zero on U. This derivation is independent of the specific Latin square; the complete pairwise block intersections proved in §2 are sufficient.
It follows that

`P_U=I−P_W−P_1=I−B^TB/n+2J/n²`.

No selected incidence pattern, quantum array, numerical fit or sampled spectrum is involved.

## 8. Formal M_*: positivity, rank, every entry and every block identity

For EVERY n≥4 and EVERY L define

`M_*=nP_1 + [n/(n−2)]P_U`.

The two nonzero spectral coefficients are positive and the two projections are orthogonal, so M_* is real symmetric PSD.
Its kernel is EXACTLY W and its rank is

`1+dim U=n²−3n+3`.

M_*1=n1 because P_11=1 and P_U1=0.
Every b_D=u_D+(1/n)1, so `M_*b_D=1` for ALL three block families, not just one class.

Substituting the expression for P_U gives, without normalization ambiguity,

`M_*=(nI−B^TB+J)/(n−2)`.

The diagonal of B^TB is3: every cell belongs to exactly one block of each of three classes.
For DISTINCT x,y it is1 when they share a prescribed block and0 otherwise. It cannot exceed1 by Latin incidence.
Therefore:

- diagonal: `(n−3+1)/(n−2)=1`;
- same-block off-diagonal: `(-1+1)/(n−2)=0`;
- every other off-diagonal: `1/(n−2)`.

For n≥4 this last value lies strictly between0 and1. Thus every displayed entry condition, including strict scalar distinctness, is satisfied.
All listed block sums, the all-one eigenvector, W-kernel and the full rank constraint hold simultaneously.
There is no contradiction between rank saturation and these entries: they are consequences of one common matrix, not independently assembled row-wise data.

**Quantifier boundary:** this proves feasibility of the FOUR DISPLAYED scalar conditions of S3 LF19–22 and the later aggregate inequality. It does not assert that EVERY possible physical moment constraint has been captured by that list.
In particular scalar distinctness M_xy<1 is not by itself a construction of pairwise nonparallel quantum rays.

## 9. Full aggregate inequality, equality, and relaxation-only sharpness

References: S3 LF66–80.
Each cell has3(n−1) distinct forced-zero neighbours; these three sets are disjoint by incidence.
The remaining off-diagonal set A_x therefore has

`d=N−1−3(n−1)=(n−1)(n−2)`

elements, positive throughout the claimed n≥4 range.
For an actual M, M1=n1 and M_xx=1 give sum_(y∈A_x)M_xy=n−1.
Real Cauchy–Schwarz on those d entries yields

`sum_(y∈A_x) M_xy² ≥ (n−1)²/d = (n−1)/(n−2)`.

Since M is real symmetric, `tr(M²)=sum_(x,y)M_xy²`.
Adding every row's diagonal contribution gives exactly

`tr(M²) ≥ n²[1+(n−1)/(n−2)]`.

There is no missing factor of two: this identity sums ORDERED pairs, as does the trace formula.
The argument permits extra actual zeros among A_x and does not assume a uniform overlap ansatz.
Equality in the total sum requires equality in EVERY row, because every row has a nonnegative Cauchy–Schwarz deficit.
Each row must therefore be constant on A_x, and its fixed row sum forces that constant to1/(n−2).
With its prescribed diagonal and forced zeros, the whole matrix is then EXACTLY M_*.
Conversely the formal M_* has those entries and attains equality in every scalar row estimate.

Thus the bound is sharp WITHIN THE SCALAR RELAXATION.
It does not prove an actual RQLS reaches that value, that the bound is physically optimal, or that M_* has an actual phase-compatible lift.
An actual equality object would necessarily have overlap matrix M_*; no converse physical assertion is made.

## 10. Boundaries, degeneracies, and the exact failed physical implication

- v1's equivalence and necessary actual-projector theorem are for n≥3. Their proofs work throughout that domain; actual feasibility may still fail. No implication is inferred from an empty feasible set.
- v2 deliberately restricts to n≥4. At n=3 its displayed nonforced value would be1, so its strict off-diagonal requirement would not be paid; it makes no n=3 formal-feasibility claim. At n=2 the denominator vanishes, and that case is also excluded. These are not silently covered by a limit.
- All actual zero overlaps, additional orthogonalities and repeated positive eigenvalues of G are permitted. The formal matrix's positive nonforced entries are a choice of relaxation witness, not a WLOG restriction on actual objects.
- L varies over EVERY admissible Latin resolution incidence. It is neither frozen to a single seed nor assumed to encode a classical quantum state.
- Traces/ranks are for the common actual cell-labelled matrix. Three individually valid basis models are not treated as a common physical array without the Gram conditions.

A real PSD M_* can be factored as an abstract Euclidean Gram matrix. Its factors need NOT be positive trace-one rank-one Hermitian n×n projectors.
Conversely, ONE common realization by positive trace-one rank-one projectors P_x in Herm_n would already suffice: choose unit representatives, use the forced zero overlaps to obtain every labelled block ONB, and use strict M_xy<1 to exclude parallel rays. Their common vector matrix then supplies G by §§3–4. There is no additional independent phase obstruction AFTER that genuine common projector realization; the unpaid step is obtaining such a realization from abstract scalar M.
A physical lift must supply a COMMON Hermitian G with diagonal1, all forced zeros, `|G_xy|²=M_xy`, strict |G_xy|<1 and G²=nG over the SAME L.
If that exists, §§3–4 supply the actual original witness. To prove the original no-go one would have to exclude every such physical lift over EVERY admissible M AND L, not merely one formal equality matrix.
Neither physical liftability nor unliftability of M_* is proved here.
Excluding M_* alone would exclude a special equality branch, not arbitrary nonuniform actual overlaps.
The source explicitly maintains this distinction, so no false scalar-to-physical converse was found.

## 11. Separate whole mathematics and dependency/application judgments

| Claim / scope | Mathematics | Dependency/application/trust boundary |
|---|---|---|
| Actual Latin resolution labels | Reconstructed from one actual transversal partition | No fixed-seed or computational-basis ansatz; all L retained |
| Complex Gram caller, BOTH directions | Reconstructed, including PSD/rank from G²=nG and all ONBs/cardinality | Ordinary Hermitian spectral factorization and complex Cauchy–Schwarz; not an M-only caller |
| Actual M kernel and projector span | Reconstructed for ALL three parallel classes on the SAME projectors | Real Hermitian Hilbert–Schmidt Gram; ordinary rank-nullity; no common-sector or ray-count conclusion |
| All-L incidence decomposition | Reconstructed as B^TB=3nP_1+nP_W | Uses exact Latin block intersections; no unsupplied primary theorem |
| Universal formal M_* | Reconstructed: PSD, exact rank, all entries, strictness and all block equations | n≥4 essential; formal scalar witness only, not actual projectors/G |
| Aggregate inequality and equality | Reconstructed with every row/equality case | Relaxation-only sharpness; no physical attainment or unrestricted exclusion |
| Primary definitions/status | Logical consequences of supplied literal quotes checked | External version/quote/Theorem1.4 fidelity and worldwide literature NOT independently read or certified |
| Original order10 witness or global no-go | **NOT_ESTABLISHED** by these packets | Exact physical Schur/Gram lift or all-L/all-M exclusion remains missing |

Named ordinary inputs: elementary complex finite-dimensional spectral theorem/Gram factorization, complex Cauchy–Schwarz with equality, real Hilbert–Schmidt inner product/rank-nullity and finite indicator-vector linear algebra. The source-specific applications and every numerical-in-n algebraic identity are proved above symbolically.
No primary construction, old phase theorem, sector split, commutant, irreducibility theorem or protected S73–S138 result is a hidden premise.
The unprovided primary source is a SOURCE-AUTHENTICATION boundary, not a fabricated review finding or a substitute for the complete current mathematical reconstructions.

## 12. Final assurance and actual return boundary

The two author packets remain unadopted by this reviewer. Parent adoption requires Main's own complete author-source AND actual full-scope return reads.
This is same-harness conventional WRITTEN support only, not formal/kernel, human, configured-family/cross-model, executable, finite-certificate or novelty acceptance.
All original author STOP/HELD/ZERO/S98-episode consumers and S73–S97 uncertainty, all earlier findings, N4UNKNOWN/historical actual child exitUNESTABLISHED, auxiliary214STOP and scientific HOLD persist.
No historical clock/cadence/provenance claim is repaired by these algebraic proofs.

No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected state/control/parameter/boundary/decimal arithmetic probe, nested agent/modelCLI/paidAPI, author contact, extra source, Git, deletion, publication or infrastructure action was used.
Only source reads permitted by this manifest, metadata pins/LF/bytes/native clock and this one reviewer-owned output were used.
The physical-lift interface and original order10 alternative remain unresolved at the stated assurance cut.

**Final finding counts: 0 FATAL / 0 MAJOR / 0 MINOR — NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

**END OF COMPLETE w18-physics-5-v1-v2 REVIEW.**
