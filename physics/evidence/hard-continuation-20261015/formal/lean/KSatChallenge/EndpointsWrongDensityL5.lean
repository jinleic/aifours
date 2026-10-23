import KSatChallenge.Model

/-! Negative control: altered density in a continuation endpoint statement. -/

open Filter

namespace KSatUpper

theorem satisfiabilityProbability_5SAT_21123_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (21118*n/1000)) atTop (nhds 0) := by
  sorry

end KSatUpper
