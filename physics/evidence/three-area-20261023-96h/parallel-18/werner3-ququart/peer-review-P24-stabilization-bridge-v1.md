# Independent written review: P24 root-disk to ordinary-plant robustness bridge

Before-creation clock observed: **2026-10-23T14:12:09-07:00**. Reviewer: PhysicsResearch96h, physics-1, temporarily cross-reviewing without taking P24 ownership. No author file was changed. No scientific program, coefficient evaluation, symbolic engine, solver, model CLI, nested agent or proof assistant was used.

## Snapshot, scope and verdict

Read the complete303-line source `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-SOF24-rational-inner-candidate-v1.md`, including the full untruncated local-chart paragraph. Observed SHA-256: **`267d717cd735537ff8c29a3c73a17ed7fb1f7939c85788a8cbd60374f74ab8a0`**.

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR. No substantiated defect found in the root-disk→Cayley→ordinary eight-state minimal real plant→whole-plant open-neighborhood bridge, at the explicit preceding algebraic premises.** The additional algebra checks below reconstruct those load-bearing preceding premises rather than substituting the false assertion that the base is complex-nondegenerate.

The mathematical argument supports the proposed non-density conclusion under the stated continuous-time real static-output-feedback model, **conditional on the full pinned construction as reconstructed here**. This is a high-risk in-harness written review, not parent promotion, human expert validation, a formal proof, executable witness replay or novelty clearance. The deliberate complex degeneracy of the base is not itself a defect: the proof uses compact **real** basepoint-freeness and proves the ordinary robustness bridge directly.

## 1. Preceding premises actually checked

### Real/rational curve and finite/projective row rank (Sections2–4)

The factorized p,q definition is an exact unitary mixing of the normalized f pair, with unimodular powers, so its circle norm identity holds identically. Expanding gives exactly the displayed degree-four/three coefficients.

Coefficientwise real/imaginary parts in V0 are real rational polynomials. Over complex coordinates, the two real rows split into disjoint sectors `(P,Q,C)` and `(bar P,bar Q,bar C)`. The first vector cannot vanish: C only vanishes at z=i and P(i)=24/5. The conjugate sector has the corresponding nonzero value at z=-i. Their disjoint supports imply complex row rank two at every finite z. The leading complex vector is `(3/5,4i/5,1)` and its conjugate sector is also nonzero, giving full leading row rank and minor degree eight. Hence the homogeneous row curve has no basepoint, including at infinity; its finite minors have gcd one.

### The rank-eight polynomial image and omitted pure power (Sections3,5–6)

I independently recovered the listed Laurent coefficients from the three terms of p and q: positive orders3,2,1 of p bar(q) are `r^2/4,-irs/2,-1/4`; its negative order1 coefficient is s^2/4. The positive orders2,1 of |p|^2 are `-irs/4,(r^2-s^2)/4`. Their support bounds are correct. In the homogeneous identity, the order4 equation forces b=0, the order3 equation gives c=9ia/40, the order2 equation is `(12+41i)a=-16id`, and the order1 imaginary equation is `27Re(a)-164Im(a)=0`. Their combination forces d=0, then a,b,c,h=0. This establishes the eight independent functions used as F's columns.

For the inhomogeneous pure-power test, the circle substitution gives exactly `(t+1)^8/(256t^4)` and the four stated positive coefficients. The forced values are b=5/384 and `c0=(20-105i)/1536`. The known order2 terms sum to `(72+95i)/3072`, yielding `(12+41i)a=-16id+(-6600+2375i)/576`. Division gives the stated positive x0,y0 and the d coefficients `-656/1825,-192/1825`. The two order1 real equations then force d to have opposite signs. These are symbolic coefficient identities, not consequences inferred from finite evaluations. Thus z8 is outside the full eight-dimensional linear image.

### Real basepoint-freeness, not complex non-degeneracy (Section5)

The J-invariant component of the simple real bivector x wedge y is the Hermitian matrix `(i/2)(xy*-yx*)`, up to the fixed normalization. It has complex rank at most two. If it vanished, multiplying the equality xy*=yx* by x shows y is a complex multiple of x, and substituting back makes that multiple real; hence the original real bivector would be zero. It cannot equal a nonzero multiple of rank-three `diag(1,1,-1)` either.

The eight independent Hermitian coefficient functions span the indicated codimension-one hyperplane, and the anti-J component pairs trivially with the row wedge. Thus the kernel contains no nonzero **real simple** bivector. Complementary Plucker coordinates of a real four-plane are real simple, so its pole polynomial is never zero. This is precisely the real compact-domain property needed later. No complex-nondegenerate theorem is applied to this complex-degenerate base.

## 2. Rational root-disk exclusion (Section7, lines191–217)

