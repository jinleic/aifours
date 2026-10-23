import RdsqsKernel.Target
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Finset.Union
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Counts forced by the definitions

Nothing here mentions data.  For a finite point type `V` (`v = card V`):

* `card_blocks_mul`: an SQS has `|B| * 4 = C(v, 3)` (the 3-subsets of the blocks partition all
  3-subsets);
* `derived_card_three`: every block of the derived design at `x` is a 3-subset avoiding `x`;
* `card_derived_mul`: `|B_x| * 3 = C(v - 1, 2)` (the 2-subsets of the derived blocks partition all
  2-subsets of `V \ {x}`);
* `card_class_mul`: a parallel class `P` of the derived design at `x` has `|P| * 3 = v - 1`;
* `card_resolution_mul`: a resolution `R` of the derived design at `x` has
  `|R| * ((v - 1) / 3) = |B_x|`.
-/

namespace Rdsqs.Counts

open Finset

variable {V : Type*} [Fintype V] [DecidableEq V]

omit [Fintype V] in
theorem mem_derivedBlocks {B : Finset (Finset V)} {x : V} {T : Finset V} :
    T ∈ derivedBlocks B x ↔ ∃ X ∈ B, x ∈ X ∧ X.erase x = T := by
  simp only [derivedBlocks, Finset.mem_image, Finset.mem_filter, and_assoc]

/-- An SQS has `|B| * 4 = C(v, 3)` blocks. -/
theorem card_blocks_mul {B : Finset (Finset V)} (h : IsSQS B) :
    B.card * 4 = (Fintype.card V).choose 3 := by
  have hcover : B.biUnion (fun X => X.powersetCard 3) = (Finset.univ : Finset V).powersetCard 3 := by
    ext T
    simp only [Finset.mem_biUnion, Finset.mem_powersetCard, Finset.subset_univ, true_and]
    constructor
    · rintro ⟨X, -, -, hT⟩
      exact hT
    · intro hT
      obtain ⟨X, ⟨hX, hTX⟩, -⟩ := h.2 T hT
      exact ⟨X, hX, hTX, hT⟩
  have hdisj : (B : Set (Finset V)).PairwiseDisjoint fun X => X.powersetCard 3 := by
    intro X hX Y hY hXY
    simp only [Function.onFun]
    rw [Finset.disjoint_left]
    intro T hTX hTY
    rw [Finset.mem_powersetCard] at hTX hTY
    obtain ⟨Z, -, hZ⟩ := h.2 T hTX.2
    exact hXY ((hZ X ⟨hX, hTX.1⟩).trans (hZ Y ⟨hY, hTY.1⟩).symm)
  have hcard := Finset.card_biUnion hdisj
  rw [hcover, Finset.card_powersetCard, Finset.card_univ] at hcard
  rw [hcard, Finset.sum_const_nat]
  intro X hX
  rw [Finset.card_powersetCard, h.1 X hX]
  rfl

omit [Fintype V] in
/-- Every block of the derived design at `x` is a 3-subset not containing `x`. -/
theorem derived_card_three {B : Finset (Finset V)} (h : IsSQS B) {x : V} {T : Finset V}
    (hT : T ∈ derivedBlocks B x) : T.card = 3 ∧ x ∉ T := by
  obtain ⟨X, hX, hx, rfl⟩ := mem_derivedBlocks.mp hT
  exact ⟨by rw [Finset.card_erase_of_mem hx, h.1 X hX], Finset.notMem_erase x X⟩

