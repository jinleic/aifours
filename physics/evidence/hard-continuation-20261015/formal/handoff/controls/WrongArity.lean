import KSatUpper
open Filter
-- Wrong statement: the 4-SAT theorem does not prove a 5-SAT claim at density 9.96.
example : Tendsto (fun n : ℕ => KSatUpper.satisfiabilityProbability 5 n (249*n/25)) atTop (nhds 0) :=
  KSatUpper.satisfiabilityProbability_4SAT_tendsto_zero
