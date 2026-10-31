# Author candidate v1 — robust strictification of the actual septic-box dual interface

**Wave:** f604-actual-septic-both-parity-box-common-spr-or-strict-dual-frontier  
**Role:** GENERALAUTHOR  
**Disposition requested:** written-mathematical review of the hard-interface theorem below.

**Original target: NOT PROVED. No actual strict-negative counterexample is supplied.**

The result below removes the weak-to-strict gap at the **universal original-box level**: it suffices to establish the frozen common-three-root condition for every eligible box, because an arbitrarily small, still-Hurwitz enlargement in just the constant and linear coefficient directions converts its weak separator into **one stable, strict common numerator for the entire original box**.

This is not a fixed-parity theorem, a neighborhood cover, or a choice of different numerators for different slices. It is a conditional theorem for an arbitrary original box, together with an exact equivalence of the remaining universal problems. It does **not** establish the missing common-three-root condition.

No scientific executable was run. All new results below are author-written mathematical candidates, not independently reviewed or accepted results.

---

## 1. Target, notation, and actual members

Let

\[
K=\left\{
a(s)=s^7+\sum_{j=0}^{6}a_js^j:
\ell_j\le a_j\le u_j
\right\}
\]

be a nonempty compact independent coefficient box, every member of which is strictly Hurwitz. Intervals may be degenerate, and both parities may vary.

For \(t=\omega^2\), write

\[
a(i\omega)=E_a(t)+i\omega O_a(t),
\]

where

\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

For a real polynomial \(q(s)=\sum_{j=0}^{7}q_js^j\), put

\[
F_q(t)=q_0-q_2t+q_4t^2-q_6t^3,\qquad
G_q(t)=q_1-q_3t+q_5t^2-q_7t^3.
\]

The physical pairing is

\[
P_{q,a}(t)
=\operatorname{Re}\!\left(q(i\omega)\overline{a(i\omega)}\right)
=F_q(t)E_a(t)+tG_q(t)O_a(t).
\]

Its raw row, in ascending coefficient order, is

\[
r_a(t)=
(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a),
\]

so that

\[
q\mathbin{\cdot}r_a(t)=P_{q,a}(t).
\]

The original synthesis target is one stable monic septic \(Q\), fixed before all member and frequency quantifiers, such that

\[
P_{Q,a}(t)>0\qquad(a\in K,\ t\ge0).
\]

The opposing certificate consists of finitely many **actual** members, positive frequencies and positive weights whose aggregate raw row has all eight coordinates strictly negative.

---

## 2. New hard-interface theorem

### Theorem 1 — two-coordinate-buffer strictification

Suppose there are \(h_0,h_1>0\) such that the enlarged independent box

\[
L=
\left\{
a+d_0+d_1s:
a\in K,\ |d_0|\le h_0,\ |d_1|\le h_1
\right\}
\]

is entirely strictly Hurwitz.

Suppose a nonzero real polynomial \(q\), of degree at most seven and with coefficientwise nonnegative coefficients, satisfies

\[
P_{q,b}(t)\ge0
\qquad(b\in L,\ t\ge0).
\tag{1}
\]

Then there is **one stable monic septic** \(Q\) and \(\eta>0\) such that

\[
P_{Q,a}(t)\ge\eta(1+t)^7
\qquad(a\in K,\ t\ge0).
\tag{2}
\]

In particular, \(Q/a\) is strictly positive real for every actual member of the original box \(K\).

The construction uses the same \(q\), one actual reference \(a_*\in K\), and one sufficiently small scalar \(\delta>0\):

\[
Q(s)=\frac{q(s)+\delta a_*(s)}{q_7+\delta}.
\tag{3}
\]

It does not require \(a_*/a\) to be positive real throughout the box.

### Proof

#### Step 1: the coefficient buffer gives a quantitative interior inequality

Fix an actual \(a\in K\) and \(t\ge0\). By independence, the member

\[
b=a+d_0+d_1s
\]

belongs to \(L\) for either sign of each permitted perturbation. Choose

\[
d_0=-h_0\operatorname{sgn}F_q(t),\qquad
d_1=-h_1\operatorname{sgn}G_q(t),
\]

with either sign allowed when the corresponding value vanishes.

