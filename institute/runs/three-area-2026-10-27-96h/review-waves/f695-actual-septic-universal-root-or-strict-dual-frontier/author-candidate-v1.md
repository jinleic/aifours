# Author candidate: an exact four-corner SDP and finite zero-dual frontier for actual septic boxes

**Status: AUTHOR-WRITTEN CANDIDATE, not yet independently reviewed or parent-dispositioned.** The original universal both-parity common-SPR/ROOT statement is **NOT PROVED**; no eligible counterexample or all-eight-strict-negative certificate is supplied. The results below give an exact per-box alternative for that original strict synthesis problem, an eight-block finite semidefinite formulation, an exact all-member eligibility criterion, and a bounded actual-corner obstruction. They do not decide the remaining universal sentence.

## 1. Original target and physical rows

Let
\[
K=\{s^7+\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\}
\]
be an independent compact real coefficient box, with degenerate intervals permitted and **every member strictly Hurwitz**. Both parities may vary. The target is one monic stable septic \(Q\), chosen before both \(a\in K\) and \(t\ge0\), such that \(Q/a\) is strictly positive real for every actual member.

Write
\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
\(a(i\omega)=E_a(t)+i\omega O_a(t)\), \(t=\omega^2\). For \(Q(s)=\sum_{j=0}^7q_js^j\), with \(q_7=1\), put
\[
F_Q=q_0-q_2t+q_4t^2-q_6t^3,\quad
G_Q=q_1-q_3t+q_5t^2-t^3,
\quad P_{Q,a}=F_QE_a+tG_QO_a.
\]
The exact ascending-coefficient raw row is
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a),\quad Q\cdot r_a=P_{Q,a}.
\]
No other row normalization or freely chosen root markers are used. The compactified row is \(\widehat r_a(t)=r_a(t)/(1+t)^7\); its limits at \(0\) and \(\infty\) are respectively \(a_0e_0\) and \(e_7\).

For such an eligible compact box, strict common synthesis is equivalent to the existence of one monic \(Q\) and \(\eta>0\) with
\[
P_{Q,a}(t)\ge\eta(1+t)^7\quad\text{for every }a\in K,\ t\ge0. \tag{1}
\]
Indeed, a strict common numerator has this uniform margin by compactifying \(t\) and using compactness of \(K\), including the positive limit \(1\) at infinity. Conversely, (1) itself implies \(Q\) is Hurwitz: for one fixed strictly Hurwitz \(a_*\in K\), \(Q/a_*\) is analytic on the closed right half-plane, tends to \(1\) at infinity, and has strictly positive real boundary values. The harmonic minimum principle gives positive real part in the open half-plane, excluding zeros of \(Q\) there; (1) excludes imaginary-axis zeros. Thus stability of the one numerator is a conclusion, not a separately assumed or slice-wise choice.

## 2. Four fixed actual corners suffice for a fixed numerator

Define actual coefficient corners \(C_{\sigma\tau}\), \(\sigma,\tau\in\{-,+\}\), by the even and odd endpoint patterns
\[
\begin{array}{c|cccc}
\sigma&(a_0,a_2,a_4,a_6)\\\hline
-& (\ell_0,u_2,\ell_4,u_6)\\
+& (u_0,\ell_2,u_4,\ell_6)
\end{array}
\qquad
\begin{array}{c|ccc}
\tau&(a_1,a_3,a_5)\\\hline
-& (\ell_1,u_3,\ell_5)\\
+& (u_1,\ell_3,u_5).
\end{array}
\]
All four have leading coefficient \(1\); they may coincide when intervals are degenerate. For **every** \(t\ge0\), their parity polynomials are the actual endpoints
\[
E_-=\ell_0-u_2t+\ell_4t^2-u_6t^3,\quad
E_+=u_0-\ell_2t+u_4t^2-\ell_6t^3,
\]
\[
O_-=\ell_1-u_3t+\ell_5t^2-t^3,\quad
O_+=u_1-\ell_3t+u_5t^2-t^3.
\]
The endpoint labels do not change with positive \(t\). Coefficient independence makes the actual parity-value set exactly \([E_-,E_+]\times[O_-,O_+]\). At each fixed frequency, a physical row of any member is a convex combination of the four corresponding actual-corner rows. The combination may depend on \(a,t\); this does **not** claim that \(K\) is the convex hull of four polynomials.

