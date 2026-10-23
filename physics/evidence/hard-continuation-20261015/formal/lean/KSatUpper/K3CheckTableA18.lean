import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the entries `108 ≤ j < 114` of `K3Data.tblA`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckTableA18

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ j, j < 114 → 108 ≤ j →
    bounds trialT128 2 (2667/625) j = tblA.getD j (0, 0) := by
  decide +kernel

end KSatUpper.K3CheckTableA18
