import Gc80.DataMc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, mcDSQS(80), points 20-39

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes and 1027 triples, and every pair avoiding `x` lies in exactly one derived triple (`pointCheck`, no hole).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem mcPt_20 : pointCheck 80 blocksMc80 20 noHole 40 1027 (colourMc80.getD 20 []) = true := by
  decide +kernel

theorem mcPt_21 : pointCheck 80 blocksMc80 21 noHole 40 1027 (colourMc80.getD 21 []) = true := by
  decide +kernel

theorem mcPt_22 : pointCheck 80 blocksMc80 22 noHole 40 1027 (colourMc80.getD 22 []) = true := by
  decide +kernel

theorem mcPt_23 : pointCheck 80 blocksMc80 23 noHole 40 1027 (colourMc80.getD 23 []) = true := by
  decide +kernel

theorem mcPt_24 : pointCheck 80 blocksMc80 24 noHole 40 1027 (colourMc80.getD 24 []) = true := by
  decide +kernel

theorem mcPt_25 : pointCheck 80 blocksMc80 25 noHole 40 1027 (colourMc80.getD 25 []) = true := by
  decide +kernel

theorem mcPt_26 : pointCheck 80 blocksMc80 26 noHole 40 1027 (colourMc80.getD 26 []) = true := by
  decide +kernel

theorem mcPt_27 : pointCheck 80 blocksMc80 27 noHole 40 1027 (colourMc80.getD 27 []) = true := by
  decide +kernel

theorem mcPt_28 : pointCheck 80 blocksMc80 28 noHole 40 1027 (colourMc80.getD 28 []) = true := by
  decide +kernel

theorem mcPt_29 : pointCheck 80 blocksMc80 29 noHole 40 1027 (colourMc80.getD 29 []) = true := by
  decide +kernel

theorem mcPt_30 : pointCheck 80 blocksMc80 30 noHole 40 1027 (colourMc80.getD 30 []) = true := by
  decide +kernel

theorem mcPt_31 : pointCheck 80 blocksMc80 31 noHole 40 1027 (colourMc80.getD 31 []) = true := by
  decide +kernel

theorem mcPt_32 : pointCheck 80 blocksMc80 32 noHole 40 1027 (colourMc80.getD 32 []) = true := by
  decide +kernel

theorem mcPt_33 : pointCheck 80 blocksMc80 33 noHole 40 1027 (colourMc80.getD 33 []) = true := by
  decide +kernel

theorem mcPt_34 : pointCheck 80 blocksMc80 34 noHole 40 1027 (colourMc80.getD 34 []) = true := by
  decide +kernel

theorem mcPt_35 : pointCheck 80 blocksMc80 35 noHole 40 1027 (colourMc80.getD 35 []) = true := by
  decide +kernel

theorem mcPt_36 : pointCheck 80 blocksMc80 36 noHole 40 1027 (colourMc80.getD 36 []) = true := by
  decide +kernel

theorem mcPt_37 : pointCheck 80 blocksMc80 37 noHole 40 1027 (colourMc80.getD 37 []) = true := by
  decide +kernel

theorem mcPt_38 : pointCheck 80 blocksMc80 38 noHole 40 1027 (colourMc80.getD 38 []) = true := by
  decide +kernel

theorem mcPt_39 : pointCheck 80 blocksMc80 39 noHole 40 1027 (colourMc80.getD 39 []) = true := by
  decide +kernel

end Mcd.Kernel
