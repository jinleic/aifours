# Strict atom certificates require many frequencies in every odd degree

**Status: WRITTEN candidate, not parent adoption.** This extends the oriented-moment argument in `frontier-20261029-strict-negative-certificate-two-band-obstruction-v1.md` (SHA-256 `33cce85c5451984a670de2ae05c921ea3a61d0c88c867c3c81a1bb94cd026783`) from septics to every odd degree. It is a direct structural no-go for strict negative-coordinate certificates, not an existence theorem.

Let \(n=2m+1\ge3\), and let \(K\) be a compact independent coefficient box of monic strictly Hurwitz degree-\(n\) real polynomials. Any finite positive-weight actual-denominator atom sum whose \(n+1\) numerator-monomial coefficients are all strictly negative must involve at least
\[
\boxed{m+2=\frac{n+3}{2}}
\]
distinct **positive** squared frequencies after merging repeated nodes. Positive zero and compactified-infinity atoms are allowed and do not reduce this requirement.

## Proof

For an actual denominator write \(a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t)\); both parts have degree \(m\). Merge atoms at repeated \(t_i>0\) using their positive-weight average denominator, which remains in \(K\). Define \(x_i=\mu_iE_i\), \(y_i=\mu_i t_iO_i\) with positive uncompactified weights. Strict negativity on the even and odd numerator monomials gives, for \(z=x,y\),
\[
(-1)^{k+1}\sum_i t_i^k z_i>0,\qquad 0\le k\le m.
\]
Zero and infinity atoms only strengthen the appropriate endpoint inequalities.

These signs force each nonzero input sequence \(z_i\) to contain the oriented alternating subsequence of length \(m+1\), beginning with \(-\). Otherwise its sign word fits inside \(m+1\) alternating blocks beginning with \(+\). Choose \(m\) positive roots at the block gaps, before the first node or after the last as needed. The polynomial \(q(t)=\prod_{r=1}^m(s_r-t)\) then has the same sign as every nonzero \(z_i\), so \(\sum z_iq(t_i)>0\). But its coefficients have signs \((+,-,+,\ldots)\), making **every** term of the moment expansion strictly negative. This contradiction proves the subsequence condition.

If there are only \(m+1\) positive nodes, neither parity has a zero at a node and both sign sequences are exactly the alternating subsequence. They begin with \((E,O)=(-- )\) and reverse both signs at all \(m\) transitions. For every stable degree-\(2m+1\) polynomial, phase rises from 0 to \((2m+1)\pi/2\); the actual box's independent parity choices imply strictly ordered global root bands \(E_1<O_1<\cdots<E_m<O_m\). Assign phase classes \(q\in\{0,\ldots,2m\}\). As in the pinned septic proof, an earlier sample's class exceeds a later one's by at most one; a simultaneous sign reversal therefore advances at least two classes. The first \((-- )\) sample has class at least 2, so the final class is at least \(2+2m\), impossible because it is at most \(2m\). Fewer than \(m+1\) nodes cannot contain the subsequence. Hence at least \(m+2\) are necessary.

For \(n=7\) this gives \(m+2=5\); the cited septic packet further proves that every hypothetical five-node strict certificate must repeat two particular, ordered parity-root bands. Neither statement excludes certificates with more nodes or supplies an actual negative box. The sign lemma, parity-root ordering, compactness and phase-advance proof are written mathematics; no formal proof, independent-family review or novelty clearance is claimed.
