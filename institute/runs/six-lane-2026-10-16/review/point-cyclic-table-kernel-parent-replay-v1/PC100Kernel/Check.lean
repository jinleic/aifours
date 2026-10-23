import PC100Kernel.Target
import Mathlib.GroupTheory.Perm.Fin

/-!
# A kernel-checkable certificate for a resolution of a 2-(v,4,1) design preserved by `x ↦ x + 1`

Raw data is a list of raw classes, each a list of raw blocks `(a, b, c, d)` of natural numbers (the
lines `i a b c d` of a strict `POINT-CYCLIC-RESOLUTION` certificate, grouped by the class index `i`).
The semantic objects they name, on the points `Fin v` (residues modulo `v`):

* `pt v n`: the residue of `n` modulo `v`; `blk v e = {pt v a, pt v b, pt v c, pt v d}`;
* `blocks v d`: the set of all `blk v e` over all listed raw blocks `e`;
* `classOf v c`: the set of the `blk v e` over the raw blocks `e` of one raw class `c`;
* `classes v d`: the set of all `classOf v c` over the raw classes `c` of `d`.

The Boolean checker `certCheck` uses only `Nat` arithmetic, list recursion and bitwise operations on
`Nat`, which the Lean kernel evaluates on literals.  It checks:

1. every listed raw block satisfies `a < b < c < d < v`;
2. inserting the codes `p * v + q` of the six pairs `p < q` of every listed block one by one into a
   bitmask never meets a bit already set, and ends at the mask of all codes `p * v + q` with
   `p < q < v` (every pair of points lies in exactly one listed block, and no block is listed twice);
3. for every raw class, inserting the four points of each of its blocks never meets a set bit and ends
   at the mask of `0, ..., v - 1` (each class partitions the points);
4. shift closure of the classes: for every raw class `c` there is a raw class `c'` such that the
   blocks of `c` translated by `+1` modulo `v` and the blocks of `c'` are the same point sets
   (compared by the bitmask codes `∑ 2 ^ p` of their points, in both directions).

