import McdKernel.Target
import Gc80.GcTarget
import Gc80.CertGc

/-!
# Audit: the gcDCQS(20^4 : 0) and mcDSQS(80) roots prove the data-independent targets

`Mcd.TargetMc`, `Mcd.TargetColoured`, `Mcd.ColourLowerBound`, `Mcd.chiPrime` and their vocabulary
are defined in `McdKernel.Target`; `Mcd.TargetGc80`, `Mcd.IsGcDCQS0`, `Mcd.IsGcSTS`,
`Mcd.IsHoleSTS`, `Mcd.IsCQS0`, `Mcd.IsGroupPartition`, `Mcd.grp80` and `Mcd.groups80` in
`Gc80.GcTarget`.  Neither module imports a proof or data.  The theorems below restate the roots
with exactly the target types, with numerals, and unfolded with Mathlib notions only (the
unfolded statements are proved by the same terms: they are the definitions, unfolded).
`witness_mc80` / `witness_gc80` name the explicit objects: the raw block lines and, at every
point, the classes of the raw `POINT x` section.
-/

namespace Mcd.Audit

universe u

open Mcd.Kernel

/-! ## mcDSQS(80) and `χ′(79)` -/

/-- An mcDSQS(80) exists on `Fin 80`. -/
theorem root_mc80 : Mcd.TargetMc 80 := exists_mcdsqs80

/-- `χ′(79) = 40`. -/
theorem root_chi79 : Mcd.chiPrime 79 = 40 := chiPrime_79

/-- Data-independent: every colouring of every STS on every 79-element type has at least 40
colour classes. -/
theorem root_lower79 : Mcd.ColourLowerBound.{u} 79 40 := Mcd.Counts.colourLowerBound_79

/-- An SQS on `Fin 80` whose derived design at every point has a 40-colouring. -/
theorem root_coloured80 : Mcd.TargetColoured 80 40 := coloured80

/-- The explicit mcDSQS(80) witness, with its counts. -/
theorem witness_mc80 : Mcd.IsMcDSQS mcdsqs80 ∧ mcdsqs80.card = 20540 ∧
    ∀ x : Fin 80, Mcd.IsColouring (Mcd.derivedBlocks mcdsqs80 x) (colouringMc80 x) ∧
      (colouringMc80 x).card = 40 ∧ (Mcd.derivedBlocks mcdsqs80 x).card = 1027 :=
  ⟨isMcDSQS_mcdsqs80, card_mcdsqs80, fun x =>
    ⟨(mc_point_spec x).1, (mc_point_spec x).2.1, (mc_point_spec x).2.2.1⟩⟩

/-- `χ′(79) = 40`, unfolded. -/
theorem root_chi79_unfolded :
    sInf {r : ℕ | ∃ S : Finset (Finset (Fin 79)),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 79), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin 79))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! P, P ∈ C ∧ T ∈ P) ∧ C.card = r} = 40 :=
  chiPrime_79

/-- The lower bound, unfolded. -/
theorem root_lower79_unfolded : ∀ (W : Type u) [Fintype W] [DecidableEq W],
    Fintype.card W = 79 → ∀ S : Finset (Finset W),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset W, P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) →
      ∀ C : Finset (Finset (Finset W)),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! P, P ∈ C ∧ T ∈ P) → 40 ≤ C.card :=
  Mcd.Counts.colourLowerBound_79

