# RQLS10 — consolidated finite-amplitude isotypic continuation

Owner PhysicsRQLS10-2. Clock actually observed before this consolidation: `Sun Oct 25 11:59:32 PDT 2026`.

**WRITTEN CANDIDATE, not independently accepted.** No scientific evaluation, interpreter/program, enumeration, replay or solver was used. Source inspection/browser rendering and metadata clocks/hashes only. V9/v10/v11 and HOLD remain binding. This is a new representation of an ACTUAL order10 resolution, not a new acceptance of old RT or the unadmitted236/52 census.

## 1. Original target, retained baseline and new scope

The target is still an ACTUAL100-ray order10 array: every row, every column and every member of one designated Latin transversal resolution is an ONB of C10, and all100 projective rays are distinct. Nothing below supplies that completed array or a root tuple satisfying all its constraints.

The pinned `global-onb-actual-seed-normal-obstruction-v2.md`,341LF, SHA256 `e7dd4776278c8363d5a5f9366aba5b1116f689e636da48e2cf0ba11629138326`, remains unchanged. Its actual seed and six mates are the input here. Its nonlinear <=13/46 assertions are under a separate frozen review; this successor neither promotes them nor uses those local obstructions as a global theorem. The supported generic local-ONB theorem likewise is not a100-ray witness.

This continuation replaces a near-classical deformation attempt by a FINITE-AMPLITUDE cyclic-isotypic problem. It proves:

- Full100 within the stated projective Z7-equivariant family requires multiplicities(2,2,2,1,1,1,1), not the tempting fixed-infinity multiplicities(4,1,1,1,1,1,1).
- There is an explicit72-distinct-ray boundary family satisfying all NINE special contexts. Its other21 contexts are NOT asserted valid; it is not a partial or full RQLS certificate.
- All remaining constraints reduce EXACTLY to three10-column unitarities, or equivalently a boundary-six-frame/four-core rendezvous with all shifted Gram conditions retained.
- The superficially easy monomial simple-character core cannot complete it. A genuinely mixed core is necessary. This is a restricted-representation obstruction, not global nonexistence.

The new boundary/core proofs below are independent of the pending local theorems in v2. No connection of every quantum component to a classical seed is assumed. A positive point in this family would solve the existential target; a negative result here would only exclude this family.

## 2. Actual board and notation

Rows and columns are X=Z7 disjoint-union{infinity_0,infinity_1,infinity_2}. Ordinary indices are modulo7, corner indices modulo3. Fix any of the six pi(t)=u*t+v, u!=0 on F3. The ACTUAL classical Latin resolution is

    M(r,c)=r+mu_(c-r),
    mu=(1,0,6,5,infinity_2,infinity_1,infinity_0),
    M(r,infinity_beta)=r+(2,3,4)_beta,
    M(infinity_alpha,c)=c+(3,5,0)_alpha,
    M(infinity_alpha,infinity_beta)=infinity_(pi(alpha+beta)).

An infinity entry in mu is not translated by r. These formulas specify every cell. The pinned seed L has ell=(1,infinity_0,infinity_1,infinity_2,2,4,6), top border(3,5,0), bottom border(2,3,4), and corner L=infinity_(beta-alpha). Its complete Latin/orthogonality proof is in v2§2: the finite differences cover all seven ordinary differences; offsets1–3 give infinity/ordinary,4–6 ordinary/infinity, and the sum/difference corner map is invertible over F3. Thus the resolution is a real order10 input, not an unvalidated numerical table or an unknown third MOLS.

Let T be unitary with T^7=I. Consider projectively equivariant arrays. By choosing phases along each free7-cell orbit we can write them EXACTLY as

    q_(r,c)=T^r v_(c-r),
    q_(r,infinity_beta)=T^r a_beta,
    q_(infinity_alpha,c)=T^c b_alpha,
    q_(infinity_alpha,infinity_beta)=w_(alpha,beta).      (1)

Every fixed-corner w is a T eigenray. Projective equivariance is an ANSATZ, not a consequence of the original problem. No positivity of an off-classical chart or smallness is imposed.

Let zeta=exp(2*pi*i/7), and let E_k be the zeta^k eigenspace, dimension m_k. P_k denotes its orthogonal projector.

## 3. Exact30-context reduction

All seven ordinary rows are ONBs iff

    A=[v_0,v_1,v_2,v_3,v_4,v_5,v_6,a_0,a_1,a_2]

is unitary. All seven ordinary columns are ONBs iff

    B=[v_0,T^-1 v_1,T^-2 v_2,T^-3 v_3,
       T^-4 v_4,T^-5 v_5,T^-6 v_6,b_0,b_1,b_2]

