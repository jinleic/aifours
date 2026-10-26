# Reserve source-control correction — parent check v1

Before-creation clock observed: **2026-10-23T13:27 PT**.

## Verdict

**CORRECTION VERIFIED (WRITTEN_CHECKED, in-harness level).** The literal plus-sign matrix displayed on p.3 of Eremenko's 3 October 2026 *Stabilizability by static output feedback* PDF is **not** a negative control for its stated repeated-pole test: for either real root of b²−b−1=0 and the explicit rank-2 L built from K=[[1,b],[1−b,−1]], the determinant is exactly z⁴. The sign-corrected τ=−1 matrix is a valid rational negative control with no real z⁴-fibre.

## Parent reconstruction (exact rational arithmetic)

- Identity `det(D−NK) = z⁴ + (b²−b−1)z²` verified as a polynomial identity in b (two generic rational values suffice; kernel-confirmed), hence exactly z⁴ at both golden-ratio-related roots.
- Complete fibre coefficient map for V_τ in the [K,I₂] chart — z⁴:1, z³:−(a+d), z²:ad−bc, z¹:τb+c−1, z⁰:a−τ — verified exactly at a generic rational point.
- Consequently the z⁴-fibre equation is τb²−b−τ²=0: discriminant 1+4τ³. τ=+1 gives discriminant 5 (two real solutions — the displayed matrix fails as a control); τ=−1 gives b²+b+1=0 with discriminant −3 (no real fibre — valid control).
- The six 2×2 minors and the Plücker non-degeneracy argument (coefficient form not decomposable for τ≠0) read and accepted; z² and 1−z³ coprime confirms no common factor.

## Boundary

- This corrects a literal displayed control in a living author's current preprint. It does **not** refute the underlying 1984 existence theorem, authenticate the original 1984 example, or settle generic (2,4) or (2,4,8) stabilizability.
- **No external author contact or publication is authorized or performed** — the correction is recorded for internal calibration only.
- The historical October 16 screening file's contrary claim remains read-only history; this correction supersedes it for all future reserve work.

Approved as the calibration boundary for the reserve selection-v2 freeze.
