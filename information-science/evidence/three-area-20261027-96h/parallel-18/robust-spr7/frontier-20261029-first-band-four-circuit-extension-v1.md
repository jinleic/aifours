# A universal first-odd-band circuit exclusion with an earlier third node

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:39:16 PDT 2026**. **WRITTEN universal theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This extends the first-band result `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`, and its all-tail addendum `frontier-20261029-first-odd-band-all-tail-extension-v1.md`, SHA-256 `a4e6925a0fb3207c73b9fe3c764a2697a398985f831c2bc753c3c63d8ec1aade`.

## 1. Four-node theorem

For any all-Hurwitz independent monic septic box with odd bands \([a,b],[c,d],[e,f]\) and extremal cubics (2) in the first named input, consider any positive four-finite-node-plus-infinity odd-canceling circuit. Let its finite nodes and actual odd values satisfy
\[
a<u_1<u_2<b,\quad u_2<u_3\le c,\quad u_4>u_3,\qquad
\operatorname{sgn}(O_i(u_i))=(-,+,-,+). \tag{1}
\]
Then its even pairing at the **same** closed Vieta vertex
\[
F(t)=(-t)(c-t)(d-t) \tag{2}
\]
is strictly positive, irrespective of the actual member chosen at each node. Zero odd values are excluded by the circuit definition. The statement holds for arbitrary node locations within (1), including \(u_3\) inside the first odd band, and for arbitrary eligible coefficient widths.

## 2. New case: the third node is in the first odd band

When \(b<u_3<c\), the statement follows from the two named predecessor packets; when \(u_3=c\), use the argument below with the third even contribution equal to zero. Assume now \(u_3\le b\).

As in the first predecessor, replace each actual even value from below by the common even upper-envelope \(U\) because \(F<0\) at the first three nodes. Reduce \(U\) by multi-affinity to the eight even-root vertex cubics \(V=(x-t)(y-t)(z-t)\), with \(x\in\{0,a\},y\in\{b,c\},z\in\{d,e\}\). The first three vertex values are negative, except that \(V(u_3)=0\) is allowed at \(u_3=y=b\); hence their pairings with \(F\) are nonnegative and the first two are strictly positive.

If \(u_4<b\), it is also in the first odd band, so its pairing is strictly positive. A positive selected odd value cannot occur in \([b,c]\) or at/above \(f\). If \(c<u_4\le d\) or \(e\le u_4<f\), the fourth vertex pairing is nonnegative by the sign argument in the all-tail predecessor. In all these cases the sum is positive.

The only nontrivial remaining placement is \(d<u_4<e\). If \(z=d\), the fourth vertex value is negative and all four pairings are nonnegative, with the first two strict. If \(z=e\), the fourth pairing is negative. The worst odd choices are \((- ,+,-,-)\), and for \(x=a\),
\[
R_-(t)=\frac{F(t)V(t)}{tO_-(t)}=-(t-y)(t-c),\qquad y\in\{b,c\}. \tag{3}
\]
This is a quadratic, so its four-node divided difference vanishes. The only endpoint correction, at \(u_2\), is strictly positive because \(R_+(u_2)>0>R_-(u_2)\) and \(H'(u_2)>0\). Hence the sum is positive. For \(x=0\), multiply each term by the positive decreasing factor \(u_i/(u_i-a)\); the first three terms are nonnegative and the last negative, so the total is at least \(u_4/(u_4-a)\) times the positive \(x=a\) total. This also covers \(u_3=c\) when its selected odd value is negative, since the third contribution vanishes and \(O_-(c)<0\).

Thus every vertex pairing is positive, and so is the upper-envelope pairing. The actual-even pairing is at least that upper-envelope pairing whenever \(F<0\); in the two intervals where \(F>0\) or vanishes at the fourth node, its fourth contribution is itself nonnegative because every actual even component has the same positive sign there, so the above lower-bound argument remains valid. This proves the four-node theorem.

## 3. Four of twelve minimal phase words are excluded

Apply (1) to every extreme odd circuit in a weak no-go with five finite nodes plus infinity. The phase/root-band facts and the conservative twelve-word list are in `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`. In each word
\[
(2,1,2,5,4),\quad(2,1,3,2,4),\quad
(2,1,3,2,5),\quad(2,1,3,5,4), \tag{4}
\]
the first-odd-band backward pair gives \(u_1,u_2\in(a,b)\), every possible third negative node is at or before the second odd band's lower endpoint \(c\), and the later selected fourth node has positive odd value. Each constituent circuit therefore has a positive pairing at the same \(F\). The weak no-go is impossible. Equality/zero-odd rows are handled by deletion as in the named input; the required backward pairs have strict nonzero parity signs.

This reduces the 12 conservative words by four, but the other eight words, all larger support sizes, and the original arbitrary-box SPR7 synthesis-or-obstruction question remain open. It does not claim to rule out direct strictly-negative-coordinate certificates whose odd moments do not cancel. The arguments are written mathematics, with no machine check, independent review, formal proof, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
