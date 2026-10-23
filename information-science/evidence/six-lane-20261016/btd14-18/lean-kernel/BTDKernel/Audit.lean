import BTDKernel.Proof

/-!
# Audit: the explicit root statement, its proof, and the axioms used

`root` states nonexistence in fully explicit form (no definitions of this development appear in its type): there
is no `14 × 18` integer matrix whose entries are `0, 1, 2`, with exactly seven entries `1` and exactly one entry `2`
in every row, every column sum `7`, and inner product `4` between any two distinct rows.  It is proved by the
definitionally equal `BTD14.no_btd`.
-/

namespace BTD14.Audit

open Finset

theorem root : ¬ ∃ M : Matrix (Fin 14) (Fin 18) ℤ,
    (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
    (∀ i, (univ.filter fun j => M i j = 1).card = 7) ∧
    (∀ i, (univ.filter fun j => M i j = 2).card = 1) ∧
    (∀ j, ∑ i, M i j = 7) ∧
    (∀ i k, i ≠ k → ∑ j, M i j * M k j = 4) :=
  BTD14.no_btd

theorem root_statement : BTD14.Statement := BTD14.no_btd

end BTD14.Audit

#print BTD14.IsBTDgen
#print BTD14.IsBTD
#print BTD14.Statement
#check @BTD14.Audit.root
#print axioms BTD14.Audit.root
#print axioms BTD14.Audit.root_statement
#print axioms BTD14.lemmaD4
