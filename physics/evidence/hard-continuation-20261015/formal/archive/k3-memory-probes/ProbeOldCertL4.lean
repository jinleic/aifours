import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : NumericalCriterion.certUpper TrialData.trialL4 3 (4967/500) 128 64 (907479/1000000) ≤ -1/20000 := by decide +kernel
