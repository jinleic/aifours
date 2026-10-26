# Independent in-harness reconstruction: seven-state PH with a canceled complex pair

Observed before creation: **2026-10-23T15:00:22-0700 PDT**. Reviewer MathShor, primary slot math-5. Parent-priority bounded review only; no author files modified, scientific program, symbolic algebra system, numerical root routine, solver, Lean, CLI model or nested agent used.

## Pin and verdict

Complete author source read: `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/proof-seven-state-complex-hidden-extension-v1.md`, all 314 lines. Independently observed SHA256:

    023ac8611a66263233288838eaf3dcd3ac0013111a5be93fb5974e7f47e39667

This exactly matches the parent's assigned pin. The current PH selection was read in full, as were the full B6 manuscript and inherited G7 manuscript. I read the actual B6 parent disposition with its additive residual-notation correction and the actual G7 parent disposition, rather than relying only on the new author's description.

**Verdict: 0 FATAL / 0 MAJOR / 0 substantive MINOR at the stated upper-construction and composed-band boundaries.** The full parameter ranges, nonreal stable hidden pair, nonnegative numerator, literal PH pair and exact cancellation reconstruct correctly. The exact-minimum statement uses the separately supported unrestricted B6 and older G7 at precisely their stated ranges; it is not an unconditional result detached from those written-check dependencies. No novelty, formal/kernel, human or general-book acceptance follows.

## 1. Whole characteristic polynomial, not a finite anchor test

Use J=m+1, L=m^2+6m+17, Q=L-2w and B=12-2w. Direct multiplication gives

    (Y-J)(Y^2+(m+5)Y+Q)=Y^3+4Y^2+BY-JQ,
    (Y^2-2Y+w)^2=Y^4-4Y^3+(4+2w)Y^2-4wY+w^2.

Multiplying these two polynomials yields the complete coefficient list, in descending order:

    1,
    -4+4=0,
    (4+2w)-16+B=0,
    -4w+4(4+2w)-4B-JQ =12w-32-JQ,
    w^2-16w+B(4+2w)+4JQ =-3w^2+48+4JQ,
    4w^2-4wB-JQ(4+2w) =12w^2-48w-4JQ-2JQw,
    Bw^2+4JQw =w[(12-2w)w+4JQ],
    -JQw^2.

The Y^4 coefficient equals the author's less simplified form:

    4w+4(m+3)^2-(m+5)Q,

because their difference is 4[(m+3)^2+8-2w-Q]=0. Thus every coefficient in the table and all feedback signs in equation (1) are bound to the full factorization, including the two zero coefficients. This is a coefficient-by-coefficient symbolic reconstruction, not an inference from values of m or w.

With eta=d/m and lambda=a+eta,

    lambda-Jeta=c,       lambda-eta=a.

Hence the literal shifted factorization is exactly

    P(s+lambda)=(s+c)((s+a)^2+b^2)^2 R(s+lambda),

with no omitted multiplicity or real-root assumption for the quadratic.

## 2. Family A signs and endpoints

At m=8, J=9, Q=129-2w, and the simplified feedbacks are exactly

    A3=1193-30w,
    A4=3w^2+72w-4692,
    A5=-48w^2+2298w+4644,
    A6=w(2w^2+60w-4644),
    A7=9Qw^2.

On 36≤w≤1193/30<40, Q≥742/15>0. A3 is nonnegative with only its upper-end zero. A4 is increasing and its lower-end value is1788. The A5 bound 2298-48w>378 leaves it strictly positive; the A6 parenthesis is increasing and equals108 at w=36. A7 is strictly positive.

The discriminant of R/eta^2 is 8w-347≤-433/15<0, so the hidden roots are genuinely nonreal throughout this closed interval. The z range is exactly

    [35/64,1163/1920].

No endpoint uses a limiting PH construction.

## 3. Family B: every sign and both rational identities

For 13/2≤m≤8,

    w=(m^2+23)/2-56/(m+7),
    Q=6m-6+112/(m+7),

so Q=L-2w. The identity

    2(m+7)w=(m+1)L+32

makes the simplified A3=JQ-12w+32 vanish identically.

