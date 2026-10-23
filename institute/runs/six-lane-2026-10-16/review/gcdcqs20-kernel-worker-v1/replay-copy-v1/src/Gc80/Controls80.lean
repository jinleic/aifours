import Gc80.Audit80

/-!
# Kernel controls for the gcDCQS(20^4 : 0) and mcDSQS(80) checkers

No root depends on this module.  Every mutation acts on the pinned literals of `Gc80.Data*`
themselves, and every Boolean statement is proved by kernel evaluation (`decide +kernel`):

* **gc swap**: in `POINT 5`, `CLASS 0` of the gcDCQS, the first points of the triples
  `(20, 68, 78)` and `(27, 47, 67)` exchanged.  The classes still pass `classOK` (pairwise
  disjoint, sorted), but the per-point check fails (`{27, 68, 78}` is not a derived triple).
* **gc holefree 9**: the per-point check at `5` with `s = 9` hole-free classes fails.
* **gc merge** (39 classes): `CLASS 38` and `CLASS 39` of `POINT 5` merged; the check with
  `r = 39` fails.
* **gc block**: the first block `(0, 1, 20, 63)` replaced by `(0, 1, 20, 62)`; the block-list
  check still passes (sorted, in range), but the per-point check at `0` fails.
* **hole**: the mcDSQS(80) blocks fail the gc hole check at `0` (they cover pairs inside the
  group of `0`), and the gcDCQS blocks fail the hole-free (SQS) check at `0`.
* **mc swap**, **mc merge** (39 classes), **mc reduce** (`(0, 13, 17)` replaced by
  `(0, 13, 97)`, the same residues modulo 80): the mcDSQS per-point check at `5` fails.
* **sts79 swap**: in `POINT 79`, `CLASS 0` of the mcDSQS, `(1, 21, 41), (2, 12, 54)` replaced by
  `(2, 21, 41), (1, 12, 54)`; the coloured-STS check on `Fin 79` fails.
* **reorder** (positive controls): the classes of `POINT 5` listed in reverse order still pass
  both per-point checks (the checkers are not keyed to the raw class order).
* **semantic**: no STS on `Fin 79` has a 39-colouring; `χ′(79) ≠ 39`; no explicit gc colouring
  has 9 hole-free classes.
-/

namespace Mcd.Kernel.Controls

open Mcd.Kernel

/-- Replace triple `t` of raw class `j` by `e`. -/
def setTriple (cls : List (List RawTriple)) (j t : ℕ) (e : RawTriple) : List (List RawTriple) :=
  cls.set j ((cls.getD j []).set t e)

/-- Merge the last two raw classes `38` and `39`. -/
def mergeLast (cls : List (List RawTriple)) : List (List RawTriple) :=
  cls.take 38 ++ [cls.getD 38 [] ++ cls.getD 39 []]

/-! ## gcDCQS(20^4 : 0) -/

def gcCol5swap : List (List RawTriple) :=
  setTriple (setTriple colGc80_5 0 0 (27, 68, 78)) 0 1 (20, 47, 67)

theorem gc_swap_spec :
    (colGc80_5.getD 0 []).take 2 = [(20, 68, 78), (27, 47, 67)] ∧
      (gcCol5swap.getD 0 []).take 2 = [(27, 68, 78), (20, 47, 67)] := by
  decide +kernel

theorem gc_swap_classes_ok : gcCol5swap.all (classOK 80) = true := by
  decide +kernel

theorem gc_swap_fails : gcPointCheck 80 20 blocksGc80 5 40 10 970 gcCol5swap = false := by
  decide +kernel

theorem gc_holefree9_fails :
    gcPointCheck 80 20 blocksGc80 5 40 9 970 (colourGc80.getD 5 []) = false := by
  decide +kernel

theorem gc_merge_spec : (mergeLast colGc80_5).length = 39 := by
  decide +kernel

theorem gc_merge_fails :
    gcPointCheck 80 20 blocksGc80 5 39 10 970 (mergeLast colGc80_5) = false := by
  decide +kernel

def blocksGcMut : List RawQuad := blocksGc80.set 0 (0, 1, 20, 62)

theorem gc_block_spec :
    blocksGc80.head? = some (0, 1, 20, 63) ∧ blocksGcMut.head? = some (0, 1, 20, 62) := by
  decide +kernel

theorem gc_block_blockCheck : blockCheck 80 19400 blocksGcMut = true := by
  decide +kernel

theorem gc_block_fails :
    gcPointCheck 80 20 blocksGcMut 0 40 10 970 (colourGc80.getD 0 []) = false := by
  decide +kernel

theorem mc_blocks_fail_gc_hole : holeCheck 80 blocksMc80 0 (groupHole 20 0) = false := by
  decide +kernel

