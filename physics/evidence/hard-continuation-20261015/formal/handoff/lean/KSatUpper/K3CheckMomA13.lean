import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the moments `121 ≤ k < 125` of `K3Data.momA`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckMomA13

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ k, k < 125 → 121 ≤ k →
    VertexEnclosures.momentLower (lowerOf tblA) (upperOf tblA) k = momA.getD k 0 := by
  decide +kernel

end KSatUpper.K3CheckMomA13