The endpoint values are

    w(13/2)=6151/216,       w(8)=1193/30,
    Q(13/2)=1115/27,        Q(8)=742/15.

The derivatives w'=m+56/(m+7)^2 and Q'=6-112/(m+7)^2 are positive on this interval. Thus 28<w<40, 41<Q<50 and 15/2≤J≤9 hold at every point, including both endpoints. The lower bounds A4>504 and the A5 inner factor>183 follow with the correct signs; A7>0 follows from Q,w,J>0.

For the remaining A6 sign put t=m+7, A=t^2-14t+72 and w=A/2-56/t. Multiplication gives

    2t^2E
      =t^2[A^2+(8t-60)A-8(t-6)(t^2-8t+24)]
        -224tA-896t^2+6720t+12544.

The bracket expands to

    t^4-28t^3+280t^2-1176t+2016.

Consequently

    2t^2E=t^6-28t^5+280t^4-1400t^3
               +4256t^2-9408t+12544=F(t),

which independently reconstructs identity (5).

For q=27/2, the coefficients of F(q+r) are obtained by the following direct binomial expressions:

| Power | Reconstructed coefficient |
|---|---|
| r^6 | 1 |
| r^5 | 6q-28=53 |
| r^4 | 15q^2-140q+280=4495/4 |
| r^3 | 20q^3-280q^2+1120q-1400=23795/2 |
| r^2 | 15q^4-280q^3+1680q^2-4200q+4256=1008911/16 |
| r | 6q^5-140q^4+1120q^3-4200q^2+8512q-9408=2175765/16 |
| 1 | F(q)=962305/64 |

Every displayed coefficient is strictly positive. Since r=m-13/2≥0 and t>0, E>0 and A6>0 on the entire interval, not only at a rational anchor.

The hidden discriminant is

    (m+5)^2-4Q=(m-7)^2-448/(m+7)<0:

its first term is at most1 and the subtracted term is at least448/15>1. The pair remains genuinely complex at every parameter.

## 4. Continuous range bridge and absence of an IVT gap

Exact simplification gives

    Z(m)=(w-1)/m^2
        =1/2+(21m+35)/(2m^2(m+7)).

This rational function has no denominator zero on [13/2,8]. For the fraction without its factor1/2, the derivative numerator is

    21m^2(m+7)-(21m+35)(3m^2+14m)
      =-14m(3m^2+18m+35)<0.

Thus Z is continuous and strictly decreasing, with endpoints1163/1920 and5935/9126. Every value between those endpoints is achieved exactly once. Equation 2(z-1/2)m^2(m+7)=21m+35 specifies that m exactly; no numerical root evaluation is required.

Family A ends where B starts. The new literal construction covers the entire closed interval

    35/64≤z≤5935/9126.

It does not by itself cover z=1/2; that portion correctly remains the inherited G7 input.

## 5. Actual PH matrix, positive h, exits and transfer

The upper-shift companion C has characteristic P: solving (xI-C)y=e7 gives y_i=x^(i-1)y_1 from its first six rows, and the last row gives P(x)y_1=1. This also proves

    e_j^T(xI-C)^(-1)e7=x^(j-1)/P(x)

as a rational identity.

All off-diagonal feedbacks are nonnegative on both families, so G=C-lambda I is Metzler. Its visible eigenvalues are -c and -a±ib, the latter pair each twice. R(x) has both roots in the open left half-plane since m+5>0 and Q>0. After subtracting lambda>0, their real parts become

    -lambda-(m+5)eta/2=-a-(m+7)eta/2<-a<0.

The discriminant checks above make them nonreal throughout. Hence G is Hurwitz, including every zero-feedback endpoint; no diagonalizability assumption enters.

Let D0=R(lambda)>0 and h_i=lambda^(i-1)/D0. Its coordinates are strictly positive. Direct row multiplication gives Gh=0 in its first six coordinates and

    (Gh)_7=-P(lambda)/D0=-K,

because the factorization gives P(lambda)=K D0. Therefore T=Delta^(-1)GDelta has first six row sums0 and last sum -KD0/lambda^6<0. Its off-diagonal entries are exactly the listed nonnegative feedbacks divided by powers of lambda and its superdiagonal equals lambda. Similarity preserves the Hurwitz spectrum, proving genuine transience.

