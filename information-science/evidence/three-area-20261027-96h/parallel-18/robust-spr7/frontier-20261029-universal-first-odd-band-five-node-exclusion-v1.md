# Universal exclusion of one five-node weak-certificate band pattern

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:34:25 PDT 2026**. **WRITTEN universal theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a rigorous proposed exclusion for a genuinely unrestricted class of eligible boxes and node positions, not a claim that all five-node certificates or unrestricted SPR7 synthesis are settled.

## 1. The result

Let \(K\) be any compact independent monic septic coefficient box, all of whose members are strictly Hurwitz. Its global odd-root bands are
\[
[a,b],\qquad[c,d],\qquad[e,f],\qquad 0<a<b<c\le d<e\le f, \tag{1}
\]
with pointwise odd extrema
\[
O_-(t)=-(t-a)(t-d)(t-e),\qquad
O_+(t)=-(t-b)(t-c)(t-f). \tag{2}
\]
The stated ordering and factor assignment follow from the standard Hermite–Biehler and independent-box root-band argument, recalled in `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`. Equality within the second or third band is allowed; the first band must have positive length for the nodes below to exist.

Let five distinct positive squared-frequency nodes lie in the **arbitrary** positions
\[
a<t_1<t_2<b<t_3<t_4<c\le d<t_5<e. \tag{3}
\]
At each node allow any actual member of \(K\), independently of the other nodes, with any positive atom weights; also allow an infinity atom and any zero-odd atoms. Then **no** such measure can satisfy the original weak odd-cancellation/eight-Vieta-vertex obstruction.

In particular this excludes, for every eligible box, every minimum-support five-finite-plus-infinity obstruction of the displayed root-band placement. It includes all choices of corner or interior actual atoms; it does not require a chosen phase class for the even parts. The previous explicitly open fixed-box/node family `frontier-20261029-open-odd-box-five-node-exclusion-v1.md`, SHA-256 `f9cdddb08d93ded38ea227e3b25a577b5dceb991ab7b3e744d3dec9b626212fd`, is one nonvacuous instance, not an additional premise of the proof below.

## 2. Reduction to a four-node positive odd circuit

At nodes \(t_3,t_4\) every actual odd value is negative, and at \(t_5\) every actual odd value is positive. Merge same-frequency atoms by averaging actual box members, and delete zero-odd rows: their Vieta-vertex even contributions are nonnegative, so this preserves a weak no-go if one existed. The remainder cannot be empty.

The odd-moment equations imply every extreme positive circuit has either five finite nodes with alternating odd signs, or four finite nodes plus infinity with signs \((- ,+,-,+)\); this is elementary Vandermonde interpolation and is spelled out in `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`. Five finite alternation is impossible because the third and fourth odd signs agree. Any infinity circuit therefore uses nodes \(t_1,t_2,t_5\) and exactly one of \(t_3,t_4\), and forces its first two odd signs to be \(-,+\).

It is enough to show that **each** such four-node circuit has strictly positive even pairing at the same closed Vieta vertex
\[
F(t)=(-t)(c-t)(d-t). \tag{4}
\]
This is one of the eight vertices because the even-root gaps are \([0,a]\), \([b,c]\), \([d,e]\). A positive combination of circuits would then have positive pairing at (4), contradicting the required nonpositive vertex value. We prove the four-node claim for arbitrary nodes
\[
a<u_1<u_2<b<u_3<c\le d<u_4<e\le f,\tag{5}
\]
with selected actual odd values of signs \((- ,+,-,+)\).

## 3. Even upper envelope and endpoint reduction

