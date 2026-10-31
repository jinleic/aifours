# F623 written review — buffered strictification and universal equivalence

**Role:** WRITTEN. **Scientific execution:** NOTRUN.  
**Review disposition:** The candidate’s strictification theorem, weak-separation lemma, universal-equivalence argument and rational finite-counterexample normal form are supported at their stated scopes. This is not a proof of universal septic synthesis or an actual counterexample, and it does not adopt the candidate on the parent’s behalf.

## 1. Frozen inputs and completed coverage

Reviewed the complete frozen packet in:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f623-septic-universal-spr-dual-root-equivalence-and-counterexample-review/`

Bindings supplied by the parent metadata:

- Manifest SHA256: `1e8894b142da3efec4ef723d91f8ea9421b30ab9e080e112b4e16b1ead104648`
- Freeze-receipt SHA256: `498eb9fb62f5fe9ff4d929c1113832b33417e62a61a4cebbfbab5d6700f48487`
- Literal-packet SHA256: `c1e2e39a57cf4f9aa35701d6caa87ee2b7645b211a20e82f527a1c92c0fa7fad`

These are **parent-supplied observations**, not child-native hash measurements.

Complete mathematical coverage:

- **S1:** f604 author candidate, SHA256 `870f63769e11b298073a3e23fc48684391789e61f40ea0330326f55bb3b84c3f`, logical LF **1–533**, including the ending.
- **S2:** actual-box three-root/cone disposition, SHA256 `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`, LF **1–46**, including the ending.
- **Packet:** LF **1–581**, read consecutively in raw windows of at most twenty lines, completed before mathematical reconstruction.

Hereafter, line references identify these source labels, not the packet’s outer line numbers.

## 2. Findings

**0 FATAL / 0 MAJOR / 0 MINOR mathematical findings.**

No patch-equivalent, source-anchored defect was established in the candidate’s claimed conditional results. The qualifications below delimit what was reconstructed and imported; they are not findings against correctly qualified claims.

## 3. Claim-by-claim disposition

| Claim | Source lines | Disposition |
|---|---|---|
| Physical pairing, raw row and common-numerator quantifiers | S1:19–77 | **SUPPORTED** |
| Two-coordinate buffer inequality | S1:128–157 | **SUPPORTED** |
| Boundary-zero exclusion for the weak numerator | S1:163–228 | **SUPPORTED** |
| Uniform endpoint repair and stability of the resulting monic septic | S1:232–308 | **SUPPORTED** |
| Arbitrarily small eligible buffers | S1:314–324 | **SUPPORTED** |
| Actual-row weak separation | S1:332–363 | **SUPPORTED** |
| Universal SPR ⇔ DUAL ⇔ ROOT | S1:369–413 | **SUPPORTED conditional on the exact S2 A ⇔ B import** |
| One fixed numerator’s handling of all listed odd-cone consumers | S1:419–460 | **SUPPORTED** |
| Rational full-width counterexample normal form with at most eight corner atoms | S1:468–490 | **SUPPORTED as an existence implication, not an exhibited witness** |
| Resolution of universal ROOT, global synthesis or an actual strict-negative certificate | S1:494–509 | **NOT PROVED, as the candidate explicitly states** |
| Author’s historical process reports and worldwide novelty/status | S1:513–533 | **Not independently certified by this review** |

## 4. Reconstruction of Theorem 1

### 4.1 The buffer supplies the required strict interior control

For fixed general \(a\in K\) and \(t\ge0\), coefficient independence permits both constant and linear perturbations simultaneously. Their contribution to the physical pairing is

\[
d_0F_q(t)+d_1tG_q(t).
\]

Minimizing these two terms over their permitted intervals gives exactly

\[
P_{q,a}(t)\ge h_0|F_q(t)|+h_1t|G_q(t)|.
\]

Thus, for \(t>0\), failure of strict positivity requires both \(F_q(t)=0\) and \(G_q(t)=0\), equivalently a positive imaginary-axis zero of \(q\). The argument does not require a single minimizing member to work at every frequency: the weak premise is quantified over **all** members of \(L\), permitting the member used in this inequality to depend on \(a,t\).

### 4.2 The boundary-zero argument is valid

For each \(b\in L\), put \(f_b=q/b\). This is proper and analytic across the imaginary axis and throughout the right half-plane, because \(b\) is strictly Hurwitz. Its limiting value at infinity is \(q_7\ge0\).

The boundary hypothesis and the harmonic minimum principle give \(\operatorname{Re}f_b\ge0\) inside the right half-plane. When the limiting value is zero, one can use arbitrarily small negative lower bounds on sufficiently large semicircles and pass to the limit; a strictly positive limiting constant is not required.

The strong minimum principle then gives strict interior positivity. The exceptional constant-pure-imaginary case is impossible for nonzero \(q\): real coefficients make \(f_b\) real on the positive real axis, forcing that constant, and hence \(q\), to vanish.

At an imaginary-axis zero \(z_0\), the local expansion

\[
f_b(s)=c(s-z_0)^m+O((s-z_0)^{m+1})
\]

must have nonnegative leading real part along every interior direction. The angular interval has width \(\pi\); therefore \(m\ge2\) is impossible, while \(m=1\) forces \(c>0\) real. Consequently,

\[
q'(z_0)/b(z_0)>0
\]

is real.

If the common numerator vanished at \(z_0=i\omega_0\), \(\omega_0>0\), every \(b(z_0)\) would therefore lie on one positive ray determined by the same nonzero \(q'(z_0)\). But the permitted independent perturbations produce

\[
a(i\omega_0)+d_0+i\omega_0d_1,
\]

a rectangle with nonempty two-dimensional interior. It cannot be contained in that ray. This establishes strict physical pairing at every positive finite frequency.

This step correctly leaves the zero-frequency and leading-coefficient issues for the separate endpoint repair.

### 4.3 The repair is uniform over the whole original box

After compactification, both \(p_a(u)\) and \(R_a(u)\) are continuous on the compact set \(K\times[0,1]\). The former is nonnegative everywhere and strictly positive in the open frequency interval. The latter satisfies

\[
R_a(0)=a_{*,0}a_0>0,\qquad R_a(1)=1.
\]

The positivity at zero is uniform: the constant coefficient is a continuous positive function on the compact eligible box. Consequently, common endpoint neighborhoods and one \(c>0\) exist with \(R_a\ge c\).

On the remaining compact middle interval, \(p_a\) has one positive minimum \(m\), while \(|R_a|\) has a finite global bound \(M\). The candidate’s choice

\[
\delta=\frac{m}{2(M+1)}
\]

therefore preserves at least \(m/2\) in the middle and supplies at least \(\delta c\) near both endpoints.

Since \(q_7+\delta>0\), the resulting

\[
Q=\frac{q+\delta a_*}{q_7+\delta}
\]

is genuinely monic of degree seven, including when \(q_7=0\). The displayed \(\eta\) is positive and provides the claimed bound simultaneously for all \(a\in K\) and \(t\ge0\). No assumption that \(a_*/a\) is positive real in the middle of the interval has entered the argument.

### 4.4 Stability follows from the constructed inequality

For any actual \(a\in K\), \(Q/a\) is proper, analytic in the right half-plane, tends to \(1\), and has strictly positive boundary real part. The harmonic argument excludes its zeros in the open right half-plane. The strict boundary inequality excludes imaginary-axis zeros of \(Q\).

Thus every zero of the monic septic \(Q\) lies strictly in the left half-plane. The coefficient-positivity statement is also justified independently by \(q\ge0\), \(\delta>0\), and the strictly positive coefficients of the real monic Hurwitz reference \(a_*\).

## 5. Buffer existence and actual-row separation

### 5.1 Eligible buffers

S1:320–324 correctly uses compact containment in the open set of Hurwitz coefficient vectors. One uniform coefficient neighborhood of \(K\) remains stable; sufficiently small positive constant and linear perturbation widths lie within it.

This does not rely on an unjustified arbitrary-vertex stability test. The resulting \(L\) remains an independent compact monic septic box, and its linear interval necessarily has positive width.

### 5.2 Endpoint removal and separation

The normalized rows extend continuously with limits

\[
\widehat r_b(0)=b_0e_0,\qquad
\widehat r_b(\infty)=e_7.
\]

Both are coordinatewise nonnegative. The compactified row set and its finite-dimensional convex hull are compact.

If that hull contained a strictly negative vector, a finite convex representation would exist. Removing its endpoint contributions preserves strict negativity, because the removed terms are nonnegative. The remaining positive-finite-frequency family cannot be empty: endpoint terms alone cannot produce a strictly negative vector. A remaining term \(\lambda_i\widehat r_{b_i}(t_i)\) corresponds to the positive raw-row weight \(\lambda_i/(1+t_i)^7\). Hence such an intersection would contradict the stated absence of a certificate.

Separation from the open negative orthant supplies a nonzero normal. Any negative coordinate of that normal would make its supremum over the negative orthant infinite. Thus the normal is coefficientwise nonnegative, and that supremum is zero. Its pairing with every normalized actual row is therefore nonnegative, yielding the claimed weak numerator after removing the positive normalization.

The proof supplies a **weak** separator only; strictification is correctly deferred to the buffered theorem.

## 6. Universal equivalence and exact import boundary

The mathematical import is **S2:13–32**, specifically its equivalence between:

- **A:** absence of an actual-member strict-negative aggregate; and
- **B:** one triple in the stated root intervals satisfying every actual-endpoint R4 condition and both R5 orientations.

S2:7–9 supplies the eligible actual-box and nondegenerate-odd setting. The full underlying Hermite–Biehler and cone-classification source proofs were not opened or independently re-audited here. This review uses the frozen disposition at precisely its supplied scope. The author’s phrase “frozen S1” refers to that original input; it is labelled **S2 in this review packet**.

With this import:

- **SPR ⇒ DUAL:** A stable monic numerator has positive coefficients. Its pairing with a coordinatewise strictly negative aggregate is negative, whereas its pairing with the corresponding positive-weight family is strictly positive.
- **DUAL ⇒ SPR:** For arbitrary original \(K\), construct eligible \(L\), apply universal DUAL to **\(L\)**, obtain the weak separator there, and strictify on **\(K\)**.
- **ROOT ⇒ SPR:** Apply universal ROOT to the eligible buffered \(L\), whose linear uncertainty is nondegenerate. Imported B ⇒ A supplies the separation premise on \(L\); strictification supplies one numerator on \(K\).
- **SPR ⇒ ROOT:** Universal SPR excludes certificates on each eligible box; imported A ⇒ B applies wherever odd uncertainty is nondegenerate.

The existential triple remains before every ray quantifier. The numerator constructed for each original box remains fixed before all its member and frequency quantifiers.

The qualification at S1:399–413 is essential and correct: the proof establishes buffered \(B(L)\Rightarrow\) strict synthesis on \(K\), **not** the same-box implication \(B(K)\Rightarrow\) strict synthesis on \(K\). Likewise, failure on \(K\) yields a certificate on an eligible buffer in the later contrapositive argument, not necessarily inside \(K\).

## 7. Consuming-side check: all odd-cone families use the same numerator

S1:419–460 correctly carries the constructed \(Q\) into the downstream pairing.

For any nonempty positive-weight actual family, its total physical pairing is strictly positive. If its signed odd-coordinate aggregate is nonpositive, its dot product with the positive odd coefficients of \(Q\) is nonpositive. Subtracting that odd contribution leaves a strictly positive even pairing.

This covers each listed consumer through its defining odd-moment condition:

- every feasible R4 omitted-moment case;
- either feasible R5 orientation;
- zero-odd singletons;
- same-frequency opposite-odd cancellations;
- positive combinations of these families.

No branch silently discards the opposite orientation, no zero odd value is divided by, and no family receives a newly chosen numerator.

## 8. Rational finite-counterexample normal form

The contrapositive step is valid: if the buffered \(L\) had no strict-negative certificate, separation and strictification would contradict the assumed failure of synthesis on \(K\).

For the resulting finite certificate:

1. At each fixed frequency, the row is affine in the uncertain coefficient vector. Decomposing an actual member into actual coefficient corners therefore preserves its row and the complete aggregate exactly.
2. Conic Carathéodory reduction in \(\mathbb R^8\) preserves that aggregate with at most eight positive corner atoms. A linear dependence permits decreasing the positive weights until one vanishes, then iterating.
3. Robust stability is open in box-endpoint parameters: sufficiently small endpoint perturbations keep the new box inside a stable neighborhood of the old compact box.
4. The eight strict aggregate inequalities are open conditions in the endpoints and finitely many positive squared frequencies and weights. Simultaneous rational approximation preserves them.
5. Degenerate intervals cause no obstruction to choosing nearby strictly ordered rational endpoints. Keeping each selected corner’s endpoint labels gives continuous perturbations of all retained atoms.

The result concerns **positive rational squared frequencies**, not necessarily rational frequencies. It bounds total corner atoms by eight; it does not guarantee exactly six frequencies or preserve a prescribed frequency set. No actual rational box, aggregate or stability certificate is exhibited.

## 9. Process chronology and additive count correction

Before any mathematical packet read, I read the complete manifest, freeze receipt, parent metadata supply, dispatch receipt, and all **fifteen** listed status-only controls, then sent the direct PREBODY ACK.

Completed control endings were:

| Listed control | Final LF read |
|---|---:|
| Owner direction addendum 2 | 14 |
| Parent L1 quarantine | 23 |
| Parent written-duty deviations | 28 |
| Held PH consumer quarantine | 49 |
| f439 status control | 23 |
| f444 status control | 16 |
| f448 status control | 20 |
| f508 status control | 22 |
| f513 status control | 22 |
| f586 status control | 23 |
| f602 status control | 23 |
| f596 status control | 24 |
| Parent AME consumer quarantine | 8 |
| Parent CORE-GRAM quarantine | 9 |
| Parent privacy quarantine | 11 |

My PREBODY ACK incorrectly said “sixteen.” I corrected this additively by direct message and acknowledged the parent’s status-only reconciliation. The error was in the reported count, not an omitted read; no scientific scope or conclusion was changed because of it.

After the ACK, I completed the ordered packet reads through both source endings before reconstructing the general arguments above. I used no fresh selected mathematical instance, probe, scientific executable, CAS, solver, enumeration, external source, sibling review, author code or held mathematical payload. No repository file was written. This complete body is returned for parent materialization under the read-only boundary.

## Overall correctness

**correct**

The candidate’s buffered strictification, actual-row separation and finite-counterexample normal form withstand written reconstruction; its universal equivalence is supported conditional on the exact frozen S2 three-root equivalence. The universal common-triple assertion and the original synthesis-or-counterexample target remain unresolved, with no novelty, independent-family, human or kernel-verification credit supplied by this review.

**Confidence:** 0.98