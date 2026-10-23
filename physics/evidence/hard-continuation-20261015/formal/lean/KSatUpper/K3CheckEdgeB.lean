import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the edge literal `K3Data.edgeLoB`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckEdgeB

open K3Data NumericalCriterion TrialDataK3

theorem edge : edgeLoB ≤ edgeLower trialT128 2 256 (239949/250000) := by
  decide +kernel

end KSatUpper.K3CheckEdgeB
