# F858: exact five-node common-ratio test and a same-box bandwidth obstruction

**Status and scope.** Prospective nonblind GENERAL AUTHOR candidate, not a review, parent disposition, or acceptance. All conclusions below are conditional on the named strict Hermite–Biehler septic interlacing import in §2, whose proof body is not in the authorized packet. The fixed-box ratio and corner criteria are exact existential equivalences, not assertions that a relation exists. The bandwidth inequality is a necessary condition for a relation on the **same** actual box. I do not use the separate at-most-five-frequency strict-negative theorem, buffered enlargement, a sparse-existence assertion, or any global SPR/ROOT implication.

## 1. Actual object, grouping, and balances

Fix **any** nonempty independent compact real coefficient box
\[
 K=\left\{s^7+\sum_{j=0}^6 a_js^j:\ \ell_j\le a_j\le u_j\right\}
\]
for which every actual member is strictly Hurwitz. Individual intervals may be points. Put \(b_j=(\ell_j+u_j)/2\), \(h_j=(u_j-\ell_j)/2\), and, for \(t>0\),
\[
\begin{aligned}
 E_a(t)&=a_0-a_2t+a_4t^2-a_6t^3,&
 O_a(t)&=a_1-a_3t+a_5t^2-t^3,\\
 H_E(t)&=h_0+h_2t+h_4t^2+h_6t^3,&
 H_O(t)&=h_1+h_3t+h_5t^2,
\end{aligned}
\]
with \(E_\pm=E_b\pm H_E\), \(O_\pm=O_b\pm H_O\). At each positive \(t\) the actual same-member value set is exactly
\[
 R(t)=[E_-(t),E_+(t)]\times[O_-(t),O_+(t)].
\]
Both coordinates are simultaneously attainable because the two coefficient blocks are independent. Its four vertices are actual parity-corner values at that frequency. This is a pointwise statement, not a claim that four polynomials generate the whole coefficient box. The origin is absent from every \(R(t)\): otherwise one actual member vanishes at \(i\sqrt t\).

Consider a nontrivial finite relation
\[
 \sum_j w_jr_{a_j}(t_j)+\lambda e_0+\mu e_7=0,\qquad
 w_j,t_j>0,\quad a_j\in K,\quad \lambda,\mu\ge0,
\tag{1}
\]
where
\[
 r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a).
\]
Endpoint rays alone cannot cancel. Actual zero-frequency rows are positive multiples of \(e_0\), because every Hurwitz member has positive constant coefficient; \(e_7\) denotes the infinity ray. Combine repeated endpoints and group the finite atoms at distinct nodes \(0<v_1<\cdots<v_n\). Their total weights \(W_i>0\) and weighted-average pairs \((E_i,O_i)\in R(v_i)\) use the **same** weights for both coordinates. Define \(X_i=W_iE_i\), \(Y_i=W_iv_iO_i\). Equation (1) is exactly
\[
 \sum_iX_i=-\lambda,\quad \sum_iX_iv_i^r=0\ (r=1,2,3);\qquad
 \sum_iY_iv_i^r=0\ (r=0,1,2),\quad \sum_iY_iv_i^3=\mu.
\tag{2}
\]
In particular, pairing the moments with the center coefficients gives
\[
 \sum_iW_iE_iE_b(v_i)=-\lambda b_0,\qquad
 \sum_iW_iv_iO_iO_b(v_i)=-\mu,\qquad b_0>0.
\tag{3}
\]
No parity division is used here, and zeros are retained. If an entire parity block is fixed, its balance in (3) is a nonnegative sum of squares and forces its grouped parity values to vanish. At each such node the other interval avoids zero by origin exclusion, so its grouped value has the same strict sign as its center; the other balance is then strictly positive on the left and nonpositive on the right, a contradiction. Hence **no** relation exists if either whole parity block is fixed. Otherwise both \(H_E,H_O\) are strictly positive for every \(t>0\). The same balances also show neither sequence \(X\) nor \(Y\) can vanish identically.

## 2. Physical bands and five-node interpolation