theorem gc_blocks_fail_no_hole : holeCheck 80 blocksGc80 0 noHole = false := by
  decide +kernel

theorem gc_reorder_ok : gcPointCheck 80 20 blocksGc80 5 40 10 970 colGc80_5.reverse = true := by
  decide +kernel

/-! ## mcDSQS(80) -/

def mcCol5swap : List (List RawTriple) :=
  setTriple (setTriple colMc80_5 0 0 (1, 13, 17)) 0 1 (0, 3, 18)

theorem mc_swap_spec :
    (colMc80_5.getD 0 []).take 2 = [(0, 13, 17), (1, 3, 18)] ∧
      (mcCol5swap.getD 0 []).take 2 = [(1, 13, 17), (0, 3, 18)] := by
  decide +kernel

theorem mc_swap_classes_ok : mcCol5swap.all (classOK 80) = true := by
  decide +kernel

theorem mc_swap_fails : pointCheck 80 blocksMc80 5 noHole 40 1027 mcCol5swap = false := by
  decide +kernel

theorem mc_merge_fails :
    pointCheck 80 blocksMc80 5 noHole 39 1027 (mergeLast colMc80_5) = false := by
  decide +kernel

theorem mc_reduce_fails :
    pointCheck 80 blocksMc80 5 noHole 40 1027 (setTriple colMc80_5 0 0 (0, 13, 97)) = false := by
  decide +kernel

theorem mc_reorder_ok : pointCheck 80 blocksMc80 5 noHole 40 1027 colMc80_5.reverse = true := by
  decide +kernel

def mcCol79swap : List (List RawTriple) :=
  setTriple (setTriple colMc80_79 0 0 (2, 21, 41)) 0 1 (1, 12, 54)

theorem sts79_swap_spec :
    (colMc80_79.getD 0 []).take 2 = [(1, 21, 41), (2, 12, 54)] ∧
      (mcCol79swap.getD 0 []).take 2 = [(2, 21, 41), (1, 12, 54)] := by
  decide +kernel

theorem sts79_swap_fails : stsColCheck 79 mcCol79swap = false := by
  decide +kernel

/-! ## Semantic controls -/

/-- No STS on `Fin 79` has a 39-colouring. -/
theorem no_39_colouring_sts79 : ¬ ∃ S : Finset (Finset (Fin 79)), IsSTS S ∧
    ∃ C : Finset (Finset (Finset (Fin 79))), IsColouring S C ∧ C.card = 39 := by
  rintro ⟨S, hS, C, hC, hcard⟩
  have := Mcd.Counts.colourLowerBound_79 (Fin 79) (Fintype.card_fin 79) S hS C hC
  omega

theorem chiPrime_79_ne_39 : chiPrime 79 ≠ 39 := by
  rw [chiPrime_79]
  decide

/-- No explicit gc colouring has exactly 9 hole-free classes. -/
theorem gc_not_9_holefree (x : Fin 80) :
    ((colouringGc80 x).filter fun P =>
      ∀ T ∈ P, Disjoint T ((grp80 (x.val / 20)).erase x)).card ≠ 9 := by
  rw [(colouringGc80_spec x).2.2]
  decide

/-- No block of the explicit gcDCQS has 5 points. -/
theorem gc_no_block_of_size_5 : ∀ X ∈ gcdcqs80, X.card ≠ 5 := by
  intro X hX
  rw [gc_card4 X hX]
  decide

end Mcd.Kernel.Controls

#print axioms Mcd.Kernel.Controls.gc_swap_fails
#print axioms Mcd.Kernel.Controls.gc_holefree9_fails
#print axioms Mcd.Kernel.Controls.gc_merge_fails
#print axioms Mcd.Kernel.Controls.gc_block_blockCheck
#print axioms Mcd.Kernel.Controls.gc_block_fails
#print axioms Mcd.Kernel.Controls.mc_blocks_fail_gc_hole
#print axioms Mcd.Kernel.Controls.gc_blocks_fail_no_hole
#print axioms Mcd.Kernel.Controls.gc_reorder_ok
#print axioms Mcd.Kernel.Controls.mc_swap_fails
#print axioms Mcd.Kernel.Controls.mc_merge_fails
#print axioms Mcd.Kernel.Controls.mc_reduce_fails
#print axioms Mcd.Kernel.Controls.mc_reorder_ok
#print axioms Mcd.Kernel.Controls.sts79_swap_fails
#print axioms Mcd.Kernel.Controls.no_39_colouring_sts79
#print axioms Mcd.Kernel.Controls.chiPrime_79_ne_39
#print axioms Mcd.Kernel.Controls.gc_not_9_holefree
#print axioms Mcd.Kernel.Controls.gc_no_block_of_size_5
