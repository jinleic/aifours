# Independent hostile algebra reconstruction: rational-inner P24 candidate

Before-creation clock observed: **2026-10-23T14:10:48-07:00**. Reviewer: `MathResearch96h`, temporarily assigned this bounded peer check by the parent; PH remains the only owned scientific problem. Complete assigned §§1–7 read, plus the remaining scope/binding sections for context. No scientific program, coefficient-rank computation, symbolic algebra engine, numerical evaluation, model CLI or nested agent was used. Only this new PH slot receives the review output.

Reviewed source: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-SOF24-rational-inner-candidate-v1.md`.

Exact SHA256: **`267d717cd735537ff8c29a3c73a17ed7fb1f7939c85788a8cbd60374f74ab8a0`**.

Read the operative `parallel-18/sof24/selection-v1.md`, especially the literal P24 dimensions8states/4inputs/2outputs, the open-family burden, complex-degenerate-vs-real-basepoint-free distinction and the separate robustness route. The prior primitive-Hermitian obstruction does not automatically refute this different kernel class.

## Verdict

**0 FATAL /0 MAJOR /0 MINOR found in the assigned algebraic slice.** I actively tried to falsify the Fourier support/elimination, coefficientwise complexification, real-simple kernel exclusion and inhomogeneous z8 argument; all reconstruct as stated. This supports only the exact §§2–7 algebra and its explicit scope. It is NOT a full P24 acceptance: the root transport, ordinary-plant binding, minimality, open-neighborhood chart, complex-nondegeneracy density/source interface and prior art need their separately assigned full checks.

The source is intentionally complex-degenerate as a pole map but real-basepoint-free. I do not impose the abandoned complex-nondegenerate-fibre route as an extra assumption on its direct open-family strategy.

## 1. Inner identity and full Laurent support table

Let r3/5,s4/5. The matrix[[r,is],[is,r]] is unitary: diagonal norms r2+s21 and off-diagonal inner products cancel. Since f1=t(1+t)/2,f2=(1-t)/2 and |t|1, their squared norms sum1. Multiplying by t2 and t respectively preserves norms, so |p|2+|q|21 holds on the full circle.

Writing all coefficients with an overall factor1/2,

    p: t2 -> is, t3 -> r-is, t4 -> r;
    q: t1 -> r, t2 -> -r+is, t3 -> is.

These are exactly the expanded rational-complex polynomials in the source. Direct multiplication gives the **complete** p bar(q) Laurent table:

    exponent -1: s2/4;
    exponent  0: -irs/2;
    exponent  1: -1/4;
    exponent  2: -irs/2;
    exponent  3: r2/4;

with every other coefficient zero. In particular its negative support ends at-1, not-3. Its conjugate can contribute to positive order1 but not2or3.

For |p|2 the complete table is

    exponent 0: 1/2;
    exponent 1: (r2-s2)/4;
    exponent 2: -irs/4;
    exponent -1: (r2-s2)/4;
    exponent -2: +irs/4.

For the linear p and q terms the positive coefficients are just the three coefficients above; their conjugates have only negative frequencies. These tables independently determine every homogeneous and inhomogeneous coefficient used below, including the potentially missed conjugate term at order1.

## 2. Homogeneous eight-real-function independence

A general Hermitian form in(p,q,1), modulo |p|2+|q|21, has precisely the eight real parameters h,d real and a,b,c complex displayed in(4). This accounts for all9Hermitian parameters minus the one known relation.

Order4 gives br/20, hence b0. Order3 gives ar2/4+cis/20, hence c9ia/40. The order2 equation simplifies exactly to

    id s+a[r+i(s+1/s)]=0,
    (12+41i)a=-16id,
    a=(-656-192i)d/1825.

The order1 equation multiplied by4 is

    d(r2-s2)-a+s2 bar(a)+2rc=0.

Writing a=x+iy, its imaginary part is27x-164y0. Substitution from the preceding line gives13776d/18250 because-17712+31488=13776. Thus d0, then a,c,b0 and finally h0 from the constant coefficient. This is a complete real independence proof, not a claim from a numerical rank.

## 3. Real polynomial conversion, degree and gcd

For real z, t=(z+i)/(z-i) lies on the unit circle and(P,Q,C)=(z-i)4(p,q,1). Coefficientwise Re/Im therefore make v_R and Jv_R genuinely real rational-coefficient polynomial rows. Their leading complex coefficient is(r,is,1); the underlying real vector(r,0,0,s,1,0) and its J-rotation(0,r,-s,0,0,1) are independent. Both row degrees are4 and the wedge has degree8, not just a nominal upper degree.

After complexifying the real coordinate pairs, the row combinations v_R±iw_R lie in two fixed complementary complex3sectors, with coordinate vectors(P,Q,C) and(bar(P),bar(Q),bar(C)). Here bars conjugate coefficients only, never z. C=(z-i)4 is nonzero away from i, and P(i)=3(2i)4/10=24/5 is nonzero. The conjugate sector is similarly nonzero at its only possible Czero,-i, with bar(P)(-i)=24/5. Thus neither sector vector vanishes anywhere over C and the two row vectors are independent at every finite complex z. A common nonconstant minor factor would have a complex root where all minors vanish, impossible. Consequently their gcd is1; the independent leading wedge also checks the point at infinity.

This proves a basepoint-free **row curve**, not a complex-basepoint-free pole-placement map. The source explicitly makes that distinction.

## 4. Exact kernel and real decomposable exclusion

The wedge v_R wedge Jv_R is J-invariant, with Hermitian evaluation represented exactly by vv*, v=(P,Q,C), under the source's i/2 convention. The inner identity gives the coefficientwise polynomial relation

    P bar(P)+Q bar(Q)-C bar(C)=0.

The line-to-circle change is invertible away from a single point and C bar(C)=(z2+1)4 is nonzero for real z. Hence any real linear relation among the eight real polynomial functions would give a relation among the eight Laurent functions on the circle minus one point, and then everywhere. Their coefficient span therefore has dimension8 and is exactly the hyperplane in Herm3 orthogonal to B=diag(1,1,-1).

The full real bivector space decomposes orthogonally into the6dimensional anti-J space and9dimensional J-invariant/Hermitian space. The trace pairing and Euclidean form pairing have the same fixed normalization under this identification; diagonal Ejj corresponds to dxj wedge dyj and off-diagonal components preserve the same scaling. Therefore the full coefficient-map kernel is exactly anti-J +R B, not merely a subspace contained in it.

For a real simple x wedge y with x,y independent, its Hermitian component H(x,y)=(i/2)(xy*-yx*) is nonzero and has complex rank<=2. If it were zero, rank1 outer-product equality would force y to be a real multiple of x. But every element of the candidate kernel has Hermitian component lambda B, of rank3 when lambda nonzero and zero when lambda0. Neither can equal that nonzero rank<=2 component. Thus there is no nonzero real simple bivector in the kernel.

The complementary Plucker coordinates of a real rank4L are a nonzero simple bivector, so det[V0;L] is never identically zero for any real L. This verifies real-basepoint-freeness on the compact real Grassmannian without falsely asserting complex non-degeneracy. The anti-J+full-rank-indefiniteB class is not the previously excluded primitive-Hermitian class.

## 5. Independent inhomogeneous z8 omission

The inverse Cayley variable is z=i(t+1)/(t-1), and z2+1=-4t/(t-1)2. Therefore z8/(z2+1)4=(t+1)8/(256t4). Its positive Fourier coefficients are exactly1/256,1/32,7/64,7/32 at orders4,3,2,1 respectively.

Order4 now gives b5/384, real. Subtracting bp's order3 contribution leaves7/256+i/192; division by is/2 gives

    c=9ia/40+(20-105i)/1536.

For order2, the known b and c0 terms sum to(72+95i)/3072. Since g2=336/3072, the remaining unknown equation is

    (12+41i)a=-16id+(-6600+2375i)/576.

Multiplication by12-41i gives

    x=x0-656d/1825, y=y0-192d/1825,
    x0=18175/1051200, y0=299100/1051200.

All numerator signs and denominators match the source. The order1 equation multiplied by400 is

    175/2=-28d+(-100+27i)a+64bar(a)+120c0.

Its imaginary part is27x-164y=525/64 and its real part is-28d-36x-27y=1375/16. Substitution gives

    (13776/1825)d=525/64+164y0-27x0>0,
    -(22300/1825)d=1375/16+36x0+27y0>0.

The first positive sign is not inferred just from x0,y0 positive: explicitly164·299100-27·18175=48561675>0. The second is immediate. Hence the same real unknown d would have to be both positive and negative, a contradiction. No constant-term adjustment can repair it because h affects only the constant coefficient. This proves z8 lies outside the full linear polynomial image before restricting to decomposable L.

## 6. Determinant functional and rational radius

The eight real polynomial functions in(14) are independent by §2/§3, so their9-by-8 real rational coefficient matrix F has rank8. The preceding omission means e8 is outside that span. Thus det[F,e8] is nonzero and the normalized determinant formula ell is a well-defined rational linear functional annihilating the exact polynomial image with ell(z8)=1.

For S=sum_(j0)^7|ell(zj)|binomial(8,j), rho=1/[2(1+S)] is a strictly positive rational <=1/2, even if S0. Every monic degree8 polynomial with roots in the closed radius-rho disk satisfies the usual elementary-symmetric coefficient bound. Because8-j>=1 and rho<=1,

    |ell(phi)-1|<=sum |ell(zj)|binomial(8,j)rho^(8-j)
                 <=rho S<1/2.

Hence it cannot lie in the image. This is an exact finite determinant recipe with a proven nonzero denominator, not an unperformed rank test or a solver placeholder. No numerical radius was evaluated here.

## 7. Remaining full-P24 verification boundary

No fatal algebraic gap was found in the assigned slice. Its conclusions are: an explicit rational real degree8 row curve with minor gcd1; exact real-basepoint-freeness of the pole map; omission of z8 from even the linear image; and exclusion of a closed root-disk family by a rational functional/radius recipe.

Those facts alone are not generic unstabilizability. The later Cayley transport of all projective closed-left-half-plane root divisors, ordinary8state realization/minimality and open ordinary-plant neighborhood are load-bearing separate steps. I read them for context but do not treat this bounded algebra verdict as their independent acceptance. In particular I neither reject the candidate merely because its pole map is complex-degenerate nor assume that its separate real-open-neighborhood route works without checking it.

No expanded8-by-8/8-by-4/2-by-8 numeric witness, execution, external-source priority authentication, publication readiness or proof-assistant kernel is certified here. The two operative parent errata remain mandatory. PH ownership and its residual six-state problem are unchanged; this is only a temporary peer check.
