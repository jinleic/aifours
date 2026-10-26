# Isolated two-dimensional sectors are impossible in five MOQLS(8); B3 needs projector-span dimension at least14 — candidate v1

Status: CANDIDATE WRITTEN BRANCH EXCLUSION, not independently reconstructed or accepted. This continues physics-4's ONE full target. No scientific execution, solver, enumeration, compilation, numerical check, CLI, nested agent or old runtime was used. The prior complete candidate remains immutable. This manuscript proves the sector result directly from the physical axioms; it does not need the previous Gram reformulation or global span budget as premises.

## 1. Primary problem, definitions and claimed delta

Let Q_1,...,Q_t be actual mutually orthogonal QLS(n). Thus every array row/column is an ONB of C^n, and for distinct cells x,y and distinct squares s,u,

    <Q_s(x),Q_s(y)> <Q_u(x),Q_u(y)>=0.                     (T)

Phases and all nonzero amplitudes are arbitrary complex numbers. All spans below belonging to square s are taken inside THAT square's C^n; no physical vector or subspace is identified between different squares.

A two-dimensional subspace B is **globally isolated in square1** if every cell vector of Q_1 lies either wholly in B or wholly in B-perp. This is an explicit branch hypothesis, not an assumption on general MOQLS.

Main result I: if B is globally isolated and at least two different orthonormal RAY-PAIRS occur among its cells, then

    n>=2(t+1).                                             (1)

In fact every distinct ray-pair uses at least t+1 actual rows. At n=8,t=5, a globally isolated B must therefore use just ONE orthonormal ray-pair. Consequently the full B3 family cannot have globally isolated B=span(e6,e7), because its standard first row and prescribed column0 already supply different ray-pairs. The same holds for C=span(e4,e5).

Main result II: under the literal B3 axes stated in §5, the real span of ALL cell rank-one projectors of square1 has dimension at least14. Both dimension12 and dimension13 branches are excluded, not merely re-described. This is still a partial B3 theorem; unrestricted n8 classicality and the B3 configurations of dimension at least14 are not settled.

## 2. Two-matchings capacity lemma

Consider two disjoint sets X={x_1,...,x_m} and Y={y_1,...,y_m} of actual cells, each containing one cell in each of the SAME m actual rows and SAME m actual columns. In every such row, its X-cell and Y-cell are different; similarly in each column.

Suppose that for each s=2,...,t, the vectors {Q_s(x):x in X} and {Q_s(y):y in Y} are ONBs of the SAME m-dimensional subspace K_s. No common K_s across different squares is assumed.

**Lemma L.** Under these hypotheses and (T), m>=t+1.

*Proof.* Fix x in X. There is exactly one y_row in Y sharing x's actual row and exactly one y_col in Y sharing its actual column. They are different: a cell sharing both its row and column with x would be x itself, contrary to X and Y being disjoint. Row/column orthogonality gives

    <Q_s(x),Q_s(y_row)>=<Q_s(x),Q_s(y_col)>=0

for every s=2,...,t. For each such s, its transition row from Q_s(x) to the Y-basis of K_s has squared norm1, hence a nonempty support among the remaining m-2 cells. These t-1 supports are pairwise disjoint: two squares being nonzero at the same y would violate (T) for x,y. Thus t-1<=m-2, proving m>=t+1. QED.

Only ONB completeness INSIDE K_s is used. It is derived below by dimension saturation, never guessed from projected vectors. The t-1 counts actual OTHER squares, not row/column lines or coordinates.

## 3. Isolated-sector theorem

Assume B is globally isolated and dim B=2. In each row of square1, exactly two cell vectors lie in B: an ONB of C^n assembled from B and B-perp has exactly dim B vectors in B. The same is true for each column.

Every ray v in B belongs to the unique unordered orthonormal ray-pair {v,v-perp}. Group all B-cells by this ray-pair. There are finitely many classes because there are finitely many cells, even though no phase or angle alphabet was imposed.

For a class a, choose names v_a,w_a for its two rays. Every row meeting this class contains BOTH rays, because its two B-vectors are orthogonal. Likewise every column meeting it contains both. If m_a rows meet the class, it has exactly2m_a cells, m_a on each ray; the number of its columns is also m_a. Its two ray-occurrence sets X_a,Y_a are therefore disjoint matchings on the same m_a actual rows and columns. Every row belongs to exactly one B-class, so

    sum_a m_a=n.                                          (2)

