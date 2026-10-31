# A mixed-band example where both endpoint selectors fail but an interior selector works

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:04:17 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational cone enumeration and witnesses**; not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is an exact barrier to two simple selector rules, not an original septic no-go.

## 1. Data and the exact interior interval

Fix an odd coefficient box whose extrema are
\[
O_-=-(t-1)(t-4)(t-5),\qquad
O_+=-(t-3/2)(t-2)(t-7),
\]
i.e. independent odd intervals \(a_1\in[20,21]\), \(a_3\in[55/2,29]\), \(a_5\in[10,21/2]\). The odd bands are \([1,3/2],[2,4],[5,7]\). Choose the five squared frequencies
\[
(t_1,t_2,t_3,t_4,t_5)=(201/200,299/200,31/20,399/200,11/5). \tag{1}
\]
Write \(\xi=(1-\theta)t_3+\theta t_4\), and test
\[
F_\theta(t)=(-t)(\xi-t)(4-t),\qquad 0\le\theta\le1. \tag{2}
\]
The roots are in the closed Vieta-gap product, and \(F_\theta\) is a convex combination of two actual Vieta vertices. For the two positive four-finite-plus-infinity odd circuits and the two middle odd endpoint choices of each, consider the correct mixed-even-envelope lower pairing functionals as in `frontier-20261029-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `8a8f5ee8430b4c313846cdd61149e99a7ec433dab36971df57d75bcb44e7f6ac`.

**Exact finite result.** All four functionals are strictly positive on every nonzero ray of the *closed* stable-even-box cone precisely when
\[
\frac{8801570077871}{24204052524794}<\theta<
\frac{20976207035859270}{21352321470099371}. \tag{3}
\]
In particular \(\theta=1/2\) is a uniform selector for **every** all-Hurwitz independent even coefficient box with the fixed odd intervals and every actual atom choice at the nodes. At the two endpoints \(\theta=0\) and \(\theta=1\), however, the corresponding uniform selector is false, as the two genuine stable boxes below show. The endpoints of (3) are claimed for *strict positivity on the entire closed cone*; no stronger assertion is made about whether the endpoints themselves work on only the strict-stability interior.

## 2. Exact cone evidence

For even-indexed interval endpoints \((\ell_0,\ldots,\ell_3,u_0,\ldots,u_3)\), take the 14 homogeneous closed inequalities: six band signs \(-E_+(1),-E_+(3/2),E_-(2),E_-(4),-E_+(5),-E_+(7)\ge0\), four widths \(u_k-\ell_k\ge0\), and four lower coefficients \(\ell_k\ge0\). This cone is full-dimensional and pointed. Every extreme ray has at least seven independent active inequalities.

Enumerating all \(\binom{14}{7}=3432\) active-row subsets, computing exact 7-by-7 determinant null vectors, retaining cone-feasible orientations, and reducing to primitive integers yields **32** distinct rays. Their complete coordinates and the exact inequality list are frozen in `frontier-20261029-selector-interior-cone-rays-frozen-v1.json`, SHA-256 `f655faab905fdc2505a024f724727c6bb9d369b2134e63ad1007f65a27cc39b0`. Intersecting the four cases' affine-in-\(\theta\) positivity conditions on those rays gives exactly (3). At \(\theta=1/2\), all 128 case/ray values are positive; the smallest value on the listed primitive rays is
\[
33004561845260000/9531570158068959>0. \tag{4}
\]
These finite counts and comparisons were computed using integer Bareiss determinants and exact `fractions.Fraction` arithmetic in one Python Eval host. The cone completeness inference is elementary polyhedral geometry, not an independently replayed enumeration.

## 3. Two actual full-width boxes defeating the endpoint rules

Let \(G\) be the even interval box centered at \((63/16,11,27/4,1)\), with independent radius \(1/1000\) in all four coordinates. Its six strict band-sign margins are
\[
2617/2000,\ 1187/1600,\ 369/400,\ 1541/400,\ 14313/2000,\ 6793/80.
\]
Define two nonnegative closed-cone endpoint vectors, in \((\ell_0,\ell_1,\ell_2,\ell_3,u_0,u_1,u_2,u_3)\) order,
\[
R_A=(12,28,15,2,15,28,15,2),\quad
R_B=(480,896,462,64,480,896,480,67). \tag{5}
\]
Their six closed band-sign vectors are respectively \((0,0,0,12,0,132)\) and \((0,0,0,0,0,4224)\), and their widths are nonnegative. Therefore the even boxes \(R_A+(1/100)G\) and \(R_B+(1/1000)G\), combined with the fixed odd intervals, are strictly Hurwitz and have all seven widths positive.

For the first box, use ray Y with finite nodes \((t_1,t_2,t_4,t_5)\), odd components \((O_-,O_+,O_+,O_+)\), infinity weight 1, and actual even endpoint components minimizing the pairing: \(E_+\) at the first two nodes and \(E_-\) at the last two. The physical finite weights are
\[
\left(\frac{3200000000000000}{111531831692589},
\frac{64000000000000}{229718024991},
\frac{64000000000000}{160494893559},
\frac{1250000000}{319163229}\right).
\]
All four odd moments cancel exactly with infinity, yet at \(\theta=0\), i.e. \(\xi=t_3\), the even pairing is
\[
-\frac{38939212298959896870839}{24305503903075845450000}<0. \tag{6}
\]

For the second box, use ray X with finite nodes \((t_1,t_2,t_3,t_5)\), the same odd-component pattern, infinity weight 1, and \(E_+\) at its first three nodes and \(E_-\) at the last. Its physical finite weights are
\[
\left(\frac{6400000000000000}{122797673277699},
\frac{6400000000000000}{2526898274901},
\frac{128000000000}{474016257},
\frac{125000000}{101198097}\right).
\]
Again the four odd moments cancel exactly, but at \(\theta=1\), i.e. \(\xi=t_4\), the even pairing is
\[
-\frac{6260275763237686545431}{1607110731961177170000}<0. \tag{7}
\]
All four atoms in either example are actual parity corners of their respective boxes. The compactified finite weights are obtained by multiplying by \((1+t_i)^7\). Equations (6)–(7), odd cancellations and sign/width bounds were checked with exact rational arithmetic in one Eval host.

Thus neither “always choose \(\xi=t_3\)” nor “always choose \(\xi=t_4\)” establishes a uniform two-circuit selector, even for these fixed odd intervals and nodes. The midpoint selector works here by (4). Neither four-node example is a no-go: positive pairing at the midpoint already rules that out.

## 4. Limits

The result is a fixed-data, fully specified admissible-box theorem and exact proof-route barrier. It neither proves the uniform-selector LP feasible for arbitrary odd boxes/nodes nor settles other minimal phase words, larger supports or unrestricted SPR7 synthesis. There was no formal proof, independent scientific review, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
