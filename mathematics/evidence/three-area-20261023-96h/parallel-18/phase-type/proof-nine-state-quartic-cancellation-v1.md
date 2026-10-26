# Nine-state PH construction through beta=1 — candidate v1

Clock actually observed before creation: **2026-10-23T15:16:24-07:00**. Owner MathResearch96h, math-1. Written reasoning only; no scientific program, symbolic package, numerical assay or proof assistant. The derivation was explored in writing before this packet freeze.

## 1. Direct statement and boundary

Let c>0, d>0, a=c+d, b>0, z=b^2/d^2, K=c(a^2+b^2)^2 and

    H(s)=K/[(s+c)((s+a)^2+b^2)^2].

**Candidate:** there is an explicit nine-state PH representation for every

    3/4<=z<=1.                                   (C9)

This is an upper9 statement, not an exact minimum9, an order-eight exclusion, a general realization theorem or the full book answer. The supported B6 barrier only gives minimum at least7 there. C8's separate unreviewed candidate interval [13/20,8/9] overlaps C9, but this source does not inherit or promote it. The now-supported C7 exact-order band ends at5935/9126; a composed whole upper bound through z=1 would still need the actual C8 bridge gate.

Status **CANDIDATE / NOVELTY_UNCLEAR**, pending separate reconstruction and parent disposition. No executable verification is requested by this proof.

## 2. Exact polynomial and complete sign table

Put

    eta=d/2, lambda=a+eta,
    w=1+b^2/eta^2=1+4z.

Then 4<=w<=5. Use the fixed hidden quartic

    q(Y)=(Y+2)^2(Y^2+3Y+7)
        =Y^4+7Y^3+23Y^2+40Y+28.                 (1)

All its coefficients are positive. The roots are -2 twice and (-3+i sqrt19)/2, (-3-i sqrt19)/2. Thus the hidden roots have strictly negative real parts, with an explicit factorization handling their multiplicities.

The visible factor expands as

    D(Y)=(Y-3)(Y^2-2Y+w)^2
        =Y^5-7Y^4+(16+2w)Y^3-(12+10w)Y^2
          +(w^2+12w)Y-3w^2.                     (2)

Multiply p(Y)=D(Y)q(Y). The complete coefficients are

| power | coefficient in p(Y) |
|---|---|
| 9 | 1 |
| 8 | 0 |
| 7 | 2w-10 |
| 6 | 4w-21 |
| 5 | w^2-12w+32 |
| 4 | 4w^2-66w+168 |
| 3 | 2w^2-68w-32 |
| 2 | -29w^2+200w-336 |
| 1 | -92w^2+336w |
| 0 | -84w^2 |

For explicit coefficient reconstruction, the lowest four rows arise respectively from

    -(12+10w)*28+(w^2+12w)*40-3w^2*23,
    (w^2+12w)*28-3w^2*40,
    -3w^2*28,

for powers2,1,0; the power3 row is

    (16+2w)*28-(12+10w)*40+(w^2+12w)*23-7*3w^2.

The higher rows follow directly from (1)–(2); every power is displayed, not inferred from point evaluations.

All nonleading coefficients are nonpositive on the full closed w-interval:

- 2w-10<=0 and 4w-21<=-1.
- w^2-12w+32=(w-4)(w-8)<=0.
- 4w^2-66w+168 is decreasing on [4,5] and equals-32 at4.
- 2w^2-68w-32<=2*5^2-68*4-32=-254<0.
- -29w^2+200w-336=(w-4)(84-29w)<=0.
- -92w^2+336w=4w(84-23w)<0, since 23w>=92>84.
- -84w^2<0.

This includes all endpoint zeros: powers5 and2 vanish at w=4; power7 vanishes at w=5. No limiting generator is invoked.

## 3. Actual characteristic factor and companion

Define

    R(x)=eta^4 q(x/eta)
        =x^4+7eta x^3+23eta^2 x^2+40eta^3 x+28eta^4,
    P(x)=eta^9 p(x/eta).

The literal factorization is

    P(x)=(x-3eta)[(x-eta)^2+b^2]^2 R(x).          (3)

Write

    P(x)=x^9-sum_(j=2,...,9) fj x^(9-j),

where fj is minus the coefficient in the table at power9-j, multiplied by eta^j. All fj>=0 and f9>0. Let C9 have superdiagonal1, last row

    (f9,f8,f7,f6,f5,f4,f3,f2,0),

and all other entries0. It is entrywise nonnegative and is the upper-shift companion of P.

