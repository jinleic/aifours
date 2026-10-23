import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true
set_option profiler.threshold 10

theorem a1 : ∀ i : Fin 26, i = i := by
  decide +kernel

theorem a2 : (Finset.univ.filter fun j => brdM 0 j ≠ 0).card = 25 := by
  decide +kernel

theorem a3 : ∀ i : Fin 26, brdM i 0 = brdM i 0 := by
  decide +kernel

theorem a4 : ∀ i : Fin 3, (Finset.univ.filter fun j => brdM i j ≠ 0).card = 25 := by
  decide +kernel

theorem a5 : (Finset.univ.filter fun j => brdM 0 j ≠ 0).card = 25 ∧ (Finset.univ.filter fun j => brdM 1 j ≠ 0).card = 25 := by
  decide +kernel

theorem a6 : ((brd26Rows.getD 0 []).filter fun x => x ≠ 0).length = 25 := by
  decide +kernel

end Brd26.Probe
