# Bounded reconstruction — PH8 cubic and PH9 quartic upper constructions

Review start clock actually observed: **2026-10-23T15:34:30-07:00**. Completion clock observed immediately before this output: **2026-10-23T15:37:23-07:00**. Reviewer PhysicsPPT44, temporarily assigned by `peer-review-wave-eighteen-v5.json`; primary ownership remains physics-3/P44. Own normalizedN4 request remains **HOLD/notGO**.

## 1. Observed snapshots, coverage and verdict

Both source SHA-256 values were observed with `shasum -a 256` and match the exact assigned pins:

- `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/proof-eight-state-cubic-cancellation-v1.md`, **all285lines read**, SHA `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`.
- `mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/proof-nine-state-quartic-cancellation-v1.md`, **all177lines read**, SHA `6ff399f1f0a72fd709cb53d4432627d867a737c15332876ca90153c14d155394`.

Also read the actual49-line selection/PH definition, the complete operative mathematics verification overlay, and the complete current parent `priority-written-dispositions-v1.md`. The latter's observed SHA is `faf0335d8569a39c2fce54f09f4e8e1474021b60cf176bd16888e1a266048787`; the overlay SHA is `a20d57baba3ee8bf905061fa8cc6064b2ef21d6b84d2b58ebc06035760291cf8`.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the exact direct-construction scope.** The C8 pair is an actual PH realization for every `13/20<=z<=8/9`; the C9 pair is an actual PH realization for every `3/4<=z<=1`. These are **upper8 and upper9**, not exact minimum8/9 and not lower bounds excluding PH7/PH8. No new global minimum-order or book-level resolution follows.

The checks below are written reconstruction from the raw factors and matrices, not arithmetic-code execution, polynomial interpolation, a solver result, a formal kernel, or a blind/cross-vendor/human review. Supplied author proofs and parent focus are shared inputs. Novelty is not assessed or cleared.

## 2. Visible factor and cubic product reconstructed

Put `r=m+1`. Directly squaring the quadratic gives

`(Y^2-2Y+w)^2=Y^4-4Y^3+(4+2w)Y^2-4wY+w^2`.

Multiplication by Y-r gives exactly

`D=Y^5-SY^4+UY^3-VY^2+WY-Z`,

with `S=m+5`, `U=4m+8+2w`, `V=4m+4+(2m+6)w`, `W=w^2+4(m+1)w`, `Z=(m+1)w^2`. This verifies C8 lines25–36 directly.

Multiplying by `q=Y^3+SY^2+BY+C` then gives the complete eight-degree coefficient list

`1, 0, B-S^2+U, C-SB+SU-V, -SC+UB-SV+W,`
`UC-VB+SW-Z, -VC+WB-SZ, WC-ZB, -ZC`.

Thus choosing `B=S^2-U` and `C=SB-SU+V` cancels exactly powers6 and5. Expanding these expressions gives precisely C8(2), including `C=m^3+7m^2+23m+49-2(m+7)w`.

I substituted each actual chart separately, not just a rational anchor:

- **I:** `(S,U,V,W,Z)=(11,32+2w,28+18w,w^2+28w,7w^2)` and `(B,C)=(89-2w,655-26w)`. The resulting powers4,3,2,1 are respectively `-3w^2+230w-4665`, `18468-760w-12w^2`, `-2w^3+424w^2-8570w-18340`, `w(-12w^2-696w+18340)`.
- **II:** `(S,U,V,W,Z)=(9,24+2w,20+14w,w^2+20w,5w^2)` and `(B,C)=(57-2w,317-22w)`. The resulting powers4,3,2,1 are exactly `-3w^2+158w-1665`, `6468-472w-12w^2`, `-2w^3+280w^2-2858w-6340`, `w(-12w^2-408w+6340)`.
- **III:** m3 with fixed B53/2,C33 gives powers6 through0 exactly as C8 lines133–139. In particular the uncanceled leading feedback coefficients are `2w-35/2` and `4w-35`, both nonpositive; the power2 row is `-(11/2)w^2+28w-528`, not a coefficient inherited from ChartIV.
- **IV:** m3 with B44-2w,C208-20w gives the displayed four polynomials with constants -912,3456,-3328,3328 and cubic terms exactly as C8 lines157–161. Every chart has constant coefficient -ZC.

## 3. All four sign intervals and their closed coverage

The chart inequalities hold on the full **closed** intervals, not just at the supplied endpoints:

