# Independent reconstruction: the actual septic four-corner SDP and zero-dual frontier

**Status: independent, nonblind AUTHOR-WRITTEN RECONSTRUCTION; UNADOPTED.** The per-box equivalences, eligibility test, ROOT consequence, conditional universal bridge, and example below are written mathematical claims for separate complete parent reading and disposition. No universal common-SPR/ROOT result, eligible zero-dual example, or strict-negative counterexample is claimed. No existing gate is automatically cleared. The exact remaining global sentence appears in §9.

## 1. Actual object and one-numerator quantifiers

Let

\[
K=\{a(s)=s^7+\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\},
\]

where all endpoints are real, all seven intervals are independent, degenerate intervals are permitted, and **every** actual member is strictly Hurwitz. This eligibility assumption is later characterized rather than replaced by corner stability. In the original strict synthesis problem, one must choose **one** real monic stable septic \(Q(s)=\sum_{j=0}^7q_js^j\), \(q_7=1\), before quantifying over every actual \(a\in K\) and every frequency; \(Q/a\) must be strictly positive real for all of them. Choosing a different \(Q\) per slice, frequency, or ray is not the problem.

For \(t=\omega^2\ge0\), write

\[
\begin{aligned}
E_a&=a_0-a_2t+a_4t^2-a_6t^3,&O_a&=a_1-a_3t+a_5t^2-t^3,\\
F_Q&=q_0-q_2t+q_4t^2-q_6t^3,&G_Q&=q_1-q_3t+q_5t^2-t^3,\\
P_{Q,a}&=F_QE_a+tG_QO_a.
\end{aligned}
\]

Thus \(a(i\omega)=E_a+i\omega O_a\) and \(P_{Q,a}=\Re(Q(i\omega)\overline{a(i\omega)})\). The **physical** row, in ascending coefficient order, is

\[
r_a=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a),\qquad Q\cdot r_a=P_{Q,a}.
\]

The strict problem is equivalent, on the stated eligible compact box, to existence of one monic \(Q\) and one \(\eta>0\) with

\[
P_{Q,a}(t)\ge\eta(1+t)^7\quad(\forall a\in K,\ \forall t\ge0).\tag{1}
\]

For the forward implication, the normalized pairing is jointly continuous on the coefficient box and the compactified frequency interval \([0,\infty]\); the limits at its endpoints are \(q_0a_0>0\) and \(1\). Strict positivity at finite frequencies and compactness give one positive minimum. Here stable real monic polynomials have strictly positive coefficients: factor each into real factors \(s+r\), \(r>0\), and real quadratic factors with strictly positive coefficients. In particular all \(a_0>0\) and \(q_0>0\).

Conversely, (1) excludes zeros of every denominator on the imaginary axis by eligibility and makes \(\Re(Q/a_*)(i\omega)>0\) for any fixed actual stable \(a_*\). The rational function \(Q/a_*\) is analytic in a neighborhood of the closed right half-plane and tends uniformly to 1 on large right half-disks. The harmonic minimum principle, applied on such half-disks and then letting their radius grow, gives positive real part in the open right half-plane. Equation (1) excludes imaginary-axis numerator zeros; the positive interior real part excludes interior numerator zeros. Thus the **same** \(Q\) is Hurwitz, not an extra unproved premise. The same boundary argument works for every \(a\in K\). If the convention for strict positive realness uses a small left shift, the uniform stability margin of compact \(K\), the uniform pairing margin, continuity on bounded frequencies, and the uniform limit 1 at infinity also furnish a common sufficiently small shift. The finite endpoint and infinity are not omitted.

## 2. Four fixed physical parity corners

Define four actual members \(C_{\sigma\tau}\), with \(\sigma,\tau\in\{-,+\}\), by independent even and odd endpoint choices:

\[
\begin{array}{c|cccc}
 &a_0&a_2&a_4&a_6\\\hline
E_-&\ell_0&u_2&\ell_4&u_6\\
E_+&u_0&\ell_2&u_4&\ell_6
\end{array}
\qquad
\begin{array}{c|ccc}
 &a_1&a_3&a_5\\\hline
O_-&\ell_1&u_3&\ell_5\\
O_+&u_1&\ell_3&u_5.
\end{array}
\]

