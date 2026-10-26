# CURRENT P44 CONSOLIDATION v12 — PART10/10: exact h-absorption SR2 families and core-dominant SN2 regions of the ORIGINAL compression chart

PhysicsPPT44-2. Actual pre-write `/bin/date`: **Sun Oct 25 22:04:30 PDT 2026**. Exact WRITTEN mathematics only. No scientific interpreter/calculator/eval/program/CAS, enumeration, solver, replay, build/test, CLI, nested agent or scientific GO. Original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 unchanged.

## H0. Scope, honesty boundary and union rule

This NEW Part10 (claims C29.1–C29.5) returns to the ORIGINAL constructive target chart: the rank-four Bob compressions R_x of the published 4x5 source state, which include the literal original N4 assay input x=(1,1,1,1). It is NOT another Bell/Weyl/Pauli covariance class. It proves NEW Schmidt-number-two regions in exactly the large core-dominant directions where the C23 d/f/g noise budget fails. It does NOT settle the literal input (1,1,1,1), does not prove every R_x is SN<=2, and constructs no PPT/SN3 pair. **Original P44 remains UNMET.**

The complete current union is ALL TEN parts and endings: the nine parts bound in `checkpoint-082-complete-current-v11-nine-part-manifest-and-Pauli-class-closure-v1.json` (SHA256 67f2571d4287d49208d448133aba4946efbafe4cf5522503c7ccccdb98f018f2) plus THIS part, with ALL mandatory overlays named there. Frozen v10 (parent freeze v111 at 21:15:23) and every older gate are unchanged; Part9 and Part10 are LATER, UNREVIEWED, not inherited. Checkpoint083 (SHA256 to be bound by its own later metadata) discloses two NEW permanent process findings: a cadence miss cp082→cp083 (38min14s) and a NEW private-written decimal-heuristic exactness MAJOR during parameter exploration. **That approximate scouting has ZERO credit and is not a premise here.** Every inequality below is proved with exact symbolic values. This does not cure any process finding, including cp063, cp081/v16, cp049, ACK-order, cp013 and N4/old-exit/old21 histories.

## H1. Exact chart, coefficient matrix and residual rule

On Alice C4, Bob C4 with P(y)=yy* unnormalized, for x=(u,v,w,z) in C4:

```
a=00+11+22, b=01+12, c=10-21, d_x=02+|3>x, e=20+33,
f=30, g=32, j=23, h_x=|0>x,
R_x=P(a)+P(b)+P(c)+3[P(d_x)+P(e)+P(f)+P(g)+P(j)+P(h_x)].     (H1.1)
```

This is the same chart as Part6 (Y1.2); PPT is the local-filter image of the published source, as already established there. For psi=alpha a+beta b+gamma c+delta d_x+eps e+phi f+eta g+kappa j+lambda h_x, the coefficient matrix (rows Alice, columns Bob) is

```
[alpha+lambda u, beta+lambda v, delta+lambda w, lambda z]
[gamma,          alpha,         beta,           0       ]
[eps,           -gamma,         alpha,          kappa   ]
[delta u+phi,    delta v,       delta w+eta,    delta z+eps].    (H1.2)
```

**Residual rule (exact).** If a probability measure on SR<=2 vectors psi in this span has ALL coefficient cross-moments E[c_k conj(c_l)] equal to zero except possibly the (kappa,lambda) pair, then

`R_x - E[P(psi)] = sum_k (D_k - E|c_k|^2)P(g_k) - (X|j><h_x| + conj(X)|h_x><j|)`,

with D=(1,1,1,3,3,3,3,3,3), g_k the generators and X=E[kappa conj(lambda)]. Each g_k other than a has SR<=2. Every vector in span{j,h_x} has Alice support in span{|0>,|2>}, hence SR<=2. Therefore, if every D_k-E|c_k|^2 is nonnegative, D_a=E|alpha|^2, and the 2x2 matrix `[[3-E|kappa|^2, -X], [-conj X, 3-E|lambda|^2]]` is PSD, the residual is a nonnegative sum of SR<=2 projectors. The integral of SR<=2 projectors lies in the closed SN<=2 cone. Then R_x is SN<=2. No linear-independence assumption is needed: cross terms are literally absent.

