import Mathlib

/-!
# Finite residual cosets: a checked finite-span core for semifilter Q2/Q3

All word orbits are literal finite ranges, including the empty word. Recognition
is never defined by the desired normal form. A finite-state lifting theorem is
proved over arbitrary finite coefficient rings, then applied to quotient modules
to prove regularity reflection, saturation and a mutual-inclusion criterion.

The F2-series instantiation uses Mathlib Language.leftQuotient and Myhill-Nerode
for ordinary regularity. Arithmetic is on series valued in ZMod 2; Language's
union and existential concatenation operations are never used as parity products.

Partial formalization relative to the original problem: the source semifilter
axioms and agreement-congruence translation, parity normal form and its Q3
finite-expression expansion, and filter classification are written-only bridges
in candidate-proof.md. The three roots below are stated precisely in claims.json.
-/

namespace Semifilter

open Set

universe u v w z

section LinearOrbits

variable {R : Type u} [Ring R]
variable {A : Type v} [AddCommGroup A] [Module R A]
variable {X : Type w}

/-- Read a word from left to right using linear letter transitions. -/
def act (d : X → A →ₗ[R] A) : List X → A →ₗ[R] A
  | [] => LinearMap.id
  | a :: w => (act d w).comp (d a)

@[simp] theorem act_nil (d : X → A →ₗ[R] A) (s : A) : act d [] s = s := rfl
@[simp] theorem act_cons (d : X → A →ₗ[R] A) (a : X) (w : List X) (s : A) :
    act d (a :: w) s = act d w (d a s) := rfl

theorem act_append (d : X → A →ₗ[R] A) (u v : List X) (s : A) :
    act d (u ++ v) s = act d v (act d u s) := by
  induction u generalizing s with
  | nil => rfl
  | cons a u ih => exact ih (d a s)

/-- Actual orbit finiteness, not a presentation by a desired normal form. -/
def FiniteOrbit (d : X → A →ₗ[R] A) (s : A) : Prop :=
  (Set.range (fun w : List X => act d w s)).Finite

theorem finiteOrbit_zero (d : X → A →ₗ[R] A) : FiniteOrbit d 0 := by
  simpa [FiniteOrbit] using (Set.finite_singleton (0 : A))

theorem finiteOrbit_add (d : X → A →ₗ[R] A) {s t : A}
    (hs : FiniteOrbit d s) (ht : FiniteOrbit d t) : FiniteOrbit d (s + t) := by
  refine ((hs.prod ht).image (fun p : A × A => p.1 + p.2)).subset ?_
  rintro _ ⟨w, rfl⟩
  exact ⟨(act d w s, act d w t), ⟨⟨w, rfl⟩, ⟨w, rfl⟩⟩, by simp⟩

theorem finiteOrbit_smul (d : X → A →ₗ[R] A) (c : R) {s : A}
    (hs : FiniteOrbit d s) : FiniteOrbit d (c • s) := by
  refine (hs.image (fun t => c • t)).subset ?_
  rintro _ ⟨w, rfl⟩
  exact ⟨act d w s, ⟨w, rfl⟩, by simp⟩

/-- Finite orbit vectors form a submodule; no intersection closure is used. -/
def locallyFinite (d : X → A →ₗ[R] A) : Submodule R A where
  carrier := {s | FiniteOrbit d s}
  zero_mem' := finiteOrbit_zero d
  add_mem' := finiteOrbit_add d
  smul_mem' := finiteOrbit_smul d

theorem finiteOrbit_step (d : X → A →ₗ[R] A) {s : A}
    (hs : FiniteOrbit d s) (a : X) : FiniteOrbit d (d a s) := by
  apply hs.subset
  rintro _ ⟨w, rfl⟩
  exact ⟨a :: w, rfl⟩