is unitary: an ordinary column c factors out the common T^c. All seven ordinary-M classes are ONBs iff

    C=[T^-1 v_0,v_1,T^-6 v_2,T^-5 v_3,
       T^-2 a_0,T^-3 a_1,T^-4 a_2,
       T^-3 b_0,T^-5 b_1,b_2]                         (2)

is unitary: factor out T^m at ordinary label m. In particular the four core exponents are mu_d=1-d for d=0,1,2,3. The other SIX entries of C are the ACTUAL top/bottom border occurrences, not freely selected streams.

The remaining nine contexts are:

- row infinity_alpha: the7-orbit of b_alpha and its three corner-row rays;
- column infinity_beta: the7-orbit of a_beta and its three corner-column rays;
- M infinity_m: the7-orbit of v_(6-m) and the three corners with pi(alpha+beta)=m.

These account for21+9=30 contexts, with no missing ordinary or infinity resolution class. Equations(1),(2) never discard the other21 contexts when constructing the nine-context boundary.

## 4. Cyclic orbit lemma and the mandatory isotypic type

For a unit x, its orbit T^r x, r=0,...,6, is orthonormal iff

    ||P_k x||^2=1/7 for EVERY k in Z7.                 (3)

Indeed its Gram coefficients are <x,T^s x>=sum_k zeta^(ks)||P_k x||^2. Discrete Fourier inversion of delta_(s,0) gives(3), in both directions. Thus every character occurs. The orbit spans the direct sum of the SEVEN lines C P_k x; its complement is the direct sum of E_k minus that line, of dimensions m_k-1.

Apply this to the nine representatives a_beta,b_alpha,v_4,v_5,v_6. A simple eigenspace m_k=1 cannot contain a corner ray: every one of the corresponding completed special orbits already spans that whole eigenspace. Thus every corner ray lies in E_extra, the sum of eigenspaces of dimension>=2.

The corner orthogonality graph is EXACTLY K_(3,3,3), partitioned by j=beta-alpha. Proof: different j in the same row/column are adjacent. If both coordinate differences are nonzero and their difference is nonzero in F3, they are opposites, so their sum is zero; these cells then share the same pi(alpha+beta). Same-j different cells share none of those three contexts. Hence the three j-class spans are mutually orthogonal.

If all9 corners are distinct, each class of3 rays has span dimension>=2. Therefore dim E_extra>=6. But all seven characters are present and the excess dimension is3. Its three possible partitions are:

    excess3:       multiplicities4,1,1,1,1,1,1;    dim E_extra=4;
    excess2+1:     multiplicities3,2,1,1,1,1,1;    dim E_extra=5;
    excess1+1+1:   multiplicities2,2,2,1,1,1,1;    dim E_extra=6.

Only the last survives. Each j-class now has span EXACTLY2. It is T-invariant, because it is spanned by eigenrays. A2-space split over two distinct eigenvalues contains only two eigenlines, not three distinct eigenrays. Thus the whole j-class lies in ONE doubled eigenspace E_(k_j), and the three classes use the three distinct doubled characters. This proves the necessity completely; it is not an assumed assignment of corner colors.

In particular the usual representation fixing all three infinity axes has only a four-dimensional repeated eigenspace and CANNOT reach full100 inside projective equivariance. This does not constrain nonsymmetric arrays.

## 5. Explicit nine-context boundary with72 distinct rays

Choose any three different characters k_0,k_1,k_2 and doubled spaces E_(k_j)=C2, with four other one-dimensional characters. In each E_(k_j), choose THREE distinct unit rays w_(j,beta), beta in F3. An explicit algebraic choice is

    w_(j,0)=(1,0), w_(j,1)=(0,1),
    w_(j,2)=(1,1)/sqrt(2).

Different j spaces are orthogonal. Set the actual corner q_(infinity_alpha,infinity_beta)=w_(beta-alpha,beta). Choose any unit vector u_(j,beta) on the orthogonal complement line to w_(j,beta) in its C2.

For each of the nine special representatives x, choose its projection line in E_(k_j) according to

    f_a_beta(j)=beta,
    f_b_alpha(j)=alpha+j,
    f_v_(6-m)(j)=(pi^-1(m)+j)/2.                     (4)

Give that projection norm1/sqrt(7), times an arbitrary unit complex coefficient. Give its projection into each singleton character norm1/sqrt(7), again retaining its arbitrary unit complex coefficient. This specifies actual unit vectors, not only scalar norm lists. Its doubled projection is on u_(j,f_x(j)); its seven nonzero character weights satisfy(3).

