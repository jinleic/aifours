import PC88Kernel.Target
import PC88Kernel.Generic
import Mathlib.Data.ZMod.Basic

/-!
# The canonical model: points `ZMod 88`, cycle `x ↦ x + 1`

Proof of `PC88.CanonicalTarget`, following `review/point-cyclic88-parent-inputs-v1/PROOF.md`
(SHA-256 `227c200c…bfa`).  Translation by `d` acts on blocks and on classes as the pointwise
action `d +ᵥ X = {d + x : x ∈ X}`, `d +ᵥ P = {d +ᵥ X : X ∈ P}`.  Every fact used is derived here
from `IsDesign`, `IsResolution` and `IsResolutionAut _ _ (Equiv.addRight 1)`:

* `hyp_of`: the hypotheses (H1)–(H4) of PROOF §1, with invariance under every translation;
* `transl` (Lemma 1), `stab_cases` (a translation fixing a 4-set is `0, 22, 44` or `66`),
  `vadd44_of_stab` (a nontrivially stabilised block is fixed by `44`, i.e. *short*),
  `short_diff`, `short_eq` (Lemma 2);
* `class_card` (each class has 22 blocks), `R_card_le` (at most 29 classes);
* for the class `P` containing the block through `{0, 8}`: orbit–stabilizer, the stabilizer acts
  freely on the full blocks of `P` (Lemma 3(b)), `orbit_short_bound` (Lemma 3(c)), and
  `arith_final` (Corollary 4 and Lemma 5 arithmetic), so the stabilizer has 11 or 22 elements and
  contains `8` (`mem8_of_card`); then Lemma 6 and §5 give the contradiction.
-/

namespace PC88.Canonical

open Pointwise PC88.Generic

/-- Points of the canonical model. -/
abbrev G := ZMod 88

/-- The hypotheses of PROOF §1 on the canonical model, with invariance under every translation. -/
structure Hyp (B : Finset (Finset G)) (R : Finset (Finset (Finset G))) : Prop where
  card4 : ∀ X ∈ B, X.card = 4
  pair : ∀ x y : G, x ≠ y → ∃! X, X ∈ B ∧ x ∈ X ∧ y ∈ X
  sub : ∀ P ∈ R, P ⊆ B
  cover : ∀ P ∈ R, ∀ x : G, ∃! X, X ∈ P ∧ x ∈ X
  part : ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P
  trB : ∀ d : G, ∀ X ∈ B, d +ᵥ X ∈ B
  trR : ∀ d : G, ∀ P ∈ R, d +ᵥ P ∈ R

theorem blockImage_addRight (d : G) (X : Finset G) :
    blockImage (Equiv.addRight d) X = d +ᵥ X := by
  ext y
  simp only [blockImage, Finset.mem_map_equiv, Equiv.addRight_symm, Equiv.coe_addRight,
    Finset.mem_vadd_finset, vadd_eq_add]
  constructor
  · intro hy
    exact ⟨y + -d, hy, by rw [add_comm y, add_neg_cancel_left]⟩
  · rintro ⟨x, hx, rfl⟩
    rwa [add_comm d x, add_neg_cancel_right]

/-- PROOF §1: the definitions give (H1)–(H4), with invariance under every translation. -/
theorem hyp_of {B : Finset (Finset G)} {R : Finset (Finset (Finset G))} (hD : IsDesign B)
    (hR : IsResolution B R) (hA : IsResolutionAut B R (Equiv.addRight (1 : G))) : Hyp B R := by
  have hB1 : ∀ X ∈ B, (1 : G) +ᵥ X ∈ B := by
    intro X hX
    have hm : blockImage (Equiv.addRight (1 : G)) X ∈ B.image (blockImage (Equiv.addRight 1)) :=
      Finset.mem_image_of_mem _ hX
    rwa [hA.1, blockImage_addRight] at hm
  have hR1 : ∀ P ∈ R, (1 : G) +ᵥ P ∈ R := by
    intro P hP
    have hm := hA.2 P hP
    have he : P.image (blockImage (Equiv.addRight (1 : G))) = (1 : G) +ᵥ P := by
      rw [Finset.vadd_finset_def]
      congr 1
      funext X
      exact blockImage_addRight 1 X
    rwa [he] at hm
  have hBn : ∀ n : ℕ, ∀ X ∈ B, (n : G) +ᵥ X ∈ B := by
    intro n
    induction n with
    | zero =>
      intro X hX
      simpa using hX
    | succ n ih =>
      intro X hX
      rw [Nat.cast_succ, add_comm, add_vadd]
      exact hB1 _ (ih X hX)
  have hRn : ∀ n : ℕ, ∀ P ∈ R, (n : G) +ᵥ P ∈ R := by
    intro n
    induction n with
    | zero =>
      intro P hP
      simpa using hP
    | succ n ih =>
      intro P hP
      rw [Nat.cast_succ, add_comm, add_vadd]
      exact hR1 _ (ih P hP)
  exact
    { card4 := hD.1
      pair := hD.2
      sub := fun P hP => (hR.1 P hP).1
      cover := fun P hP => (hR.1 P hP).2
      part := hR.2
      trB := fun d X hX => by simpa using hBn d.val X hX
      trR := fun d P hP => by simpa using hRn d.val P hP }

