import Mathlib

/- This is a construction barrier for a^(n-1) c b^(n-1), not Olson's
   theorem for arbitrary words. No novelty is claimed. -/
namespace OlsonBoundary

variable {G : Type*} [Group G] [Fintype G]

def boundaryWord (a b c : G) : List G :=
  List.replicate (Fintype.card G - 1) a ++ [c] ++
    List.replicate (Fintype.card G - 1) b

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
      ys.length = Fintype.card G ∧ ys.prod = 1 := by
  classical
  have npos : 0 < Fintype.card G := Fintype.card_pos
  refine ⟨?_, ?_⟩
  · simp only [boundaryWord, List.length_append, List.length_replicate,
      List.length_singleton]
    omega
  · by_cases hsep : ∀ k : ℕ, 0 < k → k < Fintype.card G → a ^ k ≠ b ^ k
    · let f : Fin (Fintype.card G) → G := fun k => (a ^ k.val)⁻¹ * b ^ (k.val + 1)
      have hinj : Function.Injective f := by
        intro i j hij
        apply Fin.ext
        by_contra hne
        rcases lt_or_gt_of_ne hne with hlt | hgt
        · have hp := collision_power_eq a b i.val j.val (Nat.le_of_lt hlt) hij
          exact hsep (j.val - i.val) (by omega) (by omega) hp
        · have hp := collision_power_eq a b j.val i.val (Nat.le_of_lt hgt) hij.symm
          exact hsep (i.val - j.val) (by omega) (by omega) hp
      have hsurj : Function.Surjective f :=
        ((Fintype.bijective_iff_injective_and_card f).2 ⟨hinj, by simp⟩).2
      obtain ⟨k, hk⟩ := hsurj c
      let l := Fintype.card G - 1 - k.val
      have hkbound : k.val ≤ Fintype.card G - 1 := by omega
      have hlbound : l ≤ Fintype.card G - 1 := Nat.sub_le _ _
      have hkrep : (List.replicate k.val a).Sublist
          (List.replicate (Fintype.card G - 1) a) :=
        List.sublist_replicate_iff.mpr ⟨k.val, hkbound, rfl⟩
      have hlrep : (List.replicate l b).Sublist
          (List.replicate (Fintype.card G - 1) b) :=
        List.sublist_replicate_iff.mpr ⟨l, hlbound, rfl⟩
      refine ⟨List.replicate k.val a ++ [c] ++ List.replicate l b,
        (hkrep.append (List.Sublist.refl [c])).append hlrep, ?_, ?_⟩
      · simp only [List.length_append, List.length_replicate, List.length_singleton]
        dsimp [l]
        omega
      · simp only [List.prod_append, List.prod_replicate, List.prod_singleton]
        have hc : c = (a ^ k.val)⁻¹ * b ^ (k.val + 1) := hk.symm
        rw [hc]
        simp only [← mul_assoc, mul_inv_cancel, one_mul, ← pow_add]
        have hexp : k.val + 1 + l = Fintype.card G := by dsimp [l]; omega
        rw [hexp, pow_card_eq_one]
    · push_neg at hsep
      obtain ⟨k, hkpos, hklimit, hkeq⟩ := hsep
      let l := Fintype.card G - k
      have hkbound : k ≤ Fintype.card G - 1 := by omega
      have hlbound : l ≤ Fintype.card G - 1 := by dsimp [l]; omega
      have hkrep : (List.replicate k a).Sublist
          (List.replicate (Fintype.card G - 1) a) :=
        List.sublist_replicate_iff.mpr ⟨k, hkbound, rfl⟩
      have hlrep : (List.replicate l b).Sublist
          (List.replicate (Fintype.card G - 1) b) :=
        List.sublist_replicate_iff.mpr ⟨l, hlbound, rfl⟩
      refine ⟨List.replicate k a ++ List.replicate l b, ?_, ?_, ?_⟩
      · simpa only [List.append_nil] using
          (hkrep.append (List.nil_sublist [c])).append hlrep
      · simp only [List.length_append, List.length_replicate]
        dsimp [l]
        omega
      · simp only [List.prod_append, List.prod_replicate, hkeq, ← pow_add]
        have hexp : k + l = Fintype.card G := by dsimp [l]; omega
        rw [hexp, pow_card_eq_one]

#print OlsonBoundary.boundary_word_ordered_egz
#print axioms OlsonBoundary.boundary_word_ordered_egz

end OlsonBoundary
