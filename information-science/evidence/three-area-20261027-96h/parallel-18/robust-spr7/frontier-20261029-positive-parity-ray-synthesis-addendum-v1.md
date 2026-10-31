# Addendum: positive parity rays, not only identical parity

**Status: WRITTEN candidate, not parent adoption.** This strictly generalizes the compact-family theorem in `frontier-20261029-fixed-parity-universal-synthesis-v1.md` (SHA-256 `8c6329652525eccc6a1e10e9d9ecf7b5a0e4cb4a2336b1f8e6fff0c260986ab1`).

Let \(K\) be any nonempty compact family of monic strictly Hurwitz real degree-\(n\) polynomials, \(n\ge1\), and take \(a_*\in K\). It is enough that **either** all even parts lie on the same positive ray, \(E_a=c_aE_*\) with \(c_a>0\), **or** all odd parts lie on the same positive ray, \(O_a=d_aO_*\) with \(d_a>0\). In the respective cases the same parity-scaled constructions
\[
(E_b,O_b)=(E_*,\varepsilon O_*),\qquad
(E_b,O_b)=(\varepsilon E_*,O_*)
\]
are common strictly positive-real numerators for all sufficiently small positive \(\varepsilon\), after monic normalization.

For the even-ray case the pairing is \(c_aE_*^2+\varepsilon tO_*O_a\); for the odd-ray case it is \(td_aO_*^2+\varepsilon E_*E_a\). The positive scalar factors have strictly positive minima on compact \(K\): their parity coefficient vectors depend continuously on \(a\), and a reference nonzero coefficient identifies the scalar. At the common finite parity zeros the other part has the same alternating sign for every stable member, while the zero and infinity cases are exactly those handled in the pinned proof. The same compactified-neighborhood argument therefore applies verbatim.

A transparent special case is the two-ray family \(E_a=c_aE_*\), \(O_a=d_aO_*\) with positive scalars: \(a_*\) itself is common because \(P_{a,a_*}=c_aE_*^2+td_aO_*^2>0\); the two terms cannot simultaneously vanish for a Hurwitz reference, and endpoints are positive. The theorem additionally allows the **other** parity to vary arbitrarily within the compact stable family.

For monic even degree, the even leading coefficient forces \(c_a=1\), while for monic odd degree the odd leading coefficient forces \(d_a=1\); in the opposite parity each ray may genuinely vary. This does not assert that an arbitrary full-width coefficient box has a parity-ray structure or settle the original seven-width decision. The degree, signs, phase interlacing and compactness are written deductions, not formal proof, cross-vendor review, or novelty clearance.
