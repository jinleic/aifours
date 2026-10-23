import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- One entry (j = 128) of the T = 128 exponential table: 160 squarings on the 2^-320 grid.
example : (NumericalCriterion.bounds TrialDataK3.trialT128 2 (2667/625) 128).1 ≤ 1 := by
  decide +kernel
