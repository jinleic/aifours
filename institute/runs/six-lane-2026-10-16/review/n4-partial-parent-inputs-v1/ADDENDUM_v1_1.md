# Addendum v1.1 to PROOF.md (v1 preserved unchanged)

Codex `gpt-6.1-sol` (max effort, read-only, cross-vendor relative to the Claude-family parent) reviewed the frozen
v1 package 2026-10-17 04:11:14Z–04:17:53Z UTC, exit 0: **ACCEPT-WITH-FIXES**. Every mathematical check passed: R1, R2,
reflection, relaxation validity, G-invariance, commutant, closed forms, the dual LP, and all ten stored certificates
recomputed independently. Output: `../review/codex-frozen-partial-output.md`. Its three low-severity fixes:

1. **`exact_U3.log` is incomplete.** SymPy's simplex aborted at k = 12 (`InfeasibleLPError`, a solver oscillation).
   The theorem does not use this run. `U_3(k)` for k ≥ 5 is the trace bound `K_k(X_3) ≤ Tr X_3 = 8 = K_k(T_3)`, and
   for k = 1 it is `λ_max(X_3) ≤ 4`. The run serves only as exploration showing the LP is loose at k = 2, 3, 4.
2. **`twirl_ppt_lp.py` is only partly independent.** It builds J and E_S as explicit 256×256 matrices, but its PPT
   rows and marginal coefficients use the same closed formulas as `twirl_lp_exact.py`. Its agreement therefore
   checks only the objective coefficients independently. Codex independently re-derived the PPT rows.
3. **Read-only certificate verification.** `verify_frozen_certs.py` loads the frozen `u2_dual_certificates.json`.
   It checks dimensions, multiplier signs and every dual inequality exactly with Fractions, and recomputes
   `K_k(T_2)` from the spectrum. It writes nothing. Result (`verify_frozen_certs.log`): ALL_VERIFIED. The mutation
   control (target − 1/1000) fails at every k.

Clarifications:
- In R2, `b_1 = a_1 − a_3 = p(1−p)(2−p)(3p−2)/8`; it is ≥ 0 on [2/3, 1], and p = 0 is a further zero.
- **Elementary baseline vs. increment.** k = 1 is King's multiplicativity. k = 11..15 need no LP certificate: trace
  bounds, `U_1`, R1 and reflection suffice. **The substantive content is k = 5 for all p ∈ [0, 4/3], together with
  k = 2, 3, 4 for p ∈ [2/3, 4/3]** (`U_2(2..5)` certificates plus R2).
- **Obstruction for this relaxation** (`lp1_primal_witnesses.json`). Exact rational primal points satisfy every LP
  constraint and reach objective `K_k(T_2) + 1` for `U_2` at k = 6..10 and `K_k(T_3) + 2, 2, 1` for `U_3` at
  k = 2, 3, 4. Twirling loses nothing (§3(c)), so the full untwirled PPT relaxation has the same values. Any
  certificate for those indices therefore needs information beyond PPT.
