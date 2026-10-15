import Mathlib.Probability.Moments.Variance
import Mathlib.Tactic.NormNum
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Numerical-constant negative control for bernoulli_frobenius_expectation_le.
Take one row z = 1, dimension 1, leverage bound d = 1, q = 1/2.
There is no independence condition to drop for a singleton row family.
For a fair binary observation the centered Frobenius square is always 1/4.
The positive bound q(1-q) d p = 1/4 is sharp. This deliberately false
variant divides the positive bound by two, incorrectly asserting 1/8.
The mean assumption is satisfiable (the uniform probability law on Bool).
The intended rejection is the final false real inequality, not an import,
unresolved identifier, or malformed Lean expression.
-/

open MeasureTheory
noncomputable section

namespace ReplicationNegative

def binaryObservation (b : Bool) : ℝ := if b then 1 else 0

theorem wrong_half_frobenius_constant (μ : Measure Bool) [IsProbabilityMeasure μ]
    (hmean : ∫ b, binaryObservation b ∂μ = (1 / 2 : ℝ)) :
    (∫ b, (binaryObservation b - (1 / 2 : ℝ)) ^ 2 ∂μ) ≤
      ((1 / 2 : ℝ) * (1 - 1 / 2) * 1 * 1) / 2 := by
  have hconst : (fun b => (binaryObservation b - (1 / 2 : ℝ)) ^ 2) =
      fun _ : Bool => (1 / 4 : ℝ) := by
    funext b
    cases b <;> norm_num [binaryObservation]
  rw [hconst, integral_const]
  simp only [probReal_univ, smul_eq_mul, one_mul]
  norm_num

end ReplicationNegative

namespace RippleNegative

def score (eta r : ℝ) : ℝ := r + eta * Real.sin (Real.pi * r)

-- Wrong-conclusion variant of ripple_profile_half_score: integer cancellation
-- cannot be extended to the half-integer produced by independent pooling.
theorem wrong_half_integer_cancellation {eta : ℝ} (heta : 0 < eta) :
    4 * score eta (1 / 2) - 2 * score eta 1 = 0 := by
  have hhalf : Real.pi * (1 / 2 : ℝ) = Real.pi / 2 := by ring
  norm_num [score, hhalf, Real.sin_pi_div_two, Real.sin_pi]
  linarith

end RippleNegative
