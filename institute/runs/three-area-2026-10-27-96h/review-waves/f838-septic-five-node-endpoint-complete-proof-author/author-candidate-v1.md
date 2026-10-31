# F838: five-node endpoint exclusion, exact residual, and a same-box bandwidth obstruction

**Status.** Prospective, nonblind same-harness GENERAL AUTHOR candidate; independent parent disposition and review are separate. The statements below concern an actual zero relation on ONE eligible coefficient box. They do not exhibit a zero dual or prove a global SPR/ROOT theorem. The only non-elementary mathematical import used for the five-node conclusions is the classical strict Hermite–Biehler interlacing statement explicitly specified in §2. Its original proof/body is not in this packet, so the conclusions are conditional on that named import. In particular, the at-most-five-frequency strict-negative no-go and the buffered strictification argument are **not** used.

## 1. Quantified object and moment identities

Let **every** polynomial in the nonempty compact independent real coefficient box

\[
K=\{s^7+\sum_{j=0}^6 a_js^j:\ell_j\le a_j\le u_j\}
\]

be strictly Hurwitz. Any coefficient intervals may be degenerate. Put \(b_j=(\ell_j+u_j)/2\), \(h_j=(u_j-\ell_j)/2\), and for \(t>0\) define

\[
\begin{aligned}
E_a(t)&=a_0-a_2t+a_4t^2-a_6t^3,&
O_a(t)&=a_1-a_3t+a_5t^2-t^3,\\
H_E(t)&=h_0+h_2t+h_4t^2+h_6t^3,&
H_O(t)&=h_1+h_3t+h_5t^2.
\end{aligned}
\]

The actual same-frequency value set is exactly the rectangle
\(R(t)=[E_-(t),E_+(t)]\times[O_-(t),O_+(t)]\), where \(E_\pm=E_b\pm H_E\), \(O_\pm=O_b\pm H_O\). Each of its four vertices is attained by an actual fixed parity-corner polynomial; this pointwise fact does **not** say that the entire coefficient box is the convex hull of four polynomials. Independence makes every pair in the rectangle attainable by one actual member. The origin is absent from every \(R(t)\): otherwise one actual member would vanish at \(i\sqrt t\). In particular some coordinate interval is strictly separated from zero at each \(t\).

Consider any finite nontrivial actual-member or actual-corner relation

\[
\sum_{j=1}^{m} w_j r_{a_j}(t_j)+\lambda e_0+\mu e_7=0,\quad
w_j,t_j>0,\quad \lambda,\mu\ge0,\quad a_j\in K,                 \tag{1}
\]

where
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
Endpoint rays alone cannot cancel, so there is at least one finite atom. A physical zero-frequency endpoint can be rescaled to \(\lambda e_0\) because every actual constant coefficient is positive; \(e_7\) denotes the infinity endpoint. Group equal positive frequencies into distinct \(0<v_1<\cdots<v_n\). Let \(W_i>0\) be the total weight and let \((E_i,O_i)\in R(v_i)\) be its **same** weighted-average actual pair. Define
\(X_i=W_iE_i\), \(Y_i=W_iv_iO_i\). Equation (1) is exactly

\[
\sum_iX_i=-\lambda,\quad \sum_iX_iv_i^k=0\ (k=1,2,3),\qquad
\sum_iY_iv_i^k=0\ (k=0,1,2),\quad \sum_iY_iv_i^3=\mu.       \tag{2}
\]

No division by a parity value is made here. A zero in either sequence is retained, and the two cannot vanish simultaneously at a node.

Pairing the moments with the center coefficients yields

\[
\sum_i W_iE_iE_b(v_i)=-\lambda b_0,\qquad
\sum_i W_iv_iO_iO_b(v_i)=-\mu,\qquad b_0>0.               \tag{3}
\]

Both parity coefficient blocks must have at least one positive-width interval. Indeed, if the odd block is fixed, the second left side is a sum of squares, hence all \(O_i=0\) and \(\mu=0\); origin exclusion then makes the even interval avoid zero at every node, so every \(E_iE_b(v_i)>0\), contradicting the first identity. The even-fixed case is identical with parities interchanged. Thus \(H_E(t),H_O(t)>0\) for all \(t>0\), even though other coefficient intervals may be degenerate. Also neither \(X\) nor \(Y\) is identically zero: if, for example, all \(E_i=0\), origin exclusion makes \(O_iO_b(v_i)>0\) for every node, contradicting (3); the other case is symmetric.

## 2. Actual bands and reverse pairs