Two different orthonormal ray-pairs in a complex two-space have ALL four cross inner products nonzero. Indeed if a ray from one pair were orthogonal to a ray from the other, its unique orthogonal ray would identify the two pairs.

For every other square s, let K_{s,a} be the span of its cell vectors at all cells of class a. Each ray of square1 occurs at m_a different cells. For any two of these cells, square1's inner product is a nonzero phase, so (T) makes square s's entries orthogonal. Consequently

    dim K_{s,a}>=m_a.                                      (3)

For different classes a,b, ALL square1 cross inner products are nonzero, so (T) makes K_{s,a} perpendicular to K_{s,b}. They are mutually orthogonal subspaces of C^n. Equations (2)–(3) force equality in every dimension bound:

    dim K_{s,a}=m_a,       direct_sum_a K_{s,a}=C^n.        (4)

Both the X_a and Y_a sets give m_a orthonormal vectors in this very same m_a-space, so they are ONBs of K_{s,a}. Lemma L now yields

    m_a>=t+1 for EVERY class a.                            (5)

If at least two classes occur, (2) proves (1). This completes Theorem I.

**Non-vacuous calibration of the hypotheses.** An isolated two-dimensional sector using one fixed orthonormal pair is not excluded: it may simply be part of a classical square. What is excluded at n8,t5 is two DIFFERENT pairs. The proof neither assumes nor concludes that arbitrary projected B-parts of general cells are orthogonal. The global isolation hypothesis makes the selected vectors WHOLE B-vectors.

## 4. B3 consequence: both two-dimensional blocks must mix with their complements

Assume Q_1,...,Q_5 is a full physical B3 configuration with standard row0. Write q^i=Q_1(i,0) and assume the exact supports

    i:          0       1       2      3      4      5      6       7
    supp q^i:  {0}   {1,2,3}  {6,7}  {6,7}  {4,5}  {4,5}  {2,3}  {1,2,3}.

All displayed coordinates are nonzero. Let B=span(e6,e7) and C=span(e4,e5).

Row0 contains the B-pair {e6,e7}; column0 contains {q^2,q^3}. The latter is an ONB of B, with both coordinates of each vector nonzero, so it is a different ray-pair. If B were globally isolated, Theorem I would give 8>=12, a contradiction. Hence some actual full-cell vector v satisfies

    0<||P_B v||^2<1.                                      (6)

The same argument, with q^4,q^5, gives a cell w satisfying

    0<||P_C w||^2<1.                                      (7)

These may be the SAME cell or different cells. Nothing proves that every row mixes, that either cell lies in a prescribed row, or that v,w can be assigned freely.

This excludes the WHOLE globally B-isolated branch, even allowing arbitrary A/C/Z mixing elsewhere, and the analogous C-isolated branch. It is stronger than merely asserting nonzero completion mass in a projected block.

## 5. Exact axis-span dimension and exclusion of dimension12

Put Z=span(e0) and A=span(e1,e2,e3), alongside B,C above. Let S be the real span of every cell projector Q_1(x)Q_1(x)^*, and S_axis the span from row0 union column0.

For two ONBs with unitary transition U, the intersection of their real Hermitian diagonal algebras has dimension equal to the number c of connected components of U's bipartite support graph. To see this, an operator diagonal in both bases satisfies

    diag(d) U=U diag(lambda),
    (d_k-lambda_i)U[k,i]=0.

Thus its real diagonal values are constant on each graph component, and arbitrary real component constants conversely work. The span of the two n-dimensional diagonal algebras therefore has dimension2n-c.

For the B3 axes there are exactly four graph components, on blocks Z,A,B,C of sizes1,3,2,2. The A-component is connected because q^1 and q^7 have all three coordinates nonzero. Therefore

    dim S_axis=16-4=12.                                   (8)

Every element of S_axis is block diagonal in Z,A,B,C.

If dim S=12, then S=S_axis. Every cell projector would be block diagonal. A rank-one projector vv^* can be block diagonal only when v lies wholly in one block: two nonzero block components v_X,v_Y give nonzero off-block matrix v_X v_Y^*. Hence B and C would both be globally isolated, contrary to §4. This excludes dim S=12 and establishes dim S>=13 without using the earlier global covariance candidate.

## 6. A one-dimensional off-block coherence cannot touch three or more blocks

We now assume dim S=13 and derive a contradiction. Let pi be the real-linear map deleting all four diagonal blocks of a Hermitian matrix. Since S contains the 12-dimensional S_axis and pi vanishes there,

    dim pi(S)<=1.

