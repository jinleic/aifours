# The common vertex can genuinely fail inside the second odd band

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:44:21 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational example**; not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a counterexample to one **fixed-vertex proof route**, not a common-numerator counterexample.

The additive correction `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`, identified an invalid upper-envelope lower-bound step when the final node lies in the second odd band. The exact example below shows that the very vertex \(F=(-t)(c-t)(d-t)\) can in fact have a strictly **negative** weighted even pairing on a real eligible box and one positive odd-canceling four-node-plus-infinity circuit. Another Vieta vertex has strictly positive pairing, so this circuit is not a no-go.

## 1. An explicit full-width Hurwitz box

Fix the odd intervals
\[
a_1\in[943/50,2387/125],\quad
 a_3\in[2693/100,689/25],\quad a_5\in[97/10,49/5],\quad a_7=1.
\]
Their pointwise extrema are
\[
O_- =-(t-1)(t-41/10)(t-23/5),\qquad
O_+ =-(t-11/10)(t-31/10)(t-28/5),
\]
with ordered odd bands
\([1,11/10]\), \([31/10,41/10]\), \([23/5,28/5]\).
Give the even coefficients \((a_0,a_2,a_4,a_6)\) the independent intervals with endpoint vectors
\[
\begin{aligned}
\ell&=(360899,989999,629999,99999)/100000,\\
u&=(459701,990001,630001,100001)/100000.
\end{aligned} \tag{1}
\]
Every interval width is strictly positive. Let \(E_-\) and \(E_+\) be the usual pointwise even extrema. At the six odd-band endpoints, the minimum strict signs \(-E_+(1),-E_+(11/10),E_-(31/10),E_-(41/10),-E_+(23/5),-E_+(28/5)\) are exactly
\[
37/12500,\quad 95359/100000000,\quad 367056499/100000000,\quad
9169/100000000,\quad 15530497/3125000,\quad 361110803/12500000. \tag{2}
\]
All are strictly positive. Thus the even roots of every member lie in the gaps \((0,1),(11/10,31/10),(41/10,23/5)\), the odd roots lie in the ordered bands, and classical Hermite–Biehler makes the entire box Hurwitz.

## 2. Actual corner atoms and odd cancellation

Use four positive squared frequencies and actual odd endpoint components
\[
(t_i)=(101/100,21/20,309/100,311/100),\qquad
(O_i)=(O_-,O_+,O_+,O_+). \tag{3}
\]
The final node is strictly inside the second odd band. Choose the even component \(E_+\) for the first three actual members and \(E_-\) for the fourth; all four are actual parity corners of the independent box. Their odd evaluations are
\[
(-110931/1000000,\ 3731/8000,\ -49949/1000000,\ 50049/1000000),
\]
and their even evaluations are
\[
(-563039599/100000000000,\ -7865519/800000000,\
465583241729/100000000000,\ 367356037669/100000000000). \tag{4}
\]

Take positive uncompactified finite weights
\[
\left(\frac{156250000000}{3058700463},\frac{5000000000}{411577803},
\frac{781250000000}{10232901783},\frac{2500000000000}{33667611957}\right)
\]
and compactified infinity weight 1. Direct exact arithmetic verifies
\[
\sum_{i=1}^4w_i t_iO_i(t_i)(-t_i)^k+\mathbf1_{k=3}=0
\quad(k=0,1,2,3). \tag{5}
\]
Equivalently, the finite weights are the positive four-node divided-difference circuit weights, and the compactified finite weights are \(w_i(1+t_i)^7\).

## 3. The proposed vertex really fails

For the previously used Vieta vertex
\[
F(t)=(-t)(31/10-t)(41/10-t),
\]
the finite weighted even pairing is exactly
\[
\sum_iw_iE_i(t_i)F(t_i)
=-\frac{31056186175174948483}{897271744042390080000}<0. \tag{6}
\]
The infinity atom has zero even contribution. In contrast, if one incorrectly replaces the fourth even value by the upper envelope as well, the resulting quantity is
\[
\frac{1292888161665181637}{580758410383424000}>0. \tag{7}
\]
This displays the direction error concretely: \(F(t_4)>0\) and the actual \(E_-(t_4)<E_+(t_4)\), so the upper-envelope value is **larger**, not a lower bound.

This is not a weak no-go certificate. For the different legitimate Vieta vertex
\(F_0(t)=(-t)(11/10-t)(41/10-t)\), the same actual atoms have strictly positive even pairing
\[
\sum_iw_iE_i(t_i)F_0(t_i)
=\frac{3583105569726881658403}{919726530806720000}>0. \tag{8}
\]
Hence the original interval-box synthesis question remains open. Four finite nodes plus infinity are also below the six-location weak-obstruction floor of `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`.

## 4. Assurance

All interval endpoints, six sign margins, four atom values, four odd cancellations, and pairings (6)–(8) were computed using exact integers and Python `fractions.Fraction` on one Eval host. The interlacing-to-stability inference is written mathematics. No independent replay, formal proof, cross-vendor review, parent adoption, publication or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
