import PC100Kernel.Cert100
import PC100Kernel.Data64

/-!
# Kernel controls for the point-cyclic resolution checker

No root depends on this module.  Every mutation acts on a pinned literal (`cert100` of
`PC100Kernel.Data100`, or the control literal `tz64` of `PC100Kernel.Data64`), and every statement is
proved by kernel evaluation (`decide +kernel`) or from the definitions:

* **swap** (pairs): the points `1` and `2` exchanged between the first blocks of `CLASS 0` and
  `CLASS 1` (`(0, 1, 12, 92)`, `(0, 2, 69, 74)` become `(0, 2, 12, 92)`, `(0, 1, 69, 74)`).  The pair
  insertion meets a pair twice, so `certCheck` is `false`; semantically the block set is not a
  2-(100,4,1) design (`swap_not_design`: `{2, 12}` lies in two blocks).
* **relabel** (shift only): the points `1` and `2` exchanged in every block, which is not an affine map
  of `Z_100`.  Items 1–3 of the checker pass (an isomorphic design and resolution), the shift test
  fails, and semantically `x ↦ x + 1` does not preserve the block set (`relabel_not_shift_invariant`:
  `{0, 2, 12, 92}` is a block, `{1, 3, 13, 93}` is not).
* **move** (classes): the first block of `CLASS 0` moved to the end of `CLASS 1`.  The block set is
  unchanged and the pair test passes, the class test fails, and semantically the classes are not a
  resolution (`move_not_resolution`: no block of the new class `0` contains the point `0`).
* **reduce**: `(0, 1, 12, 92)` replaced by `(0, 1, 12, 192)`, which names the same residues; the range
  test rejects it (no reduction modulo 100 is accepted).
* **drop**: the last block of `CLASS 32` removed; `certCheck` is `false`.
* **v = 64 positive control**: the checker accepts the published point-cyclic resolution of a
  2-(64,4,1) design, and `sound_of_check` gives its design, resolution and shift invariance.
* **v = 64 class trade** (classes mapped to classes only): in `tz64`, the four blocks
  `(0, 1, 3, 7) + 16 k` of `CLASS 0` and the four short blocks `(0, 16, 32, 48) + j` (`j = 0, 1, 3, 7`)
  of `CLASS 12` cover the same 16 points; exchanging them keeps the block set and every class
  partition (items 1–3 pass) but the shift test fails, and semantically the block set is still
  mapped onto itself while the new `CLASS 0` is not mapped onto a class
  (`trade_not_class_invariant`).
-/

namespace PC100.Kernel.Controls

open PC100 PC100.Kernel

/-- Replace block `j` of raw class `i` by `e`. -/
def setBlock (d : List (List RawBlock)) (i j : ℕ) (e : RawBlock) : List (List RawBlock) :=
  d.set i ((d.getD i []).set j e)

/-- Sort two numbers. -/
def sort2 (a b : ℕ) : ℕ × ℕ := (min a b, max a b)

/-- Sort four numbers (comparator network (0,1) (2,3) (0,2) (1,3) (1,2)). -/
def sort4 (a b c d : ℕ) : RawBlock :=
  let p := sort2 a b
  let q := sort2 c d
  let r := sort2 p.1 q.1
  let s := sort2 p.2 q.2
  let t := sort2 s.1 r.2
  (r.1, t.1, t.2, s.2)

/-- Apply a point relabelling to every raw block (re-sorting each block). -/
def relabelData (σ : ℕ → ℕ) (d : List (List RawBlock)) : List (List RawBlock) :=
  d.map (List.map fun e => sort4 (σ e.1) (σ e.2.1) (σ e.2.2.1) (σ e.2.2.2))

/-- Exchange the points `1` and `2`. -/
def swap12 (p : ℕ) : ℕ := if p = 1 then 2 else if p = 2 then 1 else p

/-! ## swap -/

/-- The points `1` and `2` exchanged between the first blocks of `CLASS 0` and `CLASS 1`. -/
def cert100swap : List (List RawBlock) :=
  setBlock (setBlock cert100 0 0 (0, 2, 12, 92)) 1 0 (0, 1, 69, 74)

