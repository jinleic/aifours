import CpcwKernel.Target
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# The optimality bound (generic counting, data-free)

Nothing here mentions certificate data.

* `Cpcw.card_diffs`: `Cpcw.diffs B` has exactly `n * (k * (k - 1))` elements (with multiplicity).
* `Cpcw.IsCPCW.card_mul_le`: every family satisfying `Cpcw.IsCPCW` has
  `n * (k * (k - 1)) ≤ v - 1`, since its `n * (k * (k - 1))` ordered differences are nonzero
  residues, each occurring at most once.
* `Cpcw.IsCPCW.le_bound`: hence, for `2 ≤ k`, `n ≤ (v - 1) / (k * (k - 1))`.
* `Cpcw.not_exists_of_bound_lt`: for `2 ≤ k`, no family with more than
  `(v - 1) / (k * (k - 1))` codewords satisfies `Cpcw.IsCPCW`.
* `Cpcw.card_mul_eq_of_perfect`: if every nonzero residue occurs exactly once and `0` never
  (a perfect code, i.e. a cyclic difference family), then `n * (k * (k - 1)) = v - 1`.
-/

namespace Cpcw

theorem card_offDiag_fin (k : ℕ) :
    ((Finset.univ : Finset (Fin k × Fin k)).filter fun p => p.1 ≠ p.2).card = k * (k - 1) := by
  have e : ((Finset.univ : Finset (Fin k × Fin k)).filter fun p => p.1 ≠ p.2) =
      (Finset.univ : Finset (Fin k)).offDiag := by
    ext p
    simp
  rw [e, Finset.offDiag_card, Finset.card_univ, Fintype.card_fin, Nat.mul_sub_one]

theorem card_positions (n k : ℕ) :
    ((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).card =
      n * (k * (k - 1)) := by
  rw [← Finset.univ_product_univ, Finset.filter_product_right (fun p : Fin k × Fin k => p.1 ≠ p.2),
    Finset.card_product, Finset.card_univ, Fintype.card_fin, card_offDiag_fin]

theorem card_nonzero (v : ℕ) :
    ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card = v - 1 := by
  rcases Nat.eq_zero_or_pos v with rfl | hv
  · simp
  · have e : ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0) =
        Finset.univ.erase ⟨0, hv⟩ := by
      ext x
      simp [Fin.ext_iff]
    rw [e, Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]

/-- `Cpcw.diffs B` has `n * (k * (k - 1))` elements, counted with multiplicity. -/
theorem card_diffs {v k n : ℕ} (B : Fin n → Fin k → Fin v) :
    Multiset.card (diffs B) = n * (k * (k - 1)) := by
  rw [diffs, Multiset.card_map]
  exact card_positions n k

theorem sum_count_diffs {v k n : ℕ} (B : Fin n → Fin k → Fin v) :
    ∑ e : Fin v, (diffs B).count e = n * (k * (k - 1)) := by
  rw [Multiset.sum_count_eq_card fun a _ => Finset.mem_univ a, card_diffs]

/-- **Counting bound.**  A `(v, k, 1)` CPCW code with `n` codewords has
`n * (k * (k - 1)) ≤ v - 1`. -/
theorem IsCPCW.card_mul_le {v k n : ℕ} {B : Fin n → Fin k → Fin v} (h : IsCPCW B) :
    n * (k * (k - 1)) ≤ v - 1 := by
  have hle : ∑ e : Fin v, (diffs B).count e ≤
      ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card := by
    rw [Finset.card_filter]
    refine Finset.sum_le_sum fun e _ => ?_
    by_cases he : e.val = 0
    · rw [h.2.2 e he]
      exact Nat.zero_le _
    · rw [ite_eq_left he]
      exact h.2.1 e he
  rw [sum_count_diffs, card_nonzero] at hle
  exact hle

/-- **Optimality bound.**  For `2 ≤ k`, a `(v, k, 1)` CPCW code has at most
`⌊(v - 1) / (k (k - 1))⌋` codewords. -/
theorem IsCPCW.le_bound {v k n : ℕ} {B : Fin n → Fin k → Fin v} (hk : 2 ≤ k) (h : IsCPCW B) :
    n ≤ (v - 1) / (k * (k - 1)) := by
  have hpos : 0 < k * (k - 1) := Nat.mul_pos (by omega) (by omega)
  exact (Nat.le_div_iff_mul_le hpos).2 h.card_mul_le

/-- For `2 ≤ k`, no `(v, k, 1)` CPCW code has more than `⌊(v - 1) / (k (k - 1))⌋` codewords. -/
theorem not_exists_of_bound_lt {v k n : ℕ} (hk : 2 ≤ k) (hn : (v - 1) / (k * (k - 1)) < n) :
    ¬ ∃ B : Fin n → Fin k → Fin v, IsCPCW B := by
  rintro ⟨B, hB⟩
  exact absurd (hB.le_bound hk) (by omega)

/-- A perfect code (every nonzero residue exactly once, `0` never) has
`n * (k * (k - 1)) = v - 1`. -/
theorem card_mul_eq_of_perfect {v k n : ℕ} {B : Fin n → Fin k → Fin v}
    (h1 : ∀ d : Fin v, d.val ≠ 0 → (diffs B).count d = 1)
    (h0 : ∀ d : Fin v, d.val = 0 → (diffs B).count d = 0) :
    n * (k * (k - 1)) = v - 1 := by
  have hsum : ∑ e : Fin v, (diffs B).count e =
      ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card := by
    rw [Finset.card_filter]
    refine Finset.sum_congr rfl fun e _ => ?_
    by_cases he : e.val = 0
    · rw [h0 e he, ite_eq_right (not_not.2 he)]
    · rw [h1 e he, ite_eq_left he]
  rw [sum_count_diffs, card_nonzero] at hsum
  exact hsum

end Cpcw