It is nonzero by (6), so pi(S)=R D for a nonzero Hermitian off-block matrix D. Every mixed cell projector has a nonzero real multiple of D as its off-block part; all other cells are pure in one block.

Choose a mixed unit vector v and rescale D=pi(vv^*). Its active block set J consists of the blocks where v_X!=0. If another mixed unit vector w has pi(ww^*)=lambda D, then lambda is real and nonzero. The nonzero off-block positions show that w has exactly the same active block set J. On every active pair, the rank-one outer products imply w_X=c_X v_X for nonzero complex scalars c_X, with

    c_X conjugate(c_Y)=lambda      for X!=Y in J.          (9)

If |J|>=3, take distinct X,Y,T. Equations (9) with X,Y and X,T give c_Y=c_T; their own equation gives lambda=|c_Y|^2>0. The remaining equations force all c_X to be equal. Thus w is a scalar multiple of v, and normalization gives lambda=1. ALL mixed projectors would then have the same off-block part D. A row containing a mixed cell could not have zero off-block projector sum: all its mixed cells contribute D, the pure cells contribute0, but the full ONB resolves the block-diagonal identity. Contradiction.

Therefore |J|=2. There are fixed unit rays b,c in two distinct blocks such that every mixed vector lies in

    F=span(b,c)

and has nonzero components along both. Every row containing mixed cells has at least two of them, since one nonzero off-block part cannot cancel. It has at most two, since they are orthogonal vectors in a two-space. Hence it has exactly two, forming an ONB of F. The same is true of each mixed column.

By §4 BOTH B and C must participate in mixing. Since there are only two active blocks globally, these two blocks must be B and C. We may take b in B and c in C. No A/Z mixture or additional cross-block direction is concealed in this reduction: either would contradict dim pi(S)=1 or the fixed active block set just proved.

## 7. Pure-B dimension saturation in the one-channel B-C case

Let k>=1 be the number of actual rows containing mixed cells. Each has exactly two mixed cells; the same count of two per mixed column gives exactly k mixed columns.

A mixed row has its two F-vectors forming an ONB of F. Every remaining vector is pure in one of Z,A,B,C and perpendicular to F. The B-pure entries in that row therefore consist of exactly ONE ray b-perp in B; similarly the C-pure entries consist of exactly one ray c-perp in C. This follows either from the ONB dimension count or by projecting the row resolution onto B and C. The same statements hold in every mixed column.

A nonmixed row has exactly two B-pure entries forming an ONB of B. Group these entries by their unordered B-ray-pair, as in §3. Let beta be the distinguished pair {b,b-perp}; let m_beta count nonmixed rows using beta. For every other pair alpha, let m_alpha count its rows. Then

    k+m_beta+sum_alpha m_alpha=8.                          (10)

The beta B-pure cells contain m_beta copies of ray b and m_beta+k copies of ray b-perp. Each other alpha contains m_alpha copies of each of its two rays. Its rows and columns are nonmixed, and its two occurrence sets are disjoint matchings on the same m_alpha actual rows/columns.

For square s>=2 let K_{s,beta} be the span of its entries at the beta B-pure cells; similarly define K_{s,alpha}. Different pure-B ray-pairs have all cross overlaps nonzero in square1, so these subspaces are mutually orthogonal. The repeated square1 rays give

    dim K_{s,beta}>=m_beta+k,
    dim K_{s,alpha}>=m_alpha.

Their lower bounds sum to8 by (10); all lie inside C^8. Thus every bound is saturated, and their orthogonal sum is C^8. In particular, both alpha ray-occurrence sets are ONBs of the SAME m_alpha-space. Lemma L gives

    m_alpha>=6 for every alpha.                            (11)

At least one alpha exists: the row0 B-pair {e6,e7} and column0 B-pair {q^2,q^3} are different, so they cannot BOTH equal beta. Both axes consist of pure-block cells and are nonmixed. Therefore one of their ray-pairs occurs among the alpha classes, and its m_alpha is positive.

## 8. The mixed cells consume another at-least-six-dimensional row class

For each s>=2, every vector Q_s(x) at a mixed cell x is perpendicular to K_{s,alpha} for EVERY alpha. Indeed square1's mixed vector has nonzero B-component along b, and b overlaps both rays of any alpha different from beta. Its inner product with every square1 vector on that alpha class is nonzero. Equation (T) gives the asserted orthogonality.

