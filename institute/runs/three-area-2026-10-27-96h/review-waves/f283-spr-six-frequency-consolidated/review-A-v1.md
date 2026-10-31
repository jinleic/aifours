# Slice A — written-chain review

## Verdict and exact scope

**overall_correctness: incorrect**

The frozen S1 manuscript is not a correct proof as written. There are six MAJOR proof-interface/inequality defects below. No FATAL counterexample to the stated theorem was found. The all-variable reconstruction in this report supplies the genericity and cross-member phase-order arguments, proves the required K1 classification in writing, replaces K2’s required positivity interface by a direct written proof, and repairs the endpoint, scaling, tail and reciprocal arguments.

Accordingly, **the stated six-positive-frequency lower bound is SUPPORTED by the reconstruction below**, not by an unqualified acceptance of the frozen manuscript or its receipts. The original common-numerator synthesis-or-obstruction problem is not resolved.

**confidence: 0.96**

No scientific execution was performed. K1’s reported intermediate count 676 and K2’s coefficient counts, coefficient positivity, canonical hashes and point checks remain **INCONCLUSIVE / unverified finite receipt assertions**. None is used as a premise of the reconstructed theorem.

### First unpaid premise

In the literal chain, S1 LF 22 does not justify cross-member phase ordering merely by monotonicity of each individual member’s phase; the necessary box-wide argument is supplied below. The first explicitly false reduction is S1 LF 26, “weights are finite, so \(O(t_i)\ne0\).” Finite positive weights do not exclude a node at an odd root. The required generic-frequency reduction is supplied below and also excludes even-root nodes.

If those preliminary repairs are made but this review’s supplementary proofs are not incorporated, the first declared unverified finite premise is K1’s complete classification at S1 LF 38. Conditional on K1, K2’s all-variable positivity interface at LF 71 remains unproved by S2/S3 alone, and the scale, tail and reciprocal defects still require correction.

In the reconstruction below there is **no remaining unpaid scientific premise for the stated lower bound**. The stronger coefficient-positivity assertions in S3 remain unpaid and are not required.

## Merge-blocking findings

### Finding 1

- **title:** Justify the nonzero-parity reduction before using strict class regions
- **body:** S1 LF 26 infers \(O(t_i)\ne0\) from finiteness of the weights, but a finite positive-weight atom may be placed at an odd root of its strictly Hurwitz member. The subsequent strict placements and divisions by \(O\) therefore do not cover the quantified certificates as written; even-root samples also need treatment before applying K1’s two-valued sign words. Add a simultaneous small perturbation of the distinct positive nodes, holding the actual members and positive weights fixed, which preserves all eight strict coordinate inequalities and avoids both parity root sets. This preserves the number of positive nodes and makes the subsequent generic argument applicable.
- **priority:** 1
- **confidence:** 1.0
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 26
- **line_end:** 26

### Finding 2

- **title:** Correct the sign of the variable-leading envelope correction
- **body:** In the variable-leading \((b,e)\) case, LF 59 uses \((1/\lambda_- -1/\lambda_+)\) times the \(O_+\) unit function, although the actual correction \(R_+/\lambda_+-R_-/\lambda_-\) equals \((R_+-R_-)/\lambda_-+(1/\lambda_+-1/\lambda_-)R_+\). The printed coefficient has the opposite sign whenever \(\lambda_->\lambda_+\), precisely a setting needed after reciprocity. The stated product also includes an increasing factor \(t-x\) and is not the claimed product of nonincreasing factors. Use the correct nonnegative coefficient and prove the \(x=a\) correction with \(R_+/h=[(t-a)/(t-u_1)]\,[(d-t)/(u_4-t)]\,[(e-t)/(f-t)]\); then obtain \(x=0\) by the signed-term multiplier argument.
- **priority:** 1
- **confidence:** 1.0
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 59
- **line_end:** 59

### Finding 3

