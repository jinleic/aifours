# Addendum: the noncompact septic family can be convex

**Status: WRITTEN candidate, not parent adoption.** Using the same exactly checked \(E_A,E_B,O\) in `frontier-20261029-septic-parity-compactness-necessity-v1.md`, take the **closed convex** parameter set \(u,v\ge0\), \(u+v\ge1\), and define
\[
a_{u,v}(i\sqrt t)=uE_A(t)+vE_B(t)+i\sqrt t\,O(t).
\]
This is a noncompact convex family of monic degree-seven polynomials with the same odd part. At the three positive zeros \(1,4,9\) of \(O\), both \(E_A,E_B\) have signs \(-,+,-\), respectively. Their positive combination therefore cannot vanish at any of those roots; it is also positive at zero. Thus **no** member has an imaginary-axis root. The positive-parameter set is connected and contains the previously checked Hurwitz reference \(a_{1,0}\); monic homotopy proves every member Hurwitz.

The family contains both rays \(a_{N,0},a_{0,N}\) for \(N\ge1\). The same opposing even signs on \((1/2,3/4)\) force any putative common numerator's even part to vanish identically, contradicting its positive constant. Hence this noncompact family has **no** common numerator even under convexity, monicity, stability and a fixed odd part. For each bounded intersection with \(u+v\le M\), \(M\ge1\), the pinned compact fixed-parity theorem supplies one.

This is not a finite-width independent-coefficient box and gives no original counterexample. The reference replay and its SHA-256 pins are supplied in the predecessor; convexity, axis exclusion, homotopy and the contradiction above are written mathematics, not formal or independent-family review.
