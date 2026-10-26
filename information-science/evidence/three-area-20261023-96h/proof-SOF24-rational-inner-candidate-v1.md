# P24 candidate: a non-Hermitian kernel from a rational inner curve

Before-creation clock observed: **2026-10-23T13:54:22-07:00**. **HIGH-RISK CANDIDATE / NOVELTY_UNCLEAR. Written reasoning only.** This is a materially different kernel class from the primitive-Hermitian route excluded in the previous manuscript. It has not received independent reconstruction, executable verification or formal acceptance. If the construction and robustness bridge below are correct, they would give a negative answer to P24. Do not report that conclusion as established before the full checks return.

No scientific program, coefficient-rank calculation, solver, enumeration or symbolic-algebra execution was used. Every coefficient check below is hand algebra. Earlier parent verification/timestamp errata remain operative. No external contact/publication is authorized.

## 1. Proposed conclusion and exact remaining verification burden

P24 asks whether the set of SOF-stabilizable triples with eight states, four inputs and two outputs is dense. This manuscript proposes a rational polynomial recipe for an eight-state minimal plant with a nonempty open neighborhood of SOF-unstabilizable plants.

The central ingredients requiring especially hostile checking are:

1. eight independent Hermitian functions of the explicit degree-four inner pair;
2. the real decomposable-point exclusion for the kernel `anti-J forms + R diag(1,1,-1)`;
3. the separate exact omission of the pure power z^8, including the Fourier coefficient arithmetic;
4. the Cayley/root-disk argument and continuous ordinary-plant binding.

The base curve is deliberately **complex-degenerate but real-basepoint-free**. No claim that it itself satisfies complex non-degeneracy is made. The robust open-neighborhood argument aims to prove P24 directly, without substituting a nongeneric hidden-mode example. A separate argument at the end explains why such an open neighborhood, if proved, also contains complex-nondegenerate plants. This is a change of proof route within P24, not permission to drop the open-family obligation.

## 2. An explicit polynomial inner pair on the circle

Let r=3/5, s=4/5 and |t|=1. Define

    f_1(t)=(t+t^2)/2,  f_2(t)=(1-t)/2,
    p(t)=t^2(r f_1(t)+i s f_2(t)),
    q(t)=t(i s f_1(t)+r f_2(t)).                            (1)

The identity |f_1|^2+|f_2|^2=1 follows from |1+t|^2+|1-t|^2=4 on the unit circle. The constant matrix [[r,is],[is,r]] is unitary, and multiplication of either coordinate by a power of t preserves its modulus. Therefore

    |p(t)|^2+|q(t)|^2=1.                                   (2)

Expanded exactly,

    p(t)=[4i t^2+(3-4i)t^3+3t^4]/10,
    q(t)=[3t+(-3+4i)t^2+4i t^3]/10.                       (3)

This is not a sampled norm identity; (1) proves it on the entire circle.

## 3. The eight Hermitian functions are independent

Consider a real-valued identity on the circle of the form

    h+d |p|^2+a p bar(q)+bar(a)bar(p)q
       +b p+bar(b)bar(p)+c q+bar(c)bar(q)=0,               (4)

where h,d are real and a,b,c complex. These eight real degrees of freedom describe every Hermitian form in (p,q,1), modulo the known relation (2). We show all coefficients vanish.

The positive Fourier coefficient of order 4 is b r/2, so b=0. The coefficient of order 3 is

    a r^2/4+c i s/2=0,

hence c=i a r^2/(2s)=9i a/40. The coefficient of order 2 is

    -i d r s/4-i a r s/2+c(is-r)/2=0.

Substitution and r^2+s^2=1 give

    i d s+a[r+i(s+1/s)]=0,
    (12+41i)a=-16i d,
    a=(-656-192i)d/1825.                                  (5)

The order-1 coefficient, multiplied by 4, is

    d(r^2-s^2)-a+s^2 bar(a)+2r c=0.

Writing a=x+iy and taking its imaginary part yields

    27x-164y=0.

By (5), its left side is (13776/1825)d. Thus d=0, and then a=c=b=0. The constant coefficient gives h=0. This proves the required eight-function real linear independence.

For clarity, the Laurent coefficients used above are

    [t^3](p bar q)=r^2/4,
    [t^2](p bar q)=-i r s/2,
    [t](p bar q)=-1/4,
    [t^-1](p bar q)=s^2/4,
    [t^2]|p|^2=-i r s/4,
    [t]|p|^2=(r^2-s^2)/4.

The negative-frequency support of p bar q extends only to -1, so its conjugate contributes to positive order 1 but not orders 2 or 3. This support detail is load-bearing.

## 4. Converting to a real degree-eight polynomial row curve

