# Seven-state PH extension using a canceled complex pair — candidate v1

Clock actually observed before creation: **2026-10-23T14:48:51-07:00**. Owner: MathResearch96h, math-1. Written reasoning only: no scientific program, symbolic algebra system, numerical search, solver or proof assistant ran. The symbolic derivation below was explored in writing before this packet was frozen; this is not a preregistered discovery claim.

## 1. Exact scope, baseline and candidate delta

Let c>0, d>0, a=c+d, b>0, z=b^2/d^2, and

    K=c(a^2+b^2)^2,
    H(s)=K/[(s+c)((s+a)^2+b^2)^2].

The full selected problem is the minimum finite PH order as a function of z on the entire PH-existence region. This packet does not solve that full problem or the book's general minimal-representation question.

**Candidate upper-bound theorem.** The explicit seven-state construction below works on

    35/64 <= z <= 5935/9126.                         (C7-new)

The separately written-checked inherited G7 construction works on 1/2<=z<=53/96. These intervals overlap, since 35/64<53/96. Their union therefore gives PH order at most seven throughout

    1/2 <= z <= 5935/9126.

**Conditional-on-recorded-dependencies exact-order corollary.** Compose that upper bound with the separately supported topology-unrestricted B6 theorem, which excludes every PH representation with at most six states for z>1/2. Then the minimum is exactly seven on

    1/2 < z <= 5935/9126.                           (C7-min)

At z=1/2 the minimum remains six, not seven. No impossibility of PH7 above 5935/9126 is asserted. In particular the residual is beta in (sqrt(5935/9126), beta_*), not an interval with a squared lower endpoint and an unsquared upper endpoint.

This packet is **CANDIDATE pending actual separate review and parent disposition**. Its exact-order corollary uses existing written-check-level results, not kernel theorems. Novelty remains **UNCLEAR**.

The actual change from the prior finite band is an extended seven-state upper construction: the old endpoint is 53/96, while the new endpoint is 5935/9126. Unlike the earlier G7 cancellation of two real hidden poles, the new construction cancels a stable nonreal conjugate pair. Spectral realizability alone is not the argument; Sections 5–6 give the actual PH matrices, positive scaling and full transfer cancellation.

## 2. One companion template

Take a parameter m>0, put eta=d/m and lambda=a+eta, and let w=1+b^2/eta^2=1+m^2 z. Define

    J=m+1,
    L=m^2+6m+17,
    Q=L-2w,
    R(x)=x^2+(m+5)eta x+Q eta^2.

The parameter ranges below have Q>0 and m+5>0. Consider

    P(x)=(x-J eta)[(x-eta)^2+b^2]^2 R(x)
         =eta^7 p(x/eta),
    p(Y)=(Y-J)(Y^2-2Y+w)^2(Y^2+(m+5)Y+Q).

All its factors, including the hidden quadratic, are literal factors of the proposed state characteristic polynomial. The quadratic is not assumed to split over the reals.

For the expansion, first multiply

    (Y-J)(Y^2+(m+5)Y+Q)
      =Y^3+4Y^2+(Q-m^2-6m-5)Y-JQ
      =Y^3+4Y^2+(12-2w)Y-JQ,

and

    (Y^2-2Y+w)^2
      =Y^4-4Y^3+(4+2w)Y^2-4wY+w^2.

Multiplying these two displayed polynomials gives the complete table:

| power | coefficient in p(Y) |
|---|---|
| 7 | 1 |
| 6 | 0 |
| 5 | 0 |
| 4 | 4w+4(m+3)^2-(m+5)Q |
| 3 | -3w^2+48+4JQ |
| 2 | 12w^2-48w-4JQ-2JQw |
| 1 | w[(12-2w)w+4JQ] |
| 0 | -JQw^2 |

The coefficient at power 5 vanishes precisely because Q=L-2w. In particular no coefficient identity here is inferred from finitely many point evaluations.

