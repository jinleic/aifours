import PC100Kernel.Target
import PC100Kernel.Cert100

/-!
# Audit: the v = 100 roots prove the data-independent targets

`PC100.Target`, `PC100.TargetShift`, `PC100.TargetCounts` and their vocabulary are defined in
`PC100Kernel.Target`, which imports no proof and no data of this development.  The theorems below
restate the roots with exactly the target types; `witness100` names the explicit object (the block set
and the classes listed in the raw certificate), and `root100_unfolded` spells the main root out without
the definitions of `PC100Kernel.Target`.
-/

namespace PC100.Audit

/-- Root: a 2-(100,4,1) design on `Fin 100` with a point-cyclic resolution. -/
theorem root100 : PC100.Target 100 := PC100.Kernel.exists_pc100

/-- Root: `x ↦ x + 1` is one 100-cycle on `Fin 100`, and it preserves a 2-(100,4,1) design and a
resolution of it (block set onto block set, every class onto a class). -/
theorem root100_shift : PC100.TargetShift 100 := PC100.Kernel.exists_pc100_shift

/-- Root with the counts written out: 825 blocks, 33 classes of 25 blocks. -/
theorem root100_counts : PC100.TargetCounts 100 := PC100.Kernel.counts_pc100_target

/-- The cycle type of `x ↦ x + 1` on `Fin 100` is `{100}`. -/
theorem root100_cycleType : (PC100.shift 100).cycleType = {100} := PC100.Kernel.cycleType_shift100

/-- `PC100.shift 100` is `x ↦ x + 1`. -/
theorem shift100_apply (x : Fin 100) : PC100.shift 100 x = x + 1 := rfl

/-- The explicit witness: the raw certificate's block set and classes. -/
theorem witness100 :
    PC100.IsDesign241 PC100.Kernel.pc100Blocks ∧
      PC100.IsResolution PC100.Kernel.pc100Blocks PC100.Kernel.pc100Classes ∧
      PC100.IsResolutionAutomorphism PC100.Kernel.pc100Blocks PC100.Kernel.pc100Classes
        (PC100.shift 100) ∧
      PC100.IsFullCycle (PC100.shift 100) ∧
      PC100.Kernel.pc100Blocks.card = 825 ∧ PC100.Kernel.pc100Classes.card = 33 ∧
      ∀ P ∈ PC100.Kernel.pc100Classes, P.card = 25 :=
  ⟨PC100.Kernel.isDesign241_pc100, PC100.Kernel.isResolution_pc100, PC100.Kernel.shift_pc100,
    PC100.Kernel.isFullCycle_shift100, PC100.Kernel.counts_pc100⟩

/-- Unfolded form of `root100_shift`, for reading without the definitions of `PC100Kernel.Target`. -/
theorem root100_unfolded :
    ((Equiv.addRight (1 : Fin 100)).IsCycle ∧
      (Equiv.addRight (1 : Fin 100)).support = Finset.univ) ∧
    ∃ B : Finset (Finset (Fin 100)), ∃ R : Finset (Finset (Finset (Fin 100))),
      ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 100), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 100, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      (B.image (fun X => X.map (Equiv.addRight (1 : Fin 100)).toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map (Equiv.addRight (1 : Fin 100)).toEmbedding) ∈ R) :=
  PC100.Kernel.exists_pc100_shift

end PC100.Audit

#print PC100.IsDesign241
#print PC100.IsParallelClass
#print PC100.IsResolution
#print PC100.blockImage
#print PC100.IsResolutionAutomorphism
#print PC100.IsFullCycle
#print PC100.IsPointCyclicResolution
#print PC100.shift
#print PC100.Target
#print PC100.TargetShift
#print PC100.TargetCounts
#print PC100.Kernel.RawBlock
#print PC100.Kernel.pt
#print PC100.Kernel.blk
#print PC100.Kernel.classOf
#print PC100.Kernel.blocks
#print PC100.Kernel.classes
#print PC100.Kernel.pc100Blocks
#print PC100.Kernel.pc100Classes
#print PC100.Kernel.cert100RawSha256
#print PC100.Kernel.cert100SeedSha256
#check @PC100.Audit.root100
#check @PC100.Audit.root100_shift
#check @PC100.Audit.root100_counts
#check @PC100.Audit.root100_cycleType
#check @PC100.Audit.shift100_apply
#check @PC100.Audit.witness100
#check @PC100.Audit.root100_unfolded
set_option pp.funBinderTypes true in
#check @PC100.Kernel.pc100Blocks_spec
set_option pp.funBinderTypes true in
#check @PC100.Kernel.pc100Classes_spec
set_option pp.funBinderTypes true in
#check @PC100.Kernel.cert100_shape
set_option pp.funBinderTypes true in
#check @PC100.Kernel.cert100_range
set_option pp.funBinderTypes true in
#check @PC100.Kernel.sound_of_check
#print axioms PC100.Kernel.sound_of_check
#print axioms PC100.Kernel.isFullCycle_shift
#print axioms PC100.Kernel.cycleType_shift
#print axioms PC100.Kernel.cert100_shape
#print axioms PC100.Kernel.cert100_range
#print axioms PC100.Kernel.cert100_check
#print axioms PC100.Kernel.isDesign241_pc100
#print axioms PC100.Kernel.isResolution_pc100
#print axioms PC100.Kernel.shift_pc100
#print axioms PC100.Kernel.counts_pc100
#print axioms PC100.Kernel.exists_pc100
#print axioms PC100.Kernel.exists_pc100_shift
#print axioms PC100.Kernel.counts_pc100_target
#print axioms PC100.Audit.root100
#print axioms PC100.Audit.root100_shift
#print axioms PC100.Audit.root100_counts
#print axioms PC100.Audit.root100_cycleType
#print axioms PC100.Audit.shift100_apply
#print axioms PC100.Audit.witness100
#print axioms PC100.Audit.root100_unfolded