Consequently, for the **same** \(Q,\eta\), (1) holds on the entire box if and only if it holds for all four \(C_{\sigma\tau}\) and all \(t\ge0\). This is an exact all-member physical-pairing reduction, not an inference that stability of an arbitrary collection of corners proves stability of the box.

## 3. Exact per-box compact and finite dual alternatives

For the four fixed actual corners define the compact subset of \(\mathbb R^8\)
\[
S_K=\{\widehat r_{C_{\sigma\tau}}(t):\sigma,\tau\in\{-,+\},\ 0\le t\le\infty\},
\quad H_K=\operatorname{conv}S_K.
\]

**Theorem A.** For every eligible \(K\), the original strict common-SPR target for this same \(K\) is equivalent to \(0\notin H_K\). Equivalently, failure of that target is witnessed by an identity
\[
\sum_{i=1}^{m}w_i r_{C_i}(t_i)+\lambda e_0+\mu e_7=0, \tag{2}
\]
where \(m\ge1\), each \(C_i\) is one of the four actual corners above, \(t_i>0\), \(w_i>0\), \(\lambda,\mu\ge0\), and
\[
m+\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}\le9. \tag{3}
\]
The squared frequencies and the corner choices are actual, not arbitrary ordered root markers. Repetitions are allowed.

**Proof.** If (1) holds, the normalized pairing is at least \(\eta\) on \(S_K\), so its convex hull cannot contain zero. Conversely, if \(0\notin H_K\), the compact convex set \(H_K\) has a nonzero point \(z\) of minimum norm. For every \(v\in H_K\), the projection inequality gives \(z\cdot v\ge\|z\|^2>0\). Since \(e_7\in S_K\), \(z_7\ge\|z\|^2>0\). Normalize the polynomial with coefficient vector \(z\) by \(z_7\); it satisfies (1) with one positive margin. Section 1 proves that this numerator is Hurwitz and works for every member.

If \(0\in H_K\), Carathéodory's theorem in \(\mathbb R^8\) gives a convex representation with at most nine points of \(S_K\). Replace each positive finite-frequency normalized row by the same actual raw row with its weight divided by \((1+t)^7\). All zero-frequency contributions combine into \(\lambda e_0\); all infinite-frequency contributions combine into \(\mu e_7\). This yields (2)–(3), with at least one positive finite-frequency atom, since \(\lambda e_0+\mu e_7\) alone cannot vanish nontrivially. Conversely, divide each finite atom of (2) by its positive normalization in reverse and represent \(\lambda e_0\), when present, by the \(t=0\) row of any actual corner, whose constant coefficient is positive. Together with the \(t=\infty\) row, normalization of these positive coefficients gives \(0\in H_K\). ∎

**Important distinction.** (2) is a genuine exact per-box obstruction to a **strict** common numerator, but it is **not** an all-eight-strict-negative finite-frequency certificate. Its six middle raw coordinates sum to zero, and the endpoint coordinates sum to \(-\lambda,-\mu\). The endpoint symbols are compactification contributions, not invented positive-frequency atoms. No actual box satisfying (2) is claimed here. The frozen buffered universal equivalence/conditional strict-negative normal form is not replaced by a false same-box implication.

## 4. Eight explicit 4-by-4 semidefinite blocks

Let \(v(t)=(1,t,t^2,t^3)^T\). For each of the four actual corners form
\[
p_{\sigma\tau}(t)=P_{Q,C_{\sigma\tau}}(t)-\eta(1+t)^7.
\]
Its degree is at most seven, and its coefficients are affine in \(q_0,\ldots,q_6,\eta\) for fixed box endpoints. The original strict common-SPR target on an eligible \(K\) holds **if and only if** there are one common vector \(q_0,\ldots,q_6\), one \(\eta>0\), and eight real symmetric positive semidefinite \(4\times4\) matrices \(M_{\sigma\tau},N_{\sigma\tau}\) such that
\[
p_{\sigma\tau}(t)=v(t)^T M_{\sigma\tau}v(t)+t\,v(t)^T N_{\sigma\tau}v(t)
\quad\text{for all }\sigma,\tau. \tag{4}
\]
This is a finite-dimensional LMI feasibility problem: 88 real existential scalar variables (seven free nonleading numerator coefficients, \(\eta\), and 80 independent symmetric-matrix entries), 32 coefficient equalities, and eight PSD constraints. The same numerator and margin appear in all four equalities. The coefficients in (4), not numerical samples, must match identically.