**Named conditional import — strict Hermite–Biehler, septic form.** For each actual strictly Hurwitz real monic septic, the three positive roots \(x_1<x_2<x_3\) of \(E_a\) and the three positive roots \(y_1<y_2<y_3\) of \(O_a\) are simple and satisfy
\(x_1<y_1<x_2<y_2<x_3<y_3\). The constant terms are positive, and both leading coefficients are negative. No unlisted proof or linked source is imported.

Let \(I_j^E\), respectively \(I_j^O\), be the complete ranges of the \(j\)-th even, respectively odd, positive root over actual members of \(K\). These are compact intervals: the coefficient box is compact and connected, and the simple roots vary continuously. Since an even block and an odd block can be independently combined into ONE actual member, their extrema satisfy the strict physical order

\[
I^E_1<I^O_1<I^E_2<I^O_2<I^E_3<I^O_3.                 \tag{4}
\]

For example, combine a block attaining \(\max I_j^E\) with one attaining \(\min I_j^O\), and apply the imported strict interlacing to that actual member. The other inequalities are the same. Each band is nondegenerate: at a center parity root its two actual envelopes have strictly opposite values because the corresponding \(H\) is positive. Their roots lie on opposite sides in the same interlacing interval. The bands are exactly the frequencies where the relevant parity interval contains zero. Within an even band the odd interval has a strict common sign \(+,-,+\), respectively; within an odd band the even interval has a strict common sign \(-,+,-\), respectively. At a band's left and right endpoints its own parity interval has only the ordinary one-sided pre-crossing and post-crossing signs, allowing zero.

We now derive, rather than assume, the two required reverse pairs. Delete zero entries **only for sign counting**. Each of \(X,Y\) has at least three sign changes. If one had at most two, choose a polynomial of degree at most two with one root in each sign-change gap and orient it so all products with the nonzero entries have the same strictly positive sign. Pair with \(v_iX_i\), or with \(Y_i\), and use (2) for a contradiction. If there are exactly three changes, let the monic cubic \(g(t)=\prod_{r=1}^3(t-c_r)\) have one positive root in each such gap. Its product with every nonzero term has the sign of the last nonzero term, while

\[
\sum_i X_i g(v_i)=\lambda c_1c_2c_3,\qquad
\sum_i Y_i g(v_i)=\mu.                                  \tag{5}
\]

Consequently exactly three changes force the corresponding endpoint to be positive and the last nonzero sign to be positive; an absent corresponding endpoint forces at least four changes.

In the absence of a strict reverse pair in any of one parity's three actual bands, its nonzero sign word is a subsequence of the ordinary crossing word \(+,-,+,-\): inside each band signs can only progress in the usual direction, and outside the bands the signs are fixed. That word has at most three changes, with a negative last sign if there are three, contradicting (5). Thus each parity has a strict reverse pair in one of its own physical bands. An even reverse pair is \(-\to+\) in bands 1 or 3 and \(+\to-\) in band 2; odd pairs have the analogous pattern. The one-sided endpoint signs show both members of a strict reverse pair lie in the **interior** of its band. Even and odd bands are disjoint, so these are two different bands of the same actual box.

## 3. Five-node interpolation and all endpoint cases

Assume now \(n=5\), without imposing any bound on the original number of finite atoms. Put
\[
H(t)=\prod_{i=1}^{5}(t-v_i),\quad P=\prod_{i=1}^{5}v_i>0,\quad
D_i=H'(v_i),\quad \delta_i=\operatorname{sgn}D_i=(-1)^{5-i}.
\]
Lagrange interpolation and (2) give unique nonzero polynomials \(A,B\) of degree at most one with

\[
X_i=\frac{A(v_i)}{v_iD_i},\qquad Y_i=\frac{B(v_i)}{D_i},\qquad
A(0)=-\lambda P,\qquad [t]B=\mu.                         \tag{6}
\]

For completeness: interpolate \(v_iX_iD_i\) by degree at most four; the three moments of \(v_iX_i\) successively kill its top three coefficients. Lagrange evaluation at zero then gives \(A(0)=-\lambda P\). Interpolating \(Y_iD_i\) similarly gives \(B\), and \(\sum Y_iv_i^3=[t]B\). Conversely the Lagrange identities \(\sum_i v_i^r/D_i=0\) for \(r=0,1,2,3\), and \(\sum_i v_i^4/D_i=1\), recover every moment in (2).

