import KSatUpper.Trial
import Mathlib.Tactic.FinCases

/-! Six-atom random 3-SAT trial laws, copied as exact rationals from
`physics/evidence/hard-continuation-20261015/k3-extension/certificates/compat-trials.json`
(SHA-256 `7b0d2615eaf8ba45bbcf47a81caf2985699400592ac4c4fa84bfc156c93ad044`).

* `trialT128`: rows `k3_T128_compat_4.26718` and `k3_T128_compat_4.2672`, maximum rate
  `239949/250000`.
* `trialT256`: row `k3_T256_compat_4.26685`, maximum rate `488033/500000`. -/

namespace KSatUpper.TrialDataK3

def weightT128 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 88243/500000
  | 1 => 18199/100000
  | 2 => 277249/1000000
  | 3 => 52911/250000
  | 4 => 110211/1000000
  | _ => 2121/50000

def rateT128 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 12163/250000
  | 1 => 89433/500000
  | 2 => 49679/125000
  | 3 => 33501/50000
  | 4 => 107537/125000
  | _ => 239949/250000

def trialT128 : TrialLaw 6 where
  weight := weightT128
  rate := rateT128
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weightT128]
  weight_sum := by simp [Fin.sum_univ_succ, weightT128]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rateT128]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rateT128]

def weightT256 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 10447/50000
  | 1 => 221909/1000000
  | 2 => 131703/500000
  | 3 => 192899/1000000
  | 4 => 88161/1000000
  | _ => 4937/200000

def rateT256 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 55443/1000000
  | 1 => 3568/15625
  | 2 => 58199/125000
  | 3 => 91223/125000
  | 4 => 899787/1000000
  | _ => 488033/500000

def trialT256 : TrialLaw 6 where
  weight := weightT256
  rate := rateT256
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weightT256]
  weight_sum := by simp [Fin.sum_univ_succ, weightT256]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rateT256]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rateT256]

end KSatUpper.TrialDataK3