All have leading coefficient 1. For every \(t\ge0\), these choices give

\[
\begin{aligned}
E_-&=\ell_0-u_2t+\ell_4t^2-u_6t^3,&E_+&=u_0-\ell_2t+u_4t^2-\ell_6t^3,\\
O_-&=\ell_1-u_3t+\ell_5t^2-t^3,&O_+&=u_1-\ell_3t+u_5t^2-t^3.
\end{aligned}
\]

The alternating signs do not change as a positive frequency varies. At any fixed \(t\), the attainable **actual** pair \((E_a,O_a)\) is exactly the rectangle \([E_-,E_+]\times[O_-,O_+]\). Interpolate independently in its two coordinates, with any harmless convention when an interval collapses. Since the raw row is affine in \((E,O)\), this expresses \(r_a(t)\) as a convex combination of the four actual-corner rows at that frequency. The weights generally depend on \(a\) and \(t\). This does **not** say that the seven-dimensional box of polynomials is the convex hull of four polynomials.

Consequently (1) with the same \(Q,\eta\) holds for every member and frequency if and only if it holds for these four corners and every frequency. No corner-only criterion for eligibility has been used.

## 3. Compact zero dual and finite actual atoms

Set \(\widehat r_a(t)=r_a(t)/(1+t)^7\). Its continuous compactified endpoint values are \(a_0e_0\) at \(t=0\) and \(e_7\) at \(t=\infty\). Define

\[
S_K=\{\widehat r_{C_{\sigma\tau}}(t):\sigma,\tau\in\{-,+\},\ 0\le t\le\infty\},\qquad H_K=\operatorname{conv}S_K\subset\mathbb R^8.
\]

The set \(S_K\) is compact, hence so is \(H_K\). The exact same-box alternative is

\[
\boxed{\text{one strict common-SPR numerator on }K\quad\Longleftrightarrow\quad 0\notin H_K.}\tag{2}
\]

Indeed a margin (1) strictly separates \(H_K\) from zero. Conversely, let \(z\) be the closest point of \(H_K\) to zero when zero is outside. The projection inequality gives \(z\cdot v\ge\|z\|^2>0\) for all \(v\in H_K\). Since \(e_7\in H_K\), \(z_7>0\); rescale by \(z_7\) to obtain a monic separator with a uniform positive margin. Sections 1–2 then give the original stable numerator for **every** actual member.

If \(0\in H_K\), Carathéodory in \(\mathbb R^8\) gives at most nine compactified points. Absorb each positive finite-frequency normalization into its weight, and combine the two endpoint types. The result is

\[
\sum_{i=1}^m w_i r_{C_i}(t_i)+\lambda e_0+\mu e_7=0,\qquad
 t_i>0,\ w_i>0,\ \lambda,\mu\ge0,\quad
 m+\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}\le9.\tag{3}
\]

Every \(C_i\) is one of the four **actual** parity corners; repetitions are allowed. At least one finite atom is necessary: nonnegative multiples of the distinct vectors \(e_0,e_7\) alone cannot sum to zero nontrivially. Conversely, (3) gives zero in the compact hull after reinstating the positive factors \((1+t_i)^7\), representing \(\lambda e_0\) by a zero-frequency row divided by its strictly positive actual constant coefficient, and normalizing all coefficients to sum to one. The endpoints are genuine compactification contributions, not invented positive-frequency atoms.

Equation (3) is an exact obstruction to **strict** synthesis on this same box. It does **not** itself exhibit an all-eight-strict-negative finite aggregate: its six middle raw coordinates sum to zero, and the first and last sum to \(-\lambda\) and \(-\mu\). Neither same-box weak-separator-to-strict synthesis nor the existence of an eligible box satisfying (3) follows.

## 4. Eight-block SDP, with all coefficient equations