theorem swap_spec :
    (cert100.getD 0 []).take 1 = [(0, 1, 12, 92)] ∧ (cert100.getD 1 []).take 1 = [(0, 2, 69, 74)] ∧
      (cert100swap.getD 0 []).take 1 = [(0, 2, 12, 92)] ∧
      (cert100swap.getD 1 []).take 1 = [(0, 1, 69, 74)] := by
  decide +kernel

theorem swap_range_ok : cert100swap.flatten.all (rangeOK 100) = true := by
  decide +kernel

theorem swap_pairs_fail : insertAll (cert100swap.flatten.flatMap (pairCodes 100)) 0 = none := by
  decide +kernel

theorem swap_check_false : certCheck 100 cert100swap = false := by
  decide +kernel

/-- The swapped data is not a 2-(100,4,1) design: `{2, 12}` lies in the two distinct blocks
`{0, 2, 12, 92}` and `{2, 12, 31, 89}`. -/
theorem swap_not_design : ¬ IsDesign241 (blocks 100 cert100swap) := by
  intro h
  have hT : ({2, 12} : Finset (Fin 100)).card = 2 := by decide
  obtain ⟨X, -, huniq⟩ := h.2 _ hT
  have h1 : ({0, 2, 12, 92} : Finset (Fin 100)) ∈ blocks 100 cert100swap :=
    mem_blocks.mpr ⟨(0, 2, 12, 92), by decide +kernel, by decide +kernel⟩
  have h2 : ({2, 12, 31, 89} : Finset (Fin 100)) ∈ blocks 100 cert100swap :=
    mem_blocks.mpr ⟨(2, 12, 31, 89), by decide +kernel, by decide +kernel⟩
  have e1 := huniq _ ⟨h1, by decide⟩
  have e2 := huniq _ ⟨h2, by decide⟩
  exact absurd (e1.trans e2.symm) (by decide)

/-! ## relabel -/

/-- The points `1` and `2` exchanged in every block. -/
def cert100relabel : List (List RawBlock) := relabelData swap12 cert100

theorem relabel_spec : (cert100relabel.getD 0 []).take 1 = [(0, 2, 12, 92)] := by
  decide +kernel

theorem relabel_range_ok : cert100relabel.flatten.all (rangeOK 100) = true := by
  decide +kernel

theorem relabel_pairs_ok :
    insertAll (cert100relabel.flatten.flatMap (pairCodes 100)) 0 = some (pairMask 100) := by
  decide +kernel

theorem relabel_classes_ok :
    cert100relabel.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 100)) = true := by
  decide +kernel

theorem relabel_shift_fail : shiftOK 100 cert100relabel = false := by
  decide +kernel

theorem relabel_check_false : certCheck 100 cert100relabel = false := by
  decide +kernel

/-- The relabelled data (an isomorphic design and resolution) is not preserved by `x ↦ x + 1`:
`{0, 2, 12, 92}` is a block and its translate `{1, 3, 13, 93}` is not. -/
theorem relabel_not_shift_invariant :
    ¬ IsResolutionAutomorphism (blocks 100 cert100relabel) (classes 100 cert100relabel)
      (shift 100) := by
  intro h
  have hX : ({0, 2, 12, 92} : Finset (Fin 100)) ∈ blocks 100 cert100relabel :=
    mem_blocks.mpr ⟨(0, 2, 12, 92), by decide +kernel, by decide +kernel⟩
  have himg : blockImage (shift 100) ({0, 2, 12, 92} : Finset (Fin 100)) = {1, 3, 13, 93} := by
    decide +kernel
  have hmem := Finset.mem_image_of_mem (blockImage (shift 100)) hX
  rw [h.1, himg] at hmem
  have hnot : ∀ e ∈ cert100relabel.flatten, blk 100 e ≠ {1, 3, 13, 93} := by
    decide +kernel
  obtain ⟨e, he, heq⟩ := mem_blocks.mp hmem
  exact hnot e he heq

/-! ## move -/

/-- The first block `(0, 1, 12, 92)` of `CLASS 0` moved to the end of `CLASS 1`. -/
def cert100move : List (List RawBlock) :=
  (cert100.set 0 ((cert100.getD 0 []).drop 1)).set 1 ((cert100.getD 1 []) ++ [(0, 1, 12, 92)])

theorem move_spec :
    (cert100.getD 0 []).take 1 = [(0, 1, 12, 92)] ∧ cert100move.flatten.length = 825 ∧
      (cert100move.getD 0 []).length = 24 ∧ (cert100move.getD 1 []).length = 26 := by
  decide +kernel

