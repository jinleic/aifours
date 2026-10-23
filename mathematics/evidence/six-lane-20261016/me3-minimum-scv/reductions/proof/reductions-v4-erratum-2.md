# Erratum 2 to `reductions/proof/reductions-v4.md` (editorial only)

Worker `MathPhaseType3`, the lane's integration owner, 2026-10-18 PDT. This is a static erratum, created as a new
file. It changes no file and involves no computation.

**Frozen and unchanged (sha256):**
* `reductions/proof/reductions-v4.md`: be1f7190ba71f06b3e951886581d285cc74435a49e3c2983776cebb6101f6eb1
* `reductions/proof/reductions-v4-erratum-1.md`: 4e5564ebf1b77e915afb395cec18f9232c14c230c85abaf7be96b64a9fc81085
* `reductions/STATUS-v4.md`
* the integration proof v5 and its errata 1–3
* every certificate and run
* pin v3 (`receipts/me3-candidate-pin-v3.json`, fa9327f2b35c31544128e612c55024caf97540d9fe05bdaf184861d8604d8b4b)

There is no re-pin, on the parent's instruction. The parent gate verdict
(`review/me3-minimum-scv-parent-gate-verdict-v1.md`, sha256 e4f88f9248146b35cf1aa12285e3e034f7ea9cd964630ea1c1038f962e3bc788)
is GATE MET, CORRECTNESS-ACCEPTED, NOVELTY-UNCLEAR.

**Source.** `institute/runs/six-lane-2026-10-16/review/me3-reductions-v4-delta-b-claude-v1.note.md`, sha256
693688451cdfd0de7b7767ff4177533bacc055224a1707a0a0b59196162130ba.
* Verdict: ACCEPT-WITH-FIXES, with 0 FATAL, 0 MAJOR and 4 MINOR findings, all editorial.
* Every statement and proof on the essential path is accepted as written.
* "S00:n" in the review means reductions-v4 LF n. The snapshot file `00-reductions-v4.md` is byte-identical to
  reductions-v4.

**Precedence.** Erratum 2 > erratum 1 > reductions-v4. The two errata amend disjoint passages. The review's note on
LF777–778 is already covered by erratum 1 (see N1). Each "Old" block below is quoted verbatim.

## MINOR-A. Define v_cos in this file — LF464–465, LF20–21 (with reading notes for LF469 and LF547)

**Old (verbatim, LF464–465):**

```
**Setting.** E = {−1, −1 ± iω} with ω > 0 (after the time change). V = span{e^{−t}, e^{−t} cos ωt, e^{−t} sin ωt}.
Put f_{ω,φ}(t) := e^{−t}(1 − cos(ωt − φ)).
```

**New (replaces LF464–465):**

```
**Setting.** E = {−1, −1 ± iω} with ω > 0 (after the time change). V = span{e^{−t}, e^{−t} cos ωt, e^{−t} sin ωt}.
Put f_{ω,φ}(t) := e^{−t}(1 − cos(ωt − φ)) and
  v_cos := inf_{ω>0, φ∈ℝ} SCV(f_{ω,φ}).
By Lemma 1.4 and the identity 1 − cos x = 2cos²(x/2 − π/2), v_cos does not depend on the decay rate or on the cos²
convention. It is attained (Theorem 5.6), so it equals the contract's "min".
```

Why the definition is convention-free (no new mathematics):
* **Rate.** e^{−λt}(1 − cos(ωt − φ)) = f_{ω/λ, φ}(λt). Lemma 1.4 says SCV is invariant under t ↦ λt, so every decay
  rate λ > 0 gives the same set of SCV values.
* **cos² convention.** cos²(ω′t − φ′) = (1 − cos(2ω′t − 2φ′ + π))/2. So e^{−t}cos²(ω′t − φ′) is a positive multiple
  of f_{2ω′, 2φ′ − π}, with the same SCV (Lemma 1.4). The map (ω′, φ′) ↦ (2ω′, 2φ′ − π) is onto (0, ∞) × ℝ.
  The convention control at LF601–607 records the same identity.

