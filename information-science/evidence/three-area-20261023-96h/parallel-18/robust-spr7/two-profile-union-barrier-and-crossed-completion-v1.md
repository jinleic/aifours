# SPR7 continuation v1 — the two midpoint-Euler profiles fail together, but a crossed completion succeeds

Observed `/bin/date` before creation: **Sun Oct 25 03:52:22 PDT 2026**. Owner InfoSPR7, slot info-2. **WRITTEN result, with the specifically identified finite rational identities checked in the owner's eval kernel; pending separate supplied-proof reconstruction.** This is neither proof-assistant/kernel verification nor parent/independent-model acceptance. All outputs stay in this owned root. No native scientific program, solver, background process, network request, external-model CLI or nested agent was started. The global scientific-launch HOLD and the original deadline remain binding.

## 0. Literal advance and exact boundary

The earlier separate controls left open whether selecting between the actual midpoint-even complementary-Euler profile and the actual midpoint-odd derivative profile might cover every robustly Hurwitz degree-seven coefficient box.

**Here that selection mechanism is refuted:** one literal independent monic degree-seven box is strictly Hurwitz for every member, but **both entire real two-component profile spans fail on that same box**. The failure persists in the explicit all-seven-width enlargement in §7. Thus neither parameter adjustment, either whole two-dimensional span, nor their UNION is a universal certificate.

This is an exact barrier, **not** a counterexample to unrestricted SPR7. In fact an explicit rational monic degree-seven numerator outside either span is supplied for this very box, with the global margin `P >= (1/2)(1+t)^7`. It simply crosses the even anchor from one profile with the odd anchor from the other. An integer positive-coefficient certificate, not a numerical root or feasibility search, establishes that margin. The full-width enlargement retains the same numerator and margin at least `(1/4)(1+t)^7`.

**What remains open:** unrestricted degree-seven universality, universality of the four-component hybrid span, and any equivalence of unrestricted synthesis with an even-profile condition. The old fixed-M reciprocal obstruction has not been promoted to an obstruction over all admissible numerators or all normalization constants. The delivered alternative is the task's **documented exact barrier with a named next representation**, stronger than separate profile countercontrols.

## 1. Frozen imports and what is actually consumed

1. `even-euler-comparator-candidate-v1.md`, SHA256 `ec744ccc6b269bb935aaa95e075cc559cda0ca6c44cc6bd580144306edc3c61a`: its §§1–3 define the normalized actual midpoint even cubic `F=E_mid/m_1`, complementary polynomial `H=4F-tF'`, pairing, and profile `F(-s^2)+epsilon*s*H(-s^2)`. Its sufficient budget and positive application are **not** used as premises for the new box or numerator.
2. `even-euler-entire-profile-obstruction-v1.md`, SHA256 `cf7d75fac33d83ffa93cf5af5d3f277753585375345fb38f4a18e6e511a2368f`: its §§4–5 supply the component-annihilation strategy and whole-span/zero-frequency distinction. Its reciprocal normalization and optional transferred positive witness are **not** used in the new proof.
3. Run-root `spr7-even-euler-parent-v1.md`, SHA256 `ebb381e5a7d78ee4d0c0541fa374052b5f8cbabb3ce0c22c0983a7a55a8ed06e`, and `wave-v17-partial-parent-dispositions-v1.md`, SHA256 `208b2a66fd3b012a554e6f93e1af12f8910ef2615ab866b142e31dfc33276450`: read at their stated sufficient/profile-obstruction scopes. Those dispositions do not accept this new box or certificate in advance.

Classical imports used below are the real intermediate-value theorem and polynomial degree/root counting, the degree-seven Hermite–Biehler criterion in the orientation written in §3, elementary polynomial algebra and root continuity. No sextic existence theorem, Lean development, numerical computation or prior positive-margin export is imported. Euler differentiation, diagonal midpoint scaling and positive-coefficient interval certificates have classical antecedents; novelty is **UNCLEAR**.

## 2. One literal two-width independent box

Write

`a_(x,c)(s)=s^7+x*s^6+A*s^5+B*s^4+K*s^3+C*s^2+c*s+D`,

where

`A=10000001050`, `B=50025025`,

`K=10500000050000`, `C=25025012500`, `D=12500000000`,

and the two coefficients vary **independently** over

`1 <= x <= 99`,

`10000000000000 <= c <= 990000000000000`.

All other intervals are degenerate and positive. Define

`c_0=500000000000000`, `Delta=490000000000000`.

The actual components are

`E_x(t)=-x*t^3+B*t^2-C*t+D`,

`O_c(t)=-t^3+A*t^2-K*t+c`.

