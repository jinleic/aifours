import RdsqsKernel.Target
import RdsqsKernel.Cert76

/-!
# Audit: the RDSQS(76) roots prove the data-independent targets (EXPLORATORY order)

`Rdsqs.Target`, `Rdsqs.TargetAll`, `Rdsqs.TargetCounts` and their vocabulary are defined in
`RdsqsKernel.Target`, which imports no proof and no data.  The theorems below restate the roots
with exactly the target types.  `witness76` names the explicit object: the block set generated
from the raw `POINT 0` section, and the resolution at every point for every listed multiplier.
RDSQS(76) is exploratory: correctness only; no novelty or open-status claim is made here.
-/

namespace Rdsqs.Audit

universe u

/-- Root: an RDSQS(76) exists on the point set `Fin 76`. -/
theorem root76 : Rdsqs.Target 76 := Rdsqs.Kernel.exists_rdsqs76

/-- Root on every 76-element point type. -/
theorem root76_all : Rdsqs.TargetAll.{u} 76 := Rdsqs.Kernel.exists_rdsqs76_all

/-- Root with every forced count written out. -/
theorem root76_counts : Rdsqs.TargetCounts 76 := Rdsqs.Kernel.counts_rdsqs76

/-- The explicit witness: the generated block set is an RDSQS(76), and for every point `x` and
every listed multiplier `m` (with inverse `m'`), `resAt 76 data76 m x` resolves its derived design
at `x`. -/
theorem witness76 : Rdsqs.IsRDSQS Rdsqs.Kernel.rdsqs76 ∧
    ∀ x : Fin 76, ∀ m m' : ℕ, (m, m') ∈ Rdsqs.Kernel.mults76 →
      Rdsqs.IsDerivedResolution Rdsqs.Kernel.rdsqs76 x
        (Rdsqs.Kernel.resAt 76 Rdsqs.Kernel.data76 m x) :=
  ⟨Rdsqs.Kernel.isRDSQS_rdsqs76, Rdsqs.Kernel.rdsqs76_resolutions⟩

/-- Unfolded form of the root, for reading without the definitions of `Target`. -/
theorem root76_unfolded : ∃ B : Finset (Finset (Fin 76)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 76), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 76, ∃ R : Finset (Finset (Finset (Fin 76))),
        (∀ P ∈ R, P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
          ∀ y : Fin 76, y ≠ x → ∃! T, T ∈ P ∧ y ∈ T) ∧
        ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ R ∧ T ∈ P :=
  Rdsqs.Kernel.exists_rdsqs76

end Rdsqs.Audit

#print Rdsqs.IsSQS
#print Rdsqs.derivedBlocks
#print Rdsqs.IsDerivedParallelClass
#print Rdsqs.IsDerivedResolution
#print Rdsqs.IsRDSQS
#print Rdsqs.Target
#print Rdsqs.TargetAll
#print Rdsqs.TargetCounts
#print Rdsqs.Generic.relabel
#print Rdsqs.Generic.blocksOf
#print Rdsqs.Kernel.pt
#print Rdsqs.Kernel.tri
#print Rdsqs.Kernel.seedTriples
#print Rdsqs.Kernel.seedClasses
#print Rdsqs.Kernel.blocks
#print Rdsqs.Kernel.resAt
#print Rdsqs.Kernel.rdsqs76
#print Rdsqs.Kernel.mults76
#print Rdsqs.Kernel.data76RawSha256
#print Rdsqs.Kernel.data76SeedSha256
#check @Rdsqs.Audit.root76
#check @Rdsqs.Audit.root76_all
#check @Rdsqs.Audit.root76_counts
#check @Rdsqs.Audit.witness76
#check @Rdsqs.Audit.root76_unfolded
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.rdsqs76_spec
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.data76_shape
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.data76_range
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.isRDSQS_of_check
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.resAt_of_check
#print axioms Rdsqs.Generic.isSQS_blocksOf
#print axioms Rdsqs.Generic.isDerivedResolution_affine
#print axioms Rdsqs.Generic.isRDSQS_blocksOf
#print axioms Rdsqs.Generic.targetAll_of_target
#print axioms Rdsqs.Counts.card_blocks_mul
#print axioms Rdsqs.Counts.card_derived_mul
#print axioms Rdsqs.Counts.card_class_mul
#print axioms Rdsqs.Counts.card_resolution_mul
#print axioms Rdsqs.Kernel.seed_of_check
#print axioms Rdsqs.Kernel.isRDSQS_of_check
#print axioms Rdsqs.Kernel.resAt_of_check
#print axioms Rdsqs.Kernel.data76_shape
#print axioms Rdsqs.Kernel.data76_range
#print axioms Rdsqs.Kernel.data76_seedCheck
#print axioms Rdsqs.Kernel.data76_multCheck
#print axioms Rdsqs.Kernel.isRDSQS_rdsqs76
#print axioms Rdsqs.Kernel.rdsqs76_resolutions
#print axioms Rdsqs.Kernel.exists_rdsqs76
#print axioms Rdsqs.Kernel.exists_rdsqs76_all
#print axioms Rdsqs.Kernel.counts_rdsqs76
#print axioms Rdsqs.Audit.root76
#print axioms Rdsqs.Audit.root76_all
#print axioms Rdsqs.Audit.root76_counts
#print axioms Rdsqs.Audit.witness76
#print axioms Rdsqs.Audit.root76_unfolded