Let n(z)=z+i and d_0(z)=z-i, and set

    P(z)=[4i n^2 d_0^2+(3-4i)n^3 d_0+3n^4]/10,
    Q(z)=[3n d_0^3+(-3+4i)n^2 d_0^2+4i n^3 d_0]/10,
    C(z)=d_0^4.                                           (6)

For real z, t=n/d_0 lies on the circle and (P,Q,C)=d_0^4(p(t),q(t),1). Define real polynomial rows

    v_R=(Re P,Im P,Re Q,Im Q,Re C,Im C),
    w_R=(-Im P,Re P,-Im Q,Re Q,-Im C,Re C),
    V_0=[v_R;w_R].                                        (7)

Re/Im in (7) mean coefficientwise real/imaginary parts, so every coefficient of V_0 is rational. Every row has degree 4. The leading complex vector is (r,is,1), whose underlying real vector and its J-rotation are independent; thus the maximum minor degree is 8.

The rows have full complex rank at every finite complex z. After a constant complex coordinate change, their span is equivalently generated by vectors supported on separate sectors `(P,Q,C)` and `(bar P,bar Q,bar C)`, where bars conjugate coefficients only. C vanishes only at z=i, where P(i)=24/5!=0. Similarly bar C vanishes only at z=-i, where bar P(-i)=24/5!=0. Thus neither sector vector ever vanishes, and the two rows are independent for every complex z. In particular their minors have gcd 1. This proves a degree-eight basepoint-free **row curve**; it does not yet prove non-degeneracy of the separate pole-placement map.

## 5. Its pole-placement kernel has no real decomposable point

Identify real bivectors in R^6=C^3 with their J-invariant Hermitian component and anti-J component. The real row wedge in (7), `v_R wedge Jv_R`, is J-invariant; its Hermitian matrix is a fixed nonzero normalization of

    v(z)v(z)^*,  v(z)=(P(z),Q(z),C(z)).

Equation (2) gives the exact polynomial identity

    |P(z)|^2+|Q(z)|^2-|C(z)|^2=0,                          (8)

where products again use coefficientwise conjugation and agree with ordinary absolute squares on real z.

The eight-function independence in Section 3, transported by the invertible circle-to-line change and the nonzero common denominator, shows that these Hermitian coefficient matrices span precisely the eight-dimensional hyperplane orthogonal to

    B=diag(1,1,-1).                                        (9)

Hence the kernel of the full nine-coefficient pole-polynomial linear map on real bivectors is exactly

    K = (six-dimensional anti-J two-form space) + R B.      (10)

The trace pairing and Euclidean real-bivector pairing differ only by a fixed nonzero normalization on the J-invariant sector; B in (10) means its associated real J-invariant two-form.

**Real decomposable exclusion.** If a nonzero real bivector is simple, write it as x wedge y for real-independent x,y, viewed as complex vectors. Its Hermitian component is

    H(x,y)=(i/2)(x y^*-y x^*),

of complex rank at most 2. It is nonzero: equality zero would force y to be a real multiple of x. An element of K has Hermitian component lambda B. For lambda!=0 that has rank 3, impossible for a simple bivector; for lambda=0 it has zero Hermitian component, also impossible. Thus K contains no nonzero real simple bivector.

The complementary Plucker coordinates of a real rank-4 plane L form a nonzero real simple bivector. Therefore

    det[V_0(z);L] is never the zero polynomial

for any real L. This is **real-basepoint-freeness of the compact pole-placement map**, despite complex base points. The map from the compact real Grassmannian to real projective degree-eight polynomials is consequently continuous everywhere.

This kernel class is different from trace-free-Hermitian subspaces in the preceding obstruction: it contains the anti-J sector and a full-rank indefinite Hermitian form B, rather than lying in a primitive-Hermitian sector.

## 6. The pure power z^8 is outside even the linear polynomial image

The target z^8, divided by |C(z)|^2=(z^2+1)^4 and transported to t, becomes

    T(t)=(t+1)^8/(256t^4).

Its positive Fourier coefficients g_4,g_3,g_2,g_1 are respectively

    1/256, 1/32, 7/64, 7/32.                               (11)

Suppose T belonged to the real span of the eight functions in (4), with right side T rather than zero. The same coefficient comparison gives:

- order 4: b=5/384, real;
- order 3:

      c=9i a/40+c_0, c_0=(20-105i)/1536;

- order 2:

      (12+41i)a=-16i d+(-6600+2375i)/576.

Thus, writing a=x+iy,

    x=x_0-656d/1825, y=y_0-192d/1825,
    x_0=18175/1051200>0,
    y_0=299100/1051200>0.                                  (12)

For an independently checkable intermediate anchor, the known b,c_0 terms in the order-2 coefficient sum to (72+95i)/3072, whereas g_2=336/3072.

The order-1 coefficient, multiplied by 400, is

    175/2=-28d+(-100+27i)a+64bar(a)+120c_0.