theorem move_pairs_ok :
    insertAll (cert100move.flatten.flatMap (pairCodes 100)) 0 = some (pairMask 100) := by
  decide +kernel

theorem move_classes_fail :
    cert100move.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 100)) = false := by
  decide +kernel

theorem move_check_false : certCheck 100 cert100move = false := by
  decide +kernel

/-- The moved data is not a resolution: the new class `0` has no block containing the point `0`. -/
theorem move_not_resolution :
    ¬ IsResolution (blocks 100 cert100move) (classes 100 cert100move) := by
  intro h
  have hc : cert100move.getD 0 [] ∈ cert100move := by
    decide +kernel
  obtain ⟨X, ⟨hX, h0X⟩, -⟩ := (h.1 _ (mem_classes.mpr ⟨_, hc, rfl⟩)).2 0
  obtain ⟨e, he, rfl⟩ := mem_classOf.mp hX
  have hnot : ∀ e ∈ cert100move.getD 0 [], (0 : Fin 100) ∉ blk 100 e := by
    decide +kernel
  exact hnot e he h0X

/-! ## reduce, drop -/

/-- `(0, 1, 12, 92)` replaced by `(0, 1, 12, 192)`: the same residues modulo 100. -/
def cert100reduce : List (List RawBlock) := setBlock cert100 0 0 (0, 1, 12, 192)

theorem reduce_same_points : blk 100 (0, 1, 12, 192) = blk 100 (0, 1, 12, 92) := by
  decide +kernel

theorem reduce_range_fail : cert100reduce.flatten.all (rangeOK 100) = false := by
  decide +kernel

theorem reduce_check_false : certCheck 100 cert100reduce = false := by
  decide +kernel

/-- The last block of `CLASS 32` removed. -/
def cert100drop : List (List RawBlock) := cert100.set 32 (cert100.getD 32 []).dropLast

theorem drop_spec : cert100drop.flatten.length = 824 := by
  decide +kernel

theorem drop_check_false : certCheck 100 cert100drop = false := by
  decide +kernel

/-! ## v = 64: positive control and class trade -/

theorem tz64_check : certCheck 64 tz64 = true := by
  decide +kernel

/-- The published v = 64 example passes the same checker: a 2-(64,4,1) design with a resolution
preserved by `x ↦ x + 1`. -/
theorem tz64_sound : IsDesign241 (blocks 64 tz64) ∧ IsResolution (blocks 64 tz64) (classes 64 tz64) ∧
    IsResolutionAutomorphism (blocks 64 tz64) (classes 64 tz64) (shift 64) :=
  ⟨(sound_of_check tz64_check).1, (sound_of_check tz64_check).2.1,
    (sound_of_check tz64_check).2.2.1⟩

/-- Exchange the four blocks `(0, 1, 3, 7) + 16 k` with the four short blocks
`(0, 16, 32, 48) + j` (`j = 0, 1, 3, 7`), position by position. -/
def tradeBlock (e : RawBlock) : RawBlock :=
  if e = (0, 1, 3, 7) then (0, 16, 32, 48) else if e = (0, 16, 32, 48) then (0, 1, 3, 7) else
  if e = (16, 17, 19, 23) then (1, 17, 33, 49) else if e = (1, 17, 33, 49) then (16, 17, 19, 23) else
  if e = (32, 33, 35, 39) then (3, 19, 35, 51) else if e = (3, 19, 35, 51) then (32, 33, 35, 39) else
  if e = (48, 49, 51, 55) then (7, 23, 39, 55) else if e = (7, 23, 39, 55) then (48, 49, 51, 55) else
  e

/-- `tz64` with the four-block subpartitions of `CLASS 0` and `CLASS 12` exchanged. -/
def tz64trade : List (List RawBlock) := tz64.map (List.map tradeBlock)

theorem trade_spec_class0 :
    ∀ e ∈ ([(0, 1, 3, 7), (16, 17, 19, 23), (32, 33, 35, 39), (48, 49, 51, 55)] : List RawBlock),
      e ∈ tz64.getD 0 [] ∧ tradeBlock e ∈ tz64.getD 12 [] ∧ tradeBlock e ∈ tz64trade.getD 0 [] := by
  decide +kernel

