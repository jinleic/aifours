# The gate-I anchor family under preview: exact unconditional long-preview mean-square value, a monotone profile, and strictness at every preview

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:42:36 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written, UNREVIEWED and not adopted. Main's v240 decision applies: no review wave before cutoff.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe: a, c, d and σ stay symbolic.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. The gate-I numerical identification stays CONDITIONAL at NR-GATE-I-WHOLE-V21, exactly as in the v220 parent (`13fbb1a2…`). Q-rho, Q-zero and Q1 are carried additively (`6d0103ff…`).

## 0. Setting and statements

**Gate-I family (v32 S1 form), with preview h ≥ 0.**

- dX = (−aX + c w(t−h)) dt + σX dW and z = dX;
- a, c, d, σ > 0, with q_0 := 2a − σ^2 > 0, i.e. EMS;
- the plant receives the adversary's progressive E2 input delayed by h, which is the v31/v32 preview convention;
- canonical one-Brownian filtration.

Write G1(h) and G2(h) for the literal and RMS gains, and G2^det for the deterministic-input mean-square gain (v50).

**Theorem GP.** For every plant of the family:

1. **(Exact, unconditional.)** G2^det = c d (2/(a q_0))^{1/2}.
2. **(Monotone profile.)** G1(h) and G2(h) are non-increasing in h (v50 PM), with G2(h) ≥ c d (2/(a q_0))^{1/2} for every h ≥ 0.
3. **(Exact long-preview limit, unconditional.)** lim_{h→∞} G2(h) = c d (2/(a q_0))^{1/2}, exponentially fast (v50 LD).
4. **(Strictness at every preview.)** G2(h) < G1(h) ≤ √2·G2(h) for every h ≥ 0.
   - h = 0 is parent-supported directly (v220: gate-I AHEAD).
   - For all h it is the author candidate v33 Corollary S3. Equivalently, G_rob = ∞ because c·d·σ ≠ 0, then v34 Theorem R.
5. **(Conditional comparison.)** Under the gate-I identification G2(0) = γ* = 2cd/q_0, which is conditional at NR-GATE-I-WHOLE-V21,

   `lim_{h→∞} G2(h)^2 / G2(0)^2 = q_0/(2a) = 1 − σ^2/(2a) < 1`.

   So, conditionally, the mean-square level falls by the factor (1 − σ^2/(2a))^{1/2} from zero to infinite preview. Item 1 alone gives the unconditional lower bound G2(0) ≥ c d (2/(a q_0))^{1/2}.

**NOT delivered.**

- G2(h) for 0 < h < ∞.
- Any exact G1(h).
- Any unconditional value of G2(0).
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

The latter contains the adopted v32 S1 and the named cut NR-GATE-I-WHOLE-V21.

**Parent-supported conclusions.** v31 and v32 S at any preview h; v32 S1 (gate-I AHEAD) at h = 0; v27 C1.

**Author candidates** (UNREVIEWED):

| Packet | Pin | Used for |
|---|---|---|
| v33 | `3083dc88…` | S3 |
| v34 | `6fcca986…` | Theorem R |
| v50 | `173796d0…` | PM, LD |

**Separation.** The tools are the explicit scalar stochastic flow, independence of Brownian increments, Fubini and the Fourier transform of e^{−a|u|}. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source. The gate-I value γ* is used ONLY in item 5 and is labelled conditional.

## 2. Proofs

**Item 1.**

- **Flow.** The flow is Φ(t,s) = exp(−(a + σ^2/2)(t−s) + σ(W_t − W_s)).
- **Moments.** E Φ(t,s)^2 = e^{−q_0(t−s)} and E Φ(s,s') = e^{−a(s−s')}. For s' < s ≤ t, Φ(t,s') = Φ(t,s)Φ(s,s') with independent factors, so E[Φ(t,s)Φ(t,s')] = e^{−q_0(t−s)} e^{−a(s−s')}.
- **Energy.** For a deterministic plant input v, Fubini gives

  E∫_0^∞ z^2 = d^2 c^2 · 2 ∫∫_{s'<s} v(s) v(s') e^{−a(s−s')} (∫_s^∞ e^{−q_0(t−s)} dt) ds' ds = (d^2 c^2/q_0) ∫∫ v(s) v(s') e^{−a|s−s'|} ds ds'.

- **Supremum.** The kernel e^{−a|u|} has Fourier transform 2a/(a^2 + ω^2), with maximum 2/a at ω = 0, approached by long constant inputs. Hence G2^det^2 = 2c^2 d^2/(a q_0).
- **Delay.** The delay h is an isometric shift for deterministic inputs.

**Item 2.** This is v50 Theorem PM. The lower bound holds because deterministic inputs are admissible at every h.

**Item 3.** This is v50 Theorem LD with item 1.

**Item 4.**

- c·d·σ ≠ 0 gives G_rob = ∞ (v33 S3 / v34 §4); this is h-independent.
- G2(h) ≤ G2(0) < ∞ (v31), so G_rob > G2(h), and v34 Theorem R gives strictness at each h.
- The bound √2 is v27 C1, which is parent-supported.

**Item 5.** (2c^2d^2/(a q_0)) / (4c^2d^2/q_0^2) = q_0/(2a) = 1 − σ^2/(2a). ∎

## 3. Meaning for the original preview problem (value side only)

**The adopted anchor under preview.**

- The printed literal level stays strictly above the mean-square level at EVERY preview.
- The mean-square level decreases with preview to the explicit unconditional limit c d (2/(a q_0))^{1/2}.
- Conditionally on the gate-I import, the total mean-square improvement from preview is exactly the factor (1 − σ^2/(2a))^{1/2}.

**Synthesis.** No controller, internal-EMS or synthesis statement is made. The original synthesis problem remains UNRESOLVED.

## 4. Process and assurance

- Written exact mathematics only, after v209, v236 and v240 were read and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v54.**