Let G=C9-lambda I. Since lambda-3eta=c and lambda-eta=a, (3) gives the desired visible eigenvalues -c and -a+ib,-a-ib, with each member of the latter pair repeated twice. The four hidden eigenvalues are the roots of R(s+lambda):

    -lambda-2eta, twice,
    -lambda-(3/2)eta +/- (sqrt19/2)eta i.

They are strictly stable and cannot collide with the desired nonreal pair because their real parts are strictly below-a. Thus G is Hurwitz, including every coefficient-zero endpoint. The repeated hidden real root is canceled to its full multiplicity below.

## 4. Positive PH normalization and exits

Put

    D0=R(lambda)>0,
    h_i=lambda^(i-1)/D0                (i=1,...,9),
    Delta=diag(h_1,...,h_9).

All coordinates are strictly positive. The actual PH pair is

    T=Delta^(-1)GDelta,
    alpha=(28eta^4,40eta^3 lambda,23eta^2 lambda^2,
           7eta lambda^3,lambda^4,0,0,0,0)/D0.    (4)

In literal entries, T has diagonal-lambda, superdiagonal lambda, and last row

    (f9/lambda^8,f8/lambda^7,f7/lambda^6,
     f6/lambda^5,f5/lambda^4,f4/lambda^3,
     f3/lambda^2,f2/lambda,-lambda).

It is Metzler and Hurwitz. Its first eight rows sum to0. At x=lambda, (3) gives

    P(lambda)=c(a^2+b^2)^2 R(lambda)=K D0>0.

Thus the last row sums to -K D0/lambda^8<0 and its exit vector is

    omega=-T1=(K D0/lambda^8)e_9.                 (5)

All five nonzero entries of alpha are positive and their sum is exactly R(lambda)/D0=1. The superdiagonal path and strictly positive f9 also make this generator irreducible, though that property is not an assumption on any hypothetical smaller representation. Equations (4)–(5) verify an actual transient PH pair, not merely a stable spectral list.

## 5. Full transfer and all four cancellations

For generic x, the first eight rows of (xI-C9)y=e_9 give y_i=x^(i-1)y_1, and the last gives P(x)y_1=1. Hence, as a rational identity,

    e_j^T(xI-C9)^(-1)e_9=x^(j-1)/P(x).

With

    v=28eta^4 e_1^T+40eta^3 e_2^T+23eta^2 e_3^T
      +7eta e_4^T+e_5^T,

the raw transfer is

    v(sI-G)^(-1)K e_9=K R(s+lambda)/P(s+lambda).

The shifted denominator factorization is literal:

    P(s+lambda)=(s+c)((s+a)^2+b^2)^2 R(s+lambda).

Therefore the raw transfer equals H(s), canceling the hidden real pole twice and both hidden complex poles. At x=lambda the same resolvent identity gives Gh=-K e_9; consequently alpha=v Delta and omega=Delta^(-1)K e_9. Diagonal similarity proves

    alpha(sI-T)^(-1)(-T1)=H(s).

No density sampling, spectral-only theorem, or unverified generic PH-existence import is used. The displayed generator, initial row and exit remain well defined at both z=3/4 and z=1.

At the upper endpoint w=5 the exact polynomial is

    p(Y)=Y^9-Y^6-3Y^5-62Y^4-322Y^3
              -61Y^2-620Y-2100.

This is an anchor specialization of the full coefficient proof, not the proof of the interval.

## 6. Evidence and remaining gate

The supported C7 dependency boundary is now the parent's actual `institute/runs/three-area-2026-10-23-96h/priority-written-dispositions-v1.md`, Section2: exact minimum7 on1/2<z<=5935/9126, at the named B6/G7/new-C7 written-check dependencies. Its successor qualification, rather than the defective old PH6 parent timestamp/ellipsis prose, is operative. The new C9 direct construction itself does not need that dependency.

The C8 source is `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`; it remains independently unreviewed at this freeze. Any later composed upper bound must name its actual review, not infer one from this proof.

Companion realization, hidden-mode cancellation and diagonal normalization are classical mechanisms; no worldwide-priority claim is made for this family or its bound. The frozen primary literature/corpus screen and `primary-comparison-003-skewness-and-hidden-modes-v1.md` retain their stated limits. Written construction is not Lean/kernel acceptance. The full minimum-order function and full book question remain open.

The remaining correctness gate is a separate exact written expansion of the whole coefficient table, its full-range signs, the visible/hidden multiplicities, positive normalization and all four transfer cancellations. No scientific execution or review is implied by the word candidate.
