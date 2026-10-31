# ORIGINAL FOUR-family q2 — ENTIRE intrinsic qutrit component forbids a companion

**PhysicsMOQLS8-2. NEW WRITTEN AUTHOR CANDIDATE**, no independent/parent/formal/executable/novelty acceptance. Actual precreation clock bound **2026-10-26T07:08:03-0700 PDT**. NEW prospective scope, not an expansion or transfer of any earlier five-net/C2 verdict.

## 1. Exact theorem, operative ray-gap inputs and the main boundary

N is ANY actual FOUR-net of order8. Q and R are arbitrary complex C8 unit assignments ONB on ALL32 actual N-lines; their64 products form the ordinary64-dimensional ONB. Then Q has NO intrinsic irreducible dimension3 component. The same holds for R by symmetry. Thus the ENTIRE q2 C3 stratum is excluded, not merely a selected ray pattern, a real/affine ansatz or the m4 case.

Named COMPLETE new written ray-gap inputs, unchanged:

- `four-net-global-ray-five-gap-and-uniform-switch-ceiling-v1.md`,115LF, SHA256 **a6a5c0c6264230b2864df048dcd21f50e965bb2e33cd93e243a3f9dd103d1191**: Q alone has no nonfixed ray of multiplicity5/6/7; its separate bounded primitive theorem is not used here.
- `four-net-ray-four-equality-and-all-component-companion-exclusion-v1.md`,107LF, SHA256 **4c37dfd0644cb9a906990f094b6e3da0345a088bc5ef2cea80959a198c9de519**: a nonfixed m4 ray in ANY intrinsic dimension forbids ANY such R, with full positive-Gram equality/actual component/companion halfspace/unitary support proof.

Their ENTIRE union gives every NONFIXED Q-ray multiplicity<=3. Every Q-ray in an irreducible3 component is nonfixed. Fixed singleton rays and classical families remain ALLOWED. The proof below consumes this EXACT weaker-interface consequence; it does NOT assume a nonexistent fifth class on all64 cells.

We derive an additional resolution ONLY on the24 component cells, from the ACTUAL R Gram. The later graph proof needs just five resolutions of THOSE24 cells into3-ONBs, pair intersections<=1, plus the actual eight row/column component frames and m<=3. No extension to an order8 five-net is claimed. This distinction is essential to the full dependency/application gate.

## 2. Component product completeness and sparse ACTUAL R Gram

Suppose V is Q's intrinsic irreducible3 component, with cell set C of size24. Each original N-line contains three V entries forming an ONB of V. All other Q entries are orthogonal to V. Projecting the COMPLETE ordinary Q/R product ONB onto V tensor C8 therefore gives

    sum_(x∈C) P_Qx tensor P_Rx = I_V tensor I8.

Taking the Q partial trace yields the ACTUAL tight-frame identity

    sum_(x∈C)P_Rx=3I8.                                (RF)

For an actual Q-ray v in V, let m<=3 be its multiplicity. Among the eight actual board rows, m contain v and contribute two v-orthogonal component entries each. A row WITHOUT v has at most ONE v-orthogonal component entry: two orthonormal vectors in v-perp within V would span that two-space and force the third ray to be v. Thus the TOTAL C-cells whose Q entry is orthogonal to v is at most

    2m+(8-m)=8+m.                                      (ORTH)

Fix x carrying v. The FOUR actual net lines through x have EIGHT DISTINCT other C-cells, all Q-orthogonal to v and R-orthogonal to R_x. Distinctness follows from actual net incidence. Any y∈C with nonzero R-overlap and y≠x must have Q_y orthogonal to v by ordinary product orthogonality; it cannot be one of those eight net neighbors. Hence there are at most m<=3 such y.

Let G be the COMPLEX24-by24 Gram matrix of the ACTUAL R_x,x∈C. It has diagonal1, and EACH row has at most THREE nonzero OFF-diagonal entries. RF gives

    G^2=3G.                                           (TIGHT)