/-- The finite-state error mechanism: finite error orbits imply finite state-vector
orbits, by a finite invariant span over a finite coefficient ring. -/
theorem finiteOrbit_of_finiteState [Finite R] [Finite X]
    {Q : Type z} [Finite Q] (d : X → A →ₗ[R] A)
    (S : Q → A) (δ : Q → X → Q)
    (hE : ∀ q a, FiniteOrbit d (d a (S q) - S (δ q a))) :
    ∀ q, FiniteOrbit d (S q) := by
  classical
  let E (q : Q) (a : X) := d a (S q) - S (δ q a)
  let G : Set A := Set.range S ∪ ⋃ q, ⋃ a, Set.range (fun w : List X => act d w (E q a))
  have hG : G.Finite := (Set.finite_range S).union
    (Set.finite_iUnion fun q => Set.finite_iUnion fun a => hE q a)
  let P : Submodule R A := Submodule.span R G
  have hP : (P : Set A).Finite := hG.submoduleSpan (R := R)
  have hS (q : Q) : S q ∈ P := Submodule.subset_span (Or.inl ⟨q, rfl⟩)
  have hErr (q : Q) (a : X) (w : List X) : act d w (E q a) ∈ P := by
    apply Submodule.subset_span
    exact Or.inr (Set.mem_iUnion.mpr ⟨q, Set.mem_iUnion.mpr ⟨a, ⟨w, rfl⟩⟩⟩)
  have hstable (a : X) : P ≤ P.comap (d a) := by
    apply Submodule.span_le.mpr
    intro y hy
    rcases hy with ⟨q, rfl⟩ | hy
    · change d a (S q) ∈ P
      have hh := P.add_mem (hS (δ q a)) (hErr q a [])
      simpa [E] using hh
    · rcases Set.mem_iUnion.mp hy with ⟨q, hy⟩
      rcases Set.mem_iUnion.mp hy with ⟨b, w, rfl⟩
      change d a (act d w (E q b)) ∈ P
      simpa [act_append] using hErr q b (w ++ [a])
  intro q
  apply hP.subset
  rintro _ ⟨w, rfl⟩
  induction w using List.reverseRecOn with
  | nil => exact hS q
  | append_singleton w a ih =>
    simpa [act_append] using hstable a ih

variable {B : Type*} [AddCommGroup B] [Module R B]

theorem act_map (d : X → A →ₗ[R] A) (e : X → B →ₗ[R] B)
    (π : A →ₗ[R] B) (hπ : ∀ a s, π (d a s) = e a (π s))
    (w : List X) (s : A) : π (act d w s) = act e w (π s) := by
  induction w generalizing s with
  | nil => rfl
  | cons a w ih => simpa [hπ] using ih (d a s)

theorem finiteOrbit_map (d : X → A →ₗ[R] A) (e : X → B →ₗ[R] B)
    (π : A →ₗ[R] B) (hπ : ∀ a s, π (d a s) = e a (π s))
    {s : A} (hs : FiniteOrbit d s) : FiniteOrbit e (π s) := by
  refine (hs.image π).subset ?_
  rintro _ ⟨w, rfl⟩
  exact ⟨act d w s, ⟨w, rfl⟩, act_map d e π hπ w s⟩

/-- Lift a finite orbit through a linear intertwining map when every kernel
vector has finite orbit. Finite representatives and their errors are constructed. -/
theorem finiteOrbit_lift [Finite R] [Finite X]
    (d : X → A →ₗ[R] A) (e : X → B →ₗ[R] B)
    (π : A →ₗ[R] B) (hπ : ∀ a s, π (d a s) = e a (π s))
    (hk : ∀ s, π s = 0 → FiniteOrbit d s)
    (t : A) (ht : FiniteOrbit e (π t)) : FiniteOrbit d t := by
  classical
  let Q := Set.range (fun w : List X => act e w (π t))
  letI : Finite Q := ht.to_subtype
  let q₀ : Q := ⟨π t, ⟨[], rfl⟩⟩
  let r (q : Q) : List X := if q = q₀ then [] else Classical.choose q.property
  have hr (q : Q) : act e (r q) (π t) = q.val := by
    dsimp [r]
    split_ifs with h
    · subst q
      rfl
    · exact Classical.choose_spec q.property
  let S (q : Q) : A := act d (r q) t
  have hS (q : Q) : π (S q) = q.val := (act_map d e π hπ (r q) t).trans (hr q)
  let δ (q : Q) (a : X) : Q :=
    ⟨e a q.val, r q ++ [a], by simpa [act_append, hr q]⟩
  have hE (q : Q) (a : X) : FiniteOrbit d (d a (S q) - S (δ q a)) := by
    apply hk
    simp only [map_sub, hπ, hS]
    exact sub_self _
  have hf := finiteOrbit_of_finiteState d S δ hE q₀
  simpa [S, r] using hf

