# Written review — f622 septic two-coordinate-buffer strictification

**Overall correctness: correct at the stated conditional scope.**

The buffered weak-to-strict theorem is supported by the written argument, including its nonzero-frequency boundary-zero exclusion, both compactified endpoints, uniform whole-box perturbation, and numerator stability. The universal SPR/DUAL/ROOT equivalence is supported conditional on the exact adopted three-root equivalence reproduced in S2; neither the universal ROOT assertion nor an actual counterexample is established.

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.97.**  
**Scientific execution: NOTRUN.**

## 1. Review boundary and completed source coverage

This review concerns the candidate:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f604-actual-septic-both-parity-box-common-spr-or-strict-dual-frontier/review-v1.md`

It was read as **S1, logical lines 1–533**, in the frozen f622 literal packet.

Before opening that packet, I completely read:

- The f622 manifest and freeze receipt.
- The parent metadata supply and dispatch receipt.
- All fifteen manifest-listed status-only controls, including their endings.

I then sent a direct administrative **PREBODY ACK to `agent://Main`**. Only afterward did I read the complete literal packet, **LF 1–620**, in ordered raw windows of at most twenty LF, including all source endings. Mathematical reconstruction began after that complete read.

Packet coverage was:

| Source | Complete source coverage | Use in this review |
|---|---:|---|
| S1: f604 author candidate | Logical LF 1–533 | Candidate reconstructed below |
| S2: adopted actual-box three-root/dual reduction | LF 1–46 | Exact-scope mathematical import |
| S3: adopted fixed-parity/thickening/binomial disposition | LF 1–39 | Scope context; not an arbitrary-box synthesis premise |

The frozen bindings supplied by parent metadata are:

- Manifest: `fe91a04e89a1f9f58d00b96ede39653d80f7b1d4915b465e8e6fb9d92a2a8c41`
- Freeze receipt: `8e9f8d12226672333195ab2719cf56d6423db1914c8089c475066491595994c9`
- Literal packet: `b6afb2ef6e933966391a9f76f51b4892a3424cf4ad607f44292ece60eb2cfe93`
- S1: `870f63769e11b298073a3e23fc48684391789e61f40ea0330326f55bb3b84c3f`
- S2: `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`
- S3: `967da36f40018605296da178ac5493758603cf09bfea54b240342e5fa7c2af48`

These are **parent-observed metadata**, not child-native hash computations.

No linked source, sibling review, author code, held mathematical payload, or downstream held consumer was opened. All quarantine controls were used as status-only exclusions. No additional concrete polynomial, box, frequency, parameter example, or diagnostic instance was introduced.

## 2. Claim dispositions

| Claim | Disposition | Candidate lines |
|---|---|---|
| Physical pairing and eight-coordinate raw-row identity | **SUPPORTED** | S1:30–68 |
| Two-coordinate buffer inequality | **SUPPORTED** | S1:126–157 |
| Proper-rational positive-real interior argument | **SUPPORTED** | S1:161–178 |
| Boundary-zero simplicity and positive real derivative | **SUPPORTED** | S1:180–202 |
| Exclusion of every positive imaginary-axis zero using the actual buffer rectangle | **SUPPORTED** | S1:204–228 |
| One uniform perturbation repairs both compactified endpoints and preserves the middle | **SUPPORTED** | S1:230–298 |
| Monicity, strict positive coefficients, and Hurwitz stability of the constructed numerator | **SUPPORTED** | S1:300–308 |
| Arbitrarily small eligible buffers for every eligible compact box | **SUPPORTED** | S1:312–324 |
| Weak separation from absence of a finite strict-negative actual-row certificate | **SUPPORTED** | S1:328–363 |
| Universal SPR ⇔ DUAL ⇔ ROOT equivalence | **SUPPORTED, conditional on the adopted S2 A⇔B import** | S1:367–413 |
| Actual R4, both R5 orientations, zero-odd and cancellation consumers | **SUPPORTED** | S1:417–460 |
| Rational, full-dimensional, at-most-eight-atom counterexample normal form | **SUPPORTED as an existence implication only** | S1:464–490 |
| Universal common-triple existence or universal arbitrary-box synthesis | **INCONCLUSIVE / NOT PROVED**, correctly disclosed | S1:494–509 |
| Existence of an actual strict-negative certificate | **INCONCLUSIVE / NOT SUPPLIED**, correctly disclosed | S1:7, 490, 500–507 |

No reviewed mathematical claim was refuted.

## 3. Reconstruction of Theorem 1

### 3.1 Physical pairing and the actual buffer

The parity decomposition gives

