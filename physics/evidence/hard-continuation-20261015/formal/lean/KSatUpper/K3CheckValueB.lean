import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel evaluation of the certificate value from `K3Data.momB` and `K3Data.edgeLoB`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckValueB

open K3Data NumericalCriterion TrialDataK3

theorem value : vertexOf 128 (fun k => momB.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (213359/50000) * edgeLoB ≤ -1/2000000 := by
  decide +kernel

end KSatUpper.K3CheckValueB