## H2. C29.1 — exact h-absorption SR2 vectors and the two-parameter family

**Single vector.** If u!=0 and w!=0, then

`psi0 = a + (z/w) j - (1/u) h_x`                                   (H2.1)

has coefficient rows `[0,-v/u,-w/u,-z/u], [0,1,0,0], [0,0,1,z/w], [0,0,0,0]`. Row0 equals -(v/u)row1-(w/u)row2. Rows1/2 are independent, so the Schmidt rank is EXACTLY two. At the literal x=(1,1,1,1) this is `a+j-h = 11+22+23-01-02-03`, using only the j and h budgets (one each). Thus the original input's core direction has a very cheap SR2 completion. This is consistent with Part6 C24 and is NOT an SN2 proof by itself: a single fixed-phase vector has nonzero cross-moments with a.

**Family F2.** Put d=e=f=g=0 (delta=eps=phi=eta=0) and alpha=1. Then rank<=2 iff row0 lies in span(row1,row2). Solving the first three coordinates gives EXACTLY

```
lambda = 1/( w gamma^2 + v gamma - u(1+beta gamma) ),
kappa  = z/( u beta^2 - v beta + w(1-beta gamma) ),             (H2.2)
```

whenever the displayed denominators are nonzero (if z=0, kappa=0 and the second denominator is not needed). Derivation for gamma!=0: with p=(1+lambda u)/gamma and q=lambda w-p beta, the middle coordinate equation is equivalent to lambda[v gamma+w gamma^2-u(1+beta gamma)]=1. Then q=lambda(u beta^2-v beta+w(1-beta gamma)), and the last coordinate gives kappa=lambda z/q. For gamma=0 the first coordinate forces lambda=-1/u, p=beta-v/u, q=-(w+u beta^2-v beta)/u, and the same kappa formula follows. Row1/row2 are independent in every case. At beta=gamma=0, (H2.2) recovers psi0.

## H3. C29.2 — Theorem A: the slice x=(u,0,w,0), |u|^2>=4|w|^2+1/3

Take weight 1/2 on `psi_A0=a-h_x/u`, and weight 1/2 on the uniform circle family

```
psi_theta = a + sqrt2 e^(i theta) b - sqrt2 e^(-i theta) c + h_x/(u+2w e^(-2i theta)).   (H3.1)
```

Here beta gamma=-2, and (H2.2) with v=z=0 gives exactly lambda_theta=1/(u+2w e^(-2i theta)). Since |u|>2|w|, lambda_theta=(1/u)sum_n(-2w/u)^n e^(-2in theta) converges absolutely and contains only EVEN powers.

Exact moments:
- E[lambda]=(1/2)(-1/u)+(1/2)(1/u)=0.
- a-b, a-c, b-c (E[e^(2i theta)]) vanish; b-h and c-h vanish because beta/gamma are odd powers while conj(lambda) has only even powers.
- E|beta|^2=E|gamma|^2=(1/2)2=1. E|lambda|^2=(1/2)[1/|u|^2+1/(|u|^2-4|w|^2)] by Parseval.
- kappa=0.

If |u|^2-4|w|^2>=1/3, then both terms are <=3 and E|lambda|^2<=3. The residual is `(3-E|lambda|^2)P(h_x)+3[P(d_x)+P(e)+P(f)+P(g)+P(j)]`. Hence **R_x is SN<=2 on this whole slice.** Example: x=(3,0,1,0), outside the Part6 ball (normx^2=10). The w=0 axis was already the old core0 mechanism; w!=0 points with |u|^2+|w|^2>2 are new.

## H4. C29.3 — Theorem C: the u-dominant region with arbitrary bounded z

Fix the exact constants

```
pi_1 = -3/2 + i/2,  pi_2 = -3/2 - i/2,  1+pi_k=(-1 +- i)/2,
g_k = sqrt2,  b_k = pi_k/sqrt2 = (-3 +- i)/(2 sqrt2),
|g_k|^2=2, |b_k|^2=5/4, |1+pi_k|=1/sqrt2, |1-pi_k|=sqrt26/2,
b0 = sqrt3/2.                                                    (H4.1)
```