For a special corner row/column/resolution, the orbit complement in every doubled character is precisely the ACTUAL corner ray that occurs there by(4). The three corner eigenrays are mutually orthogonal. Therefore all nine special contexts are EXACT10-dimensional ONBs, simultaneously and at finite amplitude. All63 phase coefficients are retained as actual common data for the remaining constraints.

There are exactly72 DISTINCT projective rays in this boundary:

1. Every special7-orbit is projectively free because it has all seven nonzero character projections.
2. The nine triples f_x are all affine functions j->A+B*j over F3, with slopes0,1,2 and all three intercepts. Distinct affine functions disagree in at least two coordinates. The corresponding projection lines in a doubled character are different, so no two different orbit representatives can be related by a global phase or ANY T shift. T shifts are scalar on each eigenspace and cannot change those lines.
3. The nine corners are distinct by construction. They are eigenrays and cannot coincide with a vector having all seven character projections.

Thus9*7+9=72 is an exact count, not an enumeration or numerical observation.

**Critical boundary:** these are the72 cells in the union of the nine special contexts. They have NOT yet been made orthogonal in every ordinary row/column/M class. This is a nine-context configuration, NOT an alleged partial-Latin or100-ray witness. The unused28 core cells and the full remaining ordinary constraints are retained next.

## 6. The full finite-amplitude core interface

Let the three boundary-six-frames be

    A_s=[v_4,v_5,v_6,a_0,a_1,a_2],
    B_s=[T^-4 v_4,T^-5 v_5,T^-6 v_6,b_0,b_1,b_2],
    C_s=[T^-2 a_0,T^-3 a_1,T^-4 a_2,
         T^-3 b_0,T^-5 b_1,b_2].

First ALL three must satisfy X_s^* X_s=I6. This is not automatic from§5. Once they do, put H_A=range(A_s)^perp, and similarly H_B,H_C, all dimension4. Every core vector v_d, d=0,...,3, must lie in

    H_A intersect T^d H_B intersect T^(1-d) H_C.        (5)

Equivalently it is in the kernel of the ACTUAL stacked18-by10 matrix

    [ A_s^* ; B_s^* T^-d ; C_s^* T^-(1-d) ].           (6)

No independently chosen complement line or phase can replace this intersection. The four vectors must also have unit norm and satisfy ALL THREE Gram conditions

    <v_d,v_e>=delta_de,
    <T^-d v_d,T^-e v_e>=delta_de,
    <T^-(1-d) v_d,T^-(1-e) v_e>=delta_de.              (7)

Equations(3)–(7) plus the actual corner/complement incidences are NECESSARY AND SUFFICIENT for all30 ONBs in the equivariant family. Sufficiency follows by the explicit context factorization§3 and the orbit lemma, not an unproved local integration step. This is an exact finite-amplitude interface with shared vectors and phases.

For full100, additionally require the four core7-orbits to be projectively free, no core orbit to coincide with another core or boundary orbit, and no core ray to coincide with a corner eigenray. A noncorner vector with at least two distinct character components has a free7-orbit and is not an eigenray. The remaining orbit-separation inequalities can be written

    |<x,T^r y>|<1

for every different type x,y and r=0,...,6, together with the within-core-orbit inequalities at r!=0. Boundary/boundary and boundary/corner separation were already proved in§5, not assumed. These inequalities and(5)–(7) are the exact current unsolved root problem. A separating tangent is not substituted for them.

## 7. New nonlinear theorem: a monomial simple-character core cannot work

This is a genuine finite-amplitude obstruction to an attractive shortcut in(5), not a claim that the general core has been solved.

**Theorem.** Suppose a full30-ONB completion of a§5 boundary with all9 corner rays distinct exists. Its4-by4 matrix of core coordinates in the four SINGLETON character spaces cannot be monomial: it cannot place each v_d on one different singleton character, with all its other singleton coordinates zero.

**Proof.** Every row A contains six boundary vectors with each character norm squared1/7. Taking the trace of the row-basis identity on a singleton gives total core weight1/7 there. Under the monomial hypothesis each core vector therefore has singleton weight1/7 in its own character kappa_d, and doubled-character weight6/7 in total.

For d!=e put g_j=<P_(k_j)v_d,P_(k_j)v_e>. Their singleton cross-terms are zero. The row, column and M Gram identities(7) give

    sum_j g_j=sum_j z_j g_j=sum_j z_j^-1 g_j=0,
    z_j=zeta^[k_j(d-e)].

The z_j are distinct because7 is prime, k_j are distinct, and0<|d-e|<7. Multiplying the j-th column by z_j turns the coefficient matrix into a three-point Vandermonde matrix with exponents0,1,2. It is invertible. Hence ALL g_j=0. At each doubled character the four core projections are pairwise orthogonal, so at most two are nonzero.

