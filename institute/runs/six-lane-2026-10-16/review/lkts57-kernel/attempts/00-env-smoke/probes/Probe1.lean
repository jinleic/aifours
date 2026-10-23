import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Prod

#check @Fintype.card_finset_len
#check @Finset.card_eq_three
#check @List.Pairwise.forall
#check @List.pairwise_iff_getElem
#check @Nat.testBit_or
#check @Nat.testBit_and
#check @Nat.testBit_two_pow
#check @Nat.eq_of_testBit_eq
#check @Nat.zero_testBit
#check @Nat.testBit_two_pow_sub_one
#check @Fintype.bijective_iff_injective_and_card
#check @List.pairwise_flatten
#check @List.mem_flatten
#check @List.getElem_mem
#check @List.foldl_cons

def tst : Nat := (2 ^ 100 ||| 2 ^ 3) &&& 8

theorem tst_ok : tst = 8 := by decide +kernel
#print axioms tst_ok