Ensemble, with zeta=e^(i theta) uniform:
- Type0' (weight 1/2): beta=b0 zeta, gamma=0, lambda=-1/u, kappa=z/(u b0^2 zeta^2 - v b0 zeta + w).
- Type k=1,2 (weight 1/4 each): beta=b_k zeta, gamma=g_k conj(zeta), with lambda_k, kappa_k from (H2.2), i.e.

```
lambda_k = 1/( 2w conj(zeta)^2 + sqrt2 v conj(zeta) - u(1+pi_k) ),
kappa_k  = z/( u b_k^2 zeta^2 - v b_k zeta + w(1-pi_k) ).          (H4.2)
```

Define exact margins

```
m_L = |u|/sqrt2 - sqrt2|v| - 2|w|,
m_0 = (3/4)|u| - (sqrt3/2)|v| - |w|,
m_K = (5/4)|u| - (sqrt5/2)|v| - (sqrt26/2)|w|.                  (H4.3)
```

**Theorem C.** If |u|>=1, m_L>=1, and either z=0, or m_0>0, m_K>0 and |z|<=min(m_0,m_K), then R_x is SN<=2.

Proof. m_L>0 makes each lambda_k a power series in conj(zeta) with c_k0=1/A_k, c_k1=-sqrt2 v/A_k^2, where A_k=-u(1+pi_k); |lambda_k|<=1/m_L. m_0,m_K>0 make the zeta^2 coefficient dominate each kappa denominator. Then every kappa is a power series in zeta^(-1) containing ONLY powers <=-2, and |kappa|<=|z|/m_0 or |z|/m_K. Every member is SR2 by C29.1 (all pivots/denominators nonzero). Moments:

- E[lambda] = -(1/u)[1/2 + (1/4)(1/(1+pi_1)+1/(1+pi_2))] = -(1/u)[1/2+(1/4)((-1-i)+(-1+i))] = 0.
- E[kappa]=0: no zeta^0 term exists.
- c-h: E[gamma conj(lambda)] = sum_k (1/4) g_k conj(c_k1) = -(conj v/conj u^2)(1/4)(2)[1/(1+conj pi_1)^2+1/(1+conj pi_2)^2] = -(conj v/(2conj u^2))[1/(i/2)+1/(-i/2)] = 0.
- b-h, a-b, a-c, b-c vanish by Fourier degree. b-j and c-j vanish because conj(kappa) has only powers >=2 while beta, gamma have degree +-1. The only surviving cross is j-h, X=E[kappa conj(lambda)].
- E|beta|^2=(1/2)(3/4)+(1/2)(5/4)=1, E|gamma|^2=(1/2)(2)=1, E|alpha|^2=1.
- E|lambda|^2<=(1/2)|u|^-2+(1/2)m_L^-2<=1, E|kappa|^2<=|z|^2 max(m_0^-2,m_K^-2)<=1. Ensemble Cauchy–Schwarz gives |X|<=1, so `[[3-E|kappa|^2,-X],[-conj X,3-E|lambda|^2]]` has diagonals >=2 and is PSD.

The residual rule (H1) finishes the proof. QED.

Example: x=(10,1,1,1). Exact checks: m_L=5sqrt2-sqrt2-2=4sqrt2-2>=1 because 32>=9. m_0-1=11/2-sqrt3/2>0 because 121>3. m_K-1=23/2-(sqrt5+sqrt26)/2>0 because (sqrt5+sqrt26)^2=31+2sqrt130<=55<529. So R_(10,1,1,1) is SN<=2, far outside the Part6 ball.

## H5. C29.4 — exact transfer by the source involution (w-dominant region)

