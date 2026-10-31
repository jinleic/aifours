# Extreme five-contact shape: a failed universal high-gain route

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** There is an exact, strictly stable septic interval box for which the previously successful \(b_0=b_7=1,\ b_6=1000\) five-tangency numerator fails. The associated high-gain direction also fails. This **does not** disprove a common numerator: another explicit numerator works for the whole radial family. It is a genuine obstruction to extending that particular fixed-gain/high-gain construction indiscriminately to arbitrary contact-node ratios.

## Exact boundary and actual box

Use the five-contact pattern in `frontier-20261028-five-contact-all-admissible-nodes-v1.md` with
\[
(t_1,t_2,t_3,t_4,t_5)=(1,8,118,138,4138),\quad
u=\tfrac12,\quad \lambda=\tfrac73,\quad v=4550.
\]
Its seven independent boundary intervals, listed in coefficient order \(a_0,\ldots,a_6\), have lower and upper vectors
\[
\begin{aligned}
\ell&=(18998,571044,37250,574244,1197/2,4277,1),\\
h&=(33104,4295200,114884/3,575320,4147,4676,7/3).
\end{aligned}
\]
All widths are strictly positive. Form the midpoint-centered radial box at \(\rho=9999/10000\). The independent replay checked all 28 Hurwitz determinants of its four actual parity corners and all 24 finite alternating marker signs; the sign-band and connected homotopy argument proves every member stable. The frozen record gives all seven exact rational lower and upper endpoints. The same marker argument works for every \(0\le\rho<1\).

## High-gain and fixed-normalization failures

At the five boundary contacts, impose the five tangent equations and set \(b_0=b_7=0, b_6=1\). Their exact solution has \(b_1,\ldots,b_6>0\), but for the boundary corner \((E_+,O_-)\),
\[
\left.\partial_tP_{a,b}(t)\right|_{t=0}
=-\frac{3062883757668034040}{498696348079}<0,\qquad
P_{a,b}(1/100)
=-\frac{373500533380743287712035271}{6233704350987500000000}<0.
\]
Thus the high-gain direction fails the nonnegative-boundary-pairing premise. Both values and all five tangent equations were independently recomputed by direct exact polynomial convolution. The high-gain direction has degree six and is used only to test that limiting construction.

With the different normalization \(b_0=b_7=1,b_6=1000\), solve the five tangent equations exactly. All eight resulting coefficients are positive, yet its pairing with the **actual** radial corner \((E_+,O_-)\) at \(t=1/100\) is
\[
-\frac{697648853356670876556729994326112161996369}
 {224025011815373921120000000000000000}<0.
\]
Hence that explicit degree-seven numerator is not common SPR for this eligible box. This does **not** show that every possible numerator with gain 1000 fails, because here \(b_0=b_7\) was also fixed; nor does it produce a negative atom certificate against all numerators.

## An explicit successful alternative

Set \(b_0=1,b_6=5/12,b_7=1/2750\), and solve the same five tangent equations. The unique exact solution is
\[
\begin{aligned}
b_1&=\frac{312731194027152537645593531}{277230952121525227386000},&
b_2&=\frac{681917431031172569727534}{35003908096152175175},\\
b_3&=\frac{23251889317084396645680781}{110892380848610090954400},&
b_4&=\frac{619589754602786857360141}{420046897153826102100},\\
b_5&=\frac{897489112977942114555691}{554461904243050454772000}.
\end{aligned}
\]
After dividing the actual boundary corner pairings by their contact-square factors, the independent checker verified every compactified Bernstein coefficient strictly positive, using respectively 84, 78, 20 and 96 coefficients. It separately proved
\[
\frac{P_{a_{\rm mid},b}(t)}{(1+t)^7}\ge
\frac{367477561233460009808564294113809871167584723}
{37536985473798597287451072876072430511516024832000}>0
\quad(t\ge0)
\]
with 104 strict midpoint-leaf coefficients. Affine interpolation between the midpoint and the four boundary corners therefore proves this one \(b\) strictly common SPR on **every** radial box \(0\le\rho<1\). Since \(1+\sum h_j=4950745\), the explicit unnormalized lower bound on \(\operatorname{Re}(b/a)\) is \((1-\rho)\) times the displayed midpoint margin divided by \(4950745^2\). The exact degree-seven numerator can be normalized by its positive leading coefficient.

## Evidence and limits

A deterministic exact conditioned search tested 95 admissible extreme shapes; 94 passed the high-gain residual criterion and the 95th produced the initial failure. The simpler rational shape above is independently checked; this finite search establishes no population or universal-frequency conclusion. Frozen inputs, both numerators, radial endpoints and frequency leaves: `frontier-20261028-extreme-contact-tangent-failure-frozen-v1.json`, SHA-256 `57cc93967bbb6662300012922db5d0dfa2d3013a3ff66e11dea41facf13df130`. Independent checker `frontier-20261028-extreme-contact-independent-kernel-v1.py`, SHA-256 `61311fc199bc8ada36f1627c76e15e01f71aaf1634568a6436a96edae1a2ff03`; receipt `frontier-20261028-extreme-contact-independent-result-v1.json`, SHA-256 `61295812e7d2e7aa039c9c0cdff7c1d9546af749747949182a9769e5c9a9aa31`. The receipt discloses the corrected ordering of breadth-first leaves and the resumed failed block.

All finite claims use exact integers and `fractions.Fraction` in one Python Eval host. The stability homotopy and continuum interpolation are written mathematics; no formal verification, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
