# Direct strict five-node certificates are excluded outside the second odd band

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:09:48 PDT 2026**. **WRITTEN universal theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This concerns the original **strictly negative eight-coordinate atom certificate itself**, not merely an odd-canceling reformulation. It is a partial result: the fifth node inside the second odd band remains open.

## 1. Statement

Let \(K\) be any compact independent monic septic coefficient box, all of whose members are strictly Hurwitz, with global odd-root bands \([a,b],[c,d],[e,f]\). Let five distinct positive squared frequencies satisfy
\[
a<t_1<t_2<b<t_3<t_4<c,\qquad t_5>t_4,\qquad t_5\notin(c,d). \tag{1}
\]
Allow arbitrary actual members of \(K\) at the nodes, positive weights, and any additional zero-odd, zero-frequency or compactified-infinity atoms. Then their aggregate linear pairing functional cannot be **strictly negative in all eight numerator monomial coordinates**.

The construction works for every eligible box and every node tuple in (1), with no fixed corner or scale restriction. It directly excludes part of the five-positive-frequency strict-certificate conjecture. It does not exclude the fifth node in \((c,d)\), other band placements, six or more frequencies, or a general unrestricted SPR7 obstruction.

## 2. Why odd-zero and endpoint atoms do not help

Let \(C_j\) be the weighted aggregate coefficient of numerator monomial \(s^j\). For
\[
F(t)=(-t)(c-t)(d-t)=-cd\,t+(c+d)t^2-t^3, \tag{2}
\]
the corresponding even-only numerator has nonnegative coefficients \(b_2=cd\), \(b_4=c+d\), \(b_6=1\), and all other coefficients zero. If \(C_0,\ldots,C_7<0\), its aggregate pairing is strictly negative.

At an actual odd-root frequency, \(F\) and the actual even component have the same sign on the first, second and third odd bands, allowing equality at band endpoints. Thus every zero-odd row has a **nonnegative** \(F\)-pairing and no odd-coordinate contribution. Delete it: the \(F\) sum remains strictly negative and all odd-coordinate signs remain unchanged. A zero-frequency row has zero \(F\)-pairing and zero odd coordinates. An infinity row has zero \(F\)-pairing and only a nonnegative \(b_7\) coordinate; deleting it keeps all four odd coordinates strictly negative. Merge coincident finite nodes by positive-weight averaging of actual members, which stays inside the box.

The resulting nonzero positive finite measure has four odd coordinates \(V_k<0\), \(k=0,1,2,3\), and a strictly negative \(F\)-pairing. We prove this is impossible.

## 3. Eight exact extreme rays of the odd-moment cone

On nodes \(t_3,t_4\), every actual odd value is negative. If \(t_5\le c\) or \(t_5\ge f\), every odd value at \(t_5\) is nonpositive and no nonzero odd-moment vector \(V\le0\) exists. Otherwise a nonzero measure with \(V\le0\) must have sign word
\[
\operatorname{sgn}O_i(t_i)=(-,+,-,-,+). \tag{3}
\]
To see the sign requirement, let \(m_r=\sum_iw_it_iO_i(t_i)t_i^r\); \(V_r=(-1)^r m_r\le0\). If a nonzero signed sequence begins positive and has at most three sign changes, a product \(\prod(r_j-t)\) with roots placed at those changes matches all its signs; its nonnegative coefficients in the \((-t)^r\) basis make \(\sum_r q_rV_r>0\), contradiction. If it begins negative and has at most two changes, use \((-t)\prod(r_j-t)\). Thus a feasible nonzero sequence contains \((- ,+,-,+)\) or \((+,-,+,-,+)\); under the fixed negative third/fourth nodes only (3) works.

