# F493 — Strict common-SPR synthesis for every fixed-parity Hurwitz septic box, with full-dimensional thickening

**Intended artifact:** `author-candidate-v1.md`  
**Status:** AUTHOR WRITTEN CANDIDATE; not independently checked or adopted.

## 1. Scope, provenance, and execution status

This return proves:

1. Every nonempty compact convex family of monic strictly Hurwitz real septics having **either parity fixed** admits one **strict** common-SPR numerator.
2. Every such family has a positive, quantitatively specified **independent seven-coefficient thickening** with the same strict common numerator.
3. A separate explicit, full-dimensional family has a closed-form common numerator and an exact all-member, all-frequency lower bound.

These are sufficient classes of the original problem, not a proof for every eligible septic box and not an eight-strict-negative dual certificate.

### Read and experiment chronology

- Read the complete frozen manifest, receipt, parent metadata supply, and all ten permission/status controls before sending the direct pre-body acknowledgement.
- After that acknowledgement, read the literal packet in ordered raw ranges of at most 20 LF, through its ending at LF143.
- The scientific inputs were the packet’s complete S1–S3 dispositions. Held scientific payloads and their consumers were not requested.
- The constructions below were developed as fresh written mathematics after those reads. No clean-cognition or independent-provenance certificate is asserted.
- The manifest, receipt, packet hashes, byte counts, LF counts, and clock are **parent-supplied observations**, not child-native executions.

Bindings supplied by the parent:

- Manifest: `afdad55d4eea4fc191eb656c9413681929999945fb429eb66099cbe50580b394`
- Receipt: `794095cab8c745bc810369e773dd91faeaea2e85a816dcb5ff3304ecc0d9f2a1`
- Packet: `10836cc12aab8e58544b450e1674e81f0ca64574af1df8eeb41f393106f6bddd`

**Scientific executable status: NOTRUN.** No interpreter, solver, package installation, build, test, or scientific program was run. No program output is claimed. The rational identities below are displayed written calculations. The active read-only runtime also prevented repository materialization; this is the complete body for the parent to save.

---

## 2. Original target and notation

Let \(K\) be a nonempty compact independent coefficient box of monic real septics

\[
a(s)=s^7+\sum_{j=0}^{6}a_js^j,
\]

whose **every actual member** is strictly Hurwitz. Put

\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,
\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

Thus, for \(t=\omega^2\),

\[
a(i\omega)=E_a(t)+i\omega O_a(t).
\]

For a monic numerator \(q\), write similarly

\[
q(i\omega)=F(t)+i\omega G(t).
\]

The relevant real product is exactly

\[
P_{q,a}(t)
=\operatorname{Re}\!\left(q(i\omega)\overline{a(i\omega)}\right)
=F(t)E_a(t)+tG(t)O_a(t).
\]

Consequently,

\[
\operatorname{Re}\frac{q(i\omega)}{a(i\omega)}
=\frac{P_{q,a}(\omega^2)}{|a(i\omega)|^2}.
\]

The original universal target asks for

\[
\forall K\text{ eligible}\quad
\exists q\quad
\forall a\in K\quad
\forall \omega\in\mathbb R:
\operatorname{Re}\frac{q(i\omega)}{a(i\omega)}>0,
\]

with the appropriate strict stability and high-frequency conditions.

The results below retain the existential common-\(q\) quantifier before **all members and all frequencies**. They establish it for specified entire classes, not arbitrary \(K\).

---

## 3. Two elementary tools

### 3.1 No-crossing homotopy

Consider a continuous family of monic degree-seven real polynomials on a compact parameter interval. Suppose:

- its coefficients remain bounded;
- no member has a zero on the imaginary axis;
- one member is strictly Hurwitz.

Then every member is strictly Hurwitz.

Indeed, bounded coefficients give a common finite root bound. Roots therefore cannot escape through infinity. The number of roots in each open half-plane cannot change without an imaginary-axis zero.

We will use this for actual coefficient segments, not infer all-member stability merely from corner stability.

Also, every monic strictly Hurwitz real polynomial has strictly positive coefficients. Factor it into factors \(s+\alpha\), \(\alpha>0\), and real quadratic factors

\[
s^2+2\alpha s+\alpha^2+\beta^2,
\qquad \alpha>0.
\]

