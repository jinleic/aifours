import KSatUpper.Certificates
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: density 9.90 instead of 9.96. The kernel must refuse this certificate.
theorem bad_cert4_low :
    NumericalCriterion.certUpper TrialData.trial4 3 (99/10) 128 64 (7707/10000) ≤ -1/1000 := by
  decide +kernel