**Conditional import (precise statement).** For each actual strictly Hurwitz monic real septic, the three positive roots \(x_1<x_2<x_3\) of its even polynomial and the three positive roots \(y_1<y_2<y_3\) of its odd polynomial are simple and satisfy
\[
 x_1<y_1<x_2<y_2<x_3<y_3.
\tag{HB}
\]
The leading and constant signs are as in §1. This is the classical strict Hermite–Biehler septic interlacing statement; its proof is not present here or followed through a link. All results that use physical root bands below retain this import.

Assume both parity blocks vary, as every relation requires. Let \(I_j^E\), \(I_j^O\) be the *complete actual ranges* of the corresponding indexed parity root over \(K\). Simple roots are locally continuous: choose disjoint small intervals around the simple roots with opposite endpoint signs, and use continuity of coefficients and the intermediate value theorem; the cubic degree prevents any extra roots. Compactness and connectedness of each coefficient block therefore make each range a compact interval. The independent blocks can be combined in one actual member, so extrema and (HB) give the strict same-box order
\[
 I_1^E<I_1^O<I_2^E<I_2^O<I_3^E<I_3^O.
\tag{4}
\]
For example, the actual even block attaining \(\max I_j^E\) can be combined with the actual odd block attaining \(\min I_j^O\). The strict root order for that member gives the corresponding strict gap. The bands are nondegenerate: at a center root its parity envelopes have opposite signs, and a sufficiently small positive or negative change in a nondegenerate coefficient moves that simple root to opposite sides. A parity interval contains zero exactly when the frequency is in one of its three actual root bands. On the even bands the complementary odd sign is respectively \(+,-,+\); on the odd bands the complementary even sign is respectively \(-,+,-\), each strictly for **every** actual member. At a band's endpoints its own parity has only the pre-crossing, respectively post-crossing, sign or zero; this is a local statement, not a claim about all other bands.

The moment equations give both physical reverse pairs, including zero cases. Delete zeros only for sign counting. If either nonzero sequence had at most two sign changes, a polynomial of degree at most two with a root in each change gap, suitably oriented, would have strictly positive pairing with every nonzero term of \(v_iX_i\), respectively \(Y_i\), contradicting (2). If exactly three changes occur, choose a monic cubic \(g(t)=\prod_{r=1}^3(t-c_r)\), with one positive \(c_r\) in each change gap. Every nonzero product has the sign of the last nonzero entry, while
\[
 \sum_iX_ig(v_i)=\lambda\prod_{r=1}^3c_r,\qquad
 \sum_iY_ig(v_i)=\mu.
\]
Thus exactly three changes force the corresponding endpoint to be positive and the last sign to be positive. If a parity has no strict reverse pair within any of its three physical bands, its nonzero sign word is a subsequence of the ordinary crossing word \(+,-,+,-\); with three changes its last sign is negative. Contradiction. Therefore each parity has a strict reverse pair inside one of its own bands. One-sided endpoint signs put **both** members of each pair in the strict interior. Opposite-parity bands are disjoint.

Now suppose \(n=5\), without limiting the original atom count. Put
\[
 H(t)=\prod_{i=1}^5(t-v_i),\quad P=\prod_{i=1}^5v_i,\quad
 D_i=H'(v_i),\quad \delta_i=\operatorname{sgn}D_i=(-1)^{5-i}.
\]
Lagrange interpolation of \(v_iX_iD_i\) and \(Y_iD_i\), using the three zero moments in (2), gives unique nonzero linear-or-constant polynomials \(A,B\) with
\[
 X_i={A(v_i)\over v_iD_i},\qquad Y_i={B(v_i)\over D_i},\qquad
 A(0)=-\lambda P,\qquad [t]B=\mu.
\tag{5}
\]
Conversely, (5) implies all of (2): \(\sum_i v_i^r/D_i=0\) for \(0\le r\le3\), and \(\sum_i v_i^4/D_i=1\). The endpoint identity for \(A\) also follows by Lagrange evaluation at zero. No interpolation step divides by a possibly zero \(E_i\) or \(O_i\).

