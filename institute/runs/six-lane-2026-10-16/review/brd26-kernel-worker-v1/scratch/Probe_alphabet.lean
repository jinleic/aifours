import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

theorem t : ∀ i j, brdM i j = -1 ∨ brdM i j = 0 ∨ brdM i j = 1 := by
  decide +kernel

end Brd26.Probe
