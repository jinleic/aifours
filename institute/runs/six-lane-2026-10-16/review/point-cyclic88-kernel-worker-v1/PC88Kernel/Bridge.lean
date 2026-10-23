import PC88Kernel.Canonical

/-!
# Relabelling bridge and the root theorem

* `relabel f X = f(X)` transports blocks along a bijection `f : V ≃ W`; `design_relabel`,
  `resolution_relabel` and `aut_relabel` show that `IsDesign`, `IsResolution` and
  `IsResolutionAut` are preserved (the automorphism is conjugated: if `f ∘ σ = τ ∘ f` then `τ` is
  an automorphism of the relabelled resolution).
* `exists_equiv_of_fullCycle`: if `σ` is a single cycle on all points of an 88-element type `V`,
  then for any point `x₀` the labelling `i ↦ σ^(i.val) x₀` is a bijection `e : ZMod 88 ≃ V` with
  `e (i + 1) = σ (e i)`, i.e. `e.symm ∘ σ = (· + 1) ∘ e.symm`.
* `target_of_canonical`: relabelling along `e.symm` turns a point-cyclic resolution on `V` into
  one on `ZMod 88` invariant under `x ↦ x + 1`, so `CanonicalTarget` implies `Target`.
* `target : Target` is the root.  `canonical_of_target` proves the converse specialisation
  (`x ↦ x + 1` is a full cycle on `ZMod 88`), so the canonical statement is exactly an instance.
-/

namespace PC88.Bridge

open PC88

universe u

section Transport

variable {V W : Type*} [DecidableEq V] [DecidableEq W]

/-- The image `f(X)` of a block under a relabelling `f : V ≃ W` of the points. -/
def relabel (f : V ≃ W) (X : Finset V) : Finset W := X.map f.toEmbedding

omit [DecidableEq V] [DecidableEq W] in
theorem relabel_injective (f : V ≃ W) : Function.Injective (relabel f) :=
  Finset.map_injective _

omit [DecidableEq V] [DecidableEq W] in
theorem mem_relabel (f : V ≃ W) {X : Finset V} {w : W} : w ∈ relabel f X ↔ f.symm w ∈ X :=
  Finset.mem_map_equiv

omit [DecidableEq V] in
theorem design_relabel (f : V ≃ W) {B : Finset (Finset V)} (hD : IsDesign B) :
    IsDesign (B.image (relabel f)) := by
  refine ⟨?_, ?_⟩
  · intro Y hY
    obtain ⟨X, hX, rfl⟩ := Finset.mem_image.mp hY
    rw [relabel, Finset.card_map]
    exact hD.1 X hX
  · intro x y hxy
    have hxy' : f.symm x ≠ f.symm y := fun h => hxy (f.symm.injective h)
    obtain ⟨X, ⟨hX, hxX, hyX⟩, huniq⟩ := hD.2 (f.symm x) (f.symm y) hxy'
    refine ⟨relabel f X, ⟨Finset.mem_image_of_mem _ hX, (mem_relabel f).mpr hxX,
      (mem_relabel f).mpr hyX⟩, ?_⟩
    rintro Y ⟨hY, hxY, hyY⟩
    obtain ⟨X', hX', rfl⟩ := Finset.mem_image.mp hY
    rw [huniq X' ⟨hX', (mem_relabel f).mp hxY, (mem_relabel f).mp hyY⟩]

