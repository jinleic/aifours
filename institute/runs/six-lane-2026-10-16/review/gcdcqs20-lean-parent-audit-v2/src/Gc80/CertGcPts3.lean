import Gc80.DataGc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, gcDCQS(20^4 : 0), points 60-79

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes, 10 of them hole-free, and 970 triples, and the derived design has the group hole structure (`gcPointCheck`).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem gcPt_60 : gcPointCheck 80 20 blocksGc80 60 40 10 970 (colourGc80.getD 60 []) = true := by
  decide +kernel

theorem gcPt_61 : gcPointCheck 80 20 blocksGc80 61 40 10 970 (colourGc80.getD 61 []) = true := by
  decide +kernel

theorem gcPt_62 : gcPointCheck 80 20 blocksGc80 62 40 10 970 (colourGc80.getD 62 []) = true := by
  decide +kernel

theorem gcPt_63 : gcPointCheck 80 20 blocksGc80 63 40 10 970 (colourGc80.getD 63 []) = true := by
  decide +kernel

theorem gcPt_64 : gcPointCheck 80 20 blocksGc80 64 40 10 970 (colourGc80.getD 64 []) = true := by
  decide +kernel

theorem gcPt_65 : gcPointCheck 80 20 blocksGc80 65 40 10 970 (colourGc80.getD 65 []) = true := by
  decide +kernel

theorem gcPt_66 : gcPointCheck 80 20 blocksGc80 66 40 10 970 (colourGc80.getD 66 []) = true := by
  decide +kernel

theorem gcPt_67 : gcPointCheck 80 20 blocksGc80 67 40 10 970 (colourGc80.getD 67 []) = true := by
  decide +kernel

theorem gcPt_68 : gcPointCheck 80 20 blocksGc80 68 40 10 970 (colourGc80.getD 68 []) = true := by
  decide +kernel

theorem gcPt_69 : gcPointCheck 80 20 blocksGc80 69 40 10 970 (colourGc80.getD 69 []) = true := by
  decide +kernel

theorem gcPt_70 : gcPointCheck 80 20 blocksGc80 70 40 10 970 (colourGc80.getD 70 []) = true := by
  decide +kernel

theorem gcPt_71 : gcPointCheck 80 20 blocksGc80 71 40 10 970 (colourGc80.getD 71 []) = true := by
  decide +kernel

theorem gcPt_72 : gcPointCheck 80 20 blocksGc80 72 40 10 970 (colourGc80.getD 72 []) = true := by
  decide +kernel

theorem gcPt_73 : gcPointCheck 80 20 blocksGc80 73 40 10 970 (colourGc80.getD 73 []) = true := by
  decide +kernel

theorem gcPt_74 : gcPointCheck 80 20 blocksGc80 74 40 10 970 (colourGc80.getD 74 []) = true := by
  decide +kernel

theorem gcPt_75 : gcPointCheck 80 20 blocksGc80 75 40 10 970 (colourGc80.getD 75 []) = true := by
  decide +kernel

theorem gcPt_76 : gcPointCheck 80 20 blocksGc80 76 40 10 970 (colourGc80.getD 76 []) = true := by
  decide +kernel

theorem gcPt_77 : gcPointCheck 80 20 blocksGc80 77 40 10 970 (colourGc80.getD 77 []) = true := by
  decide +kernel

theorem gcPt_78 : gcPointCheck 80 20 blocksGc80 78 40 10 970 (colourGc80.getD 78 []) = true := by
  decide +kernel

theorem gcPt_79 : gcPointCheck 80 20 blocksGc80 79 40 10 970 (colourGc80.getD 79 []) = true := by
  decide +kernel

end Mcd.Kernel
