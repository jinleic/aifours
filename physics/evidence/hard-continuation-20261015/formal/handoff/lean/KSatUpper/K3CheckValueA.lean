import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel evaluation of the certificate value from `K3Data.momA` and `K3Data.edgeLoA`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckValueA

open K3Data NumericalCriterion TrialDataK3

theorem value : vertexOf 128 (fun k => momA.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (2667/625) * edgeLoA ≤ -1/500000 := by
  decide +kernel

end KSatUpper.K3CheckValueA