Each factor has strictly positive coefficients, and so does their product.

### 3.2 Compact small-parameter lemma

Let \(X\) be compact and \(A,B:X\to\mathbb R\) continuous. Assume

\[
B\ge0,
\qquad
A(x)>0\quad\text{whenever }B(x)=0.
\]

Then, for all sufficiently small \(\delta>0\),

\[
B+\delta A>0\quad\text{on }X.
\]

**Proof.** Let \(N=\{x:A(x)\le0\}\). If \(N\) is empty, the conclusion is immediate. Otherwise \(N\) is compact and disjoint from the zero set of \(B\), so

\[
b=\min_N B>0.
\]

Let \(M=\max_X|A|\). If \(M=0\), then \(B>0\) and again the conclusion is immediate. Otherwise choose

\[
0<\delta\le \min\left(1,\frac{b}{2M}\right).
\]

On \(N\), \(B+\delta A\ge b/2>0\). Outside \(N\), \(A>0\) and \(B\ge0\). This proves the assertion. ∎

---

## 4. Theorem 1: universal strict synthesis when either parity is fixed

### Statement

Let \(K\) be any nonempty compact convex family of monic strictly Hurwitz real septics. Independence of its coefficients is not needed for this theorem.

Choose one reference member

\[
a_*(s)=E_*(-s^2)+sO_*(-s^2).
\]

Then:

**Fixed odd parity.** If every member has \(O_a=O\), there exists \(\delta_0>0\) such that, for every \(0<\delta\le\delta_0\),

\[
q_\delta(s)=\delta E_*(-s^2)+sO(-s^2)
\]

is monic, strictly Hurwitz, and satisfies

\[
P_{q_\delta,a}(t)>0
\quad\text{for every }a\in K,\ t\ge0.
\]

**Fixed even parity.** If every member has \(E_a=E\), there exists \(\delta_0>0\) such that, for every \(0<\delta\le\delta_0\),

\[
q_\delta(s)=\delta^{-1}E(-s^2)+sO_*(-s^2)
\]

has the same properties.

In either case, for each fixed permitted \(\delta\), there is a uniform margin \(m>0\) such that

\[
P_{q_\delta,a}(t)\ge m(1+t)^7
\quad\text{for every }a\in K,\ t\ge0.
\]

### 4.1 Compactifying the complete frequency axis

Put

\[
u=\frac{t}{1+t}\in[0,1),
\]

and define the polynomial transforms

\[
\widetilde E_a(u)
=(1-u)^3E_a\!\left(\frac{u}{1-u}\right),
\qquad
\widetilde O_a(u)
=(1-u)^3O_a\!\left(\frac{u}{1-u}\right).
\]

Both have degree at most three. Since every denominator is monic,

\[
\widetilde O_a(1)=-1.
\]

For any monic \(q\),

\[
\overline P_{q,a}(u)
=(1-u)^7P_{q,a}\!\left(\frac{u}{1-u}\right)
\]

extends polynomially to \([0,1]\), with the exact identity

\[
\overline P_{q,a}
=(1-u)\widetilde F\,\widetilde E_a
+u\widetilde G\,\widetilde O_a.
\]

In particular,

\[
\overline P_{q,a}(0)=q_0a_0,
\qquad
\overline P_{q,a}(1)=1.
\]

Thus this transformation includes zero frequency and infinity; it does not replace the half-axis by a finite frequency sample.

### 4.2 Fixed odd parity

For the proposed numerator,

\[
P_{q_\delta,a}(t)
=\delta E_*(t)E_a(t)+tO(t)^2.
\]

After compactification,

\[
\overline P_{q_\delta,a}(u)
=
u\widetilde O(u)^2
+\delta(1-u)\widetilde E_*(u)\widetilde E_a(u).
\]

Apply the compact small-parameter lemma on \(X=K\times[0,1]\), with

\[
B(a,u)=u\widetilde O(u)^2,
\qquad
A(a,u)=(1-u)\widetilde E_*(u)\widetilde E_a(u).
\]

Certainly \(B\ge0\).

At \(u=0\),

\[
A(a,0)=E_*(0)E_a(0)>0,
\]

because the constant coefficients of the Hurwitz members are positive.

