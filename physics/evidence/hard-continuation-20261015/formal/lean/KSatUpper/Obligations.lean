import KSatUpper.LegalConditioning
import KSatUpper.VarianceControl

/-! Assembly: an asymptotic energetic comparison with a negative finite bound forces
unsatisfiability with probability tending to one, for every arity `k`.

Derived from `SatUpper/Obligations.lean` (yamelton/sat-upper-4268, Apache-2.0), where the
arity, density and bound were fixed constants. -/

open Filter

namespace KSatUpper.Formalization

/-- The comparison obligation, for arity `k`, clause counts `M n`, a finite bound and cutoff. -/
def AsymptoticComparison (k : ℕ) (M : ℕ → ℕ) (bound : ℝ) (cutoff : ℕ) : Prop :=
  ∀ y : ℝ, 0 < y → ∀ δ : ℝ, 0 < δ → ∀ᶠ (n : ℕ) in atTop,
    (-y / n) * GroundFormula.mean k n (M n) ≤ bound + (cutoff : ℝ)*Real.exp (-y) + δ

/-- Choose the softening parameter large enough, then use Chebyshev concentration. -/
theorem upperBound_of_comparison (k : ℕ) (M : ℕ → ℕ) {α : ℝ} (hα : 0 ≤ α)
    (hM : ∀ n, (M n : ℝ) ≤ α*n) {bound : ℝ} (hbound : bound < 0) (cutoff : ℕ)
    (hcomparison : AsymptoticComparison k M bound cutoff) :
    Tendsto (fun n => satisfiabilityProbability k n (M n)) atTop (nhds 0) := by
  have hv : ∀ᶠ n in atTop, GroundFormula.variance k n (M n) ≤ α*n := by
    filter_upwards [eventually_ge_atTop 1] with n hn
    letI : NeZero n := ⟨by omega⟩
    exact (energy_variance_le k n (M n)).trans (hM n)
  have hδ : 0 < -bound/4 := by linarith
  have ht : Tendsto (fun y : ℝ => (cutoff : ℝ)*Real.exp (-y)) atTop (nhds 0) := by
    simpa using Real.tendsto_exp_neg_atTop_nhds_zero.const_mul (cutoff : ℝ)
  obtain ⟨y, hy, he⟩ := ((eventually_gt_atTop (0 : ℝ)).and (ht.eventually_le_const hδ)).exists
  let c : ℝ := -bound/(2*y)
  have hc : 0 < c := div_pos (neg_pos.mpr hbound) (mul_pos (by norm_num) hy)
  apply LegalConditioning.candidate_of_mean_and_variance_bounds k M α c α hc hα hM _ hv
  filter_upwards [hcomparison y hy _ hδ, eventually_ge_atTop 1] with n hn hnat
  have hnpos : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
  apply (mul_le_mul_iff_right₀ (div_pos hy hnpos)).mp
  calc
    (y/n)*(c*n) = -bound/2 := by dsimp [c]; field_simp
    _ ≤ (y/n)*GroundFormula.mean k n (M n) := by
      rw [neg_div, neg_mul] at hn
      linarith

end KSatUpper.Formalization
