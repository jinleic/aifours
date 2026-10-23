import KSatUpper.K3Data
import KSatUpper.TrialDataK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0

open KSatUpper K3Data NumericalCriterion TrialDataK3

example : edgeLoA ≤ edgeLower trialT128 2 256 (239949/250000) := by
  decide +kernel
