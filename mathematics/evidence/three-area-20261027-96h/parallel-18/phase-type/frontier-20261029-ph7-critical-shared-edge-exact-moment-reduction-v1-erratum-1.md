# Erratum 1: remove the spurious square in the shared-edge elimination

This additive correction is mandatory when reading `frontier-20261029-ph7-critical-shared-edge-exact-moment-reduction-v1.md` (SHA256 `e27b2028bc9dbf043fe44aa20fc17a5f3cf2661431584a3dc4a717bc27c25352`). The original graph assumptions, correct `E4/E3` equations and `Q=q*A0` identity are unchanged. The original displayed definition of `H` and the claim `H=-243*A0^2*V4` are **incorrect**: an extra term `-w_C*(w_C-B0)^2` was inserted even though the outside sum of the triangle is `x+T`, producing a term linear, not quadratic, in `x`.

The correct polynomial is

`H_correct=-243*[A0*(h0-w_C*T)+(w_C-B0)*(h1-w_C)]`.

Without division or an assumption on `A0`, using the original equations `(E4),(E3)` gives the exact identity

`H_correct=-243*A0*V4`.

Consequently a correct exclusion route would require an all-variable proof `Q>0`, forcing `A0>0` because `q>0`, and then `H_correct>0` on the actual parameter domain; the original paper's `H` sign discussion, floating stress-test and claimed `H` fraction degree are **not evidence for this corrected polynomial**. No such sign certificate or graph exclusion is asserted by this erratum.

The owner detected the error by substituting `B0=w_C-A0*x` and `h0=V4-x*h1+w_C*(x+T)` into the original formula: it yields `H_original=243*A0^2*(-V4+w_C*x^2)`, not the claimed identity. This is a source-level algebraic correction, not a retroactive scientific review, process reclassification, PH7/PH8 verdict, or parent adoption. The frozen original remains unchanged.
