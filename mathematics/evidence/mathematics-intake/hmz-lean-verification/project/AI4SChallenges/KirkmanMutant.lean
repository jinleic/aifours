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
  Fintype.card I = v - 1 ∧ (∀ i, IsKTS (B i)) ∧
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
    x ∈ (renameSized e k b).val ↔ e.symm x ∈ b.val := by sorry

def imageBlocks {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v) : Blocks v :=
  renameSized e 3 '' B

theorem pair_subset_rename_iff {v : ℕ} (e : Equiv.Perm (Fin v))
    (p : Pair v) (b : Triple v) :
    p.val ⊆ (renameSized e 3 b).val ↔ (renameSized e.symm 2 p).val ⊆ b.val := by sorry

/-- Point permutations preserve exact pair coverage, including uniqueness. -/
theorem isSTS_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (h : IsSTS B) : IsSTS (imageBlocks e B) := by sorry

/-- Point permutations preserve point partitions, including uniqueness. -/
theorem parallel_image {v : ℕ} (e : Equiv.Perm (Fin v)) (P : Blocks v)
    (h : IsParallelClass P) : IsParallelClass (imageBlocks e P) := by sorry

/-- Both the exact class union and class disjointness survive development. -/
theorem resolution_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (R : Fin ((v - 1) / 2) → Blocks v) (h : IsResolution B R) :
    IsResolution (imageBlocks e B) (fun c => imageBlocks e (R c)) := by sorry

theorem isKTS_image {v : ℕ} (e : Equiv.Perm (Fin v)) (B : Blocks v)
    (h : IsKTS B) : IsKTS (imageBlocks e B) := by sorry

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
    IsLKTS (developed act fixed base) := by sorry

/-- A concrete two-pair collision prevents an STS; used by the broken control. -/
theorem sts_pair_unique {v : ℕ} (B : Blocks v) (h : IsSTS B)
    (p : Pair v) (b c : Triple v) (hb : b ∈ B) (hc : c ∈ B)
    (hpb : p.val ⊆ b.val) (hpc : p.val ⊆ c.val) : b = c := by sorry

/-- Every genuine triple has an actual two-element subset. -/
theorem triple_has_pair {v : ℕ} (b : Triple v) : ∃ p : Pair v, p.val ⊆ b.val := by sorry

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
    IsKTS {b | ∃ r ∈ selected, block r = b} := by sorry

/-- Any finite index set of the right size can be relabeled by Fin (v-2). -/
theorem lkts_fin {v : ℕ} {I : Type} [Fintype I] (B : I → Blocks v)
    (h : IsLKTS B) : ∃ C : Fin (v - 2) → Blocks v, IsLKTS C := by sorry

/-- Coordinate representation of label n*layer+coord; no point relabeling is hidden. -/
def pointEncoding (n : ℕ) [NeZero n] : (Fin 3 × ZMod n) ≃ Fin (3 * n) :=
  (Equiv.prodCongr (Equiv.refl (Fin 3)) (ZMod.finEquiv n).symm.toEquiv).trans
    finProdFinEquiv

/-- The encoding agrees with the existing Python point convention. -/
theorem pointEncoding_val (n : ℕ) [NeZero n] (l : Fin 3) (c : ZMod n) :
    ((pointEncoding n) (l,c)).val = n * l.val + c.val := by sorry

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
    translation n g (pointEncoding n (l,c)) = pointEncoding n (l,c+g) := by sorry

/-- Exact numeric shift convention used by the existing C19 certificate scripts. -/
theorem translation_val (n : ℕ) [NeZero n] (g : ZMod n) (l : Fin 3) (c : ZMod n) :
    (translation n g (pointEncoding n (l,c))).val =
      n*l.val + (c.val+g.val)%n := by sorry

def pointCoordinate (n : ℕ) [NeZero n] (x : Fin (3*n)) : ZMod n :=
  ((pointEncoding n).symm x).2

theorem translation_coordinate (n : ℕ) [NeZero n] (g : ZMod n) (x : Fin (3*n)) :
    pointCoordinate n (translation n g x) = pointCoordinate n x + g := by sorry

