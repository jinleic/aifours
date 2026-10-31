# F522 — Written review of fixed-parity synthesis, seven-coefficient thickening, binomial boxes, and actual consumers

**Disposition:** SUPPORTED at the sufficient-class scopes stated below.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Execution:** WRITTEN ONLY; scientific execution **NOTRUN**.  
**Delivery:** Complete review returned inline for parent materialization; no repository files modified.

This is a same-harness written reconstruction, not parent adoption, independent-family review, human review, finite replay, formal/kernel verification, or novelty certification.

## 1. Input bindings and process record

Reviewed wave:

`institute/runs/three-area-2026-10-27-96h/review-waves/f522-septic-seven-coefficient-thickening-binomial-box-and-consumer-review/`

Bindings recorded by the supplied parent metadata:

| Artifact | SHA-256 |
|---|---|
| Manifest | `9e9bb12a0240f34c4dbc5f9f4beca098d5e6564032f8e382ff6263d2f8897f57` |
| Freeze receipt | `6bdc00252cfd10f653a63498c26ce4cdd33f21effbfa4bd593199127eed9b9a2` |
| Literal packet | `fe1f5c350adadf7649767737feb9499ca55487ad9e84c4a77cd6710f72cd9228` |
| S1 — complete F493 author | `5ea7d6280ff7a4853f181f4d06030fdb79b46338eb637812aa9ee19a19e25fac` |
| S2 — previous explicit-box disposition | `fdd46b6ad702530fe0bcd07d4e7b86468dca9a40e00de5975b4773e292babf08` |
| S3 — actual-box dual/ray disposition | `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae` |

These are **parent-supplied bindings**, not reviewer-native hash measurements.

Before opening the mathematical packet, I read the complete manifest, freeze receipt, metadata supply, and all eleven declared status-only controls, including the F439/F444/F448/F513 quarantines. I then sent the direct administrative pre-body ACK.

After that ACK, I read packet LF **1–924**, in consecutive raw windows of at most 20 LF, including:

- S1 logical lines **1–823**, through its final disposition;
- S2 lines **1–53**, through its limitations;
- S3 lines **1–46**, through its remaining unpaid obligations.

No omitted packet segment or unresolved elision remains. Mathematical reconstruction began after the complete packet read.

No new selected mathematical instance, scientific code, interpreter, solver, enumeration, replay, external source, author-code access, sibling review, or held scientific payload was used. The displayed rational instance and scalar calculations checked below are manuscript-assigned material. All held episodes and every associated proof, method, selection, planning, verification, reporting, and confidence consumer remain **HELD/ZERO/NONINPUT**. No clean-cognition certificate is asserted.

## 2. Exact import boundaries

**S1 is the candidate under review**, not an accepted premise.

**S2 is used for the former family’s literal coefficient ranges and comparison scope.** This review does not independently reverify S2’s reported finite execution, its linked source programs, or its external review history.

**S3 supplies the actual-member interface and the named consumer classes:** signed odd moments, all R4 omitted-moment choices, both R5 orientations, zero-odd singletons, and same-frequency cancellations. Its prior weak-separation equivalence and conditional six-node sparsification are not needed to prove the new strict synthesis constructions.

No linked document outside the frozen packet was followed. In particular, no strict common numerator for arbitrary eligible boxes is imported from a prior weak-separation or no-strict-dual statement.

## 3. Pairing identity and elementary tools — SUPPORTED

**Locations:** S1 LF34–146.

For
\[
a(i\omega)=E_a(t)+i\omega O_a(t),\qquad
q(i\omega)=F(t)+i\omega G(t),\qquad t=\omega^2,
\]
direct multiplication gives
\[
P_{q,a}(t)=F(t)E_a(t)+tG(t)O_a(t)
=\operatorname{Re}\!\left(q(i\omega)\overline{a(i\omega)}\right).
\]
The conjugation and the sign of the odd contribution are correct. Division by \(|a(i\omega)|^2\) gives the stated real-part identity whenever the denominator has no imaginary-axis zero.

The no-crossing argument is valid for the paths used here: their degree and monic leading coefficient remain fixed, and their coefficients are bounded on each compact path. A common finite root bound prevents escape through infinity; a half-plane root count cannot change without an imaginary-axis zero.

The positive-coefficient claim for monic strictly Hurwitz real polynomials follows from their real linear and conjugate-pair quadratic factors.

