import BTDKernel.Proof

/-!
# Negative control: this module MUST FAIL to compile

Two false claims, each attempted with the same tactics used elsewhere; the build must report both errors and must
not produce an olean that the replay accepts.

1. A mutated BTD(3,3;1,1,3;3,2) (entry (0,0) changed from 2 to 1) is claimed to satisfy `IsBTDgen`: `decide` must
   refute the row-count clause.
2. `bad_det` is applied to `D = 100`, which is outside its hypothesis set (and `25 d^2 = 2^28 · 100` is solvable):
   `norm_num` must fail on the side condition.
-/

namespace BTD12.ControlFail

def M3bad1 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![1, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem bad_claim_1 : BTD12.IsBTDgen 1 1 3 2 M3bad1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> decide

theorem bad_claim_2 : False :=
  BTD12.bad_det (2 ^ 15) 100 (by norm_num) (by norm_num)

end BTD12.ControlFail