No covariance contraction is called a projection, no R sector is postulated and no fifth net-line is used to derive this sparsity.

## 3. The sparse tight Gram MUST be eight isolated rank-one triples

Build its off-diagonal support graph K: an edge xy means G_xy≠0. Its maximum degree<=3. For every edge, TIGHT gives

    sum_(z≠x,y) G_xz G_zy = G_xy≠0,

because the two diagonal contributions are2G_xy. Thus EVERY edge lies in a TRIANGLE. No isolated vertex is possible, since TIGHT's diagonal would give1=3; equivalently the squared off-diagonal row mass is2.

The following small support classification is proved, not cited/enumerated. Take any triangle abc. If there is an outside vertex d adjacent to a, the edge ad must lie in a triangle. Since a already has neighbors b,c,d and maximum degree3, d must also join b or c; rename it b. Now a,b both have degree3 and are saturated. Vertices c,d may or may not be adjacent, giving a diamond or K4. No further outside vertex e can attach to c: its edge would need a triangle through a or b (their degrees are already saturated), unless c also joined d, which would exhaust its degree before e. The same holds for d. Hence every connected component is EXACTLY K3, a diamond K4 minus one edge, or K4.

The Gram block on a component of n vertices satisfies G_block^2=3G_block and has trace n, so its eigenvalues are0or3 and n must be divisible by3. The four-vertex possibilities are impossible. Therefore ALL components are K3, each block of rank1. Their three unit vectors carry one common projective R-ray; different components are mutually orthogonal.

There are24/3=8 such triples, so R restricted to C has EXACTLY EIGHT orthogonal rays, EACH appearing three times. This conclusion was DERIVED from the actual frame/sparsity/support equations, not assumed as a classical alphabet for R on the full board. R outside C may still be arbitrary complex, and need not be globally classical.

## 4. A FIFTH component resolution, NOT a fifth full-board net class

The eight R-ray triples partition C. Their Q entries are mutually orthogonal by ordinary product orthogonality at equal R, hence each triple is a3-ONB of V. No original N-line contains two cells of such a triple, because R is ONB on that line. Thus the new triples intersect every original component line in at most ONE cell.

We now have FIVE actual resolutions of the24 C-cells into EIGHT disjoint triples: the original FOUR classes restricted to C, plus these actual R-ray triples. Every triple is a Q3-ONB and every pair of distinct classes intersects in at most one cell. This is ALL that the following graph argument needs.

There is NO claim that each new triple extends to an8-cell full-board line or that those extensions make an order8 five-net. Such an unproved extension would be a dependency defect. Here the entire construction remains inside the original physical Q/R assignment, with EXACT24-point incidence/3-ONB quantifiers.

## 5. Local qutrit span>=6 at the CORRECT weaker interface — full reconstruction

Let b be the real Hermitian-projector span of the component. We prove b>=6 using ONLY: irreducible3, the actual eight ROW and COLUMN3-ONBs, and every ray's multiplicity<=3. No fifth class is used here. This is the operative weaker-interface reconstruction of the earlier local proof, not an automatic transfer of its old five-net verdict.

Fix an ACTUAL local basis E. Its diagonal projector span has dimension3. If some actual transition F is connected3, D_E intersect D_F consists only of scalars on V: shared diagonal eigenvalues must agree across every F-ray support, hence throughout the connected support. So b>=5. Otherwise all actual transitions relative E are monomial or2+1; irreducibility requires at least TWO distinct coordinate edges, giving two independent off-diagonal directions, again b>=5.

Suppose b5; W=Off_E(S) has dimension2. Connected unitary3 patterns are FULL3 or exactly ONE zero: if every row/column degree>=2, two zeros would be in different rows/columns and make two rows overlap in only ONE nonzero coordinate, impossible. Degree1 instead splits a2+1 block. These patterns exhaust all actual cases, including arbitrary complex phases.

