import KSatUpper.TrialData
import KSatUpper.NumericalCriterion
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : TrialData.trial4.moment 2 ≤ 1 := by decide +kernel
example : TrialData.trial4.markMoment 3 2 ≤ 1 := by decide +kernel
example : NumericalCriterion.argument TrialData.trial4 3 (249/25) 2 ≤ 0 := by decide +kernel
example : NumericalCriterion.edgeLower TrialData.trial4 3 4 (7707/10000) ≤ 0 := by decide +kernel
example : (NumericalCriterion.bounds TrialData.trial4 3 (249/25) 2).1 ≤ 1 := by decide +kernel
example : VertexEnclosures.vertexUpper 2 (fun _ => 0) (fun _ => 1) ≤ 0 := by decide +kernel
