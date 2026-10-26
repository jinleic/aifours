# Literal Paley conference9 normalization rigidity and a five-orientation bridge v1

PhysicsRQLS10, physics-5. New **author-written CANDIDATE**, requiring its own actual reconstruction. Same primary maximal-cardinality1-RQLS10 problem. This is the exact-bridge lane requested after parent support of the corrected axial packet, not another scientific problem or an enlarged numerical search. Stage clock observed before derivation: **2026-10-24T03:36:11-07:00**; no exact file-creation timestamp is inferred. No scientific executable, solver, enumeration, arithmetic runtime, compilation, old source or CLI ran.

## 1. Inputs, literal conventions and the new logical ingredient

Use the actual Et-Taoui core

    F9=F3[alpha]/(alpha²+1), labels x+y*alpha ↔ x+3y,
    Q_xy=chi(x-y), Q1=0, Q²=9I-J,
    s=i sqrt7, w=(1+s)/sqrt8,
    C=(J-I+sQ)/sqrt8, CC*=8I.

Thus C is symmetric, has its only zeros on the diagonal, and C_ij=w^(Q_ij) off diagonal. Put

    u=w²=(-3+s)/4, u+u^-1=-3/2.

The two imported closed seeds, at their existing **in-harness written-support level only**, are:

1. Central rho_c:t→-t, from `institute/runs/three-area-2026-10-23-96h/rqls-fixed-route-parent-v1.md`.
2. Axial rho_V=(0,2,1,6,7,8,3,4,5), from `institute/runs/three-area-2026-10-23-96h/rqls10-axial-route-parent-v1.md`, ONLY with the complete v3→v2→v1 source chain and all three mandatory errata. Its original coefficient/terminology defects are retained in history.

Each seed excludes, for every second literal C_p with entries C_(p(i),p(j)) and every arbitrary complex unit vector delta, the necessary equation

    M(p,rho)*delta=0,
    M(p,rho)_(i,t)=conjugate(C_(t,i))*(C_p)_(t,rho(i)).

Independent compatibility phases D/E are retained. The Zhang–Cao row/column/transversal and ray-cardinality interfaces are unchanged: these are local uniform-overlap Paley-route obstructions, not the full definition of1-RQLS10 or a construction of100 rays.

**First new logical input:** classify all independent left/right monomial normalizations returning this literal C to itself, also allowing simultaneous complex conjugation. The classification is derived below from u's infinite order and Q-row regularity; it is not assumed to be the rook automorphism group. This additionally puts an exact ceiling on which orientations these two seeds can cover by this class of normalizations.

## 2. Rigidity of all independent left/right monomial phases

Let epsilon=+1 denote no conjugation and epsilon=-1 denote conjugation. Suppose an arbitrary left/right monomial operation returns C exactly:

    C_ij=l_i*r_j*(C_(g(i),h(j)))^epsilon,

where all l_i,r_j are arbitrary complex phases, g,h are permutations of the nine indices, and z^epsilon means z or conjugate(z), not reciprocal notation for a general z.

### 2.1 Zero pattern and symmetry reduce the unknown gauges

The unique zero in row i of the right side occurs at h(j)=g(i). The target has its zero at j=i. Therefore h(i)=g(i) for every i: both underlying index functions are the same g. No independent row/column permutation was silently dropped; the zero pattern forced their alignment.

For i≠j, symmetry of both cores implies l_i*r_j=l_j*r_i. Hence l_i/r_i is a common phase tau. Choose one square root of tau and define d_i=sqrt(tau)*r_i. Then

    d_i*d_j=u^(n_ij),
    n_ij=[Q_ij-epsilon*Q_(g(i),g(j))]/2∈{-1,0,1}.  (1)

The d_i were unrestricted phases before(1). There is no assumed phase alphabet.

### 2.2 u has infinite multiplicative order

If u were a root of unity, both u and u^-1 would be algebraic integers. Their rational sum-3/2 would then be a rational algebraic integer, hence an integer, contradiction. Thus integer powers of u are injectively indexed by their exponent.

For any distinct i,j,k, equation(1) gives

    d_i²=u^(n_ij+n_ik-n_jk)=u^(m_i)

with an integer m_i. Its value is independent of the chosen j,k because powers of u are distinct. Squaring(1) now forces

    m_i+m_j=2*n_ij.

