import KSatUpper.CertificatesK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Wrong statement: at 4.2672 the certificate value is about -2.5e-6, so the bound -1/250000 is
-- false and the kernel must refuse it.
theorem bad_certK3_strong :
    NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 256 (239949/250000) ≤
      -1/250000 := by
  decide +kernel