Every other zero of \(B\) corresponds to a finite \(t>0\) with \(O(t)=0\). At such a \(t\), all actual even values \(E_a(t)\) are nonzero: otherwise an actual denominator would vanish at \(i\sqrt t\).

Moreover, \(E_*(t)\) and \(E_a(t)\) have the same sign. If they had opposite signs, convexity would provide an actual segment member with even value zero at that same \(t\), while its odd value remained zero. That would contradict strict Hurwitz stability. Therefore

\[
E_*(t)E_a(t)>0.
\]

Finally, \(u=1\) is not a zero of \(B\), since \(B(a,1)=1\).

The lemma now gives strict positivity for every member and every frequency when \(\delta>0\) is sufficiently small.

### 4.3 Fixed even parity

Here

\[
P_{q_\delta,a}(t)
=\delta^{-1}E(t)^2+tO_*(t)O_a(t).
\]

Multiplying its compactification by \(\delta\) gives

\[
\delta\overline P_{q_\delta,a}(u)
=
(1-u)\widetilde E(u)^2
+\delta u\widetilde O_*(u)\widetilde O_a(u).
\]

Use the lemma with

\[
B(a,u)=(1-u)\widetilde E(u)^2,
\qquad
A(a,u)=u\widetilde O_*(u)\widetilde O_a(u).
\]

Again \(B\ge0\).

At \(u=1\),

\[
A(a,1)=(-1)(-1)=1>0.
\]

A remaining zero of \(B\) corresponds to a finite positive root \(t\) of \(E\). It is positive because \(E(0)>0\). At such a root, every actual \(O_a(t)\) is nonzero. Convexity and strict Hurwitz stability again force all these values to have the same sign as \(O_*(t)\). Hence

\[
O_*(t)O_a(t)>0,
\]

and therefore \(A>0\) at every zero of \(B\).

The lemma gives the required strict positivity.

### 4.4 Stability of the constructed numerators

This step does not assume that the constructed numerator belongs to \(K\).

In the fixed-odd case, consider

\[
q_\lambda(s)=\lambda E_*(-s^2)+sO(-s^2),
\qquad \lambda>0.
\]

An imaginary-axis zero at nonzero frequency would require both \(E_*(t)=0\) and \(O(t)=0\), contradicting stability of \(a_*\). At zero frequency,

\[
q_\lambda(0)=\lambda E_*(0)>0.
\]

The polynomial remains monic of degree seven. On the compact parameter interval joining \(1\) to any chosen \(\delta>0\), the no-crossing homotopy proves its stability.

For fixed even parity, use instead

\[
q_\lambda(s)=\lambda^{-1}E(-s^2)+sO_*(-s^2),
\]

and the same argument. The interval joining \(1\) to a fixed positive \(\delta\) stays away from zero, so its coefficients are bounded.

Both constructions also have strictly positive coefficients: they simply rescale one parity of the positive coefficient vector of \(a_*\).

### 4.5 Uniform margin and strict SPR

For a fixed permitted \(\delta\), the function \(\overline P_{q_\delta,a}(u)\) is strictly positive on the compact set \(K\times[0,1]\). Therefore

\[
m=\min_{a\in K,\ u\in[0,1]}
\overline P_{q_\delta,a}(u)>0.
\]

This is precisely

\[
P_{q_\delta,a}(t)\ge m(1+t)^7.
\]

Every denominator is stable, the numerator is stable, and

\[
\operatorname{Re}\frac{q_\delta(i\omega)}{a(i\omega)}>0
\]

at every real frequency. Both polynomials are monic of degree seven, so the ratio tends to \(1\) at infinity.

This proves Theorem 1. ∎

### Relation to the frozen frontier

S2 supplied a no-strict-dual statement for fixed parity but explicitly did not claim strict common-SPR synthesis. Theorem 1 supplies that strict synthesis for the **entire fixed-parity class**, not just a selected example.

It does not strictify an arbitrary weak separator from a box in which both parities vary.

---

## 5. Exact rational construction protocol

This section describes a terminating exact construction for rational eligible fixed-parity boxes. It was **not executed**.

Choose the rational center member as \(a_*\). For successive values

\[
\delta=1,\frac12,\frac14,\ldots,
\]

form the numerator from Theorem 1.

For each actual varying-parity corner \(v\), form the exact rational polynomial

