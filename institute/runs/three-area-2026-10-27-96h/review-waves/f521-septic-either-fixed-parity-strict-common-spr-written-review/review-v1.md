# F521 — WRITTEN review of fixed-parity strict common-SPR synthesis

**Disposition:** SUPPORTED at the stated sufficient-class scope.  
**Findings:** 0 FATAL / 0 MAJOR / 0 MINOR.  
**Overall correctness:** correct.  
**Confidence:** 0.97.

This review supports the fixed-parity synthesis, quantitative thickening, explicit parameterized family, and their stated dual consumers. It does **not** establish common-SPR synthesis for arbitrary all-Hurwitz septic boxes with both parities varying.

## 1. Binding, coverage, and process

The assignment supplied:

- Manifest SHA256: `46dc9f00fc93a68adb951a80ec87e9fb7f6ad88fa0ca5ace6fee25461a879724`
- Receipt SHA256: `385430e06ae18e71d08e1326032486132377f1629ac541963c0d24ad2d89a7fa`
- Packet SHA256, recorded in the receipt and parent metadata: `fe1f5c350adadf7649767737feb9499ca55487ad9e84c4a77cd6710f72cd9228`

These are **parent-supplied bindings**, not independently recomputed reviewer hashes.

Before opening the mathematical packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all eleven listed status-only controls. I then sent the direct administrative pre-body ACK.

After the ACK, I read the entire literal packet in ordered raw windows of at most 20 LF, beginning at packet LF1 and ending with LF921–924. This included every source ending:

| Input | Complete source coverage | Supplied SHA256 |
|---|---:|---|
| S1 — F493 author candidate | Source labels 1–823 | `5ea7d6280ff7a4853f181f4d06030fdb79b46338eb637812aa9ee19a19e25fac` |
| S2 — Previous explicit-family disposition | 1–53 | `fdd46b6ad702530fe0bcd07d4e7b86468dca9a40e00de5975b4773e292babf08` |
| S3 — Actual-box dual reduction disposition | 1–46 | `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae` |

All references below use these **F521 packet source labels**. Author-internal references to an earlier packet’s “S1/S2/S3” are not treated as new imports.

The held F439/F444/F448/F513 episodes and every other quarantined episode and consumer remained NONINPUT. No excluded links, sibling reviews, author code, or additional scientific sources were followed.

**Reviewer scientific execution: NOTRUN.** No scientific program, interpreter, CAS, solver, enumeration, build, test, or finite replay was run. Reconstruction used formal variables and the manuscript’s explicitly assigned instance; no additional selected numerical probe was introduced. No reviewer-native clock observation is claimed.

No repository write was attempted under the read-only assignment. This is the complete review body for parent materialization.

## 2. Claim-by-claim dispositions

| Claim | Source LF | Disposition |
|---|---|---|
| Exact physical real-product identity and complete frequency compactification | S1 34–89, 192–239 | **SUPPORTED** |
| Strict common numerator for every nonempty compact convex fixed-odd or fixed-even Hurwitz septic family | S1 118–385 | **SUPPORTED** |
| Terminating rational dyadic/Sturm construction for eligible rational fixed-parity boxes, without a uniform runtime claim | S1 395–438 | **SUPPORTED as an unexecuted mathematical protocol** |
| Seven-independent-coefficient thickening with \(\rho=\eta/(14Q)\) and retained margin \(\eta/2\) | S1 442–549 | **SUPPORTED** |
| Scaled-binomial full-dimensional family and displayed rational instance | S1 553–696 | **SUPPORTED** |
| Exclusion of all-eight-strict-negative aggregates and strict positivity on every stated actual odd-moment-cone consumer | S1 700–787 | **SUPPORTED for the proved classes** |
| Arbitrary both-parities-varying eligible boxes remain unresolved by this return | S1 791–823 | **SUPPORTED as the exact scope limitation** |

No assigned mathematical claim was refuted. No blanket re-verification of S2’s historical execution reports or S3’s entire earlier reduction is claimed.

## 3. Independent written reconstruction

### 3.1 Physical pairing and endpoints

For the stated septic convention,
\[
a(i\omega)=E_a(t)+i\omega O_a(t),\qquad
q(i\omega)=F(t)+i\omega G(t),\qquad t=\omega^2,
\]
multiplication by the complex conjugate gives exactly
\[
P_{q,a}(t)
=\operatorname{Re}\!\left(q(i\omega)\overline{a(i\omega)}\right)
=F(t)E_a(t)+tG(t)O_a(t).
\]
The sign in front of the odd product is positive. Consequently,
\[
\operatorname{Re}\frac{q(i\omega)}{a(i\omega)}
=\frac{P_{q,a}(t)}{|a(i\omega)|^2}.
\]

