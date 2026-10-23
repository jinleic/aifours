import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true

theorem pr0 : ∀ i' : Fin 26, (0 : Fin 26) ≠ i' →
    (Finset.univ.filter fun j => brdM 0 j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM 0 j * brdM i' j = -1).card = 2 := by
  decide +kernel

theorem pr1 : ∀ i' : Fin 26, (1 : Fin 26) ≠ i' →
    (Finset.univ.filter fun j => brdM 1 j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM 1 j * brdM i' j = -1).card = 2 := by
  decide +kernel

theorem pr2 : ∀ i' : Fin 26, (2 : Fin 26) ≠ i' →
    (Finset.univ.filter fun j => brdM 2 j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM 2 j * brdM i' j = -1).card = 2 := by
  decide +kernel

theorem pr3 : ∀ i' : Fin 26, (3 : Fin 26) ≠ i' →
    (Finset.univ.filter fun j => brdM 3 j * brdM i' j = 1).card = 2 ∧
    (Finset.univ.filter fun j => brdM 3 j * brdM i' j = -1).card = 2 := by
  decide +kernel

end Brd26.Probe
