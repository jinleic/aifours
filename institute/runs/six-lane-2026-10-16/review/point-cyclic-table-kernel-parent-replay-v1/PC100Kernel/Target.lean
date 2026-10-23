import Mathlib.Data.Finset.Card
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Algebra.Group.Units.Equiv
import Mathlib.GroupTheory.Perm.Cycle.Basic

/-!
# Point-cyclic resolutions of 2-(v,4,1) designs: the target statement

This module imports no proof and no data of this development; it only fixes the meaning of the
kernel-checked roots.  Definitions follow Topalova–Zhelezova, Axioms 15 (2026) 762, Definitions 1–5
and the sentence after Definition 3 (binding as in the lane's `REDUCTION.md` Section 0), for an
arbitrary point type `V` with decidable equality:

* `IsDesign241 B`: `B` is a set of blocks, every block is a 4-subset of `V`, and every 2-subset of
  `V` lies in exactly one block (a 2-(v,4,1) design, `v = card V`; Definition 1 with `k = 4`,
  `λ = 1`).  A *set* of blocks loses nothing: a repeated block would put each of its pairs in two
  blocks.
* `IsParallelClass B P`: `P` is a set of blocks of `B` such that every point lies in exactly one
  block of `P` (a partition of the point set by blocks; Definition 2).
* `IsResolution B R`: every member of `R` is a parallel class of `B`, and every block of `B` lies in
  exactly one member of `R` (`R` partitions the blocks into parallel classes; Definition 2).
* `blockImage σ X`: the image `σ(X)` of a block under a permutation `σ` of the points.
* `IsResolutionAutomorphism B R σ`: `σ` maps the block set onto itself (Definition 3) and maps every
  member of `R` onto a member of `R` (the sentence after Definition 3, applied to `R` and itself).
* `IsFullCycle σ`: `σ` permutes all points in one cycle (`σ` is a cycle and moves every point).
* `IsPointCyclicResolution B R`: `R` is a resolution of `B` with an automorphism that is a full
  cycle (Definition 5: "A resolution is point-cyclic if it has an automorphism permuting the points
  in one cycle").
* `shift v`: the permutation `x ↦ x + 1` of `Fin v = {0, ..., v - 1}` (addition modulo `v`).
* `Target v`: a 2-(v,4,1) design on `Fin v` with a point-cyclic resolution (the design is
  "cyclically resolvable" in the sense of Definition 5).
* `TargetShift v`: `shift v` is one cycle through all `v` points, and some `B`, `R` on `Fin v` form a
  2-(v,4,1) design and a resolution of it that `shift v` preserves (block set and classes).
* `TargetCounts v`: `TargetShift v` without the cycle clause, with the counts `|B| = v(v-1)/12`,
  `|R| = (v-1)/3` and `|P| = v/4` (`P ∈ R`) written out.  The counts are not hypotheses anywhere.
-/

namespace PC100

universe u

section Defs

variable {V : Type u} [DecidableEq V]

/-- `B` is the block set of a 2-(v,4,1) design on the point type `V`: every block is a 4-subset of
`V`, and every 2-subset of `V` lies in exactly one block. -/
def IsDesign241 (B : Finset (Finset V)) : Prop :=
  (∀ X ∈ B, X.card = 4) ∧ ∀ T : Finset V, T.card = 2 → ∃! X, X ∈ B ∧ T ⊆ X

/-- `P` is a parallel class of `B`: a set of blocks of `B` such that every point lies in exactly one
block of `P`. -/
def IsParallelClass (B P : Finset (Finset V)) : Prop :=
  P ⊆ B ∧ ∀ y : V, ∃! X, X ∈ P ∧ y ∈ X

/-- `R` is a resolution of `B`: every member of `R` is a parallel class of `B`, and every block of
`B` lies in exactly one member of `R`. -/
def IsResolution (B : Finset (Finset V)) (R : Finset (Finset (Finset V))) : Prop :=
  (∀ P ∈ R, IsParallelClass B P) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P

/-- The image `σ(X)` of the block `X` under the permutation `σ` of the points. -/
def blockImage (σ : Equiv.Perm V) (X : Finset V) : Finset V :=
  X.map σ.toEmbedding

/-- `σ` is an automorphism of the resolution `R` of `B`: it maps the block set `B` onto itself, and
it maps every class of `R` onto a class of `R`. -/
def IsResolutionAutomorphism (B : Finset (Finset V)) (R : Finset (Finset (Finset V)))
    (σ : Equiv.Perm V) : Prop :=
  B.image (blockImage σ) = B ∧ ∀ P ∈ R, P.image (blockImage σ) ∈ R

/-- `σ` permutes all points of `V` in one cycle: it is a cycle, and it moves every point. -/
def IsFullCycle [Fintype V] (σ : Equiv.Perm V) : Prop :=
  σ.IsCycle ∧ σ.support = Finset.univ

/-- `R` is a point-cyclic resolution of `B`: a resolution with an automorphism permuting the points
in one cycle. -/
def IsPointCyclicResolution [Fintype V] (B : Finset (Finset V))
    (R : Finset (Finset (Finset V))) : Prop :=
  IsResolution B R ∧ ∃ σ : Equiv.Perm V, IsFullCycle σ ∧ IsResolutionAutomorphism B R σ

end Defs

/-- The permutation `x ↦ x + 1` of `Fin v` (addition modulo `v`). -/
def shift (v : ℕ) [NeZero v] : Equiv.Perm (Fin v) :=
  Equiv.addRight 1

/-- **Target.**  A 2-(v,4,1) design on the point set `Fin v` with a point-cyclic resolution. -/
def Target (v : ℕ) : Prop :=
  ∃ B : Finset (Finset (Fin v)), IsDesign241 B ∧
    ∃ R : Finset (Finset (Finset (Fin v))), IsPointCyclicResolution B R

/-- The shift `x ↦ x + 1` of `Fin v` is one cycle through all `v` points, and some 2-(v,4,1) design
on `Fin v` has a resolution such that the shift maps the block set onto itself and every class onto
a class. -/
def TargetShift (v : ℕ) [NeZero v] : Prop :=
  IsFullCycle (shift v) ∧
    ∃ B : Finset (Finset (Fin v)), ∃ R : Finset (Finset (Finset (Fin v))),
      IsDesign241 B ∧ IsResolution B R ∧ IsResolutionAutomorphism B R (shift v)

/-- The shift-preserved resolved design with its counts written out: `v (v - 1) / 12` blocks,
`(v - 1) / 3` classes, `v / 4` blocks in every class. -/
def TargetCounts (v : ℕ) [NeZero v] : Prop :=
  ∃ B : Finset (Finset (Fin v)), ∃ R : Finset (Finset (Finset (Fin v))),
    IsDesign241 B ∧ IsResolution B R ∧ IsResolutionAutomorphism B R (shift v) ∧
      B.card = v * (v - 1) / 12 ∧ R.card = (v - 1) / 3 ∧ ∀ P ∈ R, P.card = v / 4

end PC100