With \(u=t/(1+t)\), the degree-three parity transforms satisfy
\[
\overline P_{q,a}(u)
=(1-u)\widetilde F(u)\widetilde E_a(u)
+u\widetilde G(u)\widetilde O_a(u).
\]
The endpoint values are
\[
\overline P_{q,a}(0)=q_0a_0,\qquad
\overline P_{q,a}(1)=1.
\]
The second identity uses both polynomials’ monic degree-seven leading terms. Thus the argument includes zero frequency and infinity rather than replacing the frequency axis with samples.

### 3.2 Compact small-parameter lemma

The lemma at S1 LF120–146 is valid.

On the compact set \(N=\{A\le0\}\), the hypothesis \(A>0\) on \(\{B=0\}\) implies \(B\) has a strictly positive minimum \(b\). For \(M=\max|A|>0\), taking
\[
0<\delta\le\min(1,b/(2M))
\]
gives \(B+\delta A\ge b/2\) on \(N\). Outside \(N\), \(A>0\) and \(B\ge0\). The separately stated empty-\(N\) and zero-\(M\) cases are consistent.

This supplies a single parameter bound over the complete compact product \(K\times[0,1]\), not a member-dependent or frequency-dependent choice.

### 3.3 Fixed odd parity

For common odd part \(O\), the proposed numerator is
\[
q_\delta(s)=\delta E_*(-s^2)+sO(-s^2).
\]
Its compactified pairing is
\[
\overline P_{q_\delta,a}
=u\widetilde O^2
+\delta(1-u)\widetilde E_*\widetilde E_a.
\]

Set
\[
B=u\widetilde O^2,\qquad
A=(1-u)\widetilde E_*\widetilde E_a.
\]
The required zero-set check is complete:

- At \(u=0\), \(A=E_*(0)E_a(0)>0\), because Hurwitz members have positive constant coefficients.
- At a finite positive root \(t\) of \(O\), no \(E_a(t)\) can vanish without producing an imaginary-axis denominator zero.
- At that same root, \(E_*(t)\) and \(E_a(t)\) cannot have opposite signs: their coefficient segment lies in convex \(K\), and an intermediate member would have both parity values zero.
- At \(u=1\), \(B=1\), so this endpoint is not an omitted zero-set case.

Therefore the compact lemma proves strict positivity simultaneously for every actual member and every frequency for all sufficiently small positive \(\delta\).

### 3.4 Fixed even parity

For common even part \(E\), use
\[
q_\delta(s)=\delta^{-1}E(-s^2)+sO_*(-s^2).
\]
Then
\[
\delta\overline P_{q_\delta,a}
=(1-u)\widetilde E^2
+\delta u\widetilde O_*\widetilde O_a.
\]

Here
\[
B=(1-u)\widetilde E^2,\qquad
A=u\widetilde O_*\widetilde O_a.
\]

At \(u=1\), \(A=1>0\). Every other zero of \(B\) corresponds to a finite positive root of \(E\): zero frequency is excluded because \(E(0)>0\). At such a root, convexity and all-member stability force all actual \(O_a(t)\) to be nonzero and to have the reference sign. Hence \(A>0\) on the complete zero set of \(B\).

The inverse scaling does not invalidate the small-parameter argument: the expression to which the lemma is applied is \(\delta\overline P\), and division by positive \(\delta\) preserves strict positivity.

### 3.5 Numerator stability and uniform margin

The numerator-stability argument is independent of membership in \(K\).

For either prescribed scaling, a nonzero imaginary-axis root would require a simultaneous zero of the reference parity polynomials. That contradicts stability of \(a_*\). The constant coefficient remains positive.

For any fixed positive scaling parameter, the interval joining it to \(1\) is compact and bounded away from zero. The polynomials remain monic of degree seven with bounded coefficients. Hence roots cannot escape through infinity, and no half-plane crossing can occur without an imaginary-axis zero. Starting from \(a_*\), this proves numerator stability.

For each fixed permitted \(\delta\), strict positivity of \(\overline P\) on compact \(K\times[0,1]\) gives
\[
m_\delta=\min_{a,u}\overline P_{q_\delta,a}(u)>0,
\]
and therefore
\[
P_{q_\delta,a}(t)\ge m_\delta(1+t)^7.
\]

