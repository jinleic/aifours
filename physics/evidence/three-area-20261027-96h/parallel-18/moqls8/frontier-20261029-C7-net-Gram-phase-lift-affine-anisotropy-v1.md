# C7 witness gluing: the exact five-net Gram slice, phase lift, and an affine anisotropy obstruction

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual native clock immediately before writing: Thu Oct 29 14:05:46 PDT 2026. This is NEW C7 witness-interface work, not an alternate version of the q1 local-span candidate under f228/f229. It uses neither that candidate nor GAP3: all assumptions and implications below come directly from the original actual five-net and Q-line ONBs.

For every actual C7 q1 witness, its projector Gram must lie in an explicit 20-dimensional spectral slice determined solely by the five-net and its fixed-ray transversal. Its deviations from the unique isotropic matrix have exact prescribed entries and a universal norm lower bound. For the whole affine-line-transversal subclass, the deviation has squared norm at least 168/25, excluding the isotropic Gram ansatz. This does NOT exclude anisotropic physical witnesses, arbitrary transversals, nonaffine nets or C8.

## 1. Actual physical setting and fixed transversal

Q,L1,L2,L3 are four ordinary MOQLS(8): every actual row and column is an ONB in C^8, and all six same-cell tensor-product families are ONBs. The three mates L_i are classical in their own independently chosen output ONBs. Their row, column and symbol classes form an actual five-net on 64 cells: five partitions into eight lines, each line has eight cells, different classes meet exactly once, and a pair of distinct cells shares at most one line. On every such line the Q entries form an ONB, by the original Q-L_i tensor orthogonality.

Suppose Q has an intrinsic component C with complex span W of dimension SEVEN. Its orthogonal complement is one-dimensional. Every actual Q line contains seven component rays and exactly one ray f in W-perp. The eight occurrences of f form a transversal T meeting every one of the forty net lines once. Write X for the remaining 56 component cells. Nothing below assumes the 56 component rays are distinct, an affine net, a local span bound, or that an abstract scalar Gram lifts to actual rank-one projectors.

For x in X write P_x=|Q_x><Q_x|. Each net line's seven X entries form an actual W-ONB and

    sum_{x in X} P_x=8I_W.                                        (1)

## 2. Net graph, fixed-transversal incidence and an exact spectral projection

Let N be the 64-by-64 adjacency matrix of net collinearity: two distinct cells are adjacent if they share one of the five lines. Every vertex has degree 35. Two collinear vertices have 18 common neighbors: six more points on their common line, plus 4*3 intersections of their other lines in different classes. Two noncollinear vertices have 20: 5*4 intersections of lines in different classes. Therefore

    N^2=15I-2N+20J_64.                                            (2)

Partition the vertices into T and X. T is an independent set because it meets every line once. Let A be the X-by-X adjacency block and M the X-by-T incidence block. Every X vertex is adjacent to five T cells, one on each line through it, so A has degree 30. Taking T-T and X-T blocks of (2) gives

    M^T M=15I_8+20J_8,       A M=-2M+20J_(56,8).                  (3)

Thus M has rank eight. Its constant column-space direction is 1_X, with A-eigenvalue 30; the seven-dimensional image of T-contrasts has A-eigenvalue -2. On its orthogonal complement, the X-X block of (2) gives

    A^2+2A-15I=0,

so the remaining eigenvalues are 3 and -5. Their multiplicities are 28 and20, because their dimensions sum to48 and tr A=0. Hence

    spectrum(A) = 30^1, (-2)^7, 3^28, (-5)^20.                    (4)

Let B be the actual 56-by-40 incidence matrix of X cells versus the five net classes' lines. Every X point lies on five lines, and two distinct X points share at most one. Thus

    B B^T=5I_56+A.

Its kernel V=ker B^T is precisely the -5 eigenspace in (4), dimension20. Let Pi be the orthogonal projection onto V. Equation (4) gives the explicit polynomial

    Pi = [A^2-A-6I-(108/7)J_56]/24.                              (5)

In particular Pi_xx=5/14 for every x.

For x,y in X let S_x be the five T cells collinear with x, and put m_xy=|S_x intersect S_y|. Since each S_x has size five in an eight-point T, 2<=m_xy<=5. The X-X block of (2) is

    A^2+M M^T=15I-2A+20J,

and (MM^T)_xy=m_xy. Consequently, for distinct x,y,

    Pi_xy=(11-7m_xy)/168   if x,y are collinear,
    Pi_xy=(32-7m_xy)/168   if x,y are noncollinear.                (6)

All graph matrices here are determined by the supplied ACTUAL five-net and T; no chosen representative catalogue is needed.

## 3. Every actual C7 projector Gram lies on one explicit slice

Let H be the real 56-by-56 Gram of actual rank-one projectors,

    H_xy=tr(P_x P_y)=|<Q_x,Q_y>|^2.

It is PSD, H_xx=1, and H1_X=8*1_X by (1). Every component net line resolves I_W, so H B=J_(56,40). Define

    K=H-(1/7)J_56.                                                 (7)

