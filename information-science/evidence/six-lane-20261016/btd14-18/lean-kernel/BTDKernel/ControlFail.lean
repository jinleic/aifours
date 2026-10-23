import BTDKernel.Proof

/-!
# Negative control: this module MUST FAIL to compile

1. A mutated BTD(3,3;1,1,3;3,2) (entry (0,0) changed from 2 to 1) is claimed to satisfy `IsBTDgen`: `decide` must
   refute the row-count clause.
2. `bad_det4` is applied to `D = 729`, outside its hypothesis set (and `729 d^2 = 7^10 · 729` is solvable with
   `d = 7^5`): `norm_num` must fail on the side condition.
-/

namespace BTD14.ControlFail

def M3bad1 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![1, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem bad_claim_1 : BTD14.IsBTDgen 1 1 3 2 M3bad1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> decide

theorem bad_claim_2 : False :=
  BTD14.bad_det4 (7 ^ 5) 729 (by norm_num) (by norm_num)

end BTD14.ControlFail
