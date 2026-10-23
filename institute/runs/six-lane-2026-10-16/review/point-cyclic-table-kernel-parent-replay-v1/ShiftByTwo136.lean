import PCTableKernelR2.Cert112
import PCTableKernelR2.Cert136
import PCTableKernelR2.Cert160
import PCTableKernelR2.Cert196

/-! Parent-authored targets using only Mathlib notions.  For each listed v, `Statement` asserts a 2-(v,4,1)
design on `Fin v` with a resolution and a single-cycle point permutation preserving the blocks and mapping every
class onto a class; `ShiftStatement` names that permutation as `PC100.shift v`, which is x ↦ x + 1. -/
namespace ParentPCTableAudit

def Statement112 : Prop :=
  ∃ B : Finset (Finset (Fin 112)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 112), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 112))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 112, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 112),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc112 : Statement112 := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc112
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement112 : Prop :=
  ((PC100.shift 112).IsCycle ∧ (PC100.shift 112).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 112)), ∃ R : Finset (Finset (Finset (Fin 112))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 112), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 112, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 112).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 112).toEmbedding) ∈ R

theorem shift112_is_succ : ∀ x : Fin 112, PC100.shift 112 x = x + 1 := fun _ => rfl

theorem pc112_shift : ShiftStatement112 := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc112_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

def Statement136 : Prop :=
  ∃ B : Finset (Finset (Fin 136)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 136), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 136))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 136, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 136),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc136 : Statement136 := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc136
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement136 : Prop :=
  ((PC100.shift 136).IsCycle ∧ (PC100.shift 136).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 136)), ∃ R : Finset (Finset (Finset (Fin 136))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 136), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 136, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 136).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 136).toEmbedding) ∈ R

theorem shift136_is_succ : ∀ x : Fin 136, PC100.shift 136 x = x + 2 := fun _ => rfl

theorem pc136_shift : ShiftStatement136 := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc136_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

def Statement160 : Prop :=
  ∃ B : Finset (Finset (Fin 160)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 160), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 160))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 160, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 160),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc160 : Statement160 := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc160
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement160 : Prop :=
  ((PC100.shift 160).IsCycle ∧ (PC100.shift 160).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 160)), ∃ R : Finset (Finset (Finset (Fin 160))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 160), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 160, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 160).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 160).toEmbedding) ∈ R

theorem shift160_is_succ : ∀ x : Fin 160, PC100.shift 160 x = x + 1 := fun _ => rfl

theorem pc160_shift : ShiftStatement160 := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc160_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

def Statement196 : Prop :=
  ∃ B : Finset (Finset (Fin 196)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 196), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∃ R : Finset (Finset (Finset (Fin 196))),
      ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 196, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
      ∃ σ : Equiv.Perm (Fin 196),
        (σ.IsCycle ∧ σ.support = Finset.univ) ∧
        B.image (fun X => X.map σ.toEmbedding) = B ∧
        ∀ P ∈ R, P.image (fun X => X.map σ.toEmbedding) ∈ R

theorem pc196 : Statement196 := by
  obtain ⟨B, hB, R, hR, σ, hσ, hA⟩ := PC100.Kernel.exists_pc196
  exact ⟨B, hB, R, hR, σ, hσ, hA⟩

def ShiftStatement196 : Prop :=
  ((PC100.shift 196).IsCycle ∧ (PC100.shift 196).support = Finset.univ) ∧
  ∃ B : Finset (Finset (Fin 196)), ∃ R : Finset (Finset (Finset (Fin 196))),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 196), T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ((∀ P ∈ R, P ⊆ B ∧ ∀ y : Fin 196, ∃! X, X ∈ P ∧ y ∈ X) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P) ∧
    B.image (fun X => X.map (PC100.shift 196).toEmbedding) = B ∧
    ∀ P ∈ R, P.image (fun X => X.map (PC100.shift 196).toEmbedding) ∈ R

theorem shift196_is_succ : ∀ x : Fin 196, PC100.shift 196 x = x + 1 := fun _ => rfl

theorem pc196_shift : ShiftStatement196 := by
  obtain ⟨hcyc, B, R, hB, hR, hA⟩ := PC100.Kernel.exists_pc196_shift
  exact ⟨hcyc, B, R, hB, hR, hA⟩

end ParentPCTableAudit

#print axioms ParentPCTableAudit.pc112
#print axioms ParentPCTableAudit.shift112_is_succ
#print axioms ParentPCTableAudit.pc112_shift
#print axioms ParentPCTableAudit.pc136
#print axioms ParentPCTableAudit.shift136_is_succ
#print axioms ParentPCTableAudit.pc136_shift
#print axioms ParentPCTableAudit.pc160
#print axioms ParentPCTableAudit.shift160_is_succ
#print axioms ParentPCTableAudit.pc160_shift
#print axioms ParentPCTableAudit.pc196
#print axioms ParentPCTableAudit.shift196_is_succ
#print axioms ParentPCTableAudit.pc196_shift
