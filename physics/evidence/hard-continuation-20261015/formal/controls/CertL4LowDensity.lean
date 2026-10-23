import KSatUpper.Certificates
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: density 4963/500 just below the certified continuation density.
theorem bad_CertL4LowDensity :
    NumericalCriterion.certUpper TrialData.trialL4 3 (4963/500) 128 64 (907479/1000000) ≤ -1/20000 := by
  decide +kernel