**Proof of the half-line representation used in (4).** If (4) holds, each \(p\) is nonnegative for \(t\ge0\). Conversely, let any real \(p\) of degree at most seven satisfy \(p(t)\ge0\) for \(t\ge0\). The real polynomial \(g(x)=p(x^2)\) is globally nonnegative and has degree at most 14. Factoring its complex roots, with real roots of even multiplicity, gives \(g=A(x)^2+B(x)^2\) for real \(A,B\) of degree at most seven; the zero polynomial is immediate. Write \(A=A_e(x^2)+xA_o(x^2)\) and similarly for \(B\). Averaging the representations at \(x\) and \(-x\) gives
\[
p(t)=A_e(t)^2+B_e(t)^2+t\bigl(A_o(t)^2+B_o(t)^2\bigr),
\]
where all four polynomials have degree at most three. Their coefficient outer products give PSD Gram matrices. Combining this equivalence with the exact four-corner reduction proves (4), and Section 1 pays numerator stability. ∎

For rational endpoints, if the strict target holds, the numerator, positive margin, and all eight Gram matrices may in fact be chosen rational, with the matrices positive definite. To see this, first approximate the feasible numerator rationally and choose a smaller positive rational margin; compactification preserves a strictly positive residual for all four corners. Subtract a sufficiently small rational multiple of \((1+t)\sum_{j=0}^3t^{2j}\) and apply the representation just proved; adding that multiple of the identity to each of its two Gram matrices makes both positive definite. In each coefficient equation, one diagonal entry of \(M\) controls one even power and one diagonal entry of \(N\) controls one odd power. Approximate the off-diagonal entries rationally and solve those diagonal equations exactly; sufficiently close approximations preserve positive definiteness. Thus a rational positive certificate can be checked by exact coefficient equalities and exact principal-minor signs. This is an existence argument, not a submitted or executed checker.

For rational endpoints, a no-numerator obstruction (2), if one exists, can likewise be chosen with real-algebraic \(t_i,w_i,\lambda,\mu\): its bounded finite list of corner-label choices gives an existential polynomial system over \(\mathbb Q\), and the real-algebraic numbers form a real closed field. Its algebraic quantities could be represented by defining polynomials and isolating data. Again, no such witness is supplied or asserted to exist.

## 5. Exact all-member eligibility, without a corner-stability shortcut

For arbitrary endpoints with \(\ell_j\le u_j\), let the center coefficients and halfwidths be \(b_j=(\ell_j+u_j)/2\), \(h_j=(u_j-\ell_j)/2\), and put
\[
E_b=b_0-b_2t+b_4t^2-b_6t^3,\quad
O_b=b_1-b_3t+b_5t^2-t^3,
\]
\[
H_E=h_0+h_2t+h_4t^2+h_6t^3,\qquad
H_O=h_1+h_3t+h_5t^2.
\]
Let \(B(s)=s^7+\sum b_js^j\). Then **every member** of the box is strictly Hurwitz if and only if all three statements hold:

1. the center \(B\) is strictly Hurwitz;
2. \(\ell_0>0\);
3. there is no \(t>0\) with both \(E_b(t)^2\le H_E(t)^2\) and \(O_b(t)^2\le H_O(t)^2\).

