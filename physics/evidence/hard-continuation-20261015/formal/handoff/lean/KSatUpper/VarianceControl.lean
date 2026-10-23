import KSatUpper.FiniteVariance
import KSatUpper.Ground.Formula

/-! Minimum energy has one-clause Lipschitz constant one, hence linear variance.

Derived from `SatUpper/VarianceControl.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

namespace KSatUpper.Formalization

theorem energy_variance_le (k n M : ℕ) [NeZero n] : GroundFormula.variance k n M ≤ M := by
  simpa [GroundFormula.variance] using FiniteVariance.variance_fin_pi_le M
    (fun F : GroundFormula.Formula k n M => (GroundFormula.energy F : ℝ))
    (by norm_num : (0 : ℝ) ≤ 1) GroundFormula.energy_one_clause_lipschitz

end KSatUpper.Formalization
