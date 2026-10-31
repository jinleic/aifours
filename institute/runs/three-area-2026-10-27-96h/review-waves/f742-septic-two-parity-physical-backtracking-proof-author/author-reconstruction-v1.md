# F742: two-parity physical bands and endpoint-sensitive backtracking

**Status: GENERAL AUTHOR, NONBLIND, WRITTEN CANDIDATE; parent full read and disposition outstanding.** I reconstruct the assigned ordering, fixed-parity boundary, endpoint-sensitive moment obstruction, and both actual-band reverse pairs. I also reconstruct the unadopted eight-atom argument and the six-frequency implication, with the five-frequency strict-negative no-go expressly retained as an import. The strict-interior/corner-orientation refinement, the center-deficit identities, and the independent four-node and endpoint-free five-node exclusions below are additional written consequences. They are **not independently reviewed or adopted here**. Neither reverse-pair necessity nor any finite count proves an eligible zero dual exists, that none exists, or the universal SPR/ROOT problem.

Native clock observed before composing this return: `2026-10-30T17:24:49-0700 PDT`. This is not asserted to be the file-creation or research-start time.

## 1. Object, quantifiers, and exact imports

Fix one compact independent real coefficient box
\[
K=\{s^7+\sum_{j=0}^6a_js^j:\ell_j\le a_j\le u_j\}.
\]
All actual members are strictly Hurwitz; this is the eligibility hypothesis, including degenerate coefficient intervals. Let \(b\) and \(h\) be the center and halfwidths, and for \(t=\omega^2>0\) define
\[
E_a=a_0-a_2t+a_4t^2-a_6t^3,\quad
O_a=a_1-a_3t+a_5t^2-t^3,
\]
\[
H_E=h_0+h_2t+h_4t^2+h_6t^3,\quad H_O=h_1+h_3t+h_5t^2,
\quad E_\pm=E_b\pm H_E,\quad O_\pm=O_b\pm H_O.
\]
At each fixed t the actual pair set is **exactly** the rectangle
\([E_-,E_+]\times[O_-,O_+]\), whose four parity-endpoint pairs are realized by four fixed actual corner polynomials. This is a pointwise rectangle and same-frequency row decomposition; K is not asserted to be the convex hull of four polynomials.

I use the packet's scoped equivalence: eligibility is equivalent to center Hurwitz, \(\ell_0>0\), and no positive t at which both \(|E_b|\le H_E\) and \(|O_b|\le H_O\). Thus equality and tangency matter. More directly, eligibility and independence exclude any frequency at which both actual parity intervals contain zero. I also use the classical Hermite–Biehler strict interlacing statement for a real Hurwitz septic, elementary polynomial interpolation and convexity. I do **not** infer eligibility from corner stability.

The additional imports used only where named are: (i) the same-box zero-hull/strict-SPR alternative, with one monic degree-seven Q and one positive margin; (ii) the previously adopted no-go for an all-eight-strict-negative actual-member aggregate at at most five **distinct positive finite** frequencies; and (iii) the actual-band, all-actual-R4/both-R5/zero-odd/cancellation ROOT interface. The sparse zero-dual reduction is proved below, not simply assumed from the unadopted author S2. The actual no-go and ROOT imports are **not** reproved in full here.

For a nontrivial finite zero relation, let
\[
r_a(t)=(E_a,tO_a,-tE_a,-t^2O_a,t^2E_a,t^3O_a,-t^3E_a,-t^4O_a)
\]
and write
\[
\sum_{j=1}^{m}w_jr_{C_j}(t_j)+\lambda e_0+\mu e_7=0,
\qquad w_j,t_j>0,\quad \lambda,\mu\ge0.\tag{1}
\]
Each \(C_j\) is an actual physical corner. The relation is not the zero combination: at least one finite atom is present, since a nonzero nonnegative combination of \(e_0,e_7\) cannot vanish. The same proofs work for raw actual-member atoms, because their same-frequency endpoint decompositions preserve the aggregate.

