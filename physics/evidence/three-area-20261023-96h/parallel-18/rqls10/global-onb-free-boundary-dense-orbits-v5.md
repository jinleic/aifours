# RQLS10 — consolidated free-boundary dense-orbit continuation

Owner PhysicsRQLS10-2. Actual clock observed before this consolidation: `Sun Oct 25 14:22:12 PDT 2026`.

**WRITTEN CANDIDATE; no independent acceptance or scientific execution.** All new arguments are written finite-field, unitary and cyclotomic mathematics. No scientific interpreter/eval/program, enumeration, solver, symbolic program or replay was used for these mathematical claims. Earlier browser/eval calls were source rendering/navigation only; metadata clocks, hashes and LF counts are not scientific verification. No blanket clean-history assertion is made. V9/v10/v11 and HOLD remain binding. The original target, cutoff and deadline are unchanged.

## 1. Exact current target, predecessor boundaries and consequential change

The target remains an ACTUAL maximal1-RQLS10: every row, column and one designated transversal resolution is an ONB of C10, and every one of its100 projective rays is different. **No such completed matrix or array is supplied here.** The exact remaining finite-amplitude problem is stated below without dropping a context, fixing an independent stream, or treating a signature as integration.

The v2/v3/v4 sources remain immutable. In particular `global-onb-asymmetric-nine-to-ten-v4.md`,178LF, SHA256 `ddbfd185e9886fc738ad09e713b5a5b2f53a1a1d883e8f1b0c016d3e2051da1b`, contains the earlier selected ternary-theta28-ray partial configuration; its character-support wording addendum includes the trivial character whenever its vector projection is nonzero. That selected eight-core problem is unsolved. The pending v2 local statements, v3 nine-context72-ray boundary, all older RT/all-P gates and the unadmitted236/52 census are NOT accepted by this successor and are not correctness premises of its new proofs.

The present change is substantive: free the boundary entirely, normalize the ACTUAL special-row ONB, and reduce the entire covariant problem to ONE arbitrary complex10x10 unitary with TWO full diagonal orbit systems. Then supply a different literal ninth-root boundary whose two normalized special columns have no unforced zeros. Finally prove that any full orbit solution with precisely the forced zero pattern would AUTOMATICALLY have100 distinct rays. The remaining unitary closure is still unproved, not hidden behind these reductions.

No connection of every nonclassical component to a classical seed is assumed. The chosen resolution is an actual Latin square, but the representation considered below need not have a covariant classical point. A positive solution in this family would settle the existential target; a negative result here alone would not settle unrestricted RQLS10.

## 2. Actual classical resolution and its matching structure

Use G=F3^2, with additive notation and a fixed nondegenerate dot pairing; equivalently it is the additive group of F9 after choosing dual coordinates. Let X=G disjoint-union{infinity}. Define M by

    M(r,c)=-r-c when r,c in G and r!=c,
    M(r,r)=infinity,
    M(r,infinity)=r,
    M(infinity,c)=c,
    M(infinity,infinity)=infinity.                    (1)

M is Latin: in row r the removed diagonal value of -r-c is -2r=r; the new border restores exactly r, while infinity occupies that diagonal. Columns are identical by symmetry. The infinity row and column contain every ordinary symbol once and infinity once. Thus every M-symbol fiber is a genuine transversal on all100 cells.

Let P_r translate ordinary computational rays by r and fix e_infinity. Let S_0 exchange0 and infinity, and send each nonzero c to -c. Then

    S_r=P_r S_0 P_-r                                (2)

is exactly the involution taking an M label to its column in ordinary row r. In particular S_r exchanges r with infinity and pairs the other eight ordinary labels by c with -r-c. These nine matchings partition ALL45 unordered pairs of distinct elements of X.

For completeness, a finite pair{c,m} determines its matching row uniquely as r=-c-m; for an infinity pair{infinity,c}, the row is c. Each matching has five pairs. No guessed numerical Latin table is required.

## 3. Exact free-boundary normalization and unitary master variable

Start with the honest G-translation-covariant family; this is an ANSATZ, not a WLOG assertion about every RQLS10. Before normalization write the special row as {T_c b:c in G} together with its corner w, an ONB. Choose one common unitary sending that ONB to {e_c:c in G} together with e_infinity. The translation action then becomes EXACTLY P_r, since it permutes those nine basis rays regularly. Phases can be chosen along each regular orbit; the corner character is gauged to1. No scientific computation or local approximation is involved.

Let U be the normalized ordinary row0 basis matrix. Every ordinary row must be

    U_r=P_r U P_-r,    r in G,                       (3)

while the infinity row is I10. The candidate array is therefore completely explicit conditional on U:

    q_(r,c)=U_r e_c,
    q_(infinity,c)=e_c.                              (4)

