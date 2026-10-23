import KSatUpper.GeneralThreshold
import KSatUpper.Certificates
import KSatUpper.CertificatesK3
import Mathlib.Algebra.Order.Floor.Semifield

/-! Unconditional upper bounds for random 4-SAT at densities 249/25 = 9.96 and
4967/500 = 9.934, random 5-SAT at 1057/50 = 21.14 and 21123/1000 = 21.123, random 3-SAT at
2667/625 = 4.2672 and 213359/50000 = 4.26718, plus the 3-SAT regression control at
1067/250 = 4.268.

Each endpoint is `tendsto_zero_of_criterion` applied to a kernel-checked certificate. -/

open Filter

namespace KSatUpper

private theorem rate_le {f : Fin 3 → ℚ} {u : ℚ} (h0 : f 0 ≤ u) (h1 : f 1 ≤ u) (h2 : f 2 ≤ u) :
    ∀ i, f i ≤ u := by
  intro i
  fin_cases i <;> assumption

theorem psi4_le : Criterion.finiteAnalyticBound TrialData.trial4 3 ((249/25 : ℚ) : ℝ) 128 ≤
    -1/1000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialData.trial4 3 (249/25)
    (by norm_num) 128 64 (u := 7707/10000) (by norm_num)
    (rate_le (by norm_num [TrialData.trial4, TrialData.rate4])
      (by norm_num [TrialData.trial4, TrialData.rate4])
      (by norm_num [TrialData.trial4, TrialData.rate4])) (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialData.trial4 3 (249/25) 128 64 (7707/10000) : ℚ) : ℝ)
      ≤ ((-1/1000 : ℚ) : ℝ) := by exact_mod_cast Certificates.cert4
  push_cast at hc
  linarith

theorem psi5_le : Criterion.finiteAnalyticBound TrialData.trial5 4 ((1057/50 : ℚ) : ℝ) 128 ≤
    -1/2500 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialData.trial5 4 (1057/50)
    (by norm_num) 128 64 (u := 7344/10000) (by norm_num)
    (rate_le (by norm_num [TrialData.trial5, TrialData.rate5])
      (by norm_num [TrialData.trial5, TrialData.rate5])
      (by norm_num [TrialData.trial5, TrialData.rate5])) (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialData.trial5 4 (1057/50) 128 64 (7344/10000) : ℚ) : ℝ)
      ≤ ((-1/2500 : ℚ) : ℝ) := by exact_mod_cast Certificates.cert5
  push_cast at hc
  linarith

theorem psi3_le : Criterion.finiteAnalyticBound TrialData.trial3 2 ((1067/250 : ℚ) : ℝ) 128 ≤
    -1/100000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialData.trial3 2 (1067/250)
    (by norm_num) 128 64 (u := 17/20) (by norm_num)
    (rate_le (by norm_num [TrialData.trial3, TrialData.rate3])
      (by norm_num [TrialData.trial3, TrialData.rate3])
      (by norm_num [TrialData.trial3, TrialData.rate3])) (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialData.trial3 2 (1067/250) 128 64 (17/20) : ℚ) : ℝ)
      ≤ ((-1/100000 : ℚ) : ℝ) := by exact_mod_cast Certificates.cert3
  push_cast at hc
  linarith

private theorem floor_eq {q : ℚ} {a b : ℕ} (hq : (q : ℝ) = (a : ℝ) / (b : ℝ)) (n : ℕ) :
    ⌊(q : ℝ) * n⌋₊ = a*n/b := by
  have h := Nat.floor_div_eq_div (K := ℝ) (a*n) b
  have he : (q : ℝ) * n = ((a*n : ℕ) : ℝ) / (b : ℝ) := by
    rw [hq]
    push_cast
    ring
  rw [he, h]

