# No fixed interpolation parameter handles all node tuples, even for one odd box

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:29:22 PDT 2026**. **WRITTEN countermechanism with WRITTEN-checked-in-kernel exact rational witnesses**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It rules out a simple universal construction, not common-SPR synthesis.

## 1. Statement

Fix one admissible independent odd box
\[
a_1\in[260,672],\quad a_3\in[292,293],\quad a_5\in[34,35],\quad a_7=1,
\]
whose odd bands are \([1,4],[7,13],[20,24]\). For arbitrary eligible five-node tuples in the mixed-band placement, the selector family of `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`, is
\[
F_\theta(t)=(-t)((1-\theta)t_3+\theta t_4-t)(13-t),\qquad0\le\theta\le1. \tag{1}
\]
**No fixed constant \(\theta\)** makes this test have positive even pairing on every required positive odd circuit for all eligible even boxes and all allowed node tuples, even though the odd box is fixed. A successful construction in this selector family must adapt \(\theta\) to the actual data.

## 2. Two explicit all-width stable boxes and circuits

Let \(G\) be the independent even box centered at \((363/8,407/4,45/2,1)\), with radius \(1/1000\) in each coordinate. Its six strict odd-band margins have minimum \(34871/1000\). In even endpoint coordinates \((\ell_0,\ell_1,\ell_2,\ell_3,u_0,u_1,u_2,u_3)\) define
\[
R_H=(0,104,25,1,80,126,25,1),\quad
R_L=(7280,9464,1900,91,7280,9881,2275,91). \tag{2}
\]
Their six nonnegative closed band-sign vectors are \((0,0,0,390,0,1840)\) and \((0,0,0,0,0,167440)\), respectively; their widths are nonnegative. Thus the boxes \(R_H+G/10\) and \(R_L+G\), paired with the fixed odd box, are strictly Hurwitz with all seven widths positive. Their minimum six-marker margins are \(34871/10000\) and \(34871/1000\), respectively.

For the high-\(\theta\) requirement, choose the five-node tuple
\[
(103/100,399/100,401/100,41/10,17/2). \tag{3}
\]
On \(R_H+G/10\), use the Y circuit with actual odd endpoints \((O_-,O_+,O_+,O_+)\), finite support \((t_1,t_2,t_4,t_5)\), and the correct mixed even corners: \(E_+\) for the first two nodes and \(E_-\) for the last two. Its positive uncompactified finite weights are
\[
\left(\frac{12500000000000}{5953613837576013},
\frac{12500000000000}{44112069298143},
\frac{250000000}{8789388817},
\frac{400000}{52730781543}\right),
\]
with infinity weight 1; the four odd moments cancel exactly. The **full** even pairing with (1) is affine in \(\theta\) and equals
\[
-\frac{2823334351369361455032793}{201840484041994259810700}\quad(\theta=0),\qquad
-\frac{2207650084429758465430111}{807361936167977039242800}\quad(\theta=1/2). \tag{4}
\]
It is therefore negative for all \(0\le\theta\le1/2\).

For the low-\(\theta\) requirement, choose instead
\[
(101/100,5/2,69/10,699/100,701/100). \tag{5}
\]
On \(R_L+G\), use the X circuit with the same odd-endpoint pattern and finite support \((t_1,t_2,t_3,t_5)\); its first three even components are \(E_+\) and its last is \(E_-\). The positive uncompactified weights are
\[
\left(\frac{500000000000}{60546401924283},\frac{80000}{858198429},
\frac{250000000}{24386184999},\frac{500000000000}{5335417073217}\right),
\]
again with infinity weight 1 and exact odd cancellation. Its full even pairing is
\[
-\frac{488830150595000875324871}{1785240442121019422000}\quad(\theta=1/2),\qquad
-\frac{309344239971732581442067}{446310110530254855500}\quad(\theta=1). \tag{6}
\]
It is negative for all \(1/2\le\theta\le1\).

The two fixed eligible boxes and node tuples therefore cover the whole parameter interval by explicit failures. Atoms are actual parity corners; compactified finite weights are \(w_i(1+t_i)^7\). Each is only a four-finite-plus-infinity odd-canceling circuit and is **not** an original no-go certificate. The failure is specifically of requiring this single fixed-\(\theta\) polynomial to certify every circuit and box.

## 3. Assurance and next representation

The coefficient-box margin signs, positive ray weights, eight zero odd moments across the two circuits, and the four negative pairings in (4) and (6) were evaluated by exact integers and `fractions.Fraction` on one Python Eval host. The strict stability, affine-in-\(\theta\) and endpoint arguments are written deductions. There was no independent scientific review, formal proof, parent adoption or novelty clearance.

The relevant remaining representation is a **data-dependent** selector, e.g. the 16-ray mixed-envelope LP in the named predecessor. This packet does not show that LP is infeasible on any tuple, exclude a box-dependent or different test numerator, or settle the original arbitrary-box SPR7 question. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
