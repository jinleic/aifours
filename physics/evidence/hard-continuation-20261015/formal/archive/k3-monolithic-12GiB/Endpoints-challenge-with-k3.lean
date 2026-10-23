import KSatChallenge.Model

/-! Trusted challenge statements for the random k-SAT endpoints (proofs are `sorry`). -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_4SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (249*n/25)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_5SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (1057*n/50)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_3SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (1067*n/250)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_4SAT_9934_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (4967*n/500)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_5SAT_21123_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (21123*n/1000)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_3SAT_42672_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0) := by
  sorry

theorem satisfiabilityProbability_3SAT_426718_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (213359*n/50000)) atTop (nhds 0) := by
  sorry

end KSatUpper
