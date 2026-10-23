import KSatUpper.Trial
import Mathlib.Tactic.FinCases

/-! The explicit rational trial laws of the written proof (`certificates/trials.json`).

`k4` and `k5` are the new laws; `k3` is the reference law of yamelton/sat-upper-4268
(labels 1/20, 17/20, 2/5, 2/5 equally likely), used here as a regression control. -/

namespace KSatUpper.TrialData

def weight4 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 2946/10000
  | 1 => 3363/10000
  | _ => 3691/10000

def rate4 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 1745/10000
  | 1 => 7707/10000
  | _ => 4454/10000

def trial4 : TrialLaw 3 where
  weight := weight4
  rate := rate4
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weight4]
  weight_sum := by simp [Fin.sum_univ_succ, weight4]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rate4]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rate4]

def weight5 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 1009/10000
  | 1 => 6190/10000
  | _ => 2801/10000

def rate5 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 5391/10000
  | 1 => 3691/10000
  | _ => 7344/10000

def trial5 : TrialLaw 3 where
  weight := weight5
  rate := rate5
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weight5]
  weight_sum := by simp [Fin.sum_univ_succ, weight5]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rate5]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rate5]

def weight3 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 1/4
  | 1 => 1/2
  | _ => 1/4

def rate3 (i : Fin 3) : ℚ :=
  match i.val with
  | 0 => 1/20
  | 1 => 2/5
  | _ => 17/20

def trial3 : TrialLaw 3 where
  weight := weight3
  rate := rate3
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weight3]
  weight_sum := by simp [Fin.sum_univ_succ, weight3]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rate3]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rate3]

/-! Continuation laws L4 and L5 (six atoms, denominators dividing 10^6) of
`physics/evidence/hard-continuation-20261015/certificates/trials.json` (SHA-256
`1cdc03c232078cac29906c0156bfdf7658b40fbe80fe1d0577dbcfc87000913e`). -/

def weightL4 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 61927/500000
  | 1 => 62173/500000
  | 2 => 184067/1000000
  | 3 => 208197/1000000
  | 4 => 14413/50000
  | _ => 17819/250000

def rateL4 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 12429/125000
  | 1 => 119439/500000
  | 2 => 374021/1000000
  | 3 => 459127/1000000
  | 4 => 706769/1000000
  | _ => 907479/1000000

def trialL4 : TrialLaw 6 where
  weight := weightL4
  rate := rateL4
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weightL4]
  weight_sum := by simp [Fin.sum_univ_succ, weightL4]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rateL4]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rateL4]

def weightL5 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 15517/125000
  | 1 => 61949/500000
  | 2 => 35221/250000
  | 3 => 52589/250000
  | 4 => 207173/1000000
  | _ => 193553/1000000

def rateL5 (i : Fin 6) : ℚ :=
  match i.val with
  | 0 => 178367/1000000
  | 1 => 38141/125000
  | 2 => 412273/1000000
  | 3 => 25963/50000
  | 4 => 537129/1000000
  | _ => 97351/125000

def trialL5 : TrialLaw 6 where
  weight := weightL5
  rate := rateL5
  weight_nonneg := by intro i; fin_cases i <;> norm_num [weightL5]
  weight_sum := by simp [Fin.sum_univ_succ, weightL5]; norm_num
  rate_nonneg := by intro i; fin_cases i <;> norm_num [rateL5]
  rate_lt_one := by intro i; fin_cases i <;> norm_num [rateL5]

end KSatUpper.TrialData