Both numerator and denominators are stable, and their ratio tends to \(1\) at infinity. The stated strict common-SPR conclusion follows.

**Quantifier ceiling:** the permitted \(\delta_0\) depends on the family and reference member; the margin depends on the chosen positive \(\delta\). No universal parameter bound over all eligible families, or positive margin uniform as \(\delta\downarrow0\), is established or required.

## 4. Exact rational construction protocol

For a rational independent fixed-parity box, its rational center supplies a rational reference polynomial. Each dyadic \(\delta\) produces a rational numerator.

For fixed \(q\) and frequency, the pairing is affine in denominator coefficients. Therefore entire-interval positivity at all varying-parity corners implies positivity throughout the box. The stated corner counts are correct:

- Four varying even coefficients: at most \(16\) corners.
- Three varying nonleading odd coefficients: at most \(8\) corners.

Endpoint positivity together with an exact zero count on \((0,1)\) certifies positivity on the complete closed interval. A tangential root must be counted; testing only sign changes would not suffice.

Theorem 1 guarantees that the dyadic \(\delta\)-search eventually enters the valid range. Once \(q\) is fixed, compact strict positivity similarly guarantees that a sufficiently small positive dyadic \(\eta\) makes every \(p_v-\eta\) strictly positive.

This establishes mathematical termination **conditional on the eligible rational-box hypotheses**. It is not an executed implementation, a bounded-time algorithm, or a certificate that arbitrary supplied input satisfies those hypotheses.

## 5. Quantitative seven-coordinate thickening

Let
\[
Q=\sum_{j=0}^7|q_j|,\qquad
\rho=\frac{\eta}{14Q}.
\]
For \(|d_j|\le\rho\), the manuscript’s bounds give
\[
|d(i\omega)|\le7\rho(1+t)^3,\qquad
|q(i\omega)|\le Q(1+t)^{7/2}.
\]
Thus
\[
|P_{q,a+d}-P_{q,a}|
\le7\rho Q(1+t)^{13/2}
\le\frac{\eta}{2}(1+t)^7.
\]
Consequently,
\[
P_{q,a+d}(t)\ge\frac{\eta}{2}(1+t)^7.
\]
The numerical factor \(14\) is sufficient; no optimality is claimed.

The stated stability conclusion also follows under the literal theorem’s assumptions, without an additional unstated stability premise. For any resulting \(b\), consider the formal monic segment
\[
h_\theta=(1-\theta)q+\theta b.
\]
Its pairing with \(q\) is
\[
P_{q,h_\theta}
=(1-\theta)|q(i\omega)|^2+\theta P_{q,b}>0.
\]
This excludes every imaginary-axis zero along a bounded monic segment beginning at stable \(q\). The same no-crossing argument proves that \(b\) is Hurwitz. This also supports the manuscript’s intended application starting from Hurwitz members of \(K\).

For an independent box, adding the independent coefficient cube gives exactly
\[
K_\rho=\prod_{j=0}^6[\ell_j-\rho,u_j+\rho].
\]
Every previously fixed coefficient gains positive width. For a general compact convex family, the conclusion concerns its coefficient-cube thickening; it does not assert that the original family was itself an independent box.

## 6. Explicit parameterized family and assigned instance

The weighted Cauchy–Schwarz estimate is correct:
\[
\left(\sum_{j=0}^{6}x^j\right)^2
\le
\left(\sum_{j=0}^{6}\binom7j^{-1}\right)
\left(\sum_{j=0}^{6}\binom7j x^{2j}\right).
\]
The displayed arithmetic checks:
\[
\sum_{j=0}^{6}\binom7j^{-1}
=1+\frac27+\frac2{21}+\frac2{35}
=\frac{151}{105},
\]
and
\[
\frac{36}{25}-\frac{151}{105}=\frac1{525}>0.
\]
Hence
\[
\sum_{j=0}^{6}x^j\le\frac65(1+x^2)^{7/2}.
\]

With \(q_\beta=(s+\beta)^7\), this yields the all-member relative-error bound
\[
|d(i\omega)|\le\frac65\varepsilon|q_\beta(i\omega)|.
\]
Therefore, for \(\beta>0\) and \(0<\varepsilon<5/6\),
\[
P_{q_\beta,a}(t)
\ge\left(1-\frac65\varepsilon\right)(\beta^2+t)^7>0.
\]
The same estimate holds along every formal coefficient segment from \(q_\beta\) to an actual member, proving stability by no crossing.

For the manuscript-assigned \(\beta=1,\ \varepsilon=3/4\), all seven intervals are correctly displayed:

