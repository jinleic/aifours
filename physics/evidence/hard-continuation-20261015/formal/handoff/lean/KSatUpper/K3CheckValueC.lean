import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel evaluation of the certificate value from `K3Data.momC` and `K3Data.edgeUpC`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckValueC

open K3Data NumericalCriterion TrialDataK3

theorem value : 0 < vertexOf 128 (fun k => momC.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (42671/10000) * edgeUpC := by
  decide +kernel

end KSatUpper.K3CheckValueC
