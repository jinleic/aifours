import BTDKernel.Audit

/-! Parent-authored binding audit (not written by the worker).  `Statement` restates the frozen contract
`screening/info-2-btd12-15-contract.json` directly with plain functions `Fin 12 → Fin 15 → ℤ` and explicit
`Finset.filter`/`Finset.sum`: no 12 × 15 array over {0,1,2} has exactly six entries 1 and exactly two entries 2 in
every row, every column summing to 8, and inner product 6 between any two distinct rows.  Repeated columns are
allowed because nothing forbids them.  The kernel must accept the worker's root at exactly this type.
`SmallStatement` is a positive control: the same shape at BTD(3,3;1,1,3;3,2) is satisfiable. -/

namespace ParentBtdAudit

def Statement : Prop :=
  ¬ ∃ M : Fin 12 → Fin 15 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 6) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 2) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 8) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 6)

theorem no_btd : Statement := BTD12.Audit.root

def SmallStatement : Prop :=
  ∃ M : Fin 3 → Fin 3 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 1) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 1) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 3) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 2)

theorem small_exists : SmallStatement :=
  ⟨![![2, 0, 1], ![1, 2, 0], ![0, 1, 2]], by decide⟩

end ParentBtdAudit

#print axioms ParentBtdAudit.no_btd
#print axioms ParentBtdAudit.small_exists
