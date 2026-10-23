import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the moments `48 ≤ k < 59` of `K3Data.momB`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckMomB2

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ k, k < 59 → 48 ≤ k →
    VertexEnclosures.momentLower (lowerOf tblB) (upperOf tblB) k = momB.getD k 0 := by
  decide +kernel

end KSatUpper.K3CheckMomB2