The compact small-parameter lemma is also valid. The compact set \(N=\{A\le0\}\) is disjoint from \(\{B=0\}\), so \(B\) has a positive minimum on \(N\); a sufficiently small positive multiple of bounded \(A\) cannot erase that minimum. On the complement, \(A>0\) and \(B\ge0\). This supplies a uniform parameter, not a separately selected parameter at each member or frequency.

## 4. Fixed-parity strict synthesis — SUPPORTED

**Locations:** S1 LF150–391.

### 4.1 Complete-frequency compactification

The transforms
\[
\widetilde E_a(u)=(1-u)^3E_a\!\left(\frac{u}{1-u}\right),\qquad
\widetilde O_a(u)=(1-u)^3O_a\!\left(\frac{u}{1-u}\right)
\]
are polynomials extending through \(u=1\). The identity
\[
\overline P_{q,a}(u)
=(1-u)\widetilde F(u)\widetilde E_a(u)
+u\widetilde G(u)\widetilde O_a(u)
\]
has the correct powers. Monicity gives
\[
\widetilde O_a(1)=\widetilde G(1)=-1,
\quad
\overline P_{q,a}(0)=q_0a_0,
\quad
\overline P_{q,a}(1)=1.
\]
Thus both zero frequency and infinity are included.

### 4.2 Fixed odd parity

For
\[
q_\delta(s)=\delta E_*(-s^2)+sO(-s^2),
\]
the compactified pairing is
\[
u\widetilde O(u)^2+
\delta(1-u)\widetilde E_*(u)\widetilde E_a(u).
\]

At \(u=0\), the second summand’s coefficient is positive because both constant coefficients are positive. At every other zero of the nonnegative first term, \(O(t)=0\) at a finite positive \(t\). Each \(E_a(t)\) is nonzero. Convexity forces its sign to agree with \(E_*(t)\): otherwise the actual coefficient segment would contain an imaginary-axis zero. At infinity the first term equals one.

The compact lemma therefore gives **one** sufficiently small \(\delta>0\) working for **every** \(a\in K\) and every frequency.

### 4.3 Fixed even parity

For
\[
q_\delta(s)=\delta^{-1}E(-s^2)+sO_*(-s^2),
\]
multiplication of the compactified pairing by \(\delta\) gives
\[
(1-u)\widetilde E(u)^2+
\delta u\widetilde O_*(u)\widetilde O_a(u).
\]

At \(u=1\), the coefficient of \(\delta\) equals one. At any other zero of the nonnegative first term, \(E(t)=0\) at a positive finite \(t\); convexity and actual-member stability force \(O_*(t)O_a(t)>0\). The compact lemma again applies uniformly.

### 4.4 Numerator stability and strictness

In each parity-scaling homotopy, an imaginary-axis zero at nonzero frequency would require a common zero of the reference even and odd parts, contradicting stability of \(a_*\). Zero frequency is excluded by the positive constant coefficient. For each chosen positive \(\delta\), the parameter interval joining it to one is compact and stays away from zero. The no-crossing argument therefore establishes numerator stability without assuming that the constructed numerator belongs to \(K\).

For fixed permitted \(\delta\), compactness yields
\[
m=\min_{a\in K,\ u\in[0,1]}\overline P_{q_\delta,a}(u)>0.
\]
Consequently
\[
P_{q_\delta,a}(t)\ge m(1+t)^7.
\]
The stable numerator and denominators, strict all-frequency positivity, and equal-degree monic limit one supply the stated strict-SPR conditions.

**Supported scope:** every nonempty compact convex family of monic strictly Hurwitz real septics with either parity fixed. Coefficient independence is not required for this theorem.

## 5. Exact rational construction protocol — SUPPORTED as an unexecuted protocol

**Locations:** S1 LF395–438.

For rational fixed-parity boxes, the center and every proposed dyadic numerator are rational. The corner counts—at most sixteen for fixed odd parity and eight for fixed even parity—are correct.

Endpoint positivity together with an exact count of **all** interior roots certifies strict positivity on \([0,1]\). The candidate correctly requires rejection of tangential zeros. Affinity in denominator coefficients then extends the corner certificates to the complete box, at every frequency.

Theorem 1 guarantees eventual success of the dyadic numerator search. Once the numerator is fixed, its positive compact minimum guarantees eventual success of a sufficiently small positive dyadic margin search.

This is a mathematical termination argument, **not** a runtime measurement, implemented verifier, or executed certificate.

## 6. Quantitative seven-coefficient thickening — SUPPORTED

