# F784: same-box edge compression and the six-to-eight barycentric frontier

**Status: NONBLIND, SAME-HARNESS GENERAL AUTHOR; written candidate only.** I independently reconstruct the edge compression, every sparse endpoint pattern, the interpolation coefficients, and the coupled positive-weight equivalence. I also give (i) an exact determinant-only elimination of the node weights and edge-mixture parameters, including the exact minimum number of finite atoms at the prescribed nodes; (ii) endpoint-sensitive polynomial root/physical-band occupancy inequalities; and (iii) a two-corner support condition without the additional singleton assumption. These are written arguments, not executed output or an adoption. Neither feasibility nor infeasibility of the surviving eligible systems is established. The prior five-frequency theorem and the compact-hull/strict-SPR alternative remain explicit imports at the places stated below.

The native UTC clock observed before composing this return was **2026-10-31T01:21:10Z**. It is an observation before creation, not a claimed creation time or research-start time.

## 1. Object, eligibility, and zero relation

Fix one nonempty compact independent coefficient box of monic real septics
\[
K=\{s^7+\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\},
\]
with **every actual member strictly Hurwitz**, including degenerate intervals. At \(t=\omega^2>0\), let
\[
E_a=a_0-a_2t+a_4t^2-a_6t^3,\quad O_a=a_1-a_3t+a_5t^2-t^3,
\]
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
Write the center and halfwidths as \(b_j,h_j\), and put
\(H_E=h_0+h_2t+h_4t^2+h_6t^3\), \(H_O=h_1+h_3t+h_5t^2\). The actual pairs at fixed \(t\) fill exactly
\[
R(t)=[E_b-H_E,E_b+H_E]\times[O_b-H_O,O_b+H_O].
\]
Its four vertices are supplied by the four **fixed physical parity corners** of this same box. This is a pointwise row statement, not a four-polynomial convex-hull description of the coefficient box. The rectangle excludes \((0,0)\): otherwise independence realizes an actual polynomial with an imaginary-axis root. It follows that at least one of its four scalar inequalities \(E_->0,E_+<0,O_->0,O_+<0\) holds at every positive \(t\).

For reference, eligibility can be kept in the exact original form above. Equivalently, as also stated in S5, it is: the center is Hurwitz, \(\ell_0>0\), and no positive \(t\) has both \(|E_b(t)|\le H_E(t)\) and \(|O_b(t)|\le H_O(t)\). The nontrivial direction follows by the straight coefficient segment from the center to any member: it stays in the box, cannot acquire a zero-frequency or nonzero imaginary-axis root, and its monic roots remain bounded and continuous. This does **not** replace all-member eligibility by stability of the four corners.

Consider a nontrivial actual-corner relation
\[
\sum_{j=1}^m w_j r_{C_j}(t_j)+\lambda e_0+\mu e_7=0,
\quad w_j,t_j>0,\quad\lambda,\mu\ge0. \tag{1}
\]
At least one finite atom occurs. Group equal frequencies as \(0<v_1<\cdots<v_n\), with \(W_i>0\) and one actual averaged pair \((E_i,O_i)\in R(v_i)\) at each node. Put
\(X_i=W_iE_i\), \(Y_i=W_iv_iO_i\), and \(z=\mathbf 1_{\lambda>0}+\mathbf 1_{\mu>0}\). The exact eight coordinates of (1) are
\[
\sum_i X_i=-\lambda,\quad \sum_i X_iv_i^k=0\;(k=1,2,3),\qquad
\sum_iY_iv_i^k=0\;(k=0,1,2),\quad\sum_iY_iv_i^3=\mu. \tag{2}
\]
At every node the two parities are from the **same** member, and neither may be divided away merely because it could be zero.

