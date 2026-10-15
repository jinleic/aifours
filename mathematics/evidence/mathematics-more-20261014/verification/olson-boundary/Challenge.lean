import Mathlib

/- This is a construction barrier for a^(n-1) c b^(n-1), not Olson's
   theorem for arbitrary words. No novelty is claimed. -/
namespace OlsonBoundary

variable {G : Type*} [Group G] [Fintype G]

def boundaryWord (a b c : G) : List G :=
  List.replicate (Fintype.card G - 1) a ++ [c] ++
    List.replicate (Fintype.card G - 1) b

omit [Fintype G] in
private theorem collision_power_eq (a b : G) (i j : ℕ) (hij : i ≤ j)
    (h : (a ^ i)⁻¹ * b ^ (i + 1) = (a ^ j)⁻¹ * b ^ (j + 1)) :
    a ^ (j - i) = b ^ (j - i) := by
  apply mul_right_cancel (b := b ^ (i + 1))
  calc
    a ^ (j - i) * b ^ (i + 1) =
        (a ^ j * (a ^ i)⁻¹) * b ^ (i + 1) := by rw [pow_sub a hij]
    _ = a ^ j * ((a ^ i)⁻¹ * b ^ (i + 1)) := mul_assoc _ _ _
    _ = a ^ j * ((a ^ j)⁻¹ * b ^ (j + 1)) := by rw [h]
    _ = b ^ (j + 1) := by simp only [← mul_assoc, mul_inv_cancel, one_mul]
    _ = b ^ (j - i) * b ^ (i + 1) := by
      rw [← pow_add]
      congr 1
      omega

/-- Every finite group and arbitrary a,b,c obey ordered EGZ for this
    specific three-block word of length exactly 2|G|-1. -/
theorem boundary_word_ordered_egz (a b c : G) :
    (boundaryWord a b c).length = 2 * Fintype.card G - 1 ∧
    ∃ ys : List G, ys.Sublist (boundaryWord a b c) ∧
      ys.length = Fintype.card G ∧ ys.prod = 1 := by sorry

end OlsonBoundary
