import KSatChallenge.Model
import KSatChallenge.Criterion

/-! Trusted challenge statement for the general-arity theorem (proof is `sorry`). -/

open Filter

namespace KSatUpper

theorem tendsto_zero_of_criterion {p : ℕ} (T : TrialLaw p) (m : ℕ) {α : ℝ} (hα : 0 ≤ α)
    (cutoff : ℕ) (hΨ : Criterion.finiteAnalyticBound T m α cutoff < 0) :
    Tendsto (fun n : ℕ => satisfiabilityProbability (m + 1) n ⌊α*n⌋₊) atTop (nhds 0) := by
  sorry

end KSatUpper