Here U may be ANY complex matrix satisfying the equations below. No conference class, equal magnitude, real form, independent D/E normalization, selected theta or field for its unknown entries is assumed.

## 4. Necessary AND sufficient equations for all30 ONBs

Every ordinary row is an ONB iff U is unitary. Column c contains e_c and the nine U_r e_c. Orthogonality to the first vector gives diag(U)=0, transported by conjugacy to every r. Orthogonality between ordinary rows reduces, by(3), to every nonzero difference g=s-r:

    diag(U* P_g U P_-g)=0 for EVERY g!=0.             (5)

The star means Hermitian adjoint. Each of the TEN diagonal entries must vanish; a scalar trace identity is not equivalent to(5).

For the M fibers, reorder ordinary row r by S_r. Equations(2),(3) give

    U_r S_r=P_r(U S_0)P_-r.

The infinity row is still I in the M labeling. Hence the entire second system is

    diag(U S_0)=0,
    diag(S_0 U* P_g U S_0 P_-g)=0 for EVERY g!=0.      (6)

Together,

    U*U=I10, diag(U)=0, and(5),(6)                   (MASTER)

are NECESSARY AND SUFFICIENT for every row, column and M fiber of(4) to be an ONB. Row unitarity is built into U and its conjugates. Each column and each M fiber then consists of ten unit vectors with every pair orthogonal, including its first-row vector; so no additional completion step is missing. This accounts for10+10+10=30 contexts.

The two zero-diagonal conditions mean exactly that U has five zero2x2 diagonal blocks under the S_0 pairing. Both columns of a matching pair have zero entries at BOTH endpoints. Off-block entries remain arbitrary complex unknowns.

An arbitrary unitary with this zero pattern is NOT automatically a solution. Ten Hilbert-Schmidt-orthogonal unitaries are also not enough: (5),(6) require full diagonals. No multiplication-algebra closure of the U_r is assumed or inferred.

## 5. Automatic100-ray separation from the full allowed support

**Sufficient-support theorem.** If an actual solution of(MASTER) has nonzero entries at EACH of the80 positions outside its five zero2x2 blocks, then(4) has ALL100 rays distinct.

**Proof.** Conjugation transports its column support to the two forced zeros

    {c,M(r,c)}

in every nonfirst-row cell. They are exactly those zeros, not a chosen subset. Distinct zero pairs give different projective supports. By§2 every unordered pair occurs in only one ordinary row. The two cells of that pair in the row are orthogonal columns of U_r, so they give two different rays even though their zero pairs coincide. This yields45*2=90 different support-eight rays. None equals a first-row computational axis, whose support has size1. Together with the ten different axes this is100. The proof is exact, not a sampled distinction test.

This is a SUFFICIENT OPEN CONDITION, not a WLOG assertion that every possible maximalRQLS10 has support eight. If a proposed U has extra zeros, it must instead retain all explicit nonparallelity conditions |(U_r*U_s)_(c,d)|<1 for different cells, including comparisons |(U_r)_(k,c)|<1 with first-row axes. A support theorem is not evidence that a(MASTER) solution exists.

## 6. A new literal ninth-root boundary, without a ternary-theta restriction

The earlier field9 auxiliary input is no longer imposed. List t=(x,y) in G by x+3y, and let the following be an INTEGER permutation modulo9:

    mu=(0,2,3,6,1,4,7,5,8).                          (7)

Let zeta=exp(2*pi*i/9), omega=zeta^3, lambda(t)=zeta^mu(t). In C9 put

    v0=(1/3) sum_t |t>,
    a =(1/3) sum_t lambda(t)|t>,
    b =(1/3) sum_t lambda(t)^2|t>.                    (8)

All three are ACTUAL unit vectors. Since mu is a permutation, their pairwise inner products are the zero ninth-root sums at exponent differences1 and2. Let T_g multiply coordinate t by omega^(g.t), and fix an extra orthogonal w. Each vector in(8) is flat on all nine T characters, so its nine translates are an ONB of C9.

For the resolution(1), assign

    q_(r,r)=T_r v0,
    q_(r,infinity)=T_r a,
    q_(infinity,c)=T_c b,
    q_corner=w.                                     (9)

The three special contexts are complete ONBs. In every ordinary row, column and M fiber the already assigned pair is respectively a translate of(v0,a),(v0,b),(a,b); each is orthogonal. Thus(9) is a genuine28-cell partial configuration satisfying every already-applicable context constraint, NOT merely three unrelated bases.

The27 orbit rays are distinct. Equality between two different orbit types would make lambda(t)^k times a cubic character constant for k in{+/-1,+/-2}. Cubing removes the character and makes omega^(k mu(t)) constant, impossible because mu mod3 takes all3 values. Within an orbit the vectors are already orthonormal. The cornerw is orthogonal to all of C9. Hence the28-ray count is exact. No72 missing cells or27 ordinary ONBs are being declared complete.