Group equal frequencies as \(0<u_1<\cdots<u_n\), with \(W_i>0\) the total raw weight and \(a_i\in K\) the weighted average of the physical corners in that group. This averaged coefficient vector is actual because K is a box. Set \(E_i=E_{a_i}(u_i)\), \(O_i=O_{a_i}(u_i)\). The even and odd values at a given node belong to the **same** grouped member. Grouping does not assert that the entire box has only four members.

## 2. Derivation of the six actual closed bands

First suppose some even and some odd interval have positive width. Then \(H_E,H_O>0\) for every positive t, even if the only nonzero halfwidth is attached to a higher power. In particular the lower and upper envelopes in each parity are strictly ordered at every positive t.

Hermite–Biehler applied to the actual center gives simple positive roots
\[
e_1<o_1<e_2<o_2<e_3<o_3,\tag{2}
\]
where the e's are the roots of \(E_b\) and the o's of \(O_b\). Fix the odd coefficients at their center and take the two actual members with even parts \(E_-\), \(E_+\). Since both are Hurwitz and have the same odd part \(O_b\), each even envelope has exactly one simple root in each of
\((0,o_1),(o_1,o_2),(o_2,o_3)\). At \(e_j\) the lower and upper even envelopes have opposite strict signs, so their roots in the jth interval straddle \(e_j\). Their successive crossing directions are down, up, down. Consequently
\[
\{t>0:E_-(t)\le0\le E_+(t)\}
=I^E_1\cup I^E_2\cup I^E_3,
\quad I^E_j=[L^E_j,R^E_j],
\]
where each closed interval has distinct positive finite endpoints, contains \(e_j\) strictly, and the three intervals are disjoint.

Similarly fix the even coefficients at their center and vary the odd coefficients to realize \(O_-\), \(O_+\). Their roots lie one each in
\((e_1,e_2),(e_2,e_3),(e_3,\infty)\), and they define disjoint closed intervals \(I^O_j=[L^O_j,R^O_j]\), each containing \(o_j\) strictly. Both parities have certain signs \(+,-,+,-\) on their successive complementary regions. Explicitly, the lower envelope crosses first in bands 1 and 3, whereas the upper envelope crosses first in band 2.

An even band and an odd band cannot intersect, **including at endpoints**. At a common t both actual intervals would contain 0; independence would realize a single actual member with \(E=O=0\), contrary to strict Hurwitz stability. Since the ordered center roots (2) lie strictly inside their corresponding connected bands, the whole intervals must satisfy
\[
I^E_1<I^O_1<I^E_2<I^O_2<I^E_3<I^O_3.\tag{3}
\]
Here \(I<J\) means every point of I is strictly below every point of J. This conclusion uses the actual box and its actual envelope roots; arbitrary ordered markers are not asserted realizable or eligible.

## 3. Fixed and degenerate parity cases

The preceding six positive-width bands are **not** invoked if an entire parity is fixed. Relation (1) is nevertheless impossible in either fixed-parity case.

If O is fixed, \(O_a=O_b\). Pair (1) with a coefficient test vector having even part zero and odd part \(O_b\). Its finite contribution is \(\sum_iW_i u_iO_b(u_i)^2\ge0\), and its infinity contribution is \(\mu\ge0\). Hence \(\mu=0\) and every \(O_b(u_i)=0\). At each such node the actual even interval cannot contain 0, and \(E_i\) and \(E_b(u_i)\) have the same nonzero sign. Pairing with even part \(E_b\), odd part zero, gives a strictly positive finite sum plus \(\lambda b_0\ge0\), contradiction.

If E is fixed, first pair with even part \(E_b\), odd part zero. The finite terms are \(W_iE_b(u_i)^2\ge0\), and the zero-endpoint term is \(\lambda b_0\) with \(b_0>0\). Thus \(\lambda=0\) and each \(E_b(u_i)=0\). There the actual odd interval avoids 0, so \(O_i\) and \(O_b(u_i)\) have the same nonzero sign. Pairing with even part zero and odd part \(O_b\) gives strictly positive finite terms plus \(\mu\ge0\), again impossible. These linear test vectors need not be stable or coefficientwise positive. The argument includes both parities fixed, and intervals of zero width elsewhere.

