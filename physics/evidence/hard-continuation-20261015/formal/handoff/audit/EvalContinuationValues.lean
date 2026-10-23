import KSatUpper.TrialData
import KSatUpper.NumericalCriterion
open KSatUpper
def toF (q : ℚ) : Float := Float.ofInt (Rat.floor (q * 10^15)) / 1e15
#eval toF (NumericalCriterion.certUpper TrialData.trialL4 3 (4967/500) 128 64 (907479/1000000))
#eval toF (NumericalCriterion.certUpper TrialData.trialL5 4 (21123/1000) 128 64 (97351/125000))
#eval toF (NumericalCriterion.certUpper TrialData.trialL4 3 (99/10) 128 64 (907479/1000000))
#eval toF (NumericalCriterion.certUpper TrialData.trialL5 4 (211/10) 128 64 (97351/125000))
#eval toF (NumericalCriterion.certUpper TrialData.trialL4 3 (4963/500) 128 64 (907479/1000000))
#eval toF (NumericalCriterion.certUpper TrialData.trialL5 4 (21118/1000) 128 64 (97351/125000))