\[
p_v(u)
=(1-u)^7P_{q_\delta,v}\!\left(\frac{u}{1-u}\right).
\]

There are at most:

- \(2^4=16\) such corners when the odd parity is fixed;
- \(2^3=8\) when the even parity is fixed.

Test \(p_v>0\) on the **entire** interval \([0,1]\), using exact endpoint signs and an exact Sturm count of its roots in \((0,1)\). Endpoint positivity plus zero interior roots certifies strict positivity. A tangential zero must be counted and rejected; it is not acceptable to test only sign-changing roots.

For any fixed \(u\), the pairing is affine in the denominator coefficients. Therefore positivity at every corner, proved over the entire interval, implies positivity for every actual member.

Theorem 1 guarantees that this dyadic search eventually succeeds under its hypotheses. After fixing \(q\), search for a positive dyadic \(\eta\) such that every

\[
p_v-\eta
\]

is strictly positive on \([0,1]\). This also terminates, and gives

\[
P_{q,a}(t)\ge\eta(1+t)^7
\quad\text{for every }a\in K,\ t\ge0.
\]

These are exact polynomial certificates, not finite corner-frequency samples.

There is **no claimed runtime bound** for arbitrary rational input sizes. No source program or execution receipt is supplied, because no program was executed. The existence proof above does not depend on an unrun numerical result.

---

## 6. Theorem 2: quantitative independent seven-coefficient thickening

### Statement

Suppose a compact convex monic septic family \(K\) has a monic strictly Hurwitz numerator

\[
q(s)=\sum_{j=0}^{7}q_js^j,\qquad q_7=1,
\]

and a certified margin

\[
P_{q,a}(t)\ge\eta(1+t)^7
\quad\text{for all }a\in K,\ t\ge0,
\]

where \(\eta>0\).

Define

\[
Q=\sum_{j=0}^{7}|q_j|,
\qquad
\rho=\frac{\eta}{14Q}.
\]

Then every polynomial

\[
b(s)=a(s)+\sum_{j=0}^{6}d_js^j,
\qquad
a\in K,\quad |d_j|\le\rho,
\]

is strictly Hurwitz and satisfies

\[
P_{q,b}(t)\ge\frac{\eta}{2}(1+t)^7
\quad(t\ge0).
\]

Thus the same \(q\) is a strict common-SPR numerator for this entire thickened family.

### Proof

Let \(x=|\omega|\) and \(t=x^2\). Since \(j\le6\),

\[
\left|\sum_{j=0}^{6}d_j(i\omega)^j\right|
\le \rho\sum_{j=0}^{6}x^j
\le7\rho(1+t)^3.
\]

Also,

\[
|q(i\omega)|
\le Q(1+t)^{7/2}.
\]

Hence, writing \(d=b-a\),

\[
\begin{aligned}
|P_{q,b}(t)-P_{q,a}(t)|
&=\left|\operatorname{Re}\left(q(i\omega)\overline{d(i\omega)}\right)\right|\\
&\le7\rho Q(1+t)^{13/2}\\
&\le7\rho Q(1+t)^7\\
&=\frac{\eta}{2}(1+t)^7.
\end{aligned}
\]

This proves the stated pairing bound.

For stability, fix an actual representation \(b=a+d\) and follow the monic coefficient segment

\[
b_\tau=a+\tau d,\qquad 0\le\tau\le1.
\]

The same estimate applies throughout this segment, so

\[
P_{q,b_\tau}(t)>0
\]

at every \(t\ge0\). Therefore no segment member has an imaginary-axis zero. The coefficients are bounded, and \(b_0=a\) is Hurwitz. The no-crossing homotopy proves that \(b\) is Hurwitz.

The numerator is unchanged and stable, and both numerator and denominator are monic of degree seven. This proves the strict common-SPR conclusion. ∎

### Consequence for actual independent boxes

If

\[
K=\prod_{j=0}^{6}[\ell_j,u_j]
\]

in coefficient coordinates, its thickening is exactly the independent box

\[
K_\rho=\prod_{j=0}^{6}[\ell_j-\rho,u_j+\rho].
\]

Every coordinate is independently variable. In particular, applying Theorem 2 to a fixed-parity box from Theorem 1 produces a box in which **all seven nonleading intervals have positive width**.

