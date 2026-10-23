import BTDKernel.Proof

/-!
# Controls (positive)

* The definition `IsBTDgen` accepts BTD(3,3;1,1,3;3,2) with rows `(2,0,1), (1,2,0), (0,1,2)` (the calibration
  control named in the contract) and rejects two mutations of it (an entry changed; two entries swapped within a
  row).
* `square_case`: `729 d^2 = 7^10 D` is solvable for `D = 729` (`d = 7^5`), so `bad_det4` genuinely depends on its
  value hypothesis (`ControlFail` shows it cannot be applied there).
* `det4_value_1`, `det4_value_10`: `det4_pattern` reproduces the two values of the r1 determinant table on explicit
  instances (`x = -8, y = 1, w = 1` gives `3645`; `w = 10` gives `-2187`).
-/

namespace BTD14.Controls

/-- BTD(3,3;1,1,3;3,2), rows (2,0,1), (1,2,0), (0,1,2) -/
def M3 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![2, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem M3_is_btd : BTD14.IsBTDgen 1 1 3 2 M3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro i j
    fin_cases i <;> fin_cases j <;> simp [M3]
  · decide
  · decide
  · decide
  · decide

/-- entry (0,0) changed from 2 to 1 -/
def M3bad1 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![1, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem M3bad1_not_btd : ¬ BTD14.IsBTDgen 1 1 3 2 M3bad1 := by
  intro h
  have := h.2.2.1 0
  revert this
  decide

/-- row 0 entries (0,1) and (0,2) swapped: rows keep their composition, a column sum breaks -/
def M3bad2 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![2, 1, 0], ![1, 2, 0], ![0, 1, 2]]

theorem M3bad2_not_btd : ¬ BTD14.IsBTDgen 1 1 3 2 M3bad2 := by
  intro h
  have := h.2.2.2.1 1
  revert this
  decide

theorem square_case : 729 * (7 ^ 5 : ℤ) ^ 2 = 7 ^ 10 * 729 := by norm_num

theorem det4_value_1 :
    (Matrix.of ![![(10 : ℤ), -8, 1, -8], ![-8, 10, 1, 1], ![1, 1, 10, 1], ![-8, 1, 1, 28]]).det = 3645 := by
  rw [BTD14.det4_pattern]
  norm_num

theorem det4_value_10 :
    (Matrix.of ![![(10 : ℤ), -8, 1, -8], ![-8, 10, 1, 1], ![1, 1, 10, 10], ![-8, 1, 10, 28]]).det = -2187 := by
  rw [BTD14.det4_pattern]
  norm_num

end BTD14.Controls

#print axioms BTD14.Controls.M3_is_btd
#print axioms BTD14.Controls.M3bad1_not_btd
#print axioms BTD14.Controls.M3bad2_not_btd
#print axioms BTD14.Controls.det4_value_1
#print axioms BTD14.Controls.det4_value_10
