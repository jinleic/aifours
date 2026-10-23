import McdKernel.Cert38

/-! Parent-authored targets using only Mathlib notions.  `ColourCounts n` is the set of numbers
of colour classes of colourings of Steiner triple systems on `Fin n`: every block is a 3-set,
every pair lies in exactly one block, and the colour classes are nonempty sets of pairwise
disjoint blocks with every block in exactly one class.  `Statement` says an SQS(38) exists whose
derived design at EVERY point has a colouring with exactly `sInf (ColourCounts 37)` classes. -/
namespace ParentMcdAudit

def ColourCounts (n : ℕ) : Set ℕ :=
  {r | ∃ S : Finset (Finset (Fin n)),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin n), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin n))),
        ((∀ Q ∈ C, Q.Nonempty ∧ Q ⊆ S ∧ ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! Q, Q ∈ C ∧ T ∈ Q) ∧ C.card = r}

theorem chi37 : sInf (ColourCounts 37) = 19 := Mcd.Kernel.chiPrime_37

def Statement : Prop :=
  ∃ B : Finset (Finset (Fin 38)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 38), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
    ∀ x : Fin 38, ∃ C : Finset (Finset (Finset (Fin 38))),
      ((∀ Q ∈ C, Q.Nonempty ∧ (∀ T ∈ Q, ∃ X ∈ B, x ∈ X ∧ T = X.erase x) ∧
          ∀ T ∈ Q, ∀ T' ∈ Q, T ≠ T' → Disjoint T T') ∧
        ∀ X ∈ B, x ∈ X → ∃! Q, Q ∈ C ∧ X.erase x ∈ Q) ∧
      C.card = sInf (ColourCounts 37)

theorem mcdsqs38 : Statement := by
  obtain ⟨B, hB, hcol⟩ := Mcd.Kernel.exists_mcdsqs38
  refine ⟨B, hB, fun x => ?_⟩
  obtain ⟨C, ⟨hppc, huniq⟩, hcard⟩ := hcol x
  refine ⟨C, ⟨fun Q hQ => ?_, fun X hX hxX => huniq _ ?_⟩, ?_⟩
  · obtain ⟨hne, hsub, hdisj⟩ := hppc Q hQ
    refine ⟨hne, fun T hT => ?_, hdisj⟩
    obtain ⟨X, hXf, hXT⟩ := Finset.mem_image.mp (hsub hT)
    exact ⟨X, (Finset.mem_filter.mp hXf).1, (Finset.mem_filter.mp hXf).2, hXT.symm⟩
  · exact Finset.mem_image.mpr ⟨X, Finset.mem_filter.mpr ⟨hX, hxX⟩, rfl⟩
  · calc C.card = Mcd.chiPrime (38 - 1) := hcard
      _ = 19 := Mcd.Kernel.chiPrime_37
      _ = sInf (ColourCounts 37) := chi37.symm

end ParentMcdAudit

#print axioms ParentMcdAudit.chi37
#print axioms ParentMcdAudit.mcdsqs38
