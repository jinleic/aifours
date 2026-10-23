import McdKernel.Counts

/-!
# The lower bound `χ′(79) ≥ 40` over ALL Steiner triple systems on 79 points

Data-independent, from the counting lemmas of `McdKernel.Counts` (byte-identical copy of the
reviewed module): an STS on a 79-element type has `|S| * 3 = C(79, 2) = 3081`, i.e. 1027 blocks;
a partial parallel class of 3-subsets has at most `⌊79 / 3⌋ = 26` blocks; the classes of a
colouring have `∑ |P| = |S|`; and `39 * 26 = 1014 < 1027`.  So every colouring of every STS on
every 79-element type (any `DecidableEq` instance) has at least 40 colour classes.
-/

namespace Mcd.Counts

open Finset

universe u

variable {W : Type*} [Fintype W] [DecidableEq W]

/-- **Lower bound.**  Every colouring of an STS on a 79-element type has at least 40 classes. -/
theorem colour_lower_bound_79 (hW : Fintype.card W = 79) {S : Finset (Finset W)} (hS : IsSTS S)
    {C : Finset (Finset (Finset W))} (hC : IsColouring S C) : 40 ≤ C.card := by
  have h1 := card_sts_mul hS
  rw [hW] at h1
  have hc : Nat.choose 79 2 = 3081 := by decide
  have h2 := sum_card_colouring hC
  have h3 : ∀ P ∈ C, P.card ≤ 26 := by
    intro P hP
    have := card_ppc_mul_le hS.1 (hC.1 P hP)
    omega
  have h4 : ∑ P ∈ C, P.card ≤ ∑ _P ∈ C, 26 := Finset.sum_le_sum h3
  rw [Finset.sum_const_nat (fun _ _ => rfl), h2] at h4
  omega

/-- Every colouring of every STS on every 79-element type has at least 40 colour classes. -/
theorem colourLowerBound_79 : ColourLowerBound.{u} 79 40 :=
  fun _ _ _ hW _ hS _ hC => colour_lower_bound_79 hW hS hC

end Mcd.Counts
