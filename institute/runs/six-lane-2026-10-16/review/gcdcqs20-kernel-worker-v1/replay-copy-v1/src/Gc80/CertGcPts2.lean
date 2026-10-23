import Gc80.DataGc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, gcDCQS(20^4 : 0), points 40-59

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes, 10 of them hole-free, and 970 triples, and the derived design has the group hole structure (`gcPointCheck`).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem gcPt_40 : gcPointCheck 80 20 blocksGc80 40 40 10 970 (colourGc80.getD 40 []) = true := by
  decide +kernel

theorem gcPt_41 : gcPointCheck 80 20 blocksGc80 41 40 10 970 (colourGc80.getD 41 []) = true := by
  decide +kernel

theorem gcPt_42 : gcPointCheck 80 20 blocksGc80 42 40 10 970 (colourGc80.getD 42 []) = true := by
  decide +kernel

theorem gcPt_43 : gcPointCheck 80 20 blocksGc80 43 40 10 970 (colourGc80.getD 43 []) = true := by
  decide +kernel

theorem gcPt_44 : gcPointCheck 80 20 blocksGc80 44 40 10 970 (colourGc80.getD 44 []) = true := by
  decide +kernel

theorem gcPt_45 : gcPointCheck 80 20 blocksGc80 45 40 10 970 (colourGc80.getD 45 []) = true := by
  decide +kernel

theorem gcPt_46 : gcPointCheck 80 20 blocksGc80 46 40 10 970 (colourGc80.getD 46 []) = true := by
  decide +kernel

theorem gcPt_47 : gcPointCheck 80 20 blocksGc80 47 40 10 970 (colourGc80.getD 47 []) = true := by
  decide +kernel

theorem gcPt_48 : gcPointCheck 80 20 blocksGc80 48 40 10 970 (colourGc80.getD 48 []) = true := by
  decide +kernel

theorem gcPt_49 : gcPointCheck 80 20 blocksGc80 49 40 10 970 (colourGc80.getD 49 []) = true := by
  decide +kernel

theorem gcPt_50 : gcPointCheck 80 20 blocksGc80 50 40 10 970 (colourGc80.getD 50 []) = true := by
  decide +kernel

theorem gcPt_51 : gcPointCheck 80 20 blocksGc80 51 40 10 970 (colourGc80.getD 51 []) = true := by
  decide +kernel

theorem gcPt_52 : gcPointCheck 80 20 blocksGc80 52 40 10 970 (colourGc80.getD 52 []) = true := by
  decide +kernel

theorem gcPt_53 : gcPointCheck 80 20 blocksGc80 53 40 10 970 (colourGc80.getD 53 []) = true := by
  decide +kernel

theorem gcPt_54 : gcPointCheck 80 20 blocksGc80 54 40 10 970 (colourGc80.getD 54 []) = true := by
  decide +kernel

theorem gcPt_55 : gcPointCheck 80 20 blocksGc80 55 40 10 970 (colourGc80.getD 55 []) = true := by
  decide +kernel

theorem gcPt_56 : gcPointCheck 80 20 blocksGc80 56 40 10 970 (colourGc80.getD 56 []) = true := by
  decide +kernel

theorem gcPt_57 : gcPointCheck 80 20 blocksGc80 57 40 10 970 (colourGc80.getD 57 []) = true := by
  decide +kernel

theorem gcPt_58 : gcPointCheck 80 20 blocksGc80 58 40 10 970 (colourGc80.getD 58 []) = true := by
  decide +kernel

theorem gcPt_59 : gcPointCheck 80 20 blocksGc80 59 40 10 970 (colourGc80.getD 59 []) = true := by
  decide +kernel

end Mcd.Kernel