- **I, w in[122/5,149/6]:** c4 increases and its upper value is `-9641/12`. c3 decreases and its lower-end value is `-180508/25`. For c2, `24<w<25` gives derivative greater than8032, and its upper value is `-33737/108`. The decreasing c1/w starts at `-144668/25`. Bounds `B>39`, `0<C<21` follow directly from the two affine expressions; c0 is strictly negative.
- **II, w in[313/27,131/10]:** c4 increases to `-11003/100`; c3 decreases and is already below-176 using w>11. For c2, `11<w<14` gives derivative greater than2126 and upper value `-112591/500`. The decreasing c1/w starts at `-592/243`. The affine bounds `B>30`, `0<C<62` are valid; in particular C at the lower endpoint is1673/27<62. c0 is strictly negative.
- **III, w in[31/4,35/4]:** c6 and c5 are nonpositive and both vanish only at the upper end. The derivatives `2w-27`, `8w-124`, `-11w+28` make c4,c3,c2 strictly decreasing. Their lower-end values are exactly `-179/16,-1939/4,-20523/32`; c1/w is at most `-151/4`. c0 is strictly negative.
- **IV, w in[35/4,9]:** c4 increases to-3; c3 decreases from `-2171/4`; c2 increases because its derivative exceeds1562, but ends at-214. c1/w decreases from `-443/4`. Here `B>=26` and `28<=C<=33`, so c0 is strictly negative.

These derivative/endpoint comparisons prove all feedback signs, including every zero coefficient at a closed endpoint. The endpoint computations are specializations **of** the reconstructed coefficient identities, not evidence used to infer them.

Since `z=(w-1)/m^2`, the chart images are exactly

`[13/20,143/216]`, `[143/216,121/160]`,
`[3/4,31/36]`, `[31/36,8/9]`.

I/II meet at143/216; II extends past III's start by `121/160-3/4=1/160`; III/IV meet at31/36. At the III/IV join the actual hidden cubics agree, B53/2,C33. I/II may supply different matrices at their common z, which causes no existence gap and requires no limiting construction. Their union is the whole claimed C8 interval.

## 4. Hidden-cubic and quartic stability

For the cubic, the positive coefficient bounds give S,B,C>0 and SB>C in all charts: the crude bounds11*39>21,9*30>62,8*(53/2)>33 and8*26>33 suffice.

The elementary proof at C8 lines190–196 is sound. A nonnegative real root is impossible. If a complex pair p±it had p>=0, the third root would be -S-2p, and Vieta gives

`B=t^2-3p^2-2Sp`, `C=(S+2p)(p^2+t^2)`,
`SB-C=-2p[(S+p)^2+t^2]<=0`,

contradicting SB>C, including p=0. If all roots are real, all are negative. This handles repeated roots as well; no distinctness or hidden-real-root assumption is needed.

For C9, the hidden polynomial expands directly:

`(Y+2)^2(Y^2+3Y+7)=Y^4+7Y^3+23Y^2+40Y+28`.

Its roots are -2 with multiplicity2 and `(-3±i sqrt19)/2`, all strictly left-half-plane. The quadratic has value5 at -2, so that real multiplicity is exactly2. No numerical root test is used.

## 5. C9 full product and signs reconstructed

At m2 the visible factor is `Y^5-7Y^4+(16+2w)Y^3-(12+10w)Y^2+(w^2+12w)Y-3w^2`. Multiplying by the literal quartic above gives powers9 through0:

`1,0,2w-10,4w-21,w^2-12w+32,4w^2-66w+168,`
`2w^2-68w-32,-29w^2+200w-336,-92w^2+336w,-84w^2`.

For example the power4 row is `-7*28+40(16+2w)-23(12+10w)+7(w^2+12w)-3w^2`; its constant168, linear-66w and quadratic4w^2 agree. The power3,2,1,0 rows likewise follow by ordinary product collection as displayed, with no omitted intermediate power.

For w in[4,5], c7<=0,c6<=-1; c5=`(w-4)(w-8)`; c4 decreases from-32; c3 is below-254 under the stated conservative bound; c2=`(w-4)(84-29w)`; c1=`4w(84-23w)<0`; c0<0. Thus endpoint zeros at w4 andw5 introduce no negative feedback. The full interval maps to z in[3/4,1]. The upper-end polynomial in C9 lines164–165 agrees term by term with w5, but is correctly used only as an anchor.

