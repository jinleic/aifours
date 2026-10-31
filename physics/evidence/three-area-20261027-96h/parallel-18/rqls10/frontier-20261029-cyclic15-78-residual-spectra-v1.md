# The cyclic 6D complement has 78 remaining spectral classes

**EXACT-INTEGER-CHECKED CONDITIONAL AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:52:57 PDT 2026. This reduces the *cyclic-equivariant* G6 case to finitely many U spectra; it does not decide the remaining continuous amplitude/phase equations or the unrestricted QLS10 problem.

## Reduction

For `G6=Circ(15;±2,±5,±7)`, the previously pinned no-five-support theorem `frontier-20261029-cyclic15-no-five-spectral-support-v1.md` SHA-256 `595b702ae059ef2d94e7f98cf3d111ede1dd134f39a6daced541cd4cc50d75cc` says that a cyclic 45-distinct-ray 6D lift must have six distinct U eigenvalues, all occupied by v5. Normalize U so U^15=I. Orthogonality of v5 and U^(-5)v5 requires all three residue classes of eigenvalue exponents modulo 3. The all-field multiplicity theorem `frontier-20261029-cyclic15-unrestricted-multiplicity-v1.md` SHA-256 `128c8d68c92ef4db22169b0376e7a97758efa4ef18cdb086ecf4914de5482de7` excludes multiplicities `(4,1,1)` among those classes, leaving `(3,2,1)` or `(2,2,2)`.

A common exponent shift changes U only by an overall phase. The graph multipliers `u∈{1,4,11,14}` preserve its connection set `{±2,±5,±7}`. Relabeling vertices by u and replacing the cyclic implementer by the corresponding power of U therefore maps valid edge-ray configurations to valid ones; it permutes the d=2,5,7 ray orbits up to reversal. Thus the exponent sets may be classified under `a -> u a+s`.

Exact enumeration gives 5005 six-element exponent sets. Of these, 630 omit a U^5 class and 375 have the excluded `(4,1,1)` multiplicity, leaving 4000 sets in **80** affine classes. The two-coset determinant theorem `frontier-20261029-cyclic15-two-coset-determinant-no-go-v1.md` SHA-256 `b03725b2d3e562ebe70fd2e3e40ef71e167a960a5a3ba866c462ca1bf6fa8463` excludes two complete-3-coset classes. The **78 remaining** classes comprise 52 with multiplicities `(3,2,1)` and 26 with `(2,2,2)`.

The complete representatives, orbit sizes and exclusions are in `frontier-20261029-cyclic15-residual-spectra-v1.json`, SHA-256 `8a34864e6a25a22a8eb01e7c2acafaa1ad2c01c8cd1867fb02f536ee80a1fce0`. The integer-only generator `frontier-20261029-cyclic15-residual-spectra-v1.py`, SHA-256 `bca61e29cdb5f67c4b1eac7dc6fb07141313e91b116e3ecfc2379234e7f17e81`, records **PASS** at 02:52:57 PDT.

## Limits

These are **necessary spectral cases**, not existence claims; each still has unknown complex vector amplitudes and Gram constraints. A 6D lift without the named cyclic unitary need not occur in this list. The reduction depends on the unreviewed rank-4, resultant, multiplicity and determinant arguments cited above; all callers and the finite quotient require independent review. No formal-kernel proof or novelty claim is made.