The eight column functions of F are independent and e8 is outside their span, so the determinant denominator in ell is nonzero. The determinant recipe gives a genuine rational functional annihilating the complete pole-polynomial linear image, with ell(z8)=1. It does not require a floating or numerical determinant evaluation.

For a monic degree-eight polynomial with all roots in |z|<=rho, the elementary-symmetric coefficient bound is `|a_j|<=binom(8,j)rho^(8-j)`. With `rho=1/[2(1+S)]<=1/2`, each positive power rho^(8-j) is at most rho. Consequently

`|ell(phi)-1|<=rho S=S/[2(1+S)]<1/2`.

Thus **the entire closed disk-root family**, not merely one pure power, is excluded from the image. No polynomial-identity conclusion is being drawn from testing sample roots.

## 3. Cayley transport, degrees and projective roots at infinity (Section8)

The real Mobius map `R(s)=rho(s+1)/(s-1)` obeys `|s+1|<=|s-1|` exactly when Re s<=0. It maps the closed left hemisphere of the Riemann sphere, including s=infinity, into |z|<=rho; infinity maps to z=rho. Its pole s=1 lies outside that hemisphere.

Homogenizing degree eight, equation(18) is the ordinary invertible Mobius substitution on binary forms. All eight roots, including infinity roots and multiplicities, are transported. An original root z=infinity maps to s=1; therefore a transformed polynomial whose eight projective roots all lie in the closed left hemisphere cannot have an original infinity root. The original is consequently degree eight and can be made monic; every original root lies in the forbidden z disk. This gives the exact contradiction to Section7.

An infinity root of the **transformed** polynomial is not omitted: it maps to the finite boundary point z=rho and is covered by the disk test. This is important for compactified, unbounded-gain limits.

Multiplication of each degree-four row by `(s-1)^4` is the correct homogeneous transformation. At s=1 the row values are the nonzero original leading row plane; at transformed infinity they are V0(rho). Hence neither is a row basepoint. The leading-row rank remains two. Real rank-four planes still have nonzero pole polynomials because the binary-form substitution is invertible, so real compact basepoint-freeness is preserved.

## 4. The D/N chart, finite real gains and left coprimeness (Section9)

After moving the C-coordinate pair first, its leading coefficient is the displayed real2×2 matrix with determinant |C(rho)|^2=(rho^2+1)^4>0. Left normalization therefore makes D monic degree four. Subtracting D times the degree-four coefficient M of N_raw makes N strictly proper in the polynomial sense, degree at most three.

This is right multiplication of [D,N_raw] by the fixed real invertible block matrix `[[I2,-M],[0,I4]]`. For any real four-plane, multiplying its row frame by the inverse relabels another real four-plane; the determinant changes only by a nonzero fixed factor. Thus the strong **all-plane** root exclusion survives. No assertion that this column change preserves each individual finite gain numerically is needed.

Full row rank of [D,N] at every finite complex lambda survives all these operations. It implies polynomial left coprimeness: a common nonunimodular square left divisor would have a determinant root and force row-rank loss there. At infinity its leading matrix is [I2,0], also full rank. This is a proper left-fraction chart, not a hidden-mode fraction with cancellations overlooked.

For every finite real4×2 K,

`det[[D,N],[K,I4]]=det(D-NK)`.

These graph planes have rank four and are a subset of the compact Grassmannian used by the exclusion. The argument does not confuse the finite gain chart with every generalized/infinite gain plane; it proves the stronger all-plane exclusion and then restricts to the finite chart.

## 5. Ordinary eight-state realization and PBH minimality

Solving the first three block equations of the displayed observable companion gives

`x2=(sI+D3)x1-N3u`,

`x3=(s^2I+sD3+D2)x1-(sN3+N2)u`,

`x4=(s^3I+s^2D3+sD2+D1)x1-(s^2N3+sN2+N1)u`.

The last equation is exactly D(s)x1=N(s)u. Therefore the transfer is D^-1N, with the left/right order correct even when the D coefficients do not commute. Elimination also gives det(sI-A)=det D(s). The determinant lemma over the rational function field yields equation(20), and hence a polynomial identity by continuation; it does not assume D invertible at each individual s.

The observability matrix has identity diagonal blocks and blocks only at or below that diagonal, so it is invertible. A nonzero left eigenvector must have blocks `(lambda^3u,lambda^2u,lambda u,u)`. Its first block equation is uD(lambda)=0; annihilating B is uN(lambda)=0. Here u cannot be zero unless the entire eigenvector is zero. Full row rank of [D,N] rules this out by PBH. Thus the constructed ordinary plant is controllable and observable with exactly eight states.

The dimensions are genuinely eight states, four inputs, two outputs. If full input column rank is demanded separately, real compact basepoint-freeness also forbids a constant null vector of N: such a vector would put every row of V in a fixed real hyperplane, and any real four-plane inside that hyperplane would give the forbidden zero determinant. In particular B cannot have a constant column null vector. This is not needed to manufacture minimality, which already follows by PBH.