Consequently a zero dual on an eligible box requires a nondegenerate interval in **each** parity. Using the imported zero-hull alternative, each fixed-parity eligible box has strict common-SPR; this is not a same-box weak-to-strict theorem. From now on assume both parities genuinely vary, so (3) applies.

## 4. Exact endpoint moments, including zero entries

Define
\[
X_i=W_iE_i,\qquad Y_i=W_i u_iO_i.
\]
Reading all eight coordinates of (1), with no endpoint omitted, gives
\[
\sum_iX_i=-\lambda,\quad \sum_iX_i u_i^k=0\ (k=1,2,3),\qquad
\sum_iY_i u_i^k=0\ (k=0,1,2),\quad \sum_iY_i u_i^3=\mu.\tag{4}
\]
Neither sequence is identically zero. If all \(E_i=0\), at each node the odd interval avoids zero, so \(O_iO_b(u_i)>0\); the odd test \(O_b\) gives strictly positive finite pairing plus \(\mu\ge0\), contradiction. If all \(O_i=0\), the even interval avoids zero and the even test \(E_b\) gives the analogous contradiction. This uses the actual parity rectangle, including grouped members.

Remove zero entries **only for sign counting**, preserving their nodes and values in every equation. Both nonzero sign words have at least three changes. Indeed, if Y had at most two, choose a real polynomial of degree at most two with one root in each gap between consecutive sign blocks, and choose its overall sign so every nonzero \(Y_i p(u_i)>0\). This contradicts the first three Y moments in (4). For X apply the same argument to \(u_iX_i\), whose signs equal those of X and whose moments of degrees 0,1,2 vanish.

If Y has exactly three changes, take a **monic cubic** p with one positive root \(\xi_j\) in each of the three sign-change gaps. All nonzero \(Y_i p(u_i)\) have the sign of the last nonzero Y entry, and their sum is \(\mu\). Thus \(\mu>0\) and that last sign is positive. For exactly three changes of X, the same p gives
\[
\sum_i X_ip(u_i)=p(0)(-\lambda)=\lambda\xi_1\xi_2\xi_3.
\]
Thus \(\lambda>0\) and the last nonzero X sign is positive. In particular
\[
\lambda=0\Rightarrow\operatorname{var}(X)\ge4,\qquad
\mu=0\Rightarrow\operatorname{var}(Y)\ge4.\tag{5}
\]
These are sign variations **after zero deletion**. If exactly three changes occur, the first nonzero sign is negative and the last positive; if there are four or more, no last-positive conclusion is asserted. Since \(W_i,u_i>0\), X and Y have the actual grouped even and odd signs respectively. No division by an odd or even value is made.

## 5. Reverse pairs in EACH physical parity; endpoint sharpening

Fix either parity and temporarily write its sampled values as V. Suppose no reverse pair occurs in any of its three actual bands. In bands 1 and 3, the nonzero sampled values can only progress from positive to negative; in band 2 they can only progress from negative to positive. Outside the bands the signs are the certain signs \(+,-,+,-\). Hence, after deleting zeros, the complete sampled sign word is a subsequence of the four-block word \(+,-,+,-\). It has at most three changes, and if it has exactly three its final sign is negative. This contradicts Section 4. Therefore each parity has a pair of distinct positive frequencies in **one and the same actual band** with
\[
\begin{array}{ll}
\text{band 1 or 3:}&u_i<u_j,\quad V_i<0<V_j;\\
\text{band 2:}&u_i<u_j,\quad V_i>0>V_j.
\end{array}\tag{6}
\]
The even and odd bands are disjoint by (3); therefore the two required pairs use at least four distinct physical frequency groups. This holds for the **same** zero relation, not for separately selected boxes. The grouped values in (6) may mix physical corners, and the pair condition is necessary, not sufficient.