`sound_of_check` (data-independent) turns `certCheck v d = true` into `IsDesign241 (blocks v d)`,
`IsResolution (blocks v d) (classes v d)` and `IsResolutionAutomorphism (blocks v d) (classes v d)
(shift v)`, together with the counts `card (blocks v d) = length d.flatten`,
`card (classes v d) = length d` and `card (classOf v c) = length c`.  `isFullCycle_shift` shows that
`shift (n + 2)` is one cycle through all `n + 2` points (it is Mathlib's `finRotate`).
-/

namespace PC100.Kernel

open PC100

set_option linter.unusedSectionVars false

/-- A raw block `(a, b, c, d)`: the four point numbers of one block line `i a b c d` of the raw
certificate. -/
abbrev RawBlock := ℕ × ℕ × ℕ × ℕ

/-! ## The semantic objects named by raw data -/

section Semantics

variable (v : ℕ) [NeZero v]

/-- The residue of the raw number `n` modulo `v`, as a point of `Fin v`. -/
def pt (n : ℕ) : Fin v := ⟨n % v, Nat.mod_lt _ (Nat.pos_of_neZero v)⟩

/-- The point set `{a, b, c, d}` (residues modulo `v`) named by the raw block `(a, b, c, d)`. -/
def blk (e : RawBlock) : Finset (Fin v) := {pt v e.1, pt v e.2.1, pt v e.2.2.1, pt v e.2.2.2}

/-- The class named by one raw class: the set of its blocks. -/
def classOf (c : List RawBlock) : Finset (Finset (Fin v)) := (c.map (blk v)).toFinset

/-- The block set: all listed blocks, over all raw classes.  (`blocks` and `classes` are
irreducible, so that elaboration never evaluates them on concrete data; proofs use `mem_blocks`
and `mem_classes`.) -/
@[irreducible] def blocks (d : List (List RawBlock)) : Finset (Finset (Fin v)) :=
  (d.flatten.map (blk v)).toFinset

/-- The resolution: the set of the classes named by the raw classes. -/
@[irreducible] def classes (d : List (List RawBlock)) : Finset (Finset (Finset (Fin v))) :=
  (d.map (classOf v)).toFinset

end Semantics

/-! ## The Boolean checker -/

section Checker

/-- `a < b < c < d < v`. -/
def rangeOK (v : ℕ) (e : RawBlock) : Bool :=
  decide (e.1 < e.2.1) && decide (e.2.1 < e.2.2.1) && decide (e.2.2.1 < e.2.2.2) &&
    decide (e.2.2.2 < v)

/-- The four raw points of a raw block. -/
def pts (e : RawBlock) : List ℕ := [e.1, e.2.1, e.2.2.1, e.2.2.2]

/-- The codes `p * v + q` of the six pairs of a raw block `a < b < c < d`. -/
def pairCodes (v : ℕ) (e : RawBlock) : List ℕ :=
  [e.1 * v + e.2.1, e.1 * v + e.2.2.1, e.1 * v + e.2.2.2, e.2.1 * v + e.2.2.1,
    e.2.1 * v + e.2.2.2, e.2.2.1 * v + e.2.2.2]

/-- Insert the codes of `l` one by one into the bitmask `m`; `none` as soon as a bit is already
set. -/
def insertAll : List ℕ → ℕ → Option ℕ
  | [], m => some m
  | c :: l, m => if m.testBit c then none else insertAll l (m ||| 2 ^ c)

/-- Bitwise union of a list of naturals. -/
def orAll (l : List ℕ) : ℕ := l.foldl (· ||| ·) 0

/-- The codes `p * v + q` of all pairs `p < q < v`. -/
def pairList (v : ℕ) : List ℕ :=
  (List.range v).flatMap fun p =>
    ((List.range v).filter fun q => decide (p < q)).map fun q => p * v + q

/-- Bits `p * v + q` for `p < q < v`. -/
def pairMask (v : ℕ) : ℕ := orAll ((pairList v).map (2 ^ ·))

/-- Bits `0, ..., v - 1`. -/
def pointMask (v : ℕ) : ℕ := orAll ((List.range v).map (2 ^ ·))

/-- The bitmask code `∑ 2 ^ p` (bitwise union) of a list of points: it determines the set of the
listed numbers. -/
def setCode (l : List ℕ) : ℕ := orAll (l.map (2 ^ ·))

/-- The points of a raw block translated by `+1` modulo `v`. -/
def shiftPts (v : ℕ) (e : RawBlock) : List ℕ := (pts e).map fun n => (n + 1) % v

/-- The blocks of the raw class `c` translated by `+1` and the blocks of the raw class `c'` are the
same point sets (each translated block of `c` is a block of `c'`, and conversely). -/
def classShiftOK (v : ℕ) (c c' : List RawBlock) : Bool :=
  c.all (fun e => c'.any fun e' => setCode (pts e') == setCode (shiftPts v e)) &&
    c'.all (fun e' => c.any fun e => setCode (shiftPts v e) == setCode (pts e'))

/-- Every raw class translated by `+1` is a raw class. -/
def shiftOK (v : ℕ) (d : List (List RawBlock)) : Bool :=
  d.all fun c => d.any fun c' => classShiftOK v c c'

/-- The certificate checker (items 1–4 of the module documentation). -/
def certCheck (v : ℕ) (d : List (List RawBlock)) : Bool :=
  d.flatten.all (rangeOK v) &&
    insertAll (d.flatten.flatMap (pairCodes v)) 0 == some (pairMask v) &&
    d.all (fun c => insertAll (c.flatMap pts) 0 == some (pointMask v)) &&
    shiftOK v d

end Checker

/-! ## List and bit lemmas -/

section Lemmas

theorem testBit_foldl_or (l : List ℕ) (a k : ℕ) :
    (l.foldl (· ||| ·) a).testBit k = true ↔
      a.testBit k = true ∨ ∃ m ∈ l, m.testBit k = true := by
  induction l generalizing a with
  | nil => simp
  | cons m l ih =>
    rw [List.foldl_cons, ih, Nat.testBit_or, Bool.or_eq_true]
    simp only [List.mem_cons, exists_eq_or_imp]
    tauto

theorem testBit_orAll_pow (l : List ℕ) (k : ℕ) :
    (orAll (l.map (2 ^ ·))).testBit k = true ↔ k ∈ l := by
  rw [orAll, testBit_foldl_or]
  simp [Nat.testBit_two_pow]

theorem insertAll_spec : ∀ (l : List ℕ) (m m' : ℕ), insertAll l m = some m' →
    l.Nodup ∧ (∀ c ∈ l, m.testBit c = false) ∧
      ∀ k, m'.testBit k = (m.testBit k || decide (k ∈ l)) := by
  intro l
  induction l with
  | nil =>
    intro m m' h
    simp only [insertAll, Option.some.injEq] at h
    subst h
    simp
  | cons c l ih =>
    intro m m' h
    simp only [insertAll] at h
    split at h
    · exact absurd h (by simp)
    · rename_i hc
      obtain ⟨hnd, hfresh, hbits⟩ := ih _ _ h
      refine ⟨List.nodup_cons.mpr ⟨?_, hnd⟩, ?_, ?_⟩
      · intro hcl
        have h1 := hfresh c hcl
        simp [Nat.testBit_or] at h1
      · intro c' hc'
        rcases List.mem_cons.mp hc' with rfl | hc'
        · simpa using hc
        · have h1 := hfresh c' hc'
          rw [Nat.testBit_or, Bool.or_eq_false_iff] at h1
          exact h1.1
      · intro k
        rw [hbits k, Nat.testBit_or, Nat.testBit_two_pow]
        by_cases hk : k = c
        · subst hk
          simp
        · have hck : c ≠ k := fun h' => hk h'.symm
          simp [hk, hck]

theorem insertAll_zero_eq {l L : List ℕ} (h : insertAll l 0 = some (orAll (L.map (2 ^ ·)))) :
    l.Nodup ∧ ∀ k, k ∈ l ↔ k ∈ L := by
  obtain ⟨hnd, -, hbits⟩ := insertAll_spec l 0 _ h
  refine ⟨hnd, fun k => ?_⟩
  rw [← testBit_orAll_pow L k, hbits k]
  simp

theorem mem_pairList {v k : ℕ} :
    k ∈ pairList v ↔ ∃ p q, p < q ∧ q < v ∧ p * v + q = k := by
  simp only [pairList, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_filter,
    decide_eq_true_eq]
  constructor
  · rintro ⟨p, -, q, ⟨hq, hpq⟩, rfl⟩
    exact ⟨p, q, hpq, hq, rfl⟩
  · rintro ⟨p, q, hpq, hq, rfl⟩
    exact ⟨p, by omega, q, ⟨hq, hpq⟩, rfl⟩

theorem mul_add_inj {v a b c d : ℕ} (hb : b < v) (hd : d < v) (h : a * v + b = c * v + d) :
    a = c ∧ b = d := by
  have hv : 0 < v := by omega
  have h1 : ∀ x y : ℕ, y < v → (x * v + y) % v = y := by
    intro x y hy
    rw [Nat.add_comm, Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt hy]
  have h2 : ∀ x y : ℕ, y < v → (x * v + y) / v = x := by
    intro x y hy
    rw [Nat.add_comm, Nat.add_mul_div_right _ _ hv, Nat.div_eq_of_lt hy, Nat.zero_add]
  exact ⟨by rw [← h2 a b hb, ← h2 c d hd, h], by rw [← h1 a b hb, ← h1 c d hd, h]⟩

theorem eq_of_mem_of_nodup_flatMap {α β : Type*} {f : α → List β} :
    ∀ {l : List α}, (l.flatMap f).Nodup → ∀ {a b : α} {c : β}, a ∈ l → b ∈ l → c ∈ f a →
      c ∈ f b → a = b
  | [], _, _, _, _, ha, _, _, _ => absurd ha List.not_mem_nil
  | x :: l, hnd, a, b, c, ha, hb, hca, hcb => by
    rw [List.flatMap_cons, List.nodup_append] at hnd
    obtain ⟨-, hnd', hdisj⟩ := hnd
    rcases List.mem_cons.mp ha with rfl | ha' <;> rcases List.mem_cons.mp hb with rfl | hb'
    · rfl
    · exact absurd rfl (hdisj c hca c (List.mem_flatMap.mpr ⟨b, hb', hcb⟩))
    · exact absurd rfl (hdisj c hcb c (List.mem_flatMap.mpr ⟨a, ha', hca⟩))
    · exact eq_of_mem_of_nodup_flatMap hnd' ha' hb' hca hcb

theorem nodup_of_nodup_flatMap {α β : Type*} {f : α → List β} :
    ∀ {l : List α}, (∀ a ∈ l, f a ≠ []) → (l.flatMap f).Nodup → l.Nodup
  | [], _, _ => List.nodup_nil
  | x :: l, hne, hnd => by
    rw [List.flatMap_cons, List.nodup_append] at hnd
    obtain ⟨-, hnd', hdisj⟩ := hnd
    refine List.nodup_cons.mpr ⟨fun hx => ?_,
      nodup_of_nodup_flatMap (fun a ha => hne a (List.mem_cons_of_mem x ha)) hnd'⟩
    obtain ⟨c, hc⟩ := List.exists_mem_of_ne_nil _ (hne x List.mem_cons_self)
    exact hdisj c hc c (List.mem_flatMap.mpr ⟨x, hx, hc⟩) rfl

theorem setCode_eq_iff {l l' : List ℕ} : setCode l = setCode l' ↔ ∀ k, k ∈ l ↔ k ∈ l' := by
  constructor
  · intro h k
    rw [← testBit_orAll_pow l k, ← testBit_orAll_pow l' k]
    exact Iff.of_eq (congrArg (fun n => n.testBit k = true) h)
  · intro h
    apply Nat.eq_of_testBit_eq
    intro k
    have h1 := testBit_orAll_pow l k
    have h2 := testBit_orAll_pow l' k
    unfold setCode
    by_cases hk : k ∈ l
    · rw [h1.mpr hk, h2.mpr ((h k).mp hk)]
    · have hk' : k ∉ l' := fun h' => hk ((h k).mpr h')
      rw [Bool.eq_false_iff.mpr (fun h'' => hk (h1.mp h'')),
        Bool.eq_false_iff.mpr (fun h'' => hk' (h2.mp h''))]

end Lemmas

/-! ## Soundness -/

section Soundness

variable {v : ℕ} [NeZero v]

theorem pt_val {n : ℕ} (h : n < v) : (pt v n).val = n := Nat.mod_eq_of_lt h

theorem rangeOK_iff {e : RawBlock} :
    rangeOK v e = true ↔ e.1 < e.2.1 ∧ e.2.1 < e.2.2.1 ∧ e.2.2.1 < e.2.2.2 ∧ e.2.2.2 < v := by
  simp [rangeOK, and_assoc]

theorem mem_pts {e : RawBlock} {k : ℕ} :
    k ∈ pts e ↔ k = e.1 ∨ k = e.2.1 ∨ k = e.2.2.1 ∨ k = e.2.2.2 := by
  simp [pts]

theorem mem_blk {e : RawBlock} (he : rangeOK v e = true) {y : Fin v} :
    y ∈ blk v e ↔ y.val ∈ pts e := by
  obtain ⟨h1, h2, h3, h4⟩ := rangeOK_iff.mp he
  rw [mem_pts]
  simp only [blk, Finset.mem_insert, Finset.mem_singleton, Fin.ext_iff,
    pt_val (show e.1 < v by omega), pt_val (show e.2.1 < v by omega),
    pt_val (show e.2.2.1 < v by omega), pt_val h4]

theorem blk_card {e : RawBlock} (he : rangeOK v e = true) : (blk v e).card = 4 := by
  obtain ⟨h1, h2, h3, h4⟩ := rangeOK_iff.mp he
  have hne : ∀ m n : ℕ, m < v → n < v → m ≠ n → pt v m ≠ pt v n := by
    intro m n hm hn hmn h'
    have := congrArg Fin.val h'
    rw [pt_val hm, pt_val hn] at this
    exact hmn this
  unfold blk
  rw [Finset.card_insert_of_notMem, Finset.card_insert_of_notMem, Finset.card_pair]
  · exact hne _ _ (by omega) h4 (by omega)
  · simp only [Finset.mem_insert, Finset.mem_singleton, not_or]
    exact ⟨hne _ _ (by omega) (by omega) (by omega), hne _ _ (by omega) h4 (by omega)⟩
  · simp only [Finset.mem_insert, Finset.mem_singleton, not_or]
    exact ⟨hne _ _ (by omega) (by omega) (by omega), hne _ _ (by omega) (by omega) (by omega),
      hne _ _ (by omega) h4 (by omega)⟩

theorem mem_blocks {d : List (List RawBlock)} {X : Finset (Fin v)} :
    X ∈ blocks v d ↔ ∃ e ∈ d.flatten, blk v e = X := by
  simp only [blocks, List.mem_toFinset, List.mem_map]

theorem mem_classOf {c : List RawBlock} {X : Finset (Fin v)} :
    X ∈ classOf v c ↔ ∃ e ∈ c, blk v e = X := by
  simp only [classOf, List.mem_toFinset, List.mem_map]

theorem mem_classes {d : List (List RawBlock)} {P : Finset (Finset (Fin v))} :
    P ∈ classes v d ↔ ∃ c ∈ d, classOf v c = P := by
  simp only [classes, List.mem_toFinset, List.mem_map]

/-- The shift on raw points: `pt v n + 1 = pt v ((n + 1) % v)` (as values). -/
theorem val_pt_add_one {n : ℕ} (hn : n < v) : (pt v n + 1).val = (n + 1) % v := by
  rw [Fin.val_add, pt_val hn, Fin.val_one', Nat.add_mod_mod]

theorem mem_shiftPts {e : RawBlock} {k : ℕ} :
    k ∈ shiftPts v e ↔ ∃ n ∈ pts e, (n + 1) % v = k := by
  simp only [shiftPts, List.mem_map]

/-- The image of a listed block under the shift, read off from `shiftPts`. -/
theorem mem_blockImage_shift_blk {e : RawBlock} (he : rangeOK v e = true) {y : Fin v} :
    y ∈ blockImage (shift v) (blk v e) ↔ y.val ∈ shiftPts v e := by
  obtain ⟨h1, h2, h3, h4⟩ := rangeOK_iff.mp he
  have hlt : ∀ n ∈ pts e, n < v := by
    intro n hn
    rw [mem_pts] at hn
    omega
  rw [mem_shiftPts]
  simp only [blockImage, Finset.mem_map, Equiv.coe_toEmbedding]
  constructor
  · rintro ⟨x, hx, rfl⟩
    refine ⟨x.val, (mem_blk he).mp hx, ?_⟩
    have := val_pt_add_one (v := v) x.isLt
    rw [show pt v x.val = x from Fin.ext (pt_val x.isLt)] at this
    exact this.symm
  · rintro ⟨n, hn, hny⟩
    refine ⟨pt v n, (mem_blk he).mpr (by rw [pt_val (hlt n hn)]; exact hn), ?_⟩
    apply Fin.ext
    show (pt v n + 1).val = y.val
    rw [val_pt_add_one (hlt n hn), hny]

/-- Equal bitmask codes: the listed block `blk v e'` is the shift of the listed block `blk v e`. -/
theorem blk_eq_shift_of_code {e e' : RawBlock} (he : rangeOK v e = true)
    (he' : rangeOK v e' = true) (h : setCode (pts e') = setCode (shiftPts v e)) :
    blk v e' = blockImage (shift v) (blk v e) := by
  ext y
  rw [mem_blk he', mem_blockImage_shift_blk he]
  exact setCode_eq_iff.mp h y.val

/-- Two distinct points of a listed block give one of its pair codes. -/
theorem pair_code_mem {e : RawBlock} (he : rangeOK v e = true) {y z : Fin v} (hyz : y.val < z.val)
    (hy : y ∈ blk v e) (hz : z ∈ blk v e) : y.val * v + z.val ∈ pairCodes v e := by
  have hR := rangeOK_iff.mp he
  rw [mem_blk he, mem_pts] at hy hz
  simp only [pairCodes, List.mem_cons, List.not_mem_nil, or_false]
  rcases hy with hy | hy | hy | hy <;> rcases hz with hz | hz | hz | hz <;>
    first
    | (exfalso; omega)
    | simp [hy, hz]

/-- **Soundness of the certificate checker.**  No hypothesis is a semantic property of the data. -/
theorem sound_of_check {d : List (List RawBlock)} (h : certCheck v d = true) :
    IsDesign241 (blocks v d) ∧ IsResolution (blocks v d) (classes v d) ∧
      IsResolutionAutomorphism (blocks v d) (classes v d) (shift v) ∧
      (blocks v d).card = d.flatten.length ∧ (classes v d).card = d.length ∧
      ∀ c ∈ d, (classOf v c).card = c.length := by
  simp only [certCheck, shiftOK, Bool.and_eq_true, List.all_eq_true, beq_iff_eq] at h
  obtain ⟨⟨⟨hr, hp⟩, hc⟩, hs⟩ := h
  obtain ⟨hpnd, hpmem⟩ := insertAll_zero_eq hp
  have hflat : d.flatten.Nodup :=
    nodup_of_nodup_flatMap (f := pairCodes v) (fun e _ => by simp [pairCodes]) hpnd
  have hflat' : (d.flatMap id).Nodup := by rwa [List.flatMap_id]
  -- A pair of distinct points lies in at most one listed block (raw level).
  have pair_unique : ∀ e ∈ d.flatten, ∀ e' ∈ d.flatten, ∀ y z : Fin v, y ≠ z →
      y ∈ blk v e → z ∈ blk v e → y ∈ blk v e' → z ∈ blk v e' → e = e' := by
    intro e he e' he' y z hyz hy hz hy' hz'
    rcases lt_or_gt_of_ne (Fin.val_ne_of_ne hyz) with hlt | hlt
    · exact eq_of_mem_of_nodup_flatMap hpnd he he' (pair_code_mem (hr e he) hlt hy hz)
        (pair_code_mem (hr e' he') hlt hy' hz')
    · exact eq_of_mem_of_nodup_flatMap hpnd he he' (pair_code_mem (hr e he) hlt hz hy)
        (pair_code_mem (hr e' he') hlt hz' hy')
  -- Equal listed blocks are equal raw blocks.
  have blk_inj : ∀ e ∈ d.flatten, ∀ e' ∈ d.flatten, blk v e = blk v e' → e = e' := by
    intro e he e' he' heq
    have hR := rangeOK_iff.mp (hr e he)
    have h1 : pt v e.1 ∈ blk v e := by simp [blk]
    have h2 : pt v e.2.1 ∈ blk v e := by simp [blk]
    have hne : pt v e.1 ≠ pt v e.2.1 := by
      intro h'
      have := congrArg Fin.val h'
      rw [pt_val (by omega), pt_val (by omega)] at this
      omega
    exact pair_unique e he e' he' _ _ hne h1 h2 (heq ▸ h1) (heq ▸ h2)
  -- Every pair of points lies in some listed block.
  have pair_ex : ∀ y z : Fin v, y.val < z.val → ∃ e ∈ d.flatten, y ∈ blk v e ∧ z ∈ blk v e := by
    intro y z hlt
    have hk : y.val * v + z.val ∈ pairList v := mem_pairList.mpr ⟨y.val, z.val, hlt, z.isLt, rfl⟩
    obtain ⟨e, he, hke⟩ := List.mem_flatMap.mp ((hpmem _).mpr hk)
    have hR := rangeOK_iff.mp (hr e he)
    refine ⟨e, he, ?_⟩
    rw [mem_blk (hr e he), mem_blk (hr e he), mem_pts, mem_pts]
    simp only [pairCodes, List.mem_cons, List.not_mem_nil, or_false] at hke
    rcases hke with h' | h' | h' | h' | h' | h'
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inl h1, Or.inr (Or.inl h2)⟩
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inl h1, Or.inr (Or.inr (Or.inl h2))⟩
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inl h1, Or.inr (Or.inr (Or.inr h2))⟩
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inr (Or.inl h1), Or.inr (Or.inr (Or.inl h2))⟩
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inr (Or.inl h1), Or.inr (Or.inr (Or.inr h2))⟩
    · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
      exact ⟨Or.inr (Or.inr (Or.inl h1)), Or.inr (Or.inr (Or.inr h2))⟩
  -- Raw blocks of a raw class are listed blocks.
  have hcf : ∀ c ∈ d, ∀ e ∈ c, e ∈ d.flatten := fun c hcd e he => List.mem_flatten.mpr ⟨c, hcd, he⟩
  -- Every point lies in exactly one block of each class.
  have class_cover : ∀ c ∈ d, ∀ y : Fin v, ∃! X, X ∈ classOf v c ∧ y ∈ X := by
    intro c hcd y
    obtain ⟨hcnd, hcmem⟩ := insertAll_zero_eq (hc c hcd)
    have hyc : y.val ∈ c.flatMap pts := (hcmem _).mpr (List.mem_range.mpr y.isLt)
    obtain ⟨e, he, hye⟩ := List.mem_flatMap.mp hyc
    refine ⟨blk v e, ⟨mem_classOf.mpr ⟨e, he, rfl⟩, (mem_blk (hr e (hcf c hcd e he))).mpr hye⟩, ?_⟩
    rintro X ⟨hX, hyX⟩
    obtain ⟨e', he', rfl⟩ := mem_classOf.mp hX
    have hye' : y.val ∈ pts e' := (mem_blk (hr e' (hcf c hcd e' he'))).mp hyX
    rw [eq_of_mem_of_nodup_flatMap hcnd he' he hye' hye]
  -- Each class is the image of a class under the shift (for the class given by `shiftOK`).
  have class_shift : ∀ c ∈ d, ∃ c' ∈ d, (classOf v c).image (blockImage (shift v)) = classOf v c' := by
    intro c hcd
    obtain ⟨c', hc'd, hcc'⟩ := List.any_eq_true.mp (hs c hcd)
    simp only [classShiftOK, Bool.and_eq_true, List.all_eq_true, List.any_eq_true,
      beq_iff_eq] at hcc'
    obtain ⟨hfwd, hbwd⟩ := hcc'
    refine ⟨c', hc'd, ?_⟩
    ext X
    simp only [Finset.mem_image, mem_classOf]
    constructor
    · rintro ⟨Y, ⟨e, he, rfl⟩, rfl⟩
      obtain ⟨e', he', hcode⟩ := hfwd e he
      exact ⟨e', he', blk_eq_shift_of_code (hr e (hcf c hcd e he)) (hr e' (hcf c' hc'd e' he'))
        hcode⟩
    · rintro ⟨e', he', rfl⟩
      obtain ⟨e, he, hcode⟩ := hbwd e' he'
      exact ⟨blk v e, ⟨e, he, rfl⟩, (blk_eq_shift_of_code (hr e (hcf c hcd e he))
        (hr e' (hcf c' hc'd e' he')) hcode.symm).symm⟩
  -- The design.
  have hdesign : IsDesign241 (blocks v d) := by
    refine ⟨?_, ?_⟩
    · intro X hX
      obtain ⟨e, he, rfl⟩ := mem_blocks.mp hX
      exact blk_card (hr e he)
    · intro T hT
      obtain ⟨y, z, hyz, rfl⟩ := Finset.card_eq_two.mp hT
      have hpair : ∀ y z : Fin v, y ≠ z → ∃! X, X ∈ blocks v d ∧ ({y, z} : Finset (Fin v)) ⊆ X := by
        intro y z hyz
        have hex : ∃ e ∈ d.flatten, y ∈ blk v e ∧ z ∈ blk v e := by
          rcases lt_or_gt_of_ne (Fin.val_ne_of_ne hyz) with hlt | hlt
          · exact pair_ex y z hlt
          · obtain ⟨e, he, hz, hy⟩ := pair_ex z y hlt
            exact ⟨e, he, hy, hz⟩
        obtain ⟨e, he, hy, hz⟩ := hex
        refine ⟨blk v e, ⟨mem_blocks.mpr ⟨e, he, rfl⟩, ?_⟩, ?_⟩
        · intro w hw
          simp only [Finset.mem_insert, Finset.mem_singleton] at hw
          rcases hw with rfl | rfl
          · exact hy
          · exact hz
        · rintro X ⟨hX, hsub⟩
          obtain ⟨e', he', rfl⟩ := mem_blocks.mp hX
          have hy' : y ∈ blk v e' := hsub (by simp)
          have hz' : z ∈ blk v e' := hsub (by simp)
          rw [pair_unique e' he' e he y z hyz hy' hz' hy hz]
      exact hpair y z hyz
  -- The resolution.
  have hres : IsResolution (blocks v d) (classes v d) := by
    refine ⟨?_, ?_⟩
    · intro P hP
      obtain ⟨c, hcd, rfl⟩ := mem_classes.mp hP
      refine ⟨?_, class_cover c hcd⟩
      intro X hX
      obtain ⟨e, he, rfl⟩ := mem_classOf.mp hX
      exact mem_blocks.mpr ⟨e, hcf c hcd e he, rfl⟩
    · intro X hX
      obtain ⟨e, he, rfl⟩ := mem_blocks.mp hX
      obtain ⟨c, hcd, hec⟩ := List.mem_flatten.mp he
      refine ⟨classOf v c, ⟨mem_classes.mpr ⟨c, hcd, rfl⟩, mem_classOf.mpr ⟨e, hec, rfl⟩⟩, ?_⟩
      rintro P ⟨hP, hXP⟩
      obtain ⟨c', hc'd, rfl⟩ := mem_classes.mp hP
      obtain ⟨e', he'c', heq⟩ := mem_classOf.mp hXP
      obtain rfl : e' = e := blk_inj e' (hcf c' hc'd e' he'c') e he heq
      rw [eq_of_mem_of_nodup_flatMap (f := id) hflat' hc'd hcd he'c' hec]
  -- The shift.
  have hauto : IsResolutionAutomorphism (blocks v d) (classes v d) (shift v) := by
    have hsub : (blocks v d).image (blockImage (shift v)) ⊆ blocks v d := by
      intro Y hY
      obtain ⟨X, hX, rfl⟩ := Finset.mem_image.mp hY
      obtain ⟨e, he, rfl⟩ := mem_blocks.mp hX
      obtain ⟨c, hcd, hec⟩ := List.mem_flatten.mp he
      obtain ⟨c', hc'd, hcc'⟩ := class_shift c hcd
      have hmem : blockImage (shift v) (blk v e) ∈ classOf v c' := by
        rw [← hcc']
        exact Finset.mem_image_of_mem _ (mem_classOf.mpr ⟨e, hec, rfl⟩)
      obtain ⟨e', he', heq⟩ := mem_classOf.mp hmem
      exact mem_blocks.mpr ⟨e', hcf c' hc'd e' he', heq⟩
    have hinj : Function.Injective (blockImage (shift v)) := Finset.map_injective _
    refine ⟨Finset.eq_of_subset_of_card_le hsub
      (le_of_eq (Finset.card_image_of_injective _ hinj).symm), ?_⟩
    intro P hP
    obtain ⟨c, hcd, rfl⟩ := mem_classes.mp hP
    obtain ⟨c', hc'd, hcc'⟩ := class_shift c hcd
    rw [hcc']
    exact mem_classes.mpr ⟨c', hc'd, rfl⟩
  -- Counts.
  have hmapnd : (d.flatten.map (blk v)).Nodup :=
    List.Nodup.map_on (fun e he e' he' heq => blk_inj e he e' he' heq) hflat
  have hcard_blocks : (blocks v d).card = d.flatten.length := by
    rw [blocks, List.toFinset_card_of_nodup hmapnd, List.length_map]
  have hcard_class : ∀ c ∈ d, (classOf v c).card = c.length := by
    intro c hcd
    have hcnd : c.Nodup := List.Sublist.nodup (List.sublist_flatten_of_mem hcd) hflat
    have hcmapnd : (c.map (blk v)).Nodup :=
      List.Nodup.map_on (fun e he e' he' heq => blk_inj e (hcf c hcd e he) e' (hcf c hcd e' he') heq)
        hcnd
    rw [classOf, List.toFinset_card_of_nodup hcmapnd, List.length_map]
  have hne : ∀ c ∈ d, c ≠ [] := by
    intro c hcd hnil
    obtain ⟨X, hX, -⟩ := (class_cover c hcd (pt v 0)).exists
    obtain ⟨e, he, -⟩ := mem_classOf.mp hX
    rw [hnil] at he
    exact List.not_mem_nil he
  have hdnd : d.Nodup := nodup_of_nodup_flatMap (f := id) hne hflat'
  have hclassinj : ∀ c ∈ d, ∀ c' ∈ d, classOf v c = classOf v c' → c = c' := by
    intro c hcd c' hc'd heq
    obtain ⟨e, he⟩ := List.exists_mem_of_ne_nil c (hne c hcd)
    have hX : blk v e ∈ classOf v c' := heq ▸ mem_classOf.mpr ⟨e, he, rfl⟩
    obtain ⟨e', he', heq'⟩ := mem_classOf.mp hX
    obtain rfl : e' = e := blk_inj e' (hcf c' hc'd e' he') e (hcf c hcd e he) heq'
    exact eq_of_mem_of_nodup_flatMap (f := id) hflat' hcd hc'd he he'
  have hcard_classes : (classes v d).card = d.length := by
    rw [classes, List.toFinset_card_of_nodup (List.Nodup.map_on hclassinj hdnd), List.length_map]
  exact ⟨hdesign, hres, hauto, hcard_blocks, hcard_classes, hcard_class⟩

end Soundness

/-! ## The shift is one cycle through all points -/

theorem shift_eq_finRotate (n : ℕ) : shift (n + 1) = finRotate (n + 1) := by
  ext i
  rw [finRotate_apply]
  rfl

theorem isFullCycle_shift (n : ℕ) : IsFullCycle (shift (n + 2)) := by
  rw [shift_eq_finRotate]
  exact ⟨isCycle_finRotate, support_finRotate⟩

theorem cycleType_shift (n : ℕ) : (shift (n + 2)).cycleType = {n + 2} := by
  rw [shift_eq_finRotate]
  exact cycleType_finRotate

end PC100.Kernel
