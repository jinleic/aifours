import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

theorem t : ∀ i, (Finset.univ.filter fun j => brdM i j ≠ 0).card = 25 := by
  decide +kernel

end Brd26.Probe