The actual endpoint geometry sharpens (6): **both nodes of every such reverse pair lie in the strict interior of the relevant band**. For a downward band, before and at its left endpoint every actual value is nonnegative, and after and at its right endpoint every actual value is nonpositive. Thus a negative earlier value and positive later value must both lie strictly between the endpoints. The upward-band argument reverses signs. There the strict envelope signs are \(V_-<0<V_+\).

This also forces physical corner orientations, even if a group contains several corners. In a downward band the earlier negative group has positive total weight on a parity-lower corner and the later positive group has positive total weight on a parity-upper corner. In an upward band the earlier positive group uses a parity-upper corner and the later negative group a parity-lower corner. If a relevant group consists of a single corner, that corner has the indicated orientation. The opposite parity is strictly nonzero throughout that band. In particular, E-band 1/2/3 have certain O signs \(+,-,+\), while O-band 1/2/3 have certain E signs \(-,+,-\). No pointwise pair is promoted to a full-box four-corner hull claim.

### 5.1. Center-deficit identities

Pair (1) with even part \(E_b\), odd part zero, and then with even part zero, odd part \(O_b\). These are unrestricted linear tests, and give the exact identities
\[
\sum_iW_iE_iE_b(u_i)=-\lambda b_0,\qquad
\sum_iW_i u_iO_iO_b(u_i)=-\mu.\tag{7}
\]
For each parity the reverse pair implies at least one **strict center-sign mismatch**: in a downward band either the earlier negative value lies left of its center root or the later positive value lies right of it; the upward-band statement is analogous. This remains true if one sampled node is exactly the center root. Thus the negative parts of both sums in (7) are nonzero. More explicitly, if \(z_+=\max(z,0)\),
\[
\sum_i[-W_iE_iE_b(u_i)]_+
=\lambda b_0+\sum_i[W_iE_iE_b(u_i)]_+>0,
\]
\[
\sum_i[-W_i u_iO_iO_b(u_i)]_+
=\mu+\sum_i[W_i u_iO_iO_b(u_i)]_+>0.\tag{8}
\]
These give endpoint-sensitive necessary balances for any proposed actual dual; they are not contradictions and do not show the necessary conditions are attainable.

## 6. Coupling to the eight-atom and six-frequency claims

### 6.1. Compact connected support gives at most eight atoms

Normalize the four physical corner curves by \((1+t)^{-7}\), including the actual zero endpoint \(a_0e_0\) and the common infinity endpoint \(e_7\). Their union S is compact and path connected: every curve is continuous on \([0,\infty]\) and all meet at \(e_7\). If 0 lies in its convex hull, Carathéodory gives at most nine points of S in \(\mathbb R^8\).

If nine points are necessary in a chosen representation, they are affinely independent \(p_0,\ldots,p_8\) with strictly positive coefficients \(\alpha_i\). Choose a continuous path \(p(s)\) in S from \(p_0\) to \(p_1\), and use the affine coordinates \(p(s)=\sum_i c_i(s)p_i\), \(\sum_i c_i(s)=1\). While \(c_0>0\),
\[
0={\alpha_0\over c_0}p(s)+\sum_{i=1}^8
\left(\alpha_i-{\alpha_0c_i\over c_0}\right)p_i.
\]
At the starting point all coefficients are positive. As the first zero of \(c_0\) is approached, at least one other \(c_i\) stays positive because their sum tends to one; its displayed coefficient becomes negative. By continuity, before that time some displayed coefficient first vanishes while the others are nonnegative. This yields a convex representation using the path point and at most seven of \(p_1,\ldots,p_8\). Thus at most eight compactified atoms suffice; cases already using at most eight need no reduction.

Convert a normalized finite coefficient \(\alpha\) to raw weight \(\alpha/(1+t)^7\). Combine zero-endpoint and infinity-endpoint contributions into \(\lambda e_0\) and \(\mu e_7\). Conversely, any raw (1) normalizes to a nontrivial convex zero relation using an actual zero endpoint \(a_0e_0\), with its positive factor accounted for, plus \(e_7\). Neither endpoint is silently discarded.

### 6.2. Every zero relation has at least six distinct finite groups