Let \(q_E,q_O\) count zero grouped parities and put
\[
 N^E=\sum_{j=1}^3(\#\{i:v_i\in I_j^E\}-1)_+,\qquad
 N^O=\sum_{j=1}^3(\#\{i:v_i\in I_j^O\}-1)_+.
\]
The reverse pairs yield \(N^E,N^O\ge1\). Inside one closed odd band, complementary \(E_i\) has one strict sign, while consecutive sampled nodes in that interval are consecutive globally, and the signs of their \(D_i\) alternate. Hence \(A\) has a distinct root in each intervening open gap. A sampled \(E\)-zero is a distinct root outside every odd band, and \(\lambda=0\) adds the root zero. Similarly each extra node in an even band forces a distinct gap root of \(B\), and \(\mu=0\) reduces its available degree. Therefore
\[
 q_E+N^O\le1-\mathbf1_{\{\lambda=0\}},\qquad
 q_O+N^E\le1-\mathbf1_{\{\mu=0\}}.
\tag{6}
\]
Thus either missing endpoint is impossible. With both endpoints positive, \(q_E=q_O=0\) and \(N^E=N^O=1\). Exactly two nodes occupy the unique odd reverse band, exactly two occupy the unique even reverse band, and all other bands of each parity contain at most one sampled node. The two pairs are consecutive and have strict interior membership. Let their gap indices be \(p,q\), and let the respective open gaps contain \(\alpha,\beta\). From (5),
\[
 A(t)=a(t-\alpha),\qquad B(t)=\mu(t-\beta),\qquad
 a={\lambda P\over\alpha}>0.
\tag{7}
\]
At the later node of the even reverse pair, actual \(E,O\) have the same strict sign: \(++\) in even bands 1 and 3, \(--\) in even band 2. Since \(B=\mu(t-\beta)>0\) there and
\[
 (A(v_i),B(v_i))=v_iD_iW_i(E_i,O_i),
\tag{8}
\]
\(A>0\) there too. Consequently the odd reverse band precedes the even reverse band, \(\alpha<\beta\), and the two disjoint pairs satisfy \(q\ge p+2\). The only possible rows are

| odd reverse band, even reverse band | \((p,q)\) | strict signs \((E_i,O_i)\), in node order |
|---|---:|---|
| \(I_1^O,I_2^E\) | \((1,3)\) | \((--),(-+),(+-),(--),(++)\) |
| \(I_1^O,I_3^E\) | \((1,4)\) | \((--),(-+),(+-),(-+),(++)\) |
| \(I_2^O,I_3^E\) | \((2,4)\) | \((--),(++),(+-),(-+),(++)\) |

Indeed at the first odd-pair node \(A<0\); its fixed complementary even sign makes \(p\) odd in \(I_1^O\) and even in \(I_2^O\). At the first even-pair node \(B<0\); its fixed complementary odd sign makes \(q\) odd in \(I_2^E\) and even in \(I_3^E\). Together with \(q\ge p+2\) these are exactly the listed indices. Equation (8), with \(\delta_i=(+,-,+,-,+)\), gives the words. These rows are necessary physical constraints, not feasibility claims.

## 3. Exact fixed-box common-\(k\) iff, including every endpoint convention

Fix **any** eligible \(K\) and **any** \(0<v_1<\cdots<v_5\). If an entire parity block is fixed, the answer is no by §1. Otherwise, an actual-member relation (1) on exactly these five distinct nodes with \(\lambda,\mu>0\), without an atom-count cap, exists **if and only if** the following finite/continuous conditions hold simultaneously:

1. Choose one row of the table. Its odd and even pair nodes lie strictly inside the stated actual bands, and the complete closed-band occupancy conditions are \(N^E=N^O=1\). Choose \(\alpha\in(v_p,v_{p+1})\), \(\beta\in(v_q,v_{q+1})\).
2. Put
\[
 \epsilon_i=\operatorname{sgn}[\delta_i(v_i-\alpha)],\quad
 \eta_i=\operatorname{sgn}[\delta_i(v_i-\beta)],\quad
 \rho_i={|v_i-\beta|\over|v_i-\alpha|}>0.
\tag{9}
\]
At every node define the lower and upper **signed magnitudes**
\[
\begin{aligned}
 e_i^-&=\max\{0,\min(\epsilon_iE_-(v_i),\epsilon_iE_+(v_i))\},&
 e_i^+&=\max(\epsilon_iE_-(v_i),\epsilon_iE_+(v_i)),\\
 o_i^-&=\max\{0,\min(\eta_iO_-(v_i),\eta_iO_+(v_i))\},&
 o_i^+&=\max(\eta_iO_-(v_i),\eta_iO_+(v_i)).
\end{aligned}
\tag{10}
\]
Require \(e_i^+>0\) and \(o_i^+>0\) for every \(i\); these are strict-quadrant availability tests in the actual rectangle, not independent fictitious boxes.
3. Define
\[
 L_i={o_i^-\over e_i^+\rho_i},\qquad
 U_i=\begin{cases}{o_i^+\over e_i^-\rho_i},&e_i^->0,\\
 +\infty,&e_i^-=0,\end{cases}\quad
 L=\max_iL_i,\quad U=\min_iU_i.
\tag{11}
\]
Require **one common** \(k\in(0,\infty)\) with \(L\le k\le U\), where \(+\infty\) is not an actual endpoint.

The endpoint rules are exact. A positive lower bound is attained; a zero lower bound is excluded only because \(k>0\). Every finite upper bound is positive and attained; an infinite upper bound is not attained. Thus the common set is \([L,U]\cap(0,\infty)\), with the usual interpretation if \(U=\infty\). It is empty for \(L>U\); when \(L=U>0\) it is the **included singleton** \(\{L\}\); if \(L=0<U<\infty\) it is \((0,U]\); if \(L>0\) and \(U=\infty\) it is \([L,\infty)\); and for \(L=0,U=\infty\) it is \((0,\infty)\). An alleged \(L=U=0\) would be empty, although \(U>0\) follows from the stated strict-availability test. Equal coordinate endpoints, including one-point intervals, require no different convention.

**Ratio lemma.** At one node, the actual positive magnitudes are
\[
 e\in[e_i^-,e_i^+]\cap(0,\infty),\qquad
 o\in[o_i^-,o_i^+]\cap(0,\infty).
\]
For any finite \(t>0\), \(o/e=t\) is possible exactly when
\[
 {o_i^-\over e_i^+}\le t\le
 \begin{cases}o_i^+/e_i^-,&e_i^->0,\\ +\infty,&e_i^-=0.\end{cases}
\tag{12}
\]
To see sufficiency without assuming interior intervals, choose \(e\) in
\([\max(e_i^-,o_i^-/t),\min(e_i^+,o_i^+/t)]\). The two cross inequalities in (12) make this interval nonempty; its upper endpoint is positive. If its lower endpoint is zero choose a positive point below the upper endpoint; otherwise choose the included lower endpoint. Set \(o=te\). This proves both attainability and all open/closed rules, even for degenerate coordinate intervals. The converse follows immediately from the extrema.

**Necessity of the iff.** Given a relation, §2 supplies the row and markers. In (7) set \(k=\mu/a>0\). Equation (8) and \(q_E=q_O=0\) give at every node
\[
 {O_i\over E_i}=k\,{v_i-\beta\over v_i-\alpha},\qquad
 {\eta_iO_i\over\epsilon_iE_i}=k\rho_i,
\tag{13}
\]
with both signed magnitudes positive. The ratio lemma gives every bound in (11) for this **same** \(k\).

**Sufficiency of the iff.** Conversely, take a row, markers and common \(k\) passing the tests. At each node use the lemma to select positive \(e_i,o_i\) with \(o_i/e_i=k\rho_i\) in the two actual signed intervals. Independence supplies one actual member \(a_i\in K\) with the same pair \((E_i,O_i)=(\epsilon_ie_i,\eta_io_i)\). Choose any \(a>0\) and set
\[
 A(t)=a(t-\alpha),\quad B(t)=ak(t-\beta),\quad
 W_i={a(v_i-\alpha)\over v_iD_iE_i}>0,\quad
 \lambda={a\alpha\over P}>0,\quad \mu=ak>0.
\tag{14}
\]
The sign of \(E_i\) is exactly that of \(\delta_i(v_i-\alpha)\), so every displayed \(W_i\) is strictly positive. Equation (13) gives both components of (8); the converse Lagrange identities give all eight coordinates of (1). The resulting five actual members need not be the same polynomial across frequencies, but all belong to the one fixed \(K\), and each node uses one common positive weight and one actual \(E/O\) pair. This proves the iff. It does not solve the remaining existential system or assert a feasible relation.

## 4. Exact chosen-corner budget

For fixed row, markers and common feasible \(k\), let \(c=(E_c(v_i),O_c(v_i))\) range over the four actual vertices of \(R(v_i)\), with coincident vertices retained harmlessly, and define
\[
 V_i=\left\{{\eta_iO_c(v_i)\over\epsilon_iE_c(v_i)\rho_i}:
 \epsilon_iE_c(v_i)>0,\ \eta_iO_c(v_i)>0\right\},\qquad
 J=\#\{i:k\notin V_i\}.
\tag{15}
\]
The positive target ray at node \(i\) has direction
\(T_i=\delta_i(A(v_i),B(v_i))\), and
\[
 T_i=v_i|D_i|\sum_{c}w_{i,c}\,c,\qquad w_{i,c}\ge0.
\tag{16}
\]
A single positive corner atom represents that prescribed grouped contribution exactly iff a vertex lies on this **positive**, not antiparallel, ray, i.e. iff \(k\in V_i\).

If no such vertex exists, two are necessary. They are also sufficient: the feasible positive ray meets the compact actual rectangle, and origin exclusion supplies a coordinate functional strictly positive on the entire rectangle. Thus the ray intersection is compact and is bounded away from the origin. Its farthest point is on the boundary; for a nondegenerate rectangle it lies on an edge, and if not a vertex it is a strictly positive convex combination of that edge's two vertices. For a degenerate rectangle, use its segment endpoints; the same conclusion holds, with the one-vertex case already accounted for. Rescale the two positive coefficients in (16) to represent \(T_i\). Both weighted parities and hence the full grouped eight-coordinate contribution are preserved, although the sum of the corner weights need not equal the original \(W_i\).

Consequently the exact minimum **for these fixed nodes and each fixed grouped contribution** is \(5+J\) finite corner atoms. The two positive combined endpoints contribute two more, so the chosen-corner representation has at most eight total atoms iff
\[
 \boxed{J\le1}\qquad\text{equivalently,}\qquad
 k\text{ belongs to at least four of }V_1,\ldots,V_5.
\tag{17}
\]
For existence under this atom cap, quantify over the same admissible row, markers and common \(k\) in §3 and impose (17). This is not a minimum after moving nodes or redistributing contributions between groups, is not a bound on the number of arbitrary interior-member atoms, and does not assert that a sparse representation or a zero dual exists without the preceding feasibility conditions.

## 5. Strict same-box bandwidth obstruction

For any one of the three physical pairs \((I_a^O,I_b^E)\) in the table define, using the actual envelopes of the **same** fixed box,
\[
\begin{aligned}
 M_{EO}&=\min_{t\in I_a^O}\min(|E_-(t)|,|E_+(t)|),&
 M_{OO}&=\max_{t\in I_a^O}\max(|O_-(t)|,|O_+(t)|),\\
 M_{OE}&=\min_{t\in I_b^E}\min(|O_-(t)|,|O_+(t)|),&
 M_{EE}&=\max_{t\in I_b^E}\max(|E_-(t)|,|E_+(t)|),\\
 c_{ab}&={M_{EO}M_{OE}\over M_{OO}M_{EE}},&
 d_{ab}&=\min I_b^E-\max I_a^O>0.
\end{aligned}
\tag{18}
\]
The complementary-parity minima are strictly positive on the compact bands, and the own-parity maxima are positive and finite since both parity widths vary. Let \(w_a^O,w_b^E\) be the actual band lengths. If a five-node relation uses this pair, then necessarily
\[
 \boxed{w_a^O\,w_b^E>c_{ab}\,d_{ab}^{\,2}.}
\tag{19}
\]

**Derivation.** Let \(i=p+1\), \(j=q\), \(g_p=v_{p+1}-v_p\), \(g_q=v_{q+1}-v_q\), and \(s=v_q-v_{p+1}>0\). The complementary sign and actual rectangle bounds imply
\[
 c_{ab}\le { |O_j|\,|E_i|\over |E_j|\,|O_i|}.
\]
All four factors are nonzero by §2. Dividing the two same-\(k\) instances of (13) gives the exact identity
\[
 { |O_j|\,|E_i|\over |E_j|\,|O_i|}
 = {(v_{p+1}-\alpha)(\beta-v_q)\over
          (\beta-v_{p+1})(v_q-\alpha)}
 < {g_pg_q\over s^2}.
\tag{20}
\]
The last inequality is strict because \(\alpha\) and \(\beta\) lie in their open node gaps: each numerator factor is strictly below its pair gap, while each denominator factor is strictly above \(s\). Since \(s\ge d_{ab}\), \(g_p\le w_a^O\), and \(g_q\le w_b^E\), (19) follows. Nothing substitutes a strict own-parity sign at a band endpoint: the uniform lower bounds use only the complementary parity.

If (19) fails for one listed pair, that pair stratum is excluded on that box. If it fails for all three, there is no five-node relation on that box, including the already-excluded missing-endpoint cases. This is a sufficient exclusion test, not a claim that every eligible box satisfies it.

**A genuinely nonempty class.** Let \(b(s)\) be any fixed strictly Hurwitz monic septic, choose fixed half-width directions \(h_j\ge0\) with at least one positive in each parity, and let \(K_\varepsilon\) have half-widths \(\varepsilon h_j\). For all sufficiently small \(\varepsilon>0\) every actual member is strictly Hurwitz by coefficient/root continuity. Uniformly over this compact shrinking box, the indexed simple parity roots converge to the corresponding roots of \(b\): the disjoint sign-changing neighborhoods described in §2 work for every member once its coefficients are sufficiently close. Thus each actual band length tends to zero, each relevant \(d_{ab}\) tends to a positive center-root gap, and on an odd band its own-parity maximum \(M_{OO}\to0\) while the complementary minimum \(M_{EO}\) tends to a positive value; the analogous statements hold on an even band. Therefore \(c_{ab}\to+\infty\) for each of the finitely many listed pairs, whereas the band-length products tend to zero. There is an \(\varepsilon_0>0\) such that every \(0<\varepsilon<\varepsilon_0\) gives an eligible, genuinely varying box for which (19) fails for all three pairs.

For an explicit nonempty underlying stable family, take \(b(s)=(s+1)^7\) and \(h_j=1\) for every \(j\). For \(\operatorname{Re}s\ge0\), \(|s+1|\ge\max(1,|s|)\), so every \(|\Delta a_j|\le\varepsilon\) satisfies
\[
 \left|\sum_{j=0}^6\Delta a_js^j\right|
 \le7\varepsilon|s+1|^7.
\]
Hence for every \(0<\varepsilon<1/7\) no member of this box has a root in the closed right half-plane. Intersecting this explicit stability range with the positive \(\varepsilon_0\) just established proves the asserted nonempty open family. No numerical test, solver, zero-relation witness, or global synthesis conclusion is used.

## 6. Limitations and complete read/process declaration

* The result concerns exactly five **distinct positive finite nodes**, arbitrary finite positive original actual-member or corner atoms grouped at those nodes, and the two nonnegative endpoint rays. The both-positive iff includes all actual root bands, all five node conditions, a single common ratio, positive weights and the full occupancy test. It is conditional on (HB), and is not a feasibility result. No claim is made for six or more nodes, global SPR/ROOT, sourcebook identity, novelty, priority, human review, independent model family, kernel proof, or parent adoption. The separate \(\le5\) strict-negative no-go is not imported, and no fake feasible dual is constructed.
* Let `R=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. Before any literal packet body or mathematical reasoning, I read this wave's complete `manifest-v1.json`, `freeze-receipt-v1.json`, `final-pre-dispatch-binding-v1.json`, `parent-live-metadata-supply-v1.json`, `actual-dispatch-receipt-v1.json`, and all 22 manifest-listed controls as status/permissions only. Initial structured displays elided administrative fields; complete raw rereads recovered them before acknowledgement. I created `prebody-ack-v1.md` in this wave and sent a **direct** prebody ACK to Main before any packet body. The task target and administrative descriptions were visible before ACK; no scientific body was. Runtime memory summary and the general written-math protocol were read as process context, not scientific input.
* After direct ACK and before mathematical reasoning, I read the sole `literal-packet-part-01-v1.md` serially in raw windows LF 1–20, 21–40, ..., 561–580, including its ending. Each displayed window was at most 20 LF and below 30,000 bytes. No packet display was clipped. One attempted read of LF 381–400 misspelled the packet basename and returned **path not found**; I immediately read the correct LF 381–400 before proceeding to LF 401–420. It exposed no other body and skipped no packet lines. No source link was followed. The parent-supplied packet SHA-256 is `05010754bc62bbb50475983d8c5d7419a04909d9ea83b7158d48b6bb4acdb11e` (580 LF, 74550 bytes); this metadata was not independently recomputed.
* The complete rendered science bodies, in packet order, were: S1 `review-waves/f838-septic-five-node-endpoint-complete-proof-author/author-candidate-v1.md`, LF 1–246, parent pin `f2b5f74f58307d949f9da9904cf62894b10512cec741a7211155db328cb780f7`; S2 `dispositions/info-2-actual-septic-five-node-endpoints-and-six-node-mixed-edge-gap-parent-v1.md`, LF 1–24, pin `66aa98e3a42b337e781a5f95521efc7e4eff51afe850d6939d80913edc11d741`; S3 `review-waves/f816-septic-determinant-minimal-atom-root-budget-proof-author/author-candidate-v1.md`, LF 1–227, pin `4915f3cbc2994c8275c2fc5000d6ff443e719405fc09827220a26b6dbb567f6f`; S4 `dispositions/info-2-septic-positive-determinant-minimal-atoms-root-budgets-and-twelve-patterns-parent-v1.md`, LF 1–31, pin `be3e21d36784dd18d5a035557846bf300f886fb8c39d5fe3f283fb51b2f6ee22`; S5 `dispositions/info-2-actual-septic-strict-band-quadrants-and-low-frequency-subcases-parent-v1.md`, LF 1–30, pin `90ce201156b0ee89e5f09e2e6cf3c4fa9d7eb2c6178a02795c84d84dbd7fa9af`. These hashes are supplied administrative metadata, not independent identity certifications.
* The 22 controls read as status/permission only were the exact full paths and pins in the manifest: `prospective-author-method-scope-restoration-20261030-v1.json`; `contract-addendum-2-frontier-first-owner-direction-v1.json`; the root-level parent L1, privacy auxiliary, core-gram auxiliary, AME held-compression and PH held-registration quarantine controls; the manifest-listed selected-diagnostic process-major quarantine controls in f439, f444, f448, f508, f513, f586, f602, f653, f654, f659, f660 and f662; the selected-instance process-major quarantine control in f596; and the root-level parent remaining-d0-occupancy and prerun-f746/f749 correction controls. Every genuine held episode and all of its proof/method/planning/selection/verification/reporting/confidence/downstream consumers remained NONINPUT. No cognitive-isolation certification is asserted.
* No original linked source, sibling science, held body, old code, network, external model, scientific execution, CAS, solver, child subprocess, test, compilation, build, linter, formatter, Git operation, installation, or deletion was used. No verifier was requested or prepared; a prepared-code hash is not applicable. Independent checking and parent disposition are separate.