If an entire parity is fixed, (1) is impossible. For example, with odd part fixed at \(O_b\), pair (1) with the odd-center test to obtain a sum of \(W_iv_iO_b(v_i)^2\) plus \(\mu\), all nonnegative. All must vanish. At each such node the actual even interval avoids zero, so pairing with the even-center test gives a strictly positive sum plus \(\lambda b_0\ge0\), a contradiction. Interchange parities for fixed even. Thus every relation under discussion has positive pointwise widths in **both** parities; the nondegenerate rectangle used below is justified even when other coefficient intervals are degenerate.

## 2. Exact radial compression, with unchanged full aggregate

At node \(i\), let the original positive group have weight \(W\) and average pair \(p=(E,O)\ne0\). The intersection of the ray \(\{sp:s\ge1\}\) with the compact rectangle \(R(v_i)\) has a finite maximum \(s_*>0\). The point \(s_*p\) is on a rectangle edge, hence a convex combination \(\theta c+(1-\theta)d\) of its two **adjacent physical vertices**. Replace the entire group by these vertices with respective weights \(W\theta/s_*\) and \(W(1-\theta)/s_*\), omitting zero coefficients. The weighted pair remains exactly \(Wp\), and therefore all eight coordinates of its row aggregate remain exactly unchanged. The endpoint terms, box, and finite frequency are unchanged; weights remain positive. A group that originally used one corner may simply be left alone, and any group with at least two atoms becomes at most two. This proves adjacent-edge compression without increasing the finite atom count or inventing a new box. It need **not** preserve the total group weight: it preserves the weighted pair and complete row aggregate.

Consequently an edge-compressed representation at \(n\) nodes has \(n+M\) finite atoms, where \(M\) counts its genuinely two-corner groups. If \(n+M+z\le8\), the exhaustive cases are

| n | endpoint pattern | z | maximum M | minimum single-corner groups |
|---:|---|---:|---:|---:|
| 6 | \(\lambda=\mu=0\) | 0 | 2 | 4 |
| 6 | \(\lambda>0,\mu=0\) or \(\lambda=0,\mu>0\) | 1 | 1 | 5 |
| 6 | \(\lambda>0,\mu>0\) | 2 | 0 | 6 |
| 7 | \(\lambda=\mu=0\) | 0 | 1 | 6 |
| 7 | \(\lambda>0,\mu=0\) or \(\lambda=0,\mu>0\) | 1 | 0 | 7 |
| 8 | \(\lambda=\mu=0\) | 0 | 0 | 8 |

The restriction \(n\ge6\), and the existence of some representation with at most eight total compactified atoms when any zero dual exists, use the imports identified in Section 7. This table concerns a chosen sparse representation; an arbitrary original presentation need not have at most eight atoms.

## 3. Exact interpolation constraints, including all endpoint patterns

Let
\[
H(t)=\prod_{i=1}^n(t-v_i),\quad P=\prod_i v_i,\quad d=n-4,\quad D_i=H'(v_i).
\]
For \(n\ge4\), (2) is equivalent to the existence of **unique** real polynomials \(A,B\), each of degree at most \(d\), satisfying
\[
X_i=\frac{A(v_i)}{v_iD_i},\quad Y_i=\frac{B(v_i)}{D_i},\qquad
A(0)=(-1)^n\lambda P,\quad [t^d]B=\mu. \tag{3}
\]
To see this, interpolate \(v_iX_iD_i\) and \(Y_iD_i\) by polynomials of degree at most \(n-1\). The first three zero moments successively remove their top three coefficients, leaving degree at most \(n-4\). Conversely these degree bounds imply those moments by the Lagrange identity \(\sum_i v_i^k/D_i=0\) for \(k\le n-2\). Evaluating the interpolation for \(A\) at zero gives \(A(0)=-H(0)\sum_iX_i=H(0)\lambda=(-1)^n\lambda P\). For \(B\), the third moment is its \(t^d\) coefficient. No assumption that \(X_i\) or \(Y_i\) is nonzero is used.

