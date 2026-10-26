# SPR7 actual box — an explicit unrestricted common numerator and exclusion of ALL EIGHT moment balances

Actual `/bin/date` observation before creation: **Sun Oct 25 07:20:37 PDT 2026**. InfoSPR7 / info-2. **NEW WRITTEN CANDIDATE, pending separate supplied-proof reconstruction.** No scientific interpreter/eval/program, symbolic calculation, enumeration, sampling or certificate replay was used. All comparisons below are written exact algebra. Metadata/source reads only. HOLD/v7/v8 and all earlier assurance corrections remain binding.

## 0. Literal answer and scope

The accepted actual seven-width box that defeats the four-component midpoint hybrid nevertheless has an explicit common monic degree-seven numerator. The missing ingredient is to move the numerator's middle odd root from the denominator-midpoint scale R/4 to the fixed value 1000, while leaving the last odd root at T.

The numerator is

`N(s)=kappa F(-s^2)+s Q_*(-s^2)`,

`kappa=T^2/(100R)`,

`Q_*(t)=-(t-50)(t-1000)(t-T)`.

It is common to ALL members of the literal box, not selected by denominator or frequency. The written proof below gives

`P_(a,N)(t)>=(1/20000)(1+t)^7`

for every member of the ALL-SEVEN-POSITIVE-width enlargement and every finite t>=0, including zero. Its monic leading ratio is one. Thus an actual positive balance annihilating all eight numerator coordinates cannot exist on this box. The eight equations and their contradiction are written explicitly in §8.

This resolves only the unrestricted numerator problem for THIS literal box. It is not a universal SPR7 theorem, and does not revive universality of the four-component midpoint hybrid. No novelty, formal/kernel, human, cross-vendor or parent acceptance is claimed for this new construction.

## 1. Exact accepted box and imports

Read in full: run-root `spr-actual-box-parent-v1.md`, freshly observed SHA256 `ca6e2434e423f1b61a1e25cdf759e02f39d4614d7ed0afabb24fd24b91216892`. Its accepted scope supplies strict Hurwitzness of the base box and its radius-delta independent seven-width enlargement, strict crossed gain failure, and failure of the entire fixed four-component midpoint hybrid. Its assurance remains same-harness written reconstruction at named imports.

Retain

`R=10^18`, `T=R^3`, `delta=1/(100T^4)`,

`A=T+R/4+50`, `B=50R+25025`,

`K=(R/4+50)T+(25/2)R`,

`C=25025R+12500`, `D_0=12500R`.

The base box is

`a_(x,c)(s)=s^7+x s^6+A s^5+B s^4+K s^3+C s^2+c s+D_0`,

`1<=x<=99`, `RT/4<=c<=99RT/4`, independently.

Its actual components are

`E_x=50F+(50-x)t^3`,

`F=-(t-1/2)(t-500)(t-R)`,

`O_c=Q+d`, `Q=-(t-50)(t-R/4)(t-T)`,

`d=c-(25/2)RT`, `|d|<13RT`.

The accepted enlargement expands EACH of the original seven coefficient intervals by delta at both ends; all seven widths are positive and all midpoints unchanged. No correlated family or abstract frequency rectangle replaces this box.

The only non-elementary imports used for the new numerator are elementary compactification/corner identities from the v32-H-supported full-space alternative and the already accepted actual-denominator stability above. The positivity proof itself is self-contained algebra, triangle inequalities and completing a square. The old unadmitted computational data are not premises.

## 2. Eight literal numerator coefficients

The new monic polynomial is

`N(s)=s^7+kappa s^6+(T+1050)s^5`

`      +kappa(R+1001/2)s^4+(1050T+50000)s^3`

`      +kappa((1001/2)R+250)s^2+50000T s+250kappa R`.

Every coefficient is a fixed positive rational number. Its even component is kappa F and its odd component is Q_*. It is not the old crossed numerator with odd part Q. Nor is positivity inferred from a four-component compression: the preceding accepted hybrid obstruction, together with the positive proof here, means N lies outside that fixed hybrid image.

Put

`f(t)=(t-1/2)(t-500)`, `g(t)=(t-50)(t-1000)`,

`F=(R-t)f`, `Q_*=(T-t)g`.

The exact base pairing is

`P_(x,c)(t)=kappa F(t)E_x(t)+t(T-t)g(t)[(T-t)(t-50)(t-R/4)+d]`.   (P)

This identity, not a finite frequency grid, is used throughout. The proof divides the ENTIRE half-line into `0<=t<=M`, `M<=t<=100R`, and `t>=100R`, where `M=10^6`.

