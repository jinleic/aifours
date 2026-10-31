# Product-neighborhood k3 stability on every compact noise range

**CONDITIONAL AUTHOR-WRITTEN CANDIDATE.** This is a different quantifier/region from the pending uniform-high-noise candidate. It covers a rigorously specified product neighborhood at **every** noise parameter separated from the endpoints, but is not an all-state/all-p proof. It depends on the exact weight2/3/4 Hessian derivation in `frontier-20261028-59-uniform-high-noise-k3.md`, SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`, which remains unreviewed. No novelty, independent-family/human/formal acceptance or historical-process cure is claimed.

## Statement and explicit radius

Fix any \(0<\delta<1/2\), and set
\[
\begin{gathered}
g=2\delta,\quad s_1=1020/\delta,\quad
 q_0=510+1020s_1+32s_1^2,\quad s_2=2q_0/\delta,\\
 e_0=\min\left\{1,\frac1{4s_1},\frac1{4s_2},\frac g{8160},\frac g{8q_0}\right\},\\
 C_1=16(2s_1)^3\frac26+510(2s_1)^2+1020(2s_1)+1020,\\
 C_2=16(2s_2)^2e_0+1020(2s_2)+2q_0(2s_2)e_0+C_1,\\
 \varepsilon_\delta=\min\{e_0,\delta/(6C_2)\}>0.
\end{gathered}\tag{1}
\]
These are conservative explicit positive quantities, not optimized constants. For a pure four-qubit input let \(m\) be its maximal squared overlap with a pure product state. If
\[
 m\ge\frac1{1+\varepsilon_\delta^2},
\]
then for every physical p with \(t=|1-p|\in[\delta,1-\delta]\), and every actual complex rank-three projector P, the original k3 comparison holds. It is strict for every non-product such pure input. In the maximally overlapping product gauge, with \(\epsilon=\sqrt{(1-m)/m}\), the uniform actual spectral gap obeys
\[
 R_3(p)-K_3(\Lambda_p(\rho))\ge\frac{t\delta\epsilon^2}{32}.\tag{2}
\]
The non-strict conclusion extends, with the same P, to the closed convex hull of these pure inputs. It makes no assertion about a mixed density merely being close in some other metric. Endpoints \(t=0,1\) are not included in the strict statement; at \(t=0\) every output is uniform and at \(p=0\) a pure input has k3 equal to1.

## Hessian margin on the full compact range

The predecessor's direct computation shows that for any unit complex normal direction supported on weights2–4, the actual product-boundary top3 second-order coefficient satisfies \(A+K_2(M)\le-\min(\kappa_2,\kappa_3,\kappa_4)\), with
\[
\begin{aligned}
\kappa_2/t&=a(1-t^2)/8,\\
\kappa_3/t&=\frac{(1-t)(15+24t+38t^2+32t^3+3t^4)}{32(1-ab)},\\
\kappa_4/t&=1-\frac{t^6}{a^2+b^2},
\end{aligned}
\quad a=(1+t)/2,\ b=(1-t)/2.
\]
When \(t\in[\delta,1-\delta]\), respectively
\[
\kappa_2/t\ge\delta/16,\qquad
\kappa_3/t\ge15\delta/32,\qquad
\kappa_4/t\ge\delta/2.
\]
For example, \(1-t^2\ge\delta\), \(a\ge1/2\), and \(1-ab\le1\). Hence the rescaled top3 second-order coefficient is at most \(-16(\delta/16)=-\delta\), for every actual complex direction, including mixed Hamming weights.

## Uniform block argument

For \(t\in[\delta,1-\delta]\) the rescaled reference gaps satisfy
\[
 d_0-d_1=2(1+t)^3\ge2,\quad
 d_1-d_2=2(1+t)^2(1-t)\ge2\delta=g.
\]
The Pauli-string count gives \(\|D\|\le16\), \(\|V\|,\|W\|\le510\), and normalized cubic remainder \(\le1020|\epsilon|^3\). Frobenius divided-gap estimates give \(\|S_1\|\le s_1\), \(\|Q\|\le q_0\), \(\|S_2\|\le s_2\). The two unitary conjugations in the predecessor have, for \(|\epsilon|\le e_0\), matrix remainder at most \(C_2|\epsilon|^3\); the formulas in (1) bound every D, V, W and Q commutator term using \(e^{2|\epsilon|s_1}<2\) and \(e^{2\epsilon^2s_2}<2\). The chosen \(e_0\) also enforces \(\|H-D\|\le2040e_0\le g/4\) and the corresponding block-diagonal approximation perturbation \(510e_0+q_0e_0^2<g/4\), so the correct 1+4 leading blocks remain separated.

Weyl's rank-three trace estimate gives remainder at most \(3C_2|\epsilon|^3\). For \(\epsilon\le\varepsilon_\delta\), \(3C_2\epsilon\le\delta/2\), so the rescaled original top3 is at least \((\delta/2)\epsilon^2\) below its product value. Scaling back by \(t/16\) yields (2). The nearest-product variational gauge and the negative-shrink spin-flip projector map are exactly as in the predecessor. Convex combinations use one actual P for every summand.

## Actual finite checks and remaining scope

`frontier-20261028-68-product-tube-check.py`, SHA256 `822ba8c76557048bcd595345265252acb2e9651b225fa1a086167602cf2d4a67`, ran `python3 -B ...` from the repo root, exit0. For exact rational \(\delta=1/10,1/4\) it checks all inequalities implicit in (1); at \(t=1/10,1/2,9/10\) it verifies 45 exact complex-rational weight-Hessian cases meet \(\kappa_h\ge t\delta/16\). At \(\delta=1/10\) it records `e0=1/267174760800` and `epsilon_delta=1/10969298228683800`; these illustrate the conservatism, not a useful optimal radius. Native checker-pin clock **Wed Oct 28 18:41:52 PDT 2026**.

These finite checks do not prove the universal compact-range theorem, and this proper product tube does not cover arbitrary genuinely entangled states at those p. Full independent review of the predecessor's Hessians and the present all-parameter block budget remains required.