Necessity follows because, at \(t>0\), the actual complex-value set is the product rectangle centered at \((E_b,\sqrt t\,O_b)\) with the stated halfwidths; simultaneous inequalities place zero in that rectangle and hence produce an **actual** imaginary-axis zero. At \(t=0\), \(a_0=0\) is possible exactly when the positive center's constant interval reaches zero. Conversely, these three statements rule out an imaginary-axis zero for every actual member at every real frequency. The segment from the stable center \(B\) to any member remains in the independent box. Continuity of roots for monic polynomials then prevents any root from leaving the open left half-plane: such an exit would require an imaginary-axis crossing; roots cannot escape to infinity along this bounded monic segment. Hence every member is Hurwitz.

This is an exact condition, including equality/tangency and degenerate intervals. Center stability can be expressed by the seven strict Hurwitz determinants: with \(d_0=1,d_1=b_6,\ldots,d_7=b_0\), \(d_k=0\) outside \(0\le k\le7\), define \(H_{ij}=d_{2j-i}\) for \(1\le i,j\le7\); the seven leading principal determinants must be positive. Thus the eligibility condition is an explicit first-order real-polynomial formula, not a claim that checking the four corners alone is an all-member proof.

## 6. Relation to the actual ROOT/all-ray caller and the remaining universal step

Suppose an eligible box has nondegenerate odd uncertainty, and (4) is feasible. The resulting one stable \(Q\) has all coefficients strictly positive. For any positive finite collection of actual rows whose four signed odd coordinates sum componentwise to at most zero,
\[
M_{\rm odd}=\sum_iw_i(t_iO_i,-t_i^2O_i,t_i^3O_i,-t_i^4O_i)\le0,
\]
(1) yields
\[
\sum_iw_iF_Q(t_i)E_i(t_i)
=\sum_iw_iP_{Q,a_i}(t_i)-(q_1,q_3,q_5,q_7)\cdot M_{\rm odd}
\ge\eta\sum_iw_i(1+t_i)^7>0. \tag{5}
\]
This is simultaneous for every actual R4 omitted-moment case, both actual R5 orientations, zero-odd singletons, same-frequency opposite-odd cancellations, and their positive combinations. There is no per-ray choice of numerator and no division by a zero odd endpoint.

Use the frozen actual-box band import: \(O_-\) has roots \(a,d,e\), \(O_+\) has roots \(b,c,f\), \(0<a<b<c<d<e<f\), and the actual even values have signs \(-,+,-\) on \([a,b],[c,d],[e,f]\). On each band \(O_-\le0\le O_+\). At a band interior, choose two actual corners with the same even endpoint and opposite odd endpoints and positive cancellation weights; at an endpoint with zero odd value, use the actual zero-odd singleton. In either case (5) makes \(F_Q\) have the same strict band sign as the actual even value. Since \(F_Q(0)=q_0>0\), it has one root respectively in \((0,a),(b,c),(d,e)\). Its degree is three with leading coefficient \(-q_6<0\), so these are all its roots and
\[
F_Q(t)=q_6(x-t)(y-t)(z-t),\quad x\in(0,a),\ y\in(b,c),\ z\in(d,e).
\]
For every nonzero actual R4 or either R5 orientation, using its actual minimizing even endpoints \(E_F\), (5) therefore supplies the **same** triple and the homogeneous quantitative bound
\[
\sum_iw_iE_F(t_i)(x-t_i)(y-t_i)(z-t_i)
\ge {\eta\over q_6}\sum_iw_i(1+t_i)^7>0. \tag{6}
\]
The supplied actual-band import is used only within its stated scope. This is a sufficient per-box route from (4) to the full ROOT caller; it does **not** assert that a merely weak ROOT triple implies strict SPR on the same unbuffered box. The frozen universal buffered equivalence remains the basis for relating the universal ROOT, DUAL and SPR assertions.

The entire original universal question is now the following explicit fixed-size real-polynomial sentence: for **all** fourteen real endpoints with \(\ell_j\le u_j\), if the center-determinant and zero-exclusion eligibility conditions of Section 5 hold, then there **exist** the single \(q_0,\ldots,q_6\), \(\eta>0\), and eight PSD matrices satisfying the 32 coefficient equalities in (4). Replace each 4-by-4 PSD constraint by its 15 nonnegative principal minors. This is a first-order sentence over the reals; classical real-closed-field quantifier elimination decides its truth in principle. No quantifier elimination, solver, implementation, running time, verdict, or practical arbitrary-input program is claimed. In particular, merely writing the exact sentence does not establish its truth or produce a counterexample. The unpaid first step is to decide/prove that sentence, or furnish an actual eligible box with (2) and, for the requested strict-negative route, the separately required all-eight-negative actual-corner aggregate and its all-member stability proof.