## 3. An exact low-scale polynomial bound, uniform in the uncertain c

Write `h=4c/(RT)`, so `1<=h<=99`. Define the quartic comparison polynomial

`L_h(t)=(1/2)f(t)^2+(t/4)g(t)(h-t)`.

We first prove the explicit GLOBAL bound

`L_h(t)>=(1/20000)(1+t)^4`, for all t>=0 and 1<=h<=99.        (L)

L_h is affine in h. Its minimum is at h=1 where g>=0 (t<=50 or t>=1000) and at h=99 where g<=0 (50<=t<=1000). The following estimates cover all boundaries and roots:

1. **0<=t<=1.** Both terms for h=1 are nonnegative. If `|t-1/2|>=1/10`, the even square is already greater than one. Otherwise `2/5<t<3/5`, and

   `t(50-t)(1000-t)(1-t)/4>1`.

   Thus L_h>1, enough since `(1+t)^4<=16`.

2. **1<=t<=50.** The only negative term is bounded using `t(t-1)<(t-1/2)^2` and `(50-t)(1000-t)<=50000`. Since `2(500-t)^2>=405000`,

   `4L_1>=355000(t-1/2)^2`.

   This is greater than `(1+t)^4/2` after weakening constants, and in particular implies L.

3. **50<=t<=99.** Now `t(99-t)<(t-1/2)^2`, `(t-50)(1000-t)<=50000`, and `2(500-t)^2>=321602`. Hence

   `4L_99>=271602(t-1/2)^2`,

   again much stronger than L (use `t-1/2>=t/2` and `(1+t)^4<=16t^4<=160000t^2`).

4. **99<=t<=1000.** The odd term for h=99 is nonnegative. If `|t-500|>=t/10`, the even square is at least `t^4/800`. Otherwise `450<t<560`, and

   `t-50>(4/5)t`, `1000-t>(3/4)t`, `t-99>(3/5)t`.

   The odd term is then greater than `(9/100)t^4`. Either lower bound implies L because `(1+t)^4<=16t^4` and `12800<20000`.

5. **t>=1000.** Use `(t-1/2)^2>t(t-1)` to obtain

   `4L_1>=(t-1/2)^2[t^2-950t+450000]`.

   Here the bracket is at least t^2/2: its difference from t^2/2 vanishes at1000 and has positive derivative thereafter. Thus `L_1>=t^4/32`, which again implies L.

No parameter limit or computed quartic roots are used. This lemma remains a finite-scale written inequality for every real t.

## 4. Low frequencies 0<=t<=M: control of ALL finite-R,T corrections

Let `Y=1-t/T` and

`e_x(t)=-x t^3+25025t^2-12500t`,

so `E_x=50R f+e_x`. Direct expansion of P gives

`P/(RT^2)=L_h+Err_low`,

where

`Err_low= -(t/(2R))f^2 +(1/(100R))(1-t/R)f e_x`

`          +(t/4)(Y-1)g(h-t)+(t^2/R)Yg(t-50)`

`          -(t^2/(RT))Yg(t-50)(t-R/4)`.                 (EL)

This is an exact identity, not a formal asymptotic expansion. For `w=1+t`, use

`|f|<=500w^2`, `|e_x|<40000w^3`,

`|g|<=50000w^2`, `|h-t|<=99w`,

`|(t-50)(t-R/4)|<=50R w^2`,

and `0<Y<=1`, `0<1-t/R<=1` in this region. Bounding the five displayed terms separately gives the conservative uniform estimate

`|Err_low| <= [4*10^6 M/R+4*10^6 M^2/T] w^4`

`           <(1/40000)w^4`.                              (EB-L)

For clarity, the R-denominator terms are bounded by `125000 M/R`, `200000(1+M)/R`, and `2500000 M/R`, times w^4. The T-denominator terms are at most `1237500 M/T` and `2500000 M^2/T`, times w^4. Their displayed aggregate uses only M>=1. The final strict comparison uses the stipulated exact M,R,T; no arithmetic interpreter was run.

Combining L and EB-L proves

`P_(x,c)(t)>=[RT^2/40000](1+t)^4>0`, `0<=t<=M`.         (LOW)

This includes zero and the two low even roots, where the retained odd term is essential.

## 5. Middle frequencies M<=t<=100R: a positive finite-scale comparison

Put `u=t/R`,

`fhat=(1-1/(2t))(1-500/t)`,