- **title:** Clear both ray and envelope denominators in the K2 numerator
- **body:** LF 71 first defines \(N=\mathrm{Vdm}\,D_xJ\), but its subsequent displayed expansion multiplies the bare numerators \(n_i\) by \(\mathrm{Vdm}\,D_x\) without dividing by \(H'(u_i)\) and the individual envelope denominators. That is not the defined \(N\). The correct polynomial identity is \(N=\sum_iq_in_i(\mathrm{Vdm}/H'(u_i))(D_x/d_i)\), with the sign of \(\mathrm{Vdm}/H'\) included and \(d_i\) the appropriate \(f-u_i\) or \(u_i-a\) denominator. Consequently positivity of an author-claimed expanded polynomial cannot be transferred through the printed identity; two point identities in S3 do not repair an incorrect all-variable interface. Correct that interface or use the written pair proof below, which avoids K2 entirely.
- **priority:** 1
- **confidence:** 1.0
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 71
- **line_end:** 71

### Finding 4

- **title:** Use the correct symmetric-function identity in the scale argument
- **body:** The LF 71 identity has the wrong sign: for \(q_i=e_m\) of the three other nodes, \(q_2(u_2-x)-q_1(u_1-x)=(u_2-u_1)(e_m(u_3,u_4)+xe_{m-1}(u_3,u_4))\), not the printed minus. Its claimed strict positivity also fails at \(m=3,x=0\), where the difference is exactly zero, and \(e_3/e_2\) on two variables is zero rather than a mean exceeding \(x\). Thus the written proof of \(S_+>0\) and the variable-leading interface is invalid. The corrected coefficient difference is nonnegative; positivity of \(q_i(u_i-x)\) and strict increase of \(h\) still give \(S_+>0\), including this equality case.
- **priority:** 1
- **confidence:** 1.0
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 71
- **line_end:** 71

### Finding 5

- **title:** Restore the missing gap and correct order in the tail estimate
- **body:** LF 83’s expansion omits \(B-A\) from the negative bound: the derived bound is \(-a(B-A)G(A)/((A-a)(B-a))\), whose gap cancels the prefactor in LF 82. LF 85 then invokes \(A<a\), although this case has \(a<A\), and gives the cross-difference the wrong sign. These steps establish the first-band \(x=0\) tail, so the printed argument does not justify its final strict inequality. Restore the gap and use \((v-a)/(w-a)-(v-A)/(w-A)=(w-v)(A-a)/((w-a)(w-A))>0\) for \(a<A\le v<w\).
- **priority:** 1
- **confidence:** 0.99
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 83
- **line_end:** 85

### Finding 6

- **title:** Use actual reciprocal odd-envelope roots instead of outer gap bounds
- **body:** LF 89 identifies the reciprocal odd bands with \((1/e,1/d)\), \((1/c,1/b)\), and \((1/a,1/\rho_1^{\min})\), but \(a,b,c,d,e\) are original odd-envelope roots, whereas reciprocal odd roots are reciprocals of original even-envelope roots. For example, both original third even roots are strictly inside \((d,e)\), so the new first odd-band endpoints are strictly inside \((1/e,1/d)\), not equal to its endpoints. These false identities are then used to assert that reciprocal nodes meet the hypotheses of §§6–7 and Lemma 5. Define the actual reversed envelopes, reapply the class-placement lemma to the reversed box, and use \(c'>1/c\) for B’s remaining split, as proved below.
- **priority:** 1
- **confidence:** 1.0
- **severity:** MAJOR
- **file_path:** /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/manuscript-20261029-six-frequency-lower-bound-consolidated-v1.md
- **line_start:** 89
- **line_end:** 89

## 1. Actual box, endpoints, strictness and parity genericity

**Scope:** S1 LF 5, 7, 11–15, 30–31.  
**Status:** SUPPORTED with the explicit reductions below.

A real monic strictly Hurwitz polynomial has all coefficients strictly positive: its real linear factors \(s+\alpha\) and real conjugate-pair factors \(s^2+2\alpha s+\alpha^2+\beta^2\) have positive coefficients. Every interval endpoint is realized by a member of the independent box, so all lower coefficient endpoints are positive. In the variable-leading reversed box, the leading lower endpoint is also positive.

At a fixed \(t>0\), the even and odd coefficient groups are disjoint independent intervals. Their images are the complete intervals \([E_-,E_+]\) and \([O_-,O_+]\), and every combination of the two endpoint polynomials is an actual box member, not merely a sign relaxation. All four combinations are Hurwitz. No rectangle contains \((0,0)\), since that would give an actual imaginary-axis zero. This is the actual-member content needed for the root bands and cross-member phase constraints.

Atoms at a common finite node merge using their positively weighted average coefficient vector, which stays in the box. Zero/infinity atoms contribute only positive multiples of \(e_0/e_7\). Removing them makes the finite aggregate coordinatewise at least as negative and still strictly negative in all eight coordinates. Alternatively, retaining them gives exactly the tightened moment signs in LF 31. They do not change the positive-node count.

For any hypothetical strict certificate, fix its members and positive weights. Each aggregate coordinate is a continuous function of the positive finite nodes. Strict negativity, positivity and ordering of the distinct nodes persist in a sufficiently small product neighborhood. Each fixed member has only finitely many positive roots of \(E\) and \(O\). Choose the perturbed nodes in that neighborhood avoiding both root sets. The box members remain unchanged and Hurwitz, the node count remains unchanged, and all parities are now nonzero.

Therefore excluding generic certificates excludes certificates with single-parity zeros as well. Simultaneous parity zeros are already impossible by Hurwitzness. No boundary-to-interior assumption on the coefficient intervals is needed.

For
\[
F=-t(b-t)(e-t)
\quad\text{or}\quad
F=-t(c-t)(d-t),
\]
the even numerator coefficients are respectively
\[
(0,be,b+e,1),\qquad (0,cd,c+d,1).
\]
The three nonzero entries are strictly positive. Hence the test pairing with a strict aggregate is strictly negative. Endpoint atoms pair to zero. This does not require a positive constant numerator coefficient.

## 2. Root bands, cross-member order and placements

**Scope:** S1 LF 19–26.  
**Status:** SUPPORTED after genericity and the following box-wide phase argument.

Apply the stated Hermite–Biehler import to the four actual \((E_\pm,O_\pm)\) corner combinations. A common even polynomial interlaces both odd envelopes, separating the corresponding odd roots before comparing signs. Since \(O_+-O_-\) has nonnegative coefficients on \(t>0\), the smallest roots satisfy \(a\le b\), the middle roots \(c\le d\), and the largest roots \(e\le f\). Common interlacing gives
\[
a\le b<c\le d<e\le f.
\]
The same comparison with any intermediate odd polynomial puts its roots in
\[
[a,b],\quad[c,d],\quad[e,f].
\]

More strongly than the closed bounds stated in LF 19, every actual even polynomial interlaces both odd envelopes, so
\[
0<\rho_1<a,\qquad b<\rho_2<c,\qquad d<\rho_3<e.
\]
These strict bounds hold for \(E_-\) and \(E_+\) themselves.

At a fixed positive \(t\), these bands confine all actual member classes to at most two adjacent values:

- \(0/1\) below \(a\);
- \(1/2\) in \([a,b]\);
- \(2/3\) in \([b,c]\);
- \(3/4\) in \([c,d]\);
- \(4/5\) in \([d,e]\);
- \(5/6\) in \([e,f]\);
- \(6\) above \(f\).

At shared boundaries the permitted sets can be smaller. Thus member-to-member class variation at the same frequency is at most one. For \(t_i<t_j\), follow member \(i\) to \(t_j\); its class has not decreased because its own phase increases. Comparing there with member \(j\) proves
\[
q_j\ge q_i-1.
\]
When both nonzero parity signs differ, \(q_j-q_i\) is \(2\) modulo \(4\), strengthening the bound to
\[
q_j\ge q_i+2.
\]
Individual-member phase monotonicity alone would not prove this cross-member statement.

The strict placements follow:

- **A:** Classes 2 and 1 give \(a<t_1<t_2<b\); classes 3 and 2 give \(b<t_3<t_4<c\); class 4 gives \(c<t_5<e\).
- **B:** The first pair is unchanged; class 3 gives \(b<t_3<d\); classes 5 and 4 give \(d<t_4<t_5<e\).
- **C:** Class 2 gives \(a<t_1<c\); classes 4 and 3 give \(c<t_2<t_3<d\); classes 5 and 4 give \(d<t_4<t_5<e\).

The same proof works for positive variable-leading boxes:
\[
\Delta=O_+-O_-=\delta_0+\delta_1t+\delta_2t^2+\delta_3t^3,\qquad \delta_j\ge0.
\]
If a positive root of \(O_-\) and \(O_+\) coincides, \(\Delta\) vanishes there, forcing every \(\delta_j=0\). All odd intervals are then fixed. Otherwise all three odd-band widths are strictly positive.

Each A/B/C placement requires a positive odd-band width, so all three widths are positive whenever subsequent cases are needed. Degenerate odd boxes are excluded already by placements; no collapsed-band denominator is used. Degenerate even coefficient intervals cause no difficulty.

## 3. Moments, oriented subsequence and a written K1 classification

**Scope:** S1 LF 30–38; S2 LF 6–15.  
**Status:** Required signs, \(m<5\) exclusion and exact three-word classification SUPPORTED in writing. Auxiliary count 676 INCONCLUSIVE.

Set \(x_i=\mu_iE_i\), \(y_i=\mu_it_iO_i\). Coordinate negativity gives, for either sequence,
\[
\sum z_i<0,\qquad
\sum t_iz_i>0,\qquad
\sum t_i^2z_i<0,\qquad
\sum t_i^3z_i>0.
\]
Optional endpoint atoms only strengthen the relevant inequalities.

If the nonzero sign word lacks \(-,+,-,+\), it has the form \(+^*-^*+^*-^*\). Put three distinct positive roots \(r_1<r_2<r_3\) in its three block gaps. Empty blocks are handled by putting several roots in the same open gap, before the first positive node, or after the last node. Then
\[
q(t)=\prod_j(r_j-t)
\]
has alternating coefficients of strictly positive magnitudes and agrees in sign with every nonzero \(z_i\). Thus \(\sum z_iq(t_i)>0\), whereas expanding by the four moment inequalities gives a negative number.

This also proves the **non-strict moment version**: if all four signed constraints are merely non-strict, expansion gives \(\le0\), still a contradiction. That extension is needed for the cone.

Thus \(m\le3\) is impossible. For \(m=4\), both parity words must be exactly \(-,+,-,+\). Their joint class starts at least at 2 and makes three double reversals, reaching at least 8, impossible in \(\{0,\ldots,6\}\).

For five nodes each parity word has three or four changes among the four adjacent gaps. Three changes force initial sign \(-\), final sign \(+\), and exactly one no-change gap. Four changes give a fully alternating word with identical endpoint signs.

If both parities have four changes, four double steps are impossible. If one has four and the other three, there are three double steps and one single step, so
\[
q_5-q_1\ge5.
\]
The possible initial/final sign pairs are
\[
(+,-)\to(+,+),\quad
(-,-)\to(-,+),\quad
(-,+)\to(+,+),\quad
(-,-)\to(+,-).
\]
Their largest permitted class differences are respectively \(1,3,3,1\), all below 5. Hence both parities have three changes.

Their initial pair is \((-,-)\), final pair \((+,+)\). If their no-change gaps coincide, three double steps force \(q_5\ge q_1+6\ge8\). Otherwise there are two double steps and two single steps. The only possible endpoints are \(q_1=2,q_5=4\), so each double step is exactly \(+2\) and each single step exactly \(-1\).

Of the six choices for the two single-step positions, adjacent choices \(\{1,2\},\{2,3\},\{3,4\}\) create a backward displacement of two between complementary sign pairs, violating the all-pairs rule. The remaining choices give exactly:

- \(\{1,3\}\): \((2,1,3,2,4)=A\);
- \(\{1,4\}\): \((2,1,3,5,4)=B\);
- \(\{2,4\}\): \((2,4,3,5,4)=C\).

Each displayed word satisfies the all-pairs bounds. This proves the complete classification required by the theorem without trusting or executing K1. It does not verify the intermediate count 676.

## 4. Eight-ray completeness and envelope reduction

**Scope:** S1 LF 42–46.  
**Status:** SUPPORTED after replacing “the certificate’s \(y\)-vector lies in \(\mathcal C\)” by “the certificate’s positive weight vector \(\mu\) lies in \(\mathcal C\).”

The cone is a cone of nonnegative weights \(w\), not signed \(y\). It is pointed because \(w\ge0\). For an extreme ray with support size \(s\), active coordinate constraints have rank \(5-s\), and a ray requires total active rank at least four.

For \(s\le3\), the non-strict separator proof above rules out every nonzero feasible vector. For \(s=5\), all four moment constraints must be active. The Vandermonde null vector for \(z_i=w_it_iO_i\) has alternating signs \(+,-,+,-,+\), or its negative. Neither A’s odd word \(-,+,-,-,+\) nor B/C’s \(-,+,-,+,+\) permits \(w\ge0\) on all five nodes.

Therefore \(s=4\). Four moments cannot all vanish on four distinct nodes, so exactly three are active and the remaining signed moment is strictly negative.

For
\[
H(t)=\prod_{i=1}^4(t-u_i),\qquad q_i=e_{3-k}(\widehat u_i),
\]
interpolation gives
\[
\sum_i\frac{q_iu_i^r}{H'(u_i)}=(-1)^{3-k}\delta_{rk}.
\]
Hence
\[
w_i=\frac{q_i}{u_iO_iH'(u_i)}
\]
has signed moment vector \(-e_k\). All \(q_i>0\), and \(H'\) has signs \(-,+,-,+\), so positivity is equivalent to the surviving odd word \(-,+,-,+\).

The supports are exactly:

- A: \((1,2,3,5)\), \((1,2,4,5)\);
- B/C: \((1,2,3,4)\), \((1,2,3,5)\).

There are eight rays. Minkowski–Weyl supplies nonnegative combinations; any nonzero combination has a positive coefficient.

Writing \(m=3-k\),
\[
q_i-q_j=(u_j-u_i)e_{m-1}(\text{remaining two nodes}),\qquad i<j.
\]
Thus \(q_i\) is nonincreasing, constant only for \(m=0\).

On a ray \(w_i>0\). If \(F\le0\) on the support, replacing every actual \(E_i\) by \(E_+\) decreases the pairing; if \(F\ge0\), use \(E_-\). The chosen even envelope has a fixed positive leading multiplier \(\kappa\) and roots in \((0,a),(b,c),(d,e)\). Suppress the common positive \(\kappa\). Its pairing is separately affine in those roots, so checking
\[
x\in\{0,a\},\quad y\in\{b,c\},\quad z\in\{d,e\}
\]
suffices.

Artificial endpoint root polynomials need not be actual Hurwitz members. This is a multiaffine enlargement after choosing an actual envelope, not an assertion of their membership. In particular artificial \(x=0\) is harmless.

A positive term is minimized by largest \(|O|\), a negative term by smallest \(|O|\), with the required odd sign. If an endpoint envelope vanishes at a node where \(F=0\), the cancelled expression below is used only as a lower bound—not as an attained \(0/0\) quotient.

## 5. Outside-band lemma, including variable leading scales

**Scope:** S1 LF 50–59.  
**Status:** SUPPORTED by the corrected proof.

Here
\[
a<u_1<u_2<b<u_3\le c<d\le u_4<f,
\]
and \(F=-t(c-t)(d-t)\le0\) at every node. Use the upper even envelope and root vertices. Write
\[
O_-=\lambda_-O_-^0,\quad O_+=\lambda_+O_+^0,\quad
\lambda_-\ge\lambda_+>0.
\]

For \(u_4\in(d,e)\), the correct fourth-term signs are **positive for \(z=d\)** and **negative for \(z=e\)**. LF 51 reverses them, although later case headings use the correct patterns.

### \((y,z)=(c,d)\)

All terms are nonnegative; the first two are strictly positive. This includes \(u_3=c\) or \(u_4=d\).

### \((y,z)=(c,e)\)

For \(u_4\in(d,e)\), signs are \(+,+,+,-\). At \(x=a\), the unit \(O_-\) quotient is
\[
R_-=-(t-c)^2.
\]
Its unweighted third divided difference is zero. Nodes 1,3,4 use \(O_-\) at their worst endpoints. Replacing node 2’s formal \(O_-\) by its required positive \(O_+\) contributes strictly positively: \(R_+(u_2)>0>R_-(u_2)\), \(H'(u_2)>0\), and both scales are positive.

Thus the unweighted sum is positive. Monotone \(q\) reweighting preserves positivity for \(+,+,+,-\). For \(x=0\), each term is multiplied by
\[
v(t)=\frac{t}{t-a}>0,
\]
a decreasing function, so the sum is at least \(v(u_4)\) times the positive \(x=a\) sum. For \(u_4\ge e\), all terms are nonnegative and the first two strictly positive.

### \((y,z)=(b,d)\)

Nodes 1 and 4 are nonnegative. Nodes 2 and 3 both use \(O_+\). With \(h(t)=(t-u_1)(u_4-t)\),
\[
\frac{R_+(t)}{h(t)}
=
\frac{t-x}{t-u_1}\,
\frac{d-t}{f-t}\,
\frac{d-t}{u_4-t}.
\]
On \([u_2,u_3]\), these are positive nonincreasing factors; the first is strictly decreasing because \(x\le a<u_1\). The weighted middle pair is therefore strictly positive since \(q_2\ge q_3\).

Both terms share scale \(1/\lambda_+\). This also verifies, but does not require, the manuscript’s positive unweighted divided difference \(A'/\prod(f-u_i)\).

### \((y,z)=(b,e)\), \(u_4\le e\)

First take \(x=a\). Worst denominators are \(O_-\) at nodes 1,4 and \(O_+\) at 2,3. The unit \(O_-\) baseline is
\[
R_-=-(t-b)(t-c).
\]
Its weighted sums are
\[
(bc,b+c,1,0)
\]
for \(k=0,1,2,3\), not zero for every \(k\) as LF 59 claims. They are nonnegative.

Let \(\Delta_0=O_+^0-O_-^0\), \(c(t)=\Delta_0(t)/(f-t)\). The correction is at nodes 2,3. With \(h=(t-u_1)(u_4-t)\), write \(c/h=W\phi\), where
\[
W=
\frac{e-t}{f-t}
+\frac{(b-t)(c-t)}{(t-a)(d-t)},\qquad
\phi=
\frac{t-a}{t-u_1}\frac{d-t}{u_4-t}.
\]
The first summand of \(W\) is nonincreasing; its second is positive at \(u_2\) and negative at \(u_3\). Hence \(W_2>W_3\) and \(W_2>0\). Also \(\phi_2>\phi_3>0\).

If \(W_3\ge0\), these comparisons give \(W_2\phi_2>W_3\phi_3\). If \(W_3<0\), use directly \(W_2\phi_2>0>W_3\phi_3\). The negative-\(W\) chain printed in LF 59 has its last inequality reversed, but this corrected argument proves the required comparison.

Since \(c(u_2)/h(u_2)>0\) and \(q_2\ge q_3\), the weighted correction pair is strictly positive.

For actual scales the correction is
\[
\frac{R_+-R_-}{\lambda_-}+\varepsilon R_+,\qquad
\varepsilon=\frac1{\lambda_+}-\frac1{\lambda_-}\ge0.
\]
Its extra pair is nonnegative, and positive when \(\varepsilon>0\), because
\[
\frac{R_+}{h}
=
\frac{t-a}{t-u_1}\,
\frac{d-t}{u_4-t}\,
\frac{e-t}{f-t}
\]
is positive strictly decreasing. Thus the scaled \(x=a\) total is positive.

For \(x=0\), multiply all four actual terms by decreasing \(v(t)=t/(t-a)\). Their pattern is \(+,+,-,-\), so the sum is at least \(v(u_3)\) times the positive \(x=a\) sum.

For \(u_4\ge e\), nodes 1,4 are nonnegative and the middle pair is strictly positive using
\[
\frac{R_+}{h}
=
\frac{t-x}{t-u_1}\,
\frac{d-t}{u_4-t}\,
\frac{e-t}{f-t},
\]
again a product of positive nonincreasing factors with a strict factor.

### Zero envelope endpoints

At \(u_3=c\), \(F=0\), so the actual term is zero. For \(y=b\), the cancelled \(O_+\) expression gives a nonpositive formal term and is a valid lower bound; for \(y=c\), it is zero.

At \(u_4=d\), \(F=0\). For \(z=e\), the cancelled \(O_-\) expression is nonpositive and again a lower bound; for \(z=d\), it is zero. At \(u_4=e,z=e\), use the same convention or the \(u_4\ge e\) proof.

Strictness survives through the explicitly strictly positive correction or middle pair, not through an unjustified limit of positive numbers. All remaining denominators are positive node gaps, \(u_i-a\), or \(f-u_i\). No denominator at \(f\) is needed; an actual positive odd value cannot occur at or above \(f\).

## 6. Phase C first-gap case and a written replacement for K2

**Scope:** S1 LF 63–71; S3 LF 1–129.  
**Status:** Every required ray pairing SUPPORTED in writing. S3’s coefficient-expansion assertions INCONCLUSIVE.

Here
\[
b\le u_1<c<u_2<u_3<d<u_4<e,\qquad
F=-t(b-t)(e-t)\ge0.
\]
Use the lower even envelope. At \(u_1=b\), the actual term is zero; otherwise LF 63’s endpoint signs are correct. Nodes 2,3 use \(O_+,O_-\), respectively.

### \((y,z)=(b,e)\)

All terms are nonnegative and the middle terms strictly positive.

### \((y,z)=(b,d)\)

Worst-endpoint signs are \(+,+,+,-\), permitting monotone-\(q\) reduction to the unweighted case. At \(x=a\), the formal all-\(O_-\) quotient is \(-(t-b)^2\), whose third divided difference is zero.

At \(x=0\), it is
\[
-t^2+(2b-a)t-(b-a)^2-\frac{a(b-a)^2}{t-a},
\]
whose third divided difference is
\[
\frac{a(b-a)^2}{\prod_i(u_i-a)}>0.
\]
Changing node 2 from negative \(O_-\) to positive \(O_+\) adds strictly positively for either leading scale. Thus both unweighted vertex sums are positive; monotone \(q\) gives all four rays.

This avoids LF 67’s incorrect sufficient inequality for the constant interpolation coefficient: the needed comparison there is
\[
\prod_i(a+h_i)>\prod_i h_i,
\]
not the printed \(\prod_i(a+h_i)>a\prod_i h_i\).

### \((y,z)=(c,e)\)

Use the formal all-\(O_+\) quotient
\[
g(t)=\frac{(t-x)(e-t)^2}{f-t}.
\]
Node 3’s replacement by actual negative \(O_-\) strictly increases its ray term, since \(H'(u_3)<0\), \(g_+>0\), and \(g_-<0\). This remains true for either positive scale.

Let
\[
A=(f-x)(f-e)^2>0,\quad D=\prod_i(f-u_i)>0,\quad s_j=e_j(u).
\]
The cubic interpolant coefficients satisfy
\[
c_3=A/D>0,\qquad
c_2=-1+A(f-s_1)/D<0,
\]
\[
c_0=-xe^2/f-As_4/(fD)<0,
\]
\[
c_1=2e+x-f+A(f^2-fs_1+s_2)/D.
\]
If \(s_1<f\), the product bound \(D\ge f^3(f-s_1)\) and \(A<f^3\) give \(c_2<0\); if \(s_1\ge f\), this is immediate. The other Bonferroni bound gives
\[
f^2-fs_1+s_2\ge D/f^2,
\]
hence
\[
c_1\ge\frac{e^2+2xe}{f}-\frac{xe^2}{f^2}>0.
\]
Therefore \(J_k=(-1)^{3-k}c_k>0\) for all \(k\). At \(u_1=b\), the true zero term exceeds the negative cancelled formal term, so this proof covers that boundary too.

### \((y,z)=(c,d)\): direct all-variable pair proof

This is the case assigned to K2. Its required positivity has a written proof without expansion, normalization or receipt premises. It works for every \(x\in[0,a]\).

Set \(q_i=e_m(\widehat u_i)\), \(m=0,1,2,3\). The reduced unit functions for nodes 1,2 and nodes 3,4 are
\[
g_+(t)=\frac{(t-x)(d-t)(e-t)}{f-t},
\qquad
g_-(t)=-\frac{(t-x)(t-b)(t-c)}{t-a}.
\]

For the first pair put
\[
h(t)=\frac{(d-t)(e-t)}
{(u_3-t)(u_4-t)(f-t)}.
\]
Its factors \((d-t)/(u_3-t)\), \((e-t)/(u_4-t)\), and \(1/(f-t)\) are positive strictly increasing on \([u_1,u_2]\).

Write \(E_j=e_j(u_3,u_4)\), with \(E_{-1}=E_3=0\). Since
\[
q_1=E_m+u_2E_{m-1},\qquad q_2=E_m+u_1E_{m-1},
\]
we have
\[
q_2(u_2-x)-q_1(u_1-x)
=(u_2-u_1)(E_m+xE_{m-1})\ge0.
\]
Both \(q_i(u_i-x)\) are positive. Strict increase of \(h\) yields
\[
S_+
=
\frac{q_2(u_2-x)h(u_2)-q_1(u_1-x)h(u_1)}
{u_2-u_1}>0.
\]
This includes \(m=3,x=0\), where the coefficient difference is zero.

For the second pair define
\[
L(t)
=
-\frac{g_-(t)}{(t-u_1)(t-u_2)}
=
\frac{t-x}{t-a}\,
\frac{t-b}{t-u_1}\,
\frac{t-c}{t-u_2}.
\]
On \([u_3,u_4]\), all factors are positive nonincreasing because \(x\le a\), \(u_1\ge b\), \(u_2>c\). The last is strictly decreasing, so \(L(u_3)>L(u_4)>0\). As \(q_3\ge q_4\),
\[
S_-=
\frac{q_3L(u_3)-q_4L(u_4)}{u_4-u_3}>0.
\]

Thus the actual scaled sum is
\[
S_+/\lambda_+ + S_-/\lambda_->0.
\]
No comparison between the two scales is needed in this case.

At \(u_1=b\), the cancelled formal first term is negative, while the actual term is zero. Replacing it by the actual value only increases the sum. All other denominators are strictly positive.

This proves all four rays at both \(x\) vertices—and indeed every \(x\in[0,a]\)—directly.

### Exact K2 interface audit, not receipt acceptance

For \(a=1\), correct clearing is
\[
N=\sum_iq_in_i
\frac{\mathrm{Vdm}}{H'(u_i)}
\frac{D_x}{d_i}.
\]
For \(x=0\),
\[
(d_1,d_2,d_3,d_4)
=(f-u_1,f-u_2,u_3-1,u_4-1);
\]
for \(x=1\),
\[
(d_1,d_2,d_3,d_4)=(f-u_1,f-u_2,1,1).
\]
Both quotient factors are polynomials, retaining the sign of \(\mathrm{Vdm}/H'\). Since \(\mathrm{Vdm}>0,D_x>0\), a correctly proved \(N>0\) would imply \(J>0\).

The positive-coefficient assertion, counts, digests and point checks in S3 do not establish that premise in Slice A. The pair proof establishes the required \(J\) positivity instead.

The nine-positive-gap parametrization omits \(u_1=b\), where \(U=0\). A generic positive-gap certificate alone does not cover that boundary. The direct proof above does. Degenerate odd bands cannot occur in C because \(c<u_2<u_3<d\) forces \(\Delta\ne0\). Normalizing \(a>0\) is permissible but unnecessary here.

## 7. Phase C first-odd-band tail

**Scope:** S1 LF 75–85.  
**Status:** SUPPORTED by the repaired all-variable proof.

Let
\[
A=u_1\in(a,b],\quad B=u_2,\quad C=u_3\in(c,d),\quad D=u_4\in(d,e).
\]
The correct sign is \(F(A)\le0\), not \(\ge0\). Every actual \(E(A)<0\), so the first ray term is nonnegative and can be dropped.

On the tail \(F>0\), use the lower even envelope. If \(z=e\), all three tail terms are positive. Otherwise \(z=d\), with signs \(+,+,-\). Since \(q_B\ge q_C\ge q_D\), positivity of the unweighted tail implies positivity of every weighted tail.

For \(x=a\), \(y=b\) or \(c\), put
\[
g_-(t)=-\frac{(t-y)(t-b)}{\lambda_-}.
\]
Its full four-node third divided difference is zero. The tail is
\[
T_a=-\frac{g_-(A)}{H'(A)}+\frac{D_y}{H'(B)},
\]
where
\[
D_y=\frac{(B-y)\Delta(B)}
{(B-c)\lambda_-\lambda_+(f-B)}>0,
\qquad
w=\frac{(b-A)(y-A)}{\lambda_-}=-g_-(A)\ge0.
\]

If \(A<b\), \(\Delta\) is nondecreasing and
\[
\Delta(A)>\lambda_+(b-A)(c-A)(f-A).
\]
For \(y=c\), \(D_y>w\) follows from \(f-A>f-B\). For \(y=b\), use
\[
(B-b)(c-A)-(b-A)(B-c)
=\alpha\gamma+\beta\gamma+\gamma^2>0,
\]
with \(\alpha=b-A,\beta=B-c,\gamma=c-b\), together with \(f-A>f-B\). If \(A=b\), \(w=0,D_y>0\) directly.

Since \(0<H'(B)<|H'(A)|\), \(T_a>0\).

For \(x=0\),
\[
g_0(t)=-\frac{t(t-y)(t-b)}{\lambda_-(t-a)},
\]
and
\[
J_3(g_0)
=\frac{a(b-a)(y-a)}
{\lambda_-\prod_i(u_i-a)}>0.
\]
This follows from the pole residue and
\[
\sum_i\frac1{(u_i-a)H'(u_i)}
=-\frac1{\prod_i(a-u_i)}.
\]

Let \(G(t)=1/((C-t)(D-t))\), increasing on \([A,B]\). The same \(D_y>w\) comparison gives
\[
T_0>J_3(g_0)+\frac{w}{B-A}
\left[\frac{BG(B)}{B-a}-\frac{AG(A)}{A-a}\right].
\]
The bracket equals
\[
\frac{B}{B-a}(G(B)-G(A))
-\frac{a(B-A)G(A)}{(A-a)(B-a)},
\]
strictly exceeding its second term. Substitution yields
\[
T_0>
\frac{a}{\lambda_-(A-a)(B-a)}
\left[
\frac{(b-a)(y-a)}{(C-a)(D-a)}
-
\frac{(b-A)(y-A)}{(C-A)(D-A)}
\right]>0.
\]

For the last sign, pair \((b-r)/(C-r)\) and \((y-r)/(D-r)\) at \(r=a,A\). For \(a<A\le v<w\),
\[
\frac{v-a}{w-a}-\frac{v-A}{w-A}
=\frac{(w-v)(A-a)}{(w-a)(w-A)}>0.
\]
All factors are nonnegative and the left product positive, including \(A=b\). Every denominator is positive. This covers all tail vertices and all four rays with leading scales retained.

## 8. Correct reciprocity, A/B and quantified assembly

**Scope:** S1 LF 89–99.  
**Status:** SUPPORTED after replacing the false reciprocal band equalities.

For \(a^*(s)=s^7a(1/s)\), substitution gives
\[
E_{a^*}(1/t)=-t^{-3}O_a(t),\qquad
O_{a^*}(1/t)=-t^{-3}E_a(t),
\]
and
\[
P_{a^*,b^*}(1/t)=t^{-7}P_{a,b}(t).
\]
The unwrapped phase satisfies
\[
\phi_{a^*}(1/\sqrt t)=7\pi/2-\phi_a(\sqrt t),
\]
so non-axis classes transform by \(q^*=6-q\), not merely by an ambiguous sign-pair identification.

Raw rows obey
\[
\operatorname{row}(a^*,1/t)
=t^{-7}\operatorname{reverse}(\operatorname{row}(a,t)).
\]
Thus raw finite weights transform as \(\mu_i^*=\mu_it_i^7\). Compactified rows reverse exactly with unchanged weights. LF 89’s “weights unchanged” is valid only in the latter convention.

Endpoint atoms swap, retaining or absorbing their positive constant/leading factors. The reversed family is an independent box with leading interval \([\ell_0,u_0]\subset(0,\infty)\), constant coefficient 1, and roots \(1/r\) with negative real parts. All preceding variable-leading results apply.

Let \(\rho_j^\pm\) be the actual roots of original \(E_\pm\). Reversed odd envelopes are
\[
O_-^*(t)=-t^3E_+(1/t),\qquad
O_+^*(t)=-t^3E_-(1/t).
\]
Their actual band endpoints are
\[
a'=1/\rho_3^+,\quad b'=1/\rho_3^-,
\quad c'=1/\rho_2^-,\quad d'=1/\rho_2^+,
\quad e'=1/\rho_1^+,\quad f'=1/\rho_1^-.
\]
Consequently \(a',b'\) lie strictly inside \((1/e,1/d)\), \(c',d'\) strictly inside \((1/c,1/b)\), and \(e',f'>1/a\). Outer reciprocal gaps are not new odd-band endpoints. Equality between the two endpoints of a band is possible if the original even interval is degenerate.

A reverses exactly to C. Reapply the placement lemma to the actual reversed box and actual \(a',\ldots,f'\). Its first node lies in \((a',c')\), split at \(b'\); the middle pair lies in \((c',d')\), final pair in \((d',e')\). Sections 6 and 7 above exclude both possibilities. A degenerate required band makes the strict class placement impossible already.

For B with \(t_3\le c\), both original ray supports meet the outside-band lemma. For \(t_3>c\), reciprocal B is again B. Its actual reversed placements give
\[
u'_1,u'_2\in(a',b'),\quad
u'_3\in(b',d'),\quad
u'_4,u'_5\in(d',e').
\]
Since \(\rho_2^-<c\),
\[
c'=1/\rho_2^->1/c>1/t_3=u'_3.
\]
Thus \(u'_3\in(b',c')\), and both reversed supports satisfy the variable-leading outside-band lemma.

Finally, assume any strict aggregate with at most five distinct positive nodes, optional endpoint atoms and arbitrary actual members. Merge same-node atoms, remove endpoints if desired, and perform the generic perturbation preserving strictness and node count. Moments exclude \(m<5\). Written classification leaves A/B/C. For each word, the positive weight vector is a nonnegative combination of its eight odd-moment rays. Every ray has strictly positive pairing with that word’s test by the all-variable proofs above. The nonzero weight vector therefore has positive pairing, contradicting its strictly negative test pairing.

This proves the exact quantified lower bound without assuming nondegenerate coefficient intervals and without establishing the original unrestricted target.

## Per-claim disposition summary

- **SUPPORTED:** Actual-member corners, positive coefficient scales, atom merging/removal, strict moments and test pairing — S1 LF 11–15, 30–31.
- **SUPPORTED after explicit genericity/cross-member proof:** Bands, phase constraints and all placements — LF 19–26.
- **SUPPORTED in writing:** Oriented-subsequence lemma, non-strict extension, \(m<5\) exclusion and complete three-word classification — LF 33–38.
- **SUPPORTED with \(\mu\), not signed \(y\), as cone variable:** Eight-ray completeness and monotone \(q\) — LF 42–46.
- **SUPPORTED by corrected all-variable arguments:** Every outside-band vertex, endpoint and variable-leading scale — LF 50–59.
- **SUPPORTED in writing:** All first-gap C vertices, including direct positivity of both formerly K2 partial pairs — LF 63–71.
- **SUPPORTED after sign/gap/order corrections:** Every first-odd-band tail — LF 75–85.
- **REFUTED literally, repaired here:** Scale correction sign at LF 59; clearing expansion and symmetric identity at LF 71; gap/order statements at LF 83/85; reciprocal band equalities at LF 89.
- **Additional MINOR literal corrections:** \(y\)-vector versus \(\mu\) at LF 42; fourth-node signs at LF 51; lower-\(k\) quadratic sums and negative-\(W\) inequality direction at LF 59; unnecessary false product bound at LF 67; \(F(A)\le0\) at LF 75; raw/compactified weight convention at LF 89.
- **INCONCLUSIVE:** K1 count 676 in S1 LF 38/S2 LF 9; all eight K2 coefficient-positivity/count/hash assertions and point-check receipts in S1 LF 71/S3 LF 1–129.
- **SUPPORTED by reconstruction, not approved as frozen text:** Lower-bound theorem and assembly — S1 LF 5, 97.
- **OUT OF SCOPE / NOT PROVED:** Six-or-more-node certificate existence, unrestricted synthesis-or-obstruction target, novelty, and stronger certificate searches.

## Actual read, execution and assurance receipt

1. **Administrative reads before mathematics:** `memory://root/memory_summary.md` in default display, with a truncation notice—not claimed as a complete raw scientific-source read; `skill://aifours-written-math-acceptance-protocol`; `skill://independent-snapshot-review`. No external-model workflow was launched.
2. **Manifest:** Complete raw `manifest-v1.json`, opening through closing brace, before mathematics. Declared pin: SHA-256 `6af2c6c24c3f9493ac3fec94256599e38f33a5d09c810411a66e061f361c0131`; 5958 bytes, 94 LF.
3. **Packet:** Complete raw, unelided windows **1–40, 41–80, 81–120, 121–165, 166–210, 211–255**, all read before mathematical consideration. Actual source-label coverage: **S1 LF 1–101, S2 LF 1–16, S3 LF 1–129**, including every ending and closing brace. No packet text was skipped or accepted from a truncation marker.
4. **Declared packet pin:** SHA-256 `0132ac8c0eb77a4bc6a161020b754fe5a098a800dcc51c93ade482e5dacd95b9`; 32992 bytes, 255 LF. Source pins observed in manifest/packet:
   - S1: `e223cb4407051bed6b2ab07661ac70f0cba43308723b0a9e4d51efb539cfcab6`
   - S2: `84fdaf7e1045bb746e491b8c46ea2ce8babb4900c7589ef7abeb5d51cfd85c44`
   - S3: `5ccaf9f8c68f425f8682c13dfb73d06d3205fd29cdcbc6aa632f4968ac0ab88b`
   
   These are observed declared pins, **not independently recomputed hashes or byte/LF counts**.
5. No original source outside the packet was opened. Neither author kernel body was read, imported or executed. No slice B output, sibling review, ancestry source or existing review was read.
6. **Scientific executions: zero. Hash/count executions: zero. Native clock calls: zero.** No reviewer-native timestamp, process exit code, OS resource enforcement, numerical control, expansion or formal replay is asserted. All mathematical calculations here are written all-variable reasoning.
7. No network, external model, Git, deletion, infrastructure operation, certificate search, build, lint, test or formatter was performed.
8. **Output attempt:** One `functions.write` call attempted the assigned `review-A-v1.md` path with the complete report. The tool refused because it permits only `xd://` transport and `local://` scratch writes. **No repository file or alternate artifact was created.** This complete report is returned for parent materialization; no bypass was attempted.
9. **Assurance:** Same-harness mathematical review only. No human review, independent-family gate, formal/kernel verification, novelty clearance or parent adoption is claimed. Owner receipts are not trusted premises. Incorporating these proof repairs requires an explicit parent disposition; this report does not silently edit or retroactively clear frozen S1/S2/S3.