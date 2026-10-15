import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Image
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Set.Pairwise.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
Faithful finite designs and sound development from mixed invariant/transversal seeds.
No existence of a seed package is asserted. In particular this is not a proof of
universal LKTS existence, nor a certificate for order 57 or 87.
-/
namespace Kirkman

abbrev Sized (v k : ℕ) := {s : Finset (Fin v) // s.card = k}
abbrev Triple (v : ℕ) := Sized v 3
abbrev Pair (v : ℕ) := Sized v 2
abbrev Blocks (v : ℕ) := Set (Triple v)

/-- Exactly one unordered triple completes every unordered pair. -/
def IsSTS {v : ℕ} (B : Blocks v) : Prop :=
  ∀ p : Pair v, ∃! b : Triple v, b ∈ B ∧ p.val ⊆ b.val

/-- A parallel class partitions the actual point set. -/
def IsParallelClass {v : ℕ} (P : Blocks v) : Prop :=
  ∀ x : Fin v, ∃! b : Triple v, b ∈ P ∧ x ∈ b.val

/-- A resolution has genuine point partitions, disjoint block classes, and exact union. -/
def IsResolution {v : ℕ} (B : Blocks v)
    (R : Fin ((v - 1) / 2) → Blocks v) : Prop :=
  (∀ c, IsParallelClass (R c)) ∧
  Pairwise (fun c d => Disjoint (R c) (R d)) ∧ (⋃ c, R c) = B

def IsKTS {v : ℕ} (B : Blocks v) : Prop :=
  IsSTS B ∧ ∃ R : Fin ((v - 1) / 2) → Blocks v, IsResolution B R

/-- A large set includes the exact constituent count, disjointness and all triples. -/
def IsLKTS {v : ℕ} {I : Type} [Fintype I] (B : I → Blocks v) : Prop :=
  Fintype.card I = v - 2 ∧ (∀ i, IsKTS (B i)) ∧
  Pairwise (fun i j => Disjoint (B i) (B j)) ∧ (⋃ i, B i) = Set.univ

/-- The book quantifier is t >= 1. No symmetry restriction is included. -/
def FullGoal : Prop :=
  ∀ t : ℕ, 1 ≤ t → ∃ B : Fin (6 * t + 3 - 2) → Blocks (6 * t + 3), IsLKTS B

/-- Relabel a genuine k-subset by a permutation of the points. -/
def renameSized {v : ℕ} (e : Equiv.Perm (Fin v)) (k : ℕ) : Sized v k ≃ Sized v k where
  toFun b := ⟨b.val.map e.toEmbedding, by simpa using b.property⟩
  invFun b := ⟨b.val.map e.symm.toEmbedding, by simpa using b.property⟩
  left_inv b := by
    apply Subtype.ext
    ext x
    simp only [Finset.mem_map_equiv, Equiv.symm_symm, Equiv.symm_apply_apply]
  right_inv b := by
    apply Subtype.ext
    ext x
    simp only [Finset.mem_map_equiv, Equiv.symm_symm, Equiv.apply_symm_apply]

@[simp] theorem mem_renameSized {v k : ℕ} (e : Equiv.Perm (Fin v))
    (b : Sized v k) (x : Fin v) :
    x ∈ (renameSized e k b).val ↔ e.symm x ∈ b.val :=
  Finset.mem_map_equiv

def imageBlocks {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v) : Blocks v :=
  renameSized e 3 '' B

theorem pair_subset_rename_iff {v : ℕ} (e : Equiv.Perm (Fin v))
    (p : Pair v) (b : Triple v) :
    p.val ⊆ (renameSized e 3 b).val ↔ (renameSized e.symm 2 p).val ⊆ b.val :=
  Finset.map_symm_subset.symm

/-- Point permutations preserve exact pair coverage, including uniqueness. -/
theorem isSTS_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (h : IsSTS B) : IsSTS (imageBlocks e B) := by
  intro p
  obtain ⟨b, hb, hu⟩ := h (renameSized e.symm 2 p)
  refine ⟨renameSized e 3 b, ⟨⟨b, hb.1, rfl⟩,
    (pair_subset_rename_iff e p b).mpr hb.2⟩, ?_⟩
  intro c hc
  obtain ⟨d, hd, rfl⟩ := hc.1
  exact congrArg (renameSized e 3)
    (hu d ⟨hd, (pair_subset_rename_iff e p d).mp hc.2⟩)

/-- Point permutations preserve point partitions, including uniqueness. -/
theorem parallel_image {v : ℕ} (e : Equiv.Perm (Fin v)) (P : Blocks v)
    (h : IsParallelClass P) : IsParallelClass (imageBlocks e P) := by
  intro x
  obtain ⟨b, hb, hu⟩ := h (e.symm x)
  refine ⟨renameSized e 3 b, ⟨⟨b, hb.1, rfl⟩,
    (mem_renameSized e b x).mpr hb.2⟩, ?_⟩
  intro c hc
  obtain ⟨d, hd, rfl⟩ := hc.1
  exact congrArg (renameSized e 3) (hu d ⟨hd, (mem_renameSized e d x).mp hc.2⟩)

/-- Both the exact class union and class disjointness survive development. -/
theorem resolution_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (R : Fin ((v - 1) / 2) → Blocks v) (h : IsResolution B R) :
    IsResolution (imageBlocks e B) (fun c => imageBlocks e (R c)) := by
  refine ⟨fun c => parallel_image e (R c) (h.1 c), ?_, ?_⟩
  · intro c d hcd
    apply Set.disjoint_left.mpr
    rintro b ⟨x, hx, hxb⟩ ⟨y, hy, hyb⟩
    have heq : x = y := (renameSized e 3).injective (hxb.trans hyb.symm)
    subst y
    exact Set.disjoint_left.mp (h.2.1 hcd) hx hy
  · ext b
    simp only [Set.mem_iUnion]
    constructor
    · rintro ⟨c, x, hx, hxb⟩
      refine ⟨x, ?_, hxb⟩
      rw [← h.2.2]
      exact Set.mem_iUnion.mpr ⟨c, hx⟩
    · rintro ⟨x, hx, hxb⟩
      rw [← h.2.2] at hx
      obtain ⟨c, hc⟩ := Set.mem_iUnion.mp hx
      exact ⟨c, x, hc, hxb⟩

theorem isKTS_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (h : IsKTS B) : IsKTS (imageBlocks e B) := by
  obtain ⟨R, hR⟩ := h.2
  exact ⟨isSTS_image e B h.1, fun c => imageBlocks e (R c), resolution_image e B R hR⟩

/-- Owners are input constituents, not the eventual translated constituents. -/
def ownerOrbits {v : ℕ} {F A Ω : Type} (key : Triple v → Ω)
    (fixed : F → Blocks v) (base : A → Blocks v) : F ⊕ A → Set Ω
  | Sum.inl f => key '' fixed f
  | Sum.inr a => key '' base a

def developed {v : ℕ} {F A G : Type} (act : G → Equiv.Perm (Fin v))
    (fixed : F → Blocks v) (base : A → Blocks v) : F ⊕ (A × G) → Blocks v
  | Sum.inl f => fixed f
  | Sum.inr ag => imageBlocks (act ag.2) (base ag.1)

/--
Mixed-orbit certificate soundness. In the released57 route F has17 invariant
constituents (16 retained plus the jointly chosen replacement), A has2 free
bases, and G has19 elements. In the surviving87 route the sizes are27,2,29.

The hypotheses are local seed pair coverage/resolution, orbit ownership,
transversality and actual point permutations. Disjointness and global triple
coverage of the developed family are conclusions, not certificate fields.
The generic action hypotheses can be checked or proved independently; the concrete
C19 and C29 corollaries below prove them. No unbuilt OAI module is imported. A group law is unnecessary for this criterion:
its orbit-fiber and freeness hypotheses contain exactly the needed action facts.
Ownership is required only for labels attained by genuine triples, so the codomain
may contain unused labels without imposing a hidden surjectivity condition.
-/
theorem development_sound {v : ℕ} {F A G Ω : Type}
    [Fintype F] [Fintype A] [Fintype G]
    (act : G → Equiv.Perm (Fin v)) (key : Triple v → Ω)
    (fixed : F → Blocks v) (base : A → Blocks v)
    (hcount : Fintype.card F + Fintype.card A * Fintype.card G = v - 2)
    (hfixed : ∀ f, IsKTS (fixed f)) (hbase : ∀ a, IsKTS (base a))
    (hinvariant : ∀ f g b, b ∈ fixed f → renameSized (act g) 3 b ∈ fixed f)
    (hkey : ∀ g b, key (renameSized (act g) 3 b) = key b)
    (hfiber : ∀ b c, key b = key c → ∃ g, renameSized (act g) 3 b = c)
    (hfree : ∀ b g h, renameSized (act g) 3 b = renameSized (act h) 3 b → g = h)
    (htrans : ∀ a b c, b ∈ base a → c ∈ base a → key b = key c → b = c)
    (howners : ∀ b : Triple v, ∃! i : F ⊕ A, key b ∈ ownerOrbits key fixed base i) :
    IsLKTS (developed act fixed base) := by
  have own_unique : ∀ b (i j : F ⊕ A),
      key b ∈ ownerOrbits key fixed base i → key b ∈ ownerOrbits key fixed base j → i = j := by
    intro b i j hi hj
    obtain ⟨k, _, hu⟩ := howners b
    exact (hu i hi).trans (hu j hj).symm
  have owner_of : ∀ (i : F ⊕ (A × G)) b, b ∈ developed act fixed base i →
      key b ∈ ownerOrbits key fixed base (i.elim Sum.inl (fun ag => Sum.inr ag.1)) := by
    intro i b hb
    cases i with
    | inl f => exact ⟨b, hb, rfl⟩
    | inr ag =>
      obtain ⟨c, hc, rfl⟩ := hb
      exact ⟨c, hc, (hkey ag.2 c).symm⟩
  have index_unique : ∀ (i j : F ⊕ (A × G)) b,
      b ∈ developed act fixed base i → b ∈ developed act fixed base j → i = j := by
    intro i j b hi hj
    have ho := own_unique b _ _ (owner_of i b hi) (owner_of j b hj)
    cases i with
    | inl f =>
      cases j with
      | inl f' => exact congrArg Sum.inl (Sum.inl.inj ho)
      | inr ag => cases ho
    | inr ag =>
      cases j with
      | inl f => cases ho
      | inr ag' =>
        have ha : ag.1 = ag'.1 := Sum.inr.inj ho
        rcases ag with ⟨a,g⟩
        rcases ag' with ⟨a',g'⟩
        dsimp at ha
        subst a'
        obtain ⟨c, hc, hcb⟩ := hi
        obtain ⟨d, hd, hdb⟩ := hj
        have hk : key c = key d := by
          rw [← hkey g c, ← hkey g' d, hcb, hdb]
        have hcd := htrans a c d hc hd hk
        subst d
        have hg : g = g' := hfree c g g' (hcb.trans hdb.symm)
        subst g'
        rfl
  refine ⟨?_, ?_, ?_, ?_⟩
  · simpa only [Fintype.card_sum, Fintype.card_prod] using hcount
  · intro i
    cases i with
    | inl f => exact hfixed f
    | inr ag => exact isKTS_image (act ag.2) (base ag.1) (hbase ag.1)
  · intro i j hij
    apply Set.disjoint_left.mpr
    intro b hi hj
    exact hij (index_unique i j b hi hj)
  · apply Set.eq_univ_of_forall
    intro b
    obtain ⟨i, hi, _⟩ := howners b
    cases i with
    | inl f =>
      obtain ⟨c, hc, hcb⟩ := hi
      obtain ⟨g, hg⟩ := hfiber c b hcb
      exact Set.mem_iUnion.mpr ⟨Sum.inl f, hg ▸ hinvariant f g c hc⟩
    | inr a =>
      obtain ⟨c, hc, hcb⟩ := hi
      obtain ⟨g, hg⟩ := hfiber c b hcb
      exact Set.mem_iUnion.mpr ⟨Sum.inr (a,g), c, hc, hg⟩

/-- A concrete two-pair collision prevents an STS; used by the broken control. -/
theorem sts_pair_unique {v : ℕ} (B : Blocks v) (h : IsSTS B)
    (p : Pair v) (b c : Triple v) (hb : b ∈ B) (hc : c ∈ B)
    (hpb : p.val ⊆ b.val) (hpc : p.val ⊆ c.val) : b = c := by
  obtain ⟨d, _, hu⟩ := h p
  exact (hu b ⟨hb,hpb⟩).trans (hu c ⟨hc,hpc⟩).symm

/-- Every genuine triple has an actual two-element subset. -/
theorem triple_has_pair {v : ℕ} (b : Triple v) : ∃ p : Pair v, p.val ⊆ b.val := by
  have hcard : 2 ≤ b.val.card := by rw [b.property]; decide
  obtain ⟨p, hp, hpcard⟩ := Finset.exists_subset_card_eq hcard
  exact ⟨⟨p, hpcard⟩, hp⟩

/--
Soundness of the concrete selected-row convention: pair columns and
(class,point) columns are exact-one columns. This theorem derives all the
block/class uniqueness requirements, rather than assuming IsKTS as input.
-/
theorem resolved_rows_sound {v n : ℕ}
    (block : Fin n → Triple v) (color : Fin n → Fin ((v - 1) / 2))
    (selected : Finset (Fin n))
    (hpairs : ∀ p : Pair v, ∃! r : Fin n, r ∈ selected ∧ p.val ⊆ (block r).val)
    (hpoints : ∀ c x, ∃! r : Fin n,
      r ∈ selected ∧ color r = c ∧ x ∈ (block r).val) :
    IsKTS {b | ∃ r ∈ selected, block r = b} := by
  have row_unique : ∀ r s, r ∈ selected → s ∈ selected → block r = block s → r = s := by
    intro r s hr hs heq
    obtain ⟨p, hp⟩ := triple_has_pair (block r)
    obtain ⟨q, _, hu⟩ := hpairs p
    have hs' : p.val ⊆ (block s).val := heq ▸ hp
    exact (hu r ⟨hr,hp⟩).trans (hu s ⟨hs,hs'⟩).symm
  constructor
  · intro p
    obtain ⟨r, hr, hu⟩ := hpairs p
    refine ⟨block r, ⟨⟨r,hr.1,rfl⟩,hr.2⟩, ?_⟩
    intro b hb
    obtain ⟨s, hs, hsb⟩ := hb.1
    have hsr : s = r := hu s ⟨hs, hsb.symm ▸ hb.2⟩
    exact hsb.symm.trans (congrArg block hsr)
  · let R : Fin ((v - 1) / 2) → Blocks v :=
      fun c => {b | ∃ r ∈ selected, color r = c ∧ block r = b}
    refine ⟨R, ?_, ?_, ?_⟩
    · intro c x
      obtain ⟨r, hr, hu⟩ := hpoints c x
      refine ⟨block r, ⟨⟨r,hr.1,hr.2.1,rfl⟩,hr.2.2⟩, ?_⟩
      intro b hb
      obtain ⟨s, hs, hsc, hsb⟩ := hb.1
      have hsr : s = r := hu s ⟨hs, hsc, hsb.symm ▸ hb.2⟩
      exact hsb.symm.trans (congrArg block hsr)
    · intro c d hcd
      apply Set.disjoint_left.mpr
      rintro b ⟨r,hr,hrc,hrb⟩ ⟨s,hs,hsd,hsb⟩
      have hrs : r = s := row_unique r s hr hs (hrb.trans hsb.symm)
      exact hcd (hrc.symm.trans ((congrArg color hrs).trans hsd))
    · ext b
      simp only [Set.mem_iUnion, Set.mem_ofPred_eq]
      constructor
      · rintro ⟨c,r,hr,_,hrb⟩
        exact ⟨r,hr,hrb⟩
      · rintro ⟨r,hr,hrb⟩
        exact ⟨color r,r,hr,rfl,hrb⟩

/-- Any finite index set of the right size can be relabeled by Fin (v-2). -/
theorem lkts_fin {v : ℕ} {I : Type} [Fintype I] (B : I → Blocks v)
    (h : IsLKTS B) : ∃ C : Fin (v - 2) → Blocks v, IsLKTS C := by
  let e : I ≃ Fin (v - 2) := (Fintype.equivFin I).trans (finCongr h.1)
  refine ⟨fun j => B (e.symm j), ?_, ?_, ?_, ?_⟩
  · exact Fintype.card_fin _
  · intro j
    exact h.2.1 (e.symm j)
  · intro i j hij
    exact h.2.2.1 (fun he => hij (e.symm.injective he))
  · ext b
    simp only [Set.mem_iUnion, Set.mem_univ, iff_true]
    have hb : b ∈ (⋃ i, B i) := by rw [h.2.2.2]; trivial
    obtain ⟨i,hi⟩ := Set.mem_iUnion.mp hb
    exact ⟨e i, by simpa only [Equiv.symm_apply_apply] using hi⟩

/-- Coordinate representation of label n*layer+coord; no point relabeling is hidden. -/
def pointEncoding (n : ℕ) [NeZero n] : (Fin 3 × ZMod n) ≃ Fin (3 * n) :=
  (Equiv.prodCongr (Equiv.refl (Fin 3)) (ZMod.finEquiv n).symm.toEquiv).trans
    finProdFinEquiv

/-- The encoding agrees with the existing Python point convention. -/
theorem pointEncoding_val (n : ℕ) [NeZero n] (l : Fin 3) (c : ZMod n) :
    ((pointEncoding n) (l,c)).val = n * l.val + c.val := by
  cases n with
  | zero => exact (NeZero.ne 0 rfl).elim
  | succ n =>
    change c.val + (n+1)*l.val = (n+1)*l.val + c.val
    exact Nat.add_comm _ _

/-- Translation acts on the second coordinate and preserves the layer. -/
def coordinateTranslation (n : ℕ) (g : ZMod n) : Equiv.Perm (Fin 3 × ZMod n) where
  toFun p := (p.1,p.2+g)
  invFun p := (p.1,p.2-g)
  left_inv p := by simp
  right_inv p := by simp

/-- Concrete simultaneous cyclic translation on the three n-point layers. -/
def translation (n : ℕ) [NeZero n] (g : ZMod n) : Equiv.Perm (Fin (3*n)) :=
  (pointEncoding n).symm.trans ((coordinateTranslation n g).trans (pointEncoding n))

theorem translation_encoding (n : ℕ) [NeZero n] (g : ZMod n)
    (l : Fin 3) (c : ZMod n) :
    translation n g (pointEncoding n (l,c)) = pointEncoding n (l,c+g) := by
  simp [translation, coordinateTranslation]

/-- Exact numeric shift convention used by the existing C19 certificate scripts. -/
theorem translation_val (n : ℕ) [NeZero n] (g : ZMod n) (l : Fin 3) (c : ZMod n) :
    (translation n g (pointEncoding n (l,c))).val =
      n*l.val + (c.val+g.val)%n := by
  rw [translation_encoding, pointEncoding_val, ZMod.val_add]

def pointCoordinate (n : ℕ) [NeZero n] (x : Fin (3*n)) : ZMod n :=
  ((pointEncoding n).symm x).2

theorem translation_coordinate (n : ℕ) [NeZero n] (g : ZMod n) (x : Fin (3*n)) :
    pointCoordinate n (translation n g x) = pointCoordinate n x + g := by
  simp [pointCoordinate, translation, coordinateTranslation]

theorem translation_zero (n : ℕ) [NeZero n] : translation n 0 = Equiv.refl _ := by
  apply Equiv.ext
  intro x
  apply (pointEncoding n).symm.injective
  simp [translation, coordinateTranslation]

theorem translation_add (n : ℕ) [NeZero n] (g h : ZMod n) (x : Fin (3*n)) :
    translation n (g+h) x = translation n g (translation n h x) := by
  apply (pointEncoding n).symm.injective
  simp [translation, coordinateTranslation, add_comm, add_left_comm]

theorem translate_triple_zero (n : ℕ) [NeZero n] (b : Triple (3*n)) :
    renameSized (translation n 0) 3 b = b := by
  apply Subtype.ext
  simp [renameSized, translation_zero]

theorem translate_triple_add (n : ℕ) [NeZero n] (g h : ZMod n) (b : Triple (3*n)) :
    renameSized (translation n g) 3 (renameSized (translation n h) 3 b) =
      renameSized (translation n (g+h)) 3 b := by
  apply Subtype.ext
  change (b.val.map (translation n h).toEmbedding).map (translation n g).toEmbedding =
    b.val.map (translation n (g+h)).toEmbedding
  rw [Finset.map_map]
  have he : (translation n h).toEmbedding.trans (translation n g).toEmbedding =
      (translation n (g+h)).toEmbedding := by
    apply Function.Embedding.ext
    intro x
    exact (translation_add n g h x).symm
  rw [he]

/-- Actual translation orbit, with no arbitrary choice of a representative. -/
def translationOrbit (n : ℕ) [NeZero n] (b : Triple (3*n)) : Set (Triple (3*n)) :=
  {c | ∃ g : ZMod n, renameSized (translation n g) 3 b = c}

theorem translationOrbit_invariant (n : ℕ) [NeZero n] (g : ZMod n)
    (b : Triple (3*n)) :
    translationOrbit n (renameSized (translation n g) 3 b) = translationOrbit n b := by
  ext c
  constructor
  · rintro ⟨h,hh⟩
    exact ⟨h+g, (translate_triple_add n h g b).symm.trans hh⟩
  · rintro ⟨h,hh⟩
    refine ⟨h-g, ?_⟩
    rw [translate_triple_add, sub_add_cancel]
    exact hh

theorem translationOrbit_fiber (n : ℕ) [NeZero n] (b c : Triple (3*n))
    (h : translationOrbit n b = translationOrbit n c) :
    ∃ g : ZMod n, renameSized (translation n g) 3 b = c := by
  have hc : c ∈ translationOrbit n c := ⟨0, translate_triple_zero n c⟩
  rw [← h] at hc
  exact hc

/-- Sum of the coordinate residues of the three actual points. -/
def coordinateSum (n : ℕ) [NeZero n] (b : Triple (3*n)) : ZMod n :=
  ∑ x ∈ b.val, pointCoordinate n x

/-- Translating three points adds exactly 3*g, even when they lie in different layers. -/
theorem coordinateSum_translation (n : ℕ) [NeZero n] (g : ZMod n)
    (b : Triple (3*n)) :
    coordinateSum n (renameSized (translation n g) 3 b) = coordinateSum n b + 3*g := by
  change (∑ x ∈ b.val.map (translation n g).toEmbedding, pointCoordinate n x) = _
  rw [Finset.sum_map]
  simp only [Equiv.toEmbedding_apply, translation_coordinate]
  rw [Finset.sum_add_distrib, Finset.sum_const, b.property, nsmul_eq_mul]
  rfl

/-- Triple translation is free whenever 3 is invertible modulo n. -/
theorem translation_triple_free (n : ℕ) [NeZero n] (hcop : Nat.Coprime 3 n)
    (b : Triple (3*n)) (g h : ZMod n)
    (heq : renameSized (translation n g) 3 b = renameSized (translation n h) 3 b) :
    g = h := by
  have hs := congrArg (coordinateSum n) heq
  rw [coordinateSum_translation, coordinateSum_translation] at hs
  have hmul : (3 : ZMod n)*g = 3*h := add_left_cancel hs
  exact ((ZMod.isUnit_iff_coprime 3 n).mpr hcop).mul_left_cancel hmul

/-- The action facts for C19 are now proved, not seed-package assumptions. -/
theorem c19_development_sound
    (fixed : Fin 17 → Blocks 57) (base : Fin 2 → Blocks 57)
    (hfixed : ∀ f, IsKTS (fixed f)) (hbase : ∀ a, IsKTS (base a))
    (hinvariant : ∀ f g b, b ∈ fixed f → renameSized (translation 19 g) 3 b ∈ fixed f)
    (htrans : ∀ a b c, b ∈ base a → c ∈ base a →
      translationOrbit 19 b = translationOrbit 19 c → b = c)
    (howners : ∀ b : Triple 57, ∃! i : Fin 17 ⊕ Fin 2,
      translationOrbit 19 b ∈ ownerOrbits (translationOrbit 19) fixed base i) :
    IsLKTS (developed (translation 19) fixed base) := by
  apply development_sound (translation 19) (translationOrbit 19) fixed base
    (by simp [ZMod.card]) hfixed hbase hinvariant
    (translationOrbit_invariant 19) (translationOrbit_fiber 19)
    (translation_triple_free 19 (by decide)) htrans howners

/-- The same kernel-checked action supplies the surviving27+29+29 order87 criterion. -/
theorem c29_development_sound
    (fixed : Fin 27 → Blocks 87) (base : Fin 2 → Blocks 87)
    (hfixed : ∀ f, IsKTS (fixed f)) (hbase : ∀ a, IsKTS (base a))
    (hinvariant : ∀ f g b, b ∈ fixed f → renameSized (translation 29 g) 3 b ∈ fixed f)
    (htrans : ∀ a b c, b ∈ base a → c ∈ base a →
      translationOrbit 29 b = translationOrbit 29 c → b = c)
    (howners : ∀ b : Triple 87, ∃! i : Fin 27 ⊕ Fin 2,
      translationOrbit 29 b ∈ ownerOrbits (translationOrbit 29) fixed base i) :
    IsLKTS (developed (translation 29) fixed base) := by
  apply development_sound (translation 29) (translationOrbit 29) fixed base
    (by simp [ZMod.card]) hfixed hbase hinvariant
    (translationOrbit_invariant 29) (translationOrbit_fiber 29)
    (translation_triple_free 29 (by decide)) htrans howners

end Kirkman

#print Kirkman.mem_renameSized
#print axioms Kirkman.mem_renameSized
#print Kirkman.pair_subset_rename_iff
#print axioms Kirkman.pair_subset_rename_iff
#print Kirkman.isSTS_image
#print axioms Kirkman.isSTS_image
#print Kirkman.parallel_image
#print axioms Kirkman.parallel_image
#print Kirkman.resolution_image
#print axioms Kirkman.resolution_image
#print Kirkman.isKTS_image
#print axioms Kirkman.isKTS_image
#print Kirkman.development_sound
#print axioms Kirkman.development_sound
#print Kirkman.sts_pair_unique
#print axioms Kirkman.sts_pair_unique

#print Kirkman.triple_has_pair
#print axioms Kirkman.triple_has_pair
#print Kirkman.resolved_rows_sound
#print axioms Kirkman.resolved_rows_sound
#print Kirkman.lkts_fin
#print axioms Kirkman.lkts_fin

#print Kirkman.pointEncoding_val
#print axioms Kirkman.pointEncoding_val
#print Kirkman.translation_encoding
#print axioms Kirkman.translation_encoding
#print Kirkman.translation_coordinate
#print axioms Kirkman.translation_coordinate
#print Kirkman.translation_zero
#print axioms Kirkman.translation_zero
#print Kirkman.translation_add
#print axioms Kirkman.translation_add
#print Kirkman.translate_triple_zero
#print axioms Kirkman.translate_triple_zero
#print Kirkman.translate_triple_add
#print axioms Kirkman.translate_triple_add
#print Kirkman.translationOrbit_invariant
#print axioms Kirkman.translationOrbit_invariant
#print Kirkman.translationOrbit_fiber
#print axioms Kirkman.translationOrbit_fiber
#print Kirkman.coordinateSum_translation
#print axioms Kirkman.coordinateSum_translation
#print Kirkman.translation_triple_free
#print axioms Kirkman.translation_triple_free
#print Kirkman.c19_development_sound
#print axioms Kirkman.c19_development_sound
#print Kirkman.c29_development_sound
#print axioms Kirkman.c29_development_sound

#print Kirkman.translation_val
#print axioms Kirkman.translation_val

#print Kirkman.mem_renameSized
#print axioms Kirkman.mem_renameSized
#print Kirkman.pair_subset_rename_iff
#print axioms Kirkman.pair_subset_rename_iff
#print Kirkman.isSTS_image
#print axioms Kirkman.isSTS_image
#print Kirkman.parallel_image
#print axioms Kirkman.parallel_image
#print Kirkman.resolution_image
#print axioms Kirkman.resolution_image
#print Kirkman.isKTS_image
#print axioms Kirkman.isKTS_image
#print Kirkman.development_sound
#print axioms Kirkman.development_sound
#print Kirkman.sts_pair_unique
#print axioms Kirkman.sts_pair_unique
#print Kirkman.triple_has_pair
#print axioms Kirkman.triple_has_pair
#print Kirkman.resolved_rows_sound
#print axioms Kirkman.resolved_rows_sound
#print Kirkman.lkts_fin
#print axioms Kirkman.lkts_fin
#print Kirkman.pointEncoding_val
#print axioms Kirkman.pointEncoding_val
#print Kirkman.translation_encoding
#print axioms Kirkman.translation_encoding
#print Kirkman.translation_val
#print axioms Kirkman.translation_val
#print Kirkman.translation_coordinate
#print axioms Kirkman.translation_coordinate
#print Kirkman.translation_zero
#print axioms Kirkman.translation_zero
#print Kirkman.translation_add
#print axioms Kirkman.translation_add
#print Kirkman.translate_triple_zero
#print axioms Kirkman.translate_triple_zero
#print Kirkman.translate_triple_add
#print axioms Kirkman.translate_triple_add
#print Kirkman.translationOrbit_invariant
#print axioms Kirkman.translationOrbit_invariant
#print Kirkman.translationOrbit_fiber
#print axioms Kirkman.translationOrbit_fiber
#print Kirkman.coordinateSum_translation
#print axioms Kirkman.coordinateSum_translation
#print Kirkman.translation_triple_free
#print axioms Kirkman.translation_triple_free
#print Kirkman.c19_development_sound
#print axioms Kirkman.c19_development_sound
#print Kirkman.c29_development_sound
#print axioms Kirkman.c29_development_sound