omit [DecidableEq V] in
theorem resolution_relabel (f : V ≃ W) {B : Finset (Finset V)} {R : Finset (Finset (Finset V))}
    (hR : IsResolution B R) :
    IsResolution (B.image (relabel f)) (R.image fun P => P.image (relabel f)) := by
  refine ⟨?_, ?_⟩
  · intro P' hP'
    obtain ⟨P, hP, rfl⟩ := Finset.mem_image.mp hP'
    refine ⟨Finset.image_subset_image (hR.1 P hP).1, ?_⟩
    intro w
    obtain ⟨X, ⟨hX, hwX⟩, huniq⟩ := (hR.1 P hP).2 (f.symm w)
    refine ⟨relabel f X, ⟨Finset.mem_image_of_mem _ hX, (mem_relabel f).mpr hwX⟩, ?_⟩
    rintro Y ⟨hY, hwY⟩
    obtain ⟨X', hX', rfl⟩ := Finset.mem_image.mp hY
    rw [huniq X' ⟨hX', (mem_relabel f).mp hwY⟩]
  · intro Y hY
    obtain ⟨X, hX, rfl⟩ := Finset.mem_image.mp hY
    obtain ⟨P, ⟨hP, hXP⟩, huniq⟩ := hR.2 X hX
    refine ⟨P.image (relabel f), ⟨Finset.mem_image_of_mem _ hP, Finset.mem_image_of_mem _ hXP⟩, ?_⟩
    rintro P'' ⟨hP'', hXP''⟩
    obtain ⟨P', hP', rfl⟩ := Finset.mem_image.mp hP''
    obtain ⟨X', hX'P', hX'X⟩ := Finset.mem_image.mp hXP''
    have hXX : X' = X := relabel_injective f hX'X
    subst hXX
    rw [huniq P' ⟨hP', hX'P'⟩]

omit [DecidableEq V] [DecidableEq W] in
theorem blockImage_relabel (f : V ≃ W) {σ : Equiv.Perm V} {τ : Equiv.Perm W}
    (hcomm : ∀ x, f (σ x) = τ (f x)) (X : Finset V) :
    blockImage τ (relabel f X) = relabel f (blockImage σ X) := by
  simp only [blockImage, relabel, Finset.map_map]
  congr 1
  ext x
  simp [hcomm]

theorem aut_relabel (f : V ≃ W) {B : Finset (Finset V)} {R : Finset (Finset (Finset V))}
    {σ : Equiv.Perm V} {τ : Equiv.Perm W} (hcomm : ∀ x, f (σ x) = τ (f x))
    (hA : IsResolutionAut B R σ) :
    IsResolutionAut (B.image (relabel f)) (R.image fun P => P.image (relabel f)) τ := by
  have hc : blockImage τ ∘ relabel f = relabel f ∘ blockImage σ :=
    funext (blockImage_relabel f hcomm)
  refine ⟨?_, ?_⟩
  · rw [Finset.image_image, hc, ← Finset.image_image, hA.1]
  · intro P' hP'
    obtain ⟨P, hP, rfl⟩ := Finset.mem_image.mp hP'
    rw [Finset.image_image, hc, ← Finset.image_image]
    exact Finset.mem_image_of_mem _ (hA.2 P hP)

end Transport

