# A univariate norm-gap synthesis criterion for heterogeneous boxes

**Status: WRITTEN candidate with an exact WRITTEN-checked-in-kernel example; author result, not parent adoption.** The coefficientwise cone in `frontier-20261029-heterogeneous-radius-cone-theorem-v1.md` has a broader all-degree sufficient form that can be checked by exact univariate polynomial positivity. It constructs the common numerator as the stable center, but it is not a necessary condition and does not resolve arbitrary boxes.

Let \(a(s)=s^n+\sum_{j<n}a_js^j\) be a real monic Hurwitz center, and let \(r_j\ge0\) bound independent coefficient perturbations. Define \(E,O,A,B,V,H\) exactly as in the preceding heterogeneous-radius theorem:
\[
V=E^2+tO^2=|a(i\sqrt t)|^2,\qquad H=A^2+tB^2.
\]
If
\[
\boxed{\quad V(t)-H(t)>0\quad\text{for every }t\ge0,\quad}
\]
then all polynomials in the box are Hurwitz and the fixed numerator \(a\) is common SPR. The test is sufficient even when \(V-H\) has negative monomial coefficients.

**Proof.** \(V-H\) has degree \(n\) and leading coefficient 1. Strict positivity on the half-line and its limiting compactified value 1 give some \(\delta>0\) with
\[
V(t)-H(t)\ge\delta(1+t)^n\quad(t\ge0).
\]
For every box member and its straight path to \(a\), Cauchy–Schwarz gives
\[
P_{p,a}\ge V-\sqrt{VH}
=\frac{(V-H)\sqrt V}{\sqrt V+\sqrt H}
\ge\frac\delta2(1+t)^n.
\]
Thus no imaginary-axis root occurs along that path, so Hurwitz stability follows by homotopy. With \(S=\sum_j a_j+\sum_{j<n}r_j\), \(|p(i\sqrt t)|\le S(1+t)^{n/2}\), and \(\operatorname{Re}(a/p)\ge\delta/(2S^2)>0\). ∎

A rational certificate can consist of exact compactified Bernstein leaves or a Sturm/nonnegativity proof for this single univariate polynomial; no solver-based numerator search is required. The norm inequality remains conservative relative to the actual four-corner pairing minimum.

## Resonant example outside the coefficientwise cone

The wider septic box in `frontier-20261029-four-nonreal-roots-wide-box-v1.md`, centered at \((s+1)((s+1/100)^2+1)^3\) with all radii \(1/500000\), satisfies the strict norm-gap criterion, although \(V-H\) has **four negative monomial coefficients**. Independent exact convolution and 24 strictly positive compactified Bernstein coefficients give
\[
\frac{V(t)-H(t)}{(1+t)^7}\ge
\frac{6756000135001}{112000000000000000000000000}>0.
\]
The separate phase theorem proves every common numerator for this same box has at least two nonreal root pairs; hence the criterion also handles a genuinely resonant center, not just the sector-damped class.

Frozen example and leaves: `frontier-20261029-resonant-norm-gap-example-frozen-v1.json`, SHA-256 `10fcfca76926f093603e28740f9e20b3c89fef092110c285190c74680d1f2b17`. Independent checker `frontier-20261029-resonant-norm-gap-example-independent-kernel-v1.py`, SHA-256 `c20c1c513fa1cd86b150222417ab3bdde25dc753e331d1957b01bc5dad7f11ea`; receipt `frontier-20261029-resonant-norm-gap-example-independent-result-v1.json`, SHA-256 `b77fa3d0912b1dfe311360ddff8f3edf2e4bf0b1633a4d3b4eaf6107e08763fa`.

The general proof is written mathematics; the finite example uses exact integers and `fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or unrestricted negative certificate is claimed.
