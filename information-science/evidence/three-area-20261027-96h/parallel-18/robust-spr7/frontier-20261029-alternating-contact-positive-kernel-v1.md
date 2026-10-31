# Alternating contacts cannot exclude every positive septic numerator by tangency alone

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 15:19:58 PDT 2026**. **WRITTEN universal linear-algebra theorem candidate; not parent-adopted, independently reviewed, formally verified or novelty-cleared.** It applies directly to the unrestricted numerator coefficient vector, not to a chosen numerator profile. The original robust-SPR synthesis-or-obstruction question remains open.

## 1. Universal theorem

Fix \(k\ge2\), ordered positive nodes \(0<t_1<\cdots<t_m\), and nonzero real pairs \((\alpha_i,\beta_i)\) such that the signs of \(\alpha_i\beta_i\) alternate with \(i\); either initial sign is permitted. Let \(T\) be the \(m\times2k\) matrix
\[
T_{i,2r}=\alpha_i(-t_i)^r,\qquad
T_{i,2r+1}=\beta_i(-t_i)^r,\qquad 0\le r<k.
\]
If \(m\le2k-2\), then \(T\) has full row rank and there is a vector \(b\in(0,\infty)^{2k}\) satisfying \(Tb=0\). If the matrix entries are rational, \(b\) can be chosen rational. The bound is sharp for \(k=4\): §5 gives seven rational nodes and alternating rational signs for which no nonzero \(b\ge0\) is in the kernel.

For \(k=4\), write \(b(s)=\sum_{j=0}^7b_js^j\). The theorem produces a real polynomial with **all eight coefficients strictly positive**, hence exact degree seven, satisfying up to six such alternating linear constraints. It does **not** say that this polynomial is Hurwitz or is an SPR numerator.

## 2. Weak moment sign-variation lemma

Let \(0<t_1<\cdots<t_m\), let \(z_i\in\mathbb R\) not all vanish, and suppose
\[
\sum_i z_i(-t_i)^r\ge0\qquad(0\le r<k). \tag{1}
\]
Then the sign sequence of the nonzero \(z_i\), in increasing node order, has at least \(k-1\) sign changes.

Indeed, suppose it has at most \(k-2\). Choose \(k-1\) distinct positive numbers \(r_1,\ldots,r_{k-1}\) so that
\[
q(t)=-\prod_{j=1}^{k-1}(r_j-t)
\]
has the same sign as each nonzero \(z_i\). Put a root before the first nonzero node if its sign is positive; place roots in each sign-changing gap; place any unused roots beyond the last node. This is possible because the number needed before and between nodes is at most \(k-1\). None is a node. Therefore \(\sum_i z_iq(t_i)>0\). But \(-q(t)\) is a **strictly positive-coefficient linear combination** of \(1,-t,\ldots,(-t)^{k-1}\), so (1) gives \(\sum_i z_iq(t_i)\le0\), a contradiction. The argument includes the case when every moment in (1) is zero.

## 3. Proof of the positive-kernel theorem

Suppose \(y\in\mathbb R^m\) is nonzero and \(T^Ty\ge0\). Set \(x_i=\alpha_i y_i\) and \(z_i=\beta_i y_i\). Both sequences have the same nonempty support. The even and odd coordinates of \(T^Ty\) separately give (1), so §2 forces at least \(k-1\) sign changes in **each** nonzero sign sequence.

For consecutive retained indices \(i<j\), let \(g=j-i\). The relative sign \(\operatorname{sgn}(z_h/x_h)=\operatorname{sgn}(\alpha_h\beta_h)\) changes by \((-1)^g\). If \(g\) is odd, exactly one of the two sequences changes sign; if \(g\) is even, either both change or neither does. Thus the number of their combined sign changes over that gap is at most \(g\). Summing over retained gaps gives at most \(m-1\) combined changes. But the required number is at least \(2k-2>m-1\), contradiction.

Hence **no nonzero** \(y\) has \(T^Ty\ge0\), including the case \(T^Ty=0\); in particular \(T\) has full row rank. Let \(L=\operatorname{im}T^T\). The closed subspace \(L\) is disjoint from the standard nonnegative simplex. Finite-dimensional strict separation of that simplex and \(L\) gives \(b\perp L\) with \(b_j>0\) for all \(j\), hence \(Tb=0\). If \(T\) is rational, rational Gaussian elimination gives a rational basis for its kernel; rational points are dense in that real kernel, so strict positivity persists for some rational \(b\).

