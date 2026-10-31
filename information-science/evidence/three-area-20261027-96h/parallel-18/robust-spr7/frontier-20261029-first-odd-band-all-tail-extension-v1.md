# All-tail extension of the first-odd-band five-node exclusion

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:36:50 PDT 2026**. **WRITTEN universal theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This extends `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`.

## Theorem

Under the same eligible independent septic-box hypotheses and odd bands \([a,b],[c,d],[e,f]\), no weak odd-cancellation/eight-Vieta-vertex no-go measure can have its positive finite support contained in five nodes
\[
a<t_1<t_2<b<t_3<t_4<c,\qquad t_5>t_4, \tag{1}
\]
plus optional infinity and zero-odd atoms. **There is no restriction on the fifth node's location.** Actual members and positive weights are arbitrary. In particular this removes the two minimal 5-finite-plus-infinity phase words \((2,1,3,2,4)\) and \((2,1,3,2,5)\) from the conservative twelve-word classification of `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`, whenever those words have their mandatory first-odd-band and second-even-band reversed pairs. This is not an exclusion of the remaining ten words or larger support.

## Proof

The predecessor proves the assertion for \(d<t_5<e\), including arbitrary actual denominator choices and both possible four-node odd circuits. The same circuit decomposition applies generally: at \(t_3,t_4\) all actual odd parts are strictly negative, so a five-finite-only circuit cannot alternate, and any infinity circuit must use a negative first node, a positive second node, one of \(t_3,t_4\), and a positive fifth node. Therefore there is no circuit at all if \(t_5\le c\) or \(t_5\ge f\), because every odd value there is nonpositive. Odd-zero atoms are discarded exactly as in the predecessor.

It remains to exclude circuits with \(c<t_5\le d\) or \(e\le t_5<f\); if an interval is empty there is nothing to show. Write the four circuit nodes \(u_1,u_2,u_3,u_4\), with
\[
a<u_1<u_2<b<u_3<c<u_4<f, \tag{2}
\]
and odd signs \((- ,+,-,+)\). At \(u_4\) the odd component can be positive only in the listed ranges; in either range the positive contribution below is minimized by choosing \(O_+(u_4)\), the largest actual odd value.

Use the same closed Vieta vertex \(F(t)=(-t)(c-t)(d-t)\), and reduce the even upper-envelope to the eight cubics \(V=(x-t)(y-t)(z-t)\), \(x\in\{0,a\},y\in\{b,c\},z\in\{d,e\}\), exactly as in the predecessor. At \(u_1,u_2,u_3\), \(F<0\). At \(u_4\in(c,d)\), both \(F\) and \(V\) are positive; at \(u_4\in(e,f)\), both are negative. At \(u_4=d\) the product vanishes, while at \(u_4=e\) it is nonnegative, with equality possible for the boundary vertex \(z=e\). Consequently the fourth circuit contribution is never negative.

If \(y=c\), the first three \(V\)-values are negative, so all first three pairings are strictly positive and the fourth is nonnegative. If \(y=b\), only the third contribution can be negative. Its minimizing odd endpoint is \(O_+\); the first and second minimizing endpoints are \(O_-\) and \(O_+\). Choosing \(O_+\) also at the fourth node, set \(H(t)=\prod_i(t-u_i)\) and
\[
R_+(t)=\frac{F(t)V(t)}{tO_+(t)}
=-\frac{(t-x)(t-z)(t-d)}{t-f}. \tag{3}
\]
Polynomial division and the four-node divided-difference identity give
\[
\sum_i\frac{R_+(u_i)}{H'(u_i)}
=\frac{(f-x)(f-z)(f-d)}{\prod_i(u_i-f)}\ge0. \tag{4}
\]
The denominator is positive and the numerator is nonnegative. Replacing \(R_+\) by \(R_-\) at \(u_1\) adds a **strictly positive** term: \(R_-(u_1)<0<R_+(u_1)\) and \(H'(u_1)<0\). Thus the total vertex pairing is strictly positive, including the endpoint and repeated-factor cases.

This works for both possible four-node circuits at the same vertex \(F\); their arbitrary positive combination cannot satisfy the nonpositive Vieta-vertex condition. The cases together establish (1).

## Limits

The statement excludes a complete actual-box node-placement pattern, not a direct strictly-negative-coordinate certificate whose odd moments do not cancel, not all five-node weak certificates, and not the original universal synthesis-or-obstruction question. The algebra and case split are written mathematics; no machine check, independent scientific review, formal proof, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
