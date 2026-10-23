import KSatUpper.CertificatesK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
-- Altered input: same k=3 law at density 4.2671, below the certified 4.26718. The kernel must
-- refuse this certificate.
theorem bad_certK3_low :
    NumericalCriterion.certUpper TrialDataK3.trialT128 2 (42671/10000) 128 256 (239949/250000) ≤
      -1/2000000 := by
  decide +kernel
