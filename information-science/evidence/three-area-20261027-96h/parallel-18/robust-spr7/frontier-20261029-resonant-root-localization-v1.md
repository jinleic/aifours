# Two numerator roots must lie near the resonant imaginary segment

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The root-count obstruction for the explicit stable septic box in `frontier-20261029-four-nonreal-roots-wide-box-v1.md` admits a quantitative localization. Every common real exact-degree-seven SPR numerator \(b\) has **at least two upper-half-plane roots**, counted with multiplicity, within Euclidean distance
\[
R=\frac{197}{500}
\]
of the imaginary-axis segment \(i[9/10,11/10]\). Their conjugates give two lower-half-plane roots near the conjugate segment. The box has an independently certified unrestricted common numerator, so this is a root-geometry restriction, not an unrestricted negative certificate. The statement refers to literal numerator roots, including any that cancel.

## Proof

The phase proof in `frontier-20261029-common-numerator-nonreal-root-obstruction-v1.md` gives, for every common numerator,
\[
\Delta\theta_b>2\pi-3e,\qquad
 e=\frac{796040}{3990199},\qquad
\Delta\theta_b=\theta_b(11/10)-\theta_b(9/10).
\]
The sharper rational \(e\), rather than its \(1/4\) upper bound, is used here. Assume at most one upper-half-plane root of \(b\), counted with multiplicity, is within distance \(R\) of the indicated segment. Since \(R<9/10\), no real or lower-half-plane root can lie that close. If such an upper root exists, group it with its conjugate; their total phase increase is less than \(\pi\). Every one of the remaining five roots stays at least distance \(R\) from every point \(i\omega\) on the segment. If no close upper root exists, all seven roots stay that far and the even stronger bound below applies.

For a Hurwitz root \(r=-a+i\beta\), \(a>0\), its phase derivative is
\[
\frac{d}{d\omega}\arg(i\omega-r)
=\frac{a}{a^2+(\omega-\beta)^2}\le\frac1{|i\omega-r|}.
\]
Thus the remaining five roots contribute at most \(5(1/5)/R=1/R\), giving
\[
\Delta\theta_b<\pi+\frac1R.
\]
If no close pair exists, the bound \(7(1/5)/R=7/(5R)\) is also below \(\pi+1/R\), since \(R>0.4/\pi\). Exact rational arithmetic verifies
\[
\pi>\frac{281476}{89625}>\frac1R+3e,
\]
where the first inequality follows from Machin's identity and \(\arctan x>x-x^3/3\), \(\arctan x<x\). Therefore \(2\pi-3e>\pi+1/R\), a contradiction. At least two upper roots lie within \(R\) of the segment.

The anchor phase and stable-box proofs are named imports. Exact rational constants: `frontier-20261029-resonant-root-localization-frozen-v1.json`, SHA-256 `f60dc422263b765f47db62340084394829ce3e28dcf97645479dd21ba6259250`. Independent checker `frontier-20261029-resonant-root-localization-independent-kernel-v1.py`, SHA-256 `53b333aafcb8d4002d174ac391a2136a3b7b4d33f72ee965f395b699ffd612c0`; receipt `frontier-20261029-resonant-root-localization-independent-result-v1.json`, SHA-256 `23910e0b18e5cef346d9ead7bf78047c5204be315e0f21085a7c44401d1571d2`. The wider stable-box theorem is SHA-256 `fbfb4a689a0d2f194054fd4426d5cee749a8c710152c6ae6011b05192739d6a1`.

The finite rational comparison was checked on one Python Eval host; the rootwise phase derivative, conjugate-pair increment and pigeonhole argument are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
