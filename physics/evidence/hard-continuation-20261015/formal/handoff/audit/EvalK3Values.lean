import KSatUpper.TrialDataK3
import KSatUpper.NumericalCriterion
import KSatUpper.NumericalCriterionPrec

/-! Evaluation (not proof) of the k=3 certificate values and of the edge-tail bound
`m α (u^3)^(N+1)/(1-u^3)` used to choose the edge truncation `N`.
Outputs are `floor(value * 10^e)` as integers. -/

open KSatUpper

def sc (e : ℕ) (q : ℚ) : Int := Rat.floor (q * 10^e)
def uA : ℚ := 239949/250000
def uC : ℚ := 488033/500000
def tail (α u : ℚ) (N : ℕ) : ℚ := 2 * α * (u^3)^(N+1) / (1 - u^3)

#eval ("tail*1e18 T128 law (alpha 4.2672) N=64,128,192,256", sc 18 (tail (2667/625) uA 64),
  sc 18 (tail (2667/625) uA 128), sc 18 (tail (2667/625) uA 192), sc 18 (tail (2667/625) uA 256))
#eval ("tail*1e18 T256 law (alpha 4.26685) N=256,384,512", sc 18 (tail (85337/20000) uC 256),
  sc 18 (tail (85337/20000) uC 384), sc 18 (tail (85337/20000) uC 512))
#eval ("cert*1e12 T128 4.2672 N=256",
  sc 12 (NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 256 uA))
#eval ("cert*1e12 T128 4.26718 N=256",
  sc 12 (NumericalCriterion.certUpper TrialDataK3.trialT128 2 (213359/50000) 128 256 uA))
#eval ("cert*1e12 T128 4.26717 N=256",
  sc 12 (NumericalCriterion.certUpper TrialDataK3.trialT128 2 (426717/100000) 128 256 uA))
#eval ("cert*1e12 T128 4.2671 N=256",
  sc 12 (NumericalCriterion.certUpper TrialDataK3.trialT128 2 (42671/10000) 128 256 uA))
#eval ("cert*1e12 T128 4.2672 N=64",
  sc 12 (NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 64 uA))
#eval ("cert*1e12 T256 4.26685 N=512 prec(620,310,300)", sc 12 (NumericalCriterion.certUpperP
  TrialDataK3.trialT256 2 (85337/20000) 620 310 300 256 512 uC))
#eval ("cert*1e12 T256 4.26684 N=512 prec(620,310,300)", sc 12 (NumericalCriterion.certUpperP
  TrialDataK3.trialT256 2 (106671/25000) 620 310 300 256 512 uC))
