import RdsqsKernel.Cert52

/-!
# Kernel controls for the RDSQS(52) checker

No root depends on this module.  Every mutation acts on the pinned literal `data52` itself
(`RdsqsKernel.Data52`), and every statement is proved by kernel evaluation (`decide +kernel`) or
from the definitions:

* **swap**: points `26` and `15` exchanged between the first two triples of `CLASS 0`.  Every
  class is still a partition of the nonzero points, but the pair insertion meets a pair twice, so
  `seedCheck` is `false`; semantically the generated block set is not an SQS (`swap_not_sqs`).
* **relabel**: the points `1` and `2` exchanged in every triple.  The seed is still a resolvable
  STS on the nonzero points (items 1–3 of the checker pass), but the closure test fails, and the
  generated block set is not an SQS (`relabel_not_sqs`): the closure condition is essential.
* **reduce**: the triple `(1, 26, 51)` replaced by `(1, 26, 103)`, which names the same residues;
  the range test rejects it (no reduction modulo 52 is accepted).
* **drop**: the last triple of `CLASS 24` removed; `seedCheck` is `false`.
* **multiplier**: `3` is a unit modulo 52 (inverse `35`) but not in `⟨23⟩`; `multCheck` is
  `false`.
-/

namespace Rdsqs.Kernel.Controls

open Rdsqs.Kernel

/-- Replace triple `j` of raw class `i` by `e`. -/
def setTriple (d : List (List RawTriple)) (i j : ℕ) (e : RawTriple) : List (List RawTriple) :=
  d.set i ((d.getD i []).set j e)

/-- Sort the three numbers of a raw triple increasingly. -/
def sort3 (a b c : ℕ) : RawTriple :=
  (min a (min b c), a + b + c - min a (min b c) - max a (max b c), max a (max b c))

/-- Apply a point relabelling to every raw triple (re-sorting each triple). -/
def relabelData (σ : ℕ → ℕ) (d : List (List RawTriple)) : List (List RawTriple) :=
  d.map (List.map fun e => sort3 (σ e.1) (σ e.2.1) (σ e.2.2))

/-- Exchange the points `1` and `2`. -/
def swap12 (p : ℕ) : ℕ := if p = 1 then 2 else if p = 2 then 1 else p

/-! ## swap -/

/-- Points `26` and `15` exchanged between the first two triples of `CLASS 0`. -/
def data52swap : List (List RawTriple) :=
  setTriple (setTriple data52 0 0 (1, 15, 51)) 0 1 (2, 26, 34)

theorem swap_spec :
    (data52.getD 0 []).take 2 = [(1, 26, 51), (2, 15, 34)] ∧
      (data52swap.getD 0 []).take 2 = [(1, 15, 51), (2, 26, 34)] := by
  decide +kernel

theorem swap_classes_ok :
    data52swap.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 52)) = true := by
  decide +kernel

theorem swap_pairs_fail : insertAll (data52swap.flatten.flatMap (pairCodes 52)) 0 = none := by
  decide +kernel

theorem swap_seedCheck_false : seedCheck 52 data52swap = false := by
  decide +kernel

/-- The swapped seed does not generate an SQS: `{0, 1, 15}` lies in the two distinct generated
blocks `{0, 1, 15, 51}` and `{0, 1, 15, 48}`. -/
theorem swap_not_sqs : ¬ IsSQS (blocks 52 data52swap) := by
  intro h
  have hT : ({0, 1, 15} : Finset (Fin 52)).card = 3 := by decide
  obtain ⟨X, -, huniq⟩ := h.2 _ hT
  have h1 : ({0, 1, 15, 51} : Finset (Fin 52)) ∈ blocks 52 data52swap :=
    mem_blocks.mpr ⟨0, (1, 15, 51), by decide +kernel, by decide +kernel⟩
  have h2 : ({0, 1, 15, 48} : Finset (Fin 52)) ∈ blocks 52 data52swap :=
    mem_blocks.mpr ⟨0, (1, 15, 48), by decide +kernel, by decide +kernel⟩
  have e1 := huniq _ ⟨h1, by decide⟩
  have e2 := huniq _ ⟨h2, by decide⟩
  exact absurd (e1.trans e2.symm) (by decide)

/-! ## relabel -/

/-- The points `1` and `2` exchanged in every triple. -/
def data52relabel : List (List RawTriple) := relabelData swap12 data52

theorem relabel_spec : (data52relabel.getD 0 []).take 1 = [(2, 26, 51)] := by
  decide +kernel

theorem relabel_range_ok : data52relabel.flatten.all (rangeOK 52) = true := by
  decide +kernel

theorem relabel_pairs_ok :
    insertAll (data52relabel.flatten.flatMap (pairCodes 52)) 0 = some (pairMask 52) := by
  decide +kernel

theorem relabel_classes_ok :
    data52relabel.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 52)) = true := by
  decide +kernel

theorem relabel_closed_fail :
    data52relabel.flatten.all (closedOK 52 (tripleMask 52 data52relabel.flatten)) = false := by
  decide +kernel

theorem relabel_seedCheck_false : seedCheck 52 data52relabel = false := by
  decide +kernel

/-- The relabelled seed (a resolvable STS on the nonzero points) does not generate an SQS:
`{0, 24, 49}` lies in `{0, 24, 49, 50}` (the translate of `{0, 2, 26, 51}` by `50`) and in
`{0, 24, 33, 49}`. -/
theorem relabel_not_sqs : ¬ IsSQS (blocks 52 data52relabel) := by
  intro h
  have hT : ({0, 24, 49} : Finset (Fin 52)).card = 3 := by decide
  obtain ⟨X, -, huniq⟩ := h.2 _ hT
  have h1 : ({0, 24, 49, 50} : Finset (Fin 52)) ∈ blocks 52 data52relabel :=
    mem_blocks.mpr ⟨50, (2, 26, 51), by decide +kernel, by decide +kernel⟩
  have h2 : ({0, 24, 33, 49} : Finset (Fin 52)) ∈ blocks 52 data52relabel :=
    mem_blocks.mpr ⟨0, (24, 33, 49), by decide +kernel, by decide +kernel⟩
  have e1 := huniq _ ⟨h1, by decide⟩
  have e2 := huniq _ ⟨h2, by decide⟩
  exact absurd (e1.trans e2.symm) (by decide)

/-! ## reduce, drop, multiplier -/

/-- `(1, 26, 51)` replaced by `(1, 26, 103)`: the same residues modulo 52. -/
def data52reduce : List (List RawTriple) := setTriple data52 0 0 (1, 26, 103)

theorem reduce_same_points : tri 52 (1, 26, 103) = tri 52 (1, 26, 51) := by
  decide +kernel

theorem reduce_seedCheck_false : seedCheck 52 data52reduce = false := by
  decide +kernel

/-- The last triple of `CLASS 24` removed. -/
def data52drop : List (List RawTriple) := data52.set 24 (data52.getD 24 []).dropLast

theorem drop_spec : data52drop.flatten.length = 424 := by
  decide +kernel

theorem drop_seedCheck_false : seedCheck 52 data52drop = false := by
  decide +kernel

theorem mult3_unit : unitOK 52 3 35 = true := by
  decide +kernel

theorem mult3_false : multCheck 52 data52 3 35 = false := by
  decide +kernel

end Rdsqs.Kernel.Controls
