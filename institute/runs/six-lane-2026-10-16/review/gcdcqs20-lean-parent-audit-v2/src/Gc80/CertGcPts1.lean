import Gc80.DataGc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, gcDCQS(20^4 : 0), points 20-39

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes, 10 of them hole-free, and 970 triples, and the derived design has the group hole structure (`gcPointCheck`).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem gcPt_20 : gcPointCheck 80 20 blocksGc80 20 40 10 970 (colourGc80.getD 20 []) = true := by
  decide +kernel

theorem gcPt_21 : gcPointCheck 80 20 blocksGc80 21 40 10 970 (colourGc80.getD 21 []) = true := by
  decide +kernel

theorem gcPt_22 : gcPointCheck 80 20 blocksGc80 22 40 10 970 (colourGc80.getD 22 []) = true := by
  decide +kernel

theorem gcPt_23 : gcPointCheck 80 20 blocksGc80 23 40 10 970 (colourGc80.getD 23 []) = true := by
  decide +kernel

theorem gcPt_24 : gcPointCheck 80 20 blocksGc80 24 40 10 970 (colourGc80.getD 24 []) = true := by
  decide +kernel

theorem gcPt_25 : gcPointCheck 80 20 blocksGc80 25 40 10 970 (colourGc80.getD 25 []) = true := by
  decide +kernel

theorem gcPt_26 : gcPointCheck 80 20 blocksGc80 26 40 10 970 (colourGc80.getD 26 []) = true := by
  decide +kernel

theorem gcPt_27 : gcPointCheck 80 20 blocksGc80 27 40 10 970 (colourGc80.getD 27 []) = true := by
  decide +kernel

theorem gcPt_28 : gcPointCheck 80 20 blocksGc80 28 40 10 970 (colourGc80.getD 28 []) = true := by
  decide +kernel

theorem gcPt_29 : gcPointCheck 80 20 blocksGc80 29 40 10 970 (colourGc80.getD 29 []) = true := by
  decide +kernel

theorem gcPt_30 : gcPointCheck 80 20 blocksGc80 30 40 10 970 (colourGc80.getD 30 []) = true := by
  decide +kernel

theorem gcPt_31 : gcPointCheck 80 20 blocksGc80 31 40 10 970 (colourGc80.getD 31 []) = true := by
  decide +kernel

theorem gcPt_32 : gcPointCheck 80 20 blocksGc80 32 40 10 970 (colourGc80.getD 32 []) = true := by
  decide +kernel

theorem gcPt_33 : gcPointCheck 80 20 blocksGc80 33 40 10 970 (colourGc80.getD 33 []) = true := by
  decide +kernel

theorem gcPt_34 : gcPointCheck 80 20 blocksGc80 34 40 10 970 (colourGc80.getD 34 []) = true := by
  decide +kernel

theorem gcPt_35 : gcPointCheck 80 20 blocksGc80 35 40 10 970 (colourGc80.getD 35 []) = true := by
  decide +kernel

theorem gcPt_36 : gcPointCheck 80 20 blocksGc80 36 40 10 970 (colourGc80.getD 36 []) = true := by
  decide +kernel

theorem gcPt_37 : gcPointCheck 80 20 blocksGc80 37 40 10 970 (colourGc80.getD 37 []) = true := by
  decide +kernel

theorem gcPt_38 : gcPointCheck 80 20 blocksGc80 38 40 10 970 (colourGc80.getD 38 []) = true := by
  decide +kernel

theorem gcPt_39 : gcPointCheck 80 20 blocksGc80 39 40 10 970 (colourGc80.getD 39 []) = true := by
  decide +kernel

end Mcd.Kernel