end LinearOrbits

section Saturation

variable {R : Type u} [Ring R]
variable {A : Type v} [AddCommGroup A] [Module R A]
variable {X : Type w}

/-- All letter maps preserve the submodule. This implies all word maps do. -/
def Invariant (d : X → A →ₗ[R] A) (V : Submodule R A) : Prop :=
  ∀ a, V ≤ V.comap (d a)

def quotientStep (d : X → A →ₗ[R] A) (V : Submodule R A) (hV : Invariant d V) :
    X → (A ⧸ V) →ₗ[R] (A ⧸ V) :=
  fun a => V.mapQ V (d a) (hV a)

@[simp] theorem quotientStep_mk (d : X → A →ₗ[R] A) (V : Submodule R A)
    (hV : Invariant d V) (a : X) (s : A) :
    quotientStep d V hV a (V.mkQ s) = V.mkQ (d a s) := rfl

/-- Saturation is defined by finite actual residual-orbit images in the quotient. -/
def saturate (d : X → A →ₗ[R] A) (V : Submodule R A) (hV : Invariant d V) :
    Submodule R A :=
  (locallyFinite (quotientStep d V hV)).comap V.mkQ

theorem mem_saturate_iff (d : X → A →ₗ[R] A) (V : Submodule R A)
    (hV : Invariant d V) (s : A) :
    s ∈ saturate d V hV ↔
    (Set.range (fun w : List X => V.mkQ (act d w s))).Finite := by
  have h : (fun w : List X => V.mkQ (act d w s)) =
      (fun w => act (quotientStep d V hV) w (V.mkQ s)) := by
    funext w
    exact act_map d (quotientStep d V hV) V.mkQ (fun _ _ => rfl) w s
  rw [h]
  rfl

theorem invariant_saturate (d : X → A →ₗ[R] A) (V : Submodule R A)
    (hV : Invariant d V) : Invariant d (saturate d V hV) := by
  intro a s hs
  change FiniteOrbit (quotientStep d V hV) (V.mkQ (d a s))
  rw [← quotientStep_mk d V hV a s]
  exact finiteOrbit_step _ hs a

theorem le_saturate (d : X → A →ₗ[R] A) (V : Submodule R A)
    (hV : Invariant d V) : V ≤ saturate d V hV := by
  intro s hs
  change FiniteOrbit (quotientStep d V hV) (V.mkQ s)
  have hh : V.mkQ s = 0 := (Submodule.Quotient.mk_eq_zero V).mpr hs
  rw [hh]
  exact finiteOrbit_zero _

theorem locallyFinite_le_saturate (d : X → A →ₗ[R] A) (V : Submodule R A)
    (hV : Invariant d V) : locallyFinite d ≤ saturate d V hV := by
  intro s hs
  exact finiteOrbit_map d (quotientStep d V hV) V.mkQ (fun _ _ => rfl) hs

theorem saturate_mono (d : X → A →ₗ[R] A) (V W : Submodule R A)
    (hV : Invariant d V) (hW : Invariant d W) (hVW : V ≤ W) :
    saturate d V hV ≤ saturate d W hW := by
  let π : (A ⧸ V) →ₗ[R] (A ⧸ W) := V.factor hVW
  have hπ (a : X) (s : A ⧸ V) :
      π (quotientStep d V hV a s) = quotientStep d W hW a (π s) := by
    induction s using Submodule.Quotient.induction_on with
    | _ s => rfl
  intro s hs
  exact finiteOrbit_map _ _ π hπ hs