Its imaginary and real parts are

    27x-164y=525/64,
    -28d-36x-27y=1375/16.                                  (13)

Substituting (12), the first equation implies d>0, because

    (13776/1825)d=525/64+164y_0-27x_0>0.

The second implies d<0, because

    -(22300/1825)d=1375/16+36x_0+27y_0>0.

This contradiction proves z^8 is not in the full linear image, and therefore no real rank-4 L has det[V_0;L]=c z^8 with c!=0.

The argument is symbolic for the exact rational coefficients, not an unperformed rank claim or finite set of point evaluations.

## 7. An exact rational root-disk exclusion radius

This step makes the small-radius choice a closed rational recipe, not an unspecified numerical tolerance.

Let f_1,...,f_8 be the following real polynomials, all of degree <=8:

    C bar C, P bar P,
    Re(P bar Q), Im(P bar Q),
    Re(P bar C), Im(P bar C),
    Re(Q bar C), Im(Q bar C).                               (14)

Let F be their 9x8 coefficient matrix in ascending powers 1,z,...,z^8. Sections 3 and 6 prove that the 9x9 matrix [F,e_8] is invertible, where e_8 is the coefficient vector of z^8. Define the exact rational linear functional

    ell(phi)=det[F,coeff(phi)]/det[F,e_8].                  (15)

Then ell vanishes on the pole-polynomial image and ell(z^8)=1. Put lambda_j=ell(z^j), j=0,...,7, and define the explicit positive rational number

    S=sum_(j=0)^7 |lambda_j| binom(8,j),
    rho=1/[2(1+S)].                                       (16)

This is a finite determinant formula for rational coefficients, not a call to a solver. No numerical evaluation of it is claimed here.

For any monic degree-eight polynomial phi with all roots in |z|<=rho, elementary symmetric-function bounds give

    |[z^j]phi|<=binom(8,j)rho^(8-j), j<8.

Since rho<=1/2, it follows that

    |ell(phi)-1|<=rho S<1/2.

Thus ell(phi)!=0: the whole closed root-disk family is excluded from the linear image of V_0.

## 8. Mapping all closed-left-half-plane spectra into that disk

Let

    z=R(s)=rho(s+1)/(s-1),
    V_tilde(s)=(s-1)^4 V_0(R(s)).                          (17)

Every entry is an explicit rational polynomial of degree <=4. The real fractional-linear map R sends the closed left half-plane on the Riemann sphere, including infinity, into the closed disk |z|<=rho; the exceptional inverse image of z=infinity is s=1, which is not in that half-plane.

For any real rank-4 L,

    det[V_tilde(s);L]=(s-1)^8 det[V_0(R(s));L].              (18)

If the nonzero polynomial on the left had all eight projective roots in the closed left half-plane, the original polynomial would have no root at z=infinity (that would produce s=1) and all eight roots in |z|<=rho. Normalize it to be monic. This contradicts Section 7 because it belongs to ell's kernel.

Thus the compact real pole-placement map of V_tilde avoids **every closed-left-half-plane projective root configuration**, not merely z^8. Real-basepoint-freeness is preserved by (17). The row curve remains basepoint-free over C, including s=1, because its value there is the nonzero leading row plane of V_0.

## 9. Explicit ordinary eight-state plant binding

Reorder V_tilde's columns so the C-coordinate pair comes first. The leading 2x2 block of that pair is

    D_lead=[[Re C(rho),Im C(rho)],
            [-Im C(rho),Re C(rho)]],

whose determinant is (rho^2+1)^4>0. Left-multiply by D_lead^(-1). Call the resulting first block D(s), and the remaining four columns N_raw(s). Then D is monic of degree 4. Let M be the degree-four coefficient of N_raw and set

    N(s)=N_raw(s)-D(s)M.

This constant real column operation is invertible and makes deg N<=3. All plane/root exclusion properties are preserved, because it only relabels real constant rank-4 planes L and scales the polynomial by a nonzero constant.

Write

    D=s^4 I_2+D_3s^3+D_2s^2+D_1s+D_0,
    N=N_3s^3+N_2s^2+N_1s+N_0.

Every coefficient is an explicitly defined rational number via (6),(14)–(17) and these finite inverses. Define the ordinary plant by 2x2 block notation:

    A=[[ -D_3, I_2, 0,   0 ],
       [ -D_2, 0,   I_2, 0 ],
       [ -D_1, 0,   0,   I_2 ],
       [ -D_0, 0,   0,   0 ]],
    B=col(N_3,N_2,N_1,N_0),
    C_out=[I_2,0,0,0].                                    (19)

Solving the block state equations gives C_out(sI-A)^(-1)B=D(s)^(-1)N(s). The characteristic polynomial is det D(s), and the determinant lemma gives, for every finite real 4x2 gain K,

    det(sI-A-BKC_out)=det(D(s)-N(s)K).                     (20)

