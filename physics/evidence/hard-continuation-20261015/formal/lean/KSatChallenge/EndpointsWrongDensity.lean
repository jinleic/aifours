import KSatChallenge.Model

/-! Negative control: a changed target statement (density 9.90 instead of 9.96). -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_4SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (99*n/10)) atTop (nhds 0) := by
  sorry

end KSatUpper