**Old (verbatim, LF20–21):**

```
* MINOR-3 (S00:160, aimed at the owner's proof): in this file "I_1 = v_cos" now always comes from Lemma 2.4 +
  Lemma 5.1, never "by definition" (Lemma 5.1, Cor 5.7 with a new proof, Cor 7.1(1)).
```

**New (replaces LF20–21):**

```
* MINOR-3 (S00:160, aimed at the owner's proof): in this file SCV ≥ v_cos for a general D1 law is proved, not taken
  as definitional: Lemma 2.4 + Lemma 5.1 give I_1 = inf_{ω>0, φ} SCV(f_{ω,φ}), and this infimum is v_cos by its
  definition in the §5 Setting (Lemma 5.1, Cor 5.7 with a new proof, Cor 7.1(1)).
```

**Reading notes.**
* **LF469.** The bracket "[v4 MINOR-3: Lemma 2.4 + this lemma, not "by definition"]" is read in the same sense. The
  step from a general D1 law to the cos family is Lemma 2.4 + Lemma 5.1. The final "= v_cos" is the Setting's
  definition.
* **LF547.** "Hence the definition "v_cos := min" in the contract is well posed" is read as: "Hence the infimum that
  defines v_cos (§5 Setting) is attained, so it equals the contract's min."

## MINOR-B. What Remark 5.6a gives without Lemma 4.2 — LF553–554

**Old (verbatim, LF553–554):**

```
**Remark 5.6a (alternative hand route; not needed) [v4 MINOR-2].** Theorem 5.6 also holds without Lemma 4.2, with the
window 1/5 < ω_m < 4 in place of 1/4 < ω_m < 4:
```

**New (replaces LF553–554; the bullets at LF555–560 and the paragraph at LF562–564 are unchanged):**

```
**Remark 5.6a (alternative hand route; not needed) [v4 MINOR-2].** Attainment, v_cos ≤ 773/3844 and the tails hold
without Lemma 4.2, with 1/5 in place of 1/4 in both the window and the tail (there SCV > 21/104 > 0.2014), and with
773/3844 < 1/4 < Δ3:
```

What does not hold without Lemma 4.2: Theorem 5.6's clauses "773/3844 < 553/2000 < Δ3" and "ω ≤ 1/4 ⇒ SCV > 0.2014".
LF562–564 already note that on the interval (1/5, 1/4] the hand bound is only 3/17. The exact comparisons used by the
new wording:
* 21/104 > 1007/5000, because 21·5000 = 105000 > 104728 = 1007·104;
* 773/3844 < 1/4, because 4·773 = 3092 < 3844;
* Δ3 > 1/4 by L4(2).

## MINOR-C. The resultant remark needs the distinctness of the three values — LF424–425

**Old (verbatim, LF424–425):**

```
   Equivalently, since q is monic, Res_x(q(x), 24y − x(9 − x)² + 24) = ∏_i 24(y − s(x_i)) = 432·h(y) (leading term
   (24y)³ = 13824y³ = 432·32y³), so h/32 = ∏_i (y − s(x_i)) is the monic normalization of that resultant.
```

**New (replaces LF424–425):**

```
   Consequently, since (3) gives s(x1) < 1/3 < 1/2 < s(x3) < s(x2), the three roots s(x_i) of the cubic h are
   pairwise distinct, so h = 32·∏_i (y − s(x_i)). Since q is monic and x_i(9 − x_i)² − 24 = 24·s(x_i) at each root
   x_i (the closed form in (3)), Res_x(q(x), 24y − x(9 − x)² + 24) = ∏_i 24(y − s(x_i)) = 432·h(y) (leading term
   (24y)³ = 13824y³ = 432·32y³), so h/32 = ∏_i (y − s(x_i)) is the monic normalization of that resultant.
```

The chain s(x1) < 1/3 < 1/2 < s(x3) < s(x2) uses only proof part (3):
* s(x1) < s(0) = 1/3;
* s(x3) > 1/2;
* s(x3) < s(x2), because s is strictly decreasing on [x2, x3], where q < 0.