\[
P_{q,a}(t)=F_q(t)E_a(t)+tG_q(t)O_a(t),
\]

and expansion against the ascending coefficient vector of \(q\) gives exactly the raw row displayed at S1:60–68. In particular, the odd-coordinate signs agree with the physical conjugate-product pairing.

Adding \(d_0+d_1s\) changes the pairing by

\[
P_{q,a+d_0+d_1s}(t)-P_{q,a}(t)
=d_0F_q(t)+td_1G_q(t).
\]

The independent buffer permits both signs in both directions. Applying the weak inequality to the minimizing permitted signs therefore gives

\[
P_{q,a}(t)\ge h_0|F_q(t)|+h_1t|G_q(t)|.
\]

This step uses actual members of \(L\), not independently assigned parity values that might fail to represent a member. The member used to establish this inequality may depend on the frequency because the premise already quantifies over **every** member and frequency; the numerator \(q\) remains fixed.

For \(t>0\), the right-hand side is positive unless \(F_q(t)=G_q(t)=0\), equivalently \(q(i\sqrt t)=0\). Thus the subsequent boundary-zero argument addresses exactly the remaining obstruction.

### 3.2 Positive real part in the open right half-plane

For an arbitrary strictly Hurwitz \(b\), the proper real rational function

\[
f(s)=q(s)/b(s)
\]

has no poles on or to the right of the imaginary axis. Its boundary real part is nonnegative by the physical pairing assumption. Its limit at infinity is the nonnegative real number \(q_7\), including the case \(q_7=0\).

The large-half-disc argument remains valid when that limit is zero. For any positive error tolerance, the real part on sufficiently large semicircular boundaries is bounded below by the negative of that tolerance, while the imaginary-axis boundary is nonnegative. The harmonic minimum principle and passage to arbitrarily large half-discs therefore give \(\operatorname{Re}f\ge0\) throughout the open right half-plane.

If this harmonic function attained zero inside, the strong minimum principle would make its real part identically zero. Analyticity would then make \(f\) a purely imaginary constant. Real coefficients make \(f\) real on the positive real axis, so that constant must be zero, contradicting \(q\ne0\).

Consequently,

\[
\operatorname{Re}(q(s)/b(s))>0
\quad(\operatorname{Re}s>0).
\]

The proof does not assume positive limiting ratio; nonnegative limiting ratio suffices.

### 3.3 The boundary-zero derivative assertion

At a finite imaginary-axis zero \(z_0\), analyticity through the boundary permits the local expansion

\[
f(s)=c(s-z_0)^m+O((s-z_0)^{m+1}),\qquad c\ne0.
\]

Positivity in every interior approach direction forces

\[
\operatorname{Re}(ce^{im\theta})\ge0
\quad\text{throughout }-\pi/2<\theta<\pi/2.
\]

For \(m\ge2\), the angular sweep necessarily encounters a negative real part, contradicting that condition. For \(m=1\), nonnegativity throughout that entire half-plane angular interval forces \(c\) to be positive real.

Therefore the zero is simple and

\[
f'(z_0)=q'(z_0)/b(z_0)>0
\]

is real. The derivative formula is correct because \(q(z_0)=0\).

### 3.4 Why the actual two-dimensional buffer excludes positive-frequency zeros

