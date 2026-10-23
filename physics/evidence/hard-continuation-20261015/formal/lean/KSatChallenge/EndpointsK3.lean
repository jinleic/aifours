import KSatChallenge.Model

/-! Trusted challenge statements for the random 3-SAT endpoints below 4.268 (proofs are
`sorry`). -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_3SAT_42672_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_3SAT_426718_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (213359*n/50000)) atTop (nhds 0) := by
  sorry

end KSatUpper
