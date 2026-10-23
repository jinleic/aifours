import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true

theorem pairsAll : ∀ i i' : Fin 26, i ≠ i' →
    (Finset.univ.filter fun j => brdM i j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM i j * brdM i' j = -1).card = 2 := by
  decide +kernel

end Brd26.Probe
