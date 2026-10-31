# Convex Vieta geometry of the complete septic synthesis region

Owner InfoSPR7-2, info-2. Native clock observed before writing: **Thu Oct 29 15:42:50 PDT 2026**. **WRITTEN universal synthesis-coupling theorem candidate**, not parent-adopted, independently reviewed, formally verified or novelty-cleared. It concerns every possible common numerator of every eligible box, not a selected numerator profile. The original arbitrary-box existence decision remains open.

## 1. Result

Let \(K\) be any nonempty bounded closed independent monic septic coefficient box, with degenerate intervals allowed, and assume every member strictly Hurwitz. Let \(\mathcal B_K\) be the set of all real exact-degree-seven common SPR numerators, positively normalized by \(b_6=1\). Let
\[
 U_K=\{(b_0,b_2,b_4):b\in\mathcal B_K\}.
\]
Then:

1. \(\mathcal B_K\), in its seven-dimensional affine coefficient space, is an **open convex** set. Consequently \(U_K\) is an **open convex** subset of \(\mathbb R^3\). Either may be empty.
2. Every \(b\in\mathcal B_K\) is Hurwitz, and \(E_b(t)=b_0-b_2t+b_4t^2-t^3\) has three simple positive roots \(x_1<x_2<x_3\). The feasible pole set \(X_K\), consisting of these root triples, is the inverse image of \(U_K\) under the Vieta map
\[
V(x_1,x_2,x_3)=(x_1x_2x_3,\ x_1x_2+x_1x_3+x_2x_3,\ x_1+x_2+x_3). \tag{1}
\]
If nonempty, \(X_K\) is open and **contractible**, hence path-connected and without holes. It is convex after the Vieta change of variables, not asserted convex in the ordinary \(x\)-coordinates.
3. The entire allowed root-gap domain has a simple **linear** description in the Vieta variables, and \(U_K\) is a projection of one exact strict finite semidefinite feasibility problem. Thus the nonlinear-looking three-pole search from the partial-fraction representation can be convexified without excluding any valid numerator.

This is a universal structural and constructive reduction. It does not establish that \(U_K\) is nonempty for every stable box, or that any particular simple even polynomial belongs to it.

## 2. Root-gap polyhedron

For every actual denominator write \(a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t)\). Each parity cubic has three simple positive roots. Let \([\underline o_i,\overline o_i]\) be the range of the \(i\)-th odd root across the odd coefficient box. Independence of the two parity parts, compactness, and the odd-degree Hermite–Biehler criterion imply the strict separation
\[
0<\underline o_1\le\overline o_1<\underline o_2\le\overline o_2
<\underline o_3\le\overline o_3.
\]
The strict gaps follow by combining root-extremizing actual even and odd parts into one actual stable denominator. Root ranges are intervals by continuity on the connected parity coefficient box.

For any common \(b\), \(E_b\) has sign \(-,+,-\) on the respective odd-root bands: at an actual odd-root frequency the pairing is \(E_aE_b>0\), and \(E_a\) has that sign for every even part. Since \(E_b(0)>0\) and its degree is three, its roots obey
\[
0<x_1<\underline o_1,\quad
\overline o_1<x_2<\underline o_2,\quad
\overline o_2<x_3<\underline o_3. \tag{2}
\]
Conversely, (2) is **exactly** the following open polyhedron of coefficient triples \(e=(e_0,e_2,e_4)\), where \(E_e(t)=e_0-e_2t+e_4t^2-t^3\):
\[
\begin{aligned}
 e_0&>0,\\
 E_e(\underline o_1)&<0,&E_e(\overline o_1)&<0,\\
 E_e(\underline o_2)&>0,&E_e(\overline o_2)&>0,\\
 E_e(\underline o_3)&<0. \tag{3}
\end{aligned}
\]
Every row in (3) is linear in \(e\). The signs give a root in each of the three disjoint intervals in (2); cubic degree makes them the only roots and makes each simple. The converse follows from the factored sign pattern. Thus the full root-gap box, although not generally convex in ordinary root coordinates, has a **bounded open convex polyhedral** Vieta image. Degenerate odd bands cause duplicate inequalities, not a different argument.

## 3. Open convexity and an explicit pole homotopy

For a common exact-degree numerator \(b\), positivity on the imaginary axis forces its leading coefficient \(b_7>0\). Indeed \(b/a\to b_7\) as \(|\omega|\to\infty\), and exact degree rules out zero. The path \((1-\theta)a+\theta b\), for any fixed \(a\in K\), has no imaginary-axis root because its ratio to \(a\) has positive real part. Its leading coefficient remains positive, so root continuity proves \(b\) Hurwitz. In particular \(b_6>0\), making the normalization \(b_6=1\) legitimate and unique under positive scaling.

At \(t=\omega^2\), let \(P_{a,b}(t)=E_aE_b+tO_aO_b\). It is linear in \(b\). At fixed \(t\), the minimum over the independent box occurs at one of its four actual parity corners. Hence convex combinations of normalized common numerators remain common. Since \(b_7>0\), the compactified pairing \(P_{a,b}(t)/(1+t)^7\) is strictly positive also at infinity. Compactness over four corners and \(t\in[0,\infty]\) supplies a uniform positive margin; sufficiently small coefficient perturbations preserve it. This proves openness and convexity of \(\mathcal B_K\).

The coordinate projection \(b\mapsto(b_0,b_2,b_4)\) is a surjective linear map from the affine space \(b_6=1\) to \(\mathbb R^3\), hence maps an open set to an open set; it also preserves convexity. Therefore \(U_K\) is open and convex. Every element lies in (3).

