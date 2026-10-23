import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.ZMod.Defs
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Logic.Equiv.Basic

#check @List.flatten
#check @List.mem_flatten
#check @List.nodup_flatten
#check @List.flatMap
#check @List.nodup_flatMap
#check @List.mem_flatMap
#check @List.Pairwise.forall
#check @Finset.map_erase
#check @Finset.map_insert
#check @Finset.mem_map_equiv
#check @Finset.map_map
#check @Finset.map_injective
#check @Equiv.addRight
#check @Equiv.addRight_symm
#check @Equiv.coe_addRight
#check @Nat.testBit_or
#check @Nat.testBit_shiftLeft
#check @Nat.testBit_two_pow
#check @Finset.card_eq_two
#check @Finset.card_eq_three
#check @Finset.eq_of_subset_of_card_le
#check @Finset.card_image_of_injective
#check @Fin.instCommRing
#check (inferInstance : CommRing (Fin 52))
#check (inferInstance : AddCommGroup (Fin 52))
example : (3 : Fin 52) + 50 = 1 := by decide +kernel
example : ((3 : Fin 52) - 5).val = 50 := by decide +kernel
example : ((23 : Fin 52) * 43) = 1 := by decide +kernel
example (a b : Fin 52) : (a + b).val = (a.val + b.val) % 52 := Fin.val_add a b
example (a : Fin 52) : (-a).val = (52 - a.val) % 52 := by simp [Fin.neg_def]  
#check @List.range
#print List.range
#check @Nat.testBit
#print Nat.testBit
