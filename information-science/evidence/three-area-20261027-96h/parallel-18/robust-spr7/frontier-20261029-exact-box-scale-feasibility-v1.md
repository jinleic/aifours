# Exact finite linear feasibility for stable boxes with prescribed parity shapes

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:18:37 PDT 2026**. **WRITTEN all-shape theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It gives an exact **stability admission** test for a parametrized class of coefficient boxes; it is not an SPR synthesis theorem or negative certificate.

## 1. Finite data and result

Choose finitely many even cubic shapes
\[
P_i(t)=\sum_{k=0}^3(-t)^k p_{ik},\quad p_{ik}>0,\quad i=1,\ldots,N,
\]
each with three distinct positive roots, and finitely many monic odd cubic shapes
\[
Q_h(t)=\sum_{k=0}^3(-t)^k q_{hk},\quad q_{h0},q_{h1},q_{h2}>0,\quad q_{h3}=1,\quad h=1,\ldots,M.
\]
Choose unknown \(\lambda_i>0\). Form the smallest independent monic septic coefficient box \(K(\lambda)\) containing **all** parity combinations \(\lambda_iP_i\) and \(Q_h\): the four even coefficient intervals are the coordinatewise hull of \(\lambda_i p_i\), while the three nonleading odd intervals are the coordinatewise hull of \(q_h\). The leading \(s^7\) coefficient is one.

Let \(O_-(t)\le O_+(t)\) be the pointwise odd extrema on \(t\ge0\), obtained by independently selecting each odd coefficient endpoint with the alternating monomial signs. Let \(e_1<e_2<e_3\) be the roots of \(P_1\).

**Theorem.** Positive scales making **every** member of \(K(\lambda)\) Hurwitz exist if and only if the following finite tests both hold:

1. The odd-only pretest is strict:
\[
O_-(e_1)>0,\qquad O_+(e_2)<0,\qquad O_-(e_3)>0. \tag{1}
\]
2. Compute the six actual endpoints \(o_j^-\le o_j^+\) of the odd-root bands as in §2. For each \(j\in\{1,2,3\}\) and each \(T\in\{o_j^-,o_j^+\}\), put \(s_j=(-1)^j\). There exist \(\lambda_i,\delta,z_{j,T,k}\) satisfying the **linear** system
\[
\sum_{i=1}^N\lambda_i=1,\quad \lambda_i\ge\delta,\quad\delta>0,\quad
z_{j,T,k}\le s_j(-T)^k\lambda_i p_{ik}\ \ (i=1,\ldots,N),\quad
\sum_{k=0}^3z_{j,T,k}\ge\delta. \tag{2}
\]

Thus, after normalization, admissible scale vectors form a relatively open convex polyhedron, and (2) gives a complete finite linear-feasibility representation. If all input coefficients are rational, the odd root endpoints are real algebraic and all LP coefficients are exact real algebraic numbers; exact algebraic linear programming or real-closed-field elimination decides the fixed shape instance. If the relevant roots happen to be rational, (2) is a rational LP. No solver was run or complexity bound claimed here.

If the test succeeds, the resulting compact stable box can additionally be enlarged slightly in all seven nonleading coordinates, preserving strict stability and producing seven positive widths. The enlargement is an existence assertion by compactness; no uniform numerical radius is claimed.

## 2. The odd-only pretest and exact bands

If any \(K(\lambda)\) is stable, it contains \(\lambda_1P_1\) paired with every odd component in the odd coefficient hull. Hermite–Biehler then gives (1). Conversely (1), the positive odd constant term and the monic cubic leading term show every odd component has exactly one simple positive root in each of the three disjoint intervals
\[
(e_1,e_2),\quad(e_2,e_3),\quad(e_3,\infty),
\]
so all its roots are simple and positive. In particular \(O_-\) and \(O_+\) have such roots. The actual odd coefficient hull is compact and connected, and its ordered roots vary continuously, so each \(j\)-th root occupies a complete closed interval. Pointwise \(O_-\le O\le O_+\) and alternating crossings give its endpoints:
\[
\begin{array}{c|cc}
j&o_j^-&o_j^+\\\hline
1&\operatorname{root}_1(O_-)&\operatorname{root}_1(O_+)\\
2&\operatorname{root}_2(O_+)&\operatorname{root}_2(O_-)\\
3&\operatorname{root}_3(O_-)&\operatorname{root}_3(O_+).
\end{array} \tag{3}
\]
Each band is strictly separated from its neighbors because it lies strictly between the fixed reference roots; degenerate bands are allowed. The root extrema are attained by actual endpoint components, even when some coefficients have zero width.

## 3. Why six sign constraints are necessary and sufficient

At a fixed squared frequency \(T\), independent choices of the even coefficients give exactly
\[
\min_{E\in K_E}s_j E(T)
=\sum_{k=0}^3\min_i\{s_j(-T)^k\lambda_i p_{ik}\}. \tag{4}
\]
At every actual \(j\)-th odd root, stability requires \(s_jE(T)>0\) for every even component; this gives the six strict inequalities corresponding to the band endpoints in (2).

Conversely, if the six endpoint inequalities hold, every even component has positive constant term, negative leading term, and signs \(-,+,-\) at the first, second and third odd bands' endpoints. By the intermediate-value theorem, its cubic has one root in each gap
\[
(0,o_1^-),\qquad(o_1^+,o_2^-),\qquad(o_2^+,o_3^-).
\]
There are already three distinct roots, so no extra root occurs in any odd band, and these roots are simple. Therefore **every** even component interlaces **every** odd component of the box; Hermite–Biehler makes every monic septic in the box Hurwitz.

System (2) is exactly the finite strict system in (4): each \(z\) is an independent lower bound on the corresponding minimum, and choosing \(z\) equal to that minimum is possible. Scaling all even parts by one positive scalar does not change the root order, so \(\sum_i\lambda_i=1\) is without loss. The finitely many strictly positive \(\lambda_i\) and six strict margins admit one common \(\delta>0\). Conversely (2) forces all of them strictly positive. This proves the equivalence and convexity.

For the enlargement, strict Hurwitz stability is open in coefficient space and \(K(\lambda)\) is compact. Its distance to the closed complement is positive, so a sufficiently small common enlargement preserves stability and positivity of the seven lower coefficients.

## 4. Connection to the original gap

The general two-shape single-frequency obstruction `frontier-20261029-general-shared-root-width-criterion-v1.md`, SHA-256 `81b72083d1939d3423b1d2c59ee514eca9d0800a665c95beba9cb729bd3017dd`, is one subcase of (4); the present test retains *all* odd-band endpoints and permits arbitrarily many even shapes simultaneously. The exact seven-positive-width example in `frontier-20261029-shared-odd-root-sharp-width-v1.md`, SHA-256 `3cc332f1bd711be0a4d153ebdf42bbea44930e082795823b9366a74fe14c87d4`, shows this admission class is nonempty. Both are author-written imports, not parent-adopted proof.

To pursue the original synthesis-or-obstruction task, combine the feasible scale polyhedron (2) with the actual-box odd-cancellation/eight-Vieta-corner inequalities from `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`. That coupled system still contains scale-times-atom-weight products and is **not** resolved by this LP. A stable box generated by this test need not have been shown to have, or lack, a common numerator.

Named imports: odd-degree Hermite–Biehler interlacing, continuity of simple roots, compactness and elementary finite-dimensional linear programming. No scientific computation was run for this general theorem. No original verdict, independent scientific review, formal proof, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
