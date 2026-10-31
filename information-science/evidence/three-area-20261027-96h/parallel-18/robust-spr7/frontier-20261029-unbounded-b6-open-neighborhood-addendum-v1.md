# The unbounded coefficient obstruction holds on open sets of boxes

**Status: WRITTEN addendum to the exact symbolic candidate, not parent adoption.** For each fixed \(R\ge100\), the full-width box \(K_R\), atom rows \(r_i\), strictly positive cofactors \(w_i\), aggregate \(C\), and explicit common numerator \(b_R\) are those of `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`). The forced bound \(b_6>(R^2/20)b_7\) and existence of a common numerator both persist on a nonempty **14-dimensional open neighborhood** of \(K_R\). These neighborhoods can be chosen with every denominator's \(a_6<2\). Consequently, over open sets of solvable boxes, every common monic numerator can be forced to satisfy
\[
\frac{b_6}{\sup a_6}>\frac{R^2}{40},
\]
which is unbounded as \(R\to\infty\).

## A computable conservative radius

Fix \(R\), put \(H=R^2/20\), and let \(t_i\) be its five fixed atom nodes. Define
\[
T=\max(1,t_1,\ldots,t_5),\quad A=2+\max_{0\le j\le6}u_j,\quad
B=8A(1+T)^7,\quad L=8(1+T)^7.
\]
If every endpoint changes by at most \(\epsilon\le1\), each corresponding monomial pairing-row entry has magnitude below \(B\) and changes by at most \(L\epsilon\). For the cofactor weights define
\[
W=4!\,4\,B^3L,\quad w_{\min}=\min_iw_i,\quad w_{\max}=\max_iw_i,\quad
Q=5(WB+w_{\max}L).
\]
Leibniz telescoping gives \(|\Delta w_i|\le W\epsilon\); consequently every aggregate coordinate changes by at most \(Q\epsilon\). At the anchor, all of
\[
w_{\min},\quad -C_0,\quad -C_4,\quad C_6,\quad -(C_7+HC_6)
\]
are strictly positive by the pinned all-parameter replay.

Let \(S=\sum_j|(b_R)_j|\), and let \(\delta_R>0\) be the minimum, on compactified frequency \(x\in[0,1]\) and the four actual corners, of the normalized pairing of \(b_R\). This exists by the predecessor's strict all-frequency proof. One valid positive radius is any \(\eta_R\) strictly smaller than half the minimum of
\[
\begin{gathered}
1,\quad \min_j\ell_j,\quad \frac12\min_j(u_j-\ell_j),\quad 2-u_6,\quad
\frac{w_{\min}}{2W},\\
\frac{-C_0}{2Q},\quad\frac{-C_4}{2Q},\quad\frac{C_6}{2Q},\quad
\frac{-(C_7+HC_6)}{2(1+H)Q},\quad\frac{\delta_R}{28S}.
\end{gathered}
\]
All terms are explicitly defined and strictly positive. For rational \(R\), all quantities except the displayed minimum \(\delta_R\) are rational; a rational positive lower bound for \(\delta_R\) is computable by exact compactified Bernstein subdivision, so a rational radius can be produced without a numerical optimizer.

For each perturbed box, recompute the **same four-by-five matrix** from its actual corners and use its signed cofactor vector. It annihilates coordinates \(1,2,3,5\) identically; the strict bounds above keep every weight positive, \(C_0,C_4<0\), \(C_6>0\), and \(C_7+HC_6<0\). The original five-atom argument therefore proves \(b_6>Hb_7\) for every common numerator. Endpoint clipping changes any compactified pairing with the fixed \(b_R\) by at most \(14\eta_RS<\delta_R\), so \(b_R\) remains common. The same positive pairing along each coefficient segment excludes imaginary-axis crossings and transfers Hurwitz stability from the original box. Widths, positive lower coefficients and \(a_6<2\) persist by the other radius terms.

These are written finite-dimensional continuity and determinant estimates, with the anchor signs and numerator furnished by the separately checked symbolic packet. No uniform radius over \(R\), unrestricted negative answer, formal proof, cross-vendor review or novelty clearance is asserted.
