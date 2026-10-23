import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs

/-!
# Bhaskar Rao designs: target definitions (no data, no proofs)

A Bhaskar Rao design BRD(v, b, r, k, λ) is a `v × b` matrix with entries in `{-1, 0, 1}` such that
every row has exactly `r` nonzero entries, every column has exactly `k` nonzero entries, and for every
two distinct rows exactly `λ / 2` columns give the product `+1` and exactly `λ / 2` columns give the
product `-1`.  Repeated columns are allowed.  Matrices are plain functions `Fin v → Fin b → ℤ`.

* `IsBRD` states this by counting the signed products directly (`2 * #{+1} = λ` and `2 * #{-1} = λ`,
  so `λ` must be even).
* `IsBRDStd` is the literature form: the supports of two distinct rows meet in exactly `λ` columns and
  the two rows are orthogonal (`∑ j, M i j * M i' j = 0`).  Orthogonality alone is not used anywhere
  without the support-intersection count.
-/

namespace Brd26

/-- `M` is a BRD(v, b, r, k, λ), stated by counting signed products. -/
def IsBRD (v b r k lam : ℕ) (M : Fin v → Fin b → ℤ) : Prop :=
  (∀ i j, M i j = -1 ∨ M i j = 0 ∨ M i j = 1) ∧
  (∀ i, (Finset.univ.filter fun j => M i j ≠ 0).card = r) ∧
  (∀ j, (Finset.univ.filter fun i => M i j ≠ 0).card = k) ∧
  (∀ i i', i ≠ i' →
    2 * (Finset.univ.filter fun j => M i j * M i' j = 1).card = lam ∧
    2 * (Finset.univ.filter fun j => M i j * M i' j = -1).card = lam)

/-- `M` is a BRD(v, b, r, k, λ), literature form: support intersections of size `λ` and orthogonal
rows. -/
def IsBRDStd (v b r k lam : ℕ) (M : Fin v → Fin b → ℤ) : Prop :=
  (∀ i j, M i j = -1 ∨ M i j = 0 ∨ M i j = 1) ∧
  (∀ i, (Finset.univ.filter fun j => M i j ≠ 0).card = r) ∧
  (∀ j, (Finset.univ.filter fun i => M i j ≠ 0).card = k) ∧
  (∀ i i', i ≠ i' →
    (Finset.univ.filter fun j => M i j ≠ 0 ∧ M i' j ≠ 0).card = lam ∧
    ∑ j, M i j * M i' j = 0)

end Brd26
