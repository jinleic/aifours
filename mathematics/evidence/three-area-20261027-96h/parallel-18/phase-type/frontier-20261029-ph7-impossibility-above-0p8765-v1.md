# No seven-state PH representation for any ratio z >= 1753/2000 = 0.8765

**NEW ALL-TOPOLOGY THEOREM CANDIDATE (strengthens the pinned 8/9 decision).** Written proof; exact SymPy identities for a symbolic ratio z; exact integer Bernstein certificates at the single ratio z1=1753/2000; an independently implemented standard-library replay. Not independently reviewed; parent adoption, formal proof and novelty clearance pending. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 06:07:58 PDT 2026**.

## 1. Statement

For c,d>0, a=c+d, z=b²/d², let `H(s)=c(a²+b²)²/[(s+c)((s+a)²+b²)²]`.

**Theorem.** If `z>=z1:=1753/2000`, then H has no phase-type representation with at most seven states.

Equivalently, the set of ratios admitting a seven-state PH representation lies in `z<0.8765`. The separately constructed seven-state band reaches about 0.82042 (owner candidates, not re-proved here), so the exact seven-state threshold is now bracketed in roughly [0.8204, 0.8765). Not decided here: the threshold itself, minimum orders above 8/9 beyond the lower bound 8.

## 2. Proof structure

