import Mathlib.Data.Fintype.Prod

/-!
# Optimal `(v, k, 1)` CPCW codes: the target statement

This module imports no certificate data and fixes the meaning of the kernel-checked roots.

* Residues modulo `v` are the elements of `Fin v`.  For `a b : Fin v`, `a - b` is the core
  `Fin.sub`, i.e. subtraction modulo `v`: its value is `(v - b + a) % v`
  (`CpcwKernel.Facts` proves `a - b = d ↔ d ≡ a - b [ZMOD v]`).
* A family of `n` codewords of weight `k` is a map `B : Fin n → Fin k → Fin v`; codeword `i`
  lists the `k` residues `B i 0, ..., B i (k - 1)`.
* `Cpcw.diffs B` is the multiset of ordered differences `B i j - B i l` over every codeword `i`
  and every ordered pair `(j, l)` of distinct positions.  When the `k` residues of each codeword
  are distinct, these are exactly the ordered differences `a - b` of distinct elements `a, b` of
  each codeword, each codeword contributing `k * (k - 1)` of them.
* `Cpcw.IsCPCW B`: each codeword consists of `k` distinct residues, every nonzero residue occurs
  at most once in `Cpcw.diffs B`, and the residue `0` never occurs in it.  (A difference packing;
  `CpcwKernel.Facts` proves that this is equivalent to the auto- and cross-correlation form of the
  definition.)  Nonzero residues that occur zero times (the leave) are allowed.
* `Cpcw.IsOptimalCPCW B`: `Cpcw.IsCPCW B`, and the number `n` of codewords equals
  `(v - 1) / (k * (k - 1))` (natural-number division, i.e. the floor).
* `Cpcw.Target v k`: a family satisfying `Cpcw.IsOptimalCPCW` exists.
* `Cpcw.OptimalTarget v k`: `Cpcw.Target v k`, and every family satisfying `Cpcw.IsCPCW` (with any
  number of codewords) has at most `(v - 1) / (k * (k - 1))` codewords.
-/

namespace Cpcw

/-- The multiset of ordered differences `B i j - B i l` (subtraction in `Fin v`, i.e. modulo
`v`) over all codewords `i` and all ordered pairs `(j, l)` of distinct positions `j ≠ l`. -/
def diffs {v k n : ℕ} (B : Fin n → Fin k → Fin v) : Multiset (Fin v) :=
  ((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
    fun t => B t.1 t.2.1 - B t.1 t.2.2

/-- `B` is a `(v, k, 1)` CPCW code (difference form): every codeword consists of `k` distinct
residues modulo `v`, every nonzero residue occurs at most once in the multiset of ordered
differences, and the residue `0` never occurs in it. -/
def IsCPCW {v k n : ℕ} (B : Fin n → Fin k → Fin v) : Prop :=
  (∀ i : Fin n, Function.Injective (B i)) ∧
    (∀ d : Fin v, d.val ≠ 0 → (diffs B).count d ≤ 1) ∧
    (∀ d : Fin v, d.val = 0 → (diffs B).count d = 0)

/-- `B` is a `(v, k, 1)` CPCW code whose number of codewords is `⌊(v - 1) / (k (k - 1))⌋`. -/
def IsOptimalCPCW {v k n : ℕ} (B : Fin n → Fin k → Fin v) : Prop :=
  IsCPCW B ∧ n = (v - 1) / (k * (k - 1))

/-- A `(v, k, 1)` CPCW code with `⌊(v - 1) / (k (k - 1))⌋` codewords exists. -/
def Target (v k : ℕ) : Prop :=
  ∃ n : ℕ, ∃ B : Fin n → Fin k → Fin v, IsOptimalCPCW B

/-- A `(v, k, 1)` CPCW code with `⌊(v - 1) / (k (k - 1))⌋` codewords exists, and no `(v, k, 1)`
CPCW code has more codewords. -/
def OptimalTarget (v k : ℕ) : Prop :=
  Target v k ∧ ∀ n : ℕ, ∀ B : Fin n → Fin k → Fin v, IsCPCW B → n ≤ (v - 1) / (k * (k - 1))

end Cpcw