For \(1\le n\le3\), this is independent of the imported five-frequency theorem. Interpolate a polynomial F of degree at most 3 with \(F(0)=1\) and \(F(u_i)=E_i\), and interpolate \(G(t)=-t^3+H(t)\), \(\deg H\le n-1\), with \(G(u_i)=O_i\). The resulting coefficient test has \(q_0=q_7=1\). Pairing (1) gives
\[
0=\sum_iW_i(E_i^2+u_iO_i^2)+\lambda+\mu>0,
\]
a contradiction because each \(a_i\) is an actual eligible member. The test polynomial is not claimed Hurwitz. Section 7 below also excludes n=4 independently, and the n=5, \(\lambda=\mu=0\) subcase independently.

For the full n=4 or 5 statement I additionally reconstruct the S2 steering and **retain** the S4 no-go import. Compactness of K and openness of Hurwitz stability give an eligible enlargement L with positive buffers in both coefficient coordinates 0 and 1. Choose four distinct finite groups \(u_1,\ldots,u_4\) and Lagrange polynomials \(L_i(x)\) for those nodes. Perturb only their two coefficients by
\[
\delta a_{0,i}=-\epsilon\,{L_i(-1)\over W_i},\qquad
\delta a_{1,i}=-\epsilon\,{L_i(-1)\over W_i u_i}.
\]
For sufficiently small positive \(\epsilon\) these selected members lie in L. Since \(\sum_iL_i(-1)u_i^k=(-1)^k\) for \(0\le k\le3\), their finite raw aggregate changes by exactly \((-\epsilon,\ldots,-\epsilon)\). The relation (1) then becomes an all-eight-strict-negative finite aggregate on L, at exactly the original n frequencies:
\[
(-\lambda-\epsilon,-\epsilon,-\epsilon,-\epsilon,
-\epsilon,-\epsilon,-\epsilon,-\mu-\epsilon).
\]
For n=4 or 5 this contradicts the **imported** eligible at-most-five-frequency strict-negative no-go. L is a buffered enlargement; this does not turn a same-box zero dual into a same-box strict-negative aggregate.

Combining Sections 6.1–6.2, if a zero dual exists, there is a chosen actual-corner relation with \(6\le n\le m\),
\[
m+z\le8,\qquad z=\mathbf1_{\lambda>0}+\mathbf1_{\mu>0}.
\]
If M is the number of frequency groups containing more than one finite corner atom, then \(M\le m-n\le8-z-n\). Hence:

| distinct n | present endpoints z | maximum mixed groups | minimum single-corner groups |
|---|---:|---:|---:|
| 6 | 0 | 2 | 4 |
| 6 | 1 | 1 | 5 |
| 6 | 2 | 0 | 6 |
| 7 | 0 | 1 | 6 |
| 7 | 1 | 0 | 7 |
| 8 | 0 | 0 | 8 |

All other n/z combinations with \(6\le n\) exceed the eight-atom limit. In particular, when n=6 and both endpoints occur, all six finite groups are single physical corners, and the reverse-pair corner orientations in Section 5 apply individually. This is a property of the **chosen sparse representation**, not of every original representation. No rationality of nodes, existence of an eligible dual, or global proof follows.

## 7. Further independent low-node obstructions from physical quadrants

The following written argument supplies two subcases without importing the five-frequency no-go. It is an additive reconstruction; it does not replace the import in the general six-frequency claim.

For a strict pair of grouped signs, the only frequency windows where that quadrant is possible are as follows, by the envelope signs and (3):
\[
\begin{array}{c|l}
(E,O)&\text{possible positive-frequency windows}\\\hline
(+,+)&(0,R^E_1)\ \cup\ (L^O_2,R^E_3),\\
(-,-)&(L^O_1,R^E_2)\ \cup\ (L^O_3,\infty),\\
(-,+)&(L^E_1,R^O_1)\ \cup\ (L^E_3,R^O_3),\\
(+,-)&(L^E_2,R^O_2).
\end{array}\tag{9}
\]
For example, \((+,+)\) requires \(E_+>0\) and \(O_+>0\); independence makes these conditions sufficient to realize the strict pair, and the other rows are analogous. The possible \((+,+)\) and \((-,-)\) windows occur in the order
\((+,+)_1<(-,-)_1<(+,+)_2<(-,-)_2\), with gaps. The possible \((-,+)\) and \((+,-)\) windows occur in the order
\((-,+)_1<(+,-)<(-,+)_2\). These are strict-sign windows; zero values are not assigned a sign.