/-- An 88-cycle on all points of an 88-element type is conjugate to `x ↦ x + 1` on `ZMod 88`:
for a point `x₀`, `e i = σ^(i.val) x₀` is a bijection with `e (i + 1) = σ (e i)`. -/
theorem exists_equiv_of_fullCycle {V : Type u} [Fintype V] [DecidableEq V]
    (hV : Fintype.card V = 88) {σ : Equiv.Perm V} (hσ : IsFullCycle σ) :
    ∃ e : ZMod 88 ≃ V, ∀ i : ZMod 88, e (i + 1) = σ (e i) := by
  obtain ⟨hcyc, hsupp⟩ := hσ
  have hord : orderOf σ = 88 := by
    rw [hcyc.orderOf, hsupp, Finset.card_univ, hV]
  obtain ⟨x₀⟩ : Nonempty V := Fintype.card_pos_iff.mp (by omega)
  have hstep : ∀ i : ZMod 88, (σ ^ (i + 1).val) x₀ = σ ((σ ^ i.val) x₀) := by
    intro i
    have : Fact (1 < 88) := ⟨by decide⟩
    have h1 : (i + 1).val = (i.val + 1) % 88 := by
      rw [ZMod.val_add, ZMod.val_one]
    have h2 : σ ^ ((i.val + 1) % 88) = σ ^ (i.val + 1) := by
      have hm := pow_mod_orderOf σ (i.val + 1)
      rw [hord] at hm
      exact hm
    rw [h1, h2, pow_succ', Equiv.Perm.mul_apply]
  have hsurj : Function.Surjective fun i : ZMod 88 => (σ ^ i.val) x₀ := by
    intro y
    have hx₀ : σ x₀ ≠ x₀ := by
      rw [← Equiv.Perm.mem_support, hsupp]
      exact Finset.mem_univ x₀
    have hy : σ y ≠ y := by
      rw [← Equiv.Perm.mem_support, hsupp]
      exact Finset.mem_univ y
    obtain ⟨n, hn, hny⟩ := (hcyc.sameCycle hx₀ hy).exists_pow_eq'
    refine ⟨(n : ZMod 88), ?_⟩
    simp only
    rw [ZMod.val_natCast, Nat.mod_eq_of_lt (hord ▸ hn)]
    exact hny
  have hbij : Function.Bijective fun i : ZMod 88 => (σ ^ i.val) x₀ := by
    rw [Fintype.bijective_iff_surjective_and_card]
    exact ⟨hsurj, by rw [ZMod.card, hV]⟩
  exact ⟨Equiv.ofBijective _ hbij, hstep⟩

/-- `CanonicalTarget` implies `Target` (relabelling along an arbitrary 88-cycle). -/
theorem target_of_canonical (hcan : CanonicalTarget) : Target.{u} := by
  intro V _ _ hV B R hPC
  obtain ⟨hD, hR, σ, hσ, hA⟩ := hPC
  obtain ⟨e, he⟩ := exists_equiv_of_fullCycle hV hσ
  have hcomm : ∀ x : V, e.symm (σ x) = Equiv.addRight (1 : ZMod 88) (e.symm x) := by
    intro x
    obtain ⟨i, rfl⟩ := e.surjective x
    rw [Equiv.symm_apply_apply, Equiv.coe_addRight, ← he, Equiv.symm_apply_apply]
  exact hcan _ _ (design_relabel e.symm hD) (resolution_relabel e.symm hR)
    (aut_relabel e.symm hcomm hA)

/-- **Root theorem.** For every 88-point type, no `2-(88,4,1)` design has a point-cyclic
resolution. -/
theorem target : Target.{u} :=
  target_of_canonical Canonical.canonicalTarget

theorem addRight_one_pow_apply (n : ℕ) (x : ZMod 88) :
    ((Equiv.addRight (1 : ZMod 88)) ^ n) x = x + n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', Equiv.Perm.mul_apply, ih]
    show x + (n : ZMod 88) + 1 = x + ((n + 1 : ℕ) : ZMod 88)
    rw [Nat.cast_succ, add_assoc]

/-- `x ↦ x + 1` permutes the 88 points of `ZMod 88` in one cycle. -/
theorem isFullCycle_addRight_one : IsFullCycle (Equiv.addRight (1 : ZMod 88)) := by
  have hmove : ∀ x : ZMod 88, Equiv.addRight (1 : ZMod 88) x ≠ x := by
    intro x hx
    rw [Equiv.coe_addRight] at hx
    have h10 : (1 : ZMod 88) = 0 := by
      have := congrArg (fun t => t - x) hx
      simpa using this
    exact absurd h10 (by decide)
  refine ⟨⟨0, hmove 0, fun y _ => ⟨(y.val : ℤ), ?_⟩⟩, ?_⟩
  · rw [zpow_natCast, addRight_one_pow_apply, zero_add, ZMod.natCast_zmod_val]
  · apply Finset.eq_univ_of_forall
    intro x
    rw [Equiv.Perm.mem_support]
    exact hmove x

/-- Converse specialisation: `Target` (at universe 0) implies `CanonicalTarget`. -/
theorem canonical_of_target (ht : Target.{0}) : CanonicalTarget := by
  intro B R hD hR hA
  exact ht (ZMod 88) (ZMod.card 88) B R ⟨hD, hR, _, isFullCycle_addRight_one, hA⟩

end PC88.Bridge
