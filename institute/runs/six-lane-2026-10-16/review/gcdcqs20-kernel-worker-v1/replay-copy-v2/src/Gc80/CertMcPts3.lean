import Gc80.DataMc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, mcDSQS(80), points 60-79

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes and 1027 triples, and every pair avoiding `x` lies in exactly one derived triple (`pointCheck`, no hole).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem mcPt_60 : pointCheck 80 blocksMc80 60 noHole 40 1027 (colourMc80.getD 60 []) = true := by
  decide +kernel

theorem mcPt_61 : pointCheck 80 blocksMc80 61 noHole 40 1027 (colourMc80.getD 61 []) = true := by
  decide +kernel

theorem mcPt_62 : pointCheck 80 blocksMc80 62 noHole 40 1027 (colourMc80.getD 62 []) = true := by
  decide +kernel

theorem mcPt_63 : pointCheck 80 blocksMc80 63 noHole 40 1027 (colourMc80.getD 63 []) = true := by
  decide +kernel

theorem mcPt_64 : pointCheck 80 blocksMc80 64 noHole 40 1027 (colourMc80.getD 64 []) = true := by
  decide +kernel

theorem mcPt_65 : pointCheck 80 blocksMc80 65 noHole 40 1027 (colourMc80.getD 65 []) = true := by
  decide +kernel

theorem mcPt_66 : pointCheck 80 blocksMc80 66 noHole 40 1027 (colourMc80.getD 66 []) = true := by
  decide +kernel

theorem mcPt_67 : pointCheck 80 blocksMc80 67 noHole 40 1027 (colourMc80.getD 67 []) = true := by
  decide +kernel

theorem mcPt_68 : pointCheck 80 blocksMc80 68 noHole 40 1027 (colourMc80.getD 68 []) = true := by
  decide +kernel

theorem mcPt_69 : pointCheck 80 blocksMc80 69 noHole 40 1027 (colourMc80.getD 69 []) = true := by
  decide +kernel

theorem mcPt_70 : pointCheck 80 blocksMc80 70 noHole 40 1027 (colourMc80.getD 70 []) = true := by
  decide +kernel

theorem mcPt_71 : pointCheck 80 blocksMc80 71 noHole 40 1027 (colourMc80.getD 71 []) = true := by
  decide +kernel

theorem mcPt_72 : pointCheck 80 blocksMc80 72 noHole 40 1027 (colourMc80.getD 72 []) = true := by
  decide +kernel

theorem mcPt_73 : pointCheck 80 blocksMc80 73 noHole 40 1027 (colourMc80.getD 73 []) = true := by
  decide +kernel

theorem mcPt_74 : pointCheck 80 blocksMc80 74 noHole 40 1027 (colourMc80.getD 74 []) = true := by
  decide +kernel

theorem mcPt_75 : pointCheck 80 blocksMc80 75 noHole 40 1027 (colourMc80.getD 75 []) = true := by
  decide +kernel

theorem mcPt_76 : pointCheck 80 blocksMc80 76 noHole 40 1027 (colourMc80.getD 76 []) = true := by
  decide +kernel

theorem mcPt_77 : pointCheck 80 blocksMc80 77 noHole 40 1027 (colourMc80.getD 77 []) = true := by
  decide +kernel

theorem mcPt_78 : pointCheck 80 blocksMc80 78 noHole 40 1027 (colourMc80.getD 78 []) = true := by
  decide +kernel

theorem mcPt_79 : pointCheck 80 blocksMc80 79 noHole 40 1027 (colourMc80.getD 79 []) = true := by
  decide +kernel

end Mcd.Kernel