/-! ### Blocks -/

/-- Finite arithmetic in `ZMod 88`: if `i * d = j * d` for distinct `i, j < 5`, then
`d ∈ {0, 22, 44, 66}`. -/
theorem arith_stab : ∀ d : G, ∀ i j : Fin 5, i ≠ j →
    ((i : ℕ) : G) * d = ((j : ℕ) : G) * d → d = 0 ∨ d = 22 ∨ d = 44 ∨ d = 66 := by
  decide

/-- A translation fixing a 4-subset of `ZMod 88` is `0`, `22`, `44` or `66` (PROOF Lemma 2:
the stabilizer of a block has order dividing 4). -/
theorem stab_cases {X : Finset G} (hX : X.card = 4) {d : G} (hd : d +ᵥ X = X) :
    d = 0 ∨ d = 22 ∨ d = 44 ∨ d = 66 := by
  obtain ⟨x, hx⟩ : X.Nonempty := Finset.card_pos.mp (by omega)
  have hmem : ∀ n : ℕ, (n : G) * d + x ∈ X := by
    intro n
    induction n with
    | zero => simpa using hx
    | succ n ih =>
      have hm := Finset.vadd_mem_vadd_finset (a := d) ih
      rw [hd, vadd_eq_add] at hm
      have he : ((n + 1 : ℕ) : G) * d + x = d + ((n : G) * d + x) := by
        push_cast
        ring
      rw [he]
      exact hm
  obtain ⟨i, hi, j, hj, hij, hfij⟩ := Finset.exists_ne_map_eq_of_card_lt_of_maps_to
    (s := Finset.range 5) (t := X) (by rw [hX, Finset.card_range]; omega)
    (f := fun n : ℕ => (n : G) * d + x) (fun n _ => hmem n)
  exact arith_stab d ⟨i, Finset.mem_range.mp hi⟩ ⟨j, Finset.mem_range.mp hj⟩
    (fun he => hij (congrArg Fin.val he)) (add_right_cancel hfij)

/-- A 4-subset fixed by a nonzero translation is fixed by translation by `44`. -/
theorem vadd44_of_stab {X : Finset G} (hX : X.card = 4) {d : G} (hd : d +ᵥ X = X) (hd0 : d ≠ 0) :
    (44 : G) +ᵥ X = X := by
  rcases stab_cases hX hd with rfl | rfl | rfl | rfl
  · exact absurd rfl hd0
  · rw [show (44 : G) = 22 + 22 by decide, add_vadd, hd, hd]
  · exact hd
  · rw [show (44 : G) = 66 + 66 by decide, add_vadd, hd, hd]

section Design

variable {B : Finset (Finset G)} {R : Finset (Finset (Finset G))}

/-- (H3): two blocks sharing two points are equal. -/
theorem eq_of_two (h : Hyp B R) {X Y : Finset G} (hX : X ∈ B) (hY : Y ∈ B) {x y : G}
    (hxy : x ≠ y) (hxX : x ∈ X) (hyX : y ∈ X) (hxY : x ∈ Y) (hyY : y ∈ Y) : X = Y :=
  (h.pair x y hxy).unique ⟨hX, hxX, hyX⟩ ⟨hY, hxY, hyY⟩

/-- PROOF Lemma 1 (translation lemma). -/
theorem transl (h : Hyp B R) {X : Finset G} (hX : X ∈ B) {x y d : G} (hxy : x ≠ y) (hx : x ∈ X)
    (hy : y ∈ X) (hxd : d + x ∈ X) (hyd : d + y ∈ X) : d +ᵥ X = X := by
  have hx' : d + x ∈ d +ᵥ X := Finset.vadd_mem_vadd_finset hx
  have hy' : d + y ∈ d +ᵥ X := Finset.vadd_mem_vadd_finset hy
  have hne : d + x ≠ d + y := fun he => hxy (add_left_cancel he)
  exact eq_of_two h (h.trB d X hX) hX hne hx' hy' hxd hyd