The Vieta map (1) is a smooth bijection with smooth inverse between the ordered-root region (2) and its coefficient image: the roots are simple, and the Jacobian is a nonzero Vandermonde product. Its inverse sends \(U_K\) exactly to the feasible pole set \(X_K\). If \(X_K\ne\varnothing\), fix \(x^*\in X_K\) and define
\[
H(x,\theta)=V^{-1}\bigl((1-\theta)V(x)+\theta V(x^*)\bigr),\qquad 0\le\theta\le1.
\]
The argument of \(V^{-1}\) remains in the convex set \(U_K\), so this is a continuous contraction of \(X_K\) to \(x^*\). Equivalently, for any two feasible pole triples, coefficientwise interpolation of their normalized even polynomials yields a three-real-root polynomial whose root triple is feasible all along the path. No pole-feasibility path is assumed when \(U_K\) is empty.

## 4. One exact global convex synthesis problem

For each actual parity corner \(a\), compactify
\[
Q_{a,b}(u)=(1-u)^7P_{a,b}\!\left(\frac{u}{1-u}\right),\qquad 0\le u\le1,
\]
with its polynomial endpoint value \(Q_{a,b}(1)=b_7\). Let \(v_3(u)=(1,u,u^2,u^3)^T\). The original box has a common numerator **if and only if** the following strict semidefinite system is feasible:
\[
\begin{aligned}
 b_6&=1,\\
 Q_{a,b}(u)&=u\,v_3(u)^TA_av_3(u)+(1-u)\,v_3(u)^TB_av_3(u)
 &&\text{for each of the four corners},\\
 A_a&\succ0,\quad B_a\succ0
 &&\text{for each of the four corners}. \tag{4}
\end{aligned}
\]
The eight coefficient equations per corner are affine in \(b,A_a,B_a\), and the eight Gram matrices are \(4\times4\). Thus (4) is a **single convex strict LMI feasibility problem** in all numerator coefficients, not a local search over fixed poles. The inequalities (3) can be added as universal necessary linear cuts, although they are already implied by (4).

For the forward direction, each \(Q_{a,b}>0\) on \([0,1]\). Choose \(\epsilon>0\) so small that \(Q_{a,b}-\epsilon\sum_{j=0}^3u^{2j}>0\) on that interval. The one-variable odd-degree Markov–Lukács theorem represents that remainder as \(u\sigma_1+(1-u)\sigma_0\), with each sum of squares of polynomials of degree at most three. Add \(\epsilon I\) to both Gram matrices to obtain (4). Conversely, each right-hand side is strictly positive on \([0,1]\), since \(v_3\ne0\) and at least one of \(u,1-u\) is positive. In particular \(b_7=Q_{a,b}(1)>0\); four-corner affine minimization then gives the original all-frequency inequalities and exact degree seven.

For rational box endpoints, feasibility also has a fully rational certificate: the affine coefficient equations are defined over \(\mathbb Q\), their rational points are dense in the real solution affine space, and strict positive definiteness is open. One may therefore output rational \(b,A_a,B_a\) and verify coefficient identities and Sylvester principal minors exactly. The theorem is a sound and complete method for each fixed box; it does not claim a uniform runtime, run an SDP, or prove feasibility for every box.

## 5. A certified nonempty Vieta region for one difficult box

The explicit full-width box and numerator in `frontier-20261029-difficult-box-pole-synthesis-frozen-v1.json`, SHA-256 `1efd0db940af93860cd909b804bf421e60b7c20223ab0076d04a09e8c95724e5`, provide an example conditional on that separately inspectable same-host arithmetic certificate. Its monic numerator has \(b_6=31447/2000\), even roots \((1,35,455)\), and compactified four-corner pairing margin greater than \(10^{-13}\). After normalization \(b_6=1\), its Vieta point is
\[
 e^*=(15925,16415,491).
\]
The same fixed normalized odd coefficients work for every \(e\) in the closed coordinate cube \(\|e-e^*\|_\infty\le10^{-22}\). Indeed the upper endpoint sum of the box, including the monic coefficient, is
\[
 S_A=2089215543313/250000,
\]
and the normalized pairing margin exceeds \(1/157235000000000\). Perturbing the three even coefficients by at most \(\epsilon\) changes each normalized pairing by at most \(3\epsilon S_A\); exact rational arithmetic gives
\[
6\cdot10^{-22}S_A<1/157235000000000.
\]
The resulting box of \(e\)-values therefore lies strictly inside \(U_K\). This is an illustration of a genuinely open convex feasible region for one box, not evidence that every eligible box has a nonempty region.

## 6. Imports and residual

Named standard imports: odd-degree Hermite–Biehler interlacing, root continuity and finite-dimensional compactness, elementary Vieta/Jacobian facts, and the one-variable interval Markov–Lukács SOS theorem. All reductions and the openness/convexity proof are given explicitly. The illustrative cube relies on the **named, unreviewed** arithmetic certificate rather than treating it as adopted. No held historical source or external model is a premise; the parent-classified incidental search-display exposure remains recorded in `owner-incidental-held-source-search-display-v1.json`, with no clean-cognition claim.

The exact residual is the original one: prove that (4) is feasible for **every** eligible septic box, or supply one eligible box with a rigorous unrestricted infeasibility certificate. This packet gives neither outcome. No independent scientific review, formal verification or novelty clearance has occurred.