Write

    p(Y)=Y^7-A3 Y^4-A4 Y^3-A5 Y^2-A6 Y-A7.

Thus

    A3=(m+5)Q-4w-4(m+3)^2,
    A4=3w^2-48-4JQ,
    A5=-12w^2+48w+4JQ+2JQw,
    A6=w[2w^2-12w-4JQ],
    A7=JQw^2.                                     (1)

We next prove all these feedback coefficients are nonnegative on two connecting parameter families.

## 3. Family A: an interval at fixed m=8

Set

    m=8,  36<=w<=1193/30,  Q=129-2w.

Then J=9, Q>=742/15>0, and (1) becomes

    A3=1193-30w,
    A4=3w^2+72w-4692,
    A5=-48w^2+2298w+4644,
    A6=w(2w^2+60w-4644),
    A7=9Qw^2.

The signs are direct:

- A3>=0, with equality only at the upper endpoint.
- A4 is increasing for w>=36 and A4(36)=1788>0.
- A5=w(2298-48w)+4644>0 since w<40 and 2298-48*40=378>0.
- The parenthesis in A6 is increasing for w>=36 and is 108 at w=36.
- A7>0.

Since z=(w-1)/64, this family covers exactly

    35/64 <= z <= 1163/1920.                      (2)

The hidden quadratic is genuinely nonreal throughout: its discriminant after dividing out eta^2 is

    13^2-4Q=8w-347 <= -433/15 <0.

No real-hidden-pole hypothesis was smuggled into the sign argument.

## 4. Family B: a continuous curve extending the upper endpoint

For 13/2<=m<=8, set

    w=W(m)=(m^2+23)/2-56/(m+7),
    Q=6m-6+112/(m+7).                            (3)

These obey Q=L-2w. Also

    2(m+7)w=m^3+7m^2+23m+49,

so the coefficient of Y^4 vanishes: A3=0. The coefficient of Y^5 was already zero.

The simple bounds needed below hold throughout the entire closed m-interval:

    28<w<40,   41<Q<50,   15/2<=J<=9.            (4)

Indeed W is strictly increasing because W'(m)=m+56/(m+7)^2>0. Its endpoints are 6151/216 and 1193/30. Likewise Q'(m)=6-112/(m+7)^2>0, and its endpoints are 1115/27 and 742/15.

By (4),

    A4=3w^2-48-4JQ >3*28^2-48-4*9*50=504>0,

and

    A5=w(2JQ-12w+48)+4JQ>0,

because the parenthesis is greater than

    2*(15/2)*41-12*40+48=183>0.

Also A7=JQw^2>0.

The remaining sign, A6>0, is not left to a plot. Substituting Q=L-2w gives

    A6/w=E(m):=2w^2+(8m-4)w-4(m+1)(m^2+6m+17).

Put t=m+7. Equation (3) says w=(t^2-14t+72)/2-56/t. A literal expansion gives

    2t^2 E(m)=F(t),
    F(t)=t^6-28t^5+280t^4-1400t^3
          +4256t^2-9408t+12544.                 (5)

For r=t-27/2=m-13/2>=0, the same polynomial is

    F(27/2+r)
      =r^6+53r^5+(4495/4)r^4+(23795/2)r^3
       +(1008911/16)r^2+(2175765/16)r
       +962305/64.                              (6)

Every coefficient is strictly positive, so E(m)>0 and A6>0 on the entire closed interval. Equations (5)–(6) are polynomial identities with all coefficients displayed, not empirical checks.

The hidden quadratic remains genuinely nonreal here as well. Its discriminant divided by eta^2 is

    (m+5)^2-4Q=(m-7)^2-448/(m+7)<0,

since (m-7)^2<=1 and 448/(m+7)>=448/15>1.

Finally (3) implies

    z=Z(m)=(w-1)/m^2
          =1/2+(21m+35)/[2m^2(m+7)].            (7)

This continuous function is strictly decreasing for m>0. To check the sign without numerical differentiation, the numerator of the derivative of (21m+35)/[m^2(m+7)] is

    -14m(3m^2+18m+35)<0.

