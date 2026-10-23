import KSatUpper.TrialData
open KSatUpper
-- Altered input: weights summing to 9999/10000 cannot form a trial law.
def badWeight (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 2946/10000
  | 1 => 3362/10000
  | _ => 3691/10000
def badTrial : TrialLaw 3 where
  weight := badWeight
  rate := TrialData.rate4
  weight_nonneg := by intro i; fin_cases i <;> norm_num [badWeight]
  weight_sum := by simp [Fin.sum_univ_succ, badWeight]; norm_num
  rate_nonneg := TrialData.trial4.rate_nonneg
  rate_lt_one := TrialData.trial4.rate_lt_one