| Coefficient | Interval |
|---|---|
| \(a_0\) | \([1/4,7/4]\) |
| \(a_1\) | \([25/4,31/4]\) |
| \(a_2\) | \([81/4,87/4]\) |
| \(a_3\) | \([137/4,143/4]\) |
| \(a_4\) | \([137/4,143/4]\) |
| \(a_5\) | \([81/4,87/4]\) |
| \(a_6\) | \([25/4,31/4]\) |

The numerator is the stated expansion of \((s+1)^7\), and
\[
1-\frac65\frac34=\frac1{10},
\]
giving the claimed uniform bound.

This instance is outside S2’s previous explicit box: its \(a_6\) interval is near \(7\), whereas that earlier family confines \(a_6\) near \(1\). This is a comparison of the stated families, not evidence for universal synthesis.

## 7. Actual dual and ray consumers

The consuming-side identity is correct for the exact raw row:
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
For \(c=(q_0,\ldots,q_7)\),
\[
c\cdot r_a(t)=F(t)E_a(t)+tG(t)O_a(t)=P_{q,a}(t).
\]
The signs match S3 LF7.

Because the constructed numerator is strictly Hurwitz, its real monic coefficient vector is strictly positive. Any nonzero finite positive-weight actual aggregate therefore has positive dot product with \(c\). An aggregate with all eight coordinates strictly negative would have negative dot product instead. This excludes that obstruction for every proved box.

For any actual family satisfying
\[
R_1,R_3,R_5,R_7\le0,
\]
the positive odd numerator coefficients give
\[
\sum_iw_it_iG(t_i)O_i(t_i)
=q_1R_1+q_3R_3+q_5R_5+q_7R_7\le0.
\]
Consequently,
\[
\sum_iw_iF(t_i)E_i(t_i)
=\sum_iw_iP_i-\sum_iw_it_iG(t_i)O_i(t_i)>0.
\]

This applies to **every** such actual family. It therefore covers every feasible R4 omitted-moment choice, both R5 orientations, zero-odd singletons, same-frequency opposite-odd cancellations, and their combinations. No division by an odd value is used.

For independent boxes, the pointwise minimizing even endpoint and selected odd endpoint can be combined into an actual member at each node. Different nodes need not use the same minimizing polynomial. This justification is correctly restricted to independent boxes.

Zero frequency and compactified infinity retain the positive pairings \(q_0a_0\) and \(1\). No orientation or endpoint is silently discarded.

The new consumer proof needs S3’s raw-row and ray conventions, but does **not** need to re-establish its complete extreme-ray classification: the inequality already holds for the entire actual odd-moment cone.

## 8. Imports, residual, and acceptance ceiling

The main synthesis and thickening proofs are reconstructed from their displayed elementary arguments. They do not require:

- S2’s historical executable verification;
- S3’s six-node sparsification;
- a new Hermite–Biehler import;
- an arbitrary weak-to-strict separator theorem;
- any held reviewer reasoning.

S2 supplies the previous explicit-family comparison. S3 supplies the actual raw-row/ray conventions and the distinction between an earlier fixed-parity obstruction result and strict synthesis. Their linked underlying bodies and programs were not accessed.

The supported result has the following exact ceiling:

1. Every nonempty compact convex **fixed-parity** strictly Hurwitz septic family admits the prescribed strict common numerator for sufficiently small positive scaling.
2. Every such family has a positive quantitative seven-coordinate thickening retaining that numerator.
3. The displayed scaled-binomial independent boxes form an additional explicit sufficient class.
4. The stated strict-negative dual obstruction is impossible, and the stated actual odd-moment-cone pairings are strictly positive, **for those classes**.

For an arbitrary eligible box with both parities varying, these results provide fixed-parity slices and positive neighborhoods. They do not prove that one numerator’s neighborhood covers the whole original box, or that the valid-numerator sets for all slices have a common intersection. The one-common-numerator quantifier cannot be obtained by choosing separate numerators for separate slices.

Accordingly, this return supplies neither universal septic-box synthesis nor a genuine all-eight-strict-negative counterexample. It does not settle arbitrary weak-separator strictification or the general common-root-triple condition.

**Explanation:** The assigned sufficient-class claims withstand the complete written reconstruction, including numerator stability, both frequency endpoints, the quantitative perturbation constant, and every stated actual consumer. Support remains scoped written evidence only: no automatic parent adoption, finite execution, independent-family or human review, formal/kernel verification, original-source correspondence, novelty, or global original-target closure is conferred.