import BTDKernel.Audit

/-! Parent negative control: MUST FAIL to compile (inner product 6 changed to 5). -/

theorem parent_negative_NegLambdaFive :
    ¬ ∃ M : Fin 12 → Fin 15 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 6) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 2) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 8) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 5) :=
  BTD12.Audit.root
