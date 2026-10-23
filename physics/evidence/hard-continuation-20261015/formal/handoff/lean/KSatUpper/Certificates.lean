import KSatUpper.TrialData
import KSatUpper.NumericalCriterion

/-! Kernel-checked rational certificates for the finite criterion.

Each `decide +kernel` makes the Lean kernel evaluate the exact rational certificate value
`NumericalCriterion.certUpper`; `finiteAnalyticBound_le_cert` proves that this value is an
upper bound for `Psi_128`. No external numerical data is imported: the trial laws are the
rational laws of `TrialData`, and every rounding is outward and proved sound.

The two `control_*` theorems are discriminating controls: at the lower densities
`9.90` (k=4) and `21.10` (k=5), just below the cavity predictions `9.931` and `21.117`, the
same kernel computation yields a strictly positive value, so no unsatisfiability claim can
be derived there by this certificate. -/

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace KSatUpper.Certificates

open TrialData

theorem cert4 :
    NumericalCriterion.certUpper trial4 3 (249/25) 128 64 (7707/10000) ≤ -1/1000 := by
  decide +kernel

theorem cert5 :
    NumericalCriterion.certUpper trial5 4 (1057/50) 128 64 (7344/10000) ≤ -1/2500 := by
  decide +kernel

theorem cert3 :
    NumericalCriterion.certUpper trial3 2 (1067/250) 128 64 (17/20) ≤ -1/100000 := by
  decide +kernel

theorem control4_low :
    0 < NumericalCriterion.certUpper trial4 3 (99/10) 128 64 (7707/10000) := by
  decide +kernel

theorem control5_low :
    0 < NumericalCriterion.certUpper trial5 4 (211/10) 128 64 (7344/10000) := by
  decide +kernel

/-! Continuation laws L4/L5 (`TrialData.trialL4/L5`, six atoms) at the compatibility rows of
`certificates/trials.json`: `T = 128`, densities `4967/500 = 9.934` and `21123/1000 = 21.123`.
The controls show the same certificate is positive at the slightly lower densities
`4963/500 = 9.926` and `21118/1000 = 21.118`. -/

theorem certL4 :
    NumericalCriterion.certUpper trialL4 3 (4967/500) 128 64 (907479/1000000) ≤ -1/20000 := by
  decide +kernel

theorem certL5 :
    NumericalCriterion.certUpper trialL5 4 (21123/1000) 128 64 (97351/125000) ≤ -1/100000 := by
  decide +kernel

theorem controlL4_low :
    0 < NumericalCriterion.certUpper trialL4 3 (4963/500) 128 64 (907479/1000000) := by
  decide +kernel

theorem controlL5_low :
    0 < NumericalCriterion.certUpper trialL5 4 (21118/1000) 128 64 (97351/125000) := by
  decide +kernel

end KSatUpper.Certificates
