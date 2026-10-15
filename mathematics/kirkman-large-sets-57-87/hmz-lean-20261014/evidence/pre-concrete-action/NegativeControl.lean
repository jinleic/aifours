import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Image
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Set.Pairwise.Basic

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
The orbit hypotheses can be checked by full enumeration; no group theorem or
unbuilt OAI module is imported. A group law is unnecessary for this criterion:
its orbit-fiber and freeness hypotheses contain exactly the needed action facts.
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
    (howners : ∀ o, ∃! i : F ⊕ A, o ∈ ownerOrbits key fixed base i) :
    IsLKTS (developed act fixed base) := by
  have own_unique : ∀ o (i j : F ⊕ A),
      o ∈ ownerOrbits key fixed base i → o ∈ ownerOrbits key fixed base j → i = j := by
    intro o i j hi hj
    obtain ⟨k, _, hu⟩ := howners o
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
    have ho := own_unique (key b) _ _ (owner_of i b hi) (owner_of j b hj)
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
    obtain ⟨i, hi, _⟩ := howners (key b)
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
      simp only [Set.mem_iUnion, Set.mem_setOf_eq]
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

/- Concrete broken pair-cover column from the selected-row certificate convention.
   Both distinct rows complete {0,1}; exact-one pair coverage is false. -/
namespace Kirkman.Broken

def b0 : Triple 9 := ⟨{0,1,2}, by decide⟩
def b1 : Triple 9 := ⟨{0,1,3}, by decide⟩
def p01 : Pair 9 := ⟨{0,1}, by decide⟩
def block : Fin 2 → Triple 9 := fun r => if r = 0 then b0 else b1

example : ∃! r : Fin 2,
    r ∈ (Finset.univ : Finset (Fin 2)) ∧ p01.val ⊆ (block r).val := by
  unfold ExistsUnique
  decide

end Kirkman.Broken
