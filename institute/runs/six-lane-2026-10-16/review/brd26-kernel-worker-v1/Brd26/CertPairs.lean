import Brd26.Target
import Brd26.Witness

/-!
# Kernel evaluations: signed pair counts of `brdM`

The 26 × 25 ordered pairs of distinct rows are split by the first row `i` into the blocks
`[0, 4), [4, 8), [8, 12), [12, 16), [16, 20), [20, 24), [24, 26)`; one `decide +kernel` declaration per
block (each a separate kernel evaluation of the Mathlib `Decidable` instances; this bounds the
kernel memory of one declaration).  Every block statement quantifies over all `i i' : Fin 26`; the
block bounds only skip the rows `i` outside the block.  No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Brd26

/-- Kernel evaluation, first row `i` in `[0, 4)`. -/
theorem brdM_pairs_0 : ∀ i i' : Fin 26, 0 ≤ i.val → i.val < 4 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[4, 8)`. -/
theorem brdM_pairs_1 : ∀ i i' : Fin 26, 4 ≤ i.val → i.val < 8 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[8, 12)`. -/
theorem brdM_pairs_2 : ∀ i i' : Fin 26, 8 ≤ i.val → i.val < 12 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[12, 16)`. -/
theorem brdM_pairs_3 : ∀ i i' : Fin 26, 12 ≤ i.val → i.val < 16 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[16, 20)`. -/
theorem brdM_pairs_4 : ∀ i i' : Fin 26, 16 ≤ i.val → i.val < 20 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[20, 24)`. -/
theorem brdM_pairs_5 : ∀ i i' : Fin 26, 20 ≤ i.val → i.val < 24 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Kernel evaluation, first row `i` in `[24, 26)`. -/
theorem brdM_pairs_6 : ∀ i i' : Fin 26, 24 ≤ i.val → i.val < 26 → i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

/-- Every two distinct rows `i ≠ i'` of `brdM` have exactly two columns with product `+1` and exactly
two columns with product `-1` (assembled from the seven kernel evaluations above). -/
theorem brdM_pairs : ∀ i i' : Fin 26, i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  intro i i' h
  have hi := i.isLt
  by_cases h0 : i.val < 4
  · exact brdM_pairs_0 i i' (by omega) h0 h
  by_cases h1 : i.val < 8
  · exact brdM_pairs_1 i i' (by omega) h1 h
  by_cases h2 : i.val < 12
  · exact brdM_pairs_2 i i' (by omega) h2 h
  by_cases h3 : i.val < 16
  · exact brdM_pairs_3 i i' (by omega) h3 h
  by_cases h4 : i.val < 20
  · exact brdM_pairs_4 i i' (by omega) h4 h
  by_cases h5 : i.val < 24
  · exact brdM_pairs_5 i i' (by omega) h5 h
  exact brdM_pairs_6 i i' (by omega) (by omega) h

end Brd26
