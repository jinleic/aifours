import KSatUpper.K3Data
import KSatUpper.TrialDataK3
set_option maxRecDepth 100000
set_option maxHeartbeats 0
open KSatUpper K3Data NumericalCriterion TrialDataK3
-- Altered literal: entry 5 of the materialized table raised by one grid step 2^-160. The chunk
-- check against the defining computation must fail.
def tampered : List (ℚ × ℚ) :=
  tblA.set 5 ((tblA.getD 5 (0, 0)).1 + 1/2^160, (tblA.getD 5 (0, 0)).2)

theorem bad_table_tamper : ∀ j, j < 6 → 0 ≤ j →
    bounds trialT128 2 (2667/625) j = tampered.getD j (0, 0) := by
  decide +kernel
