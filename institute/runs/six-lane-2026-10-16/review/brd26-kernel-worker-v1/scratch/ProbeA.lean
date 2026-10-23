import Brd26.Target
import Brd26.Witness

namespace Brd26.ProbeA

theorem alphabet : ∀ i j, brdM i j = -1 ∨ brdM i j = 0 ∨ brdM i j = 1 := by
  decide +kernel

theorem rows : ∀ i, (Finset.univ.filter fun j => brdM i j ≠ 0).card = 25 := by
  decide +kernel

theorem cols : ∀ j, (Finset.univ.filter fun i => brdM i j ≠ 0).card = 5 := by
  decide +kernel

end Brd26.ProbeA
