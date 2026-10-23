import KSatUpper.Certificates
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: density 21118/1000 just below the certified continuation density.
theorem bad_CertL5LowDensity :
    NumericalCriterion.certUpper TrialData.trialL5 4 (21118/1000) 128 64 (97351/125000) ≤ -1/100000 := by
  decide +kernel
