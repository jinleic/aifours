import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the moments `68 ≤ k < 76` of `K3Data.momC`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckMomC4

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ k, k < 76 → 68 ≤ k →
    VertexEnclosures.momentLower (lowerOf tblC) (upperOf tblC) k = momC.getD k 0 := by
  decide +kernel

end KSatUpper.K3CheckMomC4