theorem trade_spec_class12 :
    ∀ e ∈ ([(0, 16, 32, 48), (1, 17, 33, 49), (3, 19, 35, 51), (7, 23, 39, 55)] : List RawBlock),
      e ∈ tz64.getD 12 [] ∧ tradeBlock e ∈ tz64.getD 0 [] ∧ tradeBlock e ∈ tz64trade.getD 12 [] := by
  decide +kernel

theorem trade_spec_others :
    ∀ i ∈ List.range 21, i ≠ 0 → i ≠ 12 → tz64trade.getD i [] = tz64.getD i [] := by
  decide +kernel

theorem trade_same_listed_blocks :
    (∀ e ∈ tz64trade.flatten, e ∈ tz64.flatten) ∧ (∀ e ∈ tz64.flatten, e ∈ tz64trade.flatten) := by
  decide +kernel

theorem trade_range_ok : tz64trade.flatten.all (rangeOK 64) = true := by
  decide +kernel

theorem trade_pairs_ok :
    insertAll (tz64trade.flatten.flatMap (pairCodes 64)) 0 = some (pairMask 64) := by
  decide +kernel

theorem trade_classes_ok :
    tz64trade.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask 64)) = true := by
  decide +kernel

theorem trade_shift_fail : shiftOK 64 tz64trade = false := by
  decide +kernel

theorem trade_check_false : certCheck 64 tz64trade = false := by
  decide +kernel

/-- The traded data has the same block set as `tz64`. -/
theorem trade_same_blocks : blocks 64 tz64trade = blocks 64 tz64 := by
  ext X
  rw [mem_blocks, mem_blocks]
  constructor
  · rintro ⟨e, he, rfl⟩
    exact ⟨e, trade_same_listed_blocks.1 e he, rfl⟩
  · rintro ⟨e, he, rfl⟩
    exact ⟨e, trade_same_listed_blocks.2 e he, rfl⟩

/-- `x ↦ x + 1` still maps the traded block set onto itself. -/
theorem trade_blocks_shift_invariant :
    (blocks 64 tz64trade).image (blockImage (shift 64)) = blocks 64 tz64trade := by
  rw [trade_same_blocks]
  exact tz64_sound.2.2.1

/-- ... but not every traded class onto a class: the image of the new class `0` contains
`{1, 17, 33, 49}` (the translate of `{0, 16, 32, 48}`) and `{2, 18, 34, 50}` (the translate of
`{1, 17, 33, 49}`), and no traded class contains both. -/
theorem trade_not_class_invariant :
    ¬ ∀ P ∈ classes 64 tz64trade, P.image (blockImage (shift 64)) ∈ classes 64 tz64trade := by
  intro h
  have hc : tz64trade.getD 0 [] ∈ tz64trade := by
    decide +kernel
  have hP := h _ (mem_classes.mpr ⟨_, hc, rfl⟩)
  obtain ⟨c, hc', hceq⟩ := mem_classes.mp hP
  have hY1 : ({1, 17, 33, 49} : Finset (Fin 64)) ∈
      (classOf 64 (tz64trade.getD 0 [])).image (blockImage (shift 64)) := by
    refine Finset.mem_image.mpr ⟨{0, 16, 32, 48}, ?_, by decide +kernel⟩
    exact mem_classOf.mpr ⟨(0, 16, 32, 48), by decide +kernel, by decide +kernel⟩
  have hY2 : ({2, 18, 34, 50} : Finset (Fin 64)) ∈
      (classOf 64 (tz64trade.getD 0 [])).image (blockImage (shift 64)) := by
    refine Finset.mem_image.mpr ⟨{1, 17, 33, 49}, ?_, by decide +kernel⟩
    exact mem_classOf.mpr ⟨(1, 17, 33, 49), by decide +kernel, by decide +kernel⟩
  rw [← hceq] at hY1 hY2
  have hnot : ∀ c ∈ tz64trade,
      ¬ (({1, 17, 33, 49} : Finset (Fin 64)) ∈ classOf 64 c ∧ ({2, 18, 34, 50} : Finset (Fin 64)) ∈ classOf 64 c) := by
    decide +kernel
  exact hnot c hc' ⟨hY1, hY2⟩

end PC100.Kernel.Controls