The actual midpoint has `x_0=50`, `c=c_0`. Consequently its normalized even and monic odd anchors are exactly

`F(t)=E_50(t)/50=-(t-1/2)(t-500)(t-1000000)`,

`Q(t)=O_(c_0)(t)=-(t-50)(t-1000)(t-10000000000)`.

In coefficient form,

`F=-t^3+(2001001/2)t^2-500500250*t+250000000`.

These are the actual prescribed midpoint anchors, not roots chosen after seeing a failing frequency.

## 3. Every member is strictly Hurwitz, including both closed endpoints

The following tables give the signed endpoint value closest to zero: a positive entry is a lower bound over the whole indicated coefficient interval, and a negative entry is an upper bound. The affine dependence on x or c makes checking the two endpoints sufficient. Every displayed value was checked with exact rational arithmetic.

| t | Signed bound for E_x(t), 1<=x<=99 |
|---|---:|
| 2/5 | 312249874708/125 > 0 |
| 3/5 | -312124811402/125 < 0 |
| 400 | -1993565000000 < 0 |
| 600 | 2985117500000 > 0 |
| 400000 | 1657994007500000000 > 0 |
| 60000000 | -35911411500737500000000 < 0 |

| t | Signed bound for O_c(t), c_0-Delta<=c<=c_0+Delta |
|---|---:|
| 3/5 | 462949996297223/125 > 0 |
| 200 | -709999976000000 < 0 |
| 600 | -1709999868000000 < 0 |
| 1100 | 559999884500000 > 0 |
| 1000000000 | 8999990549999960000000000000 > 0 |
| 20000000000 | -3999999790000000010000000000000 < 0 |

Thus every E_x has exactly one simple positive root in each of

`(2/5,3/5)`, `(400,600)`, `(400000,60000000)`,

and every O_c has exactly one simple positive root in each of

`(3/5,200)`, `(600,1100)`, `(1000000000,20000000000)`.

Each set exhausts a cubic's degree. The six intervals are disjoint and strictly ordered

`e_1 < o_1 < e_2 < o_2 < e_3 < o_3`.

Both components have positive constants and negative leading coefficients. Equivalently O_c has signs `+,-,+` at the three roots of E_x. This is precisely the degree-seven Hermite–Biehler orientation for the monic polynomial `E_x(-s^2)+s O_c(-s^2)`. Hence every original denominator is strictly Hurwitz, for **every independent pair (x,c)** and both closed endpoints. No pairing/cancellation assumption is used to infer this base stability.

## 4. The entire actual midpoint-odd derivative span fails

Let

`D_Q(t)=(t Q(t))'=-4t^3+3A*t^2-2K*t+c_0`.

Exact substitutions give

`D_Q(20)=91999999228000 > 0`,

`D_Q(30)=-103000000273000 < 0`.

Throughout `[20,30]`,

`D_Q'(t)=-12t^2+6A*t-2K <= 180A-2K`

`                                      =-19199999911000 < 0`.

Therefore there is exactly one simple root `tau in (20,30)`. This rational isolator is the exact specification of the finite algebraic squared frequency; no decimal root is needed. Q is positive there because all t are below its first root 50. Also

`Q'(t)=-3t^2+2A*t-K <= 60A-K=-9899999987000 < 0`,

and

`Q(20)=293999999412000 < Delta=490000000000000`.

For the actual lower-c member, `O_-(tau)=Q(tau)-Delta<0`.

Consider **all real u,v** in

`b_(u,v)(s)=u D_Q(-s^2)+v s Q(-s^2)`.

For the single actual denominator `a_(1,c_0-Delta)`, the pairing at tau is

`P_(a,b)(tau)=v*tau*Q(tau)*O_-(tau)`.

It is negative for v>0 and zero for v=0, independently of u. If v<0, the pairing has negative leading term `v*t^7`, so it is negative at sufficiently large finite t. Thus **the whole real two-dimensional odd-profile span fails**, not merely a scalar budget or positive normalization. The original exact-degree-seven condition is included; v=0 additionally fails even if one relaxes that condition.

## 5. The entire actual midpoint-even complementary-Euler span also fails

The actual complementary polynomial is

`H(t)=4F(t)-tF'(t)`

`    =-t^3+2001001*t^2-1501500750*t+1000000000`.

At the rational endpoints,

`H(2000000)=1000999500000000 > 0`,

`H(3000000)=-8995495501250000000 < 0`.

Moreover `H''(t)=-6t+4002002 <= -7997998<0` on that interval, and

`H'(2000000)=-3997497500750<0`.

Hence H has exactly one simple root `sigma in (2000000,3000000)`. All roots of F are at most 1000000, so `F(sigma)<0`.

For the same actual lower-x member, and every t in the entire isolating interval,

