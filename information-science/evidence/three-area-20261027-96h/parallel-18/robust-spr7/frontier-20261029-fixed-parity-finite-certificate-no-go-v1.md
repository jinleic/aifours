# Fixed parity forbids finite atom certificates even without compactness

**Status: WRITTEN candidate, not parent adoption.** This is a genuine obstruction to both finite zero annihilators and strictly negative-coordinate atom certificates, and also shows exactly why compactness is material to an existence-versus-certificate alternative.

## General finite-support obstruction

Let \(\mathcal F\) be **any**, possibly noncompact or nonconvex, family of monic strictly Hurwitz real degree-\(n\) polynomials whose even parts lie on one positive ray, or whose odd parts lie on one positive ray. Then no finite collection of positive-weight actual denominator/frequency atoms can have an aggregate pairing functional that is identically zero on all degree-\(\le n\) numerator coefficients. Nor can such a collection have all aggregate monomial coefficients strictly negative. The conclusion includes zero and compactified-infinity atoms.

Indeed any finite atom collection involves only finitely many actual denominators. That finite subfamily is compact and still has the same parity ray. The construction in `frontier-20261029-positive-parity-ray-synthesis-addendum-v1.md` gives it a single equal-degree numerator \(b\) with strictly positive pairings at all actual frequencies and with every coefficient strictly positive: it is obtained from a Hurwitz reference polynomial, whose coefficients are positive, by positive parity scalings. Endpoint pairings are also strictly positive. Thus the positive weighted aggregate evaluates strictly positively at \(b\); a zero coefficient vector would give 0, and an all-negative one would give a strictly negative value. Both are impossible.

For compact finite-width boxes in this class the theorem additionally supplies one common numerator for the **whole** family, giving a whole-box certificate obstruction. No claim is made for boxes with both parity parts free.

## A no-numerator family with no finite certificate

The closed convex noncompact septic family in `frontier-20261029-convex-septic-parity-compactness-addendum-v1.md` is monic and Hurwitz, has one common odd part, and has **no** common septic numerator. Nevertheless, every finite atom collection fails to be a zero or strict-negative certificate by the preceding paragraph. In this example no abstract existence step is necessary: if the finitely many selected denominators are \(a_{u_i,v_i}\), choose \(M=\max_i(u_i+v_i)\); the explicit \(b_M\) in `frontier-20261029-convex-parity-bounded-explicit-numerator-v1.md` has positive coefficients and strictly positive pairings with every selected denominator. The same contradiction applies to every finite positive-weight atom list.

Thus **all finite subfamilies** have common numerators while the whole noncompact family does not. A finite-certificate alternative proved for compact eligible boxes must not be carried over to arbitrary unbounded families. This example is not an original finite-width box and does not resolve the original decision.

The finite-subfamily argument, strict sign contradiction and the companion explicit construction are written mathematics. The reference coefficient factorizations and stability minors were checked in the independent exact replay pinned by the companion septic packet; no formal proof, cross-vendor review, novelty clearance or arbitrary-box verdict is claimed.
