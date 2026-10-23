import KSatUpper.K3Data
import KSatUpper.TrialDataK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0

open KSatUpper K3Data NumericalCriterion TrialDataK3

example : VertexEnclosures.vertexUpper 128 (lowerOf tblA) (upperOf tblA) ≤ 0 := by
  decide +kernel