**No four finite groups, independently of the five-frequency import.** At n=4, (4)–(5) force \(\lambda,\mu>0\), and both X and Y have four nonzero entries and exactly three sign changes. Let \(H_4(t)=\prod_{i=1}^4(t-u_i)\) and \(P=\prod_i u_i\). Vandermonde nullity and interpolation give
\[
X_i={\lambda P\over u_iH'_4(u_i)},\qquad
Y_i={\mu\over H'_4(u_i)}.
\]
For the X coefficient use \(\sum_i1/(u_iH'_4(u_i))=-1/P\); for Y use \(\sum_i u_i^3/H'_4(u_i)=1\). Since both endpoint coefficients are positive, each parity has the same sign sequence \(-,+,-,+\). The four required strict quadrants are therefore
\((-,-),(+,+),(-,-),(+,+)\), impossible in the first window order in (9). This uses the physical band ordering, not numerical probes or the imported no-go.

**No five finite groups when both endpoint weights vanish, independently of that import.** If \(n=5\) and \(\lambda=\mu=0\), all moments of degrees 0 through 3 vanish for both X and Y. For \(H_5(t)=\prod_i(t-u_i)\), the one-dimensional Vandermonde nullspace gives
\[
X_i={c\over H'_5(u_i)},\qquad Y_i={d\over H'_5(u_i)},\qquad c,d\ne0.
\]
Consequently both sign sequences alternate without zeros. If cd>0, the strict quadrant sequence alternates between \((+,+)\) and \((-,-)\) five times; (9) permits at most four such alternating windows. If cd<0, it alternates between \((-,+)\) and \((+,-)\) five times; (9) permits at most three. Both are impossible. This proof does not cover the remaining n=5 endpoint patterns, for which Section 6.2 retains the imported no-go.

## 8. Exact scope, corrections, and unpaid frontier

Subject to the explicit imports, for every fixed eligible independent K, failure of strict common-SPR yields a same-box physical zero relation with at most eight total finite/endpoints atoms, six to eight distinct positive finite frequencies, the exact endpoint moments (4), a strict-interior reverse pair in each distinct physical parity, the orientation constraints and balances above. Conversely any actual nontrivial zero relation (1) excludes strict common-SPR on that same K by the imported compact-hull alternative. This is an **alternative conditional on the imported equivalence**, not an example or a universal answer.

No defect was found in the S2 band order, endpoint moments, stated reverse-pair implication, or its connected-hull/steering arguments at the scope reconstructed here. The strict-interior, physical-corner, balance and Section 7 claims are additive refinements rather than edits to that unadopted candidate. The S2 source's own references to S1–S4 denote labels in **its** earlier packet; in this return S4 is the actual-band/five-frequency disposition specified in the present manifest. I do not assert independent reconstruction of every theorem or scientific link mentioned by S2.

A feasible strict same-box SDP involves ONE monic septic Q, ONE \(\eta>0\), and its eight PSD blocks/32 coefficient equations across the four actual corners. Under its exact nondegenerate-odd and actual-cone imports it supplies ONE strict-interior ROOT triple for every actual R4 and both R5 orientations, including zero-odd and cancellation cases. None of the band/sign/atom conditions above proves that SDP feasible or infeasible, establishes the all-ray ROOT assertion, obtains a same-box weak-to-strict implication, or constructs an eligible obstruction. The remaining first-order/universal problem is to exclude **all** eligible boxes and actual relations satisfying the full coupled equations, or exhibit and verify an actual eligible box and exact relation; neither is done. The imported buffered universal bridge applies to an enlargement, not a same-box shortcut.

**NOT TESTED / NOT CLAIMED:** no scientific executable, finite enumeration, solver, QE, test, build, formatter, lint, public-source search, external-model call, actual eligible counterexample, universal common numerator, actual ROOT triple, human review, independent model-family review, formal/kernel verification, source-identity audit, or literature/novelty/priority determination. No proposed finite source or GO is supplied. Parent full read, independent check, and explicit disposition are separate and not automatic.

## 9. Complete coverage, pins, process and exclusions

Wave root R: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. All paths below are R plus the stated suffix; they are source-body identifiers from the manifest, not outgoing links followed during this task.

* S1 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1-erratum-1.md`, complete LF1–5, SHA-256 `513b44b2591954b535e138df611fab0698af2b8363b89768a5e45f320d50f5d4`.
* S2 `review-waves/f734-actual-septic-global-root-or-eligible-zero-dual-frontier-author/author-candidate-v1.md`, complete LF1–182, SHA-256 `fd95da21d7ae3517475dae09516591688479c6bbddbfa593b452d5d48827b575` (UNADOPTED, nonblind author input).
* S3 `dispositions/info-2-actual-both-parity-septic-four-corner-sdp-and-zero-dual-parent-v1.md`, complete LF1–29, SHA-256 `949af8c879058b8be166086ab06dbba03d896a26adc64e1621dfbdf7a72e4d0b`.
* S4 `dispositions/info-2-actual-box-three-root-dual-odd-cone-and-six-node-sparsification-parent-v1.md`, complete LF1–46, SHA-256 `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`.
* S5 `review-waves/f706-septic-eligibility-and-root-dual-quantifier-independent-author/author-reconstruction-v1.md`, complete LF1–200, SHA-256 `ffbb995d00381931c2895e332b86e1b2ee124890d605e0dcdf415025c97c075b`.

The complete single rendered packet part is `review-waves/f742-septic-two-parity-physical-backtracking-proof-author/literal-packet-part-01-v1.md`, LF1–484, SHA-256 `83a4b7c6c626ecfecbbaa5b1b6453b193ad86553c1abb7d2eea706d46b7941ae`; I read it serially in consecutive raw windows of at most 20 LF through its ending before mathematical research. Parent freeze metadata reports source-roundtrip and persisted-byte equality; I did not independently re-render or authenticate the original source files. I did not open packet outgoing scientific links or the separately referenced multipart-policy file.

Before packet-body access I read the complete actual dispatch, manifest, freeze receipt, final binding, prepared metadata, and **all 22 manifest-listed permission/status controls** through their endings, then sent Main the direct PREBODY ACK. Observed wave metadata SHA-256: manifest `eee10a5289a5d451f5c818ccfb26f345482d0a5cc630419edd7a17ed2c01392c`; freeze `3dfd68fe8671b97b8d5bb4163353fe56d5bba0b199e4107a96f26832751cc443`; final binding `eb98f9b9a15c268160d12d98f06f254d7704cd03da59d41330d134b877842e9a`; prepared metadata `ab85154a843a624a83b0aa4d9d3ebc30c31d7c893f218d2695cd07b8f43fa2bc`; actual dispatch `0828cd67ba3d8bd5c302a31fcd3f5aae8dccba7ca4cfe1f12432ae0ffeb39035`.

**Sequencing disclosure:** Before that ACK and before body access I used administrative `wc -l` and `shasum -a 256` on the wave controls and the unopened packet, and included the packet SHA as metadata in the ACK. This exposed the live digest alongside its declared digest before the complete packet read. It was not a body read, rerender, or scientific calculation, but whether it implicates the literal pre-comparison sequencing rule is for Main to adjudicate; I disclosed it directly without backdating. No private-cognition certificate is asserted.

No held episode, held history or method, held proof, or any held proof/method/selection/planning/verification/reporting/confidence/downstream consumer was read as scientific input. No unspecified sibling proof, old code, child scientific execution, Git, install, deletion, paid/heavy or live-infrastructure action was used. Administrative metadata/hash observation and this exclusive one-write return are not scientific execution. This nonblind same-harness author return is not a parent disposition or a family/human/kernel gate.
