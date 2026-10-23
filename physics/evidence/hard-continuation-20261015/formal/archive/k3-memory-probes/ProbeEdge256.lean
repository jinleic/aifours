import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : NumericalCriterion.edgeLower TrialDataK3.trialT128 2 256 (239949/250000) ≤ 0 := by decide +kernel