Equation(20) and Section8 now exclude every Hurwitz closed-loop matrix, and even every closed-left-half-plane characteristic root divisor, for finite real gains.

## 6. Compact image avoidance and uniform nonzero normalization (Section10)

There is no need to choose a global continuous signed row frame over the real Grassmannian. One may use its compact Stiefel cover of orthonormal four-row frames. The norm of the nine polynomial coefficients of the determinant is a continuous positive function on that compact cover. Real basepoint-freeness therefore gives a uniform positive lower bound. This prevents normalized pole polynomials from disappearing under perturbation or under an escaping-gain limit.

The real projective degree-eight target set with all roots in the closed left hemisphere is compact: the symmetric product of eight copies of that compact hemisphere is compact, the conjugation-symmetric divisors form a closed subset, and the product-of-linear-factors/Vieta map to projective coefficient space is continuous. Degree drops are included by infinity roots. The base Grassmann image is compact and disjoint from this compact target, so their projective distance is positive.

Small perturbations of the polynomial coefficients change every determinant uniformly on the compact frame cover. Keeping the coefficient norm bounded away from zero makes the normalized projective images uniformly close. A sufficiently small perturbation therefore retains both real basepoint-freeness and target avoidance. This controls **all** gain planes, including limits of unbounded K, not just a bounded collection of finite gains.

## 7. Whole ordinary-plant neighborhood, with explicit continuous chart

The O=[C;CA;CA^2;CA^3] matrix is invertible at the base and in an ordinary open neighborhood. Recover the matrices D_j continuously from

`CA^4+D3 CA^3+D2 CA^2+D1 CA+D0 C=0`.

This is a unique row-basis expansion because O is invertible. For nearby A,B,C the numerator coefficients are explicitly continuous:

`N3=CB`,

`N2=CAB+D3 CB`,

`N1=CA^2B+D3 CAB+D2 CB`,

`N0=CA^3B+D3 CA^2B+D2 CAB+D1 CB`.

They give the same strict left fraction by polynomial division of the resolvent. In derivative coordinates O, the state matrix is the fourth-order row companion. Let O_D be the observability matrix of the displayed first-column companion constructed from these D_j; it is block lower triangular with identity diagonal. The change of state coordinates `x_can=O_D^-1 O x` is invertible and continuous, preserves the measured output as its first two coordinates, and puts A,B,C into exactly the canonical form(19), with the continuous D_j,N_j above. This supplies the noncommutative matrix-coefficient chart argument rather than merely asserting proximity of transfer functions.

Consequently **every sufficiently nearby ordinary triple** gives a nearby [D,N] polynomial matrix, not just triples inside the original rational-inner ansatz. Controllability and observability are open at the base, so the ordinary neighborhood can also be restricted to minimal eight-state plants. Compact root avoidance then excludes stabilization throughout that whole neighborhood. An open set of nonstabilizable triples disproves density of stabilizable triples under the stated model; omission of a single pole polynomial alone would not have done so.

## 8. Complex-nondegenerate plants inside the open family

This is secondary to the already established ordinary open-neighborhood conclusion. The explicit Wronski chart can be checked without applying a universal complex-nondegeneracy theorem to the base. Subtract z/5 times the derivative row from the monomial row, multiply the first row by five and the second by1/5. The last two columns and first four columns are exactly D_W,N_W in equation(21), with row degrees4,4 and full leading rank.

For a complex four-plane, the complementary two-dimensional polynomial subspace produces the Wronskian of two independent characteristic-zero polynomials. Its identically zero Wronskian would force a constant ratio and dependence, impossible. Thus this explicit real monic chart point has no complex basepoint.

The coefficient-vanishing incidence with the projective complex Grassmannian is algebraic and its projection is closed. The witness makes that degeneracy locus proper. A proper algebraic subset cannot contain a real Euclidean open subset of this real affine coefficient chart. Hence complex-nondegenerate chart points occur arbitrarily close to the base. Their canonical realizations depend continuously on the chart coefficients, so some lie in the ordinary open family. This does not repair a missing robustness step; that step was established independently above.

## Conclusion and boundaries

No bridge defect was found. The argument does not rely on the base being complex-nondegenerate, on evaluating finitely many gains or polynomials, on suppressing infinity roots, or on an unobservable unstable mode. The whole-plant chart and compact all-gain normalization are essential and reconstruct as stated.

This review supplies no byte-level numeric8×8 witness, software certificate, formal theorem, primary-source priority certification or human control-theory assessment. It is an ordinary in-harness reconstruction of a high-consequence candidate. Any promotion or P24 publication wording remains the parent's responsibility under the operative verification/timestamp qualifications. W4 remains this worker's sole primary problem.