omit [Fintype V] in
/-- Two derived blocks at `x` sharing two distinct points are equal. -/
theorem derived_eq_of_pair {B : Finset (Finset V)} (h : IsSQS B) {x : V} {T T' : Finset V}
    (hT : T ∈ derivedBlocks B x) (hT' : T' ∈ derivedBlocks B x) {y z : V} (hyz : y ≠ z)
    (hy : y ∈ T) (hz : z ∈ T) (hy' : y ∈ T') (hz' : z ∈ T') : T = T' := by
  obtain ⟨X, hX, hx, rfl⟩ := mem_derivedBlocks.mp hT
  obtain ⟨X', hX', hx', rfl⟩ := mem_derivedBlocks.mp hT'
  obtain ⟨hyx, hyX⟩ := Finset.mem_erase.mp hy
  obtain ⟨hzx, hzX⟩ := Finset.mem_erase.mp hz
  obtain ⟨-, hyX'⟩ := Finset.mem_erase.mp hy'
  obtain ⟨-, hzX'⟩ := Finset.mem_erase.mp hz'
  have hcard : ({x, y, z} : Finset V).card = 3 :=
    Finset.card_eq_three.mpr ⟨x, y, z, Ne.symm hyx, Ne.symm hzx, hyz, rfl⟩
  obtain ⟨W, -, hW⟩ := h.2 _ hcard
  have hsub : ∀ Y : Finset V, x ∈ Y → y ∈ Y → z ∈ Y → ({x, y, z} : Finset V) ⊆ Y := by
    intro Y h1 h2 h3 w hw
    simp only [Finset.mem_insert, Finset.mem_singleton] at hw
    rcases hw with rfl | rfl | rfl
    · exact h1
    · exact h2
    · exact h3
  rw [hW X ⟨hX, hsub X hx hyX hzX⟩, hW X' ⟨hX', hsub X' hx' hyX' hzX'⟩]

/-- The derived design at `x` has `|B_x| * 3 = C(v - 1, 2)` blocks. -/
theorem card_derived_mul {B : Finset (Finset V)} (h : IsSQS B) (x : V) :
    (derivedBlocks B x).card * 3 = (Fintype.card V - 1).choose 2 := by
  have hcover : (derivedBlocks B x).biUnion (fun T => T.powersetCard 2) =
      (Finset.univ.erase x).powersetCard 2 := by
    ext Q
    simp only [Finset.mem_biUnion, Finset.mem_powersetCard]
    constructor
    · rintro ⟨T, hT, hQT, hQ⟩
      refine ⟨fun w hw => ?_, hQ⟩
      have hxT := (derived_card_three h hT).2
      exact Finset.mem_erase.mpr ⟨fun hwx => hxT (hwx ▸ hQT hw), Finset.mem_univ _⟩
    · rintro ⟨hQ, hQ2⟩
      obtain ⟨y, z, hyz, rfl⟩ := Finset.card_eq_two.mp hQ2
      have hyx : y ≠ x := (Finset.mem_erase.mp (hQ (by simp))).1
      have hzx : z ≠ x := (Finset.mem_erase.mp (hQ (by simp))).1
      have hcard : ({x, y, z} : Finset V).card = 3 :=
        Finset.card_eq_three.mpr ⟨x, y, z, Ne.symm hyx, Ne.symm hzx, hyz, rfl⟩
      obtain ⟨X, ⟨hX, hsub⟩, -⟩ := h.2 _ hcard
      refine ⟨X.erase x, mem_derivedBlocks.mpr ⟨X, hX, hsub (by simp), rfl⟩, ?_,
        Finset.card_eq_two.mpr ⟨y, z, hyz, rfl⟩⟩
      intro w hw
      simp only [Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Finset.mem_erase.mpr ⟨hyx, hsub (by simp)⟩
      · exact Finset.mem_erase.mpr ⟨hzx, hsub (by simp)⟩
  have hdisj : ((derivedBlocks B x : Finset (Finset V)) : Set (Finset V)).PairwiseDisjoint
      fun T => T.powersetCard 2 := by
    intro T hT T' hT' hne
    simp only [Function.onFun]
    rw [Finset.disjoint_left]
    intro Q hQT hQT'
    rw [Finset.mem_powersetCard] at hQT hQT'
    obtain ⟨y, z, hyz, rfl⟩ := Finset.card_eq_two.mp hQT.2
    exact hne (derived_eq_of_pair h hT hT' hyz (hQT.1 (by simp)) (hQT.1 (by simp))
      (hQT'.1 (by simp)) (hQT'.1 (by simp)))
  have hcard := Finset.card_biUnion hdisj
  rw [hcover, Finset.card_powersetCard, Finset.card_erase_of_mem (Finset.mem_univ x),
    Finset.card_univ] at hcard
  rw [hcard, Finset.sum_const_nat]
  intro T hT
  rw [Finset.card_powersetCard, (derived_card_three h hT).1]
  rfl

/-- A parallel class of the derived design at `x` has `|P| * 3 = v - 1` blocks. -/
theorem card_class_mul {B : Finset (Finset V)} (h : IsSQS B) {x : V} {P : Finset (Finset V)}
    (hP : IsDerivedParallelClass B x P) : P.card * 3 = Fintype.card V - 1 := by
  have hcover : P.biUnion id = Finset.univ.erase x := by
    ext y
    simp only [Finset.mem_biUnion, id, Finset.mem_erase, Finset.mem_univ, and_true]
    constructor
    · rintro ⟨T, hT, hyT⟩ hyx
      exact (derived_card_three h (hP.1 hT)).2 (hyx ▸ hyT)
    · intro hyx
      obtain ⟨T, ⟨hT, hyT⟩, -⟩ := hP.2 y hyx
      exact ⟨T, hT, hyT⟩
  have hdisj : (P : Set (Finset V)).PairwiseDisjoint id := by
    intro T hT T' hT' hne
    simp only [Function.onFun, id]
    rw [Finset.disjoint_left]
    intro y hyT hyT'
    have hyx : y ≠ x := fun hyx => (derived_card_three h (hP.1 hT)).2 (hyx ▸ hyT)
    obtain ⟨S, -, hS⟩ := hP.2 y hyx
    exact hne ((hS T ⟨hT, hyT⟩).trans (hS T' ⟨hT', hyT'⟩).symm)
  have hcard := Finset.card_biUnion hdisj
  rw [hcover, Finset.card_erase_of_mem (Finset.mem_univ x), Finset.card_univ] at hcard
  rw [hcard, Finset.sum_const_nat]
  intro T hT
  exact (derived_card_three h (hP.1 hT)).1

/-- A resolution of the derived design at `x` has `|R| * ((v - 1) / 3) = |B_x|` classes. -/
theorem card_resolution_mul {B : Finset (Finset V)} (h : IsSQS B) {x : V}
    {R : Finset (Finset (Finset V))} (hR : IsDerivedResolution B x R) :
    R.card * ((Fintype.card V - 1) / 3) = (derivedBlocks B x).card := by
  have hcover : R.biUnion id = derivedBlocks B x := by
    ext T
    simp only [Finset.mem_biUnion, id]
    constructor
    · rintro ⟨P, hP, hTP⟩
      exact (hR.1 P hP).1 hTP
    · intro hT
      obtain ⟨P, ⟨hP, hTP⟩, -⟩ := hR.2 T hT
      exact ⟨P, hP, hTP⟩
  have hdisj : (R : Set (Finset (Finset V))).PairwiseDisjoint id := by
    intro P hP P' hP' hne
    simp only [Function.onFun, id]
    rw [Finset.disjoint_left]
    intro T hTP hTP'
    obtain ⟨Q, -, hQ⟩ := hR.2 T ((hR.1 P hP).1 hTP)
    exact hne ((hQ P ⟨hP, hTP⟩).trans (hQ P' ⟨hP', hTP'⟩).symm)
  have hcard := Finset.card_biUnion hdisj
  rw [hcover] at hcard
  rw [hcard, Finset.sum_const_nat]
  intro P hP
  have h3 := card_class_mul h (hR.1 P hP)
  simp only [id]
  omega

end Rdsqs.Counts
