import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card
import Mathlib.Order.Lattice.Nat

/-!
# Steiner quadruple systems with minimum colourable derived designs: the target statements

This module imports no proof and no data; it fixes the meaning of the kernel-checked roots.
Definitions follow Tan–Zhou, arXiv:2503.11934v1, §1 (parent copy
`mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`, lines 60–134), for an
arbitrary point type `V` with decidable equality:

* `IsSQS B`: every block is a 4-subset of `V` and every 3-subset of `V` lies in exactly one block
  (an `SQS(v) = S(3,4,v)`, `v = card V`).
* `IsSTS S`: every block is a 3-subset of `V` and every 2-subset of `V` lies in exactly one block
  (an `STS(v) = S(2,3,v)`).
* `derivedBlocks B x = {X \ {x} : X ∈ B, x ∈ X}`: the block set of the derived design at `x`.
* `IsPPC D P`: `P` is a partial parallel class (PPC) of the design with block set `D`: a
  nonempty set of blocks of `D` that are pairwise disjoint.
* `IsColouring D C`: `C` is a colouring of the design with block set `D`: a partition of `D`
  into colour classes, each a PPC (every member of `C` is a PPC of `D`, and every block of `D`
  lies in exactly one member of `C`).  An `r`-colouring is one with `C.card = r`.
* `chiPrime n`: `χ′(n)`, the smallest number of colours of a colouring of an STS on `Fin n`
  (the minimum over all STS(n) of their chromatic index), as `sInf` of the set of numbers of
  colours that occur; `sInf ∅ = 0`, irrelevant where the set is nonempty, which is proved for
  `n = 37`.
* `TargetColoured v r`: an SQS on `Fin v` whose derived design at EVERY point has an
  `r`-colouring.
* `IsMcDSQS B` / `TargetMc v`: an mcDSQS(v), i.e. an SQS(v) on `Fin v` whose derived design at
  every point admits a `χ′(v - 1)`-colouring (it is minimum colourable).
* `ColourLowerBound n r`: every colouring of every STS on every `n`-element type (with any
  decidable-equality instance) has at least `r` colour classes.
-/

namespace Mcd

universe u

section Defs

variable {V : Type u} [DecidableEq V]

/-- `B` is the block set of a Steiner quadruple system on `V`: every block is a 4-subset of `V`,
and every 3-subset of `V` lies in exactly one block. -/
def IsSQS (B : Finset (Finset V)) : Prop :=
  (∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset V, T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X

/-- `S` is the block set of a Steiner triple system on `V`: every block is a 3-subset of `V`,
and every 2-subset of `V` lies in exactly one block. -/
def IsSTS (S : Finset (Finset V)) : Prop :=
  (∀ T ∈ S, T.card = 3) ∧ ∀ P : Finset V, P.card = 2 → ∃! T, T ∈ S ∧ P ⊆ T

/-- The block set `B_x = {X \ {x} : X ∈ B, x ∈ X}` of the derived design of `B` at `x`. -/
def derivedBlocks (B : Finset (Finset V)) (x : V) : Finset (Finset V) :=
  (B.filter fun X => x ∈ X).image fun X => X.erase x

/-- `P` is a partial parallel class of the design with block set `D`: a nonempty set of blocks
of `D` that are pairwise disjoint. -/
def IsPPC (D P : Finset (Finset V)) : Prop :=
  P.Nonempty ∧ P ⊆ D ∧ ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T'

/-- `C` is a colouring of the design with block set `D`: every member of `C` (a colour class) is
a partial parallel class of `D`, and every block of `D` lies in exactly one member of `C`. -/
def IsColouring (D : Finset (Finset V)) (C : Finset (Finset (Finset V))) : Prop :=
  (∀ P ∈ C, IsPPC D P) ∧ ∀ T ∈ D, ∃! P, P ∈ C ∧ T ∈ P

end Defs

/-- `χ′(n)`: the least number of colours of a colouring of a Steiner triple system on `Fin n`. -/
noncomputable def chiPrime (n : ℕ) : ℕ :=
  sInf {r : ℕ | ∃ S : Finset (Finset (Fin n)), IsSTS S ∧
    ∃ C : Finset (Finset (Finset (Fin n))), IsColouring S C ∧ C.card = r}

/-- An SQS on `Fin v` whose derived design at every point has an `r`-colouring. -/
def TargetColoured (v r : ℕ) : Prop :=
  ∃ B : Finset (Finset (Fin v)), IsSQS B ∧
    ∀ x : Fin v, ∃ C : Finset (Finset (Finset (Fin v))),
      IsColouring (derivedBlocks B x) C ∧ C.card = r

/-- `B` is an mcDSQS(v): an SQS on `Fin v` whose derived design at every point admits a
`χ′(v - 1)`-colouring. -/
def IsMcDSQS {v : ℕ} (B : Finset (Finset (Fin v))) : Prop :=
  IsSQS B ∧ ∀ x : Fin v, ∃ C : Finset (Finset (Finset (Fin v))),
    IsColouring (derivedBlocks B x) C ∧ C.card = chiPrime (v - 1)

/-- **Target.**  An mcDSQS(v) exists on the point set `Fin v`. -/
def TargetMc (v : ℕ) : Prop :=
  ∃ B : Finset (Finset (Fin v)), IsMcDSQS B

/-- Every colouring of every Steiner triple system on every `n`-element type has at least `r`
colour classes. -/
def ColourLowerBound (n r : ℕ) : Prop :=
  ∀ (W : Type u) [Fintype W] [DecidableEq W], Fintype.card W = n →
    ∀ S : Finset (Finset W), IsSTS S →
      ∀ C : Finset (Finset (Finset W)), IsColouring S C → r ≤ C.card

end Mcd
