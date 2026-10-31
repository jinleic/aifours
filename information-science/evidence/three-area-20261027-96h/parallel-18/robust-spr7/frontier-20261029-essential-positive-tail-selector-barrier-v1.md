# The positive tail is essential to a uniform direct-certificate selector

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:24:41 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational witnesses and dual identities**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This gives an exact proof-route barrier and a fixed-data direct exclusion, not an arbitrary-box SPR7 verdict.

## 1. Fixed admissible odd data

Use the independent odd intervals
\[
a_1\in[260,672],\quad a_3\in[292,293],\quad a_5\in[34,35],\quad a_7=1.
\]
Their odd extrema have roots \((1,13,20)\) and \((4,7,24)\), so the global bands are \([1,4],[7,13],[20,24]\). Fix five positive squared frequencies
\[
(t_1,t_2,t_3,t_4,t_5)=(103/100,397/100,403/100,697/100,353/50). \tag{1}
\]
The fifth node lies inside the second odd band. As in `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`, set
\[
\xi_\theta=(1-\theta)t_3+\theta t_4,\qquad
F_\theta(t)=(-t)(\xi_\theta-t)(13-t),\quad0\le\theta\le1. \tag{2}
\]
For each four-node ray \(X=(t_1,t_2,t_3,t_5)\) or \(Y=(t_1,t_2,t_4,t_5)\), call the sum of its first **three** finite \(F_\theta\)-pairings the *prefix*. The final finite pairing at \(t_5\) is positive for a stable box and an odd-positive selected member. Odd-ray weights are those of the normalized infinity circuit, \(w_i=[t_iO_i(t_i)\prod_{j\ne i}(t_i-t_j)]^{-1}>0\).

## 2. Two actual boxes defeat every prefix-only selector

Let \(G\) be the even box centered at \((363/8,407/4,45/2,1)\) with independent radius \(1/1000\). Its six strict odd-band stability margins have minimum \(34871/1000\); all four even widths are positive. Define two even endpoint vectors, in \((\ell_0,\ell_1,\ell_2,\ell_3,u_0,u_1,u_2,u_3)\) order,
\[
R_Y=(0,104,25,1,80,126,25,1),\quad
R_X=(7280,9464,1900,91,7280,9881,2275,91). \tag{3}
\]
Both lie in the closed stable-even-box cone. Therefore the boxes
\[
K_Y:\ R_Y+G/1000,\qquad K_X:\ R_X+G/10000 \tag{4}
\]
are strictly Hurwitz with the fixed odd box and have all seven coefficient widths positive; all lower coefficients are positive. Their smallest six-marker margins are respectively \(34871/1000000\) and \(34871/10000000\).

For \(K_Y\), use Y with actual odd parts \((O_-,O_+,O_+,O_+)\), and choose actual even corners that minimize the prefix pairing. At \(\theta=0\) and \(\theta=9/10\), the exact prefix sums are respectively
\[
-\frac{67010425534488691647033933383}{4177327519314252151348500000},\qquad
-\frac{29896807502245101283608805583}{41773275193142521513485000000}. \tag{5}
\]
The prefix is affine in \(\theta\), so it is negative on all \([0,9/10]\).

For \(K_X\), use X with the same odd-endpoint pattern and the actual minimizing even corners. At \(\theta=9/10\) and \(\theta=1\), the exact prefix sums are
\[
-\frac{1050598007911569521592473}{599753513430758521800000},\qquad
-\frac{10367984394070937073273971}{899630270146137782700000}. \tag{6}
\]
Hence this prefix is negative on all \([9/10,1]\). Each row is an actual positive four-node odd-canceling circuit with infinity weight 1, and both boxes are actual full-width eligible interval boxes. Therefore **no** \(\theta\in[0,1]\) can make every circuit prefix positive uniformly over all eligible even boxes for this fixed odd box and node set.

At \(\theta=9/10\), the omitted fourth finite contributions in the two examples are respectively
\[
675768483512/326654521875,\qquad 1002351817692292/384907911609375,
\]
large enough that both **full** circuit pairings are positive. Thus discarding the positive tail is not a valid universally sharp reduction, even though it can succeed in other regions.

## 3. The full direct selector nevertheless works here

The failure of the prefix-only route is not a negative SPR certificate. With \(\theta=1/3\), equivalently \(\xi=501/100\), the **full** mixed-envelope functional is strictly positive on all eight direct odd-moment extreme rays and both possible worst middle odd endpoints, for every all-Hurwitz even box with these fixed odd intervals. Six strict band-sign forms, four nonnegative width forms and four strict lower-coefficient forms supply the dual cone.

The 16 exact dual representations, finite weights and their odd-moment vectors \(-e_k\) are frozen in `frontier-20261029-essential-tail-sixteen-direct-duals-v1.json`, SHA-256 `30ebc3ffa2be4565917818b9c1841d8c1bb09121709c5e7ef29ee49fe049d767`. Each identity uses nonnegative multipliers and at least one strictly positive multiplier on a strict form. Hence every full ray pairing is strictly positive. Arbitrary actual odd/even member choices cannot do worse than the appropriate endpoints, and positive combinations of the eight odd-moment rays remain positive. Because \(F_{1/3}\) has nonnegative numerator coefficients, no strictly-negative all-eight-coordinate certificate on the five nodes exists for any such stable box.

## 4. Assurance and limits

The two prefix witness signs, odd-moment cancellations, all box margins, 16 dual identities and 16 direct-ray moment vectors were checked with exact `fractions.Fraction`/integer arithmetic on one Python Eval host. Cone decomposition, linearity in \(\theta\), mixed-envelope selection and interlacing are written deductions. The result does not prove a universal selector for all odd boxes/nodes, nor settle other five-frequency patterns or unrestricted SPR7 synthesis. No independent scientific review, formal proof, parent adoption or novelty clearance occurred. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