/-- Q2's exact finite-residual mechanism, over every finite coefficient ring. -/
theorem saturate_eq_locallyFinite_iff [Finite R] [Finite X]
    (d : X → A →ₗ[R] A) (V : Submodule R A) (hV : Invariant d V) :
    saturate d V hV = locallyFinite d ↔ V ≤ locallyFinite d := by
  constructor
  · intro h
    rw [← h]
    exact le_saturate d V hV
  · intro h
    apply le_antisymm
    · intro s hs
      apply finiteOrbit_lift d (quotientStep d V hV) V.mkQ (fun _ _ => rfl) _ s hs
      intro t ht
      exact h ((Submodule.Quotient.mk_eq_zero V).mp ht)
    · exact locallyFinite_le_saturate d V hV

/-- Idempotence is proved by lifting through A/V -> A/C(V), not assumed. -/
theorem saturate_idempotent [Finite R] [Finite X]
    (d : X → A →ₗ[R] A) (V : Submodule R A) (hV : Invariant d V) :
    saturate d (saturate d V hV) (invariant_saturate d V hV) = saturate d V hV := by
  let W := saturate d V hV
  let hW : Invariant d W := invariant_saturate d V hV
  let π : (A ⧸ V) →ₗ[R] (A ⧸ W) := V.factor (le_saturate d V hV)
  have hπ (a : X) (s : A ⧸ V) :
      π (quotientStep d V hV a s) = quotientStep d W hW a (π s) := by
    induction s using Submodule.Quotient.induction_on with
    | _ s => rfl
  have hk (s : A ⧸ V) (hs : π s = 0) : FiniteOrbit (quotientStep d V hV) s := by
    induction s using Submodule.Quotient.induction_on with
    | _ t =>
      have ht : t ∈ W := (Submodule.Quotient.mk_eq_zero W).mp hs
      exact ht
  apply le_antisymm
  · intro t ht
    exact finiteOrbit_lift _ _ π hπ hk (V.mkQ t) ht
  · exact le_saturate d W hW

/-- Q3's mutual generator test for finite residual-orbit classes. -/
theorem saturate_eq_iff_mutual [Finite R] [Finite X]
    (d : X → A →ₗ[R] A) (V W : Submodule R A)
    (hV : Invariant d V) (hW : Invariant d W) :
    saturate d V hV = saturate d W hW ↔
    V ≤ saturate d W hW ∧ W ≤ saturate d V hV := by
  constructor
  · intro h
    exact ⟨h ▸ le_saturate d V hV, h.symm ▸ le_saturate d W hW⟩
  · rintro ⟨hVW, hWV⟩
    apply le_antisymm
    · have hh := saturate_mono d V (saturate d W hW) hV
        (invariant_saturate d W hW) hVW
      rwa [saturate_idempotent] at hh
    · have hh := saturate_mono d W (saturate d V hV) hW
        (invariant_saturate d V hV) hWV
      rwa [saturate_idempotent] at hh

end Saturation

section Languages

variable {X : Type w}

abbrev Series (X : Type w) := List X → ZMod 2

