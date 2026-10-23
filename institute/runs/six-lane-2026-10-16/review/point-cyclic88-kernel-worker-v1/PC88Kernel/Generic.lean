import Mathlib.Algebra.Group.Action.Pointwise.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Generic finite group-action counting lemmas

Nothing here mentions designs or the number 88.  For an additive group `G` acting on a type `β`:

* `card_orb_mul_card_stab`: orbit–stabilizer, `#orbit(b) * #stabilizer(b) = #G` (finset form);
* `card_dvd_of_free`: if a finite subgroup `K` leaves a finset `F` invariant and acts freely on it,
  then `#K ∣ #F` (the `K`-orbits in `F` all have `#K` elements);
* `card_nsmul_eq_zero_of_closed` (abelian `G`): `#K • k = 0` for every element `k` of a finite
  subgroup `K` (Lagrange, by the translation-invariance of `∑_{x ∈ K} x`).
-/

namespace PC88.Generic

open Pointwise

section Action

variable {G β : Type*} [AddGroup G] [AddAction G β] [DecidableEq β]

/-- The stabilizer of `b`, as a finset.  Irreducible, so that elaboration never tries to
evaluate it on a concrete group; it is used only through `stab_eq`/`mem_stab`. -/
@[irreducible] def stab [Fintype G] (b : β) : Finset G := Finset.univ.filter fun g => g +ᵥ b = b

/-- The orbit of `b`, as a finset (irreducible, used only through `orb_eq`/`mem_orb`). -/
@[irreducible] def orb [Fintype G] (b : β) : Finset β := Finset.univ.image fun g : G => g +ᵥ b

theorem stab_eq [Fintype G] (b : β) :
    stab (G := G) b = Finset.univ.filter fun g => g +ᵥ b = b := by
  rw [stab]

theorem orb_eq [Fintype G] (b : β) : orb (G := G) b = Finset.univ.image fun g : G => g +ᵥ b := by
  rw [orb]

theorem mem_stab [Fintype G] {b : β} {g : G} : g ∈ stab b ↔ g +ᵥ b = b := by
  simp [stab_eq]

theorem mem_orb [Fintype G] {b c : β} : c ∈ orb (G := G) b ↔ ∃ g : G, g +ᵥ b = c := by
  simp [orb_eq]

theorem zero_mem_stab [Fintype G] (b : β) : (0 : G) ∈ stab b :=
  mem_stab.mpr (zero_vadd G b)

theorem add_mem_stab [Fintype G] {b : β} {g h : G} (hg : g ∈ stab b) (hh : h ∈ stab b) :
    g + h ∈ stab b := by
  rw [mem_stab] at *
  rw [add_vadd, hh, hg]

theorem neg_mem_stab [Fintype G] {b : β} {g : G} (hg : g ∈ stab b) : -g ∈ stab b := by
  rw [mem_stab] at *
  rw [neg_vadd_eq_iff, hg]

/-- **Orbit–stabilizer theorem** (finset form). -/
theorem card_orb_mul_card_stab [Fintype G] (b : β) :
    (orb (G := G) b).card * (stab (G := G) b).card = Fintype.card G := by
  rw [orb_eq, ← Finset.card_univ,
    Finset.card_eq_sum_card_image (fun g : G => g +ᵥ b) Finset.univ]
  rw [Finset.sum_const_nat (m := (stab (G := G) b).card)]
  intro c hc
  obtain ⟨g₀, -, rfl⟩ := Finset.mem_image.mp hc
  have hfib : (Finset.univ.filter fun g : G => g +ᵥ b = g₀ +ᵥ b) =
      (stab (G := G) b).map (Equiv.addLeft g₀).toEmbedding := by
    ext g
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_map_equiv, mem_stab,
      Equiv.addLeft_symm, Equiv.coe_addLeft]
    rw [add_vadd, neg_vadd_eq_iff]
  rw [hfib, Finset.card_map]

