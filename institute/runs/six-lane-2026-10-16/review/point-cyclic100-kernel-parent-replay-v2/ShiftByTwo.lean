import PC100Kernel.Cert100

/-! Parent-authored targets using only Mathlib notions.  `Statement`: a 2-(100,4,1) design on
`Fin 100` (4-point blocks, every pair in exactly one block) with a resolution (every class a set of
blocks partitioning the points, every block in exactly one class) and a permutation of the points
that is one cycle moving every point, maps the block set onto itself and maps every class onto a
class.  `ShiftStatement` names that permutation as `PC100.shift 100`, and `shift_is_succ` proves it
is x ↦ x + 1. -/
namespace ParentPC100Audit

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 100)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 100), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 100))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 100, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 100),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc100 : Statement := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc100
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement : Prop :=
  ((PC100.shift 100).IsCycle ∧ (PC100.shift 100).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 100)), ∃ R : Finset (Finset (Finset (Fin 100))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 100), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 100, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 100).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 100).toEmbedding) ∈ R

theorem shift_is_succ : ∀ x : Fin 100, PC100.shift 100 x = x + 2 := fun _ => rfl

theorem pc100_shift : ShiftStatement := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc100_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

end ParentPC100Audit

#print axioms ParentPC100Audit.pc100
#print axioms ParentPC100Audit.shift_is_succ
#print axioms ParentPC100Audit.pc100_shift
