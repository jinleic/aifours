import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true in
theorem t0 : brdM 0 0 = -1 := by
  decide +kernel

set_option profiler true in
theorem t1 : ∀ i, (Finset.univ.filter fun j => brdM i j ≠ 0).card = 25 := by
  decide +kernel

end Brd26.Probe
