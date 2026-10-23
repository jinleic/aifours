import Mathlib.Probability.ProbabilityMassFunction.Constructions
import Mathlib.Data.ENNReal.BigOperators

/-! Finite trial warning laws with arbitrary rational weights: the definitions that appear in
the statement of the general theorem.

This replaces the hard-coded four equally likely labels of `SatUpper/Obligations.lean`
(yamelton/sat-upper-4268). A label `i : Fin p` has probability `weight i` and Bernoulli
warning rate `rate i ∈ [0,1)`. The measure-theoretic facts are in `KSatUpper.Trial`. -/

open MeasureTheory
open scoped ENNReal

namespace KSatUpper

structure TrialLaw (p : ℕ) where
  weight : Fin p → ℚ
  rate : Fin p → ℚ
  weight_nonneg : ∀ i, 0 ≤ weight i
  weight_sum : ∑ i, weight i = 1
  rate_nonneg : ∀ i, 0 ≤ rate i
  rate_lt_one : ∀ i, rate i < 1

namespace TrialLaw

variable {p : ℕ} (T : TrialLaw p)

theorem weight_nonneg_real (i : Fin p) : (0 : ℝ) ≤ T.weight i := by
  exact_mod_cast T.weight_nonneg i

theorem weight_sum_real : ∑ i, (T.weight i : ℝ) = 1 := by
  exact_mod_cast T.weight_sum

noncomputable def pmf : PMF (Fin p) :=
  PMF.ofFintype (fun i => ENNReal.ofReal (T.weight i)) (by
    rw [← ENNReal.ofReal_sum_of_nonneg (fun i _ => T.weight_nonneg_real i), T.weight_sum_real,
      ENNReal.ofReal_one])

/-- The label law. -/
noncomputable def law : Measure (Fin p) := T.pmf.toMeasure

instance : IsProbabilityMeasure T.law := by
  unfold law
  infer_instance

/-- Exact rate moments `C_h = E R^h`. -/
def moment (h : ℕ) : ℚ := ∑ i, T.weight i * T.rate i ^ h

/-- Binomial coefficients through factorials, which the kernel evaluates in linear time. -/
def binom (j t : ℕ) : ℕ := j.factorial / (t.factorial * (j - t).factorial)

/-- `nu_j = E (1 - ∏_{l<m} R_l)^j`, in exact rational form (proved in `Trial`). -/
def markMoment (m j : ℕ) : ℚ :=
  ∑ t ∈ Finset.range (j + 1), (-1 : ℚ) ^ t * (binom j t : ℚ) * T.moment t ^ m

end TrialLaw

end KSatUpper