By the saturated direct sum in §7, all such Q_s(x) lie in K_{s,beta}. They are also perpendicular to L_s, the span of square s's entries at the m_beta pure-b cells, because square1's mixed vectors overlap b. Those m_beta entries are orthonormal, so dim L_s=m_beta. Hence every mixed-cell entry of square s lies in

    W_s=K_{s,beta} intersect L_s-perp,
    dim W_s=(m_beta+k)-m_beta=k.                          (12)

Again the physical W_s can differ between squares.

Square1's mixed cells form a two-regular board on k actual rows and k actual columns, with an ONB of F on the two selected cells of each line. Group these cells by their orthonormal ray-pair in F. Let ell_a be the number of mixed rows in class a. Then sum_a ell_a=k; each ray occurs ell_a times and its two occurrence sets are matchings on the same ell_a rows/columns. Distinct F-ray-pairs have all cross overlaps nonzero.

The entries of square s at ALL mixed cells lie in its k-space W_s. For each class a, the repeated rays force span dimension at least ell_a, and different classes give orthogonal spans. Since their lower bounds sum to k, saturation makes both ray-occurrence sets of each class ONBs of the SAME ell_a-space. Lemma L applies yet again and gives

    ell_a>=6 for every nonempty mixed class a,
    k>=6.                                                 (13)

Combine any alpha from (11) with (10) and (13):

    8>=k+m_alpha>=6+6=12,

a contradiction. This excludes dim S=13.

**Theorem B3-R14.** Every actual full B3 family of five MOQLS(8), under the literal axis supports in §4, has

    dim_R span{Q_1(x)Q_1(x)^*: all64cells x}>=14.           (14)

All phases, axis amplitudes, other-square supports and unrestricted full-cell vectors were retained. The argument excludes two genuine projector-span branches; it gives no full B3 no-go. If the previous candidate's global span budget is separately validated, (14) would tighten the remaining four squares' combined surplus to at most8. That combination is not a new independently accepted claim here.

## 9. Comparison with actual inherited bounds

- The first packet's Gram equivalence is an encoding, not a scientific discovery. Its span budget alone does not eliminate a physical branch. That assessment is unchanged.
- The old D-extension verdict accepts necessary concentration at single-line scope, not a whole-grid no-go. The old propagation verdict explicitly leaves whole-vector compatibility open and only guarantees some shared-row completion mass. The present sector theorem excludes a WHOLE globally isolated two-space family even allowing arbitrary mixing in the complement. It does not misidentify projected components as orthogonal vectors.
- PURE23 was already excluded for full B3; merely deriving it again under rank12 would not be new progress. It is NOT used here. The old column1 PURE family and all its arbitrary-axis cases remain present.
- The old type-elimination notes derived no contradiction for their whole families. The present branch is specified by global sector isolation/projector-span dimension, not a recycled mass-table feasibility claim.
- Theorem B3-R14 is a new AUTHOR-WRITTEN candidate relative to the baseline sections actually read. No external novelty, priority, best-known or human/kernel claim is made. A bounded web search located direct-sum/single-square constructions, not an authenticated statement of this sector bound; that miss is not priority clearance.

## 10. Import trust and remaining full target

Only physical QLS/tensor-product orthogonality definitions from Ball–Simoens arXiv:2607.12933v2 §§2.2–2.3 and elementary finite-dimensional complex linear algebra are used. All needed counting and subspace-saturation arguments are written above. The B3 support table is an explicit conditional hypothesis imported from the old pinned table, not a claim that the unrestricted target normalizes to B3 alone.

Old records consulted for the comparison:

- institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-Dext-parent-verdict-v1.md and its stated scope;
- institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-propagation-parent-verdict-v1.md;
- the actual PURE23, PURE1 and type-elimination source manuscripts under physics/evidence/six-lane-20261018-96h/moqls8/continuations/.

No old computational result is a proof premise. GA18/18 and GB15/18, the three UNKNOWN inputs, H23/H24 unproved UNSAT premises, global U/T16/A10/A11 bridges, proof-retention limits and all runtime HOLD obligations remain unchanged. No native launch or runtime repair follows from this manuscript.

Still missing: exclusion or construction of full B3 families of projector-span dimension at least14, all other unrestricted support classes, or a direct global D=0 proof/exact D>0 point. Complete-candidate correctness must be checked on the frozen bytes by Main and an actual separate reconstruction before promotion. No automatic outside-model review is authorized.
