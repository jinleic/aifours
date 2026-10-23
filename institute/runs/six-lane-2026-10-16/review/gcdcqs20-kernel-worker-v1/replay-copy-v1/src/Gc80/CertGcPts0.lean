import Gc80.DataGc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, gcDCQS(20^4 : 0), points 0-19

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes, 10 of them hole-free, and 970 triples, and the derived design has the group hole structure (`gcPointCheck`).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem gcPt_0 : gcPointCheck 80 20 blocksGc80 0 40 10 970 (colourGc80.getD 0 []) = true := by
  decide +kernel

theorem gcPt_1 : gcPointCheck 80 20 blocksGc80 1 40 10 970 (colourGc80.getD 1 []) = true := by
  decide +kernel

theorem gcPt_2 : gcPointCheck 80 20 blocksGc80 2 40 10 970 (colourGc80.getD 2 []) = true := by
  decide +kernel

theorem gcPt_3 : gcPointCheck 80 20 blocksGc80 3 40 10 970 (colourGc80.getD 3 []) = true := by
  decide +kernel

theorem gcPt_4 : gcPointCheck 80 20 blocksGc80 4 40 10 970 (colourGc80.getD 4 []) = true := by
  decide +kernel

theorem gcPt_5 : gcPointCheck 80 20 blocksGc80 5 40 10 970 (colourGc80.getD 5 []) = true := by
  decide +kernel

theorem gcPt_6 : gcPointCheck 80 20 blocksGc80 6 40 10 970 (colourGc80.getD 6 []) = true := by
  decide +kernel

theorem gcPt_7 : gcPointCheck 80 20 blocksGc80 7 40 10 970 (colourGc80.getD 7 []) = true := by
  decide +kernel

theorem gcPt_8 : gcPointCheck 80 20 blocksGc80 8 40 10 970 (colourGc80.getD 8 []) = true := by
  decide +kernel

theorem gcPt_9 : gcPointCheck 80 20 blocksGc80 9 40 10 970 (colourGc80.getD 9 []) = true := by
  decide +kernel

theorem gcPt_10 : gcPointCheck 80 20 blocksGc80 10 40 10 970 (colourGc80.getD 10 []) = true := by
  decide +kernel

theorem gcPt_11 : gcPointCheck 80 20 blocksGc80 11 40 10 970 (colourGc80.getD 11 []) = true := by
  decide +kernel

theorem gcPt_12 : gcPointCheck 80 20 blocksGc80 12 40 10 970 (colourGc80.getD 12 []) = true := by
  decide +kernel

theorem gcPt_13 : gcPointCheck 80 20 blocksGc80 13 40 10 970 (colourGc80.getD 13 []) = true := by
  decide +kernel

theorem gcPt_14 : gcPointCheck 80 20 blocksGc80 14 40 10 970 (colourGc80.getD 14 []) = true := by
  decide +kernel

theorem gcPt_15 : gcPointCheck 80 20 blocksGc80 15 40 10 970 (colourGc80.getD 15 []) = true := by
  decide +kernel

theorem gcPt_16 : gcPointCheck 80 20 blocksGc80 16 40 10 970 (colourGc80.getD 16 []) = true := by
  decide +kernel

theorem gcPt_17 : gcPointCheck 80 20 blocksGc80 17 40 10 970 (colourGc80.getD 17 []) = true := by
  decide +kernel

theorem gcPt_18 : gcPointCheck 80 20 blocksGc80 18 40 10 970 (colourGc80.getD 18 []) = true := by
  decide +kernel

theorem gcPt_19 : gcPointCheck 80 20 blocksGc80 19 40 10 970 (colourGc80.getD 19 []) = true := by
  decide +kernel

end Mcd.Kernel
