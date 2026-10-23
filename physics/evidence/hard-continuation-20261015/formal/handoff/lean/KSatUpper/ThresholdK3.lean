import KSatUpper.GeneralThreshold
import KSatUpper.CertificatesK3
import Mathlib.Algebra.Order.Floor.Semifield

/-! Random 3-SAT endpoints below 4.268, at densities 2667/625 = 4.2672 and
213359/50000 = 4.26718.

Each endpoint is `tendsto_zero_of_criterion` applied to a certificate of `CertificatesK3`, which is
assembled from bounded kernel checks. The import closure of this module contains no monolithic
certificate `decide` (in particular not `KSatUpper.Certificates`). -/

open Filter

namespace KSatUpper

private theorem floor_eq_k3 {q : ℚ} {a b : ℕ} (hq : (q : ℝ) = (a : ℝ) / (b : ℝ)) (n : ℕ) :
    ⌊(q : ℝ) * n⌋₊ = a*n/b := by
  have h := Nat.floor_div_eq_div (K := ℝ) (a*n) b
  have he : (q : ℝ) * n = ((a*n : ℕ) : ℝ) / (b : ℝ) := by
    rw [hq]
    push_cast
    ring
  rw [he, h]

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
    rw [floor_eq_k3 (a := 2667) (b := 625) (by norm_num)]
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
    rw [floor_eq_k3 (a := 213359) (b := 50000) (by norm_num)]
  rw [hf]
  exact h

end KSatUpper
