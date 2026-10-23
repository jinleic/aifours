import RdsqsKernel.Target
import RdsqsKernel.Cert52

/-!
# Audit: the RDSQS(52) roots prove the data-independent targets

`Rdsqs.Target`, `Rdsqs.TargetAll`, `Rdsqs.TargetCounts` and their vocabulary are defined in
`RdsqsKernel.Target`, which imports no proof and no data.  The theorems below restate the roots
with exactly the target types.  `witness52` names the explicit object: the block set generated
from the raw `POINT 0` section, and the resolution at every point for every listed multiplier.
-/

namespace Rdsqs.Audit

universe u

/-- Root: an RDSQS(52) exists on the point set `Fin 52`. -/
theorem root52 : Rdsqs.Target 52 := Rdsqs.Kernel.exists_rdsqs52

/-- Root on every 52-element point type. -/
theorem root52_all : Rdsqs.TargetAll.{u} 52 := Rdsqs.Kernel.exists_rdsqs52_all

/-- Root with every forced count written out. -/
theorem root52_counts : Rdsqs.TargetCounts 52 := Rdsqs.Kernel.counts_rdsqs52

/-- The explicit witness: the generated block set is an RDSQS(52), and for every point `x` and
every listed multiplier `m` (with inverse `m'`), `resAt 52 data52 m x` resolves its derived design
at `x`. -/
theorem witness52 : Rdsqs.IsRDSQS Rdsqs.Kernel.rdsqs52 ∧
    ∀ x : Fin 52, ∀ m m' : ℕ, (m, m') ∈ Rdsqs.Kernel.mults52 →
      Rdsqs.IsDerivedResolution Rdsqs.Kernel.rdsqs52 x
        (Rdsqs.Kernel.resAt 52 Rdsqs.Kernel.data52 m x) :=
  ⟨Rdsqs.Kernel.isRDSQS_rdsqs52, Rdsqs.Kernel.rdsqs52_resolutions⟩

/-- Unfolded form of the root, for reading without the definitions of `Target`. -/
theorem root52_unfolded : ∃ B : Finset (Finset (Fin 52)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 52), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 52, ∃ R : Finset (Finset (Finset (Fin 52))),
        (∀ P ∈ R, P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
          ∀ y : Fin 52, y ≠ x → ∃! T, T ∈ P ∧ y ∈ T) ∧
        ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ R ∧ T ∈ P :=
  Rdsqs.Kernel.exists_rdsqs52

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
#print Rdsqs.Kernel.rdsqs52
#print Rdsqs.Kernel.mults52
#print Rdsqs.Kernel.data52RawSha256
#print Rdsqs.Kernel.data52SeedSha256
#check @Rdsqs.Audit.root52
#check @Rdsqs.Audit.root52_all
#check @Rdsqs.Audit.root52_counts
#check @Rdsqs.Audit.witness52
#check @Rdsqs.Audit.root52_unfolded
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.rdsqs52_spec
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.data52_shape
set_option pp.funBinderTypes true in
#check @Rdsqs.Kernel.data52_range
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
#print axioms Rdsqs.Kernel.data52_shape
#print axioms Rdsqs.Kernel.data52_range
#print axioms Rdsqs.Kernel.data52_seedCheck
#print axioms Rdsqs.Kernel.data52_multCheck
#print axioms Rdsqs.Kernel.isRDSQS_rdsqs52
#print axioms Rdsqs.Kernel.rdsqs52_resolutions
#print axioms Rdsqs.Kernel.exists_rdsqs52
#print axioms Rdsqs.Kernel.exists_rdsqs52_all
#print axioms Rdsqs.Kernel.counts_rdsqs52
#print axioms Rdsqs.Audit.root52
#print axioms Rdsqs.Audit.root52_all
#print axioms Rdsqs.Audit.root52_counts
#print axioms Rdsqs.Audit.witness52
#print axioms Rdsqs.Audit.root52_unfolded