**Locations:** S1 LF442–549.

With
\[
Q=\sum_{j=0}^7|q_j|,\qquad
\rho=\frac{\eta}{14Q},
\]
the stated estimates hold for every \(t=\omega^2\ge0\):
\[
|d(i\omega)|\le7\rho(1+t)^3,\qquad
|q(i\omega)|\le Q(1+t)^{7/2}.
\]
Hence
\[
\begin{aligned}
|P_{q,a+d}(t)-P_{q,a}(t)|
&\le7\rho Q(1+t)^{13/2}\\
&\le7\rho Q(1+t)^7\\
&=\frac{\eta}{2}(1+t)^7.
\end{aligned}
\]
The exponent comparison and factor fourteen are correct. Therefore
\[
P_{q,a+d}(t)\ge\frac{\eta}{2}(1+t)^7.
\]

The same estimate holds along every actual segment \(a+\tau d\). Positive pairing excludes every imaginary-axis zero on that segment; bounded coefficients and fixed monic degree exclude escape through infinity. Starting from the stable core member proves stability of the enlarged member.

The result does not depend on corner stability sampling. If Theorem 2’s premise is read independently of the standing eligibility definition, its original margin and stable \(q\) also establish stability of each core \(a\): the monic path \((1-\tau)q+\tau a\) has strictly positive pairing with \(q\) throughout. Thus that reading creates no missing stability premise.

For an independent box, its coordinatewise thickening is exactly
\[
\prod_{j=0}^{6}[\ell_j-\rho,u_j+\rho].
\]
All seven intervals acquire positive width, including previously fixed coordinates.

**Supported ceiling:** the radius is sufficient, not claimed optimal. No assertion is made that this neighborhood covers an arbitrary box’s complete opposite-parity variation.

## 7. Binomial full-dimensional boxes — SUPPORTED

**Locations:** S1 LF553–696; comparison with S2 LF11–27.

For \(\beta>0\) and \(0<\varepsilon<5/6\), the seven intervals
\[
a_j\in\beta^{7-j}
\left[\binom7j-\varepsilon,\binom7j+\varepsilon\right],
\qquad j=0,\ldots,6,
\]
are independent and have positive width.

The weighted Cauchy–Schwarz estimate is correct:
\[
\left(\sum_{j=0}^{6}x^j\right)^2
\le
\left(\sum_{j=0}^{6}\frac1{\binom7j}\right)
\left(\sum_{j=0}^{6}\binom7j x^{2j}\right).
\]
The manuscript’s exact scalar arithmetic checks:
\[
1+\frac27+\frac2{21}+\frac2{35}=\frac{151}{105},
\qquad
\frac{36}{25}-\frac{151}{105}=\frac1{525}>0.
\]
The second weighted sum is at most \((1+x^2)^7\), giving the sufficient factor \(6/5\).

With \(q_\beta=(s+\beta)^7\), this yields
\[
|d(i\omega)|\le\frac65\varepsilon\,|q_\beta(i\omega)|
\]
and therefore
\[
P_{q_\beta,a}(t)\ge
\left(1-\frac65\varepsilon\right)(\beta^2+t)^7>0.
\]
The same relative bound holds along \(q_\beta+\tau d\). Starting from the known stable binomial polynomial, the no-crossing proof establishes stability of **every actual member**.

### Manuscript-assigned rational instance

For the displayed \(\beta=1,\varepsilon=3/4\), all seven tabulated intervals match the binomial coefficients, and
\[
1-\frac65\frac34=\frac1{10}.
\]
Thus the stated uniform bound is correct.

Its \(a_6\) interval \([25/4,31/4]\) is disjoint from the former family’s interval near one in S2. The claimed example outside that former family is therefore supported.

This comparison does **not** establish containment of the entire former family, maximality of the new region, or universal synthesis.

## 8. Actual dual and ray consumers — SUPPORTED

**Locations:** S1 LF700–787; consuming-side definitions S3 LF7–32.

