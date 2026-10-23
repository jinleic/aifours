import KSatUpper.TrialData
import KSatUpper.NumericalCriterion
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
def toF (q : ℚ) : Float := Float.ofInt (Rat.floor (q * 10^15)) / 1e15
#eval toF (NumericalCriterion.certUpper TrialData.trial4 3 (249/25) 8 64 (7707/10000))
theorem cert4_probe : NumericalCriterion.certUpper TrialData.trial4 3 (249/25) 128 64 (7707/10000) ≤ -1/1000 := by
  decide +kernel