This is det[V;K,I_4] in the appropriate block ordering/sign convention, or equivalently its complementary-plane form; a fixed sign/column permutation changes neither its roots nor the plane quantifier. Equation (20) can also be verified directly from the block equations, without assuming invertibility at each individual s.

The plant is observable: [C_out;C_out A;C_out A^2;C_out A^3] is block lower triangular with identity diagonal. It is controllable because a left eigenvector at lambda necessarily has blocks (lambda^3u,lambda^2u,lambda u,u); if it also annihilates B, then uD(lambda)=uN(lambda)=0. This contradicts full complex row rank of [D,N] at lambda. Hence (19) is a minimal **eight-state** plant, not an embedding with unobservable/uncontrollable unstable modes.

By Section 8 no gain K in (20) can make the matrix Hurwitz; indeed no closed-left-half-plane spectrum is possible even with generalized/infinite gain planes.

## 10. Robustness and generic consequence: proposed proof of non-density

The real Grassmannian of rank-4 planes is compact. Section 5 and (17) ensure the compact pole-placement map is well-defined everywhere for V_tilde. The set of real projective degree-eight polynomials whose projective roots lie in the closed left half-plane is compact: identify a polynomial with its conjugation-symmetric eight-point divisor on the Riemann sphere and use the closed compact hemisphere, including infinity. Section 8 proves these two compact sets are disjoint. Therefore a sufficiently small perturbation of the polynomial matrix retains real-basepoint-freeness and avoidance of that entire closed-half-plane set, by uniform continuity on the Grassmannian.

This is also an open condition in the ordinary plant space near (19), not merely an open set in a thin chosen polynomial ansatz. Here is the local-chart justification. The order-four observability matrix O=[C;CA;CA^2;CA^3] is invertible at (19), hence remains so nearby. The block coefficients D_j are recovered continuously from the unique recurrence expressing CA^4 in the row basis O. The corresponding observable companion coordinate change is block lower triangular relative to O and is invertible; it puts nearby plants in the form (19) with D_j,N_j depending continuously on the original A,B,C. Equivalently these identities follow by four successive output-derivative equations. Thus every sufficiently near ordinary triple yields a nearby polynomial matrix in the same monic chart. The compact avoidance persists there and excludes every real SOF gain.

Consequently, **if the preceding lemmas and chart argument stand**, there is a nonempty open set of ordinary minimal eight-state, four-input, two-output plants that no real constant feedback stabilizes. This is the proposed negative answer to P24, not merely omission of some unrelated spectrum.

The existence of complex-nondegenerate plants inside that open set follows from the standard algebraic openness/density of non-degeneracy at mp=n, as stated in the original Byrnes–Anderson manuscript and Eremenko–Gabrielov 2002. For a more explicit algebraic witness that the bad locus is proper in the monic chart, row-reduce the standard 2-row Wronski matrix (1,z,...,z^5;0,1,2z,...,5z^4) to row degrees 4,4, normalize its last two columns as D, and obtain

    D_W=[[z^4,0],[(4/5)z^3,z^4]],
    N_W=[[5,4z,3z^2,2z^3],
         [0,1/5,(2/5)z,(3/5)z^2]].                        (21)

Its complex pole map has no basepoint because the Wronskian of two independent characteristic-zero polynomials cannot vanish identically. Complex degeneracy is an algebraic closed condition: project the coefficient-vanishing incidence with the projective complex Grassmannian. Since (21) is outside it, the condition is proper and its complement is dense in the real coefficient chart. Thus the robust open family is not confined to a complex-degenerate subvariety.

This density step is not used to hide a missing real exclusion or state-dimension defect in the base plant. The exact root exclusion and minimality were proved before invoking it.

## 11. Check list and promotion boundary

This is a complete **candidate argument**, not a verified solution report. The following still require independent reconstruction before any promotion:

- every Laurent coefficient and the inhomogeneous contradiction in Sections 3/6;
- the normalization of real/J-invariant pairing, and proof that the kernel is exactly (10), rather than merely containing it;
- the coefficientwise bar convention and complex row-basepoint proof;
- the determinant-functional radius recipe and projective root transport;
- the ordinary companion realization, finite-gain dimensions, minimality and local open-chart argument;
- the complex non-degeneracy density statement at the declared source/import boundary;
- matched prior art. No claim of first, best-known, a publication-ready solution, or expert acceptance is made.

The rational determinant recipe is exact, but its numerical coefficients and a byte-level 8x8/8x4/2x8 witness have not been expanded or independently replayed. Any such executable verification needs a separate named scientific GO with pinned inputs and controls. None is authorized here. The completed surrogate stack remains delivered with its source/novelty gate; P33 is inactive. This new route must be rejected, repaired or accepted on its own mathematics, not on the appeal of the P24 conclusion.
