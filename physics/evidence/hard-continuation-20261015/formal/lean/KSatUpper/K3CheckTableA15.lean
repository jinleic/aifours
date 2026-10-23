import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the entries `90 ≤ j < 96` of `K3Data.tblA`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckTableA15

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ j, j < 96 → 90 ≤ j →
    bounds trialT128 2 (2667/625) j = tblA.getD j (0, 0) := by
  decide +kernel

end KSatUpper.K3CheckTableA15