**One-zero3 transition, any actual pair.** Name its zero so F has a noncoordinate ray w in B=span(e0,e1), and its other two rays genuinely mix b0/e2, where b0 is the B-ray orthogonal to w. Their off-diagonal span has dimension2 and exhausts W. One direction is the pure B-edge, and B-to-e2 cross vectors in the other direction are parallel to b0. For ANY actual rank-one projector with e2 part nonzero, its B part must therefore be parallel to b0. All rays lie in B OR span(b0,e2).

Any actual3-ONB containing a mixed b0/e2 ray must have a B-pure vector outside that two-plane to span3; orthogonality forces it to be w. If there is no such mixed ray, spanning3 forces e2. Thus EVERY actual row3-ONB contains w OR e2. Both are ACTUAL rays, each occurring<=3; eight board rows would require m_w+m_e2>=8, contradicting<=6. Hence NO actual one-zero3 pair exists under b5.

**A FULL3 transition exists.** Its2-dimensional off-diagonal space has NO pure coordinate edge: if an F-diagonal Hermitian operator has E-off-diagonal support only on one pair, the omitted E-axis is its eigenvector. That axis has ALL three F coefficients nonzero, forcing all F-eigenvalues equal, hence the operator scalar. Thus no actual rank-one ray has coordinate weight2 relative E. Every other actual local basis is E itself or FULL3. At EVERY such other basis the SAME argument applies using its FULL3 transition with E. Therefore ANY two actual bases sharing a ray are the SAME unordered basis.

Group BOARD ROWS by their local unordered basis alpha. Any component cell forces its row/column bases equal. Each class-alpha row has three component cells in three DISTINCT class-alpha columns, hence there are>=3 such columns. Counting3 entries per row/column gives equal numbers r_alpha=c_alpha>=3. Each ray in alpha appears EXACTLY once in each of those rows and nowhere in another class, so r_alpha<=3 by the ray gap. Thus each nonempty row class has3 rows, impossible because their classes partition8 rows. No arbitrary dense frame or whole-column coverage is assumed.

**All-light regime.** No connected3 actual pair remains. Relative actual E, all bases are monomial or2+1. Irreducibility forces two DIFFERENT coordinate-edge directions; they exhaust W and on three coordinates form a path01,12. No02 coherence is possible. Every actual ray lies in the01 OR12 plane. Two genuine noncoordinate vectors from DIFFERENT planes cannot be orthogonal (their overlap has ONE nonzero summand), so every actual3-ONB contains e0 OR e2. Those ACTUAL rays each occur<=3, again contradicting the eight row count.

All b5 cases are excluded. Therefore b>=6 at precisely the row/column+m<=3 interface used here. No four-FULL-mate MATCH, real form, coordinate change at separate cells or artificial ray multiplicity claim is imported.

## 6. Actual five-resolution incidence forces an impossible spectrum

On C join cells sharing any of the FIVE component triples through them. Different classes have no repeated pair, so this ACTUAL graph A is simple10-regular on24 vertices. Let B be its24-by40 incidence matrix; every column has3 entries and every row5. Then

    BB*=5I+A,      A1=10*1,       tr(A^2)=240.

The actual real Q-projector Gram H has rank b, H1=8*1 and HB=J because EVERY one of these40 triples is an actual Q3-ONB. For z=Hw perpendicular to1,0=1*z=8*1*w and B*z=J*w0. Thus the(b-1)-dimensional tracezero Range(H) lies in ker(B*), the A-eigenspace-5. Section5 gives multiplicity t>=5.

After removing ONE eigenvalue10 the remaining square sum is140; six copies of-5 would give150, impossible. Thus EXACTLY five-5 eigenvalues occur. The other18 real eigenvalues mu have sum15 and square sum15. Their polynomial is MONIC INTEGER: divide A's integer characteristic polynomial by(t-10)(t+5)^5. Put nu=mu-1; their sum is-3, square sum3, and their monic polynomial is still integer.

