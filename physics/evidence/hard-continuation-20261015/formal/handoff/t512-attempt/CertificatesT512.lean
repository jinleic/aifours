import KSatUpper.TrialData
import KSatUpper.NumericalCriterionPrec

/-! Headline certificate attempt: law L4 at `T = 512`, density `3973/400 = 9.9325`, bound
`-1/200000`, with output grid `2^-600`, squaring grid `2^-1240` and 620 squarings. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.CertificatesT512

open TrialData

theorem certL4_T512 :
    NumericalCriterion.certUpperP trialL4 3 (3973/400) 1240 620 600 512 64 (907479/1000000) ≤
      -1/200000 := by
  decide +kernel

end KSatUpper.CertificatesT512
