import KSatUpper.Certificates
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Wrong statement: the k=5 certificate value is about -4.63e-4, so the bound -1/2000 is false.
theorem bad_cert5_strong :
    NumericalCriterion.certUpper TrialData.trial5 4 (1057/50) 128 64 (7344/10000) ≤ -1/2000 := by
  decide +kernel