## 7. Fresh exact diagnostic: both parities vary beyond the displayed scaled-binomial family

This example illustrates the **scope** of the exact condition, not the universal theorem. Take \(Q(s)=(s+1)^7\), and the independent box centered on its coefficients with halfwidths
\[
h_0=9/10,\qquad h_j=1/100\quad(1\le j\le6).
\]
All seven widths are positive. For every member \(a=Q+\sum_{j=0}^6d_js^j\) and \(t=\omega^2\),
\[
\left|Q(i\omega)\overline{\sum d_j(i\omega)^j}\right|
\le(1+t)^{7/2}\sum_jh_j t^{j/2}
\le\left(\frac9{10}+\frac6{100}\right)(1+t)^7
=\frac{24}{25}(1+t)^7.
\]
Hence \(P_{Q,a}(t)\ge(1/25)(1+t)^7\) for every actual member and frequency. The same inequality holds along every segment \(Q+\theta(a-Q)\), \(0\le\theta\le1\). A zero of any segment member on the imaginary axis would make this positive pairing zero. Since \(Q\) is Hurwitz and the segment is monic and bounded, the homotopy proves **all-member** Hurwitz stability. Thus this is a full-width both-parity eligible box with one fixed strict common numerator; no finite scientific program was run.

Its constant interval is \([1/10,19/10]\), whose endpoint ratio is \(19\). Every constant interval in the frozen displayed scaled-binomial sufficient family with \(0<\epsilon<5/6\), regardless of \(\beta>0\), has endpoint ratio \((1+\epsilon)/(1-\epsilon)<11\). Therefore that displayed family cannot even contain this box. This comparison does not claim to exclude every other previously proved thickening or solve arbitrary boxes.

## 8. Coverage, chronology, and assurance boundaries

- I read the assigned manifest, freeze receipt, preprepared metadata, actual dispatch and all 20 listed status/permission controls through their endings before a direct pre-body ACK to Main. The controls were issued in two parallel batches; no serial completion order is claimed. The manifest/freeze SHA-256 values were independently observed as `d7b4de6be80bb2a10d9dc72296aa9511b292ab5c1849cfe909ebca2cc0cb1468` and `9f9f6112f6dcb218d679d8fd6f77fd01d8d3a48490c72367a92a8f1d9d83ecd5`.
- Only after that ACK I read packet LF 1–660 in ordered, nonparallel, raw consecutive windows of at most 20 LF, including the ending. Its independently observed SHA-256 is `cc4597be286dfdc1da42fae1455b6db6bcccec1c20cbab2956e8abc93dd5cc18`. Packet coverage: S1 lines 1–40, S2 lines 1–46, S3 lines 1–39, and S4 logical lines 1–533, all complete as rendered. The S4 source has 532 LF and 533 logical lines. Parent-supplied metadata reports the original source/control hashes and selected-line byte equality; I did not independently re-render the packet or claim source-wide identity authentication.
- Only after the complete packet did I perform the written derivations and the selected exact diagnostic in this document. No public source or packet link was followed; no held episode, held consumer, sibling proof, historical held mathematics or old code was used. No scientific executable, solver, code, test, build, lint, package install, external-model CLI, remote work or background scientific process was run. The sole shell observations were metadata hashes and native clock readings; the clock observed before composing this output was `2026-10-30T16:28:12-0700 PDT`. No experiment result or program is represented as executed.
- Theorem A, the 4-corner LMI, eligibility criterion, quantitative ROOT consequence, and diagnostic remain **author-written claims** for independent checking. They are not a blanket family review, parent disposition, human/kernel/independent-model verification, original-source identity determination, novelty claim, actual strict-negative certificate, or global closure. All held episodes and all their consumers remain NONINPUT; no cognitive-isolation certification or historical backdating is claimed.
