import KSatUpper
open Filter
-- Wrong statement: the 4-SAT theorem does not prove the claim at density 9.90.
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 4 n (99*n/10)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_4SAT_tendsto_zero
