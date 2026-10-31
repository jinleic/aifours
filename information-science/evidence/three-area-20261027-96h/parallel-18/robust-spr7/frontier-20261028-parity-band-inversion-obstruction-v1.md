# A geometric obstruction to septic negative atom certificates

**Status: WRITTEN theorem with one WRITTEN-checked-in-kernel finite example; author candidate, not parent adoption.** The result excludes broad classes of atom supports for *every* robustly Hurwitz-stable monic septic interval box. It does not exclude the inversion-bearing supports that remain, so it is not a universal answer to the original problem.

## Ordered parity bands

For an all-member-stable independent box, write \(a(i\omega)=E_a(t)+i\omega O_a(t)\), \(t=\omega^2\), and let \(E_-,E_+,O_-,O_+\) be its four actual parity endpoints. Each endpoint cubic has three simple positive roots. Let \(I_i\) be the closed interval spanned by the \(i\)-th roots of \(E_-\) and \(E_+\), and \(J_i\) the corresponding interval for the odd endpoints. Hermite–Biehler interlacing for **all four actual corner combinations** implies the six disjoint ordered bands
\[
0<I_1<J_1<I_2<J_2<I_3<J_3.
\]
Any member's \(i\)-th even root lies in \(I_i\), and its \(i\)-th odd root in \(J_i\). Outside these bands the parity signs follow \(+,-,+,-\).

Consider finitely many actual denominator/frequency atoms \((a_k,t_k)\), with \(t_k\ge0\), and let \(\sigma_i=(-1)^{i-1}\). An **even inversion** in \(I_i\) is a pair of atoms with \(t_k<t_\ell\) in that same band and
\[
\sigma_i E_{a_k}(t_k)<0<\sigma_i E_{a_\ell}(t_\ell).
\]
An **odd inversion** is defined identically with \(O\) and \(J_i\). Equal frequencies and zero parity values do not count as inversions.

## Obstruction and constructive separator

Let \(C_j\) be the eight coefficient sums of a finite nonzero nonnegative combination of the actual pairing functionals, optionally including the compactified infinity functional. Then:

1. If there is no even inversion in any \(I_i\), the four even sums \(C_0,C_2,C_4,C_6\) cannot all be strictly negative.
2. If there is no odd inversion in any \(J_i\), the four odd sums \(C_1,C_3,C_5,C_7\) cannot all be strictly negative.
3. If neither kind of inversion occurs, **no** such combination can have all eight sums nonpositive.

Consequently every *strict* negative-coordinate septic atom certificate must contain both an even inversion and an odd inversion. They occur in disjoint parity bands and therefore involve at least four distinct positive frequencies; the geometric ordering and opposite-endpoint requirement are the substantive restrictions, not an improvement on any stronger previously obtained numerical support bound. For actual corner atoms, each inversion necessarily uses both endpoints of the relevant parity, since one fixed endpoint polynomial crosses each of its simple roots in the correct order.

**Proof.** Suppose there is no even inversion. In each \(I_i\), let the lower bound for \(r_i\) be the maximum of the band’s left endpoint and all atom frequencies with \(\sigma_iE_{a_k}(t_k)>0\); let its upper bound be the minimum of the right endpoint and all frequencies with \(\sigma_iE_{a_k}(t_k)<0\). Missing sets impose only the band endpoint. The absence of an inversion makes the lower bound no larger than the upper; choose any positive \(r_i\) between them. Then
\[
F_r(t)=\prod_{i=1}^3(r_i-t),\qquad
b_E(s)=\prod_{i=1}^3(s^2+r_i)
\]
satisfy \(F_r(t_k)E_{a_k}(t_k)\ge0\) for every atom. Outside the even bands this follows from the fixed parity sign; inside each band it follows from the threshold choice. All four nonzero coefficients of \(b_E\) are positive, and its infinity coefficient is zero. Thus \(\sum_j b_{E,j}C_j\ge0\), which contradicts strict negativity of all four even sums. This proves item 1.

The same construction in \(J_i\) produces
\[
G_q(t)=\prod_{i=1}^3(q_i-t),\qquad
b_O(s)=s\prod_{i=1}^3(s^2+q_i),
\]
with \(t_kG_q(t_k)O_{a_k}(t_k)\ge0\). Its four odd coefficients, including the infinity coefficient, are strictly positive, proving item 2.

If neither inversion occurs, use \(b=b_E+b_O\), whose eight coefficients are positive. At every positive finite atom at least one of the two pairings is strictly positive: a zero even pairing can occur only in an even band, where the odd band is disjoint and the odd pairing is strictly positive, and conversely. At \(t=0\) the even pairing is strictly positive; at infinity \(b_7>0\). Hence the weighted sum of atom pairings is strictly positive, while \(C_j\le0\) would give \(\sum_jb_jC_j\le0\), a contradiction. This proves item 3. The argument uses actual atoms and their signs, not a coefficientwise hull of corners.

## Exact example

Take the independently checked five-contact box at scale \(\rho=1/2\). Its even roots lie in the three intervals \((0,1),(2,3),(6,8)\), and its odd roots in \((1,2),(3,6),(8,11)\). Consider all four actual corners at one rational point in each band, namely
\[
(t_E,t_O)=(1/2,5/2,7;\ 3/2,4,9),
\]
plus \(t=0\) and infinity. Choosing these six points as reference roots produces the positive coefficient vector
\[
(b_0,\ldots,b_7)=(35/4,54,89/4,111/2,10,29/2,1,1).
\]
All 28 finite actual-corner/grid pairings and the infinity pairing are strictly positive. The minimum of their compactified values is exactly \(7242833/7600000000\). This is a finite-grid dual certificate only; no positivity between these points is claimed.

Frozen exact endpoints, grid, vector and margin: `frontier-20261028-parity-band-dual-example-frozen-v1.json`, SHA-256 `71b05ba27638705787c6a7e5d77534f1f77b634ed42e3411a3ffaa1c7d255b17`. Standalone checker `frontier-20261028-parity-band-dual-independent-kernel-v1.py`, SHA-256 `afbf65fcca0e2cb53dbaefa4e25444dd2ea254edd55751e85b993d2607fc3fd0`, independently checks six strict sign markers, all 28 corner Hurwitz minors, reference roots, all 28 finite pairings and infinity, and rejects a negative-sign control. Receipt `frontier-20261028-parity-band-dual-independent-result-v1.json`, SHA-256 `d86fb6bd42ab5ca326bc0b2f9f447c6bb7d6d5f3765835ab7ed5cfab102025da`.

The general obstruction is a written proof using Hermite–Biehler interlacing, parity endpoint ordering and elementary polynomial signs; only the finite example was machine-checked, using exact rational arithmetic on one host. No formal verification, cross-vendor review, novelty clearance, or arbitrary-box verdict is claimed.
