import Mathlib.Data.Finset.Powerset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Union
#check @Finset.card_biUnion
#check @Finset.sum_const_nat
#check @Finset.card_powersetCard
#check @Finset.mem_powersetCard
#check @Finset.notMem_erase
#check @Finset.card_erase_of_mem
#check @Finset.disjoint_left
#check @Fintype.card_fin
example : Nat.choose 52 3 = 22100 := by decide +kernel
example : Nat.choose 51 2 = 1275 := by decide +kernel
example : Nat.choose 76 3 = 70300 := by decide +kernel
example : Nat.choose 4 3 = 4 := by decide
