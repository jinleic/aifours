import Brd26.Data

/-!
# The explicit witness matrix `Brd26.brdM`

`brdM i j` is entry `j` of raw row `i` of `brd26Rows` (Brd26.Data), i.e. the `(j + 1)`-th token of raw
line `i + 2` of `review/brd26-parent-inputs-v1/brd26-130-witness-v1.brd` (SHA-256
`eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe`).  The kernel evaluations
`brd26Rows_shape` (26 rows, each of length 130) show that the `getD` default value `0` is never used
for an index in `Fin 26 × Fin 130`, and `brd26Header_eq` that the raw header numbers are
`26 130 25 5 4`.  No native code, no `native_decide`, no `Lean.ofReduceBool`.
-/

namespace Brd26

/-- The explicit 26 × 130 witness matrix: entry `(i, j)` is entry `j` of raw row `i`. -/
def brdM (i : Fin 26) (j : Fin 130) : Int := (brd26Rows.getD i.val []).getD j.val 0

/-- Kernel evaluation: the raw header numbers are `26 130 25 5 4`. -/
theorem brd26Header_eq : brd26Header = [26, 130, 25, 5, 4] := by
  decide +kernel

/-- Kernel evaluation: the raw data has 26 rows, each with 130 entries. -/
theorem brd26Rows_shape : brd26Rows.length = 26 ∧ ∀ row ∈ brd26Rows, row.length = 130 := by
  decide +kernel

/-- Every entry of `brdM` is the corresponding raw entry (`getElem` with the bounds of
`brd26Rows_shape`); the `getD` defaults are never used. -/
theorem brdM_eq_raw (i : Fin 26) (j : Fin 130) :
    ∃ (hi : i.val < brd26Rows.length) (hj : j.val < brd26Rows[i.val].length),
      brdM i j = brd26Rows[i.val][j.val] := by
  have hi : i.val < brd26Rows.length := by
    rw [brd26Rows_shape.1]
    exact i.isLt
  have hj : j.val < brd26Rows[i.val].length := by
    rw [brd26Rows_shape.2 _ (List.getElem_mem hi)]
    exact j.isLt
  refine ⟨hi, hj, ?_⟩
  simp only [brdM, List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi,
    List.getElem?_eq_getElem hj, Option.getD_some]

end Brd26