The cone of positive weights satisfying the four weak odd inequalities is pointed. An extreme ray supported on \(s\) finite nodes needs at least \(s-1\) independent active odd inequalities. Support at most three is impossible by the preceding sign lemma; a five-node extreme ray would need all four moments zero, whose Vandermonde null vector has strictly alternating signs, contrary to (3). Therefore every extreme ray has four nodes and the only supports are
\[
X=\{t_1,t_2,t_3,t_5\},\qquad Y=\{t_1,t_2,t_4,t_5\}. \tag{4}
\]
Exactly three odd coordinates vanish on each ray; the fourth is strictly negative. For four ordered support nodes \(u_1<\cdots<u_4\), set \(H(t)=\prod_i(t-u_i)\), and for \(k\in\{0,1,2,3\}\) put
\[
q_i^{(k)}=e_{3-k}(\{u_j:j\ne i\}),\qquad
w_i^{(k)}=\frac{q_i^{(k)}}{u_iO_i(u_i)H'(u_i)}>0. \tag{5}
\]
Here \(e_j\) is the elementary symmetric polynomial, \(e_0=1\). Lagrange interpolation gives the exact identities
\[
\sum_i w_i^{(k)}u_iO_i(u_i)(-u_i)^r=-\mathbf1_{r=k},\quad r=0,1,2,3. \tag{6}
\]
Indeed the coefficient of \(t^k\) in \(H(t)/[(t-u_i)H'(u_i)]\) is \((-1)^{3-k}q_i^{(k)}/H'(u_i)\), and interpolation of \(t^r\) gives (6). Thus (4)–(6) describe **exactly eight** extreme rays. Every nonzero measure in the odd-moment cone is a positive combination of them.

## 4. Every odd-cone ray pairs positively with the same \(F\)

If a ray exists with \(t_5\notin(c,d)\), its fourth node \(u_4\) is in \([d,f)\); its odd value is positive. Let \(U\) be the actual even upper envelope. At every selected node \(F\le0\), so the actual even pairing is at least the pairing with \(U\). The latter has its roots in the three gaps, and Vieta multi-affinity reduces it to the eight vertex cubics
\[
V(t)=(x-t)(y-t)(z-t),\quad x\in\{0,a\},\quad y\in\{b,c\},\quad z\in\{d,e\}. \tag{7}
\]
For any positive odd values consistent with the circuit, replacing the odd value at each node by the appropriate odd endpoint minimizes each term, exactly as in `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`. The following arguments establish positivity for every vertex and every \(k\).

The elementary-symmetric weights in (5) are nonincreasing with the node index: for \(i<j\), the remaining set defining \(q_i\) contains \(u_j\) in place of the smaller \(u_i\) in the remaining set defining \(q_j\). Thus \(q_1^{(k)}\ge q_2^{(k)}\ge q_3^{(k)}\ge q_4^{(k)}>0\), with equality throughout only when \(k=3\).

When \(u_4\in(d,e)\), the named predecessor proves the pairing is strictly positive for the base weights \(k=3\), for all eight vertices. If all four term signs are positive, the weighted sum is positive directly. For \((+,+,+,-)\) and \((+,+,-,-)\), multiplying by the decreasing \(q_i^{(k)}\) preserves strict positivity by factoring out respectively \(q_4\) and \(q_3\). These cover \((y,z)=(c,d),(c,e),(b,e)\).

The remaining case is \((y,z)=(b,d)\), whose term signs are \((+,+,-,+)\). The second and third minimizing odd endpoints are both \(O_+\). Set \(h(t)=(t-u_1)(u_4-t)\). Factor cancellation gives, for \(t\in(u_1,c)\),
\[
\frac{R_+(t)}{h(t)}
=\frac{t-x}{t-u_1}\,
 \frac{d-t}{f-t}\,\frac{d-t}{u_4-t},\qquad
R_+(t)=\frac{F(t)V(t)}{tO_+(t)}. \tag{8}
\]
All three factors are positive and nonincreasing, and the first is strictly decreasing because \(x\le a<u_1\); also \(u_4\ge d\). Hence \(R_+(u_2)/h(u_2)>R_+(u_3)/h(u_3)\), which says the second positive base term alone exceeds the magnitude of the third negative base term. Since \(q_2^{(k)}\ge q_3^{(k)}\), their weighted sum stays positive; the other two terms are nonnegative. This covers the remaining vertex.

At \(u_4=d\) the final \(F\)-contribution is zero. If \(y=c\) the first three contributions are positive; if \(y=b\), the same argument with
\[
\frac{R_+(t)}{h(t)}
=\frac{t-x}{t-u_1}\,\frac{z-t}{f-t}
\]
shows the second term dominates the third for either \(z=d\) or \(e\). If \(u_4\in[e,f)\), the final vertex contribution is nonnegative, and (8) with \(z=d\) or its obvious generalization with \((z-t)(d-t)\) shows the same domination whenever \(y=b\); if \(y=c\), all terms are nonnegative. Thus every extreme ray has strictly positive \(F\)-pairing in all allowed tail regions.

A positive combination of rays also has positive \(F\)-pairing, contradicting §2. This proves the direct strict-certificate exclusion.

## 5. Assurance and remaining gap

The proof uses written Hermite–Biehler/root-band ordering, finite-dimensional cone decomposition, Lagrange interpolation, the named author-written four-node vertex argument, and elementary rational monotonicity. No machine check, independent scientific review, formal proof, parent adoption or novelty clearance is claimed for this general theorem. The unresolved part of this same direct strict-certificate placement is \(c<t_5<d\), where \(F>0\) at the final node and the even **lower**, not upper, envelope must be used; the old upper-envelope gap and actual countermechanism are recorded in `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`, and `frontier-20261029-second-odd-band-fixed-vertex-failure-v1.md`, SHA-256 `acdb9f5b33f4308507929481321adfcc50e3c1eac03450f83e1fd918b5b95755`. Other five-node patterns, all larger supports and the original unrestricted SPR7 verdict remain **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
