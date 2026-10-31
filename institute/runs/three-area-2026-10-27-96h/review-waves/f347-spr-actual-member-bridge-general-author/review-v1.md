# author-candidate-v1.md

## Status and scientific outcome

**GENERAL AUTHOR CANDIDATE — UNREVIEWED, same-harness.** No independent-family, human, formal/kernel, novelty or parent-acceptance claim is made.

This candidate supplies a reduction at the **actual independent coefficient-box level**, rather than another normalized W1 vertex inequality:

1. An exact characterization of strict-negative certificate obstruction by a three-root even test polynomial and explicitly classified **actual-corner odd-moment rays**.
2. The ray classification includes the previously dangerous interfaces: **zero odd values, same-frequency cancellations, four-node rays, and both orientations of five-node annihilators**.
3. A primal sparsification consequence: any hypothetical six-frequency strict-negative certificate has a replacement on the **same six frequencies**, preserving its entire aggregate vector, with at least **four actual members equal to actual parity-envelope corner polynomials**.
4. An exact, physically realizable all-Hurwitz example falsifies a specified **W1-only moment reduction**. Its complete aggregate sign check explicitly shows that it is **not** a strict-negative certificate.

The unrestricted synthesis/certificate decision remains open. The principal advance here is a quantified actual-member reduction with its missing obligations exposed.

The attempted wave-local process-file write was refused by the available write transport. No filesystem bypass was used. This is the complete candidate body for parent materialization.

---

## 1. Original model and pairing

Let

\[
K=\left\{
a(s)=s^7+\sum_{j=0}^{6}a_js^j:
\ell_j\le a_j\le u_j
\right\}
\]

be a nonempty compact independent coefficient box, every actual member of which is strictly Hurwitz. Degenerate coefficient intervals are allowed.

Write, for \(t=\omega^2>0\),

\[
a(i\omega)=E_a(t)+i\omega O_a(t),
\]

where

\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,
\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

For a numerator \(b(s)=\sum_{j=0}^{7}b_js^j\), put

\[
B_e(t)=b_0-b_2t+b_4t^2-b_6t^3,
\qquad
B_o(t)=b_1-b_3t+b_5t^2-b_7t^3.
\]

Direct multiplication gives the raw pairing

\[
\operatorname{Re}\!\left(b(i\omega)\overline{a(i\omega)}\right)
=B_e(t)E_a(t)+tB_o(t)O_a(t).
\]

Thus the raw eight-coordinate row is

\[
r(a,t)=
\bigl(
E_a,\ tO_a,\ -tE_a,\ -t^2O_a,\
t^2E_a,\ t^3O_a,\ -t^3E_a,\ -t^4O_a
\bigr).
\]

A strict-negative certificate means

\[
\sum_i\mu_i r(a_i,t_i)\in(-\infty,0)^8,
\qquad
\mu_i>0,\quad t_i>0,\quad a_i\in K.
\]

Equivalently, both four-coordinate moment vectors are strictly negative:

\[
M^e_r=\sum_i\mu_i(-1)^rt_i^rE_{a_i}(t_i)<0,
\]

\[
M^o_r=\sum_i\mu_i(-1)^rt_i^{r+1}O_{a_i}(t_i)<0,
\qquad r=0,1,2,3.
\]

Endpoint atoms can be removed from a strict certificate: their raw compactified contributions are nonnegative multiples of the first or last coordinate vector. Removing them preserves strict negativity.

### Named imports

The box-wide Hermite–Biehler/interlacing facts below are the adopted interface in **S1 and the corrected S2**, not the defective historical manuscript. In particular:

- all actual coefficients are positive;
- the parity-envelope combinations are actual box members;
- their odd-root bands and actual even-root placements have the corrected scope stated in S2;
- the at-most-five-positive-frequency impossibility is imported **only** in Section 6.

Other general mathematical imports are finite-dimensional convex separation and the extreme-ray decomposition of a pointed polyhedral cone. The ray formulas and classifications needed here are proved below. No external scientific source was used.

---

## 2. Four actual corner polynomials, not a fictitious root box

Define the actual parity envelopes

\[
E_-(t)=\ell_0-u_2t+\ell_4t^2-u_6t^3,
\]

\[
E_+(t)=u_0-\ell_2t+u_4t^2-\ell_6t^3,
\]

and

\[
O_-(t)=\ell_1-u_3t+\ell_5t^2-t^3,
\]