## 7. Dense cross-correlation theorem: no extra special-column zeros

The mod3 fibers of(7) are

    S0={0,2,3}, S1={4,5,6}, S2={1,7,8}.

Their point sums in F3^2 are

    s0=(2,1), s1=(0,1), s2=(1,1),                   (10)

which span the whole plane. This deliberately uses three NONCOLLINEAR fiber triples rather than an affine digit partition.

For k in{+/-1,+/-2} and a cubic linear form ell, consider

    C_(k,ell)=sum_t zeta^[k mu(t)+3ell(t)].            (11)

**Theorem.** C_(k,ell)=0 iff ell=0.

**Proof.** Reduce the exponents modulo9 and form their integer count polynomial of degree<=8. A zero at zeta forces divisibility by the irreducible polynomial

    Phi9(X)=X^6+X^3+1.

Its quotient has degree<=2. Therefore the three counts in each residue class modulo3 must be equal. There are already exactly three terms in each such residue class, since k is a unit modulo9 and mu is a permutation. Each of its three lifted residues must consequently occur exactly once.

On a fixed fiber of mu mod3, write mu=r+3n with n a permutation0,1,2. Multiplication by k adds only a constant carry to k*n modulo3. Its sum is still0 modulo3. The required new high-digit permutation after adding ell thus forces

    ell(sum_(t in S_r) t)=0

for every r. By(10), ell=0. Conversely when ell=0, k mu permutes the nine integer residues, so the geometric sum is zero. This proves both directions, including the ending case.

Now normalize the special b-orbit and w to the computational basis as in§3. The coordinate c of a is <T_c b,a>, proportional to(11) with k=-1; the coordinate c of v0 uses k=-2. At c=0 these are the required zero inner products. At every other c they are NONZERO by the theorem. Their w coordinates vanish. Thus the two known columns U e_infinity and U e_0 have EXACTLY their two forced zeros and all eight allowed coordinates nonzero.

This new positive boundary avoids the additional cross-orbit zeros of the selected ternary-theta slice. Ninth roots here are not confused with field-F9 arithmetic or with a new scientific interpreter check. The unknown core entries remain arbitrary complex numbers, not constrained to ninth roots.

## 8. Exact remaining common root problem

One may normalize(9) and use its two dense known columns as literal input to(MASTER), or keep those columns free and solve the entire arbitrary-U problem. Either route still requires ONE ACTUAL U satisfying BOTH full diagonal orbit systems, unitarity and all distinctions.

In the equivalent unnormalized eight-core form, the missing vectors v_d, d!=0, must satisfy simultaneously

    [(v_d)_(d in G),a] unitary,
    [(T_-d v_d)_(d in G),b] unitary,
    [(T_d v_d)_(d!=0),a,b] unitary.                   (12)

Every v_d must lie in the common orthogonal complement of

    {v0,a,T_d v0,T_d b,T_-d a,T_-d b},                (13)

with its corner coordinate retained. These kernels have dimension at least4, but independent choices of kernel vectors do NOT solve(12). All mixed complex Gram conditions remain. A real form, diagonal/simple-character core, commuting transport, equal-modulus conference profile, product-vector factorization or D-triality is NOT imposed.

The first real gap is an actual common root of(MASTER), or equivalently(12), with the dense support or explicit100-ray distinctions. The two dense columns and the automatic-separation theorem solve neither the row completion nor the coupled column/M completion.

## 9. Assurance, provenance and nonclaims

The literal M and all new boundary/cyclotomic proofs are given above. Standard first-row/unitary-pattern normalization and character Fourier methods are known frameworks; relevant prior context includes Ball–Simoens `https://arxiv.org/html/2603.02334v1`, Zhang–Cao `https://arxiv.org/html/2608.29201v2`, and Reutter–Vicary, *Biunitary constructions in quantum information*, Corollary3.2.1. No novelty clearance is asserted for a construction framework, and no unread source ancestry is certified from a citation.

The current Zhang–Cao statement still leaves10 among its17 possible maximal1-RQLS exceptions. A maximal ordinary QLS10 without a resolution, an auxiliary81-ray order9 array, an entangled-officer/AME construction, the v3 nine-context72-ray boundary, or a no-go for any selected symmetry class is not this target.

Every predecessor and parent record stays unchanged. The two explicitly recorded over30-minute checkpoint intervals remain disclosed; later clocks are not backdated into compliant checkpoints. No computational/model-family/human/formal/kernel/novelty gate, publication, numerical promotion, scientific GO or deadline reset is conferred.

**Primary status: ACTIVE, exact full-support complex unitary root missing.** This is the consolidated parkable mathematical interface and literal positive boundary, not a declaration of completion. No full100-ray RQLS10 or unrestricted no-go has been established.