The core need not be a single polynomial or a small ball: its varying parity can have any widths compatible with the hypotheses. Only the additional thickening is bounded by the certified margin.

---

## 7. Theorem 3: an explicit full-dimensional family outside S1

The preceding theorems have general hypotheses. The following family supplies a completely explicit all-member example and a parameterized class.

Let

\[
\beta>0,\qquad 0<\varepsilon<\frac56.
\]

Independently choose

\[
a_j\in
\beta^{7-j}
\left[
\binom7j-\varepsilon,\,
\binom7j+\varepsilon
\right],
\qquad j=0,\ldots,6.
\]

Then every actual polynomial in this box is strictly Hurwitz, and the single numerator

\[
q_\beta(s)=(s+\beta)^7
\]

satisfies, for all members and all \(t\ge0\),

\[
P_{q_\beta,a}(t)
\ge
\left(1-\frac65\varepsilon\right)(\beta^2+t)^7>0.
\]

### Proof

Write

\[
a=q_\beta+d,\qquad
d_j=\beta^{7-j}\xi_j,\qquad |\xi_j|\le\varepsilon.
\]

Put \(x=|\omega|/\beta\). Then

\[
|d(i\omega)|
\le\varepsilon\beta^7\sum_{j=0}^{6}x^j.
\]

Weighted Cauchy–Schwarz gives

\[
\left(\sum_{j=0}^{6}x^j\right)^2
\le
\left(\sum_{j=0}^{6}\frac1{\binom7j}\right)
\left(\sum_{j=0}^{6}\binom7j x^{2j}\right).
\]

The exact scalar sum is

\[
\sum_{j=0}^{6}\frac1{\binom7j}
=
1+\frac27+\frac2{21}+\frac2{35}
=\frac{151}{105}.
\]

Moreover,

\[
\frac{36}{25}-\frac{151}{105}
=\frac1{525}>0,
\]

and

\[
\sum_{j=0}^{6}\binom7j x^{2j}\le(1+x^2)^7.
\]

Consequently,

\[
\sum_{j=0}^{6}x^j
\le\frac65(1+x^2)^{7/2},
\]

so

\[
|d(i\omega)|
\le\frac65\varepsilon\,|q_\beta(i\omega)|.
\]

It follows that

\[
\begin{aligned}
P_{q_\beta,a}(t)
&=|q_\beta(i\omega)|^2+
\operatorname{Re}\left(q_\beta(i\omega)\overline{d(i\omega)}\right)\\
&\ge
\left(1-\frac65\varepsilon\right)|q_\beta(i\omega)|^2\\
&=
\left(1-\frac65\varepsilon\right)(\beta^2+t)^7.
\end{aligned}
\]

For every coefficient segment \(q_\beta+\tau d\), the same strict relative-error bound excludes imaginary-axis zeros. The segment is monic with bounded coefficients, and \(q_\beta\) has all seven roots at \(-\beta\). The no-crossing argument therefore proves stability of every actual member.

This is an exact robust-polynomial argument for the complete independent box. It does not infer member stability from sampled corners or frequencies. ∎

### Literal rational instance

Take \(\beta=1\), \(\varepsilon=3/4\). The box is

| Coefficient | Independent interval |
|---|---|
| \(a_0\) | \([1/4,7/4]\) |
| \(a_1\) | \([25/4,31/4]\) |
| \(a_2\) | \([81/4,87/4]\) |
| \(a_3\) | \([137/4,143/4]\) |
| \(a_4\) | \([137/4,143/4]\) |
| \(a_5\) | \([81/4,87/4]\) |
| \(a_6\) | \([25/4,31/4]\) |

The common numerator is

\[
q(s)=s^7+7s^6+21s^5+35s^4+35s^3+21s^2+7s+1,
\]

and the exact uniform bound is

\[
P_{q,a}(t)\ge\frac1{10}(1+t)^7.
\]

All seven intervals have positive width. This box is outside S1’s stated family: its \(a_6\) interval is \([25/4,31/4]\), whereas S1’s is confined near \(1\).

This instance illustrates a proved parameterized class. It is not used as evidence for universal synthesis.

---

## 8. Actual dual and ray consumers

The consumer argument applies to every box proved above.

For an actual member at \(t>0\), the raw row is

