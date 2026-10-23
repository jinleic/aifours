import KSatUpper.Ground.SiteBound
import KSatUpper.Ground.Edge

/-! The energetic interpolation gives the certified trial bound, (A) of the written proof.

Derived from `SatUpper/Ground/Bound.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory
open scoped NNReal

namespace KSatUpper.GroundBound

/-- The clause density as a nonnegative real. -/
def density {α : ℝ} (hα : 0 ≤ α) : ℝ≥0 := ⟨α, hα⟩

theorem coe_density {α : ℝ} (hα : 0 ≤ α) : (density hα : ℝ) = α := rfl

variable {p : ℕ} (T : TrialLaw p) (m : ℕ)

/-- For every `n ≥ 1` and `y ≥ 0`, the Poisson repeated-variable energy satisfies
`-(y/n) E E(F) ≤ Psi_T + T e^{-y}`, written for the entropy functional. -/
theorem scaled_mean_le (n : ℕ) [NeZero n] {α y : ℝ} (hα : 0 ≤ α) (hy : 0 ≤ y) (cutoff : ℕ) :
    DirectPoisson.expectation (GroundComparison.mean T m n y) (density hα*n) 0 / n ≤
      Criterion.finiteAnalyticBound T m α cutoff + (cutoff : ℝ)*Real.exp (-y) := by
  have hn : (0 : ℝ) < n := Nat.cast_pos.mpr (Nat.pos_of_ne_zero (NeZero.ne n))
  have hr : ((((m : ℝ≥0)+1)*(density hα*n) : ℝ≥0) : ℝ)/(2*n) = ((m : ℝ)+1)*α/2 := by
    simp only [NNReal.coe_mul, NNReal.coe_add, NNReal.coe_natCast, NNReal.coe_one, coe_density]
    field_simp
  have h := GroundComparison.endpoint_comparison T m (n := n) hy (density hα*n)
  have hs := GroundSiteBound.endpoint T (n := n) hy (((m : ℝ≥0)+1)*(density hα*n)) hr cutoff
  have hh := div_le_div_of_nonneg_right (h.trans (sub_le_sub_right hs _)) hn.le
  have he := GroundEdge.correction_bound T m n (y := y) hα
  have he' : DirectPoisson.expectation (GroundComparison.mean T m n y) (density hα*n) 0 / n ≤
      negativeMomentSum cutoff (Criterion.noWarningMoment T m α) + (cutoff : ℝ)*Real.exp (-y) -
        (m : ℝ)*α*GroundInsertion.edgeMean T m n y := by
    convert hh using 1
    simp only [NNReal.coe_mul, NNReal.coe_natCast, coe_density]
    field_simp
  unfold Criterion.finiteAnalyticBound
  linarith

end KSatUpper.GroundBound
