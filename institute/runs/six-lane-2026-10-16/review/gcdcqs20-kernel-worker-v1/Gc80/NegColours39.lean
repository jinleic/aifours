import Gc80.Audit80

/-!
# Negative control NegColours39 (this module must FAIL to build)

The two statements are the unfolded roots `Mcd.Audit.root_gc80_unfolded` and
`Mcd.Audit.root_mc80_unfolded`, restated verbatim and proved by those roots.  Each negative
control `Gc80/Neg*.lean` is this file with exactly one textual mutation of one statement (the
replay driver re-applies the mutation to this file and compares bytes), so a failure of a
negative control is caused by its mutation of the mathematical statement.
-/

namespace Mcd.Twin

theorem twin_gc80 : ∃ A : Finset (Finset (Fin 80)),
    (((∀ G ∈ Mcd.groups80, G.Nonempty) ∧
        (∀ G ∈ Mcd.groups80, ∀ G' ∈ Mcd.groups80, G ≠ G' → Disjoint G G') ∧
        ∀ x : Fin 80, ∃ G ∈ Mcd.groups80, x ∈ G) ∧
      (∀ X ∈ A, X.card = 4) ∧
      (∀ T : Finset (Fin 80), T.card = 3 → (∀ G ∈ Mcd.groups80, ¬ T ⊆ G) →
        ∃! X, X ∈ A ∧ T ⊆ X) ∧
      ∀ T : Finset (Fin 80), T.card = 3 → ∀ G ∈ Mcd.groups80, T ⊆ G → ∀ X ∈ A, ¬ T ⊆ X) ∧
    A.card = 19400 ∧
    ∀ x : Fin 80, ((A.filter fun X => x ∈ X).image fun X => X.erase x).card = 970 ∧
      ((Mcd.grp80 (x.val / 20)).erase x ⊆ Finset.univ.erase x ∧
        (∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x),
          T.card = 3 ∧ T ⊆ Finset.univ.erase x) ∧
        (∀ P : Finset (Fin 80), P.card = 2 → P ⊆ Finset.univ.erase x →
          ¬ P ⊆ (Mcd.grp80 (x.val / 20)).erase x →
          ∃! T, T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧ P ⊆ T) ∧
        ∀ P : Finset (Fin 80), P.card = 2 → P ⊆ (Mcd.grp80 (x.val / 20)).erase x →
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ¬ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (A.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (A.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = 39 ∧
        (C.filter fun P => ∀ T ∈ P, Disjoint T ((Mcd.grp80 (x.val / 20)).erase x)).card = 10 :=
  Mcd.Audit.root_gc80_unfolded

theorem twin_mc80 : ∃ B : Finset (Finset (Fin 80)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 80), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 80, ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = sInf {r : ℕ | ∃ S : Finset (Finset (Fin 79)),
          ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 79), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
          ∃ C' : Finset (Finset (Finset (Fin 79))),
            ((∀ P ∈ C', P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
              ∀ T ∈ S, ∃! P, P ∈ C' ∧ T ∈ P) ∧ C'.card = r} :=
  Mcd.Audit.root_mc80_unfolded

end Mcd.Twin

#print axioms Mcd.Twin.twin_gc80
#print axioms Mcd.Twin.twin_mc80