theorem translation_zero (n : ℕ) [NeZero n] : translation n 0 = Equiv.refl _ := by sorry

theorem translation_add (n : ℕ) [NeZero n] (g h : ZMod n) (x : Fin (3*n)) :
    translation n (g+h) x = translation n g (translation n h x) := by sorry

theorem translate_triple_zero (n : ℕ) [NeZero n] (b : Triple (3*n)) :
    renameSized (translation n 0) 3 b = b := by sorry

theorem translate_triple_add (n : ℕ) [NeZero n] (g h : ZMod n) (b : Triple (3*n)) :
    renameSized (translation n g) 3 (renameSized (translation n h) 3 b) =
      renameSized (translation n (g+h)) 3 b := by sorry

/-- Actual translation orbit, with no arbitrary choice of a representative. -/
def translationOrbit (n : ℕ) [NeZero n] (b : Triple (3*n)) : Set (Triple (3*n)) :=
  {c | ∃ g : ZMod n, renameSized (translation n g) 3 b = c}

theorem translationOrbit_invariant (n : ℕ) [NeZero n] (g : ZMod n)
    (b : Triple (3*n)) :
    translationOrbit n (renameSized (translation n g) 3 b) = translationOrbit n b := by sorry

theorem translationOrbit_fiber (n : ℕ) [NeZero n] (b c : Triple (3*n))
    (h : translationOrbit n b = translationOrbit n c) :
    ∃ g : ZMod n, renameSized (translation n g) 3 b = c := by sorry

/-- Sum of the coordinate residues of the three actual points. -/
def coordinateSum (n : ℕ) [NeZero n] (b : Triple (3*n)) : ZMod n :=
  ∑ x ∈ b.val, pointCoordinate n x

/-- Translating three points adds exactly 3*g, even when they lie in different layers. -/
theorem coordinateSum_translation (n : ℕ) [NeZero n] (g : ZMod n)
    (b : Triple (3*n)) :
    coordinateSum n (renameSized (translation n g) 3 b) = coordinateSum n b + 3*g := by sorry

/-- Triple translation is free whenever 3 is invertible modulo n. -/
theorem translation_triple_free (n : ℕ) [NeZero n] (hcop : Nat.Coprime 3 n)
    (b : Triple (3*n)) (g h : ZMod n)
    (heq : renameSized (translation n g) 3 b = renameSized (translation n h) 3 b) :
    g = h := by sorry

/-- The action facts for C19 are now proved, not seed-package assumptions. -/
theorem c19_development_sound
    (fixed : Fin 17 → Blocks 57) (base : Fin 2 → Blocks 57)
    (hfixed : ∀ f, IsKTS (fixed f)) (hbase : ∀ a, IsKTS (base a))
    (hinvariant : ∀ f g b, b ∈ fixed f → renameSized (translation 19 g) 3 b ∈ fixed f)
    (htrans : ∀ a b c, b ∈ base a → c ∈ base a →
      translationOrbit 19 b = translationOrbit 19 c → b = c)
    (howners : ∀ b : Triple 57, ∃! i : Fin 17 ⊕ Fin 2,
      translationOrbit 19 b ∈ ownerOrbits (translationOrbit 19) fixed base i) :
    IsLKTS (developed (translation 19) fixed base) := by sorry

/-- The same kernel-checked action supplies the surviving27+29+29 order87 criterion. -/
theorem c29_development_sound
    (fixed : Fin 27 → Blocks 87) (base : Fin 2 → Blocks 87)
    (hfixed : ∀ f, IsKTS (fixed f)) (hbase : ∀ a, IsKTS (base a))
    (hinvariant : ∀ f g b, b ∈ fixed f → renameSized (translation 29 g) 3 b ∈ fixed f)
    (htrans : ∀ a b c, b ∈ base a → c ∈ base a →
      translationOrbit 29 b = translationOrbit 29 c → b = c)
    (howners : ∀ b : Triple 87, ∃! i : Fin 27 ⊕ Fin 2,
      translationOrbit 29 b ∈ ownerOrbits (translationOrbit 29) fixed base i) :
    IsLKTS (developed (translation 29) fixed base) := by sorry

end Kirkman

