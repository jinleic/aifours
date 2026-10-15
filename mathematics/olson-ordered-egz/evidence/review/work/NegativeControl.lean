import Mathlib

/- This file must FAIL: adding the missing identity to r^5 s^5 produces
   r^3 s^2 1 as a six-term ordered identity product in D_6. -/
namespace OlsonNegativeControl
open DihedralGroup

def extendedWord : List (DihedralGroup 3) :=
  List.replicate 5 (r 1) ++ List.replicate 5 (sr 0) ++ [1]

example : ((extendedWord.sublistsLen 6).all fun ys => decide (ys.prod ≠ 1)) = true := by
  decide

end OlsonNegativeControl
