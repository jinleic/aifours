import KSatUpper.CertificatesK3
import KSatUpper.TrialData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper
example : VertexEnclosures.vertexUpper 128 (NumericalCriterion.lowerOf (NumericalCriterion.table TrialDataK3.trialT128 2 (2667/625) 128)) (NumericalCriterion.upperOf (NumericalCriterion.table TrialDataK3.trialT128 2 (2667/625) 128)) ≤ 0 := by decide +kernel