Let \(v=(1,t,t^2,t^3)^T\). For each of the four actual corners, put \(p_{\sigma\tau}=P_{Q,C_{\sigma\tau}}-\eta(1+t)^7\). The strict target is equivalent to the existence of one common \((q_0,\ldots,q_6)\), one \(\eta>0\), and eight real symmetric PSD \(4\times4\) matrices \(M_{\sigma\tau},N_{\sigma\tau}\) satisfying

\[
p_{\sigma\tau}(t)=v(t)^TM_{\sigma\tau}v(t)+t\,v(t)^TN_{\sigma\tau}v(t)\quad\text{identically for all four corners}.\tag{4}
\]

The eight coefficient equalities for each corner can be written without a sampling convention. Set

\[
e=(a_0,-a_2,a_4,-a_6),\quad o=(a_1,-a_3,a_5,-1),\quad
f=(q_0,-q_2,q_4,-q_6),\quad g=(q_1,-q_3,q_5,-1).
\]

For \(k=0,\ldots,7\), with indices outside \(0,\ldots,3\) omitted, impose

\[
\sum_{i+j=k}f_ie_j+\sum_{i+j=k-1}g_io_j-\eta\binom7k
=\sum_{i+j=k}M_{ij}+\sum_{i+j=k-1}N_{ij}.\tag{5}
\]

The matrix sums are over ordered indices, so off-diagonal entries contribute twice. There are exactly 32 equalities, eight PSD blocks with ten independent entries apiece, and 88 real existential scalar variables in all. The same \(q,\eta\) occur in all four systems; the endpoints are fixed data in a per-box problem. Positivity of \(\eta\) is strict.

For completeness, here is the half-line representation behind (4). If \(p\ge0\) on \([0,\infty)\) and \(\deg p\le7\), then \(p(x^2)\) is a globally nonnegative real polynomial of degree at most 14. For a nonzero polynomial, factor it over \(\mathbb C\): real roots have even multiplicity, and conjugate roots can be split between a complex polynomial and its conjugate. Hence \(p(x^2)=A(x)^2+B(x)^2\) with real \(\deg A,\deg B\le7\); the zero case is immediate. Split \(A=A_e(x^2)+xA_o(x^2)\) and likewise for \(B\), and average the representations at \(x\) and \(-x\). Then

\[
p(t)=A_e(t)^2+B_e(t)^2+t\bigl(A_o(t)^2+B_o(t)^2\bigr),
\]

where each displayed polynomial has degree at most three. Their coefficient-vector outer products give the two PSD Grams. The converse follows directly from PSD. This establishes an exact finite LMI, not a frequency grid or approximate solver claim.

For rational endpoints, any positive instance has a certificate with rational \(q,\eta\) and rational **positive definite** Grams. Starting from a strict uniform margin, approximate \(q\) rationally and choose a smaller positive rational margin, leaving a strictly positive compactified residual. Subtract \(\varepsilon(1+t)\sum_{j=0}^3t^{2j}\), with sufficiently small positive rational \(\varepsilon\); the residual remains nonnegative on the entire half-line. Represent it as above and add \(\varepsilon I\) to both Grams. For each power \(2j\), the \(j\)-th diagonal entry of \(M\) occurs with coefficient 1, and for \(2j+1\) the corresponding diagonal of \(N\) does likewise. Approximate the off-diagonal entries by rationals and solve the eight diagonal equations exactly. Continuity of eigenvalues preserves positive definiteness for close enough approximations. Exact principal-minor signs and equalities could check such a certificate, but no checker or certificate is supplied here.

If rational endpoints instead admit (3), there is a witness with real-algebraic frequencies and weights, including \(\lambda,\mu\). For each of the finitely many lengths, endpoint-support choices, and corner-label lists, (3) and the strict/non-strict sign conditions form an existential polynomial system over \(\mathbb Q\). Transfer between real closed fields gives a solution in the real algebraic numbers whenever it has a real solution. This does not produce such a solution or claim rationality of its frequencies.

## 5. Exact eligibility, including tangencies and infinity

For arbitrary ordered endpoints let \(b_j=(\ell_j+u_j)/2\), \(h_j=(u_j-\ell_j)/2\), and

