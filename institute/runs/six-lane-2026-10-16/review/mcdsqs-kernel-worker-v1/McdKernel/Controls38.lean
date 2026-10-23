import McdKernel.Cert38

/-!
# Kernel controls for the mcDSQS(38) checkers

No root depends on this module.  Every mutation acts on the pinned literals of `McdKernel.Data38`
themselves, and every statement is proved by kernel evaluation (`decide +kernel`) or from the
definitions:

* **swap**: in `POINT 5`, `CLASS 0`, the points `0` and `1` exchanged between the triples
  `(0, 19, 24)` and `(1, 28, 31)`.  The class is still pairwise disjoint, but the colouring check
  fails; semantically `{1, 19, 24}` is not a derived block at `5` (`swap_not_derived`: the
  unique block through `{5, 1, 19}` is `{1, 5, 19, 34}`).
* **merge**: `CLASS 17` and `CLASS 18` of `POINT 5` merged into one class (18 classes): the
  merged class is not pairwise disjoint, so the colouring check fails.
* **reduce**: the triple `(0, 19, 24)` of `POINT 5` replaced by `(0, 19, 62)`, which names the
  same residues modulo 38; the range test rejects it.
* **block**: the block `(0, 1, 2, 37)` replaced by `(0, 1, 2, 36)`; the SQS check fails.
* **sts**: in `POINT 37`, `CLASS 0`, the points `0` and `1` exchanged between `(0, 4, 28)` and
  `(1, 3, 36)`; the coloured-STS check on `Fin 37` fails.
* **reorder** (positive control): the classes of `POINT 5` listed in reverse order still pass the
  colouring check (the checker is not keyed to the raw order).
-/

namespace Mcd.Kernel.Controls

open Mcd.Kernel

/-- Replace triple `t` of raw class `j` by `e`. -/
def setTriple (cls : List (List RawTriple)) (j t : ℕ) (e : RawTriple) : List (List RawTriple) :=
  cls.set j ((cls.getD j []).set t e)

/-! ## swap -/

/-- `POINT 5`, `CLASS 0`: `(0, 19, 24), (1, 28, 31)` replaced by `(1, 19, 24), (0, 28, 31)`. -/
def col5swap : List (List RawTriple) :=
  setTriple (setTriple col38_5 0 0 (1, 19, 24)) 0 1 (0, 28, 31)

theorem swap_spec :
    (col38_5.getD 0 []).take 2 = [(0, 19, 24), (1, 28, 31)] ∧
      (col5swap.getD 0 []).take 2 = [(1, 19, 24), (0, 28, 31)] := by
  decide +kernel

theorem swap_classes_ok : col5swap.all (classOK 38) = true := by
  decide +kernel

theorem swap_colCheck_false : colCheck 38 blocks38 5 col5swap = false := by
  decide +kernel

/-- The swapped triple `{1, 19, 24}` is not a block of the derived design at `5`. -/
theorem swap_not_derived : ({1, 19, 24} : Finset (Fin 38)) ∉ derivedBlocks mcdsqs38 5 := by
  intro h
  simp only [derivedBlocks, Finset.mem_image, Finset.mem_filter] at h
  obtain ⟨X, ⟨hX, h5⟩, hXT⟩ := h
  have h1 : (1 : Fin 38) ∈ X := (Finset.mem_erase.mp (hXT ▸ (by decide : (1 : Fin 38) ∈
    ({1, 19, 24} : Finset (Fin 38))))).2
  have h19 : (19 : Fin 38) ∈ X := (Finset.mem_erase.mp (hXT ▸ (by decide : (19 : Fin 38) ∈
    ({1, 19, 24} : Finset (Fin 38))))).2
  have h24 : (24 : Fin 38) ∈ X := (Finset.mem_erase.mp (hXT ▸ (by decide : (24 : Fin 38) ∈
    ({1, 19, 24} : Finset (Fin 38))))).2
  have hsub : ({5, 1, 19} : Finset (Fin 38)) ⊆ X := by
    intro w hw
    simp only [Finset.mem_insert, Finset.mem_singleton] at hw
    rcases hw with rfl | rfl | rfl
    · exact h5
    · exact h1
    · exact h19
  obtain ⟨Y, -, hY⟩ := isSQS_mcdsqs38.2 {5, 1, 19} (by decide)
  have hX0 : ({1, 5, 19, 34} : Finset (Fin 38)) ∈ mcdsqs38 :=
    (mcdsqs38_spec _).mpr ⟨(1, 5, 19, 34), by decide +kernel, by decide +kernel⟩
  have hXX0 : X = {1, 5, 19, 34} := (hY X ⟨hX, hsub⟩).trans (hY _ ⟨hX0, by decide⟩).symm
  rw [hXX0] at h24
  exact absurd h24 (by decide)

/-! ## merge, reduce, block, sts, reorder -/

/-- `CLASS 17` and `CLASS 18` of `POINT 5` merged into one class. -/
def col5merge : List (List RawTriple) :=
  (col38_5.take 17) ++ [col38_5.getD 17 [] ++ col38_5.getD 18 []]

theorem merge_length : col5merge.length = 18 := by
  decide +kernel

theorem merge_colCheck_false : colCheck 38 blocks38 5 col5merge = false := by
  decide +kernel

/-- `(0, 19, 24)` of `POINT 5` replaced by `(0, 19, 62)`: the same residues modulo 38. -/
def col5reduce : List (List RawTriple) := setTriple col38_5 0 0 (0, 19, 62)

theorem reduce_same_points : tri 38 (0, 19, 62) = tri 38 (0, 19, 24) := by
  decide +kernel

theorem reduce_colCheck_false : colCheck 38 blocks38 5 col5reduce = false := by
  decide +kernel

/-- The block `(0, 1, 2, 37)` replaced by `(0, 1, 2, 36)`. -/
def blocksMut : List RawQuad := blocks38.set 0 (0, 1, 2, 36)

theorem block_spec : blocks38.take 1 = [(0, 1, 2, 37)] ∧ blocksMut.take 1 = [(0, 1, 2, 36)] := by
  decide +kernel

theorem block_sqsCheck_false : sqsCheck 38 blocksMut = false := by
  decide +kernel

/-- `POINT 37`, `CLASS 0`: `(0, 4, 28), (1, 3, 36)` replaced by `(1, 4, 28), (0, 3, 36)`. -/
def col37swap : List (List RawTriple) :=
  setTriple (setTriple col38_37 0 0 (1, 4, 28)) 0 1 (0, 3, 36)

theorem sts_swap_spec : (col38_37.getD 0 []).take 2 = [(0, 4, 28), (1, 3, 36)] := by
  decide +kernel

theorem sts_swap_false : stsColCheck 37 col37swap = false := by
  decide +kernel

/-- Positive control: the classes of `POINT 5` in reverse order still pass. -/
theorem reorder_colCheck_true : colCheck 38 blocks38 5 col38_5.reverse = true := by
  decide +kernel

end Mcd.Kernel.Controls
