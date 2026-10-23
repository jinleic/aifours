/- Expected-failure probe (toy): shows the error format of `decide +kernel` on a false proposition. -/
namespace ProbeFail

def rows : List (List Int) := [[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]

def W : Fin 4 → Fin 4 → Int := fun i j => (rows.getD i.val []).getD j.val 0

theorem W_gram_bad : ∀ i j : Fin 4,
    ((List.finRange 4).map (fun k => W i k * W j k)).sum = if i = j then 3 else 0 := by
  decide +kernel

end ProbeFail
