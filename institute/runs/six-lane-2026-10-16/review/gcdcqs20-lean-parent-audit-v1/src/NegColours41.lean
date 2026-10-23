import ParentAudit

/-! Parent negative control: MUST FAIL with a type mismatch (40 colour classes changed to 41). -/
open ParentGc80Audit in
theorem parent_negative : ∃ A : Finset (Finset (Fin 80)),
    (((∀ G ∈ pGroups, G.Nonempty) ∧
        (∀ G ∈ pGroups, ∀ G' ∈ pGroups, G ≠ G' → Disjoint G G') ∧
        ∀ x : Fin 80, ∃ G ∈ pGroups, x ∈ G) ∧
      (∀ X ∈ A, X.card = 4) ∧
      (∀ T : Finset (Fin 80), T.card = 3 → (∀ G ∈ pGroups, ¬ T ⊆ G) → ∃! X, X ∈ A ∧ T ⊆ X) ∧
      ∀ T : Finset (Fin 80), T.card = 3 → ∀ G ∈ pGroups, T ⊆ G → ∀ X ∈ A, ¬ T ⊆ X) ∧
    A.card = 19400 ∧
    ∀ x : Fin 80, ((A.filter fun X => x ∈ X).image fun X => X.erase x).card = 970 ∧
      ((pGroup (x.val / 20)).erase x ⊆ Finset.univ.erase x ∧
        (∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x),
          T.card = 3 ∧ T ⊆ Finset.univ.erase x) ∧
        (∀ P : Finset (Fin 80), P.card = 2 → P ⊆ Finset.univ.erase x →
          ¬ P ⊆ (pGroup (x.val / 20)).erase x →
          ∃! T, T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧ P ⊆ T) ∧
        ∀ P : Finset (Fin 80), P.card = 2 → P ⊆ (pGroup (x.val / 20)).erase x →
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ¬ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ Q ∈ C, Q.Nonempty ∧ Q ⊆ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! Q, Q ∈ C ∧ T ∈ Q) ∧
        C.card = 41 ∧
        (C.filter fun Q => ∀ T ∈ Q, Disjoint T ((pGroup (x.val / 20)).erase x)).card = 10 := by
  have h := ParentGc80Audit.gc80
  unfold ParentGc80Audit.GcStatement at h
  exact h