For v=(Qeta^2,(m+5)eta,1,0,0,0,0),

    alpha=vDelta
      =(Qeta^2,(m+5)eta lambda,lambda^2,0,0,0,0)/D0.

All its nonzero entries are strictly positive, and their sum is R(lambda)/D0=1. The exit vector is Delta^(-1)Ke7=KD0/lambda^6·e7.

Finally the companion resolvent gives

    v(sI-G)^(-1)Ke7=K R(s+lambda)/P(s+lambda)=H(s),

and diagonal similarity gives the identical alpha(sI-T)^(-1)(-T1). This checks input/output orientation, normalization and cancellation of the WHOLE stable complex quadratic with a nonnegative numerator. It is not merely a spectrum realization.

## 6. Rational anchor and both shifted positive certificates

At m=7, w=32 and Q=44. The feedback formulas give

    A3=0, A4=1616, A5=13184, A6=8192, A7=360448,

hence exactly

    p(Y)=Y^7-1616Y^3-13184Y^2-8192Y-360448.

The hidden quadratic is Y^2+12Y+44, whose roots are -6±2sqrt(2)i. Shifting by lambda=a+d/7 gives the stated hidden PH poles -a-d±(2sqrt(2)d/7)i.

In addition to reconstructing the all-m degree-six F shift in section3, I hand-expanded the anchor at its positive root8. With X=Y-8,

    p(X+8)=X·[X^6+56X^5+1344X^4+17920X^3
                    +141744X^2+636160X+1305600].

Every coefficient in the degree-six bracket is positive. For example its bottom three coefficients arise as

    143360-1616=141744,
    688128-24·1616-13184=636160,
    1835008-192·1616-16·13184-8192=1305600.

The constant p(8)=0 follows from the exact integer cancellation2097152=827392+843776+65536+360448. These anchor identities are corroborating exact written algebra; they do not substitute for the full parameter proof.

## 7. Composed exact-seven band: actual dependencies and endpoints

Observed inherited source hashes match the author's pins:

- B6: `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`.
- Old G7: `59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`.
- Actual B6 parent disposition: `4b44cea16813f39b9634904ce0b0823f3bca1dddcc654eb746f3c37dc18a6b0b`.

B6's actual disposition supports the topology-unrestricted statement order≤6 iff z≤1/2. Its exclusion for z>1/2 has no upper parameter cutoff, so it applies throughout this new construction's interval. The disposition explicitly treats z=1/2 separately: order6 exists and the order5 trace obstruction applies, hence minimum6 there. Its additive correction fixes only residual beta-versus-beta-squared notation, not the theorem.

The old G7 parent disposition supports upper7 on [1/2,53/96]. The overlap with the present lower endpoint is exact:

    53/96-35/64=1/192>0.

Thus the union covers [1/2,5935/9126]. Composing with B6 yields minimum exactly7 on

    1/2<z≤5935/9126,

and NOT at z=1/2. No maximum-PH7 theorem above the upper endpoint or global minimum-order solution follows. Historical G7's earlier “six or seven” wording is its original pre-B6 boundary, not a contradiction of the later supported B6 composition.

I have read B6's complete body to bind its unrestricted scope, but this review does not replace its already completed separate reconstruction with a new formal proof audit of the entire baseline source chain. The newly reviewed seven-state construction itself requires no PH-existence theorem import.

## Findings and limits

- **FATAL / MAJOR / substantive MINOR:** none found at the reviewed scopes.
- **Supported by this reconstruction:** both continuous parameter families, every coefficient/sign identity, nonreal stable hidden cancellation, literal PH generator/initial/exit pair, and the stated interval union/composition at the named B6/G7 boundaries.
- **Not supported:** novelty, priority, human or kernel verification, unrestricted order7 impossibility above the endpoint, full H_(1,2) minimum function or the general book question.
- **Review relation:** different in-harness task agent, supplied pinned proof and shared steering; not blind, cross-vendor or human review.

The assigned bounded reconstruction is complete. I return to the Shor completion-shape consolidation gate.
