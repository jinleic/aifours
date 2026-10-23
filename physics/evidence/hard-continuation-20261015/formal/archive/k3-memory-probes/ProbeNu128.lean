import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : TrialDataK3.trialT128.markMoment 2 128 ≤ 1 := by decide +kernel
