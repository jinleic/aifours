import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel evaluation of the certificate value from `K3Data.momD` and `K3Data.edgeUpD`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckValueD

open K3Data NumericalCriterion TrialDataK3

theorem value : 0 < vertexOf 128 (fun k => momD.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (426717/100000) * edgeUpD := by
  decide +kernel

end KSatUpper.K3CheckValueD