In particular, with unspecified real lower coefficients, the full sparse coefficient constraints are
\[
\begin{array}{lll}
n=6:& A=\lambda P+a_1t+a_2t^2,& B=b_0+b_1t+\mu t^2;\\
n=7:& A=-\lambda P+a_1t+a_2t^2+a_3t^3,& B=b_0+b_1t+b_2t^2+\mu t^3;\\
n=8:& A=\lambda P+a_1t+a_2t^2+a_3t^3+a_4t^4,& B=b_0+b_1t+b_2t^2+b_3t^3+\mu t^4.
\end{array} \tag{4}
\]
The table in Section 2 sets \(\lambda,\mu\) to zero or strictly positive for each allowed row. In particular both are zero for \(n=8\), and at least one is zero for \(n=7\). These are coefficient identities, not merely degree bounds or sign conventions.

The coupled physical requirement at node \(i\) is exactly
\[
(A(v_i),B(v_i))=v_iD_i W_i(E_i,O_i),\qquad W_i>0,\quad(E_i,O_i)\in R(v_i). \tag{5}
\]
The **same** positive \(W_i\) multiplies both parities. Necessity follows from (3); conversely (3) and (5) give all eight moment equations. Cross-multiplication alone is not enough: \((A,B)\) may be antiparallel to an actual corner, which passes a zero-determinant test but requires a negative weight. Section 4 gives an exact sign-sensitive replacement, with no undetermined \(W_i\) or mixture coefficient.

## 4. Exact determinant/positive-weight elimination and minimal atom count

This section is a direct written reduction of the coupled frontier. It is not a claim that its conditions hold for an eligible box.

For each node, list its four physical vertex vectors \(c_{i,1},\ldots,c_{i,4}\). Let
\[
\delta_i=(-1)^{n-i}=\operatorname{sgn}D_i,\qquad T_i=\delta_i(A(v_i),B(v_i)).
\]
Choose a linear functional \(h_i\) which is strictly positive on the entire actual rectangle: for example choose \(h_i(E,O)=E\) if \(E_->0\), \(-E\) if \(E_+<0\), otherwise \(O\) if \(O_->0\), otherwise \(-O\). Eligibility guarantees one of these cases. Put
\[
\Delta_{i,c}=\det(c,T_i),\quad
j_i=\begin{cases}0,&\text{some }\Delta_{i,c}=0,\\1,&\text{none is zero.}\end{cases}
\]
The exact node condition is
\[
h_i(T_i)>0,\qquad \min_c\Delta_{i,c}\le0\le\max_c\Delta_{i,c}. \tag{6}
\]
For a fixed eligible \(K\), ordered distinct positive nodes, and polynomials satisfying (3), there is a same-box relation with those prescribed grouped moments and **at most eight total finite-plus-endpoint atoms** if and only if (6) holds at every node and
\[
n+z+\sum_{i=1}^n j_i\le8. \tag{7}
\]
More precisely, \(n+\sum_i j_i\) is the exact least possible number of finite corner atoms among representations preserving these nodes and their full eight-coordinate grouped contributions.

**Proof.** If (5) holds, then \(T_i=v_i|D_i|W_i(E_i,O_i)\), a positive multiple of a point of the rectangle, so \(h_i(T_i)>0\). Expanding that point in the four vertices gives a positive convex combination of the \(\Delta_{i,c}\) equal to zero, proving the determinant inequalities. Conversely, if (6) holds and some determinant vanishes, the corresponding vertex is a **positive**, not negative, scalar multiple of \(T_i\), because both have strictly positive \(h_i\). If no determinant vanishes, two vertex determinants have strict opposite signs. A convex combination \(p\) of those vertices has \(\det(p,T_i)=0\); strict positivity of \(h_i\) again gives \(T_i=\gamma p\) for some \(\gamma>0\). Moving along that ray to its farthest intersection with the rectangle makes \(p\) an adjacent-edge combination, adjusting \(\gamma\) but not \(T_i\). In either case put \(W_i=\gamma/(v_i|D_i|)>0\); then (5) holds for both parities simultaneously.

