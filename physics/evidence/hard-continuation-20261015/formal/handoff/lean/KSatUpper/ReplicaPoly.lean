import KSatUpper.ReplicaMoments
import KSatUpper.Local

/-! The nonnegative degree-`(m+1)` combination of the actual averaged replica moments.

Derived from `SatUpper/ReplicaCubic.lean` (yamelton/sat-upper-4268, Apache-2.0),
where the arity was three. Position zero carries the feature `b`; the remaining
`m` positions carry `c`. -/

open MeasureTheory
open KSatUpper.ReplicaMoments

namespace KSatUpper.ReplicaPoly

variable {Ω Ξ : Type*} [MeasurableSpace Ω] [MeasurableSpace Ξ]

def mixedFamily {m : ℕ} (b c : Ξ → Ω → ℝ) : Fin (m + 1) → Ξ → Ω → ℝ :=
  Fin.cases b (fun _ => c)

omit [MeasurableSpace Ω] [MeasurableSpace Ξ] in
theorem mixedFamily_cases {m : ℕ} {b c : Ξ → Ω → ℝ} {P : (Ξ → Ω → ℝ) → Prop}
    (hb : P b) (hc : P c) (j : Fin (m + 1)) : P (mixedFamily b c j) := by
  cases j using Fin.cases with
  | zero => exact hb
  | succ j => exact hc

omit [MeasurableSpace Ω] [MeasurableSpace Ξ] in
theorem prod_mixedFamily {m : ℕ} (b c : Ξ → Ω → ℝ) (g : (Ξ → Ω → ℝ) → Fin (m + 1) → ℝ) :
    (∏ j, g (mixedFamily b c j) j) = g b 0 * ∏ j : Fin m, g c j.succ := by
  rw [Fin.prod_univ_succ]
  rfl

theorem power_moment (ν : Measure Ξ) (μ : Measure Ω)
    [IsProbabilityMeasure ν] [IsProbabilityMeasure μ] (m r : ℕ)
    {b : Ξ → Ω → ℝ} (hb : Measurable (Function.uncurry b))
    (hb0 : ∀ x ω, 0 ≤ b x ω) (hb1 : ∀ x ω, b x ω ≤ 1) :
    productMoment ν μ (m + 1) r (fun _ => b) =
      ∫ v : Fin r → Ω, (replicaAverage ν r b v) ^ (m + 1) ∂Measure.pi (fun _ => μ) := by
  have h := productMoment_eq_replicas ν μ (m + 1) r (fun _ => hb) (fun _ => hb0) (fun _ => hb1)
  simpa only [Finset.prod_const, Finset.card_univ, Fintype.card_fin] using h

theorem mixed_moment (ν : Measure Ξ) (μ : Measure Ω)
    [IsProbabilityMeasure ν] [IsProbabilityMeasure μ] (m r : ℕ)
    {b c : Ξ → Ω → ℝ} (hb : Measurable (Function.uncurry b))
    (hc : Measurable (Function.uncurry c))
    (hb0 : ∀ x ω, 0 ≤ b x ω) (hb1 : ∀ x ω, b x ω ≤ 1)
    (hc0 : ∀ x ω, 0 ≤ c x ω) (hc1 : ∀ x ω, c x ω ≤ 1) :
    productMoment ν μ (m + 1) r (mixedFamily b c) =
      ∫ v : Fin r → Ω, replicaAverage ν r b v * (replicaAverage ν r c v) ^ m
        ∂Measure.pi (fun _ => μ) := by
  have h := productMoment_eq_replicas ν μ (m + 1) r
    (mixedFamily_cases (P := fun f => Measurable (Function.uncurry f)) hb hc)
    (mixedFamily_cases (P := fun f => ∀ x ω, 0 ≤ f x ω) hb0 hc0)
    (mixedFamily_cases (P := fun f => ∀ x ω, f x ω ≤ 1) hb1 hc1)
  rw [h]
  apply integral_congr_ae
  filter_upwards [] with v
  rw [prod_mixedFamily b c (fun f _ => replicaAverage ν r f v)]
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin]

