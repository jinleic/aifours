# Stronger disposition of the ratio-gap example

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** The particular 14-endpoint neighborhood used to illustrate `frontier-20261028-five-node-ratio-gap-open-neighborhood-v1.md` has a stronger property than the conditional five-frequency obstruction: the single numerator
\[
b(s)=(s+1)^7
\]
is common SPR for **every** box in that neighborhood. Therefore no negative atom certificate of *any* support exists for this particular example family. This does not by itself imply that an arbitrary box satisfying the three ratio-gap tests has a common numerator.

For the anchor box, the independent replay checked all 28 strict parity-corner Hurwitz determinants and 72 strict compactified Bernstein coefficients, obtaining
\[
\frac{P_{a,b}(t)}{(1+t)^7}\ge\frac1{10}\quad(a\in K,\ t\ge0),
\qquad\sum_{j=0}^7|b_j|=128.
\]
Changing each endpoint by at most \(\varepsilon=10^{-6}\), and projecting a perturbed denominator to the anchor box, changes the normalized pairing by at most \(7\varepsilon\cdot128<1/20\). The same lower bound holds along the connecting segment, so no imaginary-axis crossing occurs and homotopy preserves stability. Hence the fixed \(b\) works for every member of every perturbed box, not merely at sampled frequencies.

Frozen numerator, leaves and bounds: `frontier-20261028-wide-binomial-open-positive-frozen-v1.json`, SHA-256 `f97f4bf1732b70ccecc6f87301db83e275ef1532fbe0a0b708cf122bdc055ba8`. Independent checker `frontier-20261028-wide-binomial-open-positive-independent-kernel-v1.py`, SHA-256 `3107f40164248c8d32e85f8ce80f9e92509a1046f7605ac27af02706127c11fa`; receipt `frontier-20261028-wide-binomial-open-positive-independent-result-v1.json`, SHA-256 `dffc00202c883eb1eb7275f8a55cacf353357da28c0091442206bbef537127a9`. The receipt discloses a corrected stale local variable and resumed bound check.

The general ratio-gap theorem remains a separate conditional structural result; the named phase and root-order imports are unreviewed author candidates. Finite arithmetic used exact integers and `fractions.Fraction` on one Python Eval host, not formal or cross-vendor verification. No unrestricted arbitrary-box verdict or novelty claim is made.
