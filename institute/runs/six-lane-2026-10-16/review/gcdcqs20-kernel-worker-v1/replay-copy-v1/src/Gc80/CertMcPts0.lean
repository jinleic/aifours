import Gc80.DataMc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, mcDSQS(80), points 0-19

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes and 1027 triples, and every pair avoiding `x` lies in exactly one derived triple (`pointCheck`, no hole).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem mcPt_0 : pointCheck 80 blocksMc80 0 noHole 40 1027 (colourMc80.getD 0 []) = true := by
  decide +kernel

theorem mcPt_1 : pointCheck 80 blocksMc80 1 noHole 40 1027 (colourMc80.getD 1 []) = true := by
  decide +kernel

theorem mcPt_2 : pointCheck 80 blocksMc80 2 noHole 40 1027 (colourMc80.getD 2 []) = true := by
  decide +kernel

theorem mcPt_3 : pointCheck 80 blocksMc80 3 noHole 40 1027 (colourMc80.getD 3 []) = true := by
  decide +kernel

theorem mcPt_4 : pointCheck 80 blocksMc80 4 noHole 40 1027 (colourMc80.getD 4 []) = true := by
  decide +kernel

theorem mcPt_5 : pointCheck 80 blocksMc80 5 noHole 40 1027 (colourMc80.getD 5 []) = true := by
  decide +kernel

theorem mcPt_6 : pointCheck 80 blocksMc80 6 noHole 40 1027 (colourMc80.getD 6 []) = true := by
  decide +kernel

theorem mcPt_7 : pointCheck 80 blocksMc80 7 noHole 40 1027 (colourMc80.getD 7 []) = true := by
  decide +kernel

theorem mcPt_8 : pointCheck 80 blocksMc80 8 noHole 40 1027 (colourMc80.getD 8 []) = true := by
  decide +kernel

theorem mcPt_9 : pointCheck 80 blocksMc80 9 noHole 40 1027 (colourMc80.getD 9 []) = true := by
  decide +kernel

theorem mcPt_10 : pointCheck 80 blocksMc80 10 noHole 40 1027 (colourMc80.getD 10 []) = true := by
  decide +kernel

theorem mcPt_11 : pointCheck 80 blocksMc80 11 noHole 40 1027 (colourMc80.getD 11 []) = true := by
  decide +kernel

theorem mcPt_12 : pointCheck 80 blocksMc80 12 noHole 40 1027 (colourMc80.getD 12 []) = true := by
  decide +kernel

theorem mcPt_13 : pointCheck 80 blocksMc80 13 noHole 40 1027 (colourMc80.getD 13 []) = true := by
  decide +kernel

theorem mcPt_14 : pointCheck 80 blocksMc80 14 noHole 40 1027 (colourMc80.getD 14 []) = true := by
  decide +kernel

theorem mcPt_15 : pointCheck 80 blocksMc80 15 noHole 40 1027 (colourMc80.getD 15 []) = true := by
  decide +kernel

theorem mcPt_16 : pointCheck 80 blocksMc80 16 noHole 40 1027 (colourMc80.getD 16 []) = true := by
  decide +kernel

theorem mcPt_17 : pointCheck 80 blocksMc80 17 noHole 40 1027 (colourMc80.getD 17 []) = true := by
  decide +kernel

theorem mcPt_18 : pointCheck 80 blocksMc80 18 noHole 40 1027 (colourMc80.getD 18 []) = true := by
  decide +kernel

theorem mcPt_19 : pointCheck 80 blocksMc80 19 noHole 40 1027 (colourMc80.getD 19 []) = true := by
  decide +kernel

end Mcd.Kernel
