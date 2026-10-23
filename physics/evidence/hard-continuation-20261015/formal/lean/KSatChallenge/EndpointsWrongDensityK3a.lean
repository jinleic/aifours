import KSatChallenge.Model

/-! Negative control: the 4.2672 endpoint statement with density altered to 4.2671. -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_3SAT_42672_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (42671*n/10000)) atTop (nhds 0) := by
  sorry

end KSatUpper