Let \(U\) be the even upper-envelope cubic of \(K\). It is itself an actual even component; by independence it interlaces every odd component, so its roots lie in the three open gaps. Write
\[
U(t)=\ell_6(x-t)(y-t)(z-t),\quad
x\in(0,a),\ y\in(b,c),\ z\in(d,e),\quad\ell_6>0.
\]
At all four nodes in (5), \(F<0\). If \(E_i\) is the even part of the selected actual member, then \(E_i(u_i)\le U(u_i)\), and therefore
\[
\sum_iw_iF(u_i)E_i(u_i)\ge\sum_iw_iF(u_i)U(u_i). \tag{6}
\]
The unique positive odd circuit, with infinity weight 1 and physical finite weights, has
\[
w_i=\frac{1}{u_iO_i(u_i)H'(u_i)}>0,\qquad H(t)=\prod_{j=1}^4(t-u_j). \tag{7}
\]
Because the right side of (6) is affine in the coefficients of \(U\), Vieta multi-affinity reduces positivity to the eight vertex cubics
\[
V(t)=(x-t)(y-t)(z-t),\quad x\in\{0,a\},\ y\in\{b,c\},\ z\in\{d,e\}. \tag{8}
\]
At \(u_1,u_2\), \(V<0\), so their positive contributions are minimized by the actual odd extrema \(O_-(u_1)<0\), \(O_+(u_2)>0\). At \(u_3\), both odd extrema are negative: choose \(O_+\) if \(V(u_3)>0\), otherwise \(O_-\). At \(u_4\), both are positive: choose \(O_-\) if \(V(u_4)>0\), otherwise \(O_+\). These are exact endpoint minima of the positive/negative contributions; allowing these choices separately only makes the desired lower bound stronger.

For the four nodes put
\[
R_\pm(t)=\frac{F(t)V(t)}{tO_\pm(t)},\qquad
G=\sum_{i=1}^4\frac{R_{\sigma_i}(u_i)}{H'(u_i)},\tag{9}
\]
using the minimizing signs just specified. The derivatives \(H'(u_i)\) have signs \(-,+,-,+\). We show \(G>0\) in all four choices of \((y,z)\), for both choices of \(x\).

## 4. Four exact vertex cases

**Case \(y=c,z=d\).** All four values \(V(u_i)\) are negative. Every original term \(w_iF(u_i)V(u_i)\) is strictly positive, so \(G>0\).

**Case \(y=b,z=d\).** The minimizing odd choices are \((- ,+,+,+)\). For either \(x=0\) or \(x=a\), cancellation of the common factors gives
\[
R_+(t)=-\frac{(t-x)(t-d)^2}{t-f}.
\]
Polynomial division and the four-node divided-difference identity give
\[
\sum_i\frac{R_+(u_i)}{H'(u_i)}
=\frac{(f-x)(f-d)^2}{\prod_i(u_i-f)}>0,
\]
since all \(u_i<f\). Replacing \(R_+\) by \(R_-\) at the first node adds a positive quantity: \(R_-(u_1)<0<R_+(u_1)\) and \(H'(u_1)<0\). Thus \(G>0\).

**Case \(y=c,z=e\).** The minimizing odd choices are \((- ,+,-,-)\). For \(x=a\), factor cancellation gives \(R_-(t)=-(t-c)^2\), whose four-node divided difference is zero. The sole replacement at \(u_2\) is positive because \(R_+(u_2)>0>R_-(u_2)\) and \(H'(u_2)>0\). Thus \(G>0\). For \(x=0\), each term is the corresponding \(x=a\) term multiplied by \(u_i/(u_i-a)\), a positive decreasing function of \(u_i\). The first three terms are positive and the last is negative; hence the new sum is at least \(u_4/(u_4-a)\) times the positive \(x=a\) sum.

**Case \(y=b,z=e\).** The minimizing odd choices are \((- ,+,+,-)\). First take \(x=a\). Put \(D=O_+-O_-\) and \(\Delta(t)=D(t)/(f-t)>0\) on the nodes. Then
\[
R_-(t)=-(t-b)(t-c),\qquad R_+(t)-R_-(t)=\Delta(t).
\]
The quadratic baseline has zero four-node divided difference, so with \(h(t)=(t-u_1)(u_4-t)\),
\[
G=\frac{\Delta(u_2)/h(u_2)-\Delta(u_3)/h(u_3)}{u_3-u_2}. \tag{10}
\]
The ratio \(h(u_3)/h(u_2)\) increases as either \(u_1\) increases or \(u_4\) increases; its value is therefore strictly larger than the value obtained at \(u_1=a,u_4=d\). For the latter compare
\[
W(t)=\frac{\Delta(t)}{(t-a)(d-t)}
=\frac{e-t}{f-t}+\frac{(b-t)(c-t)}{(t-a)(d-t)}. \tag{11}
\]
At \(u_2\in(a,b)\), the second summand is positive; at \(u_3\in(b,c)\), it is negative. The first summand is nonincreasing because \(e\le f\). Hence \(W(u_2)>W(u_3)\), which together with the above ratio bound makes the numerator in (10) strictly positive. For \(x=0\), the factor \(u_i/(u_i-a)\) is positive and decreasing; the first two terms are positive and the last two negative, so the \(x=0\) sum is at least \(u_3/(u_3-a)\) times the positive \(x=a\) sum.

All eight vertices therefore have positive pairing with each four-node circuit. Multi-affinity gives positive pairing with \(U\), and (6) gives positive pairing with arbitrary actual even members. Since both possible circuits use the **same** \(F\), every positive odd-canceling combination is excluded. This proves the theorem.

## 5. Scope and assurance

The proof uses exact written algebra, the classical Hermite–Biehler/root-band ordering, elementary divided differences and finite-dimensional positive-circuit decomposition. It does not use numerical sampling, another unreviewed theorem as an implicit substitute, or any external model. The named weak-circuit/root-band packets supply the explicitly identified standard consequences; the four vertex proofs are displayed here. This result leaves other five-node placements, six or more finite frequencies, arbitrary no-go certificates and universal SPR7 synthesis **open**. It is not a formal proof, independent scientific review, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
