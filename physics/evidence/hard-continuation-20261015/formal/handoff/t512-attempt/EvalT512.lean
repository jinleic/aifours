import KSatUpper.TrialData
import KSatUpper.NumericalCriterionPrec
open KSatUpper
def toF (q : ℚ) : Float := Float.ofInt (Rat.floor (q * 10^15)) / 1e15
#eval toF (NumericalCriterion.certUpperP TrialData.trialL4 3 (3973/400) 1240 620 600 512 64 (907479/1000000))
