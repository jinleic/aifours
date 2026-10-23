import Mathlib.Data.Fintype.Prod

/-!
# Cyclic `(v, 5, 1)` difference families: the target statement

This module imports no certificate data and fixes the meaning of the kernel-checked roots.

* Residues modulo `v` are the elements of `Fin v`.  For `a b : Fin v`, `a - b` is the core
  `Fin.sub`, i.e. subtraction modulo `v`: its value is `(v - b + a) % v`
  (`CdfKernel.Facts` proves `a - b = d ↔ d ≡ a - b [ZMOD v]`).
* A family of `n` base blocks is a map `B : Fin n → Fin 5 → Fin v`; base block `i` lists the
  five residues `B i 0, ..., B i 4`.
* `Cdf.diffs B` is the multiset of ordered differences `B i j - B i k` over every base block `i`
  and every ordered pair `(j, k)` of distinct positions.  When the five residues of each block
  are distinct, these are exactly the ordered differences `a - b` of distinct elements `a, b` of
  each block, each block contributing `5 * 4 = 20` of them.
* `Cdf.IsCDF B`: each base block consists of five distinct residues, and `Cdf.diffs B` contains
  every nonzero residue exactly once and the residue `0` never.
* `Cdf.Target v`: a cyclic `(v, 5, 1)` difference family exists (with some number of blocks).
-/

namespace Cdf

/-- The multiset of ordered differences `B i j - B i k` (subtraction in `Fin v`, i.e. modulo
`v`) over all base blocks `i` and all ordered pairs `(j, k)` of distinct positions `j ≠ k`. -/
def diffs {v n : ℕ} (B : Fin n → Fin 5 → Fin v) : Multiset (Fin v) :=
  ((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
    fun t => B t.1 t.2.1 - B t.1 t.2.2

/-- `B` is a cyclic `(v, 5, 1)` difference family: every base block consists of five distinct
residues modulo `v`, every nonzero residue occurs exactly once in the multiset of ordered
differences, and the residue `0` never occurs in it. -/
def IsCDF {v n : ℕ} (B : Fin n → Fin 5 → Fin v) : Prop :=
  (∀ i : Fin n, Function.Injective (B i)) ∧
    (∀ d : Fin v, d.val ≠ 0 → (diffs B).count d = 1) ∧
    (∀ d : Fin v, d.val = 0 → (diffs B).count d = 0)

/-- A cyclic `(v, 5, 1)` difference family exists. -/
def Target (v : ℕ) : Prop :=
  ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin v, IsCDF B

end Cdf