If some determinant vanishes, one corner suffices at that node. If none does, no one-corner positive representation can have the required direction, while the preceding construction uses two adjacent corners. Since a finite row at a fixed node determines its weighted even and odd pair, the groups cannot be merged across distinct nodes without changing the prescribed grouped contributions. Thus the exact minimum is \(n+\sum j_i\), and (7) is both necessary and sufficient. Equality in (6), a zero of one parity, endpoint atoms, and actual corner coincidences caused by unrelated degenerate coefficient intervals are all retained. The determinant conditions alone, without \(h_i(T_i)>0\), do not imply positive weights. □

For the six-node/no-endpoint parametrization in Section 6, all \(T_i\) depend on the **same** scalars \(c_E,c_O\), not six separately chosen signs. Condition (6) automatically supplies one common positive local weight for E and O; it does not allow two independently optimized parity boxes or two unrelated mixture parameters.

## 5. Physical-band root allocation and every endpoint pattern

I use the classical strict Hermite–Biehler interlacing theorem. With both parities varying, the actual zero-availability sets are three disjoint compact bands for each parity, in strict order
\[
I^E_1<I^O_1<I^E_2<I^O_2<I^E_3<I^O_3. \tag{8}
\]
Briefly, the center roots interlace, and varying one parity to its two actual endpoint functions while holding the other at center shows that the two envelope roots straddle each center root. An even and an odd band cannot touch, including endpoints, because the same actual rectangle would then contain zero. Outside the bands each parity follows the ordinary four-block sign progression \(+,-,+,-\).

Neither \(X\) nor \(Y\) is identically zero: if all even values vanish, all odd values have the strictly nonzero center sign, and the odd-center test contradicts (1); the other case is symmetric. Deleting zeros **only for sign counting**, each sequence has at least three sign changes: otherwise a polynomial of degree at most two, with roots in the change gaps, gives strictly one-signed moment pairing with \(v_iX_i\) or with \(Y_i\). If there are exactly three changes, pairing with the monic cubic having roots in those gaps shows that its last sign is positive and its corresponding endpoint coefficient is positive. Thus an absent corresponding endpoint forces at least four changes.

It follows that each parity has an actual strict **reverse pair** in one of its own bands: negative then positive in a downward band 1 or 3, or positive then negative in upward band 2. Otherwise its sign word would be a subsequence of \(+,-,+,-\), with at most three changes and a negative final sign when there are three. The two reverse pairs are in disjoint bands and hence use four distinct physical groups. Their nodes are strictly inside their band: its endpoint signs exclude a reverse endpoint. The opposite parity is strictly nonzero with constant sign throughout that band.