Let S_j=sum_beta |u_(j,beta)><u_(j,beta)|. Each group of three boundary representatives a_beta or v_(6-m) uses each of the three lines once. Therefore the row-basis identity compressed to E_(k_j) gives the ACTUAL core compression

    K_j=I2-(2/7)S_j,    trace K_j=8/7.                (8)

Because the three lines are distinct, S_j is positive definite and has both eigenvalues strictly between0 and3. Consequently K_j is positive definite, with eigenvalues strictly between1/7 and1. Thus exactly TWO orthogonal core projections occur in this doubled character.

Represent it by an edge joining their two core labels. Three doubled characters give three edges on the four core labels, allowing multiplicities initially. Every vertex has total incident norm weight6/7, and each edge has endpoint-weight sum8/7. For any connected component with m vertices and e edges,

    6m=8e, i.e. 3m=4e.

There are four vertices, three edges, and no isolated vertex. Integer counting forces the whole graph to be connected with m4,e3. It is a tree and has a leaf d. That leaf core vector has nonzero components in only TWO characters: its singleton kappa_d and one doubled k_j.

Choose ANY boundary v_e with e=4,5,6. Its singleton component in kappa_d is nonzero by(3). Let A0 and B0 be its inner-product contributions with v_d in those two characters; A0!=0. Row orthogonality gives A0+B0=0. Column orthogonality gives

    zeta^[kappa_d(d-e)] A0+zeta^[k_j(d-e)] B0=0.

Substitution forces zeta^[(kappa_d-k_j)(d-e)]=1, impossible: the characters are different and d-e is nonzero modulo7. This contradiction completes the proof.

This restriction is NOT a gauge normalization: an arbitrary unitary mixing the four core columns changes their different individual d and1-d shifts in(5)–(7). One must retain the genuinely nonmonomial simple-character data instead of diagonalizing it away.

## 8. Operator-valued moment version of the remaining mixed core

For a general core define V_k=[P_k v_0,...,P_k v_3] and G_k=V_k^* V_k. These ACTUAL matrices are positive semidefinite with rank<=m_k. Put D_k=diag(1,zeta^k,zeta^(2k),zeta^(3k)). The three core Gram conditions are precisely

    sum_k G_k=I4,
    sum_k D_k G_k D_k^*=I4,
    sum_k D_k^* G_k D_k=I4.                           (9)

The traces are1/7 at each singleton and8/7 at each doubled character. The doubled spectra are those of(8). These are coupled operator moments, not four independently optimized scalar kernels. They do NOT replace the boundary/core orthogonality(5),(6), phase matching or projective separation conditions. A positive solution of only(9) is not a completed array.

The theorem§7 says the singleton coordinate matrix cannot be monomial. No general diagonalization, symmetry of the four core labels, rank-one-singleton ansatz, or all-P/RT restriction is assumed. The genuine remaining attack is the nonmonomial solution of(3)–(7), or a different component/seed if that exact problem is obstructed.

## 9. Source intake and exact remaining scientific gap

The Lam cyclic board is used only through its literal formulas and the independent Latin/orthogonality proof; the displayed bad equal-type corner is not imported. A second primary literal input was located in Delisle's2010 thesis, Figure3.1 at printed49/PDF56, source `https://dspace.library.uvic.ca/server/api/core/bitstreams/1e81a938-7216-4045-9f30-2c4400d54b3f/content`. Its PDF reader extraction failed, so the table was rendered visually in the browser. No new table was machine-checked, no classification was replayed, and that second table is not a correctness premise of§§3–8.

The new source `https://arxiv.org/html/2609.29070v1` was checked at its actual construction hypotheses: its full-rank-factorization theorem does not supply order10 or a maximal square with a classical mate. A maximal ordinary QLS10, an entangled AME10 state or two non-classical quantum mates would not substitute for the present fixed-classical-resolution target. No novelty clearance is claimed for cyclic-orbit/Fourier/Naimark methods.

**First real remaining gap:** an ACTUAL common choice of the nine corner lines, the63 actual character phases and the four complex core vectors satisfying the three boundary6-frame constraints, the simultaneous intersections(5), all three Gram equations(7), and ALL100-ray separations. No such point/curve is supplied. The72-ray boundary is not the completed target, the monomial-core theorem does not exclude a general core, and neither excludes unrestricted maximal1-RQLS10.

The primary remains ACTIVE at this exact finite-amplitude gap. Original cutoff/deadline and HOLD are unchanged. No executable/kernel/formal/configured-family/human/novelty gate has been met, no numerical or global nonexistence promotion occurred, and no source or prior pinned record was edited.
