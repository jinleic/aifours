import BTDKernel.Proof

/-!
# Audit: the explicit root statement, its proof, and the axioms used

`root` states nonexistence in fully explicit form (no definitions of this development appear in its type): there
is no `12 × 15` integer matrix whose entries are `0, 1, 2`, with exactly six entries `1` and exactly two entries `2`
in every row, every column sum `8`, and inner product `6` between any two distinct rows.  It is proved by the
definitionally equal `BTD12.no_btd`.
-/

namespace BTD12.Audit

open Finset

theorem root : ¬ ∃ M : Matrix (Fin 12) (Fin 15) ℤ,
    (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
    (∀ i, (univ.filter fun j => M i j = 1).card = 6) ∧
    (∀ i, (univ.filter fun j => M i j = 2).card = 2) ∧
    (∀ j, ∑ i, M i j = 8) ∧
    (∀ i k, i ≠ k → ∑ j, M i j * M k j = 6) :=
  BTD12.no_btd

theorem root_statement : BTD12.Statement := BTD12.no_btd

end BTD12.Audit

#print BTD12.IsBTDgen
#print BTD12.IsBTD
#print BTD12.Statement
#check @BTD12.Audit.root
#print axioms BTD12.Audit.root
#print axioms BTD12.Audit.root_statement
#print axioms BTD12.lemmaD
