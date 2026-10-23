import McdKernel.Target

/-!
# gcDCQS(20^4 : 0): the target statements

This module imports no proof and no data; together with `McdKernel.Target` (byte-identical copy
of the reviewed mcDSQS(38) target module: `IsSQS`, `IsSTS`, `derivedBlocks`, `IsPPC`,
`IsColouring`, `chiPrime`, `IsMcDSQS`, `TargetMc`, `ColourLowerBound`) it fixes the meaning of
the kernel-checked gcDCQS roots.  Definitions follow Tan–Zhou, arXiv:2503.11934v1, §2 (parent
copy `mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`: STS(v, h) and gcSTS
lines 211–236, candelabra systems lines 256–266, gcDCQS lines 281–288), specialised to an EMPTY
stem `S = ∅`:

* `IsGroupPartition Gs`: the groups are nonempty, pairwise disjoint and cover the point set.
* `IsCQS0 Gs A`: a candelabra quadruple system CQS(g^n : 0) with groups `Gs` and empty stem:
  the groups partition the points, every block is a 4-subset, every 3-subset contained in no
  group lies in exactly one block, and no 3-subset of a group lies in any block.
* `IsHoleSTS Y H D`: an incomplete Steiner triple system STS(|Y|, |H|) on the point set `Y` with
  the hole `H ⊆ Y`: every block is a 3-subset of `Y`, every 2-subset of `Y` not contained in `H`
  lies in exactly one block, and no 2-subset of `H` lies in any block (a GDD(2, 3, |Y|) of type
  1^(|Y| - |H|) |H|^1 with `H` as the long group).
* `IsGcSTS Y H D`: a good colourable gcSTS(|Y|, |H|): an `IsHoleSTS` whose blocks are
  partitioned into `r := χ′(|Y|)` partial parallel classes (`IsColouring`, each class nonempty),
  of which exactly `s := χ′(|Y|) - (|Y| - |H|) / 2` are PPCs of `Y \ H` (every block of the
  class is disjoint from `H`).  `χ′` is `chiPrime` of `McdKernel.Target`: the least number of
  colours of a colouring of ANY STS on `Fin n`, not a numeral.
* `IsGcDCQS0 Gs A`: a gcDCQS(g^n : 0): a CQS with empty stem such that for every group `G` and
  every `x ∈ G` the derived design `(X \ {x}, G \ {x}, A_x)` is a gcSTS.  Tan–Zhou's condition (2)
  on stem points is vacuous for the empty stem and therefore absent.
* `grp80 i = {20 i, ..., 20 i + 19}` and `groups80 = {grp80 0, grp80 1, grp80 2, grp80 3}`: the four
  groups of `Fin 80`; `TargetGc80`: a gcDCQS(20^4 : 0) with these groups exists on `Fin 80`.
-/

namespace Mcd

universe u

section Defs

variable {V : Type u} [DecidableEq V]

/-- The groups `Gs` partition `V`: they are nonempty, pairwise disjoint and cover `V`. -/
def IsGroupPartition (Gs : Finset (Finset V)) : Prop :=
  (∀ G ∈ Gs, G.Nonempty) ∧ (∀ G ∈ Gs, ∀ G' ∈ Gs, G ≠ G' → Disjoint G G') ∧
    ∀ x : V, ∃ G ∈ Gs, x ∈ G

/-- `A` is the block set of a candelabra quadruple system with groups `Gs` and an EMPTY stem:
the groups partition `V`, every block is a 4-subset of `V`, every 3-subset of `V` contained in no
group lies in exactly one block, and no 3-subset of a group lies in any block. -/
def IsCQS0 (Gs : Finset (Finset V)) (A : Finset (Finset V)) : Prop :=
  IsGroupPartition Gs ∧ (∀ X ∈ A, X.card = 4) ∧
    (∀ T : Finset V, T.card = 3 → (∀ G ∈ Gs, ¬ T ⊆ G) → ∃! X, X ∈ A ∧ T ⊆ X) ∧
    ∀ T : Finset V, T.card = 3 → ∀ G ∈ Gs, T ⊆ G → ∀ X ∈ A, ¬ T ⊆ X

/-- `D` is the block set of an incomplete STS on the point set `Y` with the hole `H ⊆ Y`: every
block is a 3-subset of `Y`, every 2-subset of `Y` not contained in `H` lies in exactly one block,
and no 2-subset of `H` lies in any block. -/
def IsHoleSTS (Y H : Finset V) (D : Finset (Finset V)) : Prop :=
  H ⊆ Y ∧ (∀ T ∈ D, T.card = 3 ∧ T ⊆ Y) ∧
    (∀ P : Finset V, P.card = 2 → P ⊆ Y → ¬ P ⊆ H → ∃! T, T ∈ D ∧ P ⊆ T) ∧
    ∀ P : Finset V, P.card = 2 → P ⊆ H → ∀ T ∈ D, ¬ P ⊆ T

/-- `D` is a good colourable incomplete STS on `Y` with hole `H`: it has a colouring with
`χ′(|Y|)` colour classes, of which exactly `χ′(|Y|) - (|Y| - |H|) / 2` avoid `H`. -/
def IsGcSTS (Y H : Finset V) (D : Finset (Finset V)) : Prop :=
  IsHoleSTS Y H D ∧ ∃ C : Finset (Finset (Finset V)), IsColouring D C ∧
    C.card = chiPrime Y.card ∧
    (C.filter fun P => ∀ T ∈ P, Disjoint T H).card = chiPrime Y.card - (Y.card - H.card) / 2

/-- `A` is a gcDCQS with groups `Gs` and empty stem on the finite point set `V`: a CQS whose
derived design at every point `x` of every group `G` is a good colourable incomplete STS on
`V \ {x}` with hole `G \ {x}`. -/
def IsGcDCQS0 [Fintype V] (Gs : Finset (Finset V)) (A : Finset (Finset V)) : Prop :=
  IsCQS0 Gs A ∧ ∀ G ∈ Gs, ∀ x ∈ G,
    IsGcSTS (Finset.univ.erase x) (G.erase x) (derivedBlocks A x)

end Defs

/-- The group `{20 i, ..., 20 i + 19}` of `Fin 80`. -/
def grp80 (i : ℕ) : Finset (Fin 80) :=
  Finset.univ.filter fun y => 20 * i ≤ y.val ∧ y.val < 20 * i + 20

/-- The four groups `{0, ..., 19}`, `{20, ..., 39}`, `{40, ..., 59}`, `{60, ..., 79}`. -/
def groups80 : Finset (Finset (Fin 80)) := {grp80 0, grp80 1, grp80 2, grp80 3}

/-- **Target.**  A gcDCQS(20^4 : 0) with the groups `groups80` (empty stem) exists on `Fin 80`. -/
def TargetGc80 : Prop :=
  ∃ A : Finset (Finset (Fin 80)), IsGcDCQS0 groups80 A

end Mcd
