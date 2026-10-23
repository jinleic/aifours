import KSatUpper.K3Data
import KSatUpper.TrialDataK3

/-! Kernel check of the entries `18 ≤ j < 24` of `K3Data.tblC`. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.K3CheckTableC3

open K3Data NumericalCriterion TrialDataK3

theorem chunk : ∀ j, j < 24 → 18 ≤ j →
    bounds trialT128 2 (42671/10000) j = tblC.getD j (0, 0) := by
  decide +kernel

end KSatUpper.K3CheckTableC3
