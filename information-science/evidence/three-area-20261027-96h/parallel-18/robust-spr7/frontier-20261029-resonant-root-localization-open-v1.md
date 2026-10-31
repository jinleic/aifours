# An open family with two forced localized numerator roots

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** Perturb each of the 14 endpoints of the wide septic box in `frontier-20261029-four-nonreal-roots-wide-box-v1.md` independently by at most \(10^{-17}\), retaining monicity. Every resulting box is strictly Hurwitz, has the **same fixed** common SPR numerator
\[
a(s)=(s+1)\left((s+\tfrac1{100})^2+1\right)^3,
\]
and every common numerator has at least two upper-half-plane roots within distance \(197/500\) of \(i[9/10,11/10]\), counted with multiplicity, plus their conjugates. This is a nonempty 14-dimensional open family. The root statement concerns the literal numerator, even if cancellation occurs.

The endpoint perturbation is much smaller than the anchor coefficient radius \(1/500000\), so the original denominator \(a\) remains in **every** perturbed box. The independently replayed anchor compactified pairing margin \(\delta\) and coefficient sum \(S=\sum|a_j|\) satisfy \(14\cdot10^{-17}S\le\delta\). Project each perturbed denominator coefficientwise into the anchor box: the normalized pairing with the fixed \(a\) changes by at most \(7\cdot10^{-17}S\le\delta/2\), including along the connecting segment. Thus no imaginary-axis crossing occurs; homotopy preserves Hurwitz stability and the fixed common numerator. Applying the independently supported written phase-localization theorem to the retained actual member \(a\) gives the root constraint.

Frozen constants: `frontier-20261029-resonant-root-localization-open-frozen-v1.json`, SHA-256 `50cf9f1ebadde94ea1ab7be8f7b9aa140c91d3443dcf078d1bec3e2a1d4e94f3`. Independent checker `frontier-20261029-resonant-root-localization-open-independent-kernel-v1.py`, SHA-256 `98d0b0f9246d831112f4be0b05f9e031826bfede57b7645816bc857fad96aef2`; receipt `frontier-20261029-resonant-root-localization-open-independent-result-v1.json`, SHA-256 `80b2dc98fb15909664caa72754beb39224cbc2c1349a4350417bba0885117589`. The anchor localization theorem is SHA-256 `795ea7151c2875c63ec31277a4b3a5803056f7f63f898d1af4acf3ccd7023b89`.

The finite bounds use exact integers and `fractions.Fraction` on one Python Eval host; the phase and homotopy deductions are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