Applying (1) to this actual member gives

\[
P_{q,a}(t)
\ge h_0|F_q(t)|+h_1t|G_q(t)|.
\tag{4}
\]

Thus, at every \(t>0\), strict positivity follows unless

\[
F_q(t)=G_q(t)=0,
\]

equivalently \(q(i\sqrt t)=0\). The next step excludes that exceptional possibility.

#### Step 2: a weak common numerator cannot have a positive imaginary-axis zero

We first prove the elementary rational-function fact needed here.

Let \(b\) be strictly Hurwitz and let \(q\ne0\) be real, with \(\deg q\le\deg b\), nonnegative limiting ratio at infinity, and

\[
\operatorname{Re}\frac{q(i\omega)}{b(i\omega)}\ge0
\qquad(\omega\in\mathbb R).
\]

Then

\[
\operatorname{Re}\frac{q(s)}{b(s)}>0
\qquad(\operatorname{Re}s>0).
\tag{5}
\]

Indeed, the ratio is analytic in the closed right half-plane and tends uniformly at infinity to a nonnegative real constant. The harmonic minimum principle on large right half-discs first gives nonnegative real part inside. The strong minimum principle makes it strictly positive unless the real part is identically zero. That exceptional case would make the ratio a purely imaginary constant; real coefficients and its real values on the positive real axis then force the ratio, and hence \(q\), to vanish identically.

Moreover, any imaginary-axis zero of this ratio is simple, and at a zero \(z_0\),