1. **Caller.** For z>1/2 the irreducibility theorem (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`) turns a PH representation with <=7 states into an irreducible 7x7 Metzler G of spectral bound0 with `y[(y+1)²+z]²` dividing its characteristic polynomial and hidden quadratic `y²+py+q`, p,q>0.
2. **Shift to z1.** By Lemma S of `frontier-20261029-ph7-shift-monotonicity-corollary-v1.md` (SHA256 `dde16615ea1cfcc0dcac77ca5f3329cc947e58287e4c126b13979468b7a390e1`) with `t=sqrt(z/z1)-1>=0`, one obtains such a matrix at the ratio exactly z1. So it suffices to exclude z=z1.
3. **Symmetrization.** Lemmas 1-4 of `frontier-20261029-ph7-eight-ninths-impossibility-v1.md` (SHA256 `599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4`) are independent of z: the eigenvalues `ut_1<=...<=ut_7` of `-S` are positive, and the coefficient matching with `y[(y+1)²+z]²(y²+py+q)` gives, for general z (identities checked symbolically),

        p=e1-4,  q=e2-4e1+10-2z,
        E4(z):=e3-4e2+(10-2z)e1+12z-20 = W >= 0,
        E3(z):=e4-(6+2z)e2+(20+4z)e1+3z²+6z-45 >= E4(z)*S4.

4. **Lemma C at z1.** These four conditions are infeasible for seven positive reals at z=z1. The proof is the case analysis of the no-two-cycle core (SHA256 `46659f60be21537f02d6ea76ceac3be2b89a7a55c3d2b1e8f249c7c315383745`) with z-dependent constants: with x the largest number and f_k the elementary sums of the other six,

        A=f2-4f1+10-2z,  B=f3-4f2+(10-2z)f1+12z-20,
        h1=f3-(6+2z)f1+20+4z,  h0=f4-(6+2z)f2+(20+4z)f1+3z²+6z-45,
        q=A+x(f1-4),  E4=Ax+B,  E3-E4*S4=E+xD,  D=h1-A*S4,  E=h0-B*S4,  EA-BD=h0A-h1B.

   - (a) f1<4: `A-(4-f1)²=f2+4f1-f1²-6-2z <= 6/7-2z-(7/12)(f1-24/7)² <0` because `z1>3/7`.
   - (b) f1>=4, A<=0: contradiction with `Qpol(z1)=L_Q[A²-(f1-4)B]>0`.
   - (c) f1>=4, A>0, D<=0: contradiction with `Hpol(z1)=-L_H[h0A-h1B]>0`.
   - (d) f1>=4, A>0, D>0: with the four smallest of the six (sums alpha_k) and the two largest (beta1,beta2), `D=K1+beta1 K2` (beta2 cancels), `K1=alpha3-alpha1 alpha2+4alpha1²-16alpha1+20+4z`, `K2=alpha2-alpha1²+4alpha1-6-2z`; the bounds `beta2<=beta1²/4`, `alpha3<=alpha1 alpha2/6`, `alpha2<=(3/8)alpha1²`, `beta1>=alpha1/2` reduce to the three-parameter residual `NOT(Abar>0 and Dbar>0 and f1>=4)`, certified at z1.

## 3. Certificates at z1=1753/2000 (exact integers)

Generator `frontier-20261029-ph7-threshold-z1-check.py`, **158LF/9336B**, SHA256 `586e1bc96ad4b2d89b026615790bd6e0144b390f33d3f2fd6d8dc6ae8f7be5a8`, actually printed

    symbolic-z identities PASS; case (a) bound negative at z1
    Qpol(z1) leaves 9942 Hpol(z1) leaves 5952
    SymPy 1.14.0 z1=1753/2000 exact PASS: Q leaves 9942 H leaves 5952 residual {'Abar<=0': 844, 'Dbar<=0': 828, 'f1-4<0': 64}

Qpol(z1), Hpol(z1) have individual degree2 in each of six rates; compactification `u_i=x_i/(1-x_i)` times `prod(1-x_i)^2`; every leaf has all integer Bernstein coefficients >=0, depth >=6, and every interior-domain vertex coefficient >0, giving strict positivity on the open positive orthant (the symmetrization lemma makes all seven numbers strictly positive, so no boundary face is needed). Residual chart and selectors as in the 8/9 core.

Certificate `frontier-20261029-ph7-threshold-z1-certificate-v1.json`, **22880LF/523925B**, SHA256 `62b279a132f0f7663dfefa2c0b2fd05591884f2a47928800decc58f39f6ba9af` (integer scales, coefficient digests, all 9942+5952 six-cube leaf paths and 1736 residual leaves).

Separately written standard-library replay `frontier-20261029-ph7-threshold-z1-integer-replay.py`, **175LF/10036B**, SHA256 `7ae13e57436a8d47bfdc1e846f3bac81a332369b3516231f06a1697f31b849ee`, actually printed

    identities PASS (stdlib, symbolic z, incl. characteristic matching)
    six-dimensional covers replayed: 9942 5952
    Independent stdlib replay PASS at z1=1753/2000: Q/H leaves 9942 5952 residual {'f1-4<0': 64, 'Abar<=0': 844, 'Dbar<=0': 828}

It re-derives every identity with z as an extra polynomial variable (including the characteristic matching of `y((y+1)²+z)²(y²+py+q)`), rebuilds all polynomials from their definitions, matches digests and replays every leaf with exact integer/Fraction subdivision. Same-owner independent implementation, not human/cross-vendor/Lean verification.

## 4. Limit of this route (diagnostic, not a premise)

At six equal rates, `Qpol(z)` acquires a real double root exactly when `128z³-149z²+38z-5=0`, i.e. at `z_Q≈0.8760934`; below `z_Q`, `Qpol(z)` is negative at equal rates (kernel check: Q(7/8) = -0.0034 at six rates 0.894), the case-(b) step fails, and the integer cover at z=0.876 does not terminate. Thus z1=1753/2000 is within 4.1e-4 of the limit of the crude four-condition method; lowering the threshold further needs additional coefficient information (diagnostically, adding the y² coefficient with interlacing bounds moves the numerical threshold to about 0.84-0.85).

## 5. Scope and review targets

Review should reconstruct: the symbolic-z identities, case (a) with z>3/7, the z1 certificates (polynomial digests, compactification, leaf rule, coverage), and the dependency on Lemma S and on Lemmas 1-4 of the 8/9 candidate. All imports (irreducibility caller, symmetrization lemmas, shift lemma) are unreviewed or separately reviewed as recorded by the parent. No formal, kernel, human, cross-vendor, novelty or priority acceptance is claimed; historical holds and process findings are unchanged.

END - no seven-state PH representation exists for any z>=0.8765; the seven-state threshold lies in about [0.8204, 0.8765).