`ghat=(1-50/t)(1-1000/t)`.

Both hats are in (0,1], with `1-fhat<=501/t` and `1-ghat<=1050/t`. Write

`E_x=Rt^2[50-xu+epsilon]`,

`epsilon=25025/R-25025/t-12500/(Rt)+12500/t^2`.

In this region

`|epsilon|<=25027(1+u)/t`.

The exact even contribution to P/(T^2 R t^4) differs from

`(1/100)(1-u)(50-xu)`

by at most

`[1500/t](1+u^2)`.

Indeed expand `fhat(50-xu+epsilon)`; use `|1-u|<=1+u`, `|50-xu|<=50+99u`, and

`501(50+99u)+25027(1+u)<=75000(1+u)`.

For the odd contribution set `delta_c=d/(TRt)`, so `|delta_c|<13/t`. Its exact normalized form is

`Y ghat [Y(1-50/t)(u-1/4)+delta_c]`.

Its difference from `u-1/4` is at most

`[1113/t+2t/T](1+u^2)`:

all multiplicative factors lie in [0,1], their combined deficit is at most `1100/t+2t/T`, and `|u-1/4|<=1+u^2`.

Consequently P/(T^2 R t^4) differs from the explicit comparison polynomial

`H_x(u)=1/4+(1/2-x/100)u+(x/100)u^2`

by less than

`[3000/M+200/R^2](1+u^2)<(1/200)(1+u^2)`.             (EB-M)

Here t<=100R and T=R^3, so no unspecified limiting step is present.

For EVERY 1<=x<=99,

`H_x(u)>=(1/100)(1+u^2)`, `u>=0`.

If x<=50, all remaining coefficients after subtracting that bound are nonnegative. If x>=50, a lower bound for the difference is

`6/25-(1/2)u+(49/100)u^2`

` >=(2/5)(u-5/8)^2+67/800>0`.

Combining with EB-M proves the strict middle bound

`P_(x,c)(t)>=[RT^2/200]t^4(1+u^2)>0`, `M<=t<=100R`.   (MID)

The uncertain low odd constant and the full x range were retained; neither was evaluated at one preferred denominator.

## 6. High frequencies t>=100R: all tails, including t=T and infinity

Both F and every E_x are negative here. Each factor of |F| is at least t/2, so `|F|>=t^3/8`. Also B<51R, C>0 and D_0<t^3/100 imply

`E_x<=-t^3+Bt^2+D_0<-t^3/3`.

Thus the even contribution is at least

`kappa F E_x >= T^2 t^6/(2400R)`.

Write `Z=T-t`, `H_0=(t-50)(t-R/4)>0`. The odd contribution is

`t g[H_0 Z^2+d Z] >= -t(g/H_0)d^2/4`.

For t>=100R, `0<g/H_0=(t-1000)/(t-R/4)<2`, and `d^2<200R^2T^2`. Completing the square therefore gives

`P>=T^2[t^6/(2400R)-100tR^2]`

`  >=T^2 t^6/(4800R)>0`, `t>=100R`.                    (HIGH)

The last comparison follows from `t^5>=100^5 R^5>480000R^3`. It includes the exact numerator odd zero t=T, where no odd positivity is assumed.

For an explicit weighted tail margin, if t>=4T then both actual O_c and Q_* are negative. The factors t−50,t−1000,t−R/4 are each at least t/2 and t−T>=3t/4. Since `|d|<13RT<=t^3/16`,

`|O_c|>=t^3/8`, `|Q_*|>=t^3/8`.

Hence `P>=t^7/64>=(1/8192)(1+t)^7` there. At infinity the leading coefficient of P is exactly one, as required by the monic equal-degree ratio; no additional target condition is imposed.

### Base-box weighted margin

LOW, MID and HIGH give normalized pairing greater than one on their respective portions up to4T. Explicit conservative comparisons are

`RT^2/[40000(1+M)^3]>1`,

`T^2/[25600*100^3 R^2]>1`,

`T/[2457600R]>1`.

Together with the tail bound, a single simple margin valid for ALL base members and ALL t>=0 is

`P_(a,N)(t)>=(1/10000)(1+t)^7`.                        (BASE)

Every interval boundary is covered by both adjacent nonstrict lower bounds. This is a whole-half-line proof, not extrapolation from selected frequencies.

## 7. The SAME numerator works on the ALL-SEVEN-width enlargement

Let a be any member of the accepted enlarged box and clip each coefficient to its base interval, obtaining a^0. Each coefficient difference has magnitude at most delta. Thus

