# Universal exclusion of direct phase C when its first node lies in the first gap

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:46:22 PDT 2026**. **WRITTEN theorem candidate with a WRITTEN-checked-in-kernel exact positive-polynomial certificate**, not parent-adopted, independently reviewed, formally verified or novelty-cleared.

## Theorem and remaining scope

For **every** compact independent coefficient box of monic Hurwitz septics, let \([a,b],[c,d],[e,f]\) be its ordered odd-root bands. There is no positive-weight aggregate of actual denominator/frequency atoms, even allowing zero and compactified-infinity atoms, whose eight monomial coordinates are all strictly negative and whose five positive squared frequencies satisfy
\[
b<t_1<c<t_2<t_3<d<t_4<t_5<e. \tag{1}
\]
The result is direct: it does not assume an odd-zero annihilator. It extends the near-first-root slab in `frontier-20261029-phase-c-universal-first-root-slab-v1.md`, SHA-256 `486648794818832120b606aad619ba2c4f68e08144c82d59d6c516ff7a7403ef`, to **every** admissible first even root. The full-width phase-C example in that packet shows nonvacuity.

The residual phase-C case where the first node lies in the first odd band \((a,b]\), the residual A/B cases, and the original arbitrary-box common-numerator-or-actual-counterexample problem remain **OPEN**. The argument does not exclude certificates with six or more positive nodes.

## 1. Odd rays, an even test, and endpoint reduction

Take
\[
F(t)=(-t)(b-t)(e-t), \tag{2}
\]
which is positive on all nodes in (1) and has nonnegative even numerator monomial coefficients \((0,be,b+e,1)\). Replacing each actual even evaluation by the lower even envelope \(E_-(t)\) can only lower its \(F\)-pairing. The odd signs of a hypothetical strict certificate must be \((- ,+,-,+,+)\); the odd-moment cone has exactly the eight four-node ray types in `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`.

