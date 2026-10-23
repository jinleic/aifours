import Gc80.DataMc
import Gc80.Check80

/-!
# Kernel evaluations of the per-point checker, mcDSQS(80), points 40-59

One `decide +kernel` declaration per point (each a separate kernel check): the raw `POINT x` classes colour the derived design of the raw blocks at `x` with 40 classes and 1027 triples, and every pair avoiding `x` lies in exactly one derived triple (`pointCheck`, no hole).
No `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Mcd.Kernel

theorem mcPt_40 : pointCheck 80 blocksMc80 40 noHole 40 1027 (colourMc80.getD 40 []) = true := by
  decide +kernel

theorem mcPt_41 : pointCheck 80 blocksMc80 41 noHole 40 1027 (colourMc80.getD 41 []) = true := by
  decide +kernel

theorem mcPt_42 : pointCheck 80 blocksMc80 42 noHole 40 1027 (colourMc80.getD 42 []) = true := by
  decide +kernel

theorem mcPt_43 : pointCheck 80 blocksMc80 43 noHole 40 1027 (colourMc80.getD 43 []) = true := by
  decide +kernel

theorem mcPt_44 : pointCheck 80 blocksMc80 44 noHole 40 1027 (colourMc80.getD 44 []) = true := by
  decide +kernel

theorem mcPt_45 : pointCheck 80 blocksMc80 45 noHole 40 1027 (colourMc80.getD 45 []) = true := by
  decide +kernel

theorem mcPt_46 : pointCheck 80 blocksMc80 46 noHole 40 1027 (colourMc80.getD 46 []) = true := by
  decide +kernel

theorem mcPt_47 : pointCheck 80 blocksMc80 47 noHole 40 1027 (colourMc80.getD 47 []) = true := by
  decide +kernel

theorem mcPt_48 : pointCheck 80 blocksMc80 48 noHole 40 1027 (colourMc80.getD 48 []) = true := by
  decide +kernel

theorem mcPt_49 : pointCheck 80 blocksMc80 49 noHole 40 1027 (colourMc80.getD 49 []) = true := by
  decide +kernel

theorem mcPt_50 : pointCheck 80 blocksMc80 50 noHole 40 1027 (colourMc80.getD 50 []) = true := by
  decide +kernel

theorem mcPt_51 : pointCheck 80 blocksMc80 51 noHole 40 1027 (colourMc80.getD 51 []) = true := by
  decide +kernel

theorem mcPt_52 : pointCheck 80 blocksMc80 52 noHole 40 1027 (colourMc80.getD 52 []) = true := by
  decide +kernel

theorem mcPt_53 : pointCheck 80 blocksMc80 53 noHole 40 1027 (colourMc80.getD 53 []) = true := by
  decide +kernel

theorem mcPt_54 : pointCheck 80 blocksMc80 54 noHole 40 1027 (colourMc80.getD 54 []) = true := by
  decide +kernel

theorem mcPt_55 : pointCheck 80 blocksMc80 55 noHole 40 1027 (colourMc80.getD 55 []) = true := by
  decide +kernel

theorem mcPt_56 : pointCheck 80 blocksMc80 56 noHole 40 1027 (colourMc80.getD 56 []) = true := by
  decide +kernel

theorem mcPt_57 : pointCheck 80 blocksMc80 57 noHole 40 1027 (colourMc80.getD 57 []) = true := by
  decide +kernel

theorem mcPt_58 : pointCheck 80 blocksMc80 58 noHole 40 1027 (colourMc80.getD 58 []) = true := by
  decide +kernel

theorem mcPt_59 : pointCheck 80 blocksMc80 59 noHole 40 1027 (colourMc80.getD 59 []) = true := by
  decide +kernel

end Mcd.Kernel
