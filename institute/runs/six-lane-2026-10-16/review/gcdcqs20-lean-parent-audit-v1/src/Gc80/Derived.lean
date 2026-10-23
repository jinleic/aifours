import Gc80.GcTarget

/-!
# SQS, CQS and incomplete STS from their derived designs (data-independent)

For a block set `B` of 4-subsets of a type `V`:

* `isSQS_of_derived`: if at every point `x` every 2-subset `P ∌ x` lies in exactly one block of
  the derived design `derivedBlocks B x`, then `B` is an SQS (a 3-subset `T ∋ x` lies in the block
  `X` iff `T \ {x}` lies in `X \ {x}`, and `X ↦ X \ {x}` is injective on the blocks through `x`);
* `isCQS0_of_derived`: the same with groups: if every 2-subset `P ∌ x` with `P ⊄ grp x` lies in
  exactly one derived block at `x`, and no 2-subset of `grp x \ {x}` lies in any derived block
  at `x`, then `B` is a CQS with these groups and an empty stem;
* `isHoleSTS_of_derived`: under the same two local conditions at `x`, the derived design at `x`
  is an incomplete STS on `V \ {x}` with hole `G \ {x}`, `x ∈ G`.

Finally the facts about the four groups `grp80 i` of `Fin 80` used with these lemmas.
-/

namespace Mcd

section Generic

variable {V : Type*} [DecidableEq V]

theorem mem_derivedBlocks {B : Finset (Finset V)} {x : V} {T : Finset V} :
    T ∈ derivedBlocks B x ↔ ∃ X ∈ B, x ∈ X ∧ X.erase x = T := by
  simp only [derivedBlocks, Finset.mem_image, Finset.mem_filter, and_assoc]

/-- A 3-subset `T ∋ x` lies in exactly one block if `T \ {x}` lies in exactly one derived block
at `x`. -/
theorem unique_block_of_derived {B : Finset (Finset V)} {x : V} {T : Finset V} (hxT : x ∈ T)
    (h : ∃! D, D ∈ derivedBlocks B x ∧ T.erase x ⊆ D) : ∃! X, X ∈ B ∧ T ⊆ X := by
  obtain ⟨D, ⟨hD, hTD⟩, huniq⟩ := h
  obtain ⟨X, hX, hxX, rfl⟩ := mem_derivedBlocks.mp hD
  refine ⟨X, ⟨hX, fun y hy => ?_⟩, ?_⟩
  · by_cases hyx : y = x
    · exact hyx ▸ hxX
    · exact Finset.mem_of_mem_erase (hTD (Finset.mem_erase.mpr ⟨hyx, hy⟩))
  · rintro Y ⟨hY, hTY⟩
    have hxY : x ∈ Y := hTY hxT
    have h1 := huniq (Y.erase x)
      ⟨mem_derivedBlocks.mpr ⟨Y, hY, hxY, rfl⟩, Finset.erase_subset_erase x hTY⟩
    rw [← Finset.insert_erase hxY, ← Finset.insert_erase hxX, h1]

theorem card_erase_three {T : Finset V} {x : V} (hT : T.card = 3) (hx : x ∈ T) :
    (T.erase x).card = 2 := by
  rw [Finset.card_erase_of_mem hx, hT]

/-- **SQS from derived designs.** -/
theorem isSQS_of_derived {B : Finset (Finset V)} (h4 : ∀ X ∈ B, X.card = 4)
    (hd : ∀ x : V, ∀ P : Finset V, P.card = 2 → x ∉ P → ∃! D, D ∈ derivedBlocks B x ∧ P ⊆ D) :
    IsSQS B := by
  refine ⟨h4, fun T hT => ?_⟩
  obtain ⟨x, hx⟩ : T.Nonempty := Finset.card_pos.mp (by omega)
  exact unique_block_of_derived hx (hd x _ (card_erase_three hT hx) (Finset.notMem_erase x T))