\[
r_a(t)=
(E_a,\ tO_a,\ -tE_a,\ -t^2O_a,\ t^2E_a,\ t^3O_a,\ -t^3E_a,\ -t^4O_a).
\]

Let

\[
c=(q_0,q_1,\ldots,q_7).
\]

Every coefficient of the constructed stable numerator is strictly positive, and the exact identity is

\[
c\cdot r_a(t)=P_{q,a}(t)>0.
\]

### 8.1 Exclusion of an all-eight-strict-negative aggregate

For any nonzero finite positive-weight family of actual atoms,

\[
c\cdot\sum_iw_ir_{a_i}(t_i)
=\sum_iw_iP_{q,a_i}(t_i)>0.
\]

If all eight aggregate coordinates were strictly negative, their dot product with \(c>0\) would instead be strictly negative. Thus no such certificate exists for these boxes.

This excludes **every** candidate numerator obstruction of the specified strict-negative form, not merely a chosen ray.

### 8.2 All R4 choices, both R5 orientations, and degeneracies

Suppose the four odd aggregate coordinates satisfy

\[
R_1,R_3,R_5,R_7\le0.
\]

Since the odd numerator coefficients are positive,

\[
\sum_iw_it_iG(t_i)O_i(t_i)
=q_1R_1+q_3R_3+q_5R_5+q_7R_7\le0.
\]

Therefore

\[
\sum_iw_iF(t_i)E_i(t_i)
=
\sum_iw_iP_i-
\sum_iw_it_iG(t_i)O_i(t_i)
>0.
\]

This holds for **every** positive-weight actual family satisfying the four odd inequalities. Consequently it covers:

- every R4 omitted-moment choice;
- both positive-weight R5 orientations;
- zero-odd singletons;
- same-frequency opposite-odd cancellations;
- arbitrary combinations of these configurations.

It requires no division by an odd value, so zero odd values cause no exception.

For an independent box, replacing each even value by the actual pointwise minimizing endpoint for \(F\), and each odd value by an actual endpoint, still yields actual parity combinations. The same strict pointwise inequality applies. The minimizing even endpoint need not be one fixed polynomial across different nodes.

At \(t=0\),

\[
P_{q,a}(0)=q_0a_0>0.
\]

At the compactified infinity endpoint,

\[
\overline P_{q,a}(1)=1.
\]

No endpoint, orientation, or cancellation is discarded.

The argument supplies a single common \(F,G\) before these universal consumer quantifiers. It does not infer common-test existence from separate tests chosen for individual rays.

---

## 9. What remains unproved

### Completed mathematical scope

The written proofs establish:

- strict synthesis for every eligible compact convex fixed-parity septic family;
- a positive independent seven-coordinate thickening of every such family;
- an explicit parameterized full-dimensional sufficient class outside S1;
- absence of strict-negative aggregates and strict positivity on all actual odd-moment-cone consumers for those classes.

### Exact remaining original-target gap

For an arbitrary eligible box in which both parities vary, fixing one parity at a selected actual value gives a fixed-parity subbox and hence a common numerator for that subbox. Theorem 2 extends it through some positive neighborhood.

What is **not proved** is that one such numerator and its certified neighborhood cover the original box’s entire variation in the other parity.

Equivalently, obtaining different valid numerators for different fixed-parity slices does not provide the required one numerator for their union. No gluing or common-intersection theorem is established here.

In S2’s language, this return does not prove the existence of one common root triple satisfying **all** actual R4 and both R5 families for an arbitrary eligible box. Nor does it establish arbitrary weak-separator strictification. S3’s boundary obstruction is not evaded or promoted into a universal counterexample.

No eligible box with an all-eight-strict-negative certificate is supplied.

### Acceptance and source limitations

- No independent written reconstruction or finite replay of this candidate has occurred.
- No scientific execution or runtime result is claimed.
- No public primary source was newly consulted for these proofs.
- Novelty, priority, worldwide status, original-source correspondence, human review, independent-family review, and formal/kernel verification are not established.
- Parent disposition and any independent verification remain unpaid.
- Historical held episodes remain NONINPUT; this return does not rehabilitate them.

**Final disposition:** a completed author-level sufficient-class result and strictification result, with the arbitrary all-Hurwitz septic-box synthesis problem still unresolved by this return.