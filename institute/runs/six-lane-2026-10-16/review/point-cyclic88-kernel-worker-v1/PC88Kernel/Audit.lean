import PC88Kernel.Target
import PC88Kernel.Bridge

/-!
# Audit: the root proves the data-independent target

`PC88.Target` and its vocabulary are defined in `PC88Kernel.Target`, which imports no proof.
The theorems below restate the root with exactly the target types.
-/

namespace PC88.Audit

universe u

/-- Full root: every 88-point type, every design, every resolution, every 88-cycle. -/
theorem root : PC88.Target.{u} := PC88.Bridge.target

/-- The canonical special case (points `ZMod 88`, cycle `x ↦ x + 1`). -/
theorem canonical : PC88.CanonicalTarget := PC88.Canonical.canonicalTarget

/-- Unfolded form of the root, for reading without the definitions of `Target`. -/
theorem root_unfolded {V : Type u} [Fintype V] [DecidableEq V] (hV : Fintype.card V = 88)
    (B : Finset (Finset V)) (R : Finset (Finset (Finset V))) (σ : Equiv.Perm V)
    (hD : PC88.IsDesign B) (hR : PC88.IsResolution B R) (hσ : σ.IsCycle)
    (hsupp : σ.support = Finset.univ) (hB : B.image (PC88.blockImage σ) = B)
    (hRσ : ∀ P ∈ R, P.image (PC88.blockImage σ) ∈ R) : False :=
  PC88.Bridge.target V hV B R ⟨hD, hR, σ, ⟨hσ, hsupp⟩, ⟨hB, hRσ⟩⟩

end PC88.Audit

#print PC88.IsDesign
#print PC88.IsParallelClass
#print PC88.IsResolution
#print PC88.blockImage
#print PC88.IsResolutionAut
#print PC88.IsFullCycle
#print PC88.IsPointCyclicResolution
#print PC88.Target
#print PC88.CanonicalTarget
#print Equiv.Perm.IsCycle
#print Equiv.Perm.SameCycle
set_option pp.funBinderTypes true in
#check @PC88.Bridge.target
set_option pp.funBinderTypes true in
#check @PC88.Bridge.target_of_canonical
set_option pp.funBinderTypes true in
#check @PC88.Bridge.canonical_of_target
set_option pp.funBinderTypes true in
#check @PC88.Bridge.exists_equiv_of_fullCycle
set_option pp.funBinderTypes true in
#check @PC88.Canonical.canonicalTarget
#check @PC88.Audit.root
#check @PC88.Audit.canonical
set_option pp.funBinderTypes true in
#check @PC88.Audit.root_unfolded
#print axioms PC88.Canonical.canonicalTarget
#print axioms PC88.Bridge.exists_equiv_of_fullCycle
#print axioms PC88.Bridge.target_of_canonical
#print axioms PC88.Bridge.target
#print axioms PC88.Bridge.canonical_of_target
#print axioms PC88.Audit.root
#print axioms PC88.Audit.canonical
#print axioms PC88.Audit.root_unfolded
