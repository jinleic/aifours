import KSatUpper.K3Data
import KSatUpper.TrialDataK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper K3Data NumericalCriterion TrialDataK3
-- Altered input: edge truncation N = 64 instead of 256. With maximum rate about 0.96 the proved
-- geometric tail is then about 3e-3, so the N = 256 edge literal is not a lower bound and the
-- kernel must refuse.
theorem bad_edgeK3_short :
    edgeLoA ≤ edgeLower trialT128 2 64 (239949/250000) := by
  decide +kernel
