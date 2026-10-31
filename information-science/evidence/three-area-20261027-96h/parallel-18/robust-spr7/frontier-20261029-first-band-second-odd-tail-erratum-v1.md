# Erratum: the second-odd-band tail is not proved

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:40:46 PDT 2026**. This is an additive correction to:

- `frontier-20261029-first-odd-band-all-tail-extension-v1.md`, SHA-256 `a4e6925a0fb3207c73b9fe3c764a2697a398985f831c2bc753c3c63d8ec1aade`;
- `frontier-20261029-first-band-four-circuit-extension-v1.md`, SHA-256 `02014c2e520266977bb9fd157dbb5e92793513190d9c89c2c932c0566e79d465`;
- checkpoint 068's all-tail and two-word statements, which must be read with this correction.

## Gap and corrected scope

For the chosen Vieta vertex \(F(t)=(-t)(c-t)(d-t)\), when the fourth circuit node lies in the **open second odd band** \(c<u_4<d\), one has \(F(u_4)>0\). The actual even value is bounded **above** by \(U(u_4)\), not below. Thus replacing the actual fourth value by \(U\) cannot lower-bound its pairing, and the all-tail proof's appeal to the upper-envelope vertex argument is invalid in this region. The fact that the actual fourth contribution is positive does not alone show that it offsets the possibly negative third contribution. The theorem might still hold, but this proof does not establish it; no counterexample is asserted.

The first predecessor `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`, uses only \(d<u_4<e\), where \(F<0\), and is unaffected. In the all-tail addendum, the no-circuit regions \(u_4\le c\) and \(u_4\ge f\), the point \(u_4=d\) where \(F=0\), and the region \(e\le u_4<f\) where \(F<0\) remain covered by its stated arguments; the open interval \((c,d)\) is **OPEN**.

For the four-circuit extension, its new proof for \(u_3\le b\) is valid even when \(u_4\in(c,d)\), because the first three actual contributions are nonnegative with two strict positives and the actual fourth contribution is nonnegative; no upper-envelope substitution at the fourth node is needed. The boundary \(u_3=c\) is likewise covered in \((c,d)\): \(F(u_3)=0\), the first two actual contributions are positive and the fourth is nonnegative. For \(b<u_3<c\) and \(c<u_4<d\), the four-circuit claim remains unproved. Thus use the four-circuit theorem only with the additional condition \(u_3\le b\), or \(u_3=c\), or \(u_4\notin(c,d)\).

The corrected coverage removes **three entire** conservative five-finite-plus-infinity words,
\[
(2,1,2,5,4),\qquad(2,1,3,2,5),\qquad(2,1,3,5,4),
\]
because their relevant positive fourth nodes lie after \(d\) or their third node is at/before \(b\). The word \((2,1,3,2,4)\) is only partially excluded: configurations with the fifth node in \((c,d)\) remain open when a circuit's third node lies in \((b,c)\). The other eight words also remain open. No general five-node or original SPR7 verdict follows.

This correction identifies a proof gap, not a counterexample, and does not modify frozen bytes. Exact LP experiments for some fixed data were inconclusive as a universal matter and are not a substitute for a proof. All results remain author-written and unreviewed, with no formal verification, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
