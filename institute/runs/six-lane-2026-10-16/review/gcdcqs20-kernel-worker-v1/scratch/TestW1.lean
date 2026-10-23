import Gc80.DataGc
import Gc80.DataMc
import Gc80.Check80

namespace Mcd.Kernel

theorem tw_gc0 : gcPointCheck 80 20 blocksGc80 0 40 10 970 (colourGc80.getD 0 []) = true := by
  decide +kernel

theorem tw_mc40 : pointCheck 80 blocksMc80 40 noHole 40 1027 (colourMc80.getD 40 []) = true := by
  decide +kernel

theorem tw_card : (grp80 3).card = 20 := by
  decide +kernel

end Mcd.Kernel