/-- The mcDSQS(80) root, unfolded: an SQS on `Fin 80` whose derived design at every point has a
colouring with exactly the least number of colours of any colouring of any STS on `Fin 79`. -/
theorem root_mc80_unfolded : ∃ B : Finset (Finset (Fin 80)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 80), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 80, ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = sInf {r : ℕ | ∃ S : Finset (Finset (Fin 79)),
          ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 79), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
          ∃ C' : Finset (Finset (Finset (Fin 79))),
            ((∀ P ∈ C', P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
              ∀ T ∈ S, ∃! P, P ∈ C' ∧ T ∈ P) ∧ C'.card = r} :=
  exists_mcdsqs80

/-! ## gcDCQS(20^4 : 0) -/

/-- A gcDCQS(20^4 : 0) with the groups `{0..19}, {20..39}, {40..59}, {60..79}` and an empty stem
exists on `Fin 80` (with `r = χ′(79)`, `s = χ′(79) - (79 - 19) / 2`). -/
theorem root_gc80 : Mcd.TargetGc80 := exists_gcdcqs80

/-- The same with the counts: 19400 blocks, 970 derived blocks at every point. -/
theorem root_gc80_counts : ∃ A : Finset (Finset (Fin 80)), Mcd.IsGcDCQS0 Mcd.groups80 A ∧
    A.card = 19400 ∧ ∀ x : Fin 80, (Mcd.derivedBlocks A x).card = 970 :=
  gc80_with_counts

/-- The four groups: `groups80` has 4 members of 20 points each, and `grp80 i` is the raw GROUPS
line `i`. -/
theorem groups80_spec : Mcd.IsGroupPartition Mcd.groups80 ∧
    (∀ i < 4, (Mcd.grp80 i).card = 20) ∧ Mcd.groups80 = {Mcd.grp80 0, Mcd.grp80 1, Mcd.grp80 2, Mcd.grp80 3} ∧
    ∀ i < 4, ∀ y : Fin 80, y ∈ Mcd.grp80 i ↔ y.val ∈ groupsGc80.getD i [] :=
  ⟨Mcd.isGroupPartition_groups80, fun _ hi => card_grp80 hi, rfl, fun _ hi => grp80_eq_raw hi⟩

/-- With numerals: the colourings have `40 = χ′(79)` classes, exactly `10` of them avoiding
`G(x) \ {x}`. -/
theorem root_gc80_numerals : ∃ A : Finset (Finset (Fin 80)), Mcd.IsCQS0 Mcd.groups80 A ∧
    A.card = 19400 ∧ ∀ x : Fin 80, (Mcd.derivedBlocks A x).card = 970 ∧
      Mcd.IsHoleSTS (Finset.univ.erase x) ((Mcd.grp80 (x.val / 20)).erase x)
        (Mcd.derivedBlocks A x) ∧
      ∃ C : Finset (Finset (Finset (Fin 80))), Mcd.IsColouring (Mcd.derivedBlocks A x) C ∧
        C.card = 40 ∧
        (C.filter fun P => ∀ T ∈ P, Disjoint T ((Mcd.grp80 (x.val / 20)).erase x)).card = 10 :=
  ⟨gcdcqs80, isCQS0_gcdcqs80, card_gcdcqs80, fun x =>
    ⟨(gc_point_spec x).2.2.1, isHoleSTS_gc80 x, colouringGc80 x, colouringGc80_spec x⟩⟩

/-- The explicit gcDCQS(20^4 : 0) witness. -/
theorem witness_gc80 : Mcd.IsGcDCQS0 Mcd.groups80 gcdcqs80 ∧ gcdcqs80.card = 19400 ∧
    ∀ x : Fin 80, Mcd.IsColouring (Mcd.derivedBlocks gcdcqs80 x) (colouringGc80 x) ∧
      (colouringGc80 x).card = 40 ∧
      ((colouringGc80 x).filter fun P =>
        ∀ T ∈ P, Disjoint T ((Mcd.grp80 (x.val / 20)).erase x)).card = 10 ∧
      (Mcd.derivedBlocks gcdcqs80 x).card = 970 :=
  ⟨isGcDCQS0_gcdcqs80, card_gcdcqs80, fun x =>
    ⟨(colouringGc80_spec x).1, (colouringGc80_spec x).2.1, (colouringGc80_spec x).2.2,
      (gc_point_spec x).2.2.1⟩⟩

/-- The numeral form, unfolded (Mathlib notions, `groups80` and `grp80` only). -/
theorem root_gc80_unfolded : ∃ A : Finset (Finset (Fin 80)),
    (((∀ G ∈ Mcd.groups80, G.Nonempty) ∧
        (∀ G ∈ Mcd.groups80, ∀ G' ∈ Mcd.groups80, G ≠ G' → Disjoint G G') ∧
        ∀ x : Fin 80, ∃ G ∈ Mcd.groups80, x ∈ G) ∧
      (∀ X ∈ A, X.card = 4) ∧
      (∀ T : Finset (Fin 80), T.card = 3 → (∀ G ∈ Mcd.groups80, ¬ T ⊆ G) →
        ∃! X, X ∈ A ∧ T ⊆ X) ∧
      ∀ T : Finset (Fin 80), T.card = 3 → ∀ G ∈ Mcd.groups80, T ⊆ G → ∀ X ∈ A, ¬ T ⊆ X) ∧
    A.card = 19400 ∧
    ∀ x : Fin 80, ((A.filter fun X => x ∈ X).image fun X => X.erase x).card = 970 ∧
      ((Mcd.grp80 (x.val / 20)).erase x ⊆ Finset.univ.erase x ∧
        (∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x),
          T.card = 3 ∧ T ⊆ Finset.univ.erase x) ∧
        (∀ P : Finset (Fin 80), P.card = 2 → P ⊆ Finset.univ.erase x →
          ¬ P ⊆ (Mcd.grp80 (x.val / 20)).erase x →
          ∃! T, T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧ P ⊆ T) ∧
        ∀ P : Finset (Fin 80), P.card = 2 → P ⊆ (Mcd.grp80 (x.val / 20)).erase x →
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ¬ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = 40 ∧
        (C.filter fun P => ∀ T ∈ P, Disjoint T ((Mcd.grp80 (x.val / 20)).erase x)).card = 10 :=
  root_gc80_numerals

end Mcd.Audit

#print Mcd.IsSQS
#print Mcd.IsSTS
#print Mcd.derivedBlocks
#print Mcd.IsPPC
#print Mcd.IsColouring
#print Mcd.chiPrime
#print Mcd.TargetColoured
#print Mcd.IsMcDSQS
#print Mcd.TargetMc
#print Mcd.ColourLowerBound
#print Mcd.IsGroupPartition
#print Mcd.IsCQS0
#print Mcd.IsHoleSTS
#print Mcd.IsGcSTS
#print Mcd.IsGcDCQS0
#print Mcd.grp80
#print Mcd.groups80
#print Mcd.TargetGc80
#print Mcd.Kernel.pt
#print Mcd.Kernel.quad
#print Mcd.Kernel.tri
#print Mcd.Kernel.blockSet
#print Mcd.Kernel.tripleSet
#print Mcd.Kernel.classSet
#print Mcd.Kernel.mcdsqs80
#print Mcd.Kernel.colouringMc80
#print Mcd.Kernel.gcdcqs80
#print Mcd.Kernel.colouringGc80
#print Mcd.Kernel.rawMc80Sha256
#print Mcd.Kernel.rawGc80Sha256
#check @Mcd.Audit.root_mc80
#check @Mcd.Audit.root_chi79
#check @Mcd.Audit.root_lower79
#check @Mcd.Audit.root_coloured80
#check @Mcd.Audit.witness_mc80
#check @Mcd.Audit.root_chi79_unfolded
#check @Mcd.Audit.root_lower79_unfolded
#check @Mcd.Audit.root_mc80_unfolded
#check @Mcd.Audit.root_gc80
#check @Mcd.Audit.root_gc80_counts
#check @Mcd.Audit.groups80_spec
#check @Mcd.Audit.root_gc80_numerals
#check @Mcd.Audit.witness_gc80
#check @Mcd.Audit.root_gc80_unfolded
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.mcdsqs80_spec
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.gcdcqs80_spec
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.sts79_witness
#print axioms Mcd.Counts.card_sts_mul
#print axioms Mcd.Counts.card_ppc_mul_le
#print axioms Mcd.Counts.sum_card_colouring
#print axioms Mcd.Counts.chiPrime_eq_of
#print axioms Mcd.Counts.colourLowerBound_79
#print axioms Mcd.Kernel.colouring_of_check
#print axioms Mcd.Kernel.sts_of_check
#print axioms Mcd.Kernel.holeCheck_sound
#print axioms Mcd.Kernel.colCheck_spec
#print axioms Mcd.Kernel.card_filter_classSet
#print axioms Mcd.Kernel.pointCheck_sound
#print axioms Mcd.Kernel.gcPointCheck_sound
#print axioms Mcd.Kernel.blockCheck_sound
#print axioms Mcd.isSQS_of_derived
#print axioms Mcd.isCQS0_of_derived
#print axioms Mcd.isHoleSTS_of_derived
#print axioms Mcd.isGroupPartition_groups80
#print axioms Mcd.Kernel.mc_blocks
#print axioms Mcd.Kernel.mc_points
#print axioms Mcd.Kernel.mc79_stsCheck
#print axioms Mcd.Kernel.sts79_witness
#print axioms Mcd.Kernel.chiPrime_79
#print axioms Mcd.Kernel.isSQS_mcdsqs80
#print axioms Mcd.Kernel.isMcDSQS_mcdsqs80
#print axioms Mcd.Kernel.exists_mcdsqs80
#print axioms Mcd.Kernel.gc_blocks
#print axioms Mcd.Kernel.gc_groups_raw
#print axioms Mcd.Kernel.gc_points
#print axioms Mcd.Kernel.isCQS0_gcdcqs80
#print axioms Mcd.Kernel.isGcSTS_gc80
#print axioms Mcd.Kernel.isGcDCQS0_gcdcqs80
#print axioms Mcd.Kernel.exists_gcdcqs80
#print axioms Mcd.Audit.root_mc80
#print axioms Mcd.Audit.root_chi79
#print axioms Mcd.Audit.root_lower79
#print axioms Mcd.Audit.root_coloured80
#print axioms Mcd.Audit.witness_mc80
#print axioms Mcd.Audit.root_chi79_unfolded
#print axioms Mcd.Audit.root_lower79_unfolded
#print axioms Mcd.Audit.root_mc80_unfolded
#print axioms Mcd.Audit.root_gc80
#print axioms Mcd.Audit.root_gc80_counts
#print axioms Mcd.Audit.groups80_spec
#print axioms Mcd.Audit.root_gc80_numerals
#print axioms Mcd.Audit.witness_gc80
#print axioms Mcd.Audit.root_gc80_unfolded