/-- Random 4-SAT with `⌊9.96 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one. -/
theorem satisfiabilityProbability_4SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (249*n/25)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialData.trial4 3 (α := ((249/25 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psi4_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 4 n (249*n/25)) =
      fun n : ℕ => satisfiabilityProbability (3 + 1) n ⌊((249/25 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 249) (b := 25) (by norm_num)]
  rw [hf]
  exact h

/-- Random 5-SAT with `⌊21.14 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one. -/
theorem satisfiabilityProbability_5SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (1057*n/50)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialData.trial5 4 (α := ((1057/50 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psi5_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 5 n (1057*n/50)) =
      fun n : ℕ => satisfiabilityProbability (4 + 1) n ⌊((1057/50 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 1057) (b := 50) (by norm_num)]
  rw [hf]
  exact h

/-- Regression control: the general-arity route reproduces the 3-SAT endpoint of
yamelton/sat-upper-4268 at `⌊4.268 n⌋` in this development's own model. -/
theorem satisfiabilityProbability_3SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (1067*n/250)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialData.trial3 2 (α := ((1067/250 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psi3_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 3 n (1067*n/250)) =
      fun n : ℕ => satisfiabilityProbability (2 + 1) n ⌊((1067/250 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 1067) (b := 250) (by norm_num)]
  rw [hf]
  exact h

theorem psiL4_le : Criterion.finiteAnalyticBound TrialData.trialL4 3 ((4967/500 : ℚ) : ℝ) 128 ≤
    -1/20000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialData.trialL4 3 (4967/500)
    (by norm_num) 128 64 (u := 907479/1000000) (by norm_num)
    (by intro i; fin_cases i <;> norm_num [TrialData.trialL4, TrialData.rateL4]) (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialData.trialL4 3 (4967/500) 128 64
      (907479/1000000) : ℚ) : ℝ) ≤ ((-1/20000 : ℚ) : ℝ) := by exact_mod_cast Certificates.certL4
  push_cast at hc
  linarith

theorem psiL5_le : Criterion.finiteAnalyticBound TrialData.trialL5 4 ((21123/1000 : ℚ) : ℝ) 128 ≤
    -1/100000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialData.trialL5 4 (21123/1000)
    (by norm_num) 128 64 (u := 97351/125000) (by norm_num)
    (by intro i; fin_cases i <;> norm_num [TrialData.trialL5, TrialData.rateL5]) (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialData.trialL5 4 (21123/1000) 128 64
      (97351/125000) : ℚ) : ℝ) ≤ ((-1/100000 : ℚ) : ℝ) := by exact_mod_cast Certificates.certL5
  push_cast at hc
  linarith

/-- Random 4-SAT with `⌊9.934 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one (continuation law L4, `T = 128`). -/
theorem satisfiabilityProbability_4SAT_9934_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (4967*n/500)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialData.trialL4 3 (α := ((4967/500 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psiL4_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 4 n (4967*n/500)) =
      fun n : ℕ => satisfiabilityProbability (3 + 1) n ⌊((4967/500 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 4967) (b := 500) (by norm_num)]
  rw [hf]
  exact h

/-- Random 5-SAT with `⌊21.123 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one (continuation law L5, `T = 128`). -/
theorem satisfiabilityProbability_5SAT_21123_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (21123*n/1000)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialData.trialL5 4 (α := ((21123/1000 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psiL5_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 5 n (21123*n/1000)) =
      fun n : ℕ => satisfiabilityProbability (4 + 1) n ⌊((21123/1000 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 21123) (b := 1000) (by norm_num)]
  rw [hf]
  exact h

theorem psiK3_42672_le :
    Criterion.finiteAnalyticBound TrialDataK3.trialT128 2 ((2667/625 : ℚ) : ℝ) 128 ≤
      -1/500000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialDataK3.trialT128 2 (2667/625)
    (by norm_num) 128 256 (u := 239949/250000) (by norm_num)
    (by intro i; fin_cases i <;> norm_num [TrialDataK3.trialT128, TrialDataK3.rateT128])
    (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialDataK3.trialT128 2 (2667/625) 128 256
      (239949/250000) : ℚ) : ℝ) ≤ ((-1/500000 : ℚ) : ℝ) := by
    exact_mod_cast CertificatesK3.cert_42672
  push_cast at hc
  linarith

theorem psiK3_426718_le :
    Criterion.finiteAnalyticBound TrialDataK3.trialT128 2 ((213359/50000 : ℚ) : ℝ) 128 ≤
      -1/2000000 := by
  have h := NumericalCriterion.finiteAnalyticBound_le_cert TrialDataK3.trialT128 2
    (213359/50000) (by norm_num) 128 256 (u := 239949/250000) (by norm_num)
    (by intro i; fin_cases i <;> norm_num [TrialDataK3.trialT128, TrialDataK3.rateT128])
    (by norm_num)
  have hc : ((NumericalCriterion.certUpper TrialDataK3.trialT128 2 (213359/50000) 128 256
      (239949/250000) : ℚ) : ℝ) ≤ ((-1/2000000 : ℚ) : ℝ) := by
    exact_mod_cast CertificatesK3.cert_426718
  push_cast at hc
  linarith

/-- Random 3-SAT with `⌊4.2672 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one (six-atom law `TrialDataK3.trialT128`, `T = 128`). -/
theorem satisfiabilityProbability_3SAT_42672_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialDataK3.trialT128 2 (α := ((2667/625 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psiK3_42672_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) =
      fun n : ℕ => satisfiabilityProbability (2 + 1) n ⌊((2667/625 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 2667) (b := 625) (by norm_num)]
  rw [hf]
  exact h

/-- Random 3-SAT with `⌊4.26718 n⌋` iid uniform legal signed clauses is unsatisfiable with
probability tending to one (six-atom law `TrialDataK3.trialT128`, `T = 128`). -/
theorem satisfiabilityProbability_3SAT_426718_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (213359*n/50000)) atTop (nhds 0) := by
  have h := tendsto_zero_of_criterion TrialDataK3.trialT128 2 (α := ((213359/50000 : ℚ) : ℝ))
    (by norm_num) 128 (by linarith [psiK3_426718_le])
  have hf : (fun n : ℕ => satisfiabilityProbability 3 n (213359*n/50000)) =
      fun n : ℕ => satisfiabilityProbability (2 + 1) n ⌊((213359/50000 : ℚ) : ℝ) * n⌋₊ := by
    funext n
    rw [floor_eq (a := 213359) (b := 50000) (by norm_num)]
  rw [hf]
  exact h

end KSatUpper