The endpoints are

    Z(8)=1163/1920,
    Z(13/2)=5935/9126.

Consequently Family B covers every z in that full interval, not just its two endpoints. For a specified z there, m is the unique root in [13/2,8] of

    2(z-1/2)m^2(m+7)=21m+35.

This is an exact parameter specification; no numerical root routine is a premise. Together (2) and (7) prove the full new range C7-new.

## 5. Literal PH generator and initial row

For either family put fj=eta^j Aj for j=3,...,7. Define C as the real 7x7 upper-shift companion:

    C_(i,i+1)=1       (i=1,...,6),
    C_(7,:)=(f7,f6,f5,f4,f3,0,0),

with all other entries zero. It is entrywise nonnegative by Sections 3–4. Its characteristic polynomial is P, as follows either by expanding the companion determinant or by the elementary resolvent recurrence given in Section 6.

Let G=C-lambda I. Its eigenvalues, with their algebraic multiplicities, are

- -c, once;
- -a+ib and -a-ib, each twice;
- the two roots of R(s+lambda), once each.

The first five eigenvalues follow by shifting the displayed factors of P. For the hidden factor, m+5>0 and Q>0 make the roots of R(x) have negative real parts; subtracting lambda>0 makes both strictly stable. More explicitly, the two hidden poles have real part

    -lambda-(m+5)eta/2=-a-(m+7)eta/2<-a.

Thus G is Hurwitz, even at every coefficient-zero endpoint. Repeated visible poles do not require a diagonalizability assumption.

Set

    D0=R(lambda)=lambda^2+(m+5)eta lambda+Q eta^2>0,
    h_i=lambda^(i-1)/D0                 (i=1,...,7),
    Delta=diag(h_1,...,h_7).

All seven coordinates of h are strictly positive. The actual proposed PH pair is

    T=Delta^(-1) G Delta,
    alpha=(Q eta^2, (m+5)eta lambda, lambda^2,0,0,0,0)/D0.       (8)

Equivalently, T has diagonal -lambda, superdiagonal lambda, and last row

    (f7/lambda^6, f6/lambda^5, f5/lambda^4,
     f4/lambda^3, f3/lambda^2, 0, -lambda).        (9)

The first six rows sum to zero. Since P(lambda)=K D0, the last row sums to

    -P(lambda)/lambda^6=-K D0/lambda^6<0.

Therefore its exit vector is exactly

    omega=-T1=(K D0/lambda^6)e_7.                 (10)

All off-diagonal entries in (9) are nonnegative. Similarity to the Hurwitz G proves transience. The entries of alpha are nonnegative and

    alpha 1=[Q eta^2+(m+5)eta lambda+lambda^2]/D0=1.

Thus this is a genuine seven-state PH pair, not a bare spectral realization. In particular the normalization has not been assumed to exist: its positive vector and every nonzero entry are explicit. The feedback f7 is positive on both families, so the superdiagonal path plus its return edge also makes T irreducible; this is a consequence, not an assumption on hypothetical realizations.

At the top of Family A, f3=0; throughout Family B it is zero. The coefficients corresponding to degrees six and five are zero throughout. None of these zero feedbacks destroys the positive h, the strict exit, normalization, or Hurwitz property. There is no endpoint limiting construction.

## 6. Exact transfer preservation and full hidden-pair cancellation

For generic x, solve (xI-C)y=e_7. The first six rows give y_i=x^(i-1)y_1. The last row gives P(x)y_1=1. Hence

    e_j^T(xI-C)^(-1)e_7=x^(j-1)/P(x),   j=1,...,7.           (11)

Both sides are rational functions, so the identity holds as a rational identity, not just at chosen x.

Let

    v=Q eta^2 e_1^T+(m+5)eta e_2^T+e_3^T.

Equation (11) and the definition of R give

    v(sI-G)^(-1)(K e_7)=K R(s+lambda)/P(s+lambda).

