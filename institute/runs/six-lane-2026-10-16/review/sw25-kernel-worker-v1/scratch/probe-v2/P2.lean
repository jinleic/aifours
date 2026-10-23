/- Syntax probe 2 (toy, not the deliverable): flatMap/filter counts, negation inside `if`, Fin numerals. -/
namespace P2

def rows : List (List Int) := [[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]

def W : Fin 4 → Fin 4 → Int := fun i j => (rows.getD i.val []).getD j.val 0

def Wf : Fin 4 → Fin 4 → Int := fun i j =>
  (([[1, -1, 0, 0], [-1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]] : List (List Int)).getD i.val []).getD j.val 0

theorem eq_flip : ∀ i j : Fin 4,
    Wf i j = if (i.val = 0 ∧ j.val = 1) ∨ (i.val = 1 ∧ j.val = 0) then -W i j else W i j := by
  decide +kernel

theorem entry : W 0 1 = 1 ∧ W 1 0 = 1 ∧ Wf 0 1 = -1 ∧ Wf 1 0 = -1 := by decide +kernel

theorem viol :
    ((List.finRange 4).flatMap (fun i => (List.finRange 4).filter (fun j =>
      ((List.finRange 4).map (fun k => Wf i k * Wf j k)).sum != if i = j then 2 else 0))).length = 0 := by
  decide +kernel

end P2

#print axioms P2.eq_flip
#print axioms P2.viol
