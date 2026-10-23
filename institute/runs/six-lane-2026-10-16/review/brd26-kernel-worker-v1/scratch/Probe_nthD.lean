import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true

def nthD : List Int → Nat → Int
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: l, n + 1 => nthD l n

def nthR : List (List Int) → Nat → List Int
  | [], _ => []
  | a :: _, 0 => a
  | _ :: l, n + 1 => nthR l n

def brdM2 (i : Fin 26) (j : Fin 130) : Int := nthD (nthR brd26Rows i.val) j.val

theorem rows2 : ∀ i, (Finset.univ.filter fun j => brdM2 i j ≠ 0).card = 25 := by
  decide +kernel

end Brd26.Probe
