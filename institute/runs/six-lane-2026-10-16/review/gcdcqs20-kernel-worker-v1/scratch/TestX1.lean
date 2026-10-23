import Gc80.DataGcB
import Gc80.Check80

namespace Mcd.Kernel

theorem gc_groups_raw : groupsGc80 = (List.range 4).map fun i => List.range' (20 * i) 20 := by
  decide +kernel

theorem grp80_eq_raw {i : ℕ} (hi : i < 4) (y : Fin 80) :
    y ∈ grp80 i ↔ y.val ∈ groupsGc80.getD i [] := by
  rw [gc_groups_raw, mem_grp80, List.getD_eq_getElem?_getD, List.getElem?_map,
    List.getElem?_range hi]
  simp only [Option.map_some, Option.getD_some, List.mem_range'_1]

theorem mem_hole80 (x y : Fin 80) :
    y ∈ (grp80 (x.val / 20)).erase x ↔ groupHole 20 x.val y.val = true := by
  rw [Finset.mem_erase, mem_grp80]
  simp only [groupHole, Bool.and_eq_true, decide_eq_true_eq, Bool.not_eq_true',
    decide_eq_false_iff_not, ne_eq, Fin.ext_iff]
  omega

theorem card_grp80 {i : ℕ} (hi : i < 4) : (grp80 i).card = 20 := by
  rcases (by omega : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3) with rfl | rfl | rfl | rfl <;> decide +kernel

theorem card_univ_erase80 (x : Fin 80) : (Finset.univ.erase x).card = 79 := by
  rw [Finset.card_erase_of_mem (Finset.mem_univ x), Finset.card_univ, Fintype.card_fin]

theorem card_hole80 (x : Fin 80) : ((grp80 (x.val / 20)).erase x).card = 19 := by
  rw [Finset.card_erase_of_mem (mem_grp80_self x), card_grp80 (by omega)]

example (h : (10 : ℕ) = 10) : (10 : ℕ) = 40 - (79 - 19) / 2 := h

end Mcd.Kernel
