# The constant √2 in the adapted-quotient/BMO equivalence is SHARP, even in the canonical Brownian filtration

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:15:53 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE. Not reviewed, not adopted.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- Only symbolic parameters with explicit existence arguments. No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.

## 0. Statement

**Definitions.** For progressive scalar r ∈ E2 on [0, L]:

- nu is the adapted input quotient of v25/v26: nu(r) = sup_{w∈E2} E<r,w>/N1(w);
- ||r||_*^2 := sup_{s} esssup E[∫_s^L r^2 | F_s].

v27 Theorem A proved ||r||_* ≤ nu(r) ≤ √2·||r||_*. v29 Proposition O showed that the best universal upper constant c* lies in (1, √2].

**Theorem K (sharpness).** Work in the canonical one-Brownian filtration. For every η > 0 there are a finite L and a bounded progressive r on [0, L] such that

`nu(r) ≥ (√2 − η)·||r||_* > 0`.

Hence c* = √2 exactly. The lower constant 1 is also attained, for example by deterministic r (v27). So Theorem A's two constants are both optimal over the class of all progressive r.

**Scope.** This is a statement about the dual norm only. It does NOT decide whether the descriptor-level bound G1 ≤ √2·G2 (v27 Corollary C1) is attained by any plant. That question remains OPEN. No plant, controller or synthesis statement is made.

## 1. Inputs and separation

- **Definitions used.** nu as in the adopted v25/v26 (DUAL-NORM). ||·||_* as in v27 (`af2abd51…`).
- **Separation.** No storage, Riccati/LMI, controller, selected control, changed output, quarantined guidance or RMS source is used.
- **Ordinary tools.** Independent Gaussian increments; existence of a Gaussian quantile (by continuity); conditional expectation; geometric series; the elementary inequality 1 − e^{−x} ≥ x e^{−x} for x ≥ 0.

## 2. Construction: an almost-memoryless Brownian stopping time

Fix symbolic λ > 0 and ε ∈ (0, 1/λ). Put p := λε ∈ (0,1).

**The stopping time.**

- By continuity of the Gaussian law, choose κ with P(W_ε > κ) = p.
- For k ≥ 0 let ζ_k := 1{W_{(k+1)ε} − W_{kε} > κ}. These are i.i.d. Bernoulli(p), and ζ_k is F_{(k+1)ε}-measurable.
- Let k* := min{k : ζ_k = 1} and τ := (k*+1)ε. Then τ is a stopping time, and P(τ > t) = (1−p)^{⌊t/ε⌋}.
- Put λ_ε := −ln(1−p)/ε. Then λ_ε ≥ λ, (1−p)^{⌊t/ε⌋} ≥ e^{−λ_ε t}, and e^{−λ_ε ε} = 1 − p.

**The test covector.** For finite L, let r := 1_{[0, τ∧L]}. It is progressive, bounded and E2.

**Conditional energy bound.** Fix s and let k be the index with s ∈ [kε, (k+1)ε).

- On {τ ≤ s} the conditional future energy is 0.
- On {τ > s} the current trial may still succeed. After (k+1)ε, a failure leaves a geometric number of further trials, with mean ε/p = 1/λ. Hence

  E[(τ∧L − s)^+ | F_s] ≤ ((k+1)ε − s) + 1/λ ≤ ε + 1/λ.

- Therefore ||r||_*^2 ≤ ε + 1/λ.

## 3. A near-optimal adapted input

For β ∈ (0, λ_ε), let w := e^{βt}·1_{[0,τ∧L]}. It is bounded and progressive, hence an original E2 input.

**Numerator.**

`E<r,w> = ∫_0^L e^{βt} P(τ > t) dt ≥ ∫_0^L e^{−(λ_ε−β)t} dt = (1 − e^{−(λ_ε−β)L})/(λ_ε − β)`.

**Denominator.** Since ∫_0^{τ∧L} e^{2βt} dt ≤ e^{2βτ}/(2β),

`N1(w) ≤ E[e^{βτ}]/(2β)^{1/2} = p e^{βε}/[(1 − (1−p)e^{βε})(2β)^{1/2}]`.

The geometric series converges because (1−p)e^{βε} = e^{−(λ_ε−β)ε} < 1.

**Ratio.** Use 1 − e^{−x} ≥ x e^{−x} with x = (λ_ε − β)ε, then ε/p = 1/λ and e^{−λ_ε ε} = 1 − p:

`nu(r) ≥ E<r,w>/N1(w) ≥ (2β)^{1/2}(1 − e^{−(λ_ε−β)L}) e^{−λ_ε ε}/λ = (2β)^{1/2}(1 − e^{−(λ_ε−β)L})(1 − p)/λ`.

**Limits.** Let L → ∞ for fixed β < λ_ε, then let β ↑ λ_ε. The right side tends to

(2λ_ε)^{1/2}(1 − λε)/λ ≥ √2(1 − λε)/λ^{1/2}.

Every limit here is of explicit symbolic expressions. Combined with §2:

`nu(r)/||r||_* ≥ √2(1 − λε)/λ^{1/2} · (ε + 1/λ)^{−1/2} − o(1) = √2(1 − λε)/(1 + λε)^{1/2} − o(1)`.

Here o(1) → 0 as L → ∞ and β ↑ λ_ε. Choose ε small, then L large, then β close to λ_ε. This gives Theorem K. ∎

## 4. Why the earlier Proposition O example was far from √2

v29's two-chunk example gains only a first-order amount in its rarity parameter. The near-optimal structure is different:

- an almost constant conditional expected remaining activity (memorylessness), which keeps ||r||_* at its smallest possible value;
- an exponentially growing adapted input weight e^{βt} that "doubles down" while the activity survives. Its N1 cost is a concave square root that grows only like e^{βτ}/(2β)^{1/2}.

The Brownian filtration has no totally inaccessible times. It approximates memorylessness on a fine ε-grid of independent increment trials, and the loss is (1 − λε)/(1 + λε)^{1/2} → 1.

## 5. Boundaries and residual

- **Descriptor level.** Whether sup_φ nu(r_φ) for an actual plant can approach √2·sup_φ ||r_φ||_* is OPEN. Equivalently, it is open whether G1 can approach √2·G2 for some uncontrolled EMS plant. Theorem K shows the inequality chain is not loose at the single-covector level.
- **Not settled here.** Exact gains, controlled data and the original synthesis remain UNRESOLVED. C1–C3 STOPPED; R4 not used.

## 6. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- No pinned/frozen/shared edit; no Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v35.**
