import McdKernel.Target
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Finset.Union
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# The lower bound on the number of colours, and `χ′(37) = 19` from a witness

Nothing here mentions data.  For a finite point type `W` (`n = card W`):

* `card_sts_mul`: an STS has `|S| * 3 = C(n, 2)` blocks (the 2-subsets of the blocks partition
  all 2-subsets);
* `card_ppc_mul_le`: a partial parallel class of 3-subsets has `|P| * 3 ≤ n` (its blocks are
  pairwise disjoint);
* `sum_card_colouring`: the colour classes of a colouring of `D` have `∑ |P| = |D|`;
* `colourLowerBound_37`: every colouring of every STS on every 37-element type has at least
  19 classes (`|S| = 222`, each class has at most 12 blocks, `12 * 18 < 222`);
* `chiPrime_eq_of`: if every colouring of every STS on `Fin n` has at least `r` classes and some
  STS on `Fin n` has an `r`-colouring, then `χ′(n) = r`.
-/

namespace Mcd.Counts

open Finset

variable {W : Type*} [Fintype W] [DecidableEq W]

/-- An STS has `|S| * 3 = C(n, 2)` blocks. -/
theorem card_sts_mul {S : Finset (Finset W)} (h : IsSTS S) :
    S.card * 3 = (Fintype.card W).choose 2 := by
  have hcover : S.biUnion (fun T => T.powersetCard 2) = (Finset.univ : Finset W).powersetCard 2 := by
    ext P
    simp only [Finset.mem_biUnion, Finset.mem_powersetCard, Finset.subset_univ, true_and]
    constructor
    · rintro ⟨T, -, -, hP⟩
      exact hP
    · intro hP
      obtain ⟨T, ⟨hT, hPT⟩, -⟩ := h.2 P hP
      exact ⟨T, hT, hPT, hP⟩
  have hdisj : (S : Set (Finset W)).PairwiseDisjoint fun T => T.powersetCard 2 := by
    intro T hT T' hT' hne
    simp only [Function.onFun]
    rw [Finset.disjoint_left]
    intro P hPT hPT'
    rw [Finset.mem_powersetCard] at hPT hPT'
    obtain ⟨U, -, hU⟩ := h.2 P hPT.2
    exact hne ((hU T ⟨hT, hPT.1⟩).trans (hU T' ⟨hT', hPT'.1⟩).symm)
  have hcard := Finset.card_biUnion hdisj
  rw [hcover, Finset.card_powersetCard, Finset.card_univ] at hcard
  rw [hcard, Finset.sum_const_nat]
  intro T hT
  rw [Finset.card_powersetCard, h.1 T hT]
  rfl

/-- A partial parallel class of 3-subsets has `|P| * 3 ≤ n` blocks. -/
theorem card_ppc_mul_le {D P : Finset (Finset W)} (hD : ∀ T ∈ D, T.card = 3) (hP : IsPPC D P) :
    P.card * 3 ≤ Fintype.card W := by
  obtain ⟨-, hsub, hdisj⟩ := hP
  have hpd : (P : Set (Finset W)).PairwiseDisjoint id := by
    intro T hT T' hT' hne
    exact hdisj T hT T' hT' hne
  have hcard := Finset.card_biUnion hpd
  simp only [id] at hcard
  rw [Finset.sum_const_nat (fun T hT => hD T (hsub hT))] at hcard
  rw [← hcard, ← Finset.card_univ]
  exact Finset.card_le_card (Finset.subset_univ _)

omit [Fintype W] in
/-- The colour classes of a colouring of `D` have `∑ |P| = |D|`. -/
theorem sum_card_colouring {D : Finset (Finset W)} {C : Finset (Finset (Finset W))}
    (h : IsColouring D C) : ∑ P ∈ C, P.card = D.card := by
  have hcover : C.biUnion id = D := by
    ext T
    simp only [Finset.mem_biUnion, id]
    constructor
    · rintro ⟨P, hP, hTP⟩
      exact (h.1 P hP).2.1 hTP
    · intro hT
      obtain ⟨P, ⟨hP, hTP⟩, -⟩ := h.2 T hT
      exact ⟨P, hP, hTP⟩
  have hdisj : (C : Set (Finset (Finset W))).PairwiseDisjoint id := by
    intro P hP P' hP' hne
    simp only [Function.onFun, id]
    rw [Finset.disjoint_left]
    intro T hTP hTP'
    obtain ⟨Q, -, hQ⟩ := h.2 T ((h.1 P hP).2.1 hTP)
    exact hne ((hQ P ⟨hP, hTP⟩).trans (hQ P' ⟨hP', hTP'⟩).symm)
  have hcard := Finset.card_biUnion hdisj
  simp only [id] at hcard
  rw [hcover] at hcard
  exact hcard.symm

/-- **Lower bound.**  Every colouring of an STS on a 37-element type has at least 19 classes. -/
theorem colour_lower_bound_37 (hW : Fintype.card W = 37) {S : Finset (Finset W)} (hS : IsSTS S)
    {C : Finset (Finset (Finset W))} (hC : IsColouring S C) : 19 ≤ C.card := by
  have h1 := card_sts_mul hS
  rw [hW] at h1
  have hc : Nat.choose 37 2 = 666 := by decide
  have h2 := sum_card_colouring hC
  have h3 : ∀ P ∈ C, P.card ≤ 12 := by
    intro P hP
    have := card_ppc_mul_le hS.1 (hC.1 P hP)
    omega
  have h4 : ∑ P ∈ C, P.card ≤ ∑ _P ∈ C, 12 := Finset.sum_le_sum h3
  rw [Finset.sum_const_nat (fun _ _ => rfl), h2] at h4
  omega

/-- The data-independent root (2): every colouring of every STS on every 37-element type has at
least 19 colour classes. -/
theorem colourLowerBound_37 : ColourLowerBound.{u} 37 19 :=
  fun _ _ _ hW _ hS _ hC => colour_lower_bound_37 hW hS hC

/-- `χ′(n) = r` from a lower bound on all colourings of all STS on `Fin n` and one STS on `Fin n`
with an `r`-colouring. -/
theorem chiPrime_eq_of {n r : ℕ} (hlow : ColourLowerBound.{0} n r)
    (hwit : ∃ S : Finset (Finset (Fin n)), IsSTS S ∧
      ∃ C : Finset (Finset (Finset (Fin n))), IsColouring S C ∧ C.card = r) :
    chiPrime n = r := by
  unfold chiPrime
  apply le_antisymm
  · exact Nat.sInf_le hwit
  · have hne : Set.Nonempty {r : ℕ | ∃ S : Finset (Finset (Fin n)), IsSTS S ∧
        ∃ C : Finset (Finset (Finset (Fin n))), IsColouring S C ∧ C.card = r} := ⟨r, hwit⟩
    obtain ⟨S, hS, C, hC, hcard⟩ := Nat.sInf_mem hne
    rw [← hcard]
    exact hlow (Fin n) (Fintype.card_fin n) S hS C hC

end Mcd.Counts