Let n count NONZERO nu. Removing zero roots leaves a nonzero integer product, absolute value>=1. AM–GM of positive squares gives3=sum nu^2>=n. Cauchy gives9=(sum nu)^2<=3n. Hence n3 and equality forces ALL three nonzero nu=-1. The complete ACTUAL spectrum is therefore

    10^1, (-5)^5, 0^3, 1^15.

This is an exact integrality/equality proof, not a graph catalogue or numerical eigensolver. It uses only the restricted five-resolution incidence built in §4, NOT full-board five-net intersections.

## 7. Actual complex common-neighbor geometry contradicts that spectrum

For x≠y let c_xy=(A^2)_xy. Exact regular-graph moments give

    sum_off c=24*10*9=2160,
    tr(A^4)=10^4+5*5^4+15=13140,
    sum_off c^2=13140-24*10^2=10740,
    sum_off(c^2-3c)=4260.

If Q_x,Q_y are DISTINCT rays in V=C3, every common actual neighbor is orthogonal to BOTH, hence lies on their UNIQUE common orthogonal ray. Its TOTAL multiplicity<=3, so c<=3 and c^2-3c<=0. This is valid for arbitrary complex/nonorthogonal or orthogonal distinct rays.

If they are the SAME ray, there are at most TWO partners per cell, so at most48 ordered same-ray pairs in total. For each, c<=10 and c^2-3c<=70. Therefore

    sum_off(c^2-3c)<=48*70=3360<4260,

contradiction. Common neighbors outside C are NOT vertices of this graph and are never counted. This closes the ENTIRE intrinsicC3 hypothesis.

## 8. Original residual, dependency and process limits

For an ordinary FOUR-family with TWO classical members, the actual four-net/full-Q/R hypotheses are automatic by the classical symbol-line bridge and original product definition. The full proof therefore excludes intrinsicC3 in EITHER remaining member. IntrinsicC2 is already separately supported by the accepted actual-four-net theorem; it also conflicts with the present ray-gap<=3, since a4-regular C2 orthogonality graph has shores of size>=4 carrying one ray. Hence any surviving nonclassical q2 member has intrinsic components of dimension>=4; possible partitions4+4 or one4/5/6/7/8 plus singleton axes are not solved.

This does not settle their coupled line/product/phase compatibility, q3/q4 families with fewer classical members, unrestricted four-families, numerical M(8), A10GB15/18/threeUNKNOWNs/A11, finite-object/triple/mutation/replay/family/priority gates. No affine/Egan–Wanless classification is a premise. The new proof is written from the exact222LF ray-gap chain plus the full weak-interface local/spectral arguments above, not accepted from the earlier five-net124LF source headline or an old C2 verdict.

Every new specialized sparsity/tight-frame/support-component/local-span/incidence/integrality/common-ray/application bridge is exposed. Ordinary imports are finite-dimensional complex Gram/projection/frame facts, elementary finite graph/counting, integer characteristic-polynomial division, positive-square AM–GM/Cauchy and unitary block supports. Missing ray-gap authentication remains NOT_RECONSTRUCTED until ENTIRE115+107 proofs are actually audited. Full mathematical AND dependency/application review of this ENTIRE source is required; no older freeze may be widened.

All mathematics is exact WRITTEN, not machine-checked. NO scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nestedagent/newGO/privatefloat/decimal gloss/numeric parameter trial. Metadata date/hash/LF and readonly sources only. Generic tight-frame/sparse-support/spectral methods are PRIOR mathematics; specialist theorem priority/novelty remains UNCLEARED. No human/configured-family/formal/kernel/executable/novelty acceptance or numerical-ledger promotion.

Own currentv112/visiblev105/v107/v109 intake read-order PROCESS MAJOR and all older histories remain; HELDv3 false ALL-eight-columns/global-light/staircase-only lead remains WITHDRAWN and unused. No later proof cures history or establishes clean-thought/runtime/trial-free cognition census. Exclusive new owner-root writes, immutable pinned/shared sources, no git/deletion/publication. Same18/originalprimary/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/cadence<=30min; no early final-park or96-hour closeout. Original higher-component/unrestricted-family written work continues.