But the literal shifted factorization is

    P(s+lambda)
      =(s+c)((s+a)^2+b^2)^2 R(s+lambda).

It follows that the raw transfer is exactly H(s), canceling the entire stable conjugate pair, not just one of its roots or a real scalar substitute.

For completeness, (11) at x=lambda gives

    (lambda I-C)^(-1)(K e_7)=h,

because P(lambda)=K D0. Thus G h=-K e_7. Consequently alpha=v Delta, omega=Delta^(-1)K e_7, and diagonal similarity preserves the actual PH transfer:

    alpha(sI-T)^(-1)omega
       =v(sI-G)^(-1)K e_7
       =H(s).

This separately checks positive scaling, exit coupling, initial normalization and full cancellation. No appeal to a general PH-existence characterization or to nonnegative inverse-transform sampling is used.

## 7. Rational anchor and exact-order composition boundary

An uncomplicated member of Family B is m=7:

    eta=d/7,  lambda=a+d/7,
    w=32, Q=44, z=31/49,
    p(Y)=Y^7-1616Y^3-13184Y^2-8192Y-360448.

Its hidden quadratic is Y^2+12Y+44; the two hidden PH poles are

    -a-d +/- (2sqrt(2)d/7)i.

The displayed identity is a specialization of the full symbolic proof, not a finite-point substitute for it. It supplies a simple exact matrix instance strictly beyond the old G7 range.

The exact-order corollary C7-min has precisely two external scientific dependencies:

1. **B6**, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. The actual separate PhysicsDepol4 reconstruction returned 0F/0M/0m; the actual `institute/runs/three-area-2026-10-23-96h/PH6-unrestricted-parent-disposition-v1.md` supports the topology-unrestricted iff and equality rigidity at the in-harness written-check level. That source and review were read fully. Its claim above z=1/2 excludes all orders <=6, not just a constant-diagonal ansatz.
2. **Earlier G7**, `../../proof-H12-seven-state-extension-v1.md` relative to this slot, SHA256 `59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`. It supplies upper7 on [1/2,53/96], with its separate reconstruction and actual parent disposition. Since 35/64<53/96, it bridges the small lower interval not covered by the new literal construction.

The accepted baseline `../../manuscript-repeated-pole-PH-v2.md`, SHA256 `b92639157d0e90530d1237d336f781c6707b01c2846801cfad8fcf5ef1f204f2`, still supplies the earlier exact5/6 bands, existence threshold and order blowup, each with its own stated import boundaries. None is silently upgraded to formal acceptance or rewritten. Apply the round's timestamp and verification errata; no prior finite arithmetic spot-check is treated as a kernel replay.

## 8. Prior-art and review boundary

Companion positive realization, hidden eigenvalue cancellation and diagonal normalization are classical mechanisms. The additional primary source read for calibration was Kim–Ryou, *Positive Realization of Continuous Linear Systems with Order Bound*, ICINCO 2012, pp.1–4, particularly Section4's sufficient constructions for repeated complex poles: <https://www.scitepress.org/Papers/2012/39814/39814.pdf>. That reading does not authenticate priority for these constants or prove that this is outside all earlier algorithms. The previously frozen PH literature/corpus screen also remains only a bounded screen, not a novelty certificate.

The numerical bound 5935/9126 and this explicit parameterized PH7 construction therefore remain **NOVELTY_UNCLEAR** even if independently written-checked. The first new proof obligation is correctness of this finite-band construction, not a claim of global optimality of seven-state companions, a new general realization method, or a full-book solution.

Requested bounded independent review: reconstruct the entire product table; both parameter families and all sign bounds; identities (5)–(6) coefficient by coefficient; strict range coverage and monotonicity; repeated visible poles, hidden complex stability and endpoint zeros; positive h and literal generator; normalization, exits and full transfer cancellation; and the two distinct dependencies of the exact-minimum corollary. No executable verification is requested or authorized by this packet.