Let \(q_E\) and \(q_O\) count nodes with the indicated grouped parity equal to zero, and put
\[
N^E=\sum_{j=1}^3(\#\{i:v_i\in I_j^E\}-1)_+,\qquad
N^O=\sum_{j=1}^3(\#\{i:v_i\in I_j^O\}-1)_+.
\]
The reverse pairs give \(N^E,N^O\ge1\). If consecutive sampled nodes are in one closed odd band, they are consecutive globally; the actual even values have one strict sign and \(D_i\) changes sign, so (6) forces a distinct root of \(A\) in their open gap. The gap roots counted by \(N^O\), sampled \(E\)-zero roots, and, if \(\lambda=0\), the root at zero are all distinct. The latter sampled roots cannot be in an odd band. Similarly, \(N^E\) gives distinct gap roots of \(B\); if \(\mu=0\), \(B\) has degree at most zero. Hence, including all zeros and band endpoints,

\[
q_E+N^O\le 1-\mathbf1_{\{\lambda=0\}},\qquad
q_O+N^E\le 1-\mathbf1_{\{\mu=0\}}.                     \tag{7}
\]

Thus **any** five-node relation with \(\lambda=0\) or \(\mu=0\) is impossible, including both absent and either single-endpoint case. If both endpoints are positive, (7) forces

\[
q_E=q_O=0,\qquad N^E=N^O=1.                             \tag{8}
\]

Exactly two nodes occupy one odd reverse band and exactly two occupy one even reverse band; no other band of either parity contains more than one node. Each pair is consecutive among all five nodes and lies in the strict interior. Let their open node gaps contain \(\alpha\) and \(\beta\), respectively. The two roots lie in different actual bands, and (6) now forces

\[
A(t)=a(t-\alpha),\quad a=\frac{\lambda P}{\alpha}>0,\qquad
B(t)=\mu(t-\beta),\quad \alpha,\beta>0.                 \tag{9}
\]

## 4. Correct pair order and the complete three-pattern list

Write \(p,q\in\{1,2,3,4\}\) for the odd and even reverse gaps. At the **later** node of the even reverse pair, the even and odd actual values have the same strict sign: \(++\) in even bands 1 and 3, \(--\) in even band 2. Since \(v_{q+1}>\beta\), (9) gives \(B(v_{q+1})>0\). From

\[
(A(v_i),B(v_i))=v_iD_iW_i(E_i,O_i),                      \tag{10}
\]

\(A(v_{q+1})\) has the same positive sign, so \(v_{q+1}>\alpha\). The two bands are disjoint; if the odd reverse band followed the even one, then \(\alpha>v_{q+1}\), impossible. Therefore the odd reverse band precedes the even reverse band, and \(\alpha<\beta\). The only possible actual band pairs are \((I_1^O,I_2^E)\), \((I_1^O,I_3^E)\), and \((I_2^O,I_3^E)\).

At the first odd-pair node, \(A<0\): the common even sign \(-\) in \(I_1^O\) forces \(p\) odd, while \(+\) in \(I_2^O\) forces \(p\) even. At the first even-pair node, \(B<0\): the common odd sign \(-\) in \(I_2^E\) forces \(q\) odd, while \(+\) in \(I_3^E\) forces \(q\) even. Since \(q\ge p+2\), these give exactly:

| Actual odd, even reverse bands | \((p,q)\) | Required strict quadrant word \((E_i,O_i)\), \(i=1,\ldots,5\) |
|---|---:|---|
| \(I_1^O,I_2^E\) | \((1,3)\) | \((--),(-+),(+-),(--),(++)\) |
| \(I_1^O,I_3^E\) | \((1,4)\) | \((--),(-+),(+-),(-+),(++)\) |
| \(I_2^O,I_3^E\) | \((2,4)\) | \((--),(++),(+-),(-+),(++)\) |

The words follow directly from (9) and \(\delta_i=(+,-,+,-,+)\). The listed bands are actual closed root-availability bands, not arbitrary markers; the four reverse nodes themselves are strict interior points. Zero values are not silently assigned a quadrant: their absence in this branch was proved in (8). The table is necessary, not a claim that any row is realizable.

## 5. Exact actual-rectangle residual and corner budget

The following reformulation makes the shared same-box ratio explicit; it does not select even and odd members independently.

Fix an eligible \(K\) and ordered positive \(v_1,\ldots,v_5\). For one row of the table, require its stated reverse-node band memberships and the complete occupancy condition \(N^E=N^O=1\). Choose
\[
\alpha\in(v_p,v_{p+1}),\qquad \beta\in(v_q,v_{q+1}),\qquad k>0.
\]
Define the required coordinate signs
\(\epsilon_i=\operatorname{sgn}(\delta_i(v_i-\alpha))\),
\(\eta_i=\operatorname{sgn}(\delta_i(v_i-\beta))\), and
\(\rho_i=|v_i-\beta|/|v_i-\alpha|>0\). Put
\[
\begin{aligned}
e_i^-&=\max(0,\min\{\epsilon_iE_-(v_i),\epsilon_iE_+(v_i)\}),&
e_i^+&=\max\{\epsilon_iE_-(v_i),\epsilon_iE_+(v_i)\},\\
o_i^-&=\max(0,\min\{\eta_iO_-(v_i),\eta_iO_+(v_i)\}),&
o_i^+&=\max\{\eta_iO_-(v_i),\eta_iO_+(v_i)\}.
\end{aligned}
\]
Require \(e_i^+>0\) and \(o_i^+>0\) for every node; this is the actual strict-quadrant availability test, including endpoints and degenerate individual coefficient intervals. Define
\[
L_i=\frac{o_i^-}{e_i^+\rho_i},\qquad
U_i=\begin{cases}o_i^+/(e_i^-\rho_i),&e_i^->0,\\ +\infty,&e_i^-=0.\end{cases}                      \tag{11}
\]
Then, **with no corner-atom cap**, an actual-member five-node relation with both endpoints positive exists for these fixed \(K,v_i\) if and only if there are a table row, \(\alpha,\beta\) as above, and one common \(k>0\) satisfying all the stated band/occupancy/strict-quadrant conditions and
\[
\max_iL_i\le k\le\min_iU_i.                              \tag{12}
\]
If a lower endpoint in (11) is zero, \(k>0\) handles the fact that the zero ratio itself is not allowed. A finite positive upper endpoint and a positive lower endpoint are included; if \(e_i^-=0\), its upper endpoint is infinite.

**Proof of iff.** From (9)–(10), \(k=\mu/a>0\) and
\[
\frac{O_i}{E_i}=k\frac{v_i-\beta}{v_i-\alpha}.            \tag{13}
\]
Writing \(e=\epsilon_iE_i>0\), \(o=\eta_iO_i>0\), this is \(o/e=k\rho_i\). The possible positive ratios for the sign-restricted actual rectangle are exactly the interval described by (11): the lower ratio is \(o_i^-/e_i^+\), and the upper is \(o_i^+/e_i^-\), with zero and infinity interpreted as above. Thus (12) is necessary.

Conversely, (11)–(12) let us choose a positive \(e,o\) in the two actual coordinate intervals with \(o/e=k\rho_i\) at each node. Independence supplies one actual member with the resulting **same** pair \((E_i,O_i)=(\epsilon_ie,\eta_io)\). Choose any \(a>0\), set \(A(t)=a(t-\alpha)\), \(B(t)=ak(t-\beta)\), and set
\[
W_i=\frac{A(v_i)}{v_iD_iE_i}>0,\qquad
\lambda=\frac{a\alpha}{P}>0,\qquad \mu=ak>0.
\]
Equation (13) then gives \(W_iv_iO_i=B(v_i)/D_i\). The converse part of (6) establishes all eight coordinates of (1). Each actual pair can alternatively be represented by its actual rectangle vertices; this does not change the box or combine different frequencies. This completes the exact conditional characterization, not a feasibility assertion.

For the **additional** constraint of at most eight total corner-plus-endpoint atoms, define at each node
\[
V_i=\left\{\frac{\eta_iO_c(v_i)}{\epsilon_iE_c(v_i)\rho_i}:
 c\text{ is an actual rectangle vertex},\quad
 \epsilon_iE_c(v_i)>0,\ \eta_iO_c(v_i)>0\right\}.         \tag{14}
\]
These are finite sets; coincident physical corners from degenerate intervals are harmless. A vertex is on the required **positive**, not antiparallel, ray exactly when \(k\in V_i\). If no vertex is on that ray, a farthest ray/rectangle boundary point is a positive combination of two edge vertices, so two corner atoms suffice; one does not. Therefore the exact minimum with the five node contributions fixed is \(5+J\), where \(J=\#\{i:k\notin V_i\}\). Adding both positive endpoints gives \(7+J\). The eight-total-atom condition is exactly
\[
J\le1,\quad\text{equivalently }k\text{ belongs to at least four of the }V_i. \tag{15}
\]
This is a prescribed-group minimum, not a minimum after moving nodes or redistributing their contributions. The endpoint-free exclusion above does not depend on this atom cap or on any sparsification theorem.

## 6. A further written actual-box obstruction

For an odd reverse band \(I_a^O\) followed by an even reverse band \(I_b^E\), define the following positive actual-box quantities:
\[
\begin{aligned}
M_{EO}&=\min_{t\in I_a^O}\min\{|E_-(t)|,|E_+(t)|\},&
M_{OO}&=\max_{t\in I_a^O}\max\{|O_-(t)|,|O_+(t)|\},\\
M_{OE}&=\min_{t\in I_b^E}\min\{|O_-(t)|,|O_+(t)|\},&
M_{EE}&=\max_{t\in I_b^E}\max\{|E_-(t)|,|E_+(t)|\},\\
c_{ab}&=\frac{M_{EO}M_{OE}}{M_{OO}M_{EE}},&
d_{ab}&=\min I_b^E-\max I_a^O>0.
\end{aligned}                                             \tag{16}
\]
The two minima are strictly positive because the complementary parity has one strict sign on the respective compact band. The maxima are finite and positive because the own-parity envelope width is positive. Let \(w_a^O,w_b^E\) be the two actual band lengths. A five-node both-positive relation using this band pair necessarily satisfies the **strict** condition
\[
\boxed{\quad w_a^O w_b^E>c_{ab}d_{ab}^{\,2}.\quad}       \tag{17}
\]
Thus, for a given eligible box, if (17) fails for a particular one of the three table pairs, that whole actual pair stratum is excluded. If it fails for all three pairs, no five-node relation exists on that box, including all endpoint patterns. This is an explicit sufficient exclusion criterion, not an assertion that every eligible box satisfies it.

**Proof.** Write \(g_p=v_{p+1}-v_p\), \(g_q=v_{q+1}-v_q\). For \(i\in\{p,p+1\}\) and \(j\in\{q,q+1\}\), (13), the common signs on the complementary bands, and the actual rectangle bounds give
\[
\frac{\min|O_\pm(v_j)|\,\min|E_\pm(v_i)|}
     {\max|E_\pm(v_j)|\,\max|O_\pm(v_i)|}
\le
\frac{|v_i-\alpha|\,|v_j-\beta|}
     {(\beta-v_i)(v_j-\alpha)}.                           \tag{18}
\]
Here the min/max in each factor runs over the two indicated actual envelope values; every denominator is positive. Because \(q\ge p+2\), \(\beta>v_q\), and \(\alpha<v_{p+1}\), the right side is strictly less than
\[
\frac{g_pg_q}{(v_q-v_i)(v_j-v_{p+1})}.                    \tag{19}
\]
Taking \(i=p+1\), \(j=q\), the left side of (18) is at least \(c_{ab}\), and the two denominator factors in (19) both equal \(s=v_q-v_{p+1}\ge d_{ab}\). Hence
\(g_pg_q>c_{ab}s^2\ge c_{ab}d_{ab}^2\). Both pairs lie in their indicated bands, so \(g_p\le w_a^O\) and \(g_q\le w_b^E\), proving (17). No endpoint value has been replaced by an assumed strict sign of its own parity; only the complementary parity is used for the strict minima.

The criterion has a nonempty whole-box scope. Let \(b\) be any fixed strictly Hurwitz monic septic and take \(K_\varepsilon\) with independent half-widths \(\varepsilon h_j\), for any fixed \(h_j\ge0\) having at least one positive entry in each parity. For all sufficiently small \(\varepsilon>0\), every actual member is strictly Hurwitz by openness. Root continuity makes every band shrink to its center root and each of the three relevant band gaps tend to a positive limit. On a shrinking odd band the maximum own-odd envelope magnitude tends to zero while the minimum complementary-even magnitude tends to a positive value; the analogous statement holds on a shrinking even band. Consequently each \(c_{ab}\to+\infty\), whereas each band-width product tends to zero. All three inequalities (17) therefore fail for sufficiently small positive \(\varepsilon\), and the whole corresponding box has no five-node zero relation. If an entire parity is fixed instead, §1 already excludes every relation. No numerical instance, solver, or global synthesis conclusion is used.

## 7. Boundaries, imports, and complete read declaration

* The conclusion is only about exactly five distinct positive finite nodes, arbitrary actual members/corners and endpoint multiplicities combined into \(\lambda,\mu\); the original atom count is unrestricted except where (15) is explicitly imposed. It covers every eligible box, all actual members, all degenerate coefficient intervals, zeros, and all four endpoint-presence patterns. The exact both-positive system (11)–(15) remains a conditional existential feasibility problem. Section 6 excludes a provable box subfamily; no witness or universal exclusion of the remaining boxes is claimed.
* The interlacing theorem in §2 is the named load-bearing conditional import, whose proof body is absent. Elementary interpolation, compactness/continuity, sign counting and planar convexity are written out at the points used. The named <=5-frequency strict-negative import, buffered enlargement, sparse eight-atom existence, zero-hull/SPR alternative, and ROOT interface are not needed or claimed here. No family, human, formal/kernel, source-identity, priority, novelty or parent-acceptance claim is made.
* Set \(R=\)`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. Before any packet body or assigned-target mathematical reasoning, I read this wave's manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual task dispatch receipt, and all 22 manifest-listed controls as status/permission only. Initial structured administrative displays elided fields and one long line; I recovered the entire files with raw reads before acknowledgment. I wrote `prebody-ack-v1.md` and sent a direct prebody ACK to Main before the packet body. I also read the runtime memory summary and general written-math protocol, not as scientific inputs. No prior task-specific scientific exposure is known to me; no clean-cognition certification is asserted.
* After that acknowledgment and before mathematical reasoning, I read the sole `literal-packet-part-01-v1.md` consecutively in raw windows LF 1–20, 21–40, ..., 361–380, 381–382, including the final line. Each displayed window was at most 20 LF and below 30,000 bytes. No packet display was clipped and no packet recovery or source-following was needed. The parent-supplied packet pin is `89781bb28b45227c6e316af0fc29ccfeb33bf003a014b2bc2d69700cc4d72335`; administrative hashes were not independently recomputed. The complete rendered source bodies, in packet order, are:
  1. S1 `review-waves/f816-septic-determinant-minimal-atom-root-budget-proof-author/author-candidate-v1.md`, original LF 1–227, parent pin `4915f3cbc2994c8275c2fc5000d6ff443e719405fc09827220a26b6dbb567f6f`.
  2. S2 `dispositions/info-2-septic-positive-determinant-minimal-atoms-root-budgets-and-twelve-patterns-parent-v1.md`, LF 1–31, pin `be3e21d36784dd18d5a035557846bf300f886fb8c39d5fe3f283fb51b2f6ee22`.
  3. S3 `dispositions/info-2-actual-septic-sparse-coupled-barycentric-and-six-node-frontier-parent-v1.md`, LF 1–33, pin `32db73ad861d2fcafb8fda19efec027f3b957ed5878dc0ae78b8244bc5789549`.
  4. S4 `dispositions/info-2-actual-septic-strict-band-quadrants-and-low-frequency-subcases-parent-v1.md`, LF 1–30, pin `90ce201156b0ee89e5f09e2e6cf3c4fa9d7eb2c6178a02795c84d84dbd7fa9af`.
  5. S5 `dispositions/info-2-actual-septic-eight-atom-zero-dual-six-frequency-and-parity-backtracking-parent-v1.md`, LF 1–39, pin `866dd92b58bb2422281abe815bc1e6cae8e5f8f94c96f2d7eaed00bad372a183`.
* The 22 controls, all R-relative and used only for status/permissions, were `prospective-author-method-scope-restoration-20261030-v1.json`; `contract-addendum-2-frontier-first-owner-direction-v1.json`; `parent-L1-selected-diagnostic-release-quarantine-v1.json`; `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`; `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`; `parent-ame-held-compression-claim-consumer-quarantine-v1.json`; `parent-held-ph-registration-report-consumer-quarantine-v1.json`; the `parent-selected-diagnostic-process-major-quarantine-v1.json` files in each manifest-listed f439, f444, f448, f508, f513, f586, f602, f653, f654, f659, f660 and f662 review-wave directory; the `parent-selected-instance-process-major-quarantine-v1.json` in manifest-listed f596; `parent-remaining-d0-occupancy-E-row-omission-process-major-v1.json`; and `parent-prerun-f746-matching-and-f749-occupancy-design-corrections-v1.json`. Their exact full paths and metadata are in the read manifest. All genuine held episodes and all their proof/method/planning/selection/verification/reporting/confidence/downstream consumers remain NONINPUT.
* I did not open original linked sources, sibling science, held bodies, or old code; no network, external model, scientific code/execution, child subprocess, test, compilation, build, formatter, linter, Git operation, installation, or deletion was used. No verifier was requested or prepared, so a prepared-code hash is not applicable. This is an author candidate; parent whole-read and independent dispositions remain separate.
