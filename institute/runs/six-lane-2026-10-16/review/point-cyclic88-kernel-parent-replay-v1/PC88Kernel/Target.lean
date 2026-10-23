import Mathlib.GroupTheory.Perm.Cycle.Basic
import Mathlib.Data.ZMod.Defs

/-!
# Point-cyclic resolutions of `2-(88,4,1)` designs: the target statement

This module imports no proof and fixes the meaning of the kernel-checked root `PC88.target`.
Definitions follow Topalova–Zhelezova, *Axioms* 15 (2026) 762, Definitions 1–5 (parent excerpt
`review/point-cyclic88-primary-excerpts.txt`), for an arbitrary finite point type `V`:

* `IsDesign B`: `B` is a set of blocks; every block is a 4-subset of `V`, and every 2-subset
  `{x, y}` (`x ≠ y`) of `V` lies in exactly one block (a `2-(v,4,1)` design, `v = card V`).
  A *set* of blocks loses nothing for `λ = 1`: a repeated block would put each of its pairs in
  two blocks.
* `IsParallelClass B P`: `P` is a set of blocks of `B` partitioning the point set, i.e. every point
  lies in exactly one block of `P`.
* `IsResolution B R`: `R` is a partition of the block set `B` into parallel classes: every member
  of `R` is a parallel class of `B`, and every block of `B` lies in exactly one member of `R`.
* `blockImage σ X`: the image of the block `X` under the point permutation `σ`.
* `IsResolutionAut B R σ`: `σ` is an automorphism of the resolution: it maps the block set `B`
  onto itself and maps every parallel class of `R` onto a parallel class of `R`.
* `IsFullCycle σ`: `σ` permutes the points in one cycle (`σ` is a cycle whose support is all of
  `V`, i.e. a single `card V`-cycle).
* `IsPointCyclicResolution B R`: `B` is a `2-(v,4,1)` design, `R` is a resolution of it, and some
  single cycle on all points is an automorphism of the resolution (source Definition 5).
* `Target`: for every point type `V` with exactly 88 elements (and every decidable-equality
  instance on it), no `2-(88,4,1)` design on `V` has a point-cyclic resolution.
* `CanonicalTarget`: the special case `V = ZMod 88`, `σ = (x ↦ x + 1)` (`Equiv.addRight 1`).
  `PC88.Bridge` proves that it implies `Target` by relabelling along an arbitrary 88-cycle, and
  `PC88.Controls` proves the converse specialisation.
-/

namespace PC88

universe u

section Defs

variable {V : Type u} [DecidableEq V]

/-- `B` is the block set of a `2-(v,4,1)` design on the point type `V`: every block is a 4-subset
of `V`, and every 2-subset `{x, y}` (`x ≠ y`) lies in exactly one block. -/
def IsDesign (B : Finset (Finset V)) : Prop :=
  (∀ X ∈ B, X.card = 4) ∧ ∀ x y : V, x ≠ y → ∃! X, X ∈ B ∧ x ∈ X ∧ y ∈ X

/-- `P` is a parallel class of the design `B`: a set of blocks of `B` partitioning the point set
(every point lies in exactly one block of `P`). -/
def IsParallelClass (B : Finset (Finset V)) (P : Finset (Finset V)) : Prop :=
  P ⊆ B ∧ ∀ x : V, ∃! X, X ∈ P ∧ x ∈ X

/-- `R` is a resolution of `B`: a partition of the block set `B` into parallel classes (every
member of `R` is a parallel class of `B`, and every block lies in exactly one member of `R`). -/
def IsResolution (B : Finset (Finset V)) (R : Finset (Finset (Finset V))) : Prop :=
  (∀ P ∈ R, IsParallelClass B P) ∧ ∀ X ∈ B, ∃! P, P ∈ R ∧ X ∈ P

/-- The image `σ(X)` of a block `X` under a permutation `σ` of the points. -/
def blockImage (σ : Equiv.Perm V) (X : Finset V) : Finset V :=
  X.map σ.toEmbedding

/-- `σ` is an automorphism of the resolution `R` of `B`: it maps the block set onto itself and
maps every parallel class of `R` onto a parallel class of `R`. -/
def IsResolutionAut (B : Finset (Finset V)) (R : Finset (Finset (Finset V)))
    (σ : Equiv.Perm V) : Prop :=
  B.image (blockImage σ) = B ∧ ∀ P ∈ R, P.image (blockImage σ) ∈ R

/-- `σ` permutes all points of `V` in one cycle. -/
def IsFullCycle [Fintype V] (σ : Equiv.Perm V) : Prop :=
  σ.IsCycle ∧ σ.support = Finset.univ

/-- `R` is a point-cyclic resolution of the `2-(v,4,1)` design `B` (source Definition 5): a
resolution with an automorphism permuting the points in one cycle. -/
def IsPointCyclicResolution [Fintype V] (B : Finset (Finset V))
    (R : Finset (Finset (Finset V))) : Prop :=
  IsDesign B ∧ IsResolution B R ∧ ∃ σ : Equiv.Perm V, IsFullCycle σ ∧ IsResolutionAut B R σ

end Defs

/-- **Target.** For every point type `V` with exactly 88 elements, no `2-(88,4,1)` design on `V`
has a point-cyclic resolution. -/
def Target : Prop :=
  ∀ (V : Type u) [Fintype V] [DecidableEq V], Fintype.card V = 88 →
    ∀ (B : Finset (Finset V)) (R : Finset (Finset (Finset V))), ¬ IsPointCyclicResolution B R

/-- The canonical special case: points `ZMod 88`, cycle `x ↦ x + 1`. -/
def CanonicalTarget : Prop :=
  ∀ (B : Finset (Finset (ZMod 88))) (R : Finset (Finset (Finset (ZMod 88)))),
    IsDesign B → IsResolution B R → ¬ IsResolutionAut B R (Equiv.addRight (1 : ZMod 88))

end PC88
