# One eligible septic box defeats an entire Vieta face

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:56:52 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational box and atom certificate**; not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a complete counterexample to a proposed selector face, **not** an unrestricted no-common-numerator certificate.

## 1. Result

There is an explicit all-seven-positive-width all-Hurwitz independent septic coefficient box, and one positive combination of five actual atoms plus infinity with **all four odd coordinates exactly zero**, for which the weighted even pairing is strictly negative on the **entire Vieta face with middle root \(c\)**. This defeats every root choice \((x_1,c,x_3)\) in that face, including every selector
\[
F_\theta(t)=(-t)(c-t)(((1-\theta)t_4+\theta t_5)-t),\quad0\le\theta\le1. \tag{1}
\]
The example realizes direct phase C \((2,4,3,5,4)\), with its first node outside the first odd band. Consequently neither a universal nor even a box-dependent construction restricted to (1) can give positive pairing on every odd-canceling ray combination in pattern C. In particular the dropped-first selector LP of `frontier-20261029-pattern-c-dropped-first-selector-lp-v1.md`, SHA-256 `a533a26ac4e74f546824e2e04033f8d74c3045a4e36d1fd9cce8affbba3d3c06`, is infeasible for these fixed odd/node data.

This is **not** a weak no-go: the same atom combination has strictly positive pairing on the entire opposite Vieta face with middle root \(b\). It does not rule out an unrestricted common numerator.

## 2. Exact stable interval box

Fix odd intervals
\[
a_1\in[106281/400,2139501/8000],\qquad
 a_3\in[116203/400,119921/400],\qquad
 a_5\in[351/10,703/20],\qquad a_7=1.
\]
Their odd extrema are
\[
O_-=-(t-1)(t-241/20)(t-441/20),\qquad
O_+=-(t-21/20)(t-221/20)(t-461/20),
\]
so the odd-root bands are
\[
[a,b]=[1,21/20],\quad[c,d]=[221/20,241/20],\quad[e,f]=[441/20,461/20].
\]
Give the even coefficients \((a_0,a_2,a_4,a_6)\) independent interval endpoints
\[
\ell=(47/5000,280483/10000,29011/1250,9953/10000),\quad
u=(47/2500,668897/5000,116091/5000,10047/10000). \tag{2}
\]
All seven widths and all lower coefficients are positive. The six exact box-stability margins at \(a,b,c,d,e,f\) are
\[
29033/5000,\ 398882693/80000000,\ 2041093/80000000,\
2379473/80000000,\ 6148673/80000000,\ 39965662253/80000000, \tag{3}
\]
with signs \(-E_+,-E_+,E_-,E_-,-E_+,-E_+\). They are strictly positive. The resulting even roots are in \((0,a),(b,c),(d,e)\) and the odd roots in the three separated bands, so every member is Hurwitz by Hermite–Biehler.

## 3. One actual five-node zero-odd measure

Use squared frequencies
\[
(t_1,t_2,t_3,t_4,t_5)=(241/40,11051/1000,553/50,603/50,341/20) \tag{4}
\]
and actual odd components \((O_-,O_+,O_-,O_-,O_-)\). Their odd evaluations are
\[
(-31050681/64000,\ 120001999/1000000000,\ -54726903/500000,\
552447/500000,\ 1605/4).
\]
At node 1 choose the actual even component
\[
E_1=(1-\lambda)E_-+\lambda E_+,\qquad
\lambda=13031519863/45471032126\in(0,1),
\]
which has \(E_1(t_1)=-1/1000\). At nodes 2–4 choose \(E_-\), and at node 5 choose \(E_+\). Independent coefficients make all five pairs actual members of the box. Their even evaluations are
\[
-1/1000,\quad366094992403/10000000000000,\quad169452881/1250000000,\quad
-115738069/1250000000,\quad107056151227/80000000. \tag{5}
\]
Thus their parity signs are \((--),(++),(+-),(-+),(++)\), the literal phase word \((2,4,3,5,4)\), including both reversed bands.

Use the positive uncompactified finite weights
\[
\left(\frac{23815168000000000}{10079894596505100723657},
\frac{1016650000000000000000000}{60516503978774272102401},
\frac{145000000000000}{7823579697903123},
\frac{5000000000000}{405701270738883},
\frac{6400000}{173461734685701}\right), \tag{6}
\]
with compactified infinity weight \(11/10\). Exact arithmetic verifies
\[
\sum_{i=1}^5w_it_iO_i(t_i)(-t_i)^r+\frac{11}{10}\mathbf1_{r=3}=0,
\qquad r=0,1,2,3. \tag{7}
\]
These weights are the sum of the four-finite-plus-infinity odd circuit on support \((1,2,3,4)\) and \(1/10\) times the circuit on \((1,2,3,5)\). The compactified finite atom weights are \(w_i(1+t_i)^7\).

## 4. Exact face separation

For \(x_1\in\{0,a\}\), \(x_2\in\{b,c\}\), \(x_3\in\{d,e\}\), compute
\[
G(x_1,x_2,x_3)=\sum_iw_iE_i(t_i)(x_1-t_i)(x_2-t_i)(x_3-t_i).
\]
Across the four vertices on the face \(x_2=c\), the **largest** value is
\[
-\frac{1962728339854339365738737911207083249574665346987}{113978994511448510999986879447818600896227048735800}
<-1/1000. \tag{8}
\]
Across the four vertices on the opposite face \(x_2=b\), the **smallest** value is
\[
\frac{235338534245513594293402914854361443939273868431}{3798919925055778122187343913869233106563578600}>1. \tag{9}
\]
Since \(G\) is affine in each of \(x_1,x_3\), these inequalities hold throughout the two closed faces. The entire \(x_2=c\) face is negative, so every member of (1) is negative; the opposite face is positive, so (7) is not a no-go. For example the pairings at \(\xi=t_4\) and \(\xi=t_5\) in (1) are both strictly negative, and all intermediate \(\xi\) follow by linearity.

## 5. Assurance and the actual remaining step

The intervals, six stability margins, interpolation coefficient, five atom values, positive weights, four zero odd moments and all eight vertex signs were calculated using exact integers and Python `fractions.Fraction` in one Eval host. Interlacing, phase labeling and Vieta face interpolation are written deductions. There was no independent scientific review, formal proof, parent adoption or novelty clearance.

The exact remaining representation must allow a Vieta root \(x_2\) to move **off** the face \(x_2=c\), or use a different full numerator/dual. This example establishes neither a strict-negative eight-coordinate certificate nor an unrestricted positive construction. Other phase patterns, larger supports and the original arbitrary-box SPR7 verdict remain **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
