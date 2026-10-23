import KSatUpper.TrialDataK3
import KSatUpper.NumericalCriterionPrec

/-! Random 3-SAT certificate for the six-atom law `TrialDataK3.trialT256` at `T = 256`
(row `k3_T256_compat_4.26685` of `compat-trials.json`), density `85337/20000 = 4.26685`,
bound `-3/10000000`.

The alternating sums amplify enclosure errors by up to `2^256`, so the precision form is used:
squaring grid `2^-620`, 310 squarings, output grid `2^-300`. Edge truncation `N = 512`: with
maximum rate `u = 488033/500000`, `u^3 ≈ 0.930`, the proved geometric tail
`m α (u^3)^(N+1)/(1-u^3)` is about `1e-15` (`N = 256` would leave about `9e-7`). -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.CertificatesK3T256

open TrialDataK3

theorem cert_426685 :
    NumericalCriterion.certUpperP trialT256 2 (85337/20000) 620 310 300 256 512 (488033/500000) ≤
      -3/10000000 := by
  decide +kernel

end KSatUpper.CertificatesK3T256
