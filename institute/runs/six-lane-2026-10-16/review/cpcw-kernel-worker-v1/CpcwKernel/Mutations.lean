import CpcwKernel.Generic

/-!
# Mutation operators for kernel-checked checker controls

Used only by the control module (`CpcwKernel.Controls`), never by a root.  Each operator acts on
raw certificate data, so controls are stated against the pinned literals themselves.
-/

namespace Cpcw.Kernel.Controls

open Cpcw.Kernel

/-- Add `1` modulo `v` to raw entry `j` of codeword `i` (a single changed point). -/
def bump (v : ℕ) (d : List (List ℕ)) (i j : ℕ) : List (List ℕ) :=
  d.set i ((d.getD i []).set j ((rawAt d i j + 1) % v))

/-- Set raw entry `j` of codeword `i` to `x`. -/
def setPoint (d : List (List ℕ)) (i j x : ℕ) : List (List ℕ) :=
  d.set i ((d.getD i []).set j x)

/-- Replace codeword `i` by a copy of codeword `0` (a duplicated codeword). -/
def dupFirst (d : List (List ℕ)) (i : ℕ) : List (List ℕ) :=
  d.set i (d.getD 0 [])

/-- Translate codeword `i` by `c` modulo `v`.  Ordered differences are unchanged, so a valid code
stays valid (a positive control that the checker is not keyed to the literal entries). -/
def translateBlock (v : ℕ) (d : List (List ℕ)) (i c : ℕ) : List (List ℕ) :=
  d.set i ((d.getD i []).map fun x => (x + c) % v)

/-- Multiply every entry by `m` modulo `v`.  For a unit `m` the ordered differences are permuted,
so a valid code stays valid (positive control). -/
def scale (v m : ℕ) (d : List (List ℕ)) : List (List ℕ) :=
  d.map (List.map fun x => x * m % v)

end Cpcw.Kernel.Controls
