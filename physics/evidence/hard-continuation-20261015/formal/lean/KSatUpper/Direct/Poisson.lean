import KSatUpper.BinomialPoisson

/-! A Poisson endpoint comparison from finite binomial replacements, arity `m+1`.

Derived from `SatUpper/Direct/Poisson.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory ProbabilityTheory Set
open scoped NNReal

namespace KSatUpper.DirectPoisson

theorem zero_law : poissonMeasure 0 = Measure.dirac 0 := by
  apply Measure.ext_of_singleton
  intro K
  rw [poissonMeasure, PMF.toMeasure_apply_singleton _ _ (measurableSet_singleton K)]
  change ENNReal.ofReal (poissonPMFReal 0 K) = _
  cases K <;> simp [poissonPMFReal]

noncomputable def expectation (f : ℕ → ℕ → ℝ) (r s : ℝ≥0) : ℝ :=
  ∫ K, ∫ L, f K L ∂poissonMeasure s ∂poissonMeasure r

variable {f : ℕ → ℕ → ℝ} {C : ℝ}

theorem integrable_row (hS : ∀ K L, ‖f K (L+1)-f K L‖ ≤ C) (s : ℝ≥0) (K : ℕ) :
    Integrable (f K) (poissonMeasure s) :=
  PoissonExpectation.integrable_poisson_of_linear_growth
    (PoissonExpectation.linear_growth_of_bounded_increments (hS K)) s

/-- Replace a site by a clause with probability `1/(m+1)` and an empty slot otherwise. -/
theorem comparison {m : ℕ} (hC : ∀ K L, ‖f (K+1) L-f K L‖ ≤ C)
    (hS : ∀ K L, ‖f K (L+1)-f K L‖ ≤ C) {d : ℝ}
    (h : ∀ K L, f (K+1) L-f K L - ((m : ℝ)+1)*(f K (L+1)-f K L) + (m : ℝ)*d ≤ 0)
    (a : ℝ≥0) :
    expectation f a 0 ≤ expectation f 0 (((m : ℝ≥0)+1)*a) - (m : ℝ)*a*d := by
  have hc := BinomialPoisson.comparison (m := m) (d := d) hC hS
    (fun K L => by have hk := h K L; ring_nf at hk ⊢; linarith) a
  have hgC := PoissonExpectation.linear_growth_of_bounded_increments
    (f := fun K => f K 0) (fun K => hC K 0)
  have hgS := PoissonExpectation.linear_growth_of_bounded_increments (hS 0)
  have hs := PoissonExpectation.poissonExpectation_eq_integral hgS (((m : ℝ≥0)+1)*a)
  simp only [NNReal.coe_mul, NNReal.coe_add, NNReal.coe_natCast, NNReal.coe_one] at hs hc
  rw [PoissonExpectation.poissonExpectation_eq_integral hgC a, hs] at hc
  simpa only [expectation, zero_law, integral_dirac] using hc

end KSatUpper.DirectPoisson
