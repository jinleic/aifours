import KSatUpper.ReplacementPoissonMean

/-! The Poisson count error vanishes after normalization.

Derived from `SatUpper/ReplacementAsymptotic.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open Filter
open scoped Topology

namespace KSatUpper.ReplacementAsymptotic

noncomputable def countError (α : ℝ) (n : ℕ) : ℝ :=
  Real.sqrt (α*n+1)/n

theorem countError_tendsto {α : ℝ} (hα : 0 ≤ α) : Tendsto (countError α) atTop (𝓝 0) := by
  have hi : Tendsto (fun n : ℕ => (n : ℝ)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp tendsto_natCast_atTop_atTop
  have ht := ((hi.const_mul α).add (hi.pow 2)).sqrt
  simp only [mul_zero, zero_pow (by decide : 2 ≠ 0), add_zero, Real.sqrt_zero] at ht
  apply ht.congr'
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn0 : (n : ℝ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  have ha : 0 ≤ α*n+1 := by positivity
  have he : α*(n : ℝ)⁻¹ + ((n : ℝ)⁻¹)^2 = (α*n+1)/(n : ℝ)^2 := by field_simp
  rw [he, Real.sqrt_div ha, Real.sqrt_sq (Nat.cast_nonneg n)]
  unfold countError
  ring

end KSatUpper.ReplacementAsymptotic