theorem poly_moment_nonneg (ν : Measure Ξ) (μ : Measure Ω)
    [IsProbabilityMeasure ν] [IsProbabilityMeasure μ] (m r : ℕ)
    {b c : Ξ → Ω → ℝ} (hb : Measurable (Function.uncurry b))
    (hc : Measurable (Function.uncurry c))
    (hb0 : ∀ x ω, 0 ≤ b x ω) (hb1 : ∀ x ω, b x ω ≤ 1)
    (hc0 : ∀ x ω, 0 ≤ c x ω) (hc1 : ∀ x ω, c x ω ≤ 1) :
    0 ≤ productMoment ν μ (m + 1) r (fun _ => b) -
      ((m : ℝ) + 1) * productMoment ν μ (m + 1) r (mixedFamily b c) +
      (m : ℝ) * productMoment ν μ (m + 1) r (fun _ => c) := by
  let B := replicaAverage ν r b
  let C := replicaAverage ν r c
  have hB := measurable_replicaAverage ν r hb
  have hC := measurable_replicaAverage ν r hc
  have hBb := replicaAverage_bounds ν r hb hb0 hb1
  have hCb := replicaAverage_bounds ν r hc hc0 hc1
  have hiB : Integrable (fun v => (B v) ^ (m + 1)) (Measure.pi (fun _ : Fin r => μ)) :=
    integrable_unit_interval _ (hB.pow_const _)
      (fun v => pow_nonneg (hBb v).1 _) (fun v => pow_le_one₀ (hBb v).1 (hBb v).2)
  have hiC : Integrable (fun v => (C v) ^ (m + 1)) (Measure.pi (fun _ : Fin r => μ)) :=
    integrable_unit_interval _ (hC.pow_const _)
      (fun v => pow_nonneg (hCb v).1 _) (fun v => pow_le_one₀ (hCb v).1 (hCb v).2)
  have hiBC : Integrable (fun v => B v * (C v) ^ m) (Measure.pi (fun _ : Fin r => μ)) := by
    apply integrable_unit_interval _ (hB.mul (hC.pow_const m))
      (fun v => mul_nonneg (hBb v).1 (pow_nonneg (hCb v).1 _))
    intro v
    exact mul_le_one₀ (hBb v).2 (pow_nonneg (hCb v).1 _) (pow_le_one₀ (hCb v).1 (hCb v).2)
  have hi1 : Integrable (fun v => ((m : ℝ) + 1) * (B v * (C v) ^ m))
      (Measure.pi (fun _ : Fin r => μ)) := hiBC.const_mul _
  have hi2 : Integrable (fun v => (m : ℝ) * (C v) ^ (m + 1)) (Measure.pi (fun _ : Fin r => μ)) :=
    hiC.const_mul _
  have his : Integrable (fun v => (B v) ^ (m + 1) - ((m : ℝ) + 1) * (B v * (C v) ^ m))
      (Measure.pi (fun _ : Fin r => μ)) := hiB.sub hi1
  have h : 0 ≤ ∫ v : Fin r → Ω,
      (B v) ^ (m + 1) - ((m : ℝ) + 1) * (B v * (C v) ^ m) + (m : ℝ) * (C v) ^ (m + 1)
      ∂Measure.pi (fun _ => μ) := by
    apply integral_nonneg
    intro v
    have he : (B v) ^ (m + 1) - ((m : ℝ) + 1) * (B v * (C v) ^ m) + (m : ℝ) * (C v) ^ (m + 1) =
        polyRemainder m (B v) (C v) := by
      unfold polyRemainder
      ring
    have hp := polyRemainder_nonneg m (hBb v).1 (hCb v).1
    rw [← he] at hp
    exact hp
  rw [integral_add his hi2, integral_sub hiB hi1, integral_const_mul, integral_const_mul] at h
  rw [power_moment ν μ m r hb hb0 hb1, mixed_moment ν μ m r hb hc hb0 hb1 hc0 hc1,
    power_moment ν μ m r hc hc0 hc1]
  exact h

end KSatUpper.ReplicaPoly
