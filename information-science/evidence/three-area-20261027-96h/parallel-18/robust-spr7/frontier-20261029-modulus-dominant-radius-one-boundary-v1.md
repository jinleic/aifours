# Exact radius-one boundary for modulus-dominant centers

**Status: WRITTEN; author candidate, not parent adoption.** The threshold \(r<1\) in `frontier-20261029-real-rooted-center-uniform-box-theorem-v1.md` and `frontier-20261029-sector-damped-center-uniform-box-v1.md` has the following exact boundary classification.

Let \(a\) be a real monic Hurwitz polynomial of degree \(n\), \(c>0\), and assume its scaled center \(A(z)=c^{-n}a(cz)\) satisfies
\[
|A(i\sqrt t)|^2\ge(1+t)^n\quad(t\ge0).
\]
At the **closed** independent coefficient radius \(r=1\), every denominator in the box is Hurwitz and \(a\) is a common SPR numerator **if and only if**
\[
a_0>c^n.
\]
This includes both the real-rooted and sector-damped centers in the cited theorems. It does not claim a classification for \(r>1\) or for centers without the modulus hypothesis.

**Proof.** The geometric-sum inequality in the earlier theorem is in fact strict for every \(t>0\): the polynomial \((1+t)^n-A_n(t)^2-tB_n(t)^2\) has nonnegative coefficients and its coefficient of \(t^n\) is 1. Hence for every coefficient perturbation of radius at most 1,
\[
P_{P,A}(t)\ge |A|^2-|A|\sqrt{A_n^2+tB_n^2}>0\quad(t>0).
\]
At \(t=0\), the smallest scaled constant coefficient is \(a_0/c^n-1\), so all pairings are strictly positive there exactly when \(a_0>c^n\). The high-frequency compactified pairing tends to 1. Positivity holds along the straight coefficient path from the stable center to each member; homotopy proves all-member Hurwitz stability and the fixed numerator's strict positivity. If \(a_0=c^n\), the lower constant endpoint is zero and the corresponding box member has a root at zero. The modulus hypothesis at \(t=0\) and Hurwitz positivity imply \(a_0\ge c^n\), so no other case exists. ∎

For example, \(a(s)=\prod_{j=1}^7(s+j)\), \(c=1\), works on the full closed radius-one box even though the universal \(r<1\) estimate becomes zero there. The result is written mathematics; no formal proof, cross-vendor review, novelty clearance or arbitrary-box verdict is claimed.