Let \(N^O=\sum_{j=1}^3\max(0,k^O_j-1)\), where \(k^O_j\) is the number of sampled nodes in the closed odd band \(I^O_j\). Define \(N^E\) analogously. Let \(q_E=\#\{i:E_i=0\}\), \(q_O=\#\{i:O_i=0\}\). The reverse pairs guarantee \(N^O,N^E\ge1\), and eligibility gives no simultaneous E/O zero. The following sharper necessary constraints hold for every grouped relation with \(n\ge4\):
\[
q_E+N^O\le d-\mathbf1_{\lambda=0},\qquad
q_O+N^E\le d-\mathbf1_{\mu=0}. \tag{9}
\]
**Proof.** Within one odd band all actual E values have one strict sign. For each pair of consecutive sampled nodes in it, \(X\) keeps that sign, while \(D_i\) changes sign. Hence the numerator \(A\) changes sign across that node gap and has an odd-multiplicity positive root in it. Such gaps are disjoint, including across different odd bands. Every sampled E-zero is an additional distinct positive root of \(A\), and cannot occur in an odd band. If \(\lambda=0\), the further distinct root \(A(0)=0\) also consumes one degree. \(A\) is not identically zero. This proves the first inequality; the second follows by exchanging parities and using \(B\), whose degree is at most \(d-1\) when \(\mu=0\). □

The complete sparse endpoint consequences are as follows; each displayed inequality is in addition to \(N^E,N^O\ge1\) and disjoint E/O zeros.

| n | endpoint pattern | E-root/odd-band budget | O-root/even-band budget |
|---:|---|---|---|
| 6 | \(\lambda=0,\mu=0\) | \(q_E+N^O\le1\) | \(q_O+N^E\le1\) |
| 6 | \(\lambda>0,\mu=0\) | \(q_E+N^O\le2\) | \(q_O+N^E\le1\) |
| 6 | \(\lambda=0,\mu>0\) | \(q_E+N^O\le1\) | \(q_O+N^E\le2\) |
| 6 | \(\lambda>0,\mu>0\) | \(q_E+N^O\le2\) | \(q_O+N^E\le2\) |
| 7 | \(\lambda=0,\mu=0\) | \(q_E+N^O\le2\) | \(q_O+N^E\le2\) |
| 7 | \(\lambda>0,\mu=0\) | \(q_E+N^O\le3\) | \(q_O+N^E\le2\) |
| 7 | \(\lambda=0,\mu>0\) | \(q_E+N^O\le2\) | \(q_O+N^E\le3\) |
| 8 | \(\lambda=0,\mu=0\) | \(q_E+N^O\le3\) | \(q_O+N^E\le3\) |

For instance, \(n=6,\lambda=0\) forces \(q_E=0,N^O=1\): exactly two sampled nodes occupy one odd band, and no other odd band contains two. The symmetric statement holds for \(\mu=0\). In general (9) strengthens the simple bounds \(q_E\le n-5-\mathbf1_{\lambda=0}\), \(q_O\le n-5-\mathbf1_{\mu=0}\) by charging **every** extra node in each opposite-parity band. No existence of any configuration saturating these bounds is claimed.

Each strict reverse pair also requires both endpoint orientations of its own parity somewhere in the original corner support: the negative and positive actual averages inside the band respectively need a negative lower and a positive upper endpoint contribution, with the order reversed for an upward band. Hence, if the **entire** original relation uses only two distinct physical corners, those two must differ in both parity orientations and are diagonal or antidiagonal. This does not require any reverse-pair group to be a singleton, and is only a necessary condition.

## 6. Six-node specializations, zero and nonzero endpoints

For \(n=6,\lambda=\mu=0\), (9) gives \(q_E=q_O=0\) and \(N^E=N^O=1\). Thus each reverse band contains exactly two consecutive sampled nodes, and no other band of that parity contains two. From (4) and the root gaps,
\[
A(t)=c_Et(t-\alpha),\quad B(t)=c_O(t-\beta),\quad c_Ec_O\ne0, \tag{10}
\]
where \(\alpha>0\) lies strictly between the two nodes of the odd reverse pair and \(\beta>0\) lies strictly between those of the even reverse pair. The bands are disjoint, so \(\alpha\ne\beta\). Writing \(k=c_O/c_E\), (5) gives
\[
v_i O_i(v_i-\alpha)=kE_i(v_i-\beta),\qquad
\operatorname{sgn}k=\operatorname{sgn}(\beta-\alpha). \tag{11}
\]
For the sign statement, at the later node of the even reverse pair \(E_i,O_i\) have the same strict sign in all three even bands, and \(v_i-\beta>0\). The odd band containing \(\alpha\) lies wholly on one side of the even band, so \(\operatorname{sgn}(v_i-\alpha)=\operatorname{sgn}(\beta-\alpha)\).

With only \(\lambda=0\), the same argument still gives the first factorization in (10) and its strict odd-band root \(\alpha\). If \(\mu>0\), \(B\) is a quadratic with leading coefficient \(\mu\) and has a sign-changing root \(\beta\) in an even-band sampled-node gap; therefore \(B(t)=\mu(t-\beta)(t-\gamma)\) for a real \(\gamma\ne\beta\). With only \(\mu=0\), the second factorization in (10) and its strict even-band root \(\beta\) remain; if \(\lambda>0\), \(A(0)=\lambda P>0\) and \(A\) has a sign-changing positive root \(\alpha\) in an odd-band gap. It may be linear, or quadratic with a second distinct real root. When both endpoints are positive, the same existence of an odd-band root of \(A\) and an even-band root of \(B\) follows from (9), with the coefficients fixed by (4). These observations do not assert that any endpoint stratum is feasible.

For \(n=6,\lambda=\mu=0\), equation (11) can alternatively be written using the four physical corner quintics
\[
P_C(t)=k(t-\beta)E_C(t)-t(t-\alpha)O_C(t).
\]
Every singleton group is a root of its physical \(P_C\); an edge group uses the **same** convex mixture on both parity functions and has zero mixture of its two \(P_C\) values. However, these equalities alone omit positive-weight compatibility. Sections 3–4 supply the exact iff including actual same-box eligibility, the global coefficients \(c_E,c_O\), endpoint budget, and positivity.

## 7. Explicit imports and what remains open

For the general \(n\ge6\) assertion I retain the previously adopted import stated in S4: **no all-eight-strict-negative finite actual-member aggregate on an eligible independent box can use at most five distinct positive finite frequencies.** It is not reproved here. In outline, (2) gives \(n\ge4\). If \(n=4\) or 5, compactness and openness allow a sufficiently small eligible enlargement with positive buffers in coefficients 0 and 1. On four distinct grouped nodes, perturb those two coefficients by \(-\varepsilon L_i(-1)/W_i\) and \(-\varepsilon L_i(-1)/(W_iv_i)\), respectively, where \(L_i\) are their Lagrange polynomials. All eight finite aggregate coordinates then decrease by exactly \(\varepsilon\), producing an all-strict-negative aggregate on the **enlargement**, at the same \(n\) nodes, contrary to the import. This is not same-box weak-to-strict conversion.

I separately retain S4's connected compactified-corner-support eight-total-atom reduction. Its consequence is that if any zero dual exists there is a chosen representation covered by Sections 2–6. The zero-hull/strict-SPR alternative is another scoped import from S5/S6: it concerns one monic degree-seven \(Q\) and one positive margin for **all** actual members and frequencies. Any ROOT consequence additionally retains its stated nondegenerate-odd and all-actual-R4/both-R5/zero-odd/cancellation interface. No unlisted linked source was read to establish those imports anew.

The first unpaid mathematical question remains whether **any** eligible box realizes any of the exact determinant and coefficient systems in Sections 2–6, or whether all of them can be excluded. The determinant elimination is a reformulation, not a proof of infeasibility; the band root budgets are necessary, not sufficient. I supply no eligible zero witness, global common numerator, universal SPR or ROOT theorem, counterexample, same-box weak-to-strict theorem, source-identity verification, or novelty claim. No scientific code, interpreter, solver, test, build, formatter, linter, external-model CLI, or network was used; no executable source or parent GO is proposed. Parent whole-read, an independent check and explicit disposition are separate. No human, independent-model-family, formal/kernel, or automatic parent acceptance is asserted.

## 8. Coverage, administrative pins, and sequencing

Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. The sole packet was read serially in raw windows of at most 20 LF, from LF 1 through LF 668 and its ending, before mathematical comparison or research. Every long line appeared in full in its window. Complete rendered source coverage and the parent-frozen SHA-256 pins are:

| ID | R-relative source identifier; complete rendered body | SHA-256 |
|---|---|---|
| S1 | `review-waves/f759-septic-strict-interior-quadrant-refinement-proof-author/independent-reconstruction-v1.txt`, LF 1–157 | `2d253d660505dcdd30d29f94c95eb98da33012477f6d042f48ea792213928ca7` |
| S2 | `review-waves/f760-septic-six-eight-frequency-coupled-frontier-author/author-coupled-frontier-v1.md`, LF 1–165 | `b5a248e86c2cda695851752fd8f364c5644d028c1b9daa343729ef91a67d505a` |
| S3 | `review-waves/f742-septic-two-parity-physical-backtracking-proof-author/author-reconstruction-v1.md`, LF 1–247 | `9cb4340f358000e00cdbb0b83a287e171e140143de9ed7aacd78d1f5a34f3b87` |
| S4 | `dispositions/info-2-actual-septic-eight-atom-zero-dual-six-frequency-and-parity-backtracking-parent-v1.md`, LF 1–39 | `866dd92b58bb2422281abe815bc1e6cae8e5f8f94c96f2d7eaed00bad372a183` |
| S5 | `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1.md`, LF 1–29 | `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b` |
| S6 | `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1-erratum-1.md`, LF 1–5 | `513b44b2591954b535e138df611fab0698af2b8363b89768a5e45f320d50f5d4` |

The source pins and complete-source render/roundtrip are parent metadata, not independently rerendered or authenticated source identities. The sole part `review-waves/f784-septic-coupled-corner-barycentric-author/literal-packet-part-01-v1.md` is 668 LF, SHA-256 `6fb09e68d723dfa0996a6611289aef07469852eb59ea5adf6b8c514f4d35e059`. After the complete read, administrative SHA-256 observations matched the packet and these wave-control pins: manifest `c2973791e783c3a57c07025d0834736f9ce346b56374364b4b664bfc232b54a9`; freeze receipt `a6fb070edd35c1bb002758077c616f8de38b6ead774f3312cae44e3358690929`; final binding `320a4f182ef3f697659184bfd8efc6c828831f0211fea608e492e9ebb2a8a2f9`; prepared metadata `15970b2752b1351e450594b644ea21306bd4aa79c36f19f74f4d7be9fedca9c7`; actual dispatch `1d93d04dd70ad9813f0582fcb969495b38c936339670b379013234a9536cc223`.

I first waited for Main's direct notice of the actual receipt, then read the actual dispatch, entire manifest, freeze receipt, final binding, prepared metadata, and all **22/22** manifest-listed controls through their endings. I sent Main the direct PREBODY ACK naming 22 controls and ordered packet-part LF count 668, before opening the packet body or doing mathematics/comparison. After successful packet LF 221–240, an attempted LF 241–260 read used the misspelled path `aours` and returned path-not-found, presenting no bytes. I immediately disclosed this to Main, then resumed at LF 241 with the proper path before science. Main acknowledged that no process fault was inferred merely from this empty path error. No packet bytes were read out of order.

All 22 status/permission controls, read through their endings and administratively SHA-256-observed after the complete packet, are below. Paths are R-relative; repeated `parent-selected-diagnostic-process-major-quarantine-v1.json` is abbreviated **Q** only within this table.

| # | Control | SHA-256 |
|---:|---|---|
| 1 | `prospective-author-method-scope-restoration-20261030-v1.json` | `6ab69778c11dbfc4ac895f97b381cc70d0059a5723d6b02f62b9957c7e8dcd95` |
| 2 | `contract-addendum-2-frontier-first-owner-direction-v1.json` | `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce` |
| 3 | `parent-L1-selected-diagnostic-release-quarantine-v1.json` | `ba6b4bb953e9ee20c57c4ae84b85dadbc66e26f8e800089f5176b2582a13555f` |
| 4 | `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json` | `e4d6f1e49cb18aced7735cf025dee54830400554c9adc08138250ae9f0523efc` |
| 5 | `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json` | `23fa29449cef8e02d981efc021934e4cec16960ca6bfe8f6f2178bbd048c85b4` |
| 6 | `parent-ame-held-compression-claim-consumer-quarantine-v1.json` | `c307e902eee5f3736aab0e2437738898382b3d3083f6c307118219b9a4c875b0` |
| 7 | `parent-held-ph-registration-report-consumer-quarantine-v1.json` | `97fbd5967b472783c5ed860f0745b88d7917eb93e1c340f043c974a531ac1453` |
| 8 | `review-waves/f439-depolarizing-ancillary-all-dimensional-repair-written-review/Q` | `74f9f9d57eb5866f68dec331b9bf4facca2bc8d4116186cd241b3bff1539dfee` |
| 9 | `review-waves/f444-spr-full-seven-coefficient-enlargement-and-all-ray-review/Q` | `d00f41bf0205680ef8256f38c97d2023058da935c260ba5cc7f17cb77bd8e184` |
| 10 | `review-waves/f448-kac-actual-second-arm-exterior-module-and-character-review/Q` | `f6ccc5fa10f0e30536921ea86828c437359869413919eae258cbbd82d4989805` |
| 11 | `review-waves/f508-coherent-vacuum-w4-h2-channel-and-strictness-written-review/Q` | `649349cfe636c88e60bee96400512ae6db8d8e12b875d3d100fcce3312785fd8` |
| 12 | `review-waves/f513-boolean-five-span-physical-four-fibre-xor-obstruction-review/Q` | `cb9a81b76acaf740e2d691664e57e46a274c208f44fb071f5f0724973ae1a1a8` |
| 13 | `review-waves/f586-semigroup-finite-pure-source-free-band-regularity-written-review/Q` | `e4d3dca7c41456e4e48dc154719b1df9e653b656b2cbf9324c82b195e3539681` |
| 14 | `review-waves/f602-olson-deficit-six-protected-triples-independent-actual-word-check/Q` | `df412094a47e89be2507d7a7809d68449f08476aabfaca44fd9ecb4dce2a40b8` |
| 15 | `review-waves/f596-actual-ame48-t24-entire-4555-same-tensor-frontier/parent-selected-instance-process-major-quarantine-v1.json` | `3f4b2c6d31a420ecff35a6478ce7a302637765b1203c046619715eda634b6927` |
| 16 | `review-waves/f653-sun8-psl2-small-exception-actual-cosets-written-review/Q` | `a85930a9b268d472d5ded2f31b4b9916394e99f97e854c3a3869a9c8fd7ec8de` |
| 17 | `review-waves/f654-sun8-primepower-source-and-actual-normalcut-consumer-review/Q` | `9aaf84aabb3ea428e3622c5e6b7961d21bd3f1a8b3a16a727be203077e784462` |
| 18 | `review-waves/f659-fresh-original-input-sun8-source-and-normalcut-consumer-review/Q` | `abf867950e1425ed74e1a766f6838957b255694cf0f64e936a23321c1324913b` |
| 19 | `review-waves/f660-fresh-original-input-sun8-exceptional-actual-coset-review/Q` | `f5007a354d6acb8335ad2b9cc170f457c542640e1bbd15c5439d69d0c76039ab` |
| 20 | `review-waves/f662-report-v23-werner-core-falsification-documentary-audit/Q` | `7dc07513bb05a7b08ba9795b566f38c39750a8f71fc68d576ea4367d4b0e4c38` |
| 21 | `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json` | `8a98f416ed19f9d838eb286d1de32cd9508e33324fe44b2593dd3663c9b2c70c` |
| 22 | `parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json` | `27390c73fd6741217ce1d86c5f41e388ef87e3f51b306565053943e0333afbce` |

Controls were used for status/permission only. No outgoing scientific links, old code, sibling returns, held history, held episodes or held proof/method/selection/planning/verification/reporting/confidence/downstream consumers were used. Administrative clock/hash observations are not scientific execution, source authentication, or a clean-cognition certificate.
