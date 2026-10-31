# Additive v4 correction and new symbolic identity verification

Author correction, actual observed clock Wed Oct28 17:41:48 PDT2026. The unchanged source `frontier-20261028-ph7-two-cycle-endpoint-v4.md` SHA256 `4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191` §6 incorrectly says that the earlier v2 script checked the seven normalizer equations with **general** six rates. It used six fixed rational rates, so that code alone did NOT check general rates or the new algebraic rates. Read this correction BEFORE §6/§7. No alteration of the earlier script or the v4 manuscript was made.

A **new and separate exact symbolic check** now supplies the relevant v4-specific general-rate step. `frontier-20261028-ph7-two-cycle-general-identities-check.py`, **53LF/2801B**, SHA256 `188f3a58db10b5ce4c3c45cf654b497827aef1e4df8400a6a1c8e2d74f5c67b2`, was run and returned

    SymPy 1.14.0 symbolic U,V,z,c full matrix/adjugate/all-normalizer PASS

Its exact small certificate `frontier-20261028-ph7-two-cycle-general-identities-certificate.json`, **11LF/434B**, SHA256 `b6e4c4984da9ea5ad8e78d4ce60cb80adf2fa1884e0db5f31eb4e219a92c4fe9`. It uses SymPy rational identities and no floating values. Scope is symbolic U,V,z,c, not sampled rates, for the restricted `(U,U,U;U,V,V)` family, whenever the explicit denominators are nonzero.

The check verifies the full actual 7-by7 determinant for free `U,V,w,phi,D1,D2,D3`, verifies the full adjugate numerator for free B,C, and then proves after the v4 symbolic family substitutions that `det(yI-G)=D_z(y)Q(y)`. The literal six noncentral normalizer rows and `beta h=1` are checked symbolically for free parameters. For the central row it checks the exact stronger free-parameter identity

    ((c+w)h4-h5) Q(c) (c+U)(c+V)^2
      = det(cI-G)-K Q(c).

The just-verified family determinant gives the seventh row zero for `K=D_z(c)` whenever its displayed factors are nonzero. The v4 interval checker establishes all needed positivity, including at its algebraic endpoint. Thus the full actual matrix and normalization step is now supported for the restricted symbolic family. The word `general` here does NOT mean arbitrary six-rate identities were checked; the v4 sign/contraction checker has unchanged scope.

Process correction: the first version of this NEW independent identity script exceeded its 120-second deadline before returning output; its symbolic expressions were simplified to check the free-parameter row implication and complete cleared polynomial rather than repeat huge substituted rational expressions seven times. The successful invocation above was the revised script, 2.29 seconds. This neither establishes an independent review nor validates an 8/9 witness, old PH6, novelty, or all-topology optimum.

END — v4 identity-source overstatement corrected; new restricted-family full-matrix identity checked exactly.
