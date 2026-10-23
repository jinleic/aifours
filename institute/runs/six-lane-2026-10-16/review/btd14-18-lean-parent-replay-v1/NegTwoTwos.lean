import BTDKernel.Audit

-- MUST FAIL: the target has one 2 per row, not two.
theorem parent_negative_two_twos :
    ¬ ∃ M : Fin 14 → Fin 18 → ℤ,
      (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
      (∀ i, (Finset.filter (fun j => M i j = 1) Finset.univ).card = 7) ∧
      (∀ i, (Finset.filter (fun j => M i j = 2) Finset.univ).card = 2) ∧
      (∀ j, Finset.sum Finset.univ (fun i => M i j) = 7) ∧
      (∀ i k, i ≠ k → Finset.sum Finset.univ (fun j => M i j * M k j) = 4) :=
  BTD14.Audit.root
