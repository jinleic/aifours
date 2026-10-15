import Mathlib.Data.Finset.Card

namespace AI4SComparatorProbe

theorem disjoint_union_card (s t : Finset ℕ) (h : Disjoint s t) :
    (s ∪ t).card ≤ s.card + t.card := Finset.card_union_le s t

end AI4SComparatorProbe
