import KSatUpper.Certificates
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: density 21.10 instead of 21.14. The kernel must refuse this certificate.
theorem bad_cert5_low :
    NumericalCriterion.certUpper TrialData.trial5 4 (211/10) 128 64 (7344/10000) ≤ -1/2500 := by
  decide +kernel