Set x_i=m_i/2, X=sum_i x_i. These are derived half-integers, not assumed coordinates of the original unknown phases. For each i, regularity of both Q and its relabeling gives

    0=sum_(j≠i)n_ij=sum_(j≠i)(x_i+x_j)=7x_i+X.

Summing the nine equations yields16X=0, hence X=0 and every x_i=0. Thus n_ij=0 for every pair, and

    Q_(g(i),g(j))=epsilon*Q_ij.                    (2)

Equation(1) now has all d_i*d_j=1. Returning to l/r, all off-diagonal products l_i*r_j are1, which forces l_i=lambda and r_j=lambda^-1 for a single global phase. These reciprocal global phases act trivially on every matrix.

**Rigidity conclusion:** modulo that trivial global gauge, ordinary monomial self-normalizations are precisely the literal permutations preserving Q; conjugate-monomial self-normalizations are precisely those negating Q. There are no additional nonconstant diagonal phase gauges. This classifies normalizations of this ONE literal C, not all conference9 matrices or arbitrary changes of the local three-basis problem.

## 3. The induced permutation/conjugation group is exactly144

Q_ij=+1 precisely for rook-neighbour pairs in the3×3 grid. Every maximal3-clique is one row or one column: two points sharing a column but having different rows force any third common neighbour into that same column. Thus the six maximal cliques determine the two disjoint parallel families. A graph automorphism permutes the three rows and three columns independently or interchanges the two families. Consequently

    Aut(Q)=(S3×S3) semidirect C2, |Aut(Q)|=72.

Its point0 stabilizer has order8, generated by literal coordinate sign changes g_x,g_y and coordinate interchange S. These statements concern actual finite symmetries and are proved by clique incidence, not an executed permutation census.

Multiplication by zeta=1+alpha is a nonsquare: zeta²=-alpha, zeta^4=-1. Its permutation

    R=(0,4,8,5,6,1,7,2,3),
    R(x,y)=(x-y,x+y) mod3,

therefore satisfies Q_(R(i),R(j))=-Q_ij. All complementing permutations form its coset of Aut(Q), of size72. The resulting induced normalization group G has144 elements, ordinary plus conjugating. Its point0 stabilizer G0 has16. The continuous reciprocal global gauge in section2 is trivial on matrices and is NOT being counted as a finite group.

Every point0 ordinary symmetry is linear over F3: a permutation of F3 fixing0 is a sign change, with an optional coordinate interchange. R is also linear. Thus every element of G0 commutes with central negation.

## 4. Exact all-P and all-complex-phase transport

For an allowed pair(g,epsilon), let

    (F_(g,epsilon) A)_(i,j)=(A_(g(i),g(j)))^epsilon.

By(2), F_(g,epsilon) C=C. It also permutes the ENTIRE second-core family, rather than just a selected second core. Indeed choose a_+=identity and a_-=R. If C'=C_p, then

    F_(g,epsilon) C'=C_(a_epsilon composed p composed g).

This follows from Q_(a_epsilon(x),a_epsilon(y))=epsilon*Q_xy. The map p→a_epsilon∘p∘g is a permutation bijection, and therefore induces a bijection of the5040 distinct literal cores. Any source fixed-point convention p(0)=0 can again be restored by a source translation without changing the core.

Let

    rho'=g^-1 composed rho composed g,
    delta'_t=(delta_(g(t)))^epsilon.