def letter : X → Series X →ₗ[ZMod 2] Series X := fun a =>
  { toFun := fun f v => f (a :: v)
    map_add' := fun _ _ => rfl
    map_smul' := fun _ _ => rfl }

def residual (f : Series X) (u : List X) : Series X := fun v => f (u ++ v)

theorem act_letter (u : List X) (f : Series X) :
    act letter u f = residual f u := by
  induction u generalizing f with
  | nil => rfl
  | cons a u ih =>
    rw [act_cons, ih]
    rfl

noncomputable def characteristic (T : Language X) : Series X :=
  by
    classical
    exact fun w => if w ∈ T then 1 else 0

theorem characteristic_injective : Function.Injective (characteristic (X := X)) := by
  intro T U h
  ext w
  have hh := congr_fun h w
  by_cases ht : w ∈ T <;> by_cases hu : w ∈ U <;> simp_all [characteristic]

theorem act_characteristic (T : Language X) (u : List X) :
    act letter u (characteristic T) = characteristic (T.leftQuotient u) := by
  rw [act_letter]
  rfl

/-- Faithful bridge to Mathlib's ordinary DFA regularity via actual left quotients. -/
theorem finiteOrbit_characteristic_iff_regular (T : Language X) :
    FiniteOrbit letter (characteristic T) ↔ T.IsRegular := by
  rw [Language.isRegular_iff_finite_range_leftQuotient]
  have hh : (fun w : List X => act letter w (characteristic T)) =
      characteristic ∘ T.leftQuotient := by
    funext w
    exact act_characteristic T w
  rw [FiniteOrbit, hh, Set.range_comp]
  exact Set.finite_image_iff characteristic_injective.injOn

/-- The semantic Q2 criterion in the invariant F2-series formulation.
The source-semifilter complement correspondence remains a written bridge. -/
theorem series_q2 [Finite X] (V : Submodule (ZMod 2) (Series X))
    (hV : Invariant letter V) :
    saturate letter V hV = locallyFinite letter ↔ V ≤ locallyFinite letter :=
  saturate_eq_locallyFinite_iff letter V hV

/-- Semantic saturation for actual residual cosets, including the empty alphabet. -/
theorem series_saturation [Finite X] (V : Submodule (ZMod 2) (Series X))
    (hV : Invariant letter V) :
    saturate letter (saturate letter V hV) (invariant_saturate letter V hV) =
      saturate letter V hV := by sorry

/-- Semantic mutual-inclusion criterion. The parity-expression expansion is written only. -/
theorem series_q3 [Finite X] (V W : Submodule (ZMod 2) (Series X))
    (hV : Invariant letter V) (hW : Invariant letter W) :
    saturate letter V hV = saturate letter W hW ↔
      V ≤ saturate letter W hW ∧ W ≤ saturate letter V hV := by sorry

/-- Each F2 series is the characteristic series of its support. -/
def support (f : Series X) : Language X := {w | f w = 1}

theorem characteristic_support (f : Series X) : characteristic (support f) = f := by
  classical
  funext w
  simp only [characteristic]
  have hz (z : ZMod 2) : z = 0 ∨ z = 1 := by
    fin_cases z
    · exact Or.inl rfl
    · exact Or.inr rfl
  rcases hz (f w) with h | h
  · have hm : w ∉ support f := by
      intro hm
      change f w = 1 at hm
      simp [h] at hm
    simp [hm, h]
  · have hm : w ∈ support f := h
    simp [hm, h]

theorem finiteOrbit_iff_support_regular (f : Series X) :
    FiniteOrbit letter f ↔ (support f).IsRegular := by
  simpa only [characteristic_support] using
    finiteOrbit_characteristic_iff_regular (support f)

/-- This identifies the defined saturation with the requested finite residual cosets. -/
theorem series_mem_iff_finite_residual_cosets (V : Submodule (ZMod 2) (Series X))
    (hV : Invariant letter V) (f : Series X) :
    f ∈ saturate letter V hV ↔
      (Set.range (fun u : List X => V.mkQ (residual f u))).Finite := by
  simpa only [act_letter] using mem_saturate_iff letter V hV f

/-- Ordinary-language form of the translated Q2 criterion. -/
theorem series_regular_criterion [Finite X] (V : Submodule (ZMod 2) (Series X))
    (hV : Invariant letter V) :
    (∀ T : Language X, characteristic T ∈ saturate letter V hV ↔ T.IsRegular) ↔
      ∀ f ∈ V, (support f).IsRegular := by sorry

end Languages

end Semifilter

-- Claimed theorem roots only; no helper-count claim is made.
