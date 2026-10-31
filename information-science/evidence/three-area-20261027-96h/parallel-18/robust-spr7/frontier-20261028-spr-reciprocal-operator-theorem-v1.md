# Reciprocal derivatives give further necessary SPR inequalities

**Status: WRITTEN theorem with WRITTEN-checked-in-kernel finite examples; author candidate, not parent adoption.** This extends the previous \(D\) and \(I+hD\) preservation result. It does not establish a negative certificate or an unrestricted septic theorem.

## Reciprocity and two new operators

For a real degree-\(n\) polynomial with nonzero constant term, set \(R_nf(s)=s^n f(1/s)\). If \(a,b\) are equal-degree real Hurwitz polynomials with \(b/a\) SPR and positive leading coefficients, then \(R_nb/R_na\) is SPR. At \(\omega\ne0\), it is the complex conjugate of \(b(i/\omega)/a(i/\omega)\); the endpoints \(0\) and infinity are positive coefficient ratios. Reciprocal roots of a strictly Hurwitz polynomial remain in the open left half-plane.

Applying the already proved derivative and \(I+hD\) preservers to the reciprocal ratio, then reversing back, shows that for every \(h\ge0\) both ratios
\[
\frac{n b-sb'}{n a-sa'},\qquad
\frac{b+h s(n b-sb')}{a+h s(n a-sa')}
\]
are SPR. The first ratio has equal degree \(n-1\), the second equal degree \(n\), and their denominators are Hurwitz. Indeed
\[
R_{n-1}D R_nf=n f-sf',\qquad
R_n(I+hD)R_nf=f+h s(n f-sf').
\]
A real Hurwitz polynomial with positive leading coefficient has all positive coefficients, so the leading coefficients that remain after these operations are positive and nonzero. Iterating these reciprocal operations and the earlier forward operations preserves SPR as long as the degree remains positive.

For a septic common numerator, pairings after any of these operations are again linear in the original eight numerator coefficients. They may be included in a mixed nonnegative-row certificate exactly as in the preceding operator packet, with each transformed polynomial arising from an **actual** original denominator. The transformed family is correlated; no independent rectangular hull is assumed.

## Exact example and bounded search

For \(a=(s+1)^7\), \(b=(s+1)^7+s\), the reciprocal-derivative transform and the reciprocal \(I+hD\) transforms at \(h\in\{0,1/10,1,10\}\) have complete positive rational Bernstein certificates. The smallest compactified bound among these five checks is \(7/75\). Frozen example `frontier-20261028-spr-reciprocal-operator-example-frozen-v1.json` has SHA-256 `7637ba34ca2348aa440dbab6d3b531e28dc7487dfe8dd4ada3191793d5f7fa72`. Independent standalone checker `frontier-20261028-spr-reciprocal-operator-independent-kernel-v1.py`, SHA-256 `1213a8a656cf08b82b4055b4c1c5c9eacb1b00b07d87cd4bcfa3c6463702fec2`, constructs the operators by explicit coefficient reversal and differentiation, checks 68 positive Hurwitz minors and every Bernstein leaf, and rejects a corrupted leaf. Receipt `frontier-20261028-spr-reciprocal-operator-independent-result-v1.json` has SHA-256 `0f137ac6798c7a575bfe63722d4b7482fa6fcdb0b6b1a29dbf52f245b9155012`.

A separate bounded exact search on an actual stable asymmetric septic box combined forward and reciprocal-conjugate \(D^k(I+hD)\) rows, \(k=0,\ldots,6\), \(h\in\{0,1\}\), four actual corners, and a finite frequency grid. The first and second solves used 896 and 1,344 rows respectively; both finite minimax margins were positive and the corresponding grid candidates failed at further original frequencies. It found neither a negative certificate nor full-halfline synthesis. An independent recursive-differentiation/convolution pass matched 7,168 first-grid unit-coefficient values. Search data `frontier-20261028-two-sided-operator-hybrid-search-results-v1.json` has SHA-256 `e49263d2d6c09f8c7e432401fa4997ae2b3841b0fa42dedb614a901c97f9ea8a`.

The general reciprocity/operator argument is written mathematics; only the finite examples and row identities were checked with exact rational arithmetic on one Python Eval host. No formal verification, cross-vendor review, novelty clearance, or general septic verdict is claimed.
