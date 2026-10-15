import Mathlib.Algebra.Lie.Matrix
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

set_option Elab.async false

/-!
An actual rational sl2 triple on its standard two-dimensional module.
The last declaration changes the sign in D(e v) = -a v to +a v.
All four necessary relations are checked first. The changed conclusion is
also explicitly disproved. The final proof application must be rejected.
-/

namespace SerreNegative

attribute [local instance] LieRing.ofAssociativeRing

abbrev Mat := Matrix (Fin 2) (Fin 2) ℚ
abbrev Vec := Fin 2 → ℚ

def h : Mat := !![1, 0; 0, -1]
def e : Mat := !![0, 1; 0, 0]
def f : Mat := !![0, 0; 1, 0]
def v : Vec := ![0, 1]

theorem triple_and_vector_relations :
    ⁅h, e⁆ = (2 : ℚ) • e ∧ ⁅f, e⁆ = -h ∧
      ⁅h, v⁆ = (-1 : ℚ) • v ∧ ⁅f, v⁆ = 0 := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [h, e, Ring.lie_def, Matrix.mul_apply, Fin.sum_univ_two]
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [h, e, f, Ring.lie_def, Matrix.mul_apply, Fin.sum_univ_two]
  constructor
  · ext i
    fin_cases i <;>
      norm_num [h, v, Matrix.lie_apply, Matrix.mulVec, dotProduct, Fin.sum_univ_two]
  · ext i
    fin_cases i <;>
      norm_num [f, v, Matrix.lie_apply, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

theorem actual_base_recurrence : ⁅f, ⁅e, v⁆⁆ = (1 : ℚ) • v := by
  ext i
  fin_cases i <;>
    norm_num [f, e, v, Matrix.lie_apply, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

theorem altered_sign_is_false : ¬ (⁅f, ⁅e, v⁆⁆ = (-1 : ℚ) • v) := by
  intro bad
  have bad_component := congrArg (fun w : Vec => w 1) bad
  norm_num [f, e, v, Matrix.lie_apply, Matrix.mulVec, dotProduct,
    Fin.sum_univ_two] at bad_component

#print SerreNegative.triple_and_vector_relations
#print axioms SerreNegative.triple_and_vector_relations
#print SerreNegative.actual_base_recurrence
#print axioms SerreNegative.actual_base_recurrence
#print SerreNegative.altered_sign_is_false
#print axioms SerreNegative.altered_sign_is_false

-- Deliberately invalid: a=-1, so +a is -1 while -a is +1.
theorem deliberately_altered_recurrence : ⁅f, ⁅e, v⁆⁆ = (-1 : ℚ) • v := by
  exact actual_base_recurrence

end SerreNegative
