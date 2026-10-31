# An explicit open family excluding five-frequency strict certificates

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** Let \(K\) be the box in `frontier-20261028-five-node-ratio-gap-obstruction-v1.md`: each nonleading coefficient of \((s+1)^7\) varies independently by \(9/10\). Perturb each of its 14 interval endpoints independently by at most \(10^{-6}\), retaining monicity. Every resulting box is strictly Hurwitz and satisfies all three ratio-gap tests of that packet. Consequently, **conditional on that packet's named unreviewed phase-word and root-order imports**, any strict negative-coordinate atom certificate for any box in this full 14-dimensional open neighborhood needs at least six distinct positive finite frequencies. No claim is made about certificates with six or more frequencies or about the original arbitrary-box decision.

## Stability under the perturbation

At the five rational markers
\[
\frac3{25},\quad\frac3{10},\quad\frac45,\quad\frac95,\quad\frac{53}{10},
\]
the signs of \((E_a,O_a)\) for every anchor corner are respectively
\[
(-,+),\quad(-,-),\quad(+,-),\quad(+,+),\quad(-,+).
\]
The independent checker proves that each of the **40** strict corner parity signs has margin greater than the worst possible perturbation. At \(t>0\), a single endpoint perturbation \(\varepsilon=10^{-6}\) changes the corresponding parity values by at most
\[
|\Delta E(t)|\le\varepsilon(1+t+t^2+t^3),\qquad
|\Delta O(t)|\le\varepsilon(1+t+t^2).
\]
The perturbed endpoints remain positive and ordered. At \(t=0\), both parities are positive; at infinity their leading signs are negative. The same strict signs hold for every actual member, giving the six alternating root bands and strict Hurwitz stability by Hermite–Biehler. In particular both endpoint parity groups remain nondegenerate.

## Uniform rational ratio guards

Use the four rational points
\[
(p_1,p_2,p_3,p_4)=\left(\tfrac9{50},\tfrac{39}{50},\tfrac{69}{50},\tfrac{132}{25}\right).
\]
For the perturbed root bands, the checker also proves the strict root-side signs
\[
O_-(p_1)>0,\qquad E_-(p_2)>0,\qquad
O_+(p_3)<0,\qquad E_+(p_4)<0.
\]
Together with the marker order these place \(p_1\) before \(o_1^-\), \(p_2\) after \(e_2^-\), \(p_3\) before \(o_2^+\), and \(p_4\) after \(e_3^+\), all within the appropriate adjacent root-free branches. Since each \(R_{\pm\pm}(t)=-tO_\pm(t)/E_\pm(t)\) is decreasing there, their evaluations conservatively bound the four root-ratio values \(U_1,L_2,U_2,L_3\) from the preceding theorem.

At each point, put \(n_0=t|O|\), \(d_0=|E|\), \(\Delta n=\varepsilon t(1+t+t^2)\), and \(\Delta d=\varepsilon(1+t+t^2+t^3)\). The exact checker verifies \(n_0>\Delta n\), \(d_0>\Delta d\), and confines each perturbed positive ratio to
\[
\left[\frac{n_0-\Delta n}{d_0+\Delta d},\ 
\frac{n_0+\Delta n}{d_0-\Delta d}\right].
\]
It checks three strict interval comparisons: the upper bound for \(U_1\) lies below the lower bounds for both \(L_2\) and \(L_3\), and the upper bound for \(U_2\) lies below the lower bound for \(L_3\). Thus all three ratio-gap hypotheses hold for every perturbed box, without sampling the endpoint cube. The prior theorem then excludes all three five-node phase words.

Frozen markers, root guards and exact ratio intervals: `frontier-20261028-five-node-ratio-gap-open-frozen-v1.json`, SHA-256 `f515cf1361578578d0c6a7f97821790b9a6226e3d06c593886a5a1cbb4815d4c`. Independent interval checker `frontier-20261028-five-node-ratio-gap-open-independent-kernel-v1.py`, SHA-256 `cc0f514538c3b889c5d1ddda847fadb4a33d6a2382107de27234405b72ea4d92`; receipt `frontier-20261028-five-node-ratio-gap-open-independent-result-v1.json`, SHA-256 `ae336aa02cac3dff6e2dc58fa54d250040bbfb8d7d8793f94530e678e6e2a925`. The preceding conditional ratio theorem is SHA-256 `5848805f679c049bda608e408b8a99d07481fa6378698d2b886f8e4e94810696`.

All finite interval inequalities use exact integers and `fractions.Fraction` on one Python Eval host. Root-band, monotonicity and certificate deductions are written mathematics; no formal proof, cross-vendor review, novelty clearance, unrestricted no-go theorem, or six-or-more-frequency conclusion is claimed.