\[
\begin{aligned}
E_b&=b_0-b_2t+b_4t^2-b_6t^3,&H_E&=h_0+h_2t+h_4t^2+h_6t^3,\\
O_b&=b_1-b_3t+b_5t^2-t^3,&H_O&=h_1+h_3t+h_5t^2.
\end{aligned}
\]

Every actual member is strictly Hurwitz **iff** all three conditions hold:

1. The center \(B(s)=s^7+\sum b_js^j\) is strictly Hurwitz.
2. \(\ell_0>0\).
3. No \(t>0\) satisfies both \(E_b(t)^2\le H_E(t)^2\) and \(O_b(t)^2\le H_O(t)^2\).

Necessity: the center is an actual member and all monic Hurwitz members have positive constant coefficient. At \(t>0\), the actual \((E,O)\) values fill exactly the displayed parity rectangle; the two inequalities say that rectangle contains \((0,0)\), hence some actual polynomial has an imaginary-axis zero. For sufficiency, the three conditions exclude all imaginary-axis zeros, including \(t=0\). The coefficient segment from the stable center to any member stays inside the box. Monic roots depend continuously on bounded coefficients and cannot escape to infinity along this compact segment; a root leaving the open left half-plane would cross the imaginary axis. Thus every member is stable. Equality in either inequality is included, so boundary tangencies and degenerate intervals are not lost.

The center condition itself is a real-polynomial condition. With \(d_0=1,d_1=b_6,\ldots,d_7=b_0\), and \(d_j=0\) outside \(0\le j\le7\), form \(H_{ij}=d_{2j-i}\), \(1\le i,j\le7\). The classical Routh–Hurwitz criterion says all seven leading principal determinants of this matrix are strictly positive. Roots at infinity cannot appear because the leading coefficient is identically one.

## 6. Reconstructing the actual-band and odd-cone import

This section records the actual scope of the S3 import and supplies a written reconstruction rather than assuming that arbitrary ordered markers are realizable. Assume at least one odd coefficient interval has positive width. The physical endpoints satisfy \(O_+(t)-O_-(t)>0\) for every \(t>0\).

For any actual stable septic, \(E\) and \(O\) have three positive simple roots each, with the roots of \(O\) in the successive intervals between the first and second roots of \(E\), between the second and third roots of \(E\), and after the third root of \(E\). One direct justification is to follow the continuous argument of \(a(i\omega)\) for \(\omega>0\): for every root \(z\) of \(a\), \(\Re(1/(i\omega-z))>0\), so the argument increases strictly from 0 to \(7\pi/2\); its real and imaginary crossings give exactly these simple interlacing roots. Apply this to the two actual odd endpoints paired with **any fixed actual even coefficient vector**. Since \(O_-<O_+\) for \(t>0\), their roots necessarily have the order

\[
O_-:\ a,d,e;\qquad O_+:\ b,c,f;\qquad 0<a<b<c<d<e<f.
\]

The shared even roots lie respectively before \(a\), between \(b,c\), and between \(d,e\). As the fixed actual even vector was arbitrary, every actual \(E\) is strictly negative, positive, negative on \([a,b],[c,d],[e,f]\), respectively. These three closed bands are exactly where the actual odd interval contains zero. This proves the stated band interface from the actual box and all-member stability; it does not authorize replacing it with arbitrary markers.

For a finite actual-endpoint grid at distinct positive nodes \(u_i\), let \(\alpha_i=w_i u_iO_i\). The four odd aggregate coordinates are

\[
V_k=\sum_i\alpha_i(-u_i)^k\le0,\quad k=0,1,2,3.\tag{6}
\]

Zero-odd singleton rays \(Z\) and same-node opposite-odd cancellation rays \(P\), with weights \((O_+,-O_-)\), are retained; no division by a zero odd endpoint is made. On any finite grid, a nonnegative-weight cone is pointed and generated by its extreme rays. If two opposite odd signs occur at a node, subtract their maximal common cancellation ray; duplicate columns of the same sign can similarly be split. Every other extreme ray has at most one nonzero-odd atom per distinct node and at most five nodes, since there are four inequalities.

