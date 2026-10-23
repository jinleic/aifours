import McdKernel.Target
import McdKernel.Cert38

/-!
# Audit: the mcDSQS(38) roots prove the data-independent targets

`Mcd.TargetColoured`, `Mcd.ColourLowerBound`, `Mcd.chiPrime`, `Mcd.TargetMc` and their vocabulary
are defined in `McdKernel.Target`, which imports no proof and no data.  The theorems below
restate the roots with exactly the target types, and in unfolded form with Mathlib notions
only.  `witness38` names the explicit objects: the raw block lines and, at every point, the
classes of the raw `POINT x` section.
-/

namespace Mcd.Audit

universe u

/-- Root (1): an SQS on `Fin 38` whose derived design at every point has a 19-colouring. -/
theorem root38_coloured : Mcd.TargetColoured 38 19 := Mcd.Kernel.coloured38

/-- Root (2), data-independent: every colouring of every STS on every 37-element type has at
least 19 colour classes. -/
theorem root37_lower : Mcd.ColourLowerBound.{u} 37 19 := Mcd.Counts.colourLowerBound_37

/-- Root (2): `χ′(37) = 19`. -/
theorem root37_chi : Mcd.chiPrime 37 = 19 := Mcd.Kernel.chiPrime_37

/-- Root (2): an mcDSQS(38) exists on `Fin 38`. -/
theorem root38_mc : Mcd.TargetMc 38 := Mcd.Kernel.exists_mcdsqs38

/-- The explicit witness. -/
theorem witness38 : Mcd.IsMcDSQS Mcd.Kernel.mcdsqs38 ∧
    ∀ x : Fin 38, Mcd.IsColouring (Mcd.derivedBlocks Mcd.Kernel.mcdsqs38 x)
      (Mcd.Kernel.colouring38 x) ∧ (Mcd.Kernel.colouring38 x).card = 19 :=
  ⟨Mcd.Kernel.isMcDSQS_mcdsqs38, Mcd.Kernel.colouring38_spec⟩

/-- Root (1), unfolded. -/
theorem root38_coloured_unfolded : ∃ B : Finset (Finset (Fin 38)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 38), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 38, ∃ C : Finset (Finset (Finset (Fin 38))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = 19 :=
  Mcd.Kernel.coloured38

/-- Root (2), the lower bound, unfolded. -/
theorem root37_lower_unfolded : ∀ (W : Type u) [Fintype W] [DecidableEq W],
    Fintype.card W = 37 → ∀ S : Finset (Finset W),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset W, P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) →
      ∀ C : Finset (Finset (Finset W)),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! P, P ∈ C ∧ T ∈ P) → 19 ≤ C.card :=
  Mcd.Counts.colourLowerBound_37

/-- Root (2), `χ′(37) = 19`, unfolded. -/
theorem root37_chi_unfolded :
    sInf {r : ℕ | ∃ S : Finset (Finset (Fin 37)),
      ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 37), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
      ∃ C : Finset (Finset (Finset (Fin 37))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ S, ∃! P, P ∈ C ∧ T ∈ P) ∧ C.card = r} = 19 :=
  Mcd.Kernel.chiPrime_37

/-- Root (2), the faithful mcDSQS(38) statement, unfolded: an SQS on `Fin 38` whose derived
design at every point has a colouring with exactly the least number of colours of any colouring
of any STS on `Fin 37`. -/
theorem root38_mc_unfolded : ∃ B : Finset (Finset (Fin 38)),
    ((∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset (Fin 38), T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X) ∧
      ∀ x : Fin 38, ∃ C : Finset (Finset (Finset (Fin 38))),
        ((∀ P ∈ C, P.Nonempty ∧ P ⊆ (B.filter fun X => x ∈ X).image (fun X => X.erase x) ∧
            ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
          ∀ T ∈ (B.filter fun X => x ∈ X).image (fun X => X.erase x), ∃! P, P ∈ C ∧ T ∈ P) ∧
        C.card = sInf {r : ℕ | ∃ S : Finset (Finset (Fin 37)),
          ((∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset (Fin 37), P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T) ∧
          ∃ C' : Finset (Finset (Finset (Fin 37))),
            ((∀ P ∈ C', P.Nonempty ∧ P ⊆ S ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
              ∀ T ∈ S, ∃! P, P ∈ C' ∧ T ∈ P) ∧ C'.card = r} :=
  Mcd.Kernel.exists_mcdsqs38

end Mcd.Audit

#print Mcd.IsSQS
#print Mcd.IsSTS
#print Mcd.derivedBlocks
#print Mcd.IsPPC
#print Mcd.IsColouring
#print Mcd.chiPrime
#print Mcd.TargetColoured
#print Mcd.IsMcDSQS
#print Mcd.TargetMc
#print Mcd.ColourLowerBound
#print Mcd.Kernel.pt
#print Mcd.Kernel.quad
#print Mcd.Kernel.tri
#print Mcd.Kernel.blockSet
#print Mcd.Kernel.tripleSet
#print Mcd.Kernel.classSet
#print Mcd.Kernel.mcdsqs38
#print Mcd.Kernel.colouring38
#print Mcd.Kernel.data38RawSha256
#check @Mcd.Audit.root38_coloured
#check @Mcd.Audit.root37_lower
#check @Mcd.Audit.root37_chi
#check @Mcd.Audit.root38_mc
#check @Mcd.Audit.witness38
#check @Mcd.Audit.root38_coloured_unfolded
#check @Mcd.Audit.root37_lower_unfolded
#check @Mcd.Audit.root37_chi_unfolded
#check @Mcd.Audit.root38_mc_unfolded
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.mcdsqs38_spec
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.data38_shape
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.data38_range
set_option pp.funBinderTypes true in
#check @Mcd.Kernel.sts37_witness
#print axioms Mcd.Counts.card_sts_mul
#print axioms Mcd.Counts.card_ppc_mul_le
#print axioms Mcd.Counts.sum_card_colouring
#print axioms Mcd.Counts.colourLowerBound_37
#print axioms Mcd.Counts.chiPrime_eq_of
#print axioms Mcd.Kernel.isSQS_of_check
#print axioms Mcd.Kernel.colouring_of_check
#print axioms Mcd.Kernel.sts_of_check
#print axioms Mcd.Kernel.data38_shape
#print axioms Mcd.Kernel.data38_range
#print axioms Mcd.Kernel.blocks38_sqsCheck
#print axioms Mcd.Kernel.colour38_check_a
#print axioms Mcd.Kernel.colour38_check_b
#print axioms Mcd.Kernel.colour38_check_c
#print axioms Mcd.Kernel.colour38_check_d
#print axioms Mcd.Kernel.col38_37_stsCheck
#print axioms Mcd.Kernel.isSQS_mcdsqs38
#print axioms Mcd.Kernel.colouring38_spec
#print axioms Mcd.Kernel.coloured38
#print axioms Mcd.Kernel.sts37_witness
#print axioms Mcd.Kernel.chiPrime_37
#print axioms Mcd.Kernel.isMcDSQS_mcdsqs38
#print axioms Mcd.Kernel.exists_mcdsqs38
#print axioms Mcd.Audit.root38_coloured
#print axioms Mcd.Audit.root37_lower
#print axioms Mcd.Audit.root37_chi
#print axioms Mcd.Audit.root38_mc
#print axioms Mcd.Audit.witness38
#print axioms Mcd.Audit.root38_coloured_unfolded
#print axioms Mcd.Audit.root37_lower_unfolded
#print axioms Mcd.Audit.root37_chi_unfolded
#print axioms Mcd.Audit.root38_mc_unfolded
