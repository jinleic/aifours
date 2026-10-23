import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

theorem t : ∀ i', (0 : Fin 26) ≠ i' →
    (Finset.univ.filter fun j => brdM 0 j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM 0 j * brdM i' j = -1).card = 2 := by
  decide +kernel

end Brd26.Probe
