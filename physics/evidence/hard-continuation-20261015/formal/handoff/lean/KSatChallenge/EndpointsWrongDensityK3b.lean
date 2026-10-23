import KSatChallenge.Model

/-! Negative control: the 4.26718 endpoint statement with density altered to 4.26717. -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_3SAT_426718_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (426717*n/100000)) atTop (nhds 0) := by
  sorry

end KSatUpper
