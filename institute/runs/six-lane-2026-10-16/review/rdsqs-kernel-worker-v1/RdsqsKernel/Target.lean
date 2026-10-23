import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card

/-!
# Steiner quadruple systems with resolvable derived designs: the target statement

This module imports no proof and no data; it fixes the meaning of the kernel-checked roots.
Definitions follow Tan–Zhou, arXiv:2503.11934v1, §1 (parent copy
`mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`, lines 48–82), for an
arbitrary point type `V` with decidable equality:

* `IsSQS B`: `B` is a set of blocks; every block is a 4-subset of `V`, and every 3-subset of `V`
  lies in exactly one block (an `SQS(v) = S(3,4,v)`, `v = card V`).  A *set* of blocks loses
  nothing: a repeated block would put each of its 3-subsets in two blocks.
* `derivedBlocks B x`: the block set `B_x = {X \ {x} : X ∈ B, x ∈ X}` of the derived design of `B`
  at the point `x` (a design on the point set `V \ {x}`).
* `IsDerivedParallelClass B x P`: `P` is a parallel class of the derived design at `x`: a set of
  blocks of `B_x` such that every point `y ≠ x` lies in exactly one block of `P` (so the blocks
  of `P` are pairwise disjoint and partition `V \ {x}`; no block of `B_x` contains `x`).
* `IsDerivedResolution B x R`: `R` is a resolution of the derived design at `x`: every member of
  `R` is a parallel class of the derived design at `x`, and every block of `B_x` lies in exactly
  one member of `R` (so `R` partitions `B_x`).
* `IsRDSQS B`: `B` is an SQS and its derived design at EVERY point `x : V` has a resolution.
* `Target v`: an RDSQS exists on the `v`-element point set `Fin v = {0, ..., v - 1}`.
* `TargetAll v`: every finite type with exactly `v` elements (with any decidable-equality
  instance) carries an RDSQS.
* `TargetCounts v`: `Target v` with all forced counts written out: `v(v-1)(v-2)/24` blocks; at
  every point `x`, `(v-1)(v-2)/6` derived blocks, each a 3-subset not containing `x`, and a
  resolution with `(v-2)/2` classes of `(v-1)/3` blocks.

`IsSQS`, `IsDerivedParallelClass`, `IsDerivedResolution` and `IsRDSQS` fix no number of blocks,
classes or blocks per class: on `v` points they are forced by the definitions, and
`RdsqsKernel.Counts` derives them (it is how `TargetCounts` is proved, not an assumption).
-/

namespace Rdsqs

universe u

section Defs

variable {V : Type u} [DecidableEq V]

/-- `B` is the block set of a Steiner quadruple system on the point type `V`: every block is a
4-subset of `V`, and every 3-subset of `V` lies in exactly one block. -/
def IsSQS (B : Finset (Finset V)) : Prop :=
  (∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset V, T.card = 3 → ∃! X, X ∈ B ∧ T ⊆ X

/-- The block set `B_x = {X \ {x} : X ∈ B, x ∈ X}` of the derived design of `B` at the point `x`
(a design on the point set `V \ {x}`). -/
def derivedBlocks (B : Finset (Finset V)) (x : V) : Finset (Finset V) :=
  (B.filter fun X => x ∈ X).image fun X => X.erase x

/-- `P` is a parallel class of the derived design of `B` at `x`: a set of blocks of `B_x` such
that every point other than `x` lies in exactly one block of `P` (`P` partitions `V \ {x}`). -/
def IsDerivedParallelClass (B : Finset (Finset V)) (x : V) (P : Finset (Finset V)) : Prop :=
  P ⊆ derivedBlocks B x ∧ ∀ y : V, y ≠ x → ∃! T, T ∈ P ∧ y ∈ T

/-- `R` is a resolution of the derived design of `B` at `x`: every member of `R` is a parallel
class of the derived design at `x`, and every block of `B_x` lies in exactly one member of `R`
(`R` partitions `B_x` into parallel classes). -/
def IsDerivedResolution (B : Finset (Finset V)) (x : V) (R : Finset (Finset (Finset V))) :
    Prop :=
  (∀ P ∈ R, IsDerivedParallelClass B x P) ∧ ∀ T ∈ derivedBlocks B x, ∃! P, P ∈ R ∧ T ∈ P

/-- `B` is an RDSQS: an SQS whose derived design at every point `x` is resolvable. -/
def IsRDSQS (B : Finset (Finset V)) : Prop :=
  IsSQS B ∧ ∀ x : V, ∃ R : Finset (Finset (Finset V)), IsDerivedResolution B x R

end Defs

/-- **Target.** An `RDSQS(v)` exists on the point set `Fin v = {0, ..., v - 1}`. -/
def Target (v : ℕ) : Prop :=
  ∃ B : Finset (Finset (Fin v)), IsRDSQS B

/-- Every point type with exactly `v` elements (and every decidable-equality instance on it)
carries an `RDSQS(v)`. -/
def TargetAll (v : ℕ) : Prop :=
  ∀ (V : Type u) [Fintype V] [DecidableEq V], Fintype.card V = v →
    ∃ B : Finset (Finset V), IsRDSQS B

/-- `Target v` with every count forced by the definitions written out explicitly: an SQS on
`Fin v` with `v (v - 1) (v - 2) / 24` blocks such that at every point `x` the derived design has
`(v - 1) (v - 2) / 6` blocks, each a 3-subset of `Fin v` not containing `x`, and a resolution
with `(v - 2) / 2` parallel classes of `(v - 1) / 3` blocks each. -/
def TargetCounts (v : ℕ) : Prop :=
  ∃ B : Finset (Finset (Fin v)), IsSQS B ∧ B.card = v * (v - 1) * (v - 2) / 24 ∧
    ∀ x : Fin v, (∀ T ∈ derivedBlocks B x, T.card = 3 ∧ x ∉ T) ∧
      (derivedBlocks B x).card = (v - 1) * (v - 2) / 6 ∧
      ∃ R : Finset (Finset (Finset (Fin v))), IsDerivedResolution B x R ∧
        R.card = (v - 2) / 2 ∧ ∀ P ∈ R, P.card = (v - 1) / 3

end Rdsqs
