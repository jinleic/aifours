import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the moments `116 ≤ k < 121` of `K3Data.momA`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckMomA12

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ k, k < 121 → 116 ≤ k →
    VertexEnclosures.momentLower (lowerOf tblA) (upperOf tblA) k = momA.getD k 0 := by
  decide +kernel

end KSatUpper.K3CheckMomA12
