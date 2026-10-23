import Gc80.Audit80

/-! Parent-authored binding audit for the GcdcqsKernel development (not written by that worker).

* `pGroup i` is defined independently by integer division (`y / 20 = i`), not by the worker's interval form; the
  kernel-checked equalities below identify it with `Mcd.grp80` and the four groups with `Mcd.groups80`.
* `GcStatement` is Tan–Zhou's gcDCQS(20^4 : 0) with empty stem, written with Mathlib notions only: a CQS(20^4 : 0)
  on `Fin 80` (4-subsets; every 3-subset meeting two groups in exactly one block; no 3-subset of a group in any
  block) whose derived design at every point x is an incomplete STS on `Fin 80 \ {x}` with hole `G(x) \ {x}` and
  has a colouring with 40 classes, exactly 10 of which avoid the hole.
* `chi79` binds 40 = χ′(79) (least number of classes of any colouring of any STS(79) on `Fin 79`), so
  r = χ′(79) = 40 and s = χ′(79) - (79 - 19)/2 = 10, as in Tan–Zhou's definition.
* `McStatement` is the mcDSQS(80) statement with r = χ′(79). -/

namespace ParentGc80Audit

def pGroup (i : ℕ) : Finset (Fin 80) := Finset.univ.filter fun y => y.val / 20 = i

def pGroups : Finset (Finset (Fin 80)) := {pGroup 0, pGroup 1, pGroup 2, pGroup 3}

theorem pGroup_eq (i : ℕ) (_hi : i < 4) : pGroup i = Mcd.grp80 i := by
  ext y
  simp only [pGroup, Mcd.grp80, Finset.mem_filter, Finset.mem_univ, true_and]
  omega

theorem pGroups_eq : pGroups = Mcd.groups80 := by
  simp only [pGroups, Mcd.groups80, pGroup_eq 0 (by decide), pGroup_eq 1 (by decide),
    pGroup_eq 2 (by decide), pGroup_eq 3 (by decide)]

theorem hole_eq (x : Fin 80) : Mcd.grp80 (x.val / 20) = pGroup (x.val / 20) :=
  (pGroup_eq _ (by omega)).symm

noncomputable def ChiPrime79 : ℕ :=
  sInf {r : ℕ | ∃ S : Finset (Finset (Fin 79)),
    ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 79), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
    ∃ C : Finset (Finset (Finset (Fin 79))),
      ((∀ Q ∈ C, Q.Nonempty ∧ Q ⊆ S ∧ ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
        ∀ T ∈ S, ∃! Q, Q ∈ C ∧ T ∈ Q) ∧ C.card = r}

theorem chi79 : ChiPrime79 = 40 := Mcd.Audit.root_chi79_unfolded

def GcStatement : Prop :=
  ∃ A : Finset (Finset (Fin 80)),
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
        C.card = 40 ∧
        (C.filter fun Q => ∀ T ∈ Q, Disjoint T ((pGroup (x.val / 20)).erase x)).card = 10

theorem gc80 : GcStatement := by
  have h := Mcd.Audit.root_gc80_unfolded
  rw [← pGroups_eq] at h
  simp only [hole_eq] at h
  exact h

theorem gc80_parameters : ChiPrime79 = 40 ∧ ChiPrime79 - (79 - 19) / 2 = 10 := by
  refine ⟨chi79, ?_⟩
  rw [chi79]

def McStatement : Prop :=
  ∃ B : Finset (Finset (Fin 80)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 80), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 80, ∃ C : Finset (Finset (Finset (Fin 80))),
        ((∀ Q ∈ C, Q.Nonempty ∧ Q ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! Q, Q ∈ C ∧ T ∈ Q) ∧
        C.card = ChiPrime79

theorem mc80 : McStatement := Mcd.Audit.root_mc80_unfolded

end ParentGc80Audit

#print axioms ParentGc80Audit.pGroups_eq
#print axioms ParentGc80Audit.chi79
#print axioms ParentGc80Audit.gc80
#print axioms ParentGc80Audit.gc80_parameters
#print axioms ParentGc80Audit.mc80
