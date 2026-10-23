import KSatUpper.K3Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper K3Data NumericalCriterion
-- Altered input: the materialized moments at density 4.2671 (below the certified 4.26718). The
-- certificate value is positive there, so the kernel must refuse the claimed bound.
theorem bad_certK3_low :
    vertexOf 128 (fun k => momC.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (42671/10000) * edgeUpC ≤ -1/2000000 := by
  decide +kernel
