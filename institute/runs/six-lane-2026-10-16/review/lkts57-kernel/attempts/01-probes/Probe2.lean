import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.Prod

#check @List.getD_eq_getElem
#check @List.mem_iff_getElem
#check @Finset.card_eq_two
#check @Nat.mul_add_div
#check @Nat.mul_add_mod
#check @Fintype.card_prod
#check @Fintype.card_fin
#check @List.mem_flatMap
#check @List.mem_filter
#check @List.all_eq_true
#check @beq_iff_eq
#check @List.getElem_map
#check @Set.disjoint_left
#check @Set.eq_univ_of_forall
#check @Set.mem_iUnion
#check @List.Pairwise.cons
#check @Finset.pair_comm
#check @Finset.insert_subset_iff
#check @Fin.ext_iff
#check @Nat.div_add_mod
#check @Nat.lt_mul_div_succ
#check @Nat.div_mul_le_self

example (a b c a' b' c' : Nat) (h1 : a < b) (h2 : b < c) (h1' : a' < b') (h2' : b' < c')
    (e1 : a = a' ∨ a = b' ∨ a = c') (e2 : b = a' ∨ b = b' ∨ b = c') (e3 : c = a' ∨ c = b' ∨ c = c')
    (f1 : a' = a ∨ a' = b ∨ a' = c) (f2 : b' = a ∨ b' = b ∨ b' = c) (f3 : c' = a ∨ c' = b ∨ c' = c) :
    a = a' ∧ b = b' ∧ c = c' := by
  omega

example (v x : Nat) (h : x < 3) (hv : v * x + 1 = 5) : x < 3 := by omega

theorem chooseTest : (57 - 2) * ((57 - 1) / 2 * (57 / 3)) = Nat.choose 57 3 := by decide +kernel
theorem chooseTest87 : (87 - 2) * ((87 - 1) / 2 * (87 / 3)) = Nat.choose 87 3 := by decide +kernel
#print axioms chooseTest