Then, entry by entry,

    M(F_(g,epsilon)C',rho')_(i,t)
       =(M(C',rho)_(g(i),g(t)))^epsilon,

and hence

    [M(F_(g,epsilon)C',rho')*delta']_i
       =([M(C',rho)*delta]_(g(i)))^epsilon.         (3)

The map on delta is an invertible permutation, optionally followed by complex conjugation. It preserves the FULL unit torus, including phases outside K or any finite alphabet. D/E transform to conjugated/permuted diagonal phase matrices and remain independent and arbitrary. Equation(3) neither assumes an invariant delta nor discards a left/right phase freedom.

Therefore the existence predicate

    F(rho): there exist a second literal core C' and delta∈T9
            with M(C',rho)*delta=0

satisfies F(rho) iff F(g^-1 rho g). The two imported negative predicates may be transported throughout their actual G-orbits. This is the bridge's load-bearing new equivalence.

## 5. Exact five-element union at fixed point0

The ordinary point0 stabilizer fixes rho_c:t→-t, and every complementing point0 symmetry also commutes with it by linearity. Thus the central seed contributes exactly one point0 matching.

The ordinary point0 stabilizer sends rho_V only to rho_V and its coordinate transpose rho_H. Coordinate signs preserve rho_V; interchange gives the distinct rho_H. Its ordinary orbit size is2. The complementing coset supplies exactly two more matchings, with zero rather than four rook-positive pairs. They cannot overlap the two positive ones. A coset acts bijectively on the ordinary orbit because Aut(Q) is normal of index2 in G; hence no additional members are hidden.

Here are ALL five matchings in the union, printed on the SAME first-core labels:

| Name | Tuple | Pairs | First-rook-positive pairs |
|---|---|---|---|
| central | (0,2,1,6,8,7,3,5,4) | {1,2},{3,6},{4,8},{5,7} |2|
| rho_V | (0,2,1,6,7,8,3,4,5) | {1,2},{3,6},{4,7},{5,8} |4|
| rho_H | (0,2,1,6,5,4,3,8,7) | {1,2},{3,6},{4,5},{7,8} |4|
| R^-1 rho_V R | (0,6,3,2,8,7,1,5,4) | {1,6},{2,3},{4,8},{5,7} |0|
| R^-1 rho_H R | (0,3,6,1,8,7,2,5,4) | {1,3},{2,6},{4,8},{5,7} |0|

For example R^-1 sends the rho_V pairs{1,2},{3,6},{4,7},{5,8} to{5,7},{8,4},{1,6},{3,2}. The same calculation with rho_H gives the final row. This is written permutation algebra, not an executed search.

By(3), EACH of these five orientations excludes every second literal P and every arbitrary complex diagonal phase vector. The genuinely new ordinary-D8 orientation orbit supplied by the conjugating bridge is the two-member, zero-rook-positive orbit. The central and positive-axis orbits were the original two seeds. In ordinary point0-D8 language these are three orbits of sizes1,2,2; in the extended normalization group they are two orbits of sizes1 and4.

## 6. Forty-five literal involutions across all fixed points, and the exact ceiling

There are105 one-fixed-point involutions of type1+2^4 fixing0, because the eight other points have7!!=105 pairings. There are9*105=945 of this type if the fixed point may vary. These are counts of matching/orientation objects in the local bridge, not QLS witnesses or distinct scientific problems.

Translations preserve the actual first C. Conjugating a listed rho by T_c:t→t+c gives a matching with fixed point c, and equation(3) still applies. Distinct c have distinct fixed points, so the five lists give exactly45 literal involutions, with the seed central orbit contributing9 and the axial extended orbit contributing36. The central translate is explicitly t→2c-t.

Because section2 classifies ALL independent left/right monomial self-normalizations, with or without simultaneous complex conjugation, this transport class cannot enlarge those two seed orbits beyond these45. At fixed0 it leaves100 of105 involutions uncovered; across fixed points it leaves900 of945 uncovered. **Uncovered is not feasible, not an openness certificate for each object and not100 new problems.** It is an exact limit of this symmetry-only reduction. Other logical obstructions or broader equivalences could cover more; none are presumed here.

This ceiling is important: an unrestricted phase gauge cannot turn the presently proved axial route into a WLOG argument for all105. The phase gauges of that literal core were derived to be trivial, and the actual conjugating extension has only the two extra negative-axis matchings at fixed0.

## 7. Evidence boundary and next gate

New delta: one complete normalization-rigidity lemma, an exact unrestricted-torus transport identity, and a rigorously counted nontrivial union of five point0 orientations/45 literal translates. These strengthen the two previously supported fixed-route statements without running the permanently superseded assay or claiming a new QLS construction.

The bridge is **CANDIDATE** until its own actual reconstruction. Its two obstruction premises retain their original written-support provenance; the axial premise MUST retain all three errata and its original1MAJOR+1MINOR finding history. No old source is rewritten and no new scientific GO is inferred from the parent acceptance of either seed.

Not claimed: a classification of all conference9 monomial classes, equivalence of arbitrary QLS resolutions to these matchings, all remaining orientations, all complex H0 lifts, nonuniform100-ray arrays, novelty/publication priority, formal/kernel verification, or unrestricted maximal1-RQLS10 impossibility. The full primary remains UNKNOWN. The modern Huang–Li/Zhang–Cao target's ray and transversal quantifiers are unchanged.