The constant direction of H has eigenvalue8. Consequently K>=0, K1=0 and K B=0, so K=Pi K Pi. Moreover

    diag K=6/7,       tr K=48.                                    (8)

Set

    D=K-(12/5)Pi.                                                  (9)

Using (5), (8) and dim V=20 gives D=Pi D Pi, tr D=0 and diag D=0. If x,y are distinct collinear cells, actual Q-line orthogonality gives H_xy=0. Substituting (6) into (7)-(9) yields the exact net/witness coupling

    D_xy=(m_xy-3)/10.                                             (10)

Because Pi D=D and tr D=0,

    tr(K^2)=20*(12/5)^2+||D||_F^2
           =576/5+||D||_F^2,
    ||D||_F^2 >= (1/100) sum_(ordered collinear x!=y) (m_xy-3)^2.  (11)

Equation (10) fixes actual off-diagonal entries of the ANISOTROPIC deviation for every net edge simultaneously. It is not a numerical sample, an abstract graph constraint alone, or a statement about an arbitrary projector space.

## 4. The scalar isotropic relaxation and its exact limitation

The UNIQUE isotropic point of slice (8) is

    K_iso=(12/5)Pi,       H_iso=(1/7)J_56+(12/5)Pi.                (12)

It is PSD, has diagonal one, H_iso 1=8*1 and H_iso B=J_(56,40); its real rank is21. For distinct cells, (6) gives

    (H_iso)_xy=(3-m_xy)/10    on a net edge,
    (H_iso)_xy=(6-m_xy)/10    off net edges.                      (13)

Therefore H_iso satisfies the mandatory zero on EVERY net edge iff **m_xy=3 for every collinear pair**. When that happens its other entries are in [1/10,4/10], so the matrix is also entrywise nonnegative. This proves an exact iff ONLY for the stated PSD/diagonal/line-sum/edge-zero SCALAR relaxation. It does not assert that H_iso is the Gram of 56 rank-one projectors in C^7.

The condition m=3 has an explicit all-net-line consequence. Fix a net line l, let t0 be its unique T point, and let its seven X cells be x. Put U_x=T minus S_x, a three-subset of the other seven T points. On this line, m_xy=3 is equivalent to |U_x intersect U_y|=1. The seven triples are distinct; no pair of T points lies in two of them, since any two triples intersect in exactly one. Their seven triples contain all 21 pairs of the seven-point ground set exactly once. Thus they form a Fano Steiner triple system on T minus {t0}. This local Fano condition is a NECESSARY consequence of isotropy, not a classification of all nets or a constructed witness.

## 5. The exact phase-sensitive physical lift

For a given five-net and transversal T, a physical C7 q1 witness is equivalent to the following finite but CONTINUOUS certificate on X:

1. A complex Hermitian matrix C is PSD, has rank seven and C_xx=1.
2. C_xy=0 whenever distinct x,y are collinear in the five-net.
3. The graph on X with an edge when C_xy!=0 is connected.

Necessity follows by C_xy=<Q_x,Q_y>. Conversely factor C as the Gram of 56 unit vectors in C^7. Each net line has seven X cells; condition 2 makes their vectors a seven-ONB. Add ONE unit f orthogonal to C^7 at all T cells. Every one of the five net lines is then a full Q-ONB. Use any two net classes as row/column and the other three as the classical mate labels; the actual five-net incidences give the three classical QLS and all six original pair-product ONBs. Connectedness makes the 56-cell nonorthogonality component intrinsically C7, not a reducible substitute. Thus this is an actual-object iff, with phases and a single consistent vector realization retained.

The line bases also imply

    C^2=8C,       H=C Hadamard-product conjugate(C).              (16)

Equation (16), the rank-seven PSD/zero conditions, and the connectivity condition are the precise phase-lift obligations which a scalar matrix H_iso does NOT pay. No such C is constructed here. The original C7 witness question remains open even on a net whose isotropic relaxation passes Section 4.

## 6. Affine five-nets with an affine-line fixed transversal

Now impose a clearly separate net hypothesis. Identify the 64 cells with F_8^2, let the fixed transversal be the affine line T={(t,0):t in F_8}, and suppose the five net classes are FIVE DISTINCT non-T-parallel affine directions. After this coordinate choice each class has equations

    x+c_i y=t,          i=1,...,5,       c_i distinct in F_8.        (17)

The five classes may be assigned in any order to rows, columns and classical symbols. No assumption is made about Q-vector realness, phases, alphabet, span or isotropy. Every point of X has y!=0.

For each i put

    D_i={c_i+c_j:j!=i} subset F_8^*,  |D_i|=4,
    S=sum_i c_i,         E_2=sum_{i<j} c_i c_j.

Two distinct X points on a class-i line have coordinates (t+c_i b,b) and (t+c_i b',b') with b,b' in F_8^*. Their T-neighbor sets are t+b({0} union D_i) and t+b'({0} union D_i). Writing q=b'/b!=1,

    m_xy=1+|D_i intersect q D_i|.                                  (18)

