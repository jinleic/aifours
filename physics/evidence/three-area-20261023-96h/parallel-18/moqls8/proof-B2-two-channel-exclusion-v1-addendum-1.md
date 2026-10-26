# B2 discrete-channel exclusion v1 — named residual and non-load-bearing boundary

Apply after immutable `proof-B2-two-channel-exclusion-v1.md`. The exact unclosed span13 cases are:

- **SHARED-B:** every B/complement cross image has the same complex B factor ray b, while its complement factors range over a real two-plane with two complex-independent generators.
- **SHARED-C:** every cross image has the same complex complement factor ray c, while its B factors range over a real two-plane with two complex-independent generators.

If both factors were fixed, this would be the already treated one-channel case. Neither SHARED-B nor SHARED-C is assumed finite, real-only, sign-valued or a union of two discrete physical channels. Their three-dimensional rank-one cones are still OPEN here.

Excluding BOTH named residuals, after the existing dimension0/1 and discrete-plane exclusions are separately validated, would exclude full B2 span13 and strengthen the OPTIONAL B2 bound from a>=13 to a>=14. It would not create a new problem slot or itself prove a GB Boolean input UNSAT.

**The frozen full conditional assembly does not need that strengthening.** Its B2 argument only requires a>=12 and its B3 argument only the axes' a>=12. Those were frozen separately at assembly SHA256 `6024ef4f8956c288661a362895681fa15ee86e5d2130dd4d6ad8f5b182a8c1cf`. This auxiliary branch work is non-load-bearing whether the shared-factor residual is resolved or remains open. A review must localize a defect rather than automatically invalidate or promote the earlier a>=12 route. Conversely a defect in a SHARED core saturation lemma actually reused there must be traced honestly through all dependencies.
