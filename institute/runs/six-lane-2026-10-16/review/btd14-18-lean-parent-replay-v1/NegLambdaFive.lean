import BTDKernel.Audit

-- MUST FAIL: the target inner product is 4, not 5.
theorem parent_negative_lambda_five :
    ¬ ∃ M : Fin 14 → Fin 18 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 7) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 1) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 7) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 5) :=
  BTD14.Audit.root
