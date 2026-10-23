import Brd26.Target
import Brd26.Witness

namespace Brd26.Probe

set_option profiler true
set_option profiler.threshold 10

def nthD : List Int → Nat → Int
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: l, n + 1 => nthD l n

-- index lookups on Nat via List.range, rows 0..25: getD
theorem idx1 : (List.range 26).all (fun i => (List.range 130).all (fun j => (brd26Rows.getD i []).getD j 0 != 5)) = true := by
  decide +kernel

-- same via nthD
theorem idx2 : (List.range 26).all (fun i => (List.range 130).all (fun j => nthD (brd26Rows.getD i []) j != 5)) = true := by
  decide +kernel

-- Fin-indexed, via List.finRange without Finset
theorem idx3 : (List.finRange 26).all (fun i => (List.finRange 130).all (fun j => brdM i j != 5)) = true := by
  decide +kernel

-- Finset forall with trivial body
theorem idx4 : ∀ i : Fin 26, ∀ j : Fin 130, brdM i j ≠ 5 := by
  decide +kernel

end Brd26.Probe