The raw row is consistent with the physical real-conjugate product:
\[
r_a(t)=
(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
For \(c=(q_0,\ldots,q_7)\),
\[
c\cdot r_a(t)=P_{q,a}(t).
\]
Every coefficient of the constructed stable numerator is strictly positive.

### 8.1 All-eight-strict-negative aggregates

For every nonzero finite nonnegative-weight family of actual atoms,
\[
c\cdot\sum_iw_ir_{a_i}(t_i)
=\sum_iw_iP_{q,a_i}(t_i)>0.
\]
An aggregate whose eight coordinates were strictly negative would have negative dot product with \(c>0\), a contradiction.

This excludes the specified strict-negative certificates for the supported families without relying on a frequency-count bound.

### 8.2 All four signed odd-moment inequalities

Using S3’s actual signed coordinates,
\[
R_1,R_3,R_5,R_7\le0
\]
implies
\[
\sum_iw_it_iG(t_i)O_i(t_i)
=q_1R_1+q_3R_3+q_5R_5+q_7R_7\le0.
\]
Consequently
\[
\sum_iw_iF(t_i)E_i(t_i)
=\sum_iw_iP_i-\sum_iw_it_iG(t_i)O_i(t_i)
\ge\sum_iw_iP_i>0.
\]
The common \(F,G\) are fixed **before** the atom and ray quantifiers.

### 8.3 Consuming-side coverage

The argument reaches every named S3 consumer:

- **Every R4 omitted moment.** For arbitrary omitted index \(k\), the stated Lagrange/Vandermonde weights give moments proportional to  
  \(\sum_iw_i u_i^{j+1}O_i=(-1)^{3-k}\delta_{jk}\).  
  After the signed-coordinate factor \((-1)^j\), the sole nonzero odd coordinate is negative. Thus every omitted-moment choice satisfies the four required inequalities.

- **Both R5 orientations.** The five-node identity  
  \(\sum_i u_i^j/H_5'(u_i)=0\) for \(j=0,\ldots,3\) makes all four odd moments zero for either normalization. Both positive-weight orientations therefore receive the same strict even-pairing conclusion.

- **Zero-odd singletons.** All four odd coordinates vanish; the even pairing equals the strictly positive full pairing.

- **Same-frequency opposite-odd cancellations.** The stated positive weights cancel the odd value and hence all four odd moments. The summed even pairing is strictly positive.

- **Combinations of these configurations.** The aggregate identity applies directly to every nonzero finite nonnegative combination.

The proof never divides by an odd value. Zero values are therefore not silently excluded.

### 8.4 Actual endpoint choices and frequency endpoints

For independent boxes, the pointwise minimizing even endpoint and an independently selected odd endpoint form an actual member at each node. The pairing inequality applies to those actual members; it does not require the minimizing even endpoint polynomial to remain the same across nodes.

This endpoint-replacement claim is properly restricted to independent boxes, not generalized to arbitrary convex families.

At zero frequency, \(P_{q,a}(0)=q_0a_0>0\). At compactified infinity, \(\overline P_{q,a}(1)=1\). Neither endpoint is lost.

## 9. Accepted mathematical ceiling and remaining gap

The written reconstruction supports:

1. Strict common-SPR synthesis for every eligible compact convex **fixed-parity** septic family.
2. A positive, quantitatively specified independent seven-coordinate thickening with the **same** numerator.
3. The complete binomial-box family for \(\beta>0\), \(0<\varepsilon<5/6\), including the displayed rational instance and its exact bound.
4. Exclusion of all-eight-strict-negative actual aggregates for those families.
5. Strict even pairing for every actual family in the four-inequality odd-moment cone, including all R4 choices, both R5 orientations, cancellations, zero-odd atoms, and the stated endpoint handling.

The following remain **unproved by this return**:

- A common strict numerator for every eligible box with both parities varying.
- Coverage of an arbitrary original box by one fixed-parity slice’s certified thickening.
- A gluing or common-intersection theorem for separately synthesized slices.
- Arbitrary weak-separator strictification.
- A common root triple satisfying all required rays for every eligible nondegenerate-odd box.
- A genuine eligible box with an all-eight-strict-negative certificate.

The candidate states these limitations accurately at S1 LF791–823. The prior weak-separation, six-node, and W1-only results are not promoted into stronger conclusions.

No source-wide correspondence, novelty, priority, worldwide status, human review, independent-family acceptance, or formal/kernel verification is established.

## 10. Final verdict

**Findings:** None meeting the actionable-defect criteria. **0 FATAL / 0 MAJOR / 0 MINOR.**

**Overall correctness:** **correct**, within the stated sufficient-class scopes.

**Explanation:** The fixed-parity constructions, quantitative thickening, and binomial boxes admit complete written reconstruction, including all-member stability and the actual consumer routes. They do not resolve the arbitrary all-Hurwitz septic-box synthesis problem.

**Confidence:** **0.97**.