Part6 Y4.1 proved, for z!=0, R_x=(U tensor F_x)R_x'(U* tensor F_x*) with invertible F_x and x'=(w/z,v/z,-u/z,1/z). Invertible local filters preserve SN exactly. Writing x=(-w'/z',v'/z',u'/z',1/z') shows: **R_x' is SN<=2 whenever x=(-w'/z',v'/z',u'/z',1/z') satisfies Theorem C.** After multiplying by |z'|, this is the w-dominant region:

```
|w'|>=|z'|, |w'|/sqrt2 - sqrt2|v'| - 2|u'| >= |z'|,
(3/4)|w'|-(sqrt3/2)|v'|-|u'| >= 1, (5/4)|w'|-(sqrt5/2)|v'|-(sqrt26/2)|u'| >= 1.   (H5.1)
```

The source involution likewise transfers Theorem A/C to the k4=0 boundary compressions not in the affine chart, exactly as in Part6 Y4/Y6.

## H6. C29.5 — exact status of the literal original input x=(1,1,1,1)

The literal input lies OUTSIDE every proved region. It fails Part6's ball (normx^2=4>2) and its projective criterion (4<=2 false). It also fails the old generic region (3>1/3), every axis/auxiliary merge, Theorem A (v,z!=0) and Theorem C (m_L=1/sqrt2-sqrt2-2<0). In (H5.1), |w'|/sqrt2-sqrt2-2 is negative. **Its Schmidt number therefore remains UNKNOWN.** The historical N4 attempt remains UNKNOWN/incomplete/overrun/exit-unestablished; nothing was rerun.

Exact new facts at that point:
1. psi0=a+j-h is SR2 (H2.1).
2. F2 at x=(1,1,1,1) is `lambda=1/(gamma^2+gamma-1-beta gamma)`, `kappa=1/(beta^2-beta+1-beta gamma)`. For beta=(1+i sqrt5)/2,gamma=0: beta^2-beta+1=-1/2, so kappa=-2, lambda=-1, and b-cost is 3/2.
3. **Restricted-witness exclusion.** Consider a range witness whose coefficient form is H(c)=-A|alpha|^2+2t Re(conj(alpha)(kappa-lambda))+sum_k B_k|c_k|^2, with real B_k>=0 and t real. Its value on psi0 needs A<=4t+B_j+B_h. Its value on fact2's vector needs (3/2)B_b+4B_j+B_h>=A+2t. A negative state value needs A>B_b+B_c+3(B_d+B_e+B_f+B_g+B_j+B_h).

   These three inequalities are incompatible for t>=0. The first and third imply 4t>B_b+B_c+2B_j+2B_h. The second and third imply (1/2)B_b+B_j>2B_h+2t+3(B_d+B_e+B_f+B_g)+B_c>=2t. Then 4t>B_b+2B_j>=4t, a contradiction. For t<0 the psi0 inequality A<=4t+B_j+B_h<B_j+B_h contradicts the third inequality directly. Hence NO witness of this restricted diagonal-plus-(a,j)/(a,h) form certifies SN3 at the literal input. This is a restricted-form exclusion only, not an SN2 proof and not a general witness classification.

## H7. What changed, imports and the original gap

New relative to Part6: C23 controls small charts by k/tau noise in d,f,g. Here the h_x generator, absent from C23's ensembles, absorbs the a-row pivot (lambda~1/u). The paired circle families cancel every forbidden cross-moment by Fourier degree and the exact phase identities (1+pi_k)^2=+-i/2 conjugate. This covers arbitrarily LARGE core-dominant compressions (u-dominant; by involution w-dominant), including bounded z. Remaining open in this chart: v-dominant and balanced directions, notably the literal (1,1,1,1). No claim about those.

Ordinary imports: finite complex rank/PSD algebra, absolutely convergent Laurent series on the unit circle with Fourier orthogonality and Parseval, closedness of the SN<=2 cone, and the already-proved Part6 source involution and PPT image. No numerical value, sampled point, approximate decimal, program output, old solver/N4 result or unreviewed table is a premise. Examples are verified by exact squared-integer comparisons shown inline.

**Original physics-3/P44 remains UNMET:** no explicit rational 4x4 PPT state with a verified universal complex-SR<=2 strict negative separator, and no unrestricted all-4x4-PPT SN<=2 theorem. This part narrows the ORIGINAL compression route (it now fails in all sufficiently core-dominant directions). It is not a no-go for the chart, the input (1,1,1,1) or P44. All claims are author-WRITTEN candidates needing fresh complete reconstruction. Not formal/kernel/executable/triple/configured-family/human/cross-vendor/novelty/SOTA/publication acceptance, not a park and not a round closeout. Same eighteen owners, cutoff and deadline.

**END OF COMPLETE CURRENT v12 PART10/10.**