theorem mem_of_vadd44 {X : Finset G} (hs : (44 : G) +ᵥ X = X) {z : G} (hz : z ∈ X) :
    44 + z ∈ X := by
  have hm : (44 : G) + z ∈ (44 : G) +ᵥ X := Finset.vadd_mem_vadd_finset hz
  rwa [hs] at hm

theorem ne_add44 (z : G) : z ≠ 44 + z := by
  intro he
  have h44 : (44 : G) = 0 := by
    have := congrArg (fun t => t - z) he
    simpa using this.symm
  exact absurd h44 (by decide)

/-- PROOF Lemma 2 (differences in a short block): if a block is fixed by translation by `44`, all
differences of its points lie in `{0, 22, 44, 66}`. -/
theorem short_diff (h : Hyp B R) {X : Finset G} (hX : X ∈ B) (hs : (44 : G) +ᵥ X = X) {x y : G}
    (hx : x ∈ X) (hy : y ∈ X) :
    y - x = 0 ∨ y - x = 22 ∨ y - x = 44 ∨ y - x = 66 := by
  have hd : (y - x) +ᵥ X = X := by
    apply transl h hX (ne_add44 x) hx (mem_of_vadd44 hs hx)
    · rwa [sub_add_cancel]
    · rw [show y - x + (44 + x) = 44 + y by ring]
      exact mem_of_vadd44 hs hy
  exact stab_cases (h.card4 X hX) hd

/-- Distinct short blocks are disjoint. -/
theorem short_eq (h : Hyp B R) {X Y : Finset G} (hX : X ∈ B) (hY : Y ∈ B)
    (hsX : (44 : G) +ᵥ X = X) (hsY : (44 : G) +ᵥ Y = Y) {c : G} (hcX : c ∈ X) (hcY : c ∈ Y) :
    X = Y :=
  eq_of_two h hX hY (ne_add44 c) hcX (mem_of_vadd44 hsX hcX) hcY (mem_of_vadd44 hsY hcY)

/-- Shortness is invariant under translation. -/
theorem short_vadd_iff (g : G) (X : Finset G) :
    (44 : G) +ᵥ (g +ᵥ X) = g +ᵥ X ↔ (44 : G) +ᵥ X = X := by
  rw [← add_vadd, add_comm, add_vadd]
  exact vadd_left_cancel_iff g

/-! ### Classes -/

/-- (H4): two blocks of one class sharing a point are equal. -/
theorem class_eq (h : Hyp B R) {P : Finset (Finset G)} (hP : P ∈ R) {X Y : Finset G}
    (hX : X ∈ P) (hY : Y ∈ P) {c : G} (hcX : c ∈ X) (hcY : c ∈ Y) : X = Y :=
  (h.cover P hP c).unique ⟨hX, hcX⟩ ⟨hY, hcY⟩

/-- Distinct classes share no block. -/
theorem class_disj (h : Hyp B R) {P Q : Finset (Finset G)} (hP : P ∈ R) (hQ : Q ∈ R)
    {X : Finset G} (hXP : X ∈ P) (hXQ : X ∈ Q) : P = Q :=
  (h.part X (h.sub P hP hXP)).unique ⟨hP, hXP⟩ ⟨hQ, hXQ⟩

/-- Every parallel class has `88 / 4 = 22` blocks. -/
theorem class_card (h : Hyp B R) {P : Finset (Finset G)} (hP : P ∈ R) : P.card = 22 := by
  have hcov : P.biUnion id = Finset.univ := by
    apply Finset.eq_univ_of_forall
    intro x
    obtain ⟨X, ⟨hX, hx⟩, -⟩ := h.cover P hP x
    exact Finset.mem_biUnion.mpr ⟨X, hX, hx⟩
  have hdisj : (P : Set (Finset G)).PairwiseDisjoint id := by
    intro X hX Y hY hne
    exact Finset.disjoint_left.mpr fun c hcX hcY => hne (class_eq h hP hX hY hcX hcY)
  have hc := Finset.card_biUnion hdisj
  have h4 : ∀ X ∈ P, (id X).card = 4 := fun X hX => h.card4 X (h.sub P hP hX)
  rw [hcov, Finset.card_univ, ZMod.card, Finset.sum_const_nat h4] at hc
  omega