There are no such rays on one, two, or three distinct nodes. For \(m\le3\) and each \(i\), both \(p_i(t)=\prod_{j\ne i}(u_j-t)\) and \(-t p_i(t)\) are nonnegative linear combinations of \(1,-t,t^2,-t^3\). Applying (6) to them gives simultaneously \(\alpha_i p_i(u_i)\le0\) and \(-u_i\alpha_i p_i(u_i)\le0\), impossible for nonzero \(\alpha_i\). For four nodes, \(p_i\) alone forces the odd signs \((-,+,-,+)\). An extreme ray has three active independent moments. If moment \(k\) is omitted and \(H_4(t)=\prod_{j=1}^4(t-u_j)\), Lagrange interpolation gives the positive actual weights

\[
w_i=\frac{e_{3-k}(\{u_j:j\ne i\})}{u_iO_iH_4'(u_i)},\qquad k\in\{0,1,2,3\}.\tag{7}
\]

Indeed \(\sum_i u_i^\ell e_{3-k}(\widehat u_i)/H_4'(u_i)=(-1)^{3-k}\delta_{\ell k}\) for \(\ell=0,1,2,3\): the omitted signed moment is negative and the other three vanish. For five nodes all four moments are active; the one-dimensional Vandermonde nullspace gives both orientations

\[
w_i=\frac{\pm1}{u_iO_iH_5'(u_i)},\qquad H_5(t)=\prod_{j=1}^5(t-u_j),\tag{8}
\]

with the sign selected so all weights are positive. The two possible odd sign patterns are \((+,-,+,-,+)\) and \((-,+,-,+,-)\). These are exactly the actual \(R4\), both \(R5\), \(Z\), and \(P\) rays used below, with all four \(R4\) omitted moments retained.

There is also an exact **weak**, pointwise box-level equivalence. Let \(A(K)\) mean that no finite positive-weight actual-member/positive-frequency aggregate has **all eight** raw coordinates strictly negative. With nondegenerate odd uncertainty, let \(B(K)\) mean that one triple

\[
x\in[0,a],\quad y\in[b,c],\quad z\in[d,e],\quad F(t)=(x-t)(y-t)(z-t)
\]

makes the even pairing nonnegative on every actual \(R4\) and both actual \(R5\) orientations, after choosing \(E_F=E_-\) where \(F\ge0\) and \(E_F=E_+\) where \(F<0\). The existential triple precedes all ray quantifiers. Then \(A(K)\iff B(K)\).

For \(A\Rightarrow B\), the compact row hull is disjoint from the open negative orthant: otherwise replace any endpoint atoms by sufficiently nearby finite-frequency actual rows and preserve strict negativity. Separation from that open cone supplies a nonzero coefficientwise nonnegative vector \(q\) with \(P_{q,a}\ge0\) for every actual \(a,t\). Its even polynomial \(F_q\) cannot vanish identically: opposite odd endpoints on the interior of the first band would force its odd polynomial \(G_q\) to vanish on an interval too. Canceling opposite odd values with the same actual even endpoint shows \(F_q\le0,\ge0,\le0\) on the three bands. As \(F_q(0)=q_0\ge0\), it has roots in the three indicated intervals. The intervals are disjoint and \(\deg F_q\le3\); hence \(F_q=q_6F\) with \(q_6>0\). For every ray with odd sums \(V_k\le0\), the odd coefficient vector of \(q\) is nonnegative, so the corresponding even pairing is nonnegative. This is one triple for all rays.

For \(B\Rightarrow A\), a hypothetical all-eight-strict-negative aggregate has strictly negative pairing with the nonnegative even coefficient vector \((xyz,xy+xz+yz,x+y+z,1)\) of \(F\), even if \(x=0\). Replace each even value by its actual pointwise minimizer \(E_F\) and split each odd value into actual endpoint atoms at the same node; independence preserves actual physical pairing and all odd moments while not increasing the even pairing. The finite cone decomposition into (7), (8), \(Z\), and \(P\) then gives a nonnegative pairing: \(R4/R5\) by \(B\), and \(Z/P\) automatically because \(F\) has signs \(-,+,-\) on the actual bands where \(E\) has those strict signs. This contradicts strict negativity. Nothing here turns weak \(B(K)\) into strict synthesis on the same unbuffered \(K\).

## 7. Feasible SDP implies one strict triple and all actual rays

Assume an eligible box has nondegenerate odd uncertainty and (4) is feasible. The resulting single stable \(Q\) has strictly positive coefficients. For any nonzero finite positive collection of actual atoms whose four odd aggregate coordinates form \(M_{\rm odd}\le0\),

\[
\sum_iw_iF_Q(t_i)E_i(t_i)
=\sum_iw_iP_{Q,a_i}(t_i)-(q_1,q_3,q_5,q_7)\cdot M_{\rm odd}
\ge\eta\sum_iw_i(1+t_i)^7>0.\tag{9}
\]

This uses the same \(Q,\eta\) for every collection. At an interior band node use two actual members with one even endpoint and opposite odd endpoints and the positive cancellation weights; at an endpoint use the actual zero-odd singleton. Thus \(F_Q\) has the strict signs \(-,+,-\) on the three closed bands. Since \(F_Q(0)=q_0>0\), it has three distinct roots

\[
x\in(0,a),\quad y\in(b,c),\quad z\in(d,e),\qquad F_Q(t)=q_6(x-t)(y-t)(z-t).
\]

The degree-three bound and \(q_6>0\) show these are all its roots. In particular, applying (9) to the actual minimizing even endpoints gives, for every nonzero actual \(R4\) and either \(R5\) orientation,

\[
\sum_iw_iE_F(t_i)(x-t_i)(y-t_i)(z-t_i)
\ge\frac{\eta}{q_6}\sum_iw_i(1+t_i)^7>0.\tag{10}
\]

This includes all four omitted moments and both five-node orientations, as well as the \(Z/P\) cases and positive combinations in (9). It is a one-way per-box consequence: a weak triple from §6 is not asserted to imply (4) on the same box.

## 8. Universal buffered bridge and conditional strict-negative normal form

This reconstructs the scope of S2 and distinguishes it from the stronger, unsupported same-box converse. Write \(W(K)\) for a nonzero coefficientwise nonnegative polynomial \(q\), of degree at most seven, satisfying \(P_{q,a}(t)\ge0\) for every actual \(a\in K,t\ge0\). The separation argument in §6, including endpoint approximation, gives \(A(K)\iff W(K)\); it does not require odd uncertainty.

Given any eligible compact \(K\), stability is open and compactness gives an eligible enlargement \(L\) containing independent positive buffers \(h_0,h_1\) in the constant and linear coefficient directions. Suppose \(W(L)\) holds. For each \(a\in K\), choosing buffer signs adversarially yields

\[
P_{q,a}(t)\ge h_0|F_q(t)|+h_1t|G_q(t)|.\tag{11}
\]

For each \(a_L\in L\), \(q/a_L\) is analytic on the closed right half-plane, has nonnegative real boundary values and a nonnegative limit at infinity. The harmonic minimum principle gives nonnegative interior real part; it is strictly positive inside because \(q(x)/a_L(x)>0\) for real \(x>0\). If \(q(i\omega_0)=0\) at some \(\omega_0>0\), the tangential derivative of its nonnegative boundary real part vanishes, while the Hopf boundary lemma gives a strictly positive normal derivative. Hence \(q'(i\omega_0)/a_L(i\omega_0)\) is a strictly positive **real** number for every \(a_L\in L\). This is impossible: varying the independent constant and linear buffers makes their complex values contain a genuine two-dimensional rectangle at \(\omega_0>0\), not a single positive ray. Thus \(q(i\omega)\ne0\) at every positive finite frequency, and (11) is strictly positive there.

Fix \(a_*\in K\). The normalized \(P_{a_*,a}\) is uniformly positive in neighborhoods of \(0\) and \(\infty\): its endpoint values are \(a_{*,0}a_0>0\) and 1. On the remaining compact middle-frequency region, (11) gives a uniform positive margin, whereas \(P_{a_*,a}/(1+t)^7\) is uniformly bounded. Consequently one sufficiently small \(\delta>0\) makes

\[
Q=(q+\delta a_*)/(q_7+\delta)
\]

satisfy (1) for all of \(K\), even if \(q_0=0\) or \(q_7=0\). Section 1 then gives its stability. This proves \(W(L)\Rightarrow\) strict synthesis on \(K\), **not** \(W(K)\Rightarrow\) strict synthesis on \(K\).

The following are therefore equivalent as **universal** statements: (SPR) every eligible both-parity box has one strict common numerator; (DUAL) every eligible box satisfies \(A(K)\); and (ROOT) every eligible box with nondegenerate odd uncertainty satisfies the one-triple/all-\(R4\)/both-\(R5\) condition \(B(K)\). SPR implies DUAL because a stable numerator has strictly positive coefficients and a positive pairing. DUAL implies SPR by applying \(W\) to the eligible buffer \(L\). For nondegenerate odd uncertainty, §6 gives \(A\iff B\); when all odd coefficients are fixed, \(q(s)=sO(-s^2)\) has nonnegative coefficients and physical pairing \(tO(t)^2\ge0\), so \(A\) holds automatically. Thus ROOT and DUAL are universally equivalent without treating the fixed-odd case as a three-band theorem.

A conditional normal form also follows, without asserting that a counterexample exists. If any eligible \(K\) fails strict synthesis, take a sufficiently small **full-width** eligible enlargement \(L\) with the two positive buffers. If \(L\) had no all-eight-strict-negative finite actual aggregate, the buffered argument would give strict synthesis on \(K\), a contradiction. Replace each actual row of a strict-negative aggregate on \(L\) by its four frequencywise actual-corner mixture. Strict negativity and stability of the compact box are open conditions, so perturb the full-width endpoints, positive frequencies, and positive weights to nearby rationals while retaining eligibility and all eight strict inequalities. Conic Carathéodory in \(\mathbb R^8\), implemented abstractly by deleting a positive linear dependence, preserves the entire aggregate with at most eight positive actual-corner atoms; rational data allow rational elimination. This is a **conditional existence** of some rational full-width eligible box and certificate if universal SPR fails, not a supplied certificate, six-frequency claim, or same-box transformation of (3).

## 9. The exact unpaid global sentence

For arbitrary real endpoints \(\ell_j\le u_j\), let \(\operatorname{Eligible}(\ell,u)\) be the seven strict center Hurwitz determinants, \(\ell_0>0\), and

\[
\forall t\,[t\le0\ \lor\ E_b(t)^2>H_E(t)^2\ \lor\ O_b(t)^2>H_O(t)^2].
\]

Let \(\operatorname{SDP}(\ell,u,q,\eta,M,N)\) be the 32 equations (5), \(\eta>0\), and all 15 principal minors nonnegative for each of the eight symmetric blocks. The original universal strict problem is exactly the real first-order sentence

\[
\forall(\ell,u)\;\bigl[(\ell_j\le u_j\ \forall j\ \wedge\operatorname{Eligible}(\ell,u))
\Longrightarrow\exists q_0,\ldots,q_6,\eta,M,N\;\operatorname{SDP}(\ell,u,q,\eta,M,N)\bigr].\tag{12}
\]

All coefficients here are rational constants; the endpoint expressions merely substitute real variables. Classical quantifier elimination over real closed fields decides (12) **in principle**. No quantifier elimination or scientific program has been run; no practical runtime, arbitrary-input implementation, truth value, or global ROOT conclusion follows from writing the sentence. The unpaid original step is to prove (12), or give an actual eligible box with (3); a separately requested all-eight-strict-negative certificate requires the distinct strict conditions (or the conditional enlargement argument above), not merely a zero dual.

## 10. Reconstructing the displayed full-width example and its comparison

The following is a written verification of the **already supplied S1 example**, not an executed diagnostic and not a proof of (12). Let \(Q=(s+1)^7\), and let the independent coefficient box be centered on \(Q\) with halfwidths \(h_0=9/10\) and \(h_j=1/100\) for \(1\le j\le6\). All seven widths are positive. Write \(a=Q+\sum_{j=0}^6d_js^j\), \(|d_j|\le h_j\). Since \(|Q(i\omega)|=(1+t)^{7/2}\) and \(t^{j/2}\le(1+t)^{7/2}\) for \(0\le j\le6\),

\[
\left|Q(i\omega)\overline{\sum_jd_j(i\omega)^j}\right|
\le(1+t)^{7/2}\sum_jh_jt^{j/2}
\le\left(\frac9{10}+\frac6{100}\right)(1+t)^7
=\frac{24}{25}(1+t)^7.
\]

Hence \(P_{Q,a}\ge(1/25)(1+t)^7\) for all actual members and all frequencies. The same estimate applies to every point of each segment \(Q+\theta(a-Q)\), \(0\le\theta\le1\), excluding imaginary-axis zeros; bounded monic homotopy from the stable \(Q\) gives all-member stability. This is one eligible, both-parity-varying positive box, not a universal result.

Its constant interval is \([1/10,19/10]\), with ratio 19. In the **particular** S4 scaled-binomial family, a constant interval has positive endpoint ratio \((1+\epsilon)/(1-\epsilon)<11\) when \(0<\epsilon<5/6\), independently of the scale \(\beta>0\). A positive interval containing \([1/10,19/10]\) must have endpoint ratio at least 19. Thus no one displayed scaled-binomial box contains this example. This does not exclude every other previously adopted thickening or enlarge any prior gate automatically.

## 11. Imports, exposure, and limits

- Standard mathematical inputs used above: compact convex separation/projection and Carathéodory (convex and conic); root continuity for bounded monic families; factorization of a univariate globally nonnegative polynomial; the harmonic minimum principle and Hopf boundary lemma; Routh–Hurwitz; finite pointed-polyhedral-cone generation and Vandermonde/Lagrange identities; and real-closed-field transfer and quantifier elimination. These are identified imports, not claims of formal-kernel verification. Sections 6 and 8 reconstruct the actual-scope S3 and S2 interfaces rather than importing held reviewer content.
- Frozen source packet: one ordered part, observed SHA-256 `7c776fa3df1aa8075ea6cf786f38ea518f7f159d1192b1278eb5913bd52662b9`, 45,669 bytes and 325 LF. After the direct pre-body ACK, I read LF 1–325 consecutively in raw windows of at most 20 LF, through the ending, with no parallel body access. It renders complete S1 (182 LF), S2 (40 LF), S3 (46 LF), and S4 (39 LF). The original-source SHA pins and packet rendering/roundtrip are parent-supplied metadata; I did not independently re-render or authenticate the original sources.
- Before body access I read the complete manifest, freeze receipt, final pre-dispatch binding, prepared metadata, actual dispatch, all **21** listed status/permission controls, and the multipart policy. I directly acknowledged Main before reading the packet; my initial ACK mistakenly said 20 controls, and I corrected that count to 21 in a second direct message **before** any packet access. The user-specified manifest, freeze, and final-binding SHA-256 pins matched my `shasum` observations. The task and manifest previewed the claims before the packet, so this author is nonblind; no cognition or family-independence certificate is asserted.
- All held episodes and **all** their consumers remained NONINPUT. No held history, sibling proof, old code, or outgoing link was accessed. No scientific child code, solver, test, build, lint, formatter, external-model CLI, package installation, or paid/heavy job was run. The written example was already in the packet. Metadata shell use was limited to the stated hash/size checks, native clock observations, and creating a fresh exclusive output directory. Native clock observed before composing this output: `2026-10-30T16:46:28-0700 PDT`.
- This reconstruction has not received the parent full read/disposition, a separate independent review, a human or formal proof check, source-identity authentication, or novelty clearance. Parent must perform its own full read and separately decide the exact scoped disposition; no previous gate is automatically passed or backdated.