`E_1(t)=-t^3+B*t^2-C*t+D`

`       >= -(3000000)^3+B*(2000000)^2-C*3000000+D`

`       =173025024975000000000 > 0`.

Now take **all real u,v** in

`b_(u,v)(s)=u F(-s^2)+v s H(-s^2)`.

If u>0, its pairing with the same `a_(1,c_0-Delta)` at sigma is

`P_(a,b)(sigma)=u F(sigma)E_1(sigma)<0`,

independently of v. If u<=0, its pairing at zero is

`u F(0)D <= 0`.

Therefore **the whole real two-dimensional even-profile span fails on this very same box**. Sections 4–5 refute the UNION of the two profiles at their actual, simultaneously prescribed midpoint anchors. They do not exclude sums of the two spans or arbitrary numerator coefficients.

## 6. An explicit crossed completion, with an exact all-frequency certificate

Set `k=10000000000` and define

`N(s)=k F(-s^2)+s Q(-s^2)`.

This is a monic real polynomial of exact degree seven with all rational, indeed integer, coefficients:

`N(s)=s^7+10000000000*s^6+10000001050*s^5`

`       +10005005000000000*s^4+10500000050000*s^3`

`       +5005002500000000000*s^2+500000000000000*s`

`       +2500000000000000000`.

Its even component comes from the even profile and its odd component from the odd profile, not either profile's Euler companion. Q is not proportional to H (their monic t^2 coefficients differ), and D_Q is not proportional to F (their leading-coefficient ratio 4 does not match their t^2 coefficients). Thus N is outside both excluded two-dimensional spans, but inside their four-dimensional sum.

### 6.1 Exactly what the finite certificate proves

For each of the four endpoint pairs

`x in {1,99}`, `c in {10000000000000,990000000000000}`,

form the integer polynomial

`G_(x,c)(t)=2[E_x(t)*kF(t)+t O_c(t)Q(t)]-(1+t)^7`.

The companion `two-profile-union-barrier-rational-certificate-v1.json` contains the literal eight ascending coefficients of every G, all 128 integer transformed coefficients, the following formulas and their strict signs. Nothing is inferred from finite frequency evaluations.

For `G(t)=sum_(r=0)^7 g_r t^r` and a finite interval `[a,b]`, put

`T_(a,b)(u)=S*(1+u)^7*G((a+b*u)/(1+u))`.

The coefficient of u^j is exactly

`C_j=S*sum_(r=0)^7 g_r`

`          *sum_(h=max(0,j-(7-r)))^min(r,j)`

`             binom(r,h)*a^(r-h)*b^h*binom(7-r,j-h)`.

For the tail `[T,infinity)`, use `G(T+u)` with coefficient

`C_j=sum_(r=j)^7 g_r*binom(r,j)*T^(r-j)`.

All these formulas are finite integer/rational identities. The four regions and multipliers are:

| Region | Interval | Transformation multiplier S |
|---|---|---:|
| 0 | [0,3/5] | 5^7=78125 |
| 1 | [3/5,500] | 5^7=78125 |
| 2 | [500,10000000000] | 1 |
| 3 | [10000000000,infinity) | Tail translation, no multiplier |

The exact computed coefficient lower bounds are tabulated below. An entry q means **each of the eight transformed integer coefficients is at least `10^q`**, not a floating approximation to a minimum.

| x | c | Region 0 | Region 1 | Region 2 | Region 3 |
|---:|---:|---:|---:|---:|---:|
| 1 | 10000000000000 | 32 | 32 | 33 | 0 |
| 99 | 10000000000000 | 32 | 32 | 33 | 0 |
| 1 | 990000000000000 | 33 | 34 | 33 | 0 |
| 99 | 990000000000000 | 33 | 34 | 33 | 0 |

Positive coefficients imply positive transformed polynomial for all u>=0. In a finite region u covers `[a,b)`, and the positive leading coefficient separately gives `G(b)>0`; both closed endpoints are included. Tail translation covers every remaining finite t. Thus every corner has

`P_(a,N)(t) >= (1/2)(1+t)^7`, `t>=0`.

The pairing is affine in each of the two independent uncertain coefficients, so every interior denominator is a convex combination of these four corner pairings **at the same t and the same fixed numerator**. The same bound therefore holds on the entire original box. Since its denominators were already proved Hurwitz in §3, N is a genuine common strict SPR numerator, without a cancellation argument or an assumed stability consequence of a solver status. The bound includes zero and the whole finite-frequency tail.

## 7. The barrier and the completion persist with ALL SEVEN widths positive

This is an ancillary strengthening of the same control, not an additional discovery count. Let

`delta=1/1000000000000000000000`.

