import RdsqsKernel.Cert52

/-! Parent-authored target.  Only Mathlib notions appear in `Statement`: an SQS(52) on `Fin 53`
(every block has 4 points, every 3-subset lies in exactly one block) whose derived design at EVERY
point `x` (blocks `X.erase x` for the blocks `X` through `x`) has a resolution `R`: a set of
parallel classes, each consisting of derived blocks and partitioning the points other than `x`,
such that every derived block lies in exactly one class. -/
namespace ParentRdsqsAudit

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 53)),
    (∀ X ∈ B, X.card = 4) ∧
    (∀ T : Finset (Fin 53), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∀ x : Fin 53, ∃ R : Finset (Finset (Finset (Fin 53))),
      (∀ P ∈ R, (∀ T ∈ P, ∃ X ∈ B, x ∈ X ∧ T = X.erase x) ∧
        ∀ y : Fin 53, y ≠ x → ∃! T, T ∈ P ∧ y ∈ T) ∧
      (∀ X ∈ B, x ∈ X → ∃! P, P ∈ R ∧ X.erase x ∈ P)

theorem rdsqs52 : Statement := by
  obtain ⟨B, ⟨hcard, hcover⟩, hres⟩ := Rdsqs.Kernel.exists_rdsqs52
  refine ⟨B, hcard, hcover, fun x => ?_⟩
  obtain ⟨R, hclasses, hunique⟩ := hres x
  refine ⟨R, fun P hP => ?_, fun X hX hxX => hunique _ ?_⟩
  · obtain ⟨hsub, hpart⟩ := hclasses P hP
    refine ⟨fun T hT => ?_, hpart⟩
    obtain ⟨X, hXf, hXT⟩ := Finset.mem_image.mp (hsub hT)
    exact ⟨X, (Finset.mem_filter.mp hXf).1, (Finset.mem_filter.mp hXf).2, hXT.symm⟩
  · exact Finset.mem_image.mpr ⟨X, Finset.mem_filter.mpr ⟨hX, hxX⟩, rfl⟩

end ParentRdsqsAudit

#print axioms ParentRdsqsAudit.rdsqs52