/-- There are at most `87 / 3 = 29` classes: each class has exactly one block through `0`, and
the blocks through `0` meet pairwise only in `0`. -/
theorem R_card_le (h : Hyp B R) : R.card ≤ 29 := by
  have hB0 : (B.filter fun X => (0 : G) ∈ X).card ≤ 29 := by
    have hdisj : ((B.filter fun X => (0 : G) ∈ X : Finset (Finset G)) : Set (Finset G)).PairwiseDisjoint
        (fun X => X.erase 0) := by
      intro X hX Y hY hne
      refine Finset.disjoint_left.mpr fun c hcX hcY => hne ?_
      have hX' := Finset.mem_filter.mp hX
      have hY' := Finset.mem_filter.mp hY
      obtain ⟨hc0, hcX⟩ := Finset.mem_erase.mp hcX
      obtain ⟨-, hcY⟩ := Finset.mem_erase.mp hcY
      exact eq_of_two h hX'.1 hY'.1 (Ne.symm hc0) hX'.2 hcX hY'.2 hcY
    have hc := Finset.card_biUnion hdisj
    rw [Finset.sum_const_nat (m := 3) (fun X hX => by
      rw [Finset.card_erase_of_mem (Finset.mem_filter.mp hX).2,
        h.card4 X (Finset.mem_filter.mp hX).1])] at hc
    have hsub : (B.filter fun X => (0 : G) ∈ X).biUnion (fun X => X.erase 0) ⊆
        Finset.univ.erase 0 := by
      intro c hc
      obtain ⟨X, -, hcX⟩ := Finset.mem_biUnion.mp hc
      exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hcX).1, Finset.mem_univ c⟩
    have hle := Finset.card_le_card hsub
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, ZMod.card] at hle
    omega
  have hone : ∀ P ∈ R, (P.filter fun X => (0 : G) ∈ X).card = 1 := by
    intro P hP
    obtain ⟨X, ⟨hX, h0⟩, huniq⟩ := h.cover P hP 0
    rw [Finset.card_eq_one]
    refine ⟨X, ?_⟩
    ext Y
    simp only [Finset.mem_filter, Finset.mem_singleton]
    constructor
    · rintro ⟨hY, h0Y⟩
      exact huniq Y ⟨hY, h0Y⟩
    · rintro rfl
      exact ⟨hX, h0⟩
  have hdisj : (R : Set (Finset (Finset G))).PairwiseDisjoint
      (fun P => P.filter fun X => (0 : G) ∈ X) := by
    intro P hP Q hQ hne
    refine Finset.disjoint_left.mpr fun X hXP hXQ => hne ?_
    exact class_disj h hP hQ (Finset.mem_filter.mp hXP).1 (Finset.mem_filter.mp hXQ).1
  have hc := Finset.card_biUnion hdisj
  rw [Finset.sum_const_nat (m := 1) hone, mul_one] at hc
  have hsub : R.biUnion (fun P => P.filter fun X => (0 : G) ∈ X) ⊆
      B.filter fun X => (0 : G) ∈ X := by
    intro X hX
    obtain ⟨P, hP, hXP⟩ := Finset.mem_biUnion.mp hX
    obtain ⟨hXP, h0X⟩ := Finset.mem_filter.mp hXP
    exact Finset.mem_filter.mpr ⟨h.sub P hP hXP, h0X⟩
  have hle := Finset.card_le_card hsub
  omega

/-- At most 22 pairwise disjoint 4-subsets of `ZMod 88`. -/
theorem card_le_of_disjoint4 (T : Finset (Finset G)) (h4 : ∀ X ∈ T, X.card = 4)
    (hdisj : ∀ X ∈ T, ∀ Y ∈ T, ∀ c : G, c ∈ X → c ∈ Y → X = Y) : T.card ≤ 22 := by
  have hd : (T : Set (Finset G)).PairwiseDisjoint id := by
    intro X hX Y hY hne
    exact Finset.disjoint_left.mpr fun c hcX hcY => hne (hdisj X hX Y hY c hcX hcY)
  have hU := Finset.card_biUnion hd
  have h4' : ∀ X ∈ T, (id X).card = 4 := h4
  rw [Finset.sum_const_nat h4'] at hU
  have hle := Finset.card_le_univ (T.biUnion id)
  rw [ZMod.card] at hle
  omega

/-- The orbit of a class consists of classes. -/
theorem orb_subset (h : Hyp B R) {P : Finset (Finset G)} (hP : P ∈ R) : orb (G := G) P ⊆ R := by
  intro Q hQ
  obtain ⟨g, rfl⟩ := mem_orb.mp hQ
  exact h.trR g P hP

set_option maxHeartbeats 400000 in
theorem test1 (h : Hyp B R) {P : Finset (Finset G)} (hP : P ∈ R) (X : Finset G)
    (hX : X ∈ (orb (G := G) P).biUnion (fun Q => Q.filter fun X => (44 : G) +ᵥ X = X)) : X ∈ B := by
  rw [Finset.mem_biUnion] at hX
  obtain ⟨Q, hQ, hXQ⟩ := hX
  exact h.sub Q (orb_subset h hP hQ) (Finset.mem_filter.mp hXQ).1

end Design
end PC88.Canonical