`|E_a-E_(a^0)|<=delta(1+t)^3`,

`|O_a-O_(a^0)|<=delta(1+t)^2`.

All coefficients of N are positive. Let C_N be their sum. Its even-coefficient sum is below10T^2, and its odd-coefficient sum is below10^5T. In particular

`C_N<10^6 T^2`.

Separating those even/odd sums gives directly

`|P_(a,N)-P_(a^0,N)|<=delta C_N(1+t)^7`

`                         <[10^4/T^2](1+t)^7`

`                         <(1/20000)(1+t)^7`.

Combining with BASE proves the advertised expanded-box bound

`P_(a,N)(t)>=(1/20000)(1+t)^7>0`                       (ALL7)

for every actual independently varying coefficient choice and every finite t>=0. The denominators' strict Hurwitzness is the named accepted import; no common-factor cancellation is used. N is monic of exact degree seven, with positive ratio at zero and limiting ratio one.

## 8. The EIGHT actual moment equations, and why no positive balance exists

Use the full coefficient order

`c_b=(e_0,e_1,e_2,e_3; o_0,o_1,o_2,o_3)`,

where `E_b=sum_(j=0)^3 (-1)^j e_j t^j` and `O_b=sum_(j=0)^3 (-1)^j o_j t^j`. This is the unrestricted eight-coordinate space, not the four midpoint columns.

For actual corner/frequency atoms v_i,t_i with finite t_i>=0, positive weights lambda_i, and total infinity weight lambda_infty, put `rho_i=(1+t_i)^(-7)`. The full zero-balance equations are, for j=0,1,2,3,

`M_Ej=sum_finite lambda_i rho_i (-1)^j t_i^j E_(v_i)(t_i)=0`,

`M_Oj=sum_finite lambda_i rho_i (-1)^j t_i^(j+1) O_(v_i)(t_i)`

`                              +1_(j=3)lambda_infty=0`.       (8M)

Weights are nonnegative, total weight one; zero is a legal finite atom. At infinity only the last odd coordinate survives and equals +1, which is why its term has the displayed positive sign. These are the literal eight equations from v32-H's compactified alternative. A failure certificate could use at most nine atoms, but the argument below excludes ANY positive finite balance, not merely that safe bound.

On this actual box their anchors can be written explicitly as

`E_v=50F+(50-x)t^3+eta_E(t)`,

`O_v=Q+d+eta_O(t)`,

where `eta_E=-epsilon_1 t^3+epsilon_3 t^2-epsilon_5 t+epsilon_7`,

`eta_O=epsilon_2 t^2-epsilon_4 t+epsilon_6`,

and `|epsilon_j|<=delta` for the enlarged box (all zero in the base). Corners are the ACTUAL endpoint choices; no independent surrogate atom values are introduced. Substitution in (8M) gives its box-specific moment system. The old F,D_Q,H,Q balances are only four linear combinations of this system and cannot replace it.

The new numerator coefficient vector is exactly

`c_N=(250kappa R, kappa((1001/2)R+250),`

`      kappa(R+1001/2), kappa;`

`      50000T,1050T+50000,T+1050,1)`.

If all eight equations (8M) held, dotting them with THIS full vector would give zero. But ALL7 makes each finite atom's normalized pairing at least1/20000, while the infinity atom contributes exactly1. Their weighted sum is therefore at least1/20000 because weights sum to one. Contradiction.

Thus no actual positive eight-coordinate balance exists on this literal box. The positive construction, rather than a projected-obstruction heuristic, settles its unrestricted numerator question.

## 9. Scientific conclusion and remaining scope

This exact box simultaneously has: whole-box Hurwitzness; strict crossed-SG failure; infeasibility of its entire fixed four-component midpoint hybrid; and the explicit unrestricted common numerator N proved here. Hence the preceding negative result was genuinely a numerator-representation limitation, not an unrestricted SPR7 counterexample.

What remains globally open is unrestricted degree-seven synthesis for EVERY robustly Hurwitz independent box. The middle odd-root relocation used here is an actual successful mechanism on this structural example, not a proof that such a relocation can always be chosen. No universal selection theorem is asserted.

All new algebraic bounds, coefficient identities and endpoint arguments are WRITTEN candidates requiring complete separate reconstruction and parent disposition. No scientific program/eval/replay was run, no historical computation was promoted, no pinned file was modified, and no formal/kernel/human/cross-vendor or novelty acceptance is claimed. The previously assigned v49-A cross-domain review was completed and returned before this primary packet.
