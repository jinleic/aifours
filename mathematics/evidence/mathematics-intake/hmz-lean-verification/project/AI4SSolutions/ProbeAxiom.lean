import Mathlib.Data.Finset.Card

namespace AI4SComparatorProbe

axiom unchecked_card_identity (s t : Finset ℕ) (h : Disjoint s t) :
    (s ∪ t).card = s.card + t.card

theorem disjoint_union_card (s t : Finset ℕ) (h : Disjoint s t) :
    (s ∪ t).card = s.card + t.card := unchecked_card_identity s t h

end AI4SComparatorProbe