Expand every one of the seven base coefficient intervals by delta at both endpoints: the x interval becomes `[1-delta,99+delta]`, the c interval becomes `[c_0-Delta-delta,c_0+Delta+delta]`, and each of A,B,K,C,D becomes its symmetric interval of radius delta. All endpoints remain positive and all seven widths are strictly positive. All midpoints are unchanged, so F,Q,H,D_Q remain **exactly the actual midpoint profiles**. The original lower-c/lower-x denominator remains a member; both profile-span obstructions are unchanged.

To prove both stability and the fixed numerator's positivity for the enlarged box, clip each coefficient of an enlarged member a to its original interval, obtaining `a^0` in the stable base box. Each of the seven coefficient errors has magnitude at most delta. Hence, for t>=0,

`|E_a-E_(a^0)| <= delta(1+t+t^2+t^3) <= delta(1+t)^3`,

`|O_a-O_(a^0)| <= delta(1+t+t^2) <= delta(1+t)^2`.

The sum of the eight positive coefficients of N is exactly

`C_N=7515518025000051051 < 10^19`.

Separating that sum into its even and odd parts gives

`|P_(a,N)-P_(a^0,N)| <= delta*C_N*(1+t)^7 < (1/100)(1+t)^7`.

Combining with §6 yields, in particular,

`P_(a,N)(t) >= (1/4)(1+t)^7 > 0`.

This bound is algebraic and does not presume the enlarged member stable. Interpolate linearly from its stable clipped member to a. The full path remains in the expanded coefficient box and satisfies the strict pairing bound. An imaginary-axis denominator zero would force the pairing to vanish, contradiction. Fixed monic degree and bounded path coefficients prevent root escape through infinity. Root continuity therefore proves every enlarged denominator strictly Hurwitz before any cancellation. The same fixed N is a common monic exact-degree-seven SPR numerator for the **full independent seven-width box**.

## 8. The next representation is a hybrid cone, not another scalar-budget repair

The exact barrier is now stronger than the previous two separate examples:

- Robust Hurwitzness does not force successful selection from the UNION, even when each profile is enlarged to its entire real two-component span and all seven widths are positive.
- Thus no improvement in either scalar sufficient budget, nor a test that merely picks one of those two whole spans, can be a universal proof.
- The four-dimensional sum can succeed when the union fails: the explicit N above uses the crossed components F and Q. This is a literal witness, not a claim that arbitrary blending always works.

The next named representation is the **four-coefficient hybrid cone**

`E_b(t)=alpha F(t)+beta D_Q(t)`,

`O_b(t)=gamma H(t)+zeta Q(t)`,

with one common real quadruple `(alpha,beta,gamma,zeta)` and exact corner pairings on `t>=0`. The present witness is `(k,0,0,1)`. On an arbitrary independent seven-coefficient box there are at most 128 coefficient corners; checking all their full-half-line pairings is sufficient for a fixed quadruple, but finding or proving the existence of such a quadruple remains a genuine mathematical obligation. This four-dimensional cone is **not** asserted equivalent to the unrestricted eight-coefficient numerator space.

If the hybrid cone fails, the next logically unrestricted representation is a pair of independent degree-at-most-three numerator cubics `(E_b,O_b)`, with the leading coefficient of O_b negative to ensure a positive monic degree-seven normalization. A dual obstruction must separate that entire eight-dimensional numerator cone, not merely the Euler companions. No such obstruction is delivered here. No claim of branch (b)'s all-M obstruction or branch (c)'s characterization is made.

## 9. Verification and parkable state

The owner kernel used only Python exact integers, `fractions.Fraction`, binomial coefficients and finite polynomial arithmetic. Specifically checked were: the §3 signed endpoint bounds; the §4–5 rational isolator endpoint values and derivative bounds; expansion of N; all four G coefficient vectors; all 128 exact transformed coefficients and their positive lower-bound exponents; and `C_N<10^19`. No floats, native scientific process, CAS import, solver or asynchronous work were used. The four-region certificate was selected after exact positive-coefficient exploration, not preregistered or independently implemented.

The analytic coverage of continuous coefficient boxes, algebraic frequencies, whole real half-line, closed endpoints and root-continuity stability is **WRITTEN** at the named classical imports. The finite arithmetic identities are **WRITTEN-checked-in-kernel**, not formal theorem checking. Neither an independent reviewer nor the parent has reconstructed these new bytes yet. No novelty, publication, human, cross-vendor or Lean/kernel claim is made.

The exact remaining gap is **unrestricted universal SPR7**, with the hybrid-cone existence/obstruction question as the next representation. This new barrier and explicit completion are a complete parkable result; no native run or hold release is required to interpret them.
