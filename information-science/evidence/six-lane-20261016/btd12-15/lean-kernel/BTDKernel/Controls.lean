import BTDKernel.Proof

/-!
# Controls (positive)

* The definition `IsBTDgen` accepts the published BTD(3,3;1,1,3;3,2) with rows `(2,0,1), (1,2,0), (0,1,2)` (contract
  control) and rejects two mutations of it (an entry changed, two entries swapped within a row).
* The closing arithmetic: `bad_det` covers exactly the four determinant values of Step 8 and Step 7; an actual
  square multiple (`D = 100`, `d = 2^15`) is a solution of `25 d^2 = 2^28 D`.
-/

namespace BTD12.Controls

/-- BTD(3,3;1,1,3;3,2), rows (2,0,1), (1,2,0), (0,1,2) -/
def M3 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![2, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem M3_is_btd : BTD12.IsBTDgen 1 1 3 2 M3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro i j
    fin_cases i <;> fin_cases j <;> simp [M3]
  · decide
  · decide
  · decide
  · decide
/-- entry (0,0) changed from 2 to 1 -/
def M3bad1 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![1, 0, 1], ![1, 2, 0], ![0, 1, 2]]

theorem M3bad1_not_btd : ¬ BTD12.IsBTDgen 1 1 3 2 M3bad1 := by
  intro h
  have := h.2.2.1 0
  revert this
  decide

/-- row 0 entries (0,1) and (0,2) swapped: rows keep their composition, a column sum breaks -/
def M3bad2 : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of ![![2, 1, 0], ![1, 2, 0], ![0, 1, 2]]

theorem M3bad2_not_btd : ¬ BTD12.IsBTDgen 1 1 3 2 M3bad2 := by
  intro h
  have := h.2.2.2.1 1
  revert this
  decide

/-- `25 d^2 = 2^28 D` is solvable for `D = 100` (so `bad_det` is not vacuous in form) -/
theorem square_case : 25 * (2 ^ 15 : ℤ) ^ 2 = 2 ^ 28 * 100 := by norm_num

end BTD12.Controls

#print axioms BTD12.Controls.M3_is_btd
#print axioms BTD12.Controls.M3bad1_not_btd
#print axioms BTD12.Controls.M3bad2_not_btd