\[
\frac{q'(z_0)}{b(z_0)}>0
\quad\hbox{is real}.
\tag{6}
\]

For completeness, write its local expansion as

\[
\frac{q(s)}{b(s)}
=c(s-z_0)^m+O((s-z_0)^{m+1}),\qquad c\ne0.
\]

Approaching \(z_0\) along the interior directions
\(s-z_0=re^{i\theta}\), \(-\pi/2<\theta<\pi/2\), equation (5) requires

\[
\operatorname{Re}(ce^{im\theta})\ge0
\]

for all these directions. This is impossible for \(m\ge2\). For \(m=1\), it requires \(c\) to be positive real, proving (6).

Apply this fact to every \(b\in L\). Its hypotheses hold because \(q_7\ge0\) and (1) holds. If \(q(i\omega_0)=0\) for some \(\omega_0>0\), then for every \(b\in L\),

\[
b(i\omega_0)
\]

must lie on the same positive real ray through \(q'(i\omega_0)\), by (6).

But varying \(d_0,d_1\) independently makes the actual values

\[
b(i\omega_0)=a(i\omega_0)+d_0+i\omega_0d_1
\]

contain a rectangle with nonempty two-dimensional interior. Such a rectangle cannot lie on a ray. This contradiction excludes all positive imaginary-axis zeros of \(q\).

Combining this with (4),

\[
P_{q,a}(t)>0
\qquad(a\in K,\ 0<t<\infty).
\tag{7}
\]

A possible zero of \(q\) at \(s=0\), or a zero leading septic coefficient \(q_7\), has not been silently excluded. Both are handled next.

#### Step 3: repair both compactified endpoints with one perturbation

Choose one actual \(a_*\in K\). Compactify by \(u=t/(1+t)\), and define

\[
p_a(u)=\frac{P_{q,a}(t)}{(1+t)^7},\qquad
R_a(u)=\frac{P_{a_*,a}(t)}{(1+t)^7}.
\]

These extend continuously to \(K\times[0,1]\). We have

\[
p_a(u)\ge0
\]

everywhere, and by (7) it is strictly positive for \(0<u<1\).

The endpoint values of the perturbation direction are

\[
R_a(0)=a_{*,0}a_0>0,\qquad R_a(1)=1.
\tag{8}
\]

Strict positivity at zero is uniform because \(K\) is compact and all its members are Hurwitz, hence their constant coefficients are positive.

Consequently, there are \(0<\gamma<1/2\) and \(c>0\) such that

\[
R_a(u)\ge c
\]

for every \(a\in K\) whenever
\(u\in[0,\gamma]\cup[1-\gamma,1]\).

On the middle compact set, define

\[
m=\min_{a\in K,\ \gamma\le u\le1-\gamma}p_a(u)>0,
\qquad
M=\max_{a\in K,\ 0\le u\le1}|R_a(u)|<\infty.
\]

Take, for example,

\[
\delta=\frac{m}{2(M+1)}>0.
\]

Then

\[
p_a(u)+\delta R_a(u)
\ge
\begin{cases}
\delta c,&u\in[0,\gamma]\cup[1-\gamma,1],\\[2mm]
m/2,&u\in[\gamma,1-\gamma].
\end{cases}
\]

Since \(q_7+\delta>0\), formula (3) yields (2), with

\[
\eta=
\frac{\min\{\delta c,m/2\}}{q_7+\delta}>0.
\tag{9}
\]

This is one \(\delta\), one numerator and one margin for the entire original box and the entire frequency half-axis.

#### Step 4: numerator stability is a conclusion, not an assumption

For any actual \(a\in K\), equation (2) gives strictly positive boundary real part for \(Q/a\). This proper rational function is analytic in the right half-plane and tends to \(1\) at infinity. The same harmonic argument gives positive real part throughout the open right half-plane.

A right-half-plane zero of \(Q\) would contradict this positivity. An imaginary-axis zero would contradict (2). Thus \(Q\) is strictly Hurwitz.

Its coefficients are also strictly positive directly: \(q\) is coefficientwise nonnegative, \(a_*\) is a monic real Hurwitz polynomial and therefore has strictly positive coefficients, and \(\delta>0\).

This proves the theorem. ∎

---

## 3. The buffer is available for every original eligible box

### Lemma 2 — arbitrarily small eligible buffers exist

For every eligible \(K\), there exist arbitrarily small positive \(h_0,h_1\) for which the box \(L\) in Theorem 1 is entirely strictly Hurwitz.

### Proof

The set of monic degree-seven Hurwitz coefficient vectors is open. The compact coefficient box \(K\) is contained in that open set. Therefore a sufficiently small uniform coefficient neighborhood of \(K\) remains inside it.

The two-coordinate perturbations defining \(L\) can be chosen inside that neighborhood, and can then be decreased arbitrarily. ∎

This step uses all-member strict Hurwitz stability and compactness. It does not assert that checking arbitrary box vertices suffices.

---

## 4. Absence of a strict-negative certificate supplies the needed weak numerator

The following separation argument is included so that the strictification theorem is not resting on an unexplained weak-numerator premise.

### Lemma 3 — actual-row weak separation

Let \(L\) be an eligible compact independent septic box. If no finite positive-weight aggregate of actual rows at positive frequencies is strictly negative in all eight coordinates, then there is a nonzero coefficientwise nonnegative \(q\), of degree at most seven, such that

\[
P_{q,b}(t)\ge0
\qquad(b\in L,\ t\ge0).
\tag{10}
\]

### Proof

Consider the normalized actual rows

\[
\widehat r_b(t)=\frac{r_b(t)}{(1+t)^7}.
\]

Their compactification has endpoint values

\[
\widehat r_b(0)=b_0e_0,\qquad
\widehat r_b(\infty)=e_7.
\]

The compactified row set is compact, and so is its convex hull in \(\mathbb R^8\).

Its convex hull is disjoint from the open strictly negative orthant. Otherwise, a finite convex representation of a strictly negative vector could have its zero- and infinite-frequency endpoint contributions removed. Those endpoint contributions are coordinatewise nonnegative, so removing them preserves strict negativity. Rescaling the remaining normalized rows would give a forbidden finite certificate at positive finite frequencies.

Separate this compact convex hull from the open negative orthant. The separating normal can be chosen nonzero and coefficientwise nonnegative: a negative normal coordinate would make its supremum on the negative orthant infinite. The supremum for a nonnegative normal is zero, so its pairing with every compactified actual row is nonnegative.

Interpret that normal as the coefficients of \(q\). Removing the positive normalization gives (10). ∎

---

## 5. Exact universal equivalence: the separate weak-to-strict obstacle disappears

Let the following assertions be universal over eligible independent monic septic boxes.

**SPR:** Every such box admits one stable monic strict common-SPR numerator.

**DUAL:** No such box has a finite actual-member, positive-frequency, positive-weight aggregate with all eight raw coordinates strictly negative.

**ROOT:** For every such box with nondegenerate odd uncertainty, the frozen S1 condition B holds: **one** common triple in its actual permitted root intervals satisfies every actual-endpoint R4 condition and both orientations of every R5 condition.

### Theorem 4

Using the frozen S1 equivalence between its conditions A and B,

\[
\boxed{\mathrm{SPR}\iff\mathrm{DUAL}\iff\mathrm{ROOT}.}
\]

For the implication from ROOT to SPR, it is sufficient to know ROOT for boxes whose constant and linear coefficient intervals both have positive width.

### Proof

**SPR implies DUAL.** A stable monic real numerator has strictly positive coefficients. Its dot product with a strictly negative eight-coordinate aggregate would therefore be negative. But that dot product is a positive-weight sum of strictly positive physical pairings, a contradiction.

**DUAL implies SPR.** Start with an arbitrary original box \(K\). Choose an eligible two-coordinate buffer \(L\) by Lemma 2. Apply DUAL to \(L\), and obtain a weak nonnegative numerator from Lemma 3. Theorem 1 then constructs one strict stable numerator for the whole original \(K\).

**ROOT implies SPR.** Choose the same eligible buffer \(L\). Its odd uncertainty is nondegenerate because the linear coefficient was widened. Frozen S1 gives absence of a strict-negative certificate on \(L\) from ROOT. Lemma 3 and Theorem 1 finish the construction.

**SPR implies ROOT.** SPR excludes strict-negative certificates on every eligible box, and frozen S1 gives condition B on every box to which its three-root equivalence applies. ∎

### Exact qualification

This does **not** prove the per-box implication

\[
B(K)\Longrightarrow \text{strict common-SPR on that same }K.
\]

The proved implication is

\[
B(L)\Longrightarrow \text{strict common-SPR on the original }K
\]

when \(L\) contains the stated positive two-coordinate buffer of \(K\).

That distinction is essential. Nevertheless, because every original eligible box has such an eligible enlargement, the **universal** common-three-root theorem would settle the **universal original strict synthesis problem**, with no additional weak-to-strict conjecture left over.

---

## 6. Actual dual consumers: all R4 cases and both R5 orientations

The constructed \(Q\) is fixed once for the whole original \(K\). Let \(c_j>0\) be its coefficients.

For any nonempty finite positive-weight family of actual members at positive squared frequencies,

\[
\sum_i w_i P_{Q,a_i}(t_i)
\ge
\eta\sum_i w_i(1+t_i)^7>0.
\tag{11}
\]

Suppose its four signed odd-coordinate sums are nonpositive:

\[
M_{\rm odd}
=
\sum_iw_i
(t_iO_i,-t_i^2O_i,t_i^3O_i,-t_i^4O_i)
\le0
\]

coordinatewise. Their pairing with the positive odd coefficients of \(Q\) is nonpositive. Therefore

\[
\sum_iw_i F_Q(t_i)E_i(t_i)
=
\sum_iw_iP_{Q,a_i}(t_i)
-
(c_1,c_3,c_5,c_7)\mathbin{\cdot}M_{\rm odd}
>0.
\tag{12}
\]

Thus the same numerator simultaneously gives strict even pairing for:

- every actual R4 omitted-moment case;
- both actual R5 orientations;
- zero-odd singletons;
- same-frequency opposite-odd cancellations;
- arbitrary positive combinations of these configurations.

No odd value is divided by. No sign orientation is discarded. No new numerator is selected for an individual ray. This argument uses the physical pairing itself, not a weaker surrogate moment condition.

---

## 7. Rational finite-counterexample normal form

A further consequence identifies a complete finite search space **if the universal synthesis statement is false**. It is not an actual counterexample.

### Corollary 5

If some eligible independent septic box lacks a strict common-SPR numerator, then there exists an eligible independent box with:

- rational endpoints and all seven interval widths positive;
- at most eight positive actual-corner atoms;
- positive rational squared frequencies;
- positive rational weights;
- an aggregate raw row strictly negative in all eight coordinates.

### Proof

Let \(K\) lack a strict common numerator, and choose an eligible buffer \(L\).

If \(L\) had no strict-negative certificate, Lemma 3 and Theorem 1 would produce a strict common numerator for \(K\), a contradiction. Hence \(L\) has a finite strict-negative certificate.

At each fixed frequency the raw row is affine in the seven uncertain coefficients. Replace each actual member by its convex decomposition into actual coefficient corners of \(L\). This preserves the aggregate exactly.

Conic Carathéodory reduction in \(\mathbb R^8\) preserves that aggregate using at most eight corner atoms. Explicitly, when more than eight vectors have positive weights, use a nonzero linear dependence and decrease the weights along it until one becomes zero; iterate.

Finally, strict negativity is an open condition, as is robust Hurwitz stability of a compact box. Approximate the box endpoints by rational endpoints with all widths positive, and approximate the finitely many positive squared frequencies and weights by positive rationals. Preserve each corner’s endpoint labels during the approximation. All eight strict inequalities and all-member Hurwitz stability persist for sufficiently close approximations. ∎

**Limits of this corollary:** no rational box, numerical values or stability certificate has been produced here. The statement establishes a normal form for a possible disproof, not evidence that one exists. It does not guarantee exactly six frequencies, nor that sparsification retains a prescribed frequency set.

---

## 8. Precisely unpaid original step

The unresolved mathematical step remains:

> For every actual all-Hurwitz independent septic box with nondegenerate odd uncertainty, prove the existence of one common triple in the frozen actual root intervals that satisfies every actual-endpoint R4 pairing and both R5 orientations—or supply an actual eligible strict-negative counterexample.

This candidate has **not**:

- proved that common-triple statement;
- derived a new universal inequality from the actual three-band coefficient constraints;
- replaced the common-triple existential quantifier by separate choices for different rays;
- established common intersection from slice-wise synthesis;
- supplied an actual strict-negative aggregate;
- claimed that the buffered box’s certificate, if any, is a certificate inside the unexpanded original box.

What has been supplied is a written proof that, at the universal level, solving the frozen weak common-triple problem suffices for the original **strict, stable, whole-box** synthesis target. The endpoint and imaginary-zero issues in that implication have been explicitly paid.

---

## 9. Inputs, chronology, and execution boundary

1. Read the required memory summary and relevant acceptance/review skills.
2. Read the complete frozen manifest, all thirteen controls in their declared order through their endings, the complete freeze receipt, and the complete parent metadata supply and dispatch receipt. Required control reads used raw chunks of at most twenty LF.
3. Sent the required **direct pre-body ACK to `agent://Main` before opening the literal packet**.
4. Read the complete literal packet, LF 1–87, in ordered raw chunks of at most twenty LF, including both source endings.
5. Only afterward began mathematical work and public-source searching.
6. Public exposure included the opening 300 displayed lines of [Xu et al., *Robust Strictly Positive Real Synthesis for Sixth-Order Interval Polynomial Families*, arXiv:2609.26541v1](https://arxiv.org/html/2609.26541v1). That partial reading was not a complete paper audit. No theorem, formalization claim or seventh-order conclusion from that paper is used as a premise in the proofs above.
7. No scientific calculation, solver, code, test, build, lint, external-model CLI or background scientific process was run. Accordingly, there are no executable results or calculation source files to report.
8. No repository file was written. This complete body is returned for Main materialization under the read-only role boundary.
9. All named held episodes and all their consumers remained NONINPUT. Links to excluded or unneeded artifacts were not followed. No clean-cognition or independent-provenance certificate is asserted.

**Frozen bindings, supplied by parent metadata rather than recomputed by this child:**

- Manifest SHA256: `54168f7bd64884f28eff78b08787ec18e0184e408803cd482e94a9575e4562cb`
- Receipt SHA256: `ab4195a0b0a57b781283aa5af8eebdccbdabc02ecb6b56df62a495f04caf3305`
- Literal packet SHA256: `30c43bc8975aa23ea4ccf2554f9ee7a83016db4c555d452e20e7845f2f64e227`
- S1 SHA256: `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`
- S2 SHA256: `967da36f40018605296da178ac5493758603cf09bfea54b240342e5fa7c2af48`

**Acceptance boundary:** this is an unreviewed author candidate for the strictification and universal-equivalence interface. It is not global septic synthesis, an actual counterexample, a novelty determination, independent-family verification, human verification or formal/kernel acceptance.