/-- If a finite subgroup `K` (given as a finset containing `0` and closed under `(a, b) ↦ -a + b`)
leaves `F` invariant and acts freely on it, then `#K ∣ #F`. -/
theorem card_dvd_of_free (K : Finset G) (h0 : (0 : G) ∈ K)
    (hsub : ∀ a ∈ K, ∀ b ∈ K, -a + b ∈ K) :
    ∀ F : Finset β, (∀ k ∈ K, ∀ X ∈ F, k +ᵥ X ∈ F) →
      (∀ k ∈ K, ∀ X ∈ F, k +ᵥ X = X → k = 0) → K.card ∣ F.card := by
  intro F
  induction F using Finset.strongInduction with
  | H F ih =>
    intro hinv hfree
    rcases F.eq_empty_or_nonempty with hF | ⟨X, hX⟩
    · rw [hF, Finset.card_empty]
      exact Nat.dvd_zero _
    -- the orbit of `X`
    set O : Finset β := K.image fun k => k +ᵥ X with hOdef
    have hOF : O ⊆ F := by
      intro Y hY
      obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp hY
      exact hinv k hk X hX
    have hOcard : O.card = K.card := by
      apply Finset.card_image_of_injOn
      intro k hk k' hk' hkk
      have h1 : (-k' + k) +ᵥ X = X := by
        simp only at hkk
        rw [add_vadd, hkk, neg_vadd_vadd]
      have h2 : -k' + k = 0 := hfree _ (hsub k' hk' k hk) X hX h1
      calc k = k' + (-k' + k) := by rw [add_neg_cancel_left]
        _ = k' := by rw [h2, add_zero]
    have hXO : X ∈ O := Finset.mem_image.mpr ⟨0, h0, zero_vadd G X⟩
    have hlt : F \ O ⊂ F := Finset.sdiff_ssubset hOF ⟨X, hXO⟩
    have hinv' : ∀ k ∈ K, ∀ Y ∈ F \ O, k +ᵥ Y ∈ F \ O := by
      intro k hk Y hY
      obtain ⟨hYF, hYO⟩ := Finset.mem_sdiff.mp hY
      refine Finset.mem_sdiff.mpr ⟨hinv k hk Y hYF, fun hkY => hYO ?_⟩
      obtain ⟨k', hk', hk'X⟩ := Finset.mem_image.mp hkY
      refine Finset.mem_image.mpr ⟨-k + k', hsub k hk k' hk', ?_⟩
      rw [add_vadd, hk'X, neg_vadd_vadd]
    have hfree' : ∀ k ∈ K, ∀ Y ∈ F \ O, k +ᵥ Y = Y → k = 0 :=
      fun k hk Y hY => hfree k hk Y (Finset.mem_sdiff.mp hY).1
    have hdvd := ih (F \ O) hlt hinv' hfree'
    rw [← Finset.card_sdiff_add_card_eq_card hOF, hOcard]
    exact Nat.dvd_add hdvd (Nat.dvd_refl _)

end Action

section Lagrange

variable {G : Type*} [AddCommGroup G]

/-- Lagrange for a finite subgroup of an abelian group, given as a finset closed under addition and
negation: `#K • k = 0` for every `k ∈ K`. -/
theorem card_nsmul_eq_zero_of_closed (K : Finset G) (hadd : ∀ a ∈ K, ∀ b ∈ K, a + b ∈ K)
    (hneg : ∀ a ∈ K, -a ∈ K) {k : G} (hk : k ∈ K) : K.card • k = 0 := by
  have hsum : ∑ x ∈ K, (x + k) = ∑ x ∈ K, x := by
    refine Finset.sum_nbij' (fun x => x + k) (fun x => x + -k) ?_ ?_ ?_ ?_ ?_
    · intro x hx
      exact hadd x hx k hk
    · intro x hx
      exact hadd x hx (-k) (hneg k hk)
    · intro x _
      simp
    · intro x _
      simp
    · intro x _
      rfl
  rw [Finset.sum_add_distrib, Finset.sum_const] at hsum
  have := congrArg (fun t => t - ∑ x ∈ K, x) hsum
  simpa using this

end Lagrange

end PC88.Generic