/-- **CQS with empty stem from derived designs.**  `grp x` is the group of `x`. -/
theorem isCQS0_of_derived {Gs : Finset (Finset V)} {A : Finset (Finset V)} (grp : V → Finset V)
    (hpart : IsGroupPartition Gs) (hgrp : ∀ G ∈ Gs, ∀ x ∈ G, G = grp x)
    (h4 : ∀ X ∈ A, X.card = 4)
    (hcov : ∀ x : V, ∀ P : Finset V, P.card = 2 → x ∉ P → ¬ P ⊆ grp x →
      ∃! D, D ∈ derivedBlocks A x ∧ P ⊆ D)
    (hhole : ∀ x : V, ∀ P : Finset V, P.card = 2 → P ⊆ (grp x).erase x →
      ∀ D ∈ derivedBlocks A x, ¬ P ⊆ D) :
    IsCQS0 Gs A := by
  refine ⟨hpart, h4, fun T hT hnot => ?_, fun T hT G hG hTG X hX hTX => ?_⟩
  · obtain ⟨x, hx⟩ : T.Nonempty := Finset.card_pos.mp (by omega)
    obtain ⟨G, hG, hxG⟩ := hpart.2.2 x
    refine unique_block_of_derived hx
      (hcov x _ (card_erase_three hT hx) (Finset.notMem_erase x T) fun hsub => ?_)
    apply hnot G hG
    intro y hy
    by_cases hyx : y = x
    · exact hyx ▸ hxG
    · rw [hgrp G hG x hxG]
      exact hsub (Finset.mem_erase.mpr ⟨hyx, hy⟩)
  · obtain ⟨x, hx⟩ : T.Nonempty := Finset.card_pos.mp (by omega)
    have hxX : x ∈ X := hTX hx
    have hG' := hgrp G hG x (hTG hx)
    refine hhole x (T.erase x) (card_erase_three hT hx) ?_ (X.erase x)
      (mem_derivedBlocks.mpr ⟨X, hX, hxX, rfl⟩) (Finset.erase_subset_erase x hTX)
    rw [← hG']
    exact Finset.erase_subset_erase x hTG

/-- **Incomplete STS from the derived design at `x ∈ G`.** -/
theorem isHoleSTS_of_derived [Fintype V] {A : Finset (Finset V)} {x : V} {G : Finset V}
    (h4 : ∀ X ∈ A, X.card = 4)
    (hcov : ∀ P : Finset V, P.card = 2 → x ∉ P → ¬ P ⊆ G → ∃! D, D ∈ derivedBlocks A x ∧ P ⊆ D)
    (hhole : ∀ P : Finset V, P.card = 2 → P ⊆ G.erase x → ∀ D ∈ derivedBlocks A x, ¬ P ⊆ D) :
    IsHoleSTS (Finset.univ.erase x) (G.erase x) (derivedBlocks A x) := by
  refine ⟨Finset.erase_subset_erase x (Finset.subset_univ G), fun T hT => ?_,
    fun P hP hPY hPH => ?_, hhole⟩
  · obtain ⟨X, hX, hxX, rfl⟩ := mem_derivedBlocks.mp hT
    exact ⟨by rw [Finset.card_erase_of_mem hxX, h4 X hX],
      Finset.erase_subset_erase x (Finset.subset_univ X)⟩
  · have hxP : x ∉ P := fun h => Finset.notMem_erase x _ (hPY h)
    refine hcov P hP hxP fun hPG => hPH fun y hy => Finset.mem_erase.mpr ⟨?_, hPG hy⟩
    rintro rfl
    exact hxP hy

end Generic

/-! ## The four groups of `Fin 80` -/

theorem mem_grp80 {i : ℕ} {y : Fin 80} : y ∈ grp80 i ↔ 20 * i ≤ y.val ∧ y.val < 20 * i + 20 := by
  simp [grp80]

theorem mem_grp80_self (x : Fin 80) : x ∈ grp80 (x.val / 20) := by
  rw [mem_grp80]
  omega

theorem grp80_mem_groups80 (x : Fin 80) : grp80 (x.val / 20) ∈ groups80 := by
  simp only [groups80, Finset.mem_insert, Finset.mem_singleton]
  rcases (by omega : x.val / 20 = 0 ∨ x.val / 20 = 1 ∨ x.val / 20 = 2 ∨ x.val / 20 = 3) with
    h | h | h | h <;> simp [h]

theorem eq_grp80_of_mem {G : Finset (Fin 80)} (hG : G ∈ groups80) {x : Fin 80} (hx : x ∈ G) :
    G = grp80 (x.val / 20) := by
  simp only [groups80, Finset.mem_insert, Finset.mem_singleton] at hG
  rcases hG with rfl | rfl | rfl | rfl <;> rw [mem_grp80] at hx <;> congr 1 <;> omega

theorem isGroupPartition_groups80 : IsGroupPartition groups80 := by
  refine ⟨fun G hG => ?_, fun G hG G' hG' hne => ?_,
    fun x => ⟨_, grp80_mem_groups80 x, mem_grp80_self x⟩⟩
  · simp only [groups80, Finset.mem_insert, Finset.mem_singleton] at hG
    rcases hG with rfl | rfl | rfl | rfl
    · exact ⟨⟨0, by omega⟩, mem_grp80.mpr (by simp)⟩
    · exact ⟨⟨20, by omega⟩, mem_grp80.mpr (by simp)⟩
    · exact ⟨⟨40, by omega⟩, mem_grp80.mpr (by simp)⟩
    · exact ⟨⟨60, by omega⟩, mem_grp80.mpr (by simp)⟩
  · rw [Finset.disjoint_left]
    intro y hy hy'
    exact hne ((eq_grp80_of_mem hG hy).trans (eq_grp80_of_mem hG' hy').symm)

end Mcd
