import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the moments `0 ≤ k < 34` of `K3Data.momD`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckMomD0

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ k, k < 34 → 0 ≤ k →
    VertexEnclosures.momentLower (lowerOf tblD) (upperOf tblD) k = momD.getD k 0 := by
  decide +kernel

end KSatUpper.K3CheckMomD0
