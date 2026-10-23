import KSatUpper.CertificatesK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: edge truncation N = 64 instead of 256. With maximum rate about 0.96 the proved
-- geometric tail is then about 0.025, so the certificate is positive and the kernel must refuse.
theorem bad_certK3_short_edge :
    NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 64 (239949/250000) ≤
      -1/500000 := by
  decide +kernel