No proof uses this remark. The equation h(Δ3) = 0 rests on the remainder identity at LF422–423.

## MINOR-D. Notation: m* → v* and m_K → v_K — LF534–538 and LF770–774

The fix map promises that m_k denotes only moments, so the two symbols for minimum values are renamed. Every
occurrence is listed; no other change.

**Old (verbatim, LF534–535 and LF538):**

```
* Attainment: SCV is continuous on (0, ∞) × ℝ (5.2, m1 > 0) and 2π-periodic in φ. So its minimum m* over the
  compact set [1/4, 4] × [0, 2π] is attained, and m* ≤ SCV(1, φ_e) = 773/3844.
* Hence m* = v_cos, it is attained, and every minimizer (ω_m, φ_m) has 1/4 < ω_m < 4. ∎
```

**New:** the same three lines with every "m*" replaced by "v*":
* "So its minimum v* over the compact set [1/4, 4] × [0, 2π] is attained, and v* ≤ SCV(1, φ_e) = 773/3844."
* "Hence v* = v_cos, it is attained, …"

**Old (verbatim, LF770 and LF773–774):**

```
* By Lemma 2.4(1) and (3), m_K := min_{K∖0} SCV exists and is attained on an extreme ray of the same cone K.
* SCV is constant on rays (Lemma 1.4). So m_K = S_2(r, ω, φ0) for some φ0 ∈ [0, θ1(r)], and m_K > v_cos by hypothesis.
* Hence SCV(f) ≥ m_K > v_cos for every f ∈ K∖0. ∎
```

**New:** the same three lines with every "m_K" replaced by "v_K". Reductions-v4 erratum 1 writes this minimum as
"min_{K∖0} SCV", with no symbol, so nothing there needs renaming.

## Notes (the review: "no action required"; recorded here)

* **N1 — LF777–778**, the "If the theorem holds …" premise in Remark 7.2a. This is already replaced by reductions-v4
  erratum 1 E1 (sha 4e5564eb…1085), which governs.
  * Erratum 1's text, "Once Lemmas D/M and Corollary 7.2 establish strictness on every D2 cone, Corollary 7.1(2)
    implies that I_2 = v_cos is an unattained infimum", and its note that each cone has a positive gap but there is no
    uniform gap, cover both points of this review's note: I_2 = v_cos alone does not decide attainment, and there is no
    uniform gap.
  * No further change.
* **N2 — LF339–340**, integrability in Lemma 3.4(5).

  **Old (verbatim):**

  ```
     (t ↦ t/μ_u), SCV(g_u) = SCV((t − μ_uτ)² e^{−t}) ≥ Δ3. The integrability in 2.3 holds because the integrand is
     continuous in u on the compact Σ. ∎
  ```

  **New** (replaces the sentence "The integrability in 2.3 holds because the integrand is continuous in u on the
  compact Σ."): "The integrability hypothesis of Lemma 2.3 holds by the uniform majorant of Remark 2.3a(2):
  (1 + t²)g_u(t) ≤ (1 + t²)(t − τ)²e^{μ_max|τ|}e^{−μ_min t} for every u ∈ Σ, so ∫_Σ ∫_0^∞ (1 + t²)g_u dt du < ∞."

  Continuity in u alone does not bound the t-integral uniformly in u.
* **N3 — the parent hunk table (the review's SOURCE02:38 and 51–53).** It lists Lemma 5.1 as unchanged since v1,
  although its statement changed at LF467–469. That table is not a lane file, and this erratum makes no change for it.

## Information only (the review's "not verified here" items that point outside this file)

* The owner-side loci of the old MINOR-3 and MINOR-5 are in the integration proof:
  * `proof/me3-theorem-v5.md` LF102–108 and LF243–244;
  * `proof/me3-theorem-v5-erratum-2.md` m8;
  * `proof/me3-theorem-v5-erratum-3.md` F3.
* Lemma M compares only against exact constants. In erratum 1 E6 of the theorem file, step 1 uses
  T > 773/3844 ≥ v_cos, and step 7 uses the definition of v_cos at r = 0. It never uses U or Theorem 5.8.
