import BTDKernel.Audit

/-! Parent-authored binding of the frozen BTD(14,18;7,1,9;7,4) contract, using plain functions and explicit
Finset operations. Repeated columns are unrestricted. The root must have exactly this type, not merely the
worker's `Statement` definition. A satisfiable BTD(3,3;1,1,3;3,2) checks the same incidence-condition shape. -/
namespace ParentBtd14Audit

def Statement : Prop :=
  ¬ ∃ M : Fin 14 → Fin 18 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 7) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 1) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 7) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 4)

theorem no_btd : Statement := BTD14.Audit.root

def SmallStatement : Prop :=
  ∃ M : Fin 3 → Fin 3 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 1) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 1) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 3) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 2)

theorem small_exists : SmallStatement :=
  ⟨![![2, 0, 1], ![1, 2, 0], ![0, 1, 2]], by decide⟩

end ParentBtd14Audit

#print axioms ParentBtd14Audit.no_btd
#print axioms ParentBtd14Audit.small_exists
