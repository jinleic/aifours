import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 256 (239949/250000) ≤ -1/500000 := by decide +kernel
