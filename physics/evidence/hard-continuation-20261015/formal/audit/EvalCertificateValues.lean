import KSatUpper.TrialData
import KSatUpper.NumericalCriterion
open KSatUpper
def toF (q : ℚ) : Float := Float.ofInt (Rat.floor (q * 10^15)) / 1e15
#eval toF (NumericalCriterion.certUpper TrialData.trial4 3 (249/25) 128 64 (7707/10000))
#eval toF (NumericalCriterion.certUpper TrialData.trial5 4 (1057/50) 128 64 (7344/10000))
#eval toF (NumericalCriterion.certUpper TrialData.trial3 2 (1067/250) 128 64 (17/20))
#eval toF (NumericalCriterion.certUpper TrialData.trial4 3 (99/10) 128 64 (7707/10000))
#eval toF (NumericalCriterion.certUpper TrialData.trial5 4 (211/10) 128 64 (7344/10000))
