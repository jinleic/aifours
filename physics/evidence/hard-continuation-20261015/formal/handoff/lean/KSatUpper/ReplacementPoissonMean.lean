import KSatUpper.Ground.Clause
import KSatUpper.Ground.Bound
import KSatUpper.PoissonCountMoments

/-! De-Poissonize the integer-energy mean using its one-clause bound.

Derived from `SatUpper/ReplacementPoissonMean.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory ProbabilityTheory
open scoped NNReal

namespace KSatUpper.ReplacementPoissonMean

variable {p : ℕ} (T : TrialLaw p) (m : ℕ)

theorem scaled_fixed_floor_le (n : ℕ) [NeZero n] {α y : ℝ} (hα : 0 ≤ α) (hy : 0 ≤ y)
    (cutoff : ℕ) :
    (-y/n) * GroundFormula.mean (m + 1) n ⌊α*n⌋₊ ≤
      Criterion.finiteAnalyticBound T m α cutoff + (cutoff : ℝ)*Real.exp (-y) +
        y*(Real.sqrt (α*n+1)/n) := by
  have hn : (0 : ℝ) < n := Nat.cast_pos.mpr (Nat.pos_of_ne_zero (NeZero.ne n))
  have h := PoissonCountMoments.fixed_floor_le
    (f := fun K => GroundComparison.mean T m n y K 0)
    (fun K => GroundComparison.clause_difference_bound T m hy K 0) (GroundBound.density hα*n)
  simp only [NNReal.coe_mul, NNReal.coe_natCast, GroundBound.coe_density] at h
  have hb := GroundBound.scaled_mean_le T m n hα hy cutoff
  simp only [DirectPoisson.expectation, DirectPoisson.zero_law, integral_dirac] at hb
  have hh := div_le_div_of_nonneg_right h hn.le
  rw [GroundClause.fixed_mean T, add_div] at hh
  rw [div_mul_eq_mul_div]
  calc
    _ ≤ _ := hh
    _ ≤ _ := by rw [mul_div_assoc]; exact add_le_add_right hb _

end KSatUpper.ReplacementPoissonMean
