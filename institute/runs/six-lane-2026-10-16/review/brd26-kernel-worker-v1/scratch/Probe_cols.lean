import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

theorem t : ∀ j, (Finset.univ.filter fun i => brdM i j ≠ 0).card = 5 := by
  decide +kernel

end Brd26.Probe
