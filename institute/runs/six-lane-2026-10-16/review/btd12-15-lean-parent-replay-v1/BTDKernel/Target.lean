import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# BTD(12,15;6,2,10;8,6): the target statement

This module contains no proof.  It fixes the meaning of the kernel-checked root, following the frozen contract
`institute/runs/six-lane-2026-10-16/screening/info-2-btd12-15-contract.json` and the Francel–Hurd definition
(Australas. J. Combin. 42 (2008), pp. 3–5): a balanced ternary design BTD(V,B;ρ₁,ρ₂,R;K,Λ) is represented by its
`V × B` incidence matrix with entries `0, 1, 2`; every row has exactly `ρ₁` entries `1` and exactly `ρ₂` entries `2`
(so `R = ρ₁ + 2ρ₂`), every column sums to `K`, and any two distinct rows have inner product `Λ`.  Repeated columns
(repeated blocks) are allowed; no simplicity, cyclicity, orbit or ordering assumption is made.

* `IsBTDgen ρ₁ ρ₂ K Λ M` : the incidence-matrix conditions above for an integer matrix `M`.
* `IsBTD M` : the target instance `V = 12`, `B = 15`, `ρ₁ = 6`, `ρ₂ = 2`, `K = 8`, `Λ = 6`.
* `Statement` : no `12 × 15` integer matrix satisfies `IsBTD`.
-/

namespace BTD12

open Finset

/-- `M` (a `V × B` integer matrix) is the incidence matrix of a balanced ternary design with `ρ₁` entries `1` and
`ρ₂` entries `2` per row, column sums `K` and pairwise row inner products `Λ`. -/
def IsBTDgen {V B : ℕ} (ρ₁ ρ₂ : ℕ) (K Λ : ℤ) (M : Matrix (Fin V) (Fin B) ℤ) : Prop :=
  (∀ i j, M i j = 0 ∨ M i j = 1 ∨ M i j = 2) ∧
  (∀ i, (univ.filter fun j => M i j = 1).card = ρ₁) ∧
  (∀ i, (univ.filter fun j => M i j = 2).card = ρ₂) ∧
  (∀ j, ∑ i, M i j = K) ∧
  (∀ i k, i ≠ k → ∑ j, M i j * M k j = Λ)

/-- the target instance BTD(12,15;6,2,10;8,6) -/
def IsBTD (M : Matrix (Fin 12) (Fin 15) ℤ) : Prop := IsBTDgen 6 2 8 6 M

/-- the statement proved in `BTDKernel.Proof` -/
def Statement : Prop := ¬ ∃ M : Matrix (Fin 12) (Fin 15) ℤ, IsBTD M

end BTD12