\[
O_+(t)=u_1-\ell_3t+u_5t^2-t^3.
\]

For each \(\sigma,\tau\in\{-,+\}\), the polynomial with even parity \(E_\sigma\) and odd parity \(O_\tau\) is an **actual member** \(a^{\sigma\tau}\in K\). Independence of the coefficient intervals is essential here.

At a fixed positive \(t\), the image of \(K\) under

\[
a\longmapsto(E_a(t),O_a(t))
\]

is exactly

\[
[E_-(t),E_+(t)]\times[O_-(t),O_+(t)].
\]

Consequently every raw row \(r(a,t)\) is a convex combination of the four rows \(r(a^{\sigma\tau},t)\).

This is a statement about the **row image at one frequency**. It does **not** say that the entire coefficient box is the convex hull of four polynomials. The convex coefficients may depend on \(t\), which is legitimate because the certificate allows arbitrary actual members at its different atoms.

Suppose at least one odd coefficient interval has positive width. Then

\[
O_+(t)-O_-(t)
=(u_1-\ell_1)+(u_3-\ell_3)t+(u_5-\ell_5)t^2>0
\]

for every \(t>0\).

Using the adopted actual-box interlacing result, label the roots by

\[
O_-=(a-t)(d-t)(e-t),\qquad
O_+=(b-t)(c-t)(f-t),
\]

with

\[
0<a<b<c<d<e<f.
\]

Every actual even polynomial has one root in each of

\[
(0,a),\qquad(b,c),\qquad(d,e).
\]

In particular every actual \(E\) is strictly negative on \([a,b]\), strictly positive on \([c,d]\), and strictly negative on \([e,f]\).

No converse realization claim is being made: arbitrary ordered markers do not define an eligible box.

---

## 3. Complete finite-grid odd-moment ray classification

Fix finitely many distinct positive frequencies \(T\). At each \(t\in T\), retain the two actual odd endpoints \(O_-(t),O_+(t)\). Define

\[
\mathcal C_T=
\left\{
w\ge0:
\sum_{t\in T,\tau}w_{t,\tau}(-1)^rt^{r+1}O_\tau(t)\le0,\
r=0,1,2,3
\right\}.
\]

This is a pointed polyhedral cone in its nonnegative **weight variables**.

Its extreme rays are precisely the following feasible rays.

### Z. Zero-odd singleton rays

If \(O_\tau(t)=0\), the singleton weight at that atom is a ray. All four odd moments vanish.

These cannot be removed by asserting that finite weights imply nonzero parity.

### P. Same-frequency cancellation rays

If

\[
O_-(t)<0<O_+(t),
\]

there is the ray

\[
w_{t,-}=O_+(t),\qquad
w_{t,+}=-O_-(t),
\]

with all other weights zero. Again all four odd moments vanish.

Such a ray merges into an actual member with odd value zero at that frequency. It remains relevant even when neither odd endpoint vanishes.

### R4. Four-distinct-frequency rays

Let

\[
u_1<u_2<u_3<u_4,\qquad
H_4(t)=\prod_{i=1}^{4}(t-u_i),
\]

and choose nonzero actual odd endpoint values \(O_i\) having signs

\[
(-,+,-,+).
\]

For \(k=0,1,2,3\), define

\[
q_i=e_{3-k}(u_1,\ldots,\widehat{u_i},\ldots,u_4).
\]

Then

