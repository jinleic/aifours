# An independent storage-free proof of the gate-I mean-square value G2 = 2cd/q_0, without the v21 import

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:44:20 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written, UNREVIEWED and not adopted. Main's v240 decision applies: no review wave before cutoff.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proof. No machine-checked identity.
- No chosen numeric probe: a, c, d and σ stay symbolic.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched.

**Scope of the parent cut.** The v220 parent (`13fbb1a2…`) keeps every gate-I value identification CONDITIONAL at NR-GATE-I-WHOLE-V21, because the 284-LF v21 proof was not supplied. This packet does NOT change that adopted status. It offers an independent, self-contained written proof of the identification for review. Only the parent can decide whether it discharges the cut.

## 0. Statement

**Gate-I family (v32 S1 form).**

- dX = (−aX + c w(t−h)) dt + σX dW and z = dX;
- a, c, d, σ > 0 with q_0 := 2a − σ^2 > 0;
- preview h ≥ 0;
- canonical one-Brownian filtration;
- adversary inputs are progressive and E2.

**Theorem G.**

1. **(Upper bound, every h ≥ 0.)** G2(h) ≤ 2cd/q_0.
2. **(Exact value at h = 0.)** G2(0) = 2cd/q_0 = γ*, the value the v220 parent records conditionally.
3. **(Exact energy identity, every h.)** For every adapted plant input w̃,

   `E∫_0^∞ X_t^2 dt = (2c/q_0) E∫_0^∞ w̃(s) X_s ds`.

**Corollary G1.** With v54 (`2b9bbee2…`, UNREVIEWED), the long-preview ratio lim_{h→∞} G2(h)^2/G2(0)^2 = 1 − σ^2/(2a) holds unconditionally, subject only to the review status of v54 and v55. Also

`G2(h) ∈ [cd (2/(a q_0))^{1/2}, 2cd/q_0]`

for every h, with equality on the right at h = 0 and the left value as the limit.

**NOT delivered.**

- G2(h) for 0 < h < ∞.
- Exact G1 (the gate-I literal gain stays in (G2, √2 G2], with strictness parent-supported at h = 0).
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

The latter defines the family and records γ* = 2cd/q_0 as conditional.

**Parent-supported conclusion used.** v31: G2 < ∞, at any preview.

**Author candidate.** v54 `2b9bbee2…` (UNREVIEWED), for Corollary G1 only.

**Separation.** The proof uses:

- the explicit scalar flow;
- independence of Brownian increments;
- Fubini and Minkowski's integral inequality;
- an explicit ADVERSARY input-feedback strategy w = λX for the lower bound. This is a disturbance strategy, not a control.

No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or the v21 proof/RMS source is used.

## 2. Proof

**Flow and moments.** Φ(t,s) = exp(−(a + σ^2/2)(t−s) + σ(W_t − W_s)), so E Φ(t,s)^2 = e^{−q_0(t−s)}. Φ(t,s) is independent of F_s, and Φ(t,s') = Φ(t,s)Φ(s,s') for s' ≤ s ≤ t. For an adapted plant input w̃, X_t = c ∫_0^t Φ(t,s) w̃(s) ds.

**Item 1 (Minkowski).**

- (E∫|X|^2)^{1/2} ≤ c ∫_0^∞ (E∫ Φ(s+u,s)^2 w̃(s)^2 ds)^{1/2} du.
- By independence this equals c ∫_0^∞ e^{−q_0u/2} du ||w̃|| = (2c/q_0)||w̃||.
- Multiply by d.

**Item 3 (identity).**

- **Fubini.** This is justified by item 1, since all integrands are dominated by the same Minkowski bound. Symmetrizing,

  E∫X^2 = 2c^2 E∫∫_{s'<s} w̃(s) w̃(s') ∫_s^∞ Φ(t,s)Φ(t,s') dt ds' ds.

- **Conditioning.** Condition on F_s. Then w̃(s), w̃(s') and Φ(s,s') are F_s-measurable, and E[∫_s^∞ Φ(t,s)^2 dt | F_s] = 1/q_0. Hence

  E∫X^2 = (2c^2/q_0) E∫∫_{s'<s} w̃(s) w̃(s') Φ(s,s') ds' ds = (2c/q_0) E∫ w̃(s) X_s ds.

**Item 2 (lower bound at h = 0).** Fix ε > 0 and λ ∈ (0, q_0/(2c)), and use the adapted input w := 1_{[0,ε]} + λX 1_{(ε,∞)}, where the plant input equals w at h = 0.

1. **Finite energy.** The truncation w_T := 1_{[0,ε]} + λX 1_{(ε,T]} has finite energy. Item 3 gives

   E∫_0^T X^2 ≤ (2c/q_0)(P + λ E∫_ε^T X^2), where P := E∫_0^ε X_s ds.

   So (1 − 2cλ/q_0) E∫_ε^T X^2 ≤ (2c/q_0) P uniformly in T, and w ∈ E2.
2. **Blow-up.** Put Q := E∫_0^∞ X^2 and Q_ε := E∫_0^ε X^2. Item 3 gives Q(1 − 2cλ/q_0) = (2c/q_0)(P − λQ_ε).
   - E X_s = c ∫_0^s e^{−a(s−s')} ds' ≥ c s e^{−aε} on [0, ε], so P ≥ c ε^2 e^{−aε}/2.
   - Cauchy–Schwarz and E Φ^2 ≤ e^{σ^2 ε} on [0, ε] give Q_ε ≤ c^2 e^{σ^2ε} ε^3/3.
   - Fix ε so small that P − (q_0/(2c)) Q_ε > 0. Then P − λQ_ε > 0 for all admissible λ, and Q → ∞ as λ ↑ q_0/(2c).
3. **Ratio.** E∫z^2/E∫w^2 = d^2 Q/(ε + λ^2(Q − Q_ε)) → d^2/λ^2 → d^2 (2c/q_0)^2. Hence G2(0) ≥ 2cd/q_0.

Together with item 1, G2(0) = 2cd/q_0. ∎

**Corollary G1.** v54 item 1 gives G2^det = cd(2/(a q_0))^{1/2} and v54 items 2–3 give the monotone limit. The ratio is (2c^2d^2/(a q_0))/(4c^2d^2/q_0^2) = q_0/(2a). ∎

## 3. Meaning (value side only)

**Gate-I value.** The gate-I mean-square value γ* = 2cd/q_0 follows from a few lines of explicit moment calculus:

- the upper bound from Minkowski with E Φ^2 = e^{−q_0 u};
- the lower bound from the critical adversary feedback w = λX, with λ ↑ q_0/(2c), via the exact energy identity.

If accepted by review, this would make the gate-I identification, and with v54 the whole gate-I preview profile endpoints, independent of the unsupplied v21 proof.

**Synthesis.** No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209, v236 and v240 were read and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v55.**
