# Certified enclosure of v_cos (control (f)) — addendum to reductions-v1.md (v1)

Worker `MathPhaseType3.ME3Reductions`, 2026-10-18 (host clock in `../STATUS.md`). Correctness only. This file adds
Theorem 5.8 to §5 of `reductions-v1.md`; every lemma number refers to that file.

**Theorem 5.8.** 0.20090156350055 ≤ v_cos < U = 0.2009015635005569588013806824561593216569.
So v_cos = 0.2009015635005(5…6)…, with U − L < 7·10⁻¹⁵. The interval lies inside the contract band
[0.20090144, 0.20090185].

## Proof

Put L := 0.20090156350055 (an exact decimal).

**(i) Reduction to two variables.** For ω > 0 and φ ∈ ℝ, put u := 1 − cos(φ − 2 arctan ω) ∈ [0, 2] and
S := sin(φ − 2 arctan ω). Lemma 5.3 gives
SCV(ω, φ) = 2(X² + aX + aωS − Y_m²)/((1 + ω²)X²) − 1, with X = ω² + u, a = ω²(1 + ω²) and
Y_m = ω√(u(2 − u)) = ω|S|. Since aωS ≥ −aY_m:
  SCV(ω, φ) ≥ F(ω, u) := 2(X² + aX − aY_m − Y_m²)/((1 + ω²)X²) − 1.
Hence v_cos ≥ inf{F(w, u) : w > 0, 0 ≤ u ≤ 2}. Equality holds, using the phase with S ≤ 0, but it is not needed.

**(ii) Tail w ≤ 1/4 (written lemma).** Steps 2–5 of the proof of Lemma 5.4 bound F(w, u) + 1 itself from below by
(1 + Δ3)/(1 + w²). With Δ3 > 2765/10000 (Sturm certificate, re-done inside the run), for w ≤ 1/4:
F ≥ (2765/10000 − 1/16)/(17/16) = 0.20141176… > L.

**(iii) Tail w ≥ 4 (written lemma).** Choose φ with sin(φ − 2 arctan w) = −√(u(2 − u)) and cos(φ − 2 arctan w) = 1 − u.
Then F(w, u) = SCV(w, φ). Lemma 5.5 holds with ρ̄ = 2425356251/10¹⁰ ≥ (1 + w²)^{−1/2}; the check ρ̄² ≥ 1/17 is exact.
It gives F ≥ 2(1 − ρ̄)(1 − ρ̄³)/(1 + ρ̄²)² − 1 = 0.33200060929… > L.

**(iv) Middle [1/4, 4] × [0, 2] (certified computation).**
* Method: branch-and-bound over dyadic boxes, in python-flint 0.9.0 arb ball arithmetic at 128 bits (outward
  rounding). Box endpoints are dyadic, hence exact. Each box is bisected across its longer side.
* A box B = [w_l, w_h] × [u_l, u_h] is certified F > L on B by either of two tests:
  * (a) The natural ball extension of F on B has lower endpoint > L.
  * (b) Mean-value form, used only when 0 < u_l and u_h < 2. There F is C¹ on the convex set B, and for every
    p ∈ B, F(p) ≥ F(c) − sup_B|∂_wF|·h_w − sup_B|∂_uF|·h_u. Here c is the box center and h are the half-widths. F(c)
    is evaluated as a ball at the exact center, and the sup bounds come from ball evaluation of the gradient on B.
* A box is never discarded otherwise: it is either certified or bisected. If a center ever has a certified
  F(c) < L, the claimed bound is refuted and the run stops. The run ends only when the stack of uncertified boxes is
  empty.
* Code: functions `F_ball`, `grad_ball` of `reductions/code/ctl_f_d1bnb_v1.py` (sha256
  `508b148870fc18e3cb32de6ada1c5245aca4271db92867b959597b4ba29341b7`).
* **Exact verification of that code** (run `ctl-f-gradsym-v1`): the two functions were extracted verbatim (AST) and
  run on sympy symbols. `grad_ball` equals (∂_wF, ∂_uF) of `F_ball` identically, and `F_ball` + 1 equals m0m2/m1² of
  Lemma 5.3 with C = 1 − u and S = −√(u(2 − u)) identically (simplify residuals 0). 60-digit spot residuals are below
  10⁻¹⁹⁰.
* Result (run `ctl-f-main-v1`, argv `0.20090156350055 1/4 4 certify 3000000`):
  * 38439 boxes processed; 115 leaves certified by (a) and 19105 by (b); the rest were bisected;
  * max depth 55; no refutation, no abort, empty final stack; wall time about 1 s.
  * The smallest center value, F = 0.2009015635005569722… at (w, u) = (1112324551/2³⁰, 94330227/2²⁷), is EXPLORATORY
    information only.

(i)–(iv) give v_cos ≥ L. The upper bound v_cos < U is Theorem 5.6 (run `ctl-c-v2`). ∎

## Mutation controls (each rejected for the intended reason)

* `ctl-f-mut-L-above-v1` (argv `0.200901563500557 1/4 4 reject 3000000`). The claimed L' = 0.200901563500557 exceeds
  v_cos. The B&B refutes it at the certified center (1112324551/2³⁰, 94330227/2²⁷), where
  F = 0.2009015635005569722025419 ± 7.5·10⁻²⁷ < L'. Outcome reject, as expected.
* `ctl-f-mut-tail-v1` (argv `0.2009 1/2 4 reject 3000000`). With the middle box starting at w_lo = 1/2, the Lemma 5.4
  tail bound at w = 1/2 is 0.0212 < 0.2009, so the tail certificate fails. Outcome reject, as expected, even though the
  B&B part on [1/2, 4] succeeds.

## Scope

Theorem 5.8 encloses the *value* v_cos. It does not by itself certify that the Newton stationary point of
`ctl-c-v2` is the unique global minimizer. Its value, 0.200901563500556958801380679…, lies in [L, U). No D2 statement
is made here.
