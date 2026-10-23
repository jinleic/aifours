import KSatUpper.K3Data
import KSatUpper.TrialDataK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0

open KSatUpper K3Data NumericalCriterion TrialDataK3

example : ∀ j, j < 129 → 113 ≤ j →
    bounds trialT128 2 (2667/625) j = tblA.getD j (0, 0) := by
  decide +kernel
