import CdfKernel.Generic

/-!
# Mutation operators for kernel-checked checker controls

Used only by the control modules (`CdfKernel.Controls*`), never by a root.  Each operator acts on
raw certificate data, so controls are stated against the pinned literals themselves.
-/

namespace Cdf.Kernel.Controls

open Cdf.Kernel

/-- Add `1` modulo `v` to raw entry `j` of block `i` (a single changed residue). -/
def bump (v : ℕ) (d : List (List ℕ)) (i j : ℕ) : List (List ℕ) :=
  d.set i ((d.getD i []).set j ((rawAt d i j + 1) % v))

/-- Replace block `i` by a copy of block `0` (a duplicated block). -/
def dupFirst (d : List (List ℕ)) (i : ℕ) : List (List ℕ) :=
  d.set i (d.getD 0 [])

/-- Translate block `i` by `c` modulo `v`.  Ordered differences are unchanged, so a valid family
stays valid (a positive control that the checker is not keyed to the literal entries). -/
def translateBlock (v : ℕ) (d : List (List ℕ)) (i c : ℕ) : List (List ℕ) :=
  d.set i ((d.getD i []).map fun x => (x + c) % v)

/-- Multiply every entry by `m` modulo `v`.  For a unit `m` the differences are permuted, so a
valid family stays valid (positive control). -/
def scale (v m : ℕ) (d : List (List ℕ)) : List (List ℕ) :=
  d.map (List.map fun x => x * m % v)

end Cdf.Kernel.Controls
