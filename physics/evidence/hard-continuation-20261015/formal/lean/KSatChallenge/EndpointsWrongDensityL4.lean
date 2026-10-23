import KSatChallenge.Model

/-! Negative control: altered density in a continuation endpoint statement. -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_4SAT_9934_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (4963*n/500)) atTop (nhds 0) := by
  sorry

end KSatUpper