If \(q(i\omega_0)=0\) with \(\omega_0>0\), the preceding result applies to **every** \(b\in L\). It would place every \(b(i\omega_0)\) on the single positive real ray through the same nonzero \(q'(i\omega_0)\).

For a fixed actual \(a\in K\), the permitted values

\[
a(i\omega_0)+d_0+i\omega_0d_1
\]

contain a rectangle with nonempty two-dimensional interior because \(h_0,h_1,\omega_0\) are all positive. Such a rectangle cannot be contained in that ray.

This excludes every positive imaginary-axis zero of \(q\). Combining it with the buffer inequality gives

\[
P_{q,a}(t)>0\qquad(a\in K,\ 0<t<\infty).
\]

The argument does **not** incorrectly apply this rectangle conclusion at zero frequency. Nor does it infer \(q_7>0\). Those two possible endpoint defects remain available for the next step to repair.

### 3.5 Uniform repair of both compactified endpoints

Both \(P_{q,a}\) and \(P_{a_*,a}\) have degree at most seven in \(t\), so division by \((1+t)^7\) and the substitution \(u=t/(1+t)\) give continuous functions on \(K\times[0,1]\).

For the reference direction,

\[
R_a(0)=a_{*,0}a_0,\qquad R_a(1)=1.
\]

The first expression is uniformly positive: monic real Hurwitz polynomials have positive constant coefficients, and compactness makes their minimum over \(K\) positive. The second expression follows from the monic leading terms of both septics.

Joint continuity and compactness therefore give common endpoint neighborhoods on which \(R_a\ge c>0\). On the complementary middle compact set, the already established strict positivity of \(p_a\) gives a common minimum \(m>0\). The absolute value of \(R_a\) has a finite global maximum \(M\).

For the stated choice

\[
\delta=\frac{m}{2(M+1)},
\]

one has \(\delta M<m/2\). Hence:

- On the endpoint neighborhoods, \(p_a+\delta R_a\ge\delta c\).
- On the middle, \(p_a+\delta R_a\ge m-\delta M>m/2\).

The same \(\delta\) works for every \(a\in K\) and every compactified frequency. It is not selected separately by member, ray, or frequency.

Because \(q_7+\delta>0\), normalization produces a monic septic and the stated uniform margin

\[
\eta=\frac{\min\{\delta c,m/2\}}{q_7+\delta}>0.
\]

No positive-real assumption on \(a_*/a\) is needed. Its possible negative contribution in the middle is precisely what the finite bound \(M\) controls.

### 3.6 Numerator stability

For any actual \(a\in K\), the constructed \(Q/a\) has strictly positive imaginary-axis real part and limit \(1\) at infinity. The same harmonic argument gives positive real part throughout the open right half-plane.

A zero of \(Q\) in that half-plane would make the ratio zero, contradicting this positivity. An imaginary-axis zero would contradict the uniform physical-pairing inequality. Thus every root of \(Q\) lies strictly in the left half-plane.

The construction also gives strict positivity of every coefficient: \(q\) is coefficientwise nonnegative, \(a_*\) is a monic real Hurwitz polynomial with strictly positive coefficients, and \(\delta>0\).

This completes the claimed stable, monic, strict whole-box construction without assuming numerator stability.

## 4. Buffer existence and weak separation

### 4.1 Eligible buffers

The monic degree-seven Hurwitz coefficient set is open. A compact \(K\) contained in that open set has a uniform coefficient neighborhood contained in it. Choosing both constant- and linear-direction perturbation widths sufficiently small places the entire independent enlargement \(L\) in that neighborhood.

The widths may then be decreased while remaining positive. This proves the “arbitrarily small” statement, including boxes with initially degenerate intervals. It uses all-member strict stability and does not replace that premise by an unsupported vertex test.

### 4.2 Absence of a strict-negative certificate yields the required weak numerator

The normalized actual row set compactifies continuously with endpoints

\[
b_0e_0,\qquad e_7,
\]

both coordinatewise nonnegative. Its convex hull is compact in \(\mathbb R^8\).

If that convex hull contained a strictly negative vector, a finite convex representation could have its endpoint contributions removed. Subtracting coordinatewise nonnegative endpoint terms preserves strict negativity. The remaining positive finite-frequency normalized rows can be converted to raw rows by absorbing their positive normalizing factors into the weights. That would contradict the assumed absence of a finite certificate.

Separation from the open negative orthant supplies a nonzero normal. Its coordinates must all be nonnegative: any negative normal coordinate would make its supremum on the negative orthant infinite. For a nonnegative normal that supremum is zero, so every compactified actual row has nonnegative pairing with the normal.

Interpreting the normal as the coefficients of \(q\) supplies exactly the nonzero, degree-at-most-seven, coefficientwise nonnegative weak numerator required by Theorem 1. Neither closure nor endpoint compactification introduces a forbidden certificate at zero or infinite frequency.

## 5. Universal equivalence and exact imported scope

The candidate’s references to its “frozen S1” root equivalence refer to the predecessor disposition reproduced as **S2 in this review packet**.

The mathematical import used here is specifically:

- **S2:13–17:** A⇔B for eligible independent boxes with nondegenerate odd uncertainty.
- **S2:19–26:** The actual-endpoint ray conditions, including every R4 omitted-moment case, both R5 orientations, zero-odd singletons, and same-frequency cancellations.
- **S2:30–34:** The adopted scope and the distinction from strict synthesis.

I do not claim to have independently audited the unprovided underlying author/reviewer bodies or authenticated their historical executions.

At this exact import scope, all implications in Theorem 4 are valid:

1. **SPR ⇒ DUAL.** A stable monic real numerator has positive coefficients. Its dot product with an all-eight-strict-negative aggregate is negative, whereas the same dot product is a positive-weight sum of strictly positive physical pairings.

2. **DUAL ⇒ SPR.** For arbitrary \(K\), choose an eligible buffer \(L\). Universal DUAL applies to \(L\), Lemma 3 supplies the weak numerator on \(L\), and Theorem 1 supplies strict synthesis on the original \(K\).

3. **ROOT ⇒ SPR.** The same \(L\) has nondegenerate odd uncertainty because its linear interval was widened. The adopted A⇔B equivalence converts ROOT on \(L\) into absence of its strict-negative certificate. Lemma 3 and Theorem 1 then apply.

4. **SPR ⇒ ROOT.** Universal SPR excludes certificates for every eligible box, and the adopted equivalence gives B on every box in its nondegenerate-odd scope.

The essential quantifier distinction is preserved:

\[
B(L)\Longrightarrow\text{strict common synthesis on }K
\]

when \(L\) contains the stated eligible positive buffer. The argument does not establish the stronger unbuffered implication \(B(K)\Rightarrow\) strict common synthesis on that same \(K\).

Nevertheless, because every eligible original box has such an eligible enlargement, the **universal** statements are equivalent. The restriction to constant- and linear-positive-width boxes for the sufficient ROOT premise is therefore legitimate.

## 6. Consuming-side actual dual configurations

The constructed \(Q\) is fixed before every member, frequency, and ray quantifier. Its positive coefficients pair with the raw row exactly as required.

For any nonempty finite positive-weight actual-member family, the uniform theorem gives

\[
\sum_iw_iP_{Q,a_i}(t_i)>0.
\]

If its four signed odd-coordinate sums are nonpositive, their pairing with the positive odd coefficients of \(Q\) is nonpositive. Subtracting that contribution leaves a **strictly positive** even pairing.

This consumes the theorem’s output correctly for:

- Every actual R4 omitted-moment case.
- Both R5 orientations.
- Zero-odd singletons.
- Same-frequency opposite-odd cancellations.
- Positive combinations of those configurations.

There is no division by a zero odd value, discarded orientation, or fresh numerator choice per ray. Actual endpoint replacements remain subject to the independent-box actual-member interface supplied in S2.

## 7. Rational finite-counterexample normal form

Corollary 5 is supported as a counterfactual existence result.

If \(K\) lacks strict common synthesis, an eligible buffer \(L\) cannot lack a strict-negative certificate: otherwise Lemma 3 and Theorem 1 would synthesize a numerator for \(K\).

At each certificate frequency, the raw row is affine in the seven coefficient coordinates. Decomposing actual members into actual box corners therefore preserves the entire aggregate exactly.

Conic Carathéodory reduction in \(\mathbb R^8\) then reduces the representation to at most eight positive corner atoms. The stated dependence-elimination argument preserves the vector while maintaining nonnegative weights and removing at least one positive atom per reduction.

Finally:

- Robust Hurwitz stability of a compact coefficient box persists under sufficiently small endpoint perturbations.
- All eight strict-negative aggregate inequalities persist under sufficiently small perturbations of their finite data.
- Positive rational squared frequencies and positive rational weights can approximate the existing positive data.
- Rational endpoint approximations can give every interval positive width, including initially degenerate coordinates.
- Keeping each corner’s endpoint labels makes each retained atom vary continuously with those endpoint perturbations.

Thus the claimed rational, full-dimensional, at-most-eight-atom normal form follows.

This is a finite-atom rational normal form, **not** an exhibited counterexample, a finite exhaustive list, a runtime bound, or a six-frequency theorem. It does not move the buffered certificate back inside the unexpanded original box.

## 8. Acceptance boundary and process statement

The following are supported by this written reconstruction:

- Theorem 1 in its full stated arbitrary-box, positive two-coordinate-buffer scope.
- Lemmas 2 and 3.
- Theorem 4 conditional on the exact adopted S2 A⇔B import.
- The actual dual-consumer consequences.
- Corollary 5 as an existence implication.

The following remain unproved or unverified here:

- Universal existence of the common triple.
- Universal arbitrary-box strict common-SPR synthesis as an unconditional theorem.
- Any actual eligible strict-negative aggregate.
- A per-box unbuffered weak-to-strict theorem.
- Historical finite-check executions referenced in S3.
- Novelty, worldwide status, original printed-source equivalence, independent-family review, human verification, or formal/kernel acceptance.

No scientific executable, interpreter, CAS, solver, enumeration, replay, build, test, lint, external-model CLI, or background scientific process was run. No repository file was written under the read-only boundary; this complete body is returned for parent materialization.

**Final verdict: correct at the reconstructed conditional scope; 0 FATAL / 0 MAJOR / 0 MINOR.**