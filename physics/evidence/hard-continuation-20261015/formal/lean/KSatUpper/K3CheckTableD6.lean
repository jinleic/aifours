import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the entries `36 ≤ j < 42` of `K3Data.tblD`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckTableD6

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ j, j < 42 → 36 ≤ j →
    bounds trialT128 2 (426717/100000) j = tblD.getD j (0, 0) := by
  decide +kernel

end KSatUpper.K3CheckTableD6
