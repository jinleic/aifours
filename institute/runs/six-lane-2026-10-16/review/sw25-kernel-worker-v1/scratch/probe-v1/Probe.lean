/- Syntax/cost probe on a toy symmetric weighing matrix W(4,2) (not the deliverable). -/
namespace Probe

def rows : List (List Int) := [[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]

def W : Fin 4 → Fin 4 → Int := fun i j => (rows.getD i.val []).getD j.val 0

theorem finRange_vals : (List.finRange 4).map Fin.val = List.range 4 := by decide +kernel

theorem W_table :
    (List.finRange 4).map (fun i => (List.finRange 4).map (fun j => W i j)) = rows := by
  decide +kernel

theorem W_entries : ∀ i j : Fin 4, W i j = -1 ∨ W i j = 0 ∨ W i j = 1 := by decide +kernel

theorem W_symm : ∀ i j : Fin 4, W i j = W j i := by decide +kernel

theorem W_gram : ∀ i j : Fin 4,
    ((List.finRange 4).map (fun k => W i k * W j k)).sum = if i = j then 2 else 0 := by
  decide +kernel

theorem W_rowWeight : ∀ i : Fin 4, ((List.finRange 4).filter (fun k => W i k != 0)).length = 2 := by
  decide +kernel

theorem exists_swm :
    ∃ W : Fin 4 → Fin 4 → Int,
      (∀ i j : Fin 4, W i j = -1 ∨ W i j = 0 ∨ W i j = 1) ∧
      (∀ i j : Fin 4, W i j = W j i) ∧
      (∀ i j : Fin 4,
        ((List.finRange 4).map (fun k => W i k * W j k)).sum = if i = j then 2 else 0) :=
  ⟨W, W_entries, W_symm, W_gram⟩

def Wf : Fin 4 → Fin 4 → Int := fun i j =>
  if (i.val = 0 ∧ j.val = 2) ∨ (i.val = 2 ∧ j.val = 0) then 1 else W i j

theorem not_Wf_gram : ¬ ∀ i j : Fin 4,
    ((List.finRange 4).map (fun k => Wf i k * Wf j k)).sum = if i = j then 2 else 0 := by
  decide +kernel

theorem Wf_pair : ((List.finRange 4).map (fun k => Wf 0 k * Wf 2 k)).sum = 2 := by decide +kernel

theorem fin25 : (List.finRange 25).length = 25 ∧ (24 : Fin 25).val = 24 ∧ (0 : Fin 25) ≠ 2 := by
  decide +kernel

end Probe

#print Probe.exists_swm
#print axioms Probe.exists_swm
#print axioms Probe.not_Wf_gram
#print axioms Probe.W_table
#print axioms Probe.fin25