The next elementary classification is proved here, without a catalogue or executable enumeration.

**Difference-set lemma.** For ANY four-subset D of F_8^*, all six nontrivial ratios q satisfy |D intersect qD|=2 iff

    e_1(D)=0  OR  e_2(D)=e_1(D)^2,                               (19)

where e_1 is the sum of elements and e_2 the sum of their pairwise products.

*Proof.* Let U=F_8^* and C=U minus D, a three-set. Since |U|=7,

    |D intersect qD|=1+|C intersect qC|.

For q!=1, the latter equals one for every q iff the six ratios of DISTINCT elements of C are all six nonidentity elements of U. Normalize C={1,x,y}. Every x!=1 has order seven; writing y=x^k, the ratios cover the six nonzero exponents exactly when k=3 or5: the pairs {+/-1,+/-k,+/-(k-1)} must be the three distinct inverse pairs in Z/7.

Every x!=0,1 in F_8 satisfies one of x^3+x+1=0 or x^3+x^2+1=0, since their product is x^6+x^5+...+x+1. For k=3, the first case gives 1+x+y=0, while the second gives x+y+xy=0. For k=5, the first gives x+y+xy=0, while the second gives 1+x+y=0. Thus C is either the three nonzero vectors of a two-dimensional F_2-subspace, or its pointwise inverse is such a line.

Conversely, multiplicative translates of an additive line are distinct: a nonidentity multiplier has order seven and cannot preserve a three-set. Two distinct two-dimensional subspaces of F_2^3 meet in exactly one nonzero vector, so |C intersect qC|=1 for all q!=1. Inversion preserves the ratio property. Finally e_1(U)=e_2(U)=0, and C is the complement of D, so e_1(C)=e_1(D) and e_2(C)=e_2(D)+e_1(D)^2. The alternatives e_1(C)=0 or e_2(C)=0 are exactly (19). ∎

In characteristic two, direct expansion gives

    e_1(D_i)=S+c_i,       e_2(D_i)=E_2.                           (20)

Indeed four copies of c_i vanish in e_1; in e_2, six copies of c_i^2 vanish and the three occurrences of each cross term give c_i sum_(j!=i)c_j, which cancels the same term in E_2.

The six counts in (18) are all two for class i iff S+c_i=0 OR (S+c_i)^2=E_2. The five S+c_i are distinct. The square map of F_8 is injective, so at most one is zero and at most one has a given square. Hence AT MOST TWO classes have all counts equal to two; at least THREE classes fail the condition m=3 on every collinear pair.

For a failing class, n_q=|D_i intersect qD_i| lies in {1,2,3}: it is at least one by cardinality, and cannot be four because any q!=1 generates the order-seven group and cannot stabilize a four-set. Also n_q=n_(q^-1) and sum_(q!=1)n_q=4*3=12. The six ratios form three inverse pairs; if not all n_q=2, one pair has value1 and another value3. Thus

    sum_(q!=1)(n_q-2)^2 >=4.                                      (21)

For each q there are seven ordered pairs (b,qb) on each of eight lines, hence 56 ordered collinear component-cell pairs. Distinct net classes cannot count the same pair. Combining (18), (21) and at least three failing classes gives the EXACT uniform incidence bound

    sum_(ordered collinear x!=y)(m_xy-3)^2 >=3*56*4=672.            (22)

By (11), EVERY actual C7 witness on this affine-line-transversal subclass must satisfy

    ||D||_F^2 >=168/25,
    tr(K^2) >=576/5+168/25 =3048/25.                             (23)

In particular K=(12/5)Pi is impossible throughout this entire affine subclass. This is a global phase-independent obstruction to a SPECIFIC isotropic projector-Gram ansatz, not a proof that no anisotropic C7 witness exists. Equations (22)-(23) were derived symbolically for all five distinct c_i, not by selecting or running a numeric instance.

## 7. Remaining gap and review boundary

For a general five-net/transversal, equations (10)-(11) constrain the actual witness; isotropic scalar feasibility is characterized by m_xy=3 on all net edges, with the Fano-line consequence. For affine T in an unused direction, isotropy is uniformly impossible and the explicit anisotropy bound (23) holds. Neither result establishes an actual complex rank-seven phase lift C, excludes every anisotropic C7 lift, settles C8, or closes q1.

No earlier q1 uniqueness/span packet, f228/f229 return, C4/C5/C6 theorem, catalogue, held input, numerical probe, solver or external-model review is a premise. The separately adopted q4 disposition and all historical findings remain unchanged. Main's f228/f229 frozen source and all predecessor records are untouched; this packet requires its OWN complete review of the graph spectrum, exact range slice, affine difference-set classification, ordered-pair variance and physical phase-lift iff. No parent, independent-family, human, formal/kernel, executable, novelty or priority acceptance is claimed.