## 4. Direct boundary-contact consequence for the septic task

For a real septic \(a\), put \(a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t)\) and
\[
P_{a,b}(t)=E_a(t)E_b(t)+tO_a(t)O_b(t).
\]
At a positive simple imaginary-axis boundary contact where \(E_a(t_i)=O_a(t_i)=0\),
\[
P'_{a,b}(t_i)=E_a'(t_i)E_b(t_i)+t_iO_a'(t_i)O_b(t_i). \tag{2}
\]
Consequently, the necessary tangency equations \(P'_{a_i,b}(t_i)=0\) have the matrix form of §1 with \(\alpha_i=E_{a_i}'(t_i)\) and \(\beta_i=t_iO_{a_i}'(t_i)\).

For the common five-contact ordering of the six interleaved parity-root bands, the contacts occur between successive bands. If the relevant even and odd endpoint roots at those contacts have ordinal pairs
\[
(1,1),\ (2,1),\ (2,2),\ (3,2),\ (3,3),
\]
then the product signs of their simple cubic derivatives are \((+,-,+,-,+)\): the sign of a cubic \(\prod_j(r_j-t)\) derivative at its first, second and third roots is respectively \((- ,+,-)\), independent of its positive scale. Hence §1 supplies a strictly positive-coefficient exact-degree-seven polynomial satisfying **all five tangency equations simultaneously**, for every such contact geometry and every nonzero derivative magnitudes.

Therefore an argument that only imposes these alternating contact equalities plus nonnegative numerator coefficients cannot prove an unrestricted negative septic-box verdict: it must also use a genuinely independent condition, such as whole-frequency nonnegative pairing, contact curvature/sign, or actual finite atom inequalities. No arbitrary-box synthesis follows from the positive tangent solution. Contact positivity, inward transfer to a stable box, all-frequency strictness, and the original conclusion remain to be established separately.

## 5. Sharp abstract seven-node example

Take \(k=4\), \(m=7\), \(t_i=i\), \(\alpha_i=1\), and set \(\beta_i=Y_i/X_i\), where
\[
X=(14/5,\ 1/10000,\ 1/10000,\ 1/10000,\ -14,\ 96/5,\ -7),
\]
\[
Y=(10,\ -20,\ 15,\ -4,\ -1/10000,\ -1/10000,\ -1/10000).
\]
All \(X_i,Y_i\) are nonzero and \(\operatorname{sgn}(\alpha_i\beta_i)=(+,-,+,-,+,-,+)\). Direct rational arithmetic gives
\[
\min_{0\le r<4}\sum_{i=1}^7X_i(-i)^r=9901/10000>0,\qquad
\min_{0\le r<4}\sum_{i=1}^7Y_i(-i)^r=989/1000>0.
\]
Thus for the row multiplier \(y=X\), **all eight** coordinates of \(T^Ty\) are strictly positive. No nonzero nonnegative kernel vector can exist. This abstract linear-algebra example establishes sharpness of the six-node threshold; it is **not** asserted to come from an actual stable interval box or seven physical septic contacts. Its two finite moment minima were checked using Python `fractions.Fraction` in one Eval host; the universal proof is written mathematics.

## 6. Provenance and residual

Named standard import: strict separation of a compact convex simplex from a disjoint closed subspace, plus rational Gaussian elimination. The moment lemma, rank, sign-variation bound and boundary differentiation are explicitly proved above. The five-contact root-order application uses only the displayed simple-root derivative signs. No earlier unreviewed claim, held historical source, or external model is a premise. Parent-classified incidental search-display exposure is carried in `owner-incidental-held-source-search-display-v1.json`; no clean-cognition assertion is made.

The theorem rules out a tangency-only negative argument, not an original counterexample. For the original unrestricted target, a surviving tangent polynomial must still satisfy the whole continuum of four-corner pairings and the exact-degree/septic stability requirements; conversely, an actual negative certificate must use additional information beyond these contact equations. No formal proof, independent scientific review, publication or novelty claim follows.
