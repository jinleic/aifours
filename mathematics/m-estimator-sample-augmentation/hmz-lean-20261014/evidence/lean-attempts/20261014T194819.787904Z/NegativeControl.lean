import Mathlib.Probability.Moments.Variance
import Mathlib.Tactic.NormNum

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
