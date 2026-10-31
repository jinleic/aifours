# The unbounded solution ray rules out a larger dual cone

**Status: WRITTEN corollary, not parent adoption.** For any box in the parametric family of `frontier-20261029-unbounded-monic-solution-ray-v1.md` (SHA-256 `43ad9b13e6f28e32ba29e3c9f07baa1f11f8e3225bccc426604884d0e2c4f4ce`), no finite positive-weight actual atom collection containing at least one **finite-frequency** atom can have aggregate numerator coefficients
\[
C_0,\ldots,C_6\le0,
\]
even if \(C_7\) is completely unrestricted and even if infinity atoms are included. This also holds in each open neighborhood where the same ray persists.

Indeed the pinned degree-six direction \(c_R\) has \(c_0,\ldots,c_6>0\), \(c_7=0\), and strictly positive pairing with every actual denominator at every finite frequency, including zero. Every finite atom contributes positively to \(C\cdot c_R\), while an infinity atom contributes 0. Hence \(C\cdot c_R>0\). But if \(C_0,\ldots,C_6\le0\), the same sum is nonpositive, contradiction. If all atoms are at infinity there is no contradiction: they have \(C_0=\cdots=C_6=0\) and \(C_7>0\).

In particular a positive atom functional with one negative nonleading coordinate, all other nonleading coordinates nonpositive, and arbitrary leading coordinate cannot prove an upper bound on that monic numerator coefficient. This is consistent with the explicit \(b_R+\tau c_R\) ray, along which **every** nonleading coefficient tends to infinity. The conclusion is stronger than merely observing that these boxes have some common numerator, but it is specific to this solvable family and does not preclude a strict negative-coordinate certificate for another box.

The finite-direction positivity and actual-box stability are supplied by the pinned exact symbolic replay; the dual sign contradiction is written mathematics. No formal proof, cross-vendor review, novelty clearance or original arbitrary-box verdict is claimed.