## 6. Actual companions, PH normalization and complete transfer

For either source let n=8 or9, hidden degree k=n-5, and `R(x)=eta^k q(x/eta)`. Since `eta=d/m` and `w=1+b^2/eta^2`, scaling the literal visible factor proves

`P(x)=(x-(m+1)eta)[(x-eta)^2+b^2]^2 R(x)`.

With `lambda=a+eta=c+(m+1)eta`, shifting x=s+lambda gives precisely

`P(s+lambda)=(s+c)((s+a)^2+b^2)^2 R(s+lambda)`.

The upper-shift companion with the listed nonnegative last row has characteristic polynomial P. Its last diagonal is0 because the degree n-1 coefficient is0. Hence G=C_n-lambda I is Metzler. The visible eigenvalues are -c and the desired pair -a±ib, each nonreal pole repeated twice. Each hidden q-root has negative real part; after multiplication by eta and shifting by -lambda its real part is below-lambda<-a. Thus all hidden and visible eigenvalues are stable and cannot collide with one another. C9's hidden real root remains double until fully canceled. All this remains valid when feedback coefficients vanish at a chart endpoint.

Because the hidden polynomial has strictly positive coefficients, `D0=R(lambda)>0`. For `h_i=lambda^(i-1)/D0`, the listed similarity gives superdiagonal lambda and feedback `f_j/lambda^(j-1)`, exactly the sources' literal T rows. The initial alpha is v*Delta with the ascending hidden numerator coefficients; every listed nonzero entry is positive, and its sum is `R(lambda)/D0=1`.

The first n-1 rows of T sum to0. At lambda, `P(lambda)=K D0>0`, so its last row sum is `-K D0/lambda^(n-1)`. Therefore `omega=-T1=(K D0/lambda^(n-1))e_n` is a genuine nonnegative exit, strictly positive at the last coordinate. Together with Hurwitz/Metzler this is an actual transient PH pair. The positive return feedback f_n and superdiagonal path imply irreducibility, but no irreducibility assumption is used for a lower-bound claim.

Finally `(xI-C_n)y=e_n` gives `y_i=x^(i-1)y_1` and `P(x)y_1=1`. Thus the ascending coefficient row v produces numerator R(x) exactly. Substitution x=s+lambda gives

`v(sI-G)^(-1)K e_n =K R(s+lambda)/P(s+lambda)=H(s)`.

Also `Gh=-K e_n`, `alpha=vDelta`, and `omega=Delta^(-1)K e_n`. Diagonal similarity therefore preserves the full transfer as claimed. The **entire same hidden R** cancels, including all real/complex multiplicities; the visible repeated pair is retained. Neither source substitutes a stable spectral list for PH positivity or a density sample for a rational identity.

## 7. Composition interfaces and limits

The actual parent disposition, Section2, states at its named written dependencies: B6 excludes all order<=6 for z>1/2, and old G7 plus new C7 give exact minimum7 on `1/2<z<=5935/9126`; at z1/2 the minimum is6. I authenticated the current source hashes against that interface: B6 is `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, C7 is `023ac8611a66263233288838eaf3dcd3ac0013111a5be93fb5974e7f47e39667`. This review reads the actual disposition interface; it is **not a fresh reconstruction of the B6/C7/G7 proof bodies or all historical imports**. The older defective timestamp/ellipsis record is not substituted for the operative qualification.

C7/C8 overlap because `20*5935-13*9126=62>0`; C8/C9 overlap on[3/4,8/9]. Thus at the stated inherited dependencies the upper bounds can be composed through z1. Any claim also covering z<=1/2 retains its earlier baseline dependency and is not freshly reproved here.

For C8's direct interval the supported B6 lower interface yields only minimum in{7,8}; for C9's interval only a minimum between7 and9, with sharper known subbands retained. **Nothing excludes PH7 above C7's endpoint or PH8 anywhere in C9's residual. Exact8/exact9 are not established.** z is beta-squared: C8's endpoint is z8/9, not beta8/9.

## Evidence boundary and return

No scientific program, arithmetic code, symbolic package, solver, enumeration, compilation, tests, CLI or nested agent ran. Only source reads, SHA metadata and actual clocks were used. Both direct upper constructions pass this scoped supplied-proof reconstruction with **0F/0M/0m**. Parent acceptance, formal verification, source-wide novelty and worldwide priority remain separate. This single assigned review is complete; P44 primary ownership and normalizedN4 HOLD are unchanged.
