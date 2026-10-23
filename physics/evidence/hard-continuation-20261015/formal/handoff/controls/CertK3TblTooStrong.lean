import KSatUpper.K3Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper K3Data NumericalCriterion
-- Wrong statement: at 4.2672 the certificate value is about -2.5e-6, so the bound -1/250000 is
-- false and the kernel must refuse it.
theorem bad_certK3_strong :
    vertexOf 128 (fun k => momA.getD k 0) +
      (-((2 : ℕ) : ℚ)) * (2667/625) * edgeLoA ≤ -1/250000 := by
  decide +kernel