For either support \((u_1,u_2,u_3,u_4)=(t_1,t_2,t_3,t_4)\) or \((t_1,t_2,t_3,t_5)\), the physical weights are
\[
w_i^{(k)}=\frac{e_{3-k}(\widehat u_i)}{u_i O_i(u_i)H'(u_i)}>0,\qquad
H(t)=\prod_{j=1}^4(t-u_j),\quad k=0,1,2,3. \tag{3}
\]
Normalize \(E_-\) by its positive leading even coefficient. By root-band interlacing its three even roots lie in \((0,a),(b,c),(d,e)\); their coefficient vector is a convex combination of the eight root vertices
\[
E_{x,y,z}(t)=(x-t)(y-t)(z-t),\quad
x\in\{0,a\},\ y\in\{b,c\},\ z\in\{d,e\}. \tag{4}
\]
At nodes 2 and 3 every vertex even value is positive. Elsewhere its sign is fixed by \(y,z\), independent of \(x\). To minimize a ray's even pairing over all actual odd values, use the following endpoints independently:
\[
\begin{array}{c|cccc}
(y,z)&O_1&O_2&O_3&O_4\\\hline
(b,e)&O_-&O_+&O_-&O_+\\
(b,d)&O_-&O_+&O_-&O_-\\
(c,e)&O_+&O_+&O_-&O_+\\
(c,d)&O_+&O_+&O_-&O_-.
\end{array} \tag{5}
\]
For the inside-band nodes, actual reciprocal odd magnitudes may be unbounded near zero; their coefficients are positive, so the displayed maximal-magnitude odd endpoints minimize the contribution. At the other nodes, the reciprocal magnitude ranges between endpoint values. Thus independent endpoint choices are a valid lower-bound relaxation.

## 2. Three vertices by interpolation

Write \(m=3-k\), and for \(g(u_i)=E_{x,y,z}(u_i)F(u_i)/(u_iO_i(u_i))\), let
\[
J_k(g)=\sum_i\frac{e_m(\widehat u_i)g(u_i)}{H'(u_i)}
=(-1)^{3-k}[t^k]I_g(t), \tag{6}
\]
where \(I_g\) is the cubic interpolant. Every \((b,e)\) vertex gives positive summands directly.

For \((b,d)\), use \(O_-\) formally at all nodes. The only replacement, \(O_-\to O_+\) at node 2, adds a positive contribution. The formal reduced function is
\[
g_-(t)=-\frac{(t-x)(t-b)^2}{t-a}. \tag{7}
\]
For \(x=a\), it is \(-(t-b)^2\), with \(J_k=(b^2,2b,1,0)\). For \(x=0\), it is
\[
-t^2+(2b-a)t-(b-a)^2-\frac{a(b-a)^2}{t-a}. \tag{8}
\]
The polynomial part has alternating-sign coefficients, and the interpolant of \(1/(t-a)\) has coefficient signs \((+,-,+,-)\) because \(0<a<u_i\): divide \(H(t)-H(a)\) by \(t-a\) after writing \(H(a+s)=\prod_i(s-(u_i-a))\). Hence (8) gives positive \(J_k\), including \(k=3\).

For \((c,e)\), use \(O_+\) as baseline; switching node 3 to \(O_-\) adds a positive term. The baseline is
\[
g_+(t)=\frac{(t-x)(e-t)^2}{f-t},\qquad x\in\{0,a\}. \tag{9}
\]
Its interpolant has coefficient signs \((- ,+,-,+)\). Specifically, let \(D=H(f)>0\), \(s_j=e_j(u_1,\ldots,u_4)\), \(A=(f-x)(f-e)^2>0\). Its leading coefficient is \(A/D>0\), its quadratic coefficient is \(-1+(A/D)(f-s_1)<0\), its linear coefficient is at least
\((e^2+2xe)/f-xe^2/f^2>0\), and its constant is \(-xe^2/f-A s_4/(fD)<0\). The bounds use the first and second Bonferroni inequalities for \(\prod_i(1-u_i/f)\). Thus all four \(J_k\) are positive.

## 3. The hard \((c,d)\) vertex: exact positive polynomials

For \((y,z)=(c,d)\), the endpoints are \((O_+,O_+,O_-,O_-)\). Normalize \(a=1\) by positive rescaling of the squared-frequency variable and introduce nine strictly positive gaps
\[
\begin{aligned}
b&=1+B,&u_1&=b+U,&c&=u_1+V,&u_2&=c+X,\\
u_3&=u_2+Y,&d&=u_3+Z,&u_4&=d+P,&e&=u_4+W,&f&=e+R.
\end{aligned} \tag{10}
\]
The normalization changes a ray pairing only by a positive factor. With \(O_+=(b-t)(c-t)(f-t)\) and \(O_-=(a-t)(d-t)(e-t)\), the reduced functions at nodes 1,2 and 3,4 respectively are
\[
\begin{array}{c|cc}
x&g_+(t)&g_-(t)\\\hline
0&\displaystyle\frac{t(d-t)(e-t)}{f-t}&\displaystyle-\frac{t(b-t)(c-t)}{t-a}\\[1ex]
a&\displaystyle\frac{(t-a)(d-t)(e-t)}{f-t}&-(b-t)(c-t).
\end{array} \tag{11}
\]
For each \(x\in\{0,a\}\) and \(m\in\{0,1,2,3\}\), multiply \(J_{3-m}(g)\) by the strictly positive Vandermonde \(\prod_{i<j}(u_j-u_i)\), and by
\[
D_0=(f-u_1)(f-u_2)(u_3-a)(u_4-a),\qquad
D_a=(f-u_1)(f-u_2), \tag{12}
\]
respectively. The result is an integer polynomial in the nine gaps in (10). **Every nonzero coefficient is positive** in each of the eight polynomials:

| First even root | \(m=0\) | \(m=1\) | \(m=2\) | \(m=3\) |
|---|---:|---:|---:|---:|
| \(x=0\) | 11,357 | 27,170 | 53,462 | 89,883 |
| \(x=a\) | 1,292 | 4,969 | 12,719 | 24,167 |

The entries are counts of nonzero monomials; the smallest coefficient in every polynomial is 1. The complete deterministic integer expansion and signed cross-multiplication recipe are `frontier-20261029-phase-c-gap-positive-polynomials-kernel-v1.py`, SHA-256 `e01dc6d405f45498146fd9c75753a11c4a62a696275194cceaf5c2267c4047eb`. Its result and lexicographically serialized coefficient hashes are `frontier-20261029-phase-c-gap-positive-polynomials-result-v1.json`, SHA-256 `5ccaf9f8c68f425f8682c13dfb73d06d3205fd29cdcbc6aa632f4968ac0ab88b`. In addition, two exact rational pointwise cross-multiplication identities were checked for each polynomial in the same host. Positivity of all eight polynomials proves the hard vertex for arbitrary strictly ordered bands and nodes; no sampled-grid inference is used.

## 4. Conclusion and assurance

All eight Vieta vertices have strictly positive \(F\)-pairing on every odd ray, for arbitrary actual denominator choices. Convex interpolation proves it for the actual \(E_-\); positive ray combinations preserve strict positivity. A zero atom contributes zero to (2), and infinity contributes zero to the even test while only increasing the fourth odd coordinate. Hence these atoms cannot repair an all-negative aggregate, proving (1).

The eight integer expansions, their 225,019 positive coefficients and the 16 pointwise Fraction identities were computed in one Python Eval host using only exact integer and rational arithmetic. The gap substitution, cross-multiplication equivalence, endpoint domination, ray reduction and interlacing are written arguments; the machine calculation is not a Lean/kernel proof, independent replay, cross-vendor review or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