\[
w_i=\frac{q_i}{u_iO_iH_4'(u_i)}>0.
\]

Its signed odd-moment vector is exactly \(-e_k\). The other three moments vanish.

### R5. Five-distinct-frequency annihilator rays: both orientations

Let

\[
u_1<\cdots<u_5,\qquad H_5(t)=\prod_{i=1}^{5}(t-u_i).
\]

There are two possible sign orientations:

\[
\operatorname{sgn}O_i=(+,-,+,-,+),
\]

with

\[
w_i=\frac{1}{u_iO_iH_5'(u_i)}>0,
\]

or

\[
\operatorname{sgn}O_i=(-,+,-,+,-),
\]

with

\[
w_i=-\frac{1}{u_iO_iH_5'(u_i)}>0.
\]

All four odd moments vanish.

The second orientation cannot be discarded merely because the currently studied W1 normalization uses the first.

### Proof of completeness

A support containing a zero-odd atom and another positive weight is not extreme: subtract a small positive multiple of its feasible singleton ray.

If both nonzero endpoint atoms at one frequency have positive weights:

- when their odd values have the same sign, one can redistribute their weights in both directions while preserving all odd moments;
- when their signs differ, one can subtract a positive cancellation ray until one weight vanishes.

Thus, except for Z and P themselves, an extreme ray has distinct frequencies and nonzero odd values.

Let its support size be \(p\). On its positive support, the active odd-moment equations must have nullity one. There are at most four independent moment equations, so \(p\le5\).

Supports \(p\le3\) are impossible. Indeed, for any nonzero signed sequence \(z_i=w_iu_iO_i\) on at most three ordered positive nodes, choose three positive roots so that

\[
Q(t)=\prod_{j=1}^{3}(r_j-t)
\]

agrees in sign with every \(z_i\). This is possible because such a word lacks the oriented four-term subsequence \(-,+,-,+\). Its coefficients alternate with strictly positive magnitudes. Therefore

\[
\sum_i z_iQ(u_i)>0,
\]

whereas the four nonpositive signed moment constraints make that same expression nonpositive.

For \(p=4\), exactly three moments are active: all four cannot vanish on four distinct nodes. Omitting moment \(k\), Lagrange interpolation gives

\[
\sum_{i=1}^{4}\frac{q_iu_i^r}{H_4'(u_i)}
=(-1)^{3-k}\delta_{rk}.
\]

After multiplication by \((-1)^r\), the remaining signed moment is \(-1\). All \(q_i>0\), so positive weights require the R4 sign word.

For \(p=5\), all four moments are active. Their Vandermonde matrix has rank four, so

\[
w_iu_iO_i=\frac{C}{H_5'(u_i)}.
\]

Either sign of \(C\) is possible, giving exactly the two R5 orientations.

Each listed feasible ray has a one-dimensional active nullspace on its support and is extreme. The pointed polyhedral cone is generated by these rays. ∎

---

## 4. Candidate Theorem: exact actual-box reduction

For a real cubic \(F\), define the actual minimizing even envelope

\[
E_F(t)=
\begin{cases}
E_-(t),&F(t)\ge0,\\
E_+(t),&F(t)<0.
\end{cases}
\]

At \(F(t)=0\), the choice is immaterial to the pairing.

For an R4 ray define

\[
\mathcal R_{4,k}(F)=
\sum_{i=1}^{4}
\frac{
e_{3-k}(\widehat u_i)\,E_F(u_i)F(u_i)
}{
u_iO_iH_4'(u_i)
}.
\]

For an R5 ray, write \(\varepsilon=+1\) for the positive-first orientation and \(\varepsilon=-1\) for the negative-first orientation, and define

\[
\mathcal R_{5,\varepsilon}(F)=
\varepsilon\sum_{i=1}^{5}
\frac{E_F(u_i)F(u_i)}
{u_iO_iH_5'(u_i)}.
\]

All odd values in these formulas are actual endpoint values, and every displayed weight is positive.

### Theorem

Suppose \(K\) is an eligible monic septic box and at least one odd coefficient interval has positive width. The following are equivalent.

**A.** There is no positive finite actual-member certificate with all eight aggregate coordinates strictly negative.

**B.** There exist

\[
x\in[0,a],\qquad y\in[b,c],\qquad z\in[d,e]
\]

such that, for

\[
F(t)=(x-t)(y-t)(z-t),
\]

both of the following hold:

1. \(\mathcal R_{4,k}(F)\ge0\) for every R4 configuration of positive distinct nodes and actual odd endpoint choices, and every \(k=0,1,2,3\);
2. \(\mathcal R_{5,\varepsilon}(F)\ge0\) for every R5 configuration, **in both orientations**.

Thus the full actual-box obstruction question reduces exactly to a common three-root even test and four-/five-node actual-corner inequalities. It does not reduce to the presently studied W1 table alone.

### Proof: A implies B

#### 4.1 A nonnegative polynomial separator exists

Compactify the raw row by

\[
\widehat r(a,t)=\frac{r(a,t)}{(1+t)^7}.
\]

It extends continuously to \(t=0,\infty\), with limits

\[
a_0e_0,\qquad e_7.
\]

Its image over \(K\times[0,\infty]\) is compact, and its convex hull is compact in \(\mathbb R^8\).

Under A, that convex hull is disjoint from the open strictly negative orthant. Otherwise its finite convex representation would give a strict certificate; endpoint contributions could be removed as explained in Section 1.

Finite-dimensional separation therefore gives a nonzero vector

\[
q=(q_0,\ldots,q_7)\ge0
\]

such that

\[
q\cdot r(a,t)\ge0
\]

for every actual member and every positive finite \(t\). Nonnegativity of \(q\) follows because a negative component would make its supremum over the negative orthant infinite.

Write its even and odd test polynomials as

\[
F(t)=q_0-q_2t+q_4t^2-q_6t^3,
\]

\[
G(t)=q_1-q_3t+q_5t^2-q_7t^3.
\]

Then

\[
F(t)E_a(t)+tG(t)O_a(t)\ge0.
\]

#### 4.2 The even part is not zero

Choose four distinct nodes in the first odd band \((a,b)\), and select odd endpoints with signs \(-,+,-,+\). For each \(k\), the R4 formula produces a positive actual-corner weight vector with signed odd moments \(-e_k\). Summing the four vectors makes all four odd moments strictly negative.

Consequently a nonzero separator supported only on odd coefficients is impossible. Its pairing with that positive combination would be negative.

Hence \(F\ne0\).

For any finite actual-member weighted family with nonpositive odd moments, the separator gives

\[
\sum_iw_iE_{a_i}(t_i)F(t_i)
\ge
-\sum_{r=0}^{3}q_{2r+1}M^o_r
\ge0. \tag{1}
\]

#### 4.3 Actual zero-odd cancellations force the three-root box

At every interior point of an odd band, the actual endpoints have opposite signs. Use a P cancellation with the same arbitrary actual even polynomial at its two atoms. Equation (1) then forces

\[
E(t)F(t)\ge0.
\]

The actual even signs therefore imply

\[
F\le0\ \text{on }[a,b],\qquad
F\ge0\ \text{on }[c,d],\qquad
F\le0\ \text{on }[e,f]. \tag{2}
\]

These conclusions include band endpoints by continuity.

Also \(F(0)=q_0\ge0\), and \(F\) has degree at most three. Since \(F\ne0\), its sign on each nonempty band interior is strict except at isolated roots.

The three required sign transitions force three distinct roots:

- one in \([0,a]\), allowing the root \(0\) when \(F(0)=0\);
- one in \([b,c]\);
- one in \([d,e]\).

There is no degree available for another root. Thus

\[
F(t)=\kappa(x-t)(y-t)(z-t),
\qquad \kappa>0,
\]

with exactly the asserted root placements. Divide by \(\kappa\).

#### 4.4 All R4 and both R5 inequalities follow

At each ray node choose the actual even endpoint \(E_F\) and the specified actual odd endpoint. These are actual corner members of \(K\).

Apply (1). Its left side is exactly the corresponding \(\mathcal R_{4,k}\) or \(\mathcal R_{5,\varepsilon}\). This proves B. ∎

### Proof: B implies A

Suppose instead that there is an actual strict-negative certificate.

Its even pairing with \(F\) is strictly negative. Indeed,

\[
F(t)=xyz-(xy+xz+yz)t+(x+y+z)t^2-t^3
\]

has nonnegative numerator coefficients, with its coefficients at \(t,t^2,t^3\) having strictly positive magnitudes. Therefore

\[
L=\sum_i\mu_iE_{a_i}(t_i)F(t_i)<0. \tag{3}
\]

At each atom, replace the actual even polynomial by \(E_F\), leaving its odd polynomial unchanged. Independence makes this a valid actual member, and the replacement cannot increase \(L\).

Next express its odd value at that node as a convex combination of \(O_-(t_i)\) and \(O_+(t_i)\). Split the weight accordingly, using the same \(E_F\) at both split atoms. This preserves all four odd moments and the even pairing.

The resulting nonnegative weights belong to \(\mathcal C_T\) on the finite set of certificate frequencies. Decompose them into the rays in Section 3.

- Every R4 contribution is nonnegative by B.
- Every R5 contribution, in either orientation, is nonnegative by B.
- A Z ray is nonnegative because its node is a band endpoint and (2) has the same sign as every actual even polynomial there.
- A P ray contributes
  \[
  (O_+(t)-O_-(t))E_F(t)F(t)\ge0
  \]
  by the same band signs.

Thus the lowered even pairing is nonnegative, contradicting (3). This proves A. ∎

---

## 5. What this reduction does and does not preserve

The theorem is a **dual obstruction reduction**.

It does not assert that an individual four- or five-node ray preserves the four strict even inequalities of an original six-node certificate. It generally does not.

Its correct quantifiers are:

> There must be **one common** \(F\) for which **every** relevant ray pairing is nonnegative.

They are not:

> Each six-node certificate can be replaced by one W1 five-node certificate.

Nor may the adopted at-most-five-node certificate impossibility be used to assert the scalar nonnegativity of every R4 or R5 pairing. A moment ray need not itself satisfy all four even inequalities.

The actual even factor is also important. It is the piecewise selection \(E_F\) from two **actual** envelopes. If \(F\) changes sign across the support, both actual even envelopes may appear. Replacing this expression by a single normalized root-vertex polynomial requires an additional valid argument.

### Relation to the normalized W1 results

For the positive-first R5 orientation, taking

\[
F(t)=-t(b-t)(e-t)
\]

recovers the five-node annihilator normalization used in S3–S6, including the cancellation of the node factor against the factor \(t\) in \(F\).

But those adopted results cover particular placements and explicit normalized even vertices. They do not establish:

- the negative-first R5 orientation;
- every possible actual-endpoint placement;
- the full piecewise actual-even expression;
- all R4 inequalities;
- the existence of one common root triple satisfying every required inequality.

The theorem identifies exactly where those further obligations enter.

---

## 6. Primal consequence: six frequencies need at least four pure actual corners

### Proposition

If an eligible box has a strict-negative certificate on exactly six distinct positive frequencies, it has a replacement certificate:

- on those **same six frequencies**;
- with the **same complete eight-coordinate aggregate vector**;
- using at most eight positive actual-corner atoms before same-frequency merging.

After merging, at least four of the six actual members are single actual corner polynomials \(a^{\sigma\tau}\). At most two frequencies use nontrivial corner mixtures.

### Proof

At each original frequency, express its raw row as a convex combination of the four actual-corner rows from Section 2. This preserves its raw row exactly.

The aggregate is now a positive conic combination of finitely many vectors in \(\mathbb R^8\), on the original frequencies. It has a representation using at most eight of those vectors:

If more than eight positive generators remain, choose a linear dependence

\[
\sum_j c_jr_j=0
\]

and change the coefficients to \(w_j-\lambda c_j\), with the sign of \(c\) and \(\lambda>0\) chosen so that no coefficient becomes negative and at least one becomes zero. Iterate.

This is conic sparsification preserving the aggregate exactly.

No original frequency can disappear. If one did, the surviving actual-corner atoms could be merged at equal frequencies into actual members, giving a strict-negative certificate on at most five positive frequencies. That contradicts the adopted S1/S2 theorem.

Thus six frequency groups remain, each containing at least one corner atom, while the total number of atoms is at most eight. There are at most two atoms beyond the mandatory one per frequency. Therefore at most two frequency groups are non-pure, leaving at least four pure groups. ∎

This is a structural restriction on a hypothetical six-node witness. It is not an existence proof and does not justify testing six independent arbitrary root envelopes.

---

## 7. Exact physical falsification of a W1-only bridge

### 7.1 A genuine actual all-Hurwitz independent box

Consider

\[
a_\delta(s)=
s^7+s^6+9s^5+\frac{13}{2}s^4
+23s^3+11s^2+(15+\delta)s+4,
\qquad -1\le\delta\le1.
\]

This is a compact independent coefficient box: only the coefficient of \(s\) varies; the other intervals are degenerate.

Its parities are

\[
E(t)=
\left(\frac12-t\right)(2-t)(4-t)
=4-11t+\frac{13}{2}t^2-t^3,
\]

\[
O_\delta(t)=(1-t)(3-t)(5-t)+\delta.
\]

For every actual \(\delta\in[-1,1]\),

\[
O_\delta(1/2)=\frac{45}{8}+\delta>0,
\]

\[
O_\delta(2)=-3+\delta<0,
\qquad
O_\delta(4)=3+\delta>0,
\]

and \(O_\delta(t)\to-\infty\).

The cubic therefore has exactly one simple root in each of

\[
(1/2,2),\qquad(2,4),\qquad(4,\infty).
\]

Together with the even roots \(1/2,2,4\), these are strict Hermite–Biehler interlacings in the Hurwitz orientation. Hence **every actual member of this independent box is strictly Hurwitz**. This is an exact sign/interlacing proof, not a numerical root check.

### 7.2 Six actual members and positive exact weights

Choose

\[
u_i=\frac{26+i}{30},\qquad i=1,\ldots,6,
\]

so the nodes are

\[
\frac{27}{30},\frac{28}{30},\frac{29}{30},
\frac{30}{30},\frac{31}{30},\frac{32}{30}.
\]

Choose actual members so that

\[
O_{\delta_i}(u_i)=\frac{(-1)^i}{10}.
\]

The exact parameters are:

| \(i\) | \(u_i\) | \(\delta_i\) |
|---|---:|---:|
| 1 | \(27/30\) | \(-961/1000\) |
| 2 | \(28/30\) | \(-3107/6750\) |
| 3 | \(29/30\) | \(-10081/27000\) |
| 4 | \(30/30\) | \(1/10\) |
| 5 | \(31/30\) | \(4321/27000\) |
| 6 | \(32/30\) | \(4097/6750\) |

Each lies strictly in \([-1,1]\). These follow by substituting

\[
O_0(n/30)=\frac{(30-n)(90-n)(150-n)}{27000}.
\]

Let

\[
H_6(t)=\prod_{i=1}^{6}(t-u_i).
\]

Its derivative has signs \((-,+,-,+,-,+)\), matching the selected odd values. Set

\[
\mu_i=\frac{1}{u_iO_{\delta_i}(u_i)H_6'(u_i)}>0.
\]

Explicitly,

\[
H_6'(u_i)=
30^{-5}(-1)^i(i-1)!(6-i)!,
\]

so

\[
\mu_i=
\frac{10\cdot30^5}
{u_i(i-1)!(6-i)!}.
\]

There is no approximate feasibility assertion here: the members and weights are exact.

### 7.3 Exact moment and all-eight-coordinate checks

By six-node Lagrange interpolation,

\[
\sum_{i=1}^{6}\frac{u_i^r}{H_6'(u_i)}=0,
\qquad r=0,1,2,3,4.
\]

Therefore all four odd aggregate coordinates vanish exactly.

Every chosen node lies in \((1/2,2)\), so \(E(u_i)<0\). Since all weights and nodes are positive, the complete raw aggregate has sign pattern

\[
\boxed{(-,\ 0,\ +,\ 0,\ -,\ 0,\ +,\ 0)}.
\]

In particular this is **not** an all-eight-strict-negative certificate.

The example retains both required physical checks:

- all actual denominator members belong to one eligible all-Hurwitz independent box;
- all eight aggregate coordinate signs are explicitly accounted for.

### 7.4 The precise false bridge

The following assertion is false:

> For any six fixed positive nodes, actual member values and positive weights with four zero odd moments, the weight vector is a nonnegative combination of five-node zero-odd-moment vectors of orientation \((+,-,+,-,+)\), using subsets of those same nodes and the same actual odd values.

To see this, put

\[
L=u_6-u_1=\frac16,
\]

\[
H_L(t)=\prod_{i=1}^{5}(t-u_i),
\qquad
H_R(t)=\prod_{i=2}^{6}(t-u_i).
\]

Define positive five-node weights by

\[
\mu_i^L=-\frac1{u_iO_iH_L'(u_i)}
\quad(i=1,\ldots,5),
\]

and

\[
\mu_i^R=\frac1{u_iO_iH_R'(u_i)}
\quad(i=2,\ldots,6).
\]

The left support has orientation

\[
(-,+,-,+,-),
\]

and the right support has orientation

\[
(+,-,+,-,+).
\]

Extending either vector by zero off its support,

\[
\mu=\frac1L(\mu^L+\mu^R)=6(\mu^L+\mu^R).
\]

This identity follows from

\[
H_L'(u_i)=\frac{H_6'(u_i)}{u_i-u_6},
\qquad
H_R'(u_i)=\frac{H_6'(u_i)}{u_i-u_1}.
\]

More strongly, every zero-odd-moment vector on these six frozen data has

\[
w_iu_iO_i=\frac{Au_i+B}{H_6'(u_i)}.
\]

Nonnegative weights are equivalent to

\[
Au_i+B\ge0
\]

at the six nodes, hence to the two endpoint inequalities. The two extreme rays are exactly those represented by \(u_6-t\) and \(t-u_1\), namely \(\mu^L\) and \(\mu^R\).

The displayed \(\mu\) uses both extreme rays with positive coefficients. The positive-first five-node ray alone cannot supply its positive first coordinate.

**Scope of falsification:** this defeats a moment-only W1 reduction on frozen actual data. It does not disprove a hypothetical reduction using all four additional strict even inequalities; those hypotheses are absent here, and this example deliberately fails them.

### 7.5 Original-model class obstruction as a consistency check

For any box with fixed even parity \(E\), no strict-negative certificate exists at any number of nodes. Use the even numerator test \(B_e=E\), whose numerator coefficients are positive. Every atom contributes

\[
E(t)^2\ge0,
\]

whereas an all-eight-strict-negative aggregate would have negative pairing with those nonnegative numerator coefficients.

Similarly, fixed odd parity \(O\) gives the obstruction \(tO(t)^2\ge0\).

These elementary class obstructions include the physical example. They are not advertised as the principal reduction theorem or as new common-strictly-positive-real synthesis results.

---

## 8. Exact remaining obligation

The main theorem pays an **actual-member reduction obligation**:

- actual coefficient independence is used explicitly;
- the replacement denominators are actual corner members;
- arbitrary actual odd values are reduced without pretending they are nonzero;
- same-frequency cancellation rays are retained;
- both five-node orientations are retained;
- six-node certificates are not identified with their individual moment rays.

It does **not** establish that every eligible box satisfies condition B, nor construct a box violating A.

To close the original certificate target through this route, one must do one of the following:

1. For every eligible box, prove the existence of one
   \[
   (x,y,z)\in[0,a]\times[b,c]\times[d,e]
   \]
   satisfying **all** actual R4 and both-orientation R5 inequalities; or
2. Produce an eligible box and an actual positive-weight aggregate with all eight coordinates strictly negative, checking the entire box’s Hurwitz property independently.

The current normalized W1 vertex results do not discharge either obligation. In particular, proving all remaining normalized W1 vertices would still leave the other ray placements, the opposite orientation, the actual piecewise-even interface and the common-test quantifier unpaid.

The six-frequency sparsification supplies a concrete search restriction—at least four pure actual corners—but no witness search or numerical optimization was executed here.

No passage from a nonnegative separator to a **strict** common SPR numerator is claimed.

---

## 9. Read, calculation and metadata receipt

### Complete input reads

Before mathematical construction, I read:

- the complete f347 manifest and freeze receipt;
- all six named permission/status controls, including endings;
- the ordered scientific packet in unelided raw windows:
  **1–245, 246–490, 491–745, 746–985, 986–1215, 1216–1427**.

This covered:

- S1 lines 1–34;
- S2 logical lines 1–709;
- S3 lines 1–38;
- S4 lines 1–31;
- S5 lines 1–39;
- S6 logical lines 1–574.

No linked held scientific payload was opened. S3–S6 were read completely but their individual positive-vertex conclusions are not premises of the new reduction theorem.

### Bindings

The supplied bindings were:

- Manifest: `c21e7e75b00a5352482e9c5fb3f60d34d13c6d2195e0bc3738bdb3cf9b22b1a2`
- Receipt: `b950fac572a8fea1238f8e60ba1da3f134c7961fb652e0aa8391ccf3c2af1c57`
- Packet: `751846e52bc0338e5ade0cdeb2ac39237c4cf0fbc22c099c20f783493df01052`

I subsequently read the complete `parent-live-metadata-supply-v1.json`. Its matching live source/control hashes and byte/LF counts are **parent-supplied checks**, not my executions.

Parent-native observations received were **2026-10-30T08:47:07-0700 PDT**, **08:51:05**, and **08:53:54**. They are not asserted as my native start time, private calculation times or artifact-write times.

### Calculations and execution limits

- Scientific executable/interpreter/CAS/solver runs: **zero**.
- Child hash/count/date executions: **zero**.
- Numerical root checks or approximate feasibility results: **zero**.
- The selected example uses written exact rational substitution, explicit positive weights, Lagrange identities and exact sign/interlacing checks.
- No program stdout, exit status or computational certificate is invented.
- No external-model, package installation, build, test, lint, formatter, credential/provider change, deletion, commit/push or infrastructure mutation occurred.

The wave-local process-file write was attempted and refused because the write tool permits only device transport and session-local scratch paths. No alternate file-write route was used.

**Final scientific disposition:** a complete **UNREVIEWED actual-box reduction candidate**, an actual six-frequency corner-sparsification consequence, and an exact physically checked falsification of a specified W1-only moment bridge. The universal original-model certificate/synthesis decision remains unpaid.