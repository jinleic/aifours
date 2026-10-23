import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Data.ZMod.Defs
#check @List.nodup_append
#check @List.nodup_cons
#check @List.flatMap_cons
#check @List.not_mem_nil
#check @List.mem_nil_iff
#check @Nat.zero_testBit
#check @Fin.val_zero
#check @Fin.val_ne_of_ne
#check @List.flatMap_id
#check @List.flatten_eq_flatMap
#check @Finset.map_eq_image
#check @add_eq_right
#check @eq_neg_of_add_eq_zero_left
#check @eq_sub_of_add_eq
#check @List.exists_mem_of_ne_nil
#check @Finset.card_insert_of_notMem
#check @Finset.notMem_singleton
example (v : ℕ) [NeZero v] (a b : Fin v) : a * (b + a) = a * b + a * a := mul_add _ _ _
example : ((0 : Fin 52) - 5).val = 47 := by decide +kernel
#synth Neg (Fin 52)
