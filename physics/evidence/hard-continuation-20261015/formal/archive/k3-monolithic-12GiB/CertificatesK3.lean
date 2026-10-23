import KSatUpper.TrialDataK3
import KSatUpper.NumericalCriterion

/-! Kernel-checked random 3-SAT certificates for the six-atom law `TrialDataK3.trialT128`
(`T = 128`, rows `k3_T128_compat_4.2672` and `k3_T128_compat_4.26718` of `compat-trials.json`).

Edge truncation `N = 256`. With maximum rate `u = 239949/250000`, `u^3 ≈ 0.884`, the proved
geometric tail `m α (u^3)^(N+1)/(1-u^3)` is about `1e-13` at `α ≈ 4.267` (`N = 64` would leave
about `0.025`, and `N = 128` about `9e-6`), against certified margins of order `1e-7`.

The two controls show that the same certificate is positive for the same law at the densities
4.2671 and 4.26717, just below the certified ones. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.CertificatesK3

open TrialDataK3

theorem cert_42672 :
    NumericalCriterion.certUpper trialT128 2 (2667/625) 128 256 (239949/250000) ≤ -1/500000 := by
  decide +kernel

theorem cert_426718 :
    NumericalCriterion.certUpper trialT128 2 (213359/50000) 128 256 (239949/250000) ≤
      -1/2000000 := by
  decide +kernel

theorem control_42671_low :
    0 < NumericalCriterion.certUpper trialT128 2 (42671/10000) 128 256 (239949/250000) := by
  decide +kernel

theorem control_426717_low :
    0 < NumericalCriterion.certUpper trialT128 2 (426717/100000) 128 256 (239949/250000) := by
  decide +kernel

end KSatUpper.CertificatesK3
