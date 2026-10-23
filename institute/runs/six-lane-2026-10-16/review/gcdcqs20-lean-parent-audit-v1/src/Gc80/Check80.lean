import McdKernel.Check
import Gc80.Derived

/-!
# Per-point kernel checkers for SQS / CQS certificates with coloured derived designs

`McdKernel.Check` (byte-identical copy of the reviewed mcDSQS(38) checker module) supplies the
raw-data semantics (`pt`, `quad`, `tri`, `blockSet`, `tripleSet`, `classSet`), the colouring
checker `colCheck` with its soundness theorem `colouring_of_check`, and the coloured-STS
checker `stsColCheck` with `sts_of_check`.  Its global SQS checker `sqsCheck` is not used: for
`v = 80` its bitmask over all `80^3` triple codes is too large to fill 82160 times in one kernel
declaration.  Instead the SQS / CQS property is derived from the derived designs, point by
point (`Gc80.Derived`), with the new Boolean checkers below; they use only `Nat` arithmetic,
list recursion and bitwise operations on `Nat`, like `McdKernel.Check`:

* `holeCheck v bl x hole`: for the codes `k` of the derived triples `X \ {x}` (`eraseCode`, as in
  `colCheck`), inserting the codes `p * v + q` of the three pairs of every derived triple
  (`pairCodesOfCode`) one by one into a bitmask never meets a set bit and ends at the mask of
  the codes of all pairs `p < q < v` with `p ≠ x`, `q ≠ x` and not both in the hole
  (`hole p && hole q`).  (`holeCheck_sound`: every 2-subset avoiding `x` and not inside the hole
  lies in exactly one derived block at `x`; no 2-subset inside the hole lies in any.)
* `holeFree hole c`: no point of the raw class `c` is in the hole.
* `pointCheck v bl x hole r n cls`: `colCheck`, `holeCheck`, `r` raw classes and `n` raw triples.
* `gcPointCheck`: `pointCheck` for the group hole `groupHole g x`, and exactly `s` hole-free
  raw classes.
* `blockCheck v n bl`: every block satisfies `a < b < c < d < v`, the block codes `code4` are
  strictly increasing (so the raw blocks are pairwise distinct), and there are `n` of them.
-/

namespace Mcd.Kernel

/-! ## The Boolean checkers -/

section Checker

/-- The codes of the three pairs of the triple with code `k = (a * v + b) * v + c`:
`a * v + b`, `a * v + c`, `b * v + c`. -/
def pairCodesOfCode (v k : ℕ) : List ℕ :=
  [k / v, k / v / v * v + k % v, k / v % v * v + k % v]

/-- The codes of the pairs `p < q < v` with `p ≠ x`, `q ≠ x` and not both `p`, `q` in the hole. -/
def pairListAt (v x : ℕ) (hole : ℕ → Bool) : List ℕ :=
  (List.range v).flatMap fun p => ((List.range' (p + 1) (v - (p + 1))).filter fun q =>
    !(p == x) && !(q == x) && !(hole p && hole q)).map fun q => p * v + q

/-- The derived-design checker at the point `x`, with the hole `hole`. -/
def holeCheck (v : ℕ) (bl : List RawQuad) (x : ℕ) (hole : ℕ → Bool) : Bool :=
  insertAll ((bl.filterMap (eraseCode v x)).flatMap (pairCodesOfCode v)) 0 ==
    some (orAll ((pairListAt v x hole).map (2 ^ ·)))

/-- No point of the raw class `c` lies in the hole. -/
def holeFree (hole : ℕ → Bool) (c : List RawTriple) : Bool :=
  c.all fun e => (pts e).all fun p => !hole p

/-- Everything checked at the point `x`: the raw classes `cls` colour the derived design
(`colCheck`), the derived design has the hole structure (`holeCheck`), `r` raw classes, `n` raw
triples. -/
def pointCheck (v : ℕ) (bl : List RawQuad) (x : ℕ) (hole : ℕ → Bool) (r n : ℕ)
    (cls : List (List RawTriple)) : Bool :=
  colCheck v bl x cls && holeCheck v bl x hole && cls.length == r && cls.flatten.length == n

/-- The hole at `x` for groups `{g i, ..., g i + g - 1}`: the other points of the group of `x`. -/
def groupHole (g x p : ℕ) : Bool :=
  decide (p / g = x / g) && !decide (p = x)

/-- No hole. -/
def noHole (_ : ℕ) : Bool := false

/-- `pointCheck` with the group hole, and exactly `s` hole-free raw classes. -/
def gcPointCheck (v g : ℕ) (bl : List RawQuad) (x r s n : ℕ) (cls : List (List RawTriple)) :
    Bool :=
  pointCheck v bl x (groupHole g x) r n cls && (cls.filter (holeFree (groupHole g x))).length == s

/-- The code of a raw block. -/
def code4 (v : ℕ) (b : RawQuad) : ℕ := code3 v b.1 b.2.1 b.2.2.1 * v + b.2.2.2

/-- The list is strictly increasing. -/
def increasing : List ℕ → Bool
  | a :: b :: l => decide (a < b) && increasing (b :: l)
  | _ => true

/-- The block-list checker. -/
def blockCheck (v n : ℕ) (bl : List RawQuad) : Bool :=
  bl.all (quadOK v) && increasing (bl.map (code4 v)) && bl.length == n

end Checker

/-! ## Soundness -/

section Soundness

variable {v : ℕ} [NeZero v]

theorem pairCodesOfCode_codeT {e : RawTriple} (he : triOK v e = true) :
    pairCodesOfCode v (codeT v e) = pairCodes v e := by
  obtain ⟨h1, h2, h3⟩ := triOK_iff.mp he
  have hv : 0 < v := Nat.pos_of_neZero v
  have hdiv : ∀ a b : ℕ, b < v → (a * v + b) / v = a := fun a b hb => by
    rw [Nat.add_comm, Nat.add_mul_div_right _ _ hv, Nat.div_eq_of_lt hb, Nat.zero_add]
  have hmod : ∀ a b : ℕ, b < v → (a * v + b) % v = b := fun a b hb => by
    rw [Nat.add_comm, Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt hb]
  simp only [pairCodesOfCode, codeT, code3, pairCodes]
  rw [hdiv (e.1 * v + e.2.1) e.2.2 (by omega), hmod (e.1 * v + e.2.1) e.2.2 (by omega),
    hdiv e.1 e.2.1 (by omega), hmod e.1 e.2.1 (by omega)]

omit [NeZero v] in
theorem mem_pairListAt {x k : ℕ} {hole : ℕ → Bool} :
    k ∈ pairListAt v x hole ↔ ∃ p q, p < q ∧ q < v ∧ p ≠ x ∧ q ≠ x ∧
      ¬ (hole p = true ∧ hole q = true) ∧ p * v + q = k := by
  simp only [pairListAt, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_filter,
    List.mem_range'_1, Bool.and_eq_true, Bool.not_eq_true', beq_eq_false_iff_ne, ne_eq,
    Bool.and_eq_false_iff]
  constructor
  · rintro ⟨p, hp, q, ⟨⟨hq1, hq2⟩, ⟨hpx, hqx⟩, hh⟩, rfl⟩
    refine ⟨p, q, by omega, by omega, hpx, hqx, ?_, rfl⟩
    rintro ⟨h1, h2⟩
    rcases hh with h | h <;> simp_all
  · rintro ⟨p, q, hpq, hqv, hpx, hqx, hh, rfl⟩
    refine ⟨p, by omega, q, ⟨⟨by omega, by omega⟩, ⟨hpx, hqx⟩, ?_⟩, rfl⟩
    by_cases h1 : hole p = true
    · right
      simpa [h1] using hh
    · left
      simpa using h1

/-- Two points whose pair code lies in the pair codes of a listed triple lie in it. -/
theorem mem_tri_of_pairCode {e : RawTriple} (he : triOK v e = true) {y z : Fin v}
    (hk : y.val * v + z.val ∈ pairCodes v e) :
    y ∈ tri v e ∧ z ∈ tri v e := by
  have hR := triOK_iff.mp he
  rw [mem_tri he, mem_tri he]
  simp only [pairCodes, List.mem_cons, List.not_mem_nil, or_false] at hk
  rcases hk with h' | h' | h'
  · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
    exact ⟨Or.inl h1, Or.inr (Or.inl h2)⟩
  · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
    exact ⟨Or.inl h1, Or.inr (Or.inr h2)⟩
  · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
    exact ⟨Or.inr (Or.inl h1), Or.inr (Or.inr h2)⟩

omit [NeZero v] in
/-- Every 2-subset of `Fin v` is `{y, z}` with `y < z`. -/
theorem exists_sorted_two {P : Finset (Fin v)} (h : P.card = 2) :
    ∃ y z : Fin v, y.val < z.val ∧ P = {y, z} := by
  obtain ⟨y, z, hyz, rfl⟩ := Finset.card_eq_two.mp h
  rcases Nat.lt_or_gt_of_ne (Fin.val_ne_of_ne hyz) with hlt | hlt
  · exact ⟨y, z, hlt, rfl⟩
  · exact ⟨z, y, hlt, Finset.pair_comm y z⟩

/-- The derived blocks at `x` are the triples `tri v e` whose codes are listed by `eraseCode`. -/
theorem mem_derived_iff {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {T : Finset (Fin v)} :
    T ∈ derivedBlocks (blockSet v bl) (pt v x) ↔
      ∃ e : RawTriple, triOK v e = true ∧ codeT v e ∈ bl.filterMap (eraseCode v x) ∧
        tri v e = T := by
  rw [mem_derivedBlocks]
  constructor
  · rintro ⟨X, hX, hxX, rfl⟩
    obtain ⟨b, hb, rfl⟩ := mem_blockSet.mp hX
    rcases eraseCode_spec (hq b hb) hx with ⟨-, hnot⟩ | ⟨e, hsome, he, -, herase⟩
    · exact absurd hxX hnot
    · exact ⟨e, he, List.mem_filterMap.mpr ⟨b, hb, hsome⟩, herase.symm⟩
  · rintro ⟨e, he, hk, rfl⟩
    obtain ⟨b, hb, hbk⟩ := List.mem_filterMap.mp hk
    rcases eraseCode_spec (hq b hb) hx with ⟨hnone, -⟩ | ⟨e', hsome, he', hxb, herase⟩
    · rw [hnone] at hbk
      exact absurd hbk (by simp)
    · rw [hsome, Option.some.injEq] at hbk
      obtain rfl : e' = e := codeT_inj he' he hbk
      exact ⟨quad v b, mem_blockSet.mpr ⟨b, hb, rfl⟩, hxb, herase⟩

/-- Every code listed by `eraseCode` is the code of a raw triple `a < b < c < v`. -/
theorem exists_of_mem_filterMap {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {k : ℕ} (hk : k ∈ bl.filterMap (eraseCode v x)) :
    ∃ e : RawTriple, triOK v e = true ∧ codeT v e = k := by
  obtain ⟨b, hb, hbk⟩ := List.mem_filterMap.mp hk
  rcases eraseCode_spec (hq b hb) hx with ⟨hnone, -⟩ | ⟨e, hsome, he, -, -⟩
  · rw [hnone] at hbk
    exact absurd hbk (by simp)
  · rw [hsome, Option.some.injEq] at hbk
    exact ⟨e, he, hbk⟩

/-- **Soundness of the derived-design checker at `x`.** -/
theorem holeCheck_sound {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {hole : ℕ → Bool} (h : holeCheck v bl x hole = true) :
    (∀ P : Finset (Fin v), P.card = 2 → pt v x ∉ P → (∃ y ∈ P, hole y.val = false) →
      ∃! T, T ∈ derivedBlocks (blockSet v bl) (pt v x) ∧ P ⊆ T) ∧
    (∀ P : Finset (Fin v), P.card = 2 → (∀ y ∈ P, hole y.val = true) →
      ∀ T ∈ derivedBlocks (blockSet v bl) (pt v x), ¬ P ⊆ T) := by
  simp only [holeCheck, beq_iff_eq] at h
  obtain ⟨hnd, hmem⟩ := insertAll_zero_eq h
  refine ⟨fun P hP hxP hfree => ?_, fun P hP hall T hT hPT => ?_⟩
  · obtain ⟨y, z, hyz, rfl⟩ := exists_sorted_two hP
    have hy : y.val ≠ x := (ne_pt_iff hx y).mp fun h' => hxP (h' ▸ Finset.mem_insert_self y _)
    have hz : z.val ≠ x := (ne_pt_iff hx z).mp fun h' =>
      hxP (h' ▸ Finset.mem_insert_of_mem (Finset.mem_singleton_self z))
    have hh : ¬ (hole y.val = true ∧ hole z.val = true) := by
      rintro ⟨h1, h2⟩
      obtain ⟨w, hw, hwf⟩ := hfree
      simp only [Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl <;> simp_all
    have hk : y.val * v + z.val ∈ pairListAt v x hole :=
      mem_pairListAt.mpr ⟨y.val, z.val, hyz, z.isLt, hy, hz, hh, rfl⟩
    obtain ⟨k, hkK, hkp⟩ := List.mem_flatMap.mp ((hmem _).mpr hk)
    obtain ⟨e, he, rfl⟩ := exists_of_mem_filterMap hq hx hkK
    rw [pairCodesOfCode_codeT he] at hkp
    obtain ⟨hye, hze⟩ := mem_tri_of_pairCode he hkp
    have hsub : ({y, z} : Finset (Fin v)) ⊆ tri v e := by
      intro w hw
      simp only [Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact hye
      · exact hze
    refine ⟨tri v e, ⟨(mem_derived_iff hq hx).mpr ⟨e, he, hkK, rfl⟩, hsub⟩, ?_⟩
    rintro T' ⟨hT', hsubT⟩
    obtain ⟨e', he', hk', rfl⟩ := (mem_derived_iff hq hx).mp hT'
    have h1 : y.val * v + z.val ∈ pairCodesOfCode v (codeT v e') := by
      rw [pairCodesOfCode_codeT he']
      exact pairCode_mem he' hyz (hsubT (by simp)) (hsubT (by simp))
    have h2 : y.val * v + z.val ∈ pairCodesOfCode v (codeT v e) := by
      rw [pairCodesOfCode_codeT he]
      exact hkp
    rw [codeT_inj he' he (eq_of_mem_of_nodup_flatMap hnd hk' hkK h1 h2)]
  · obtain ⟨y, z, hyz, rfl⟩ := exists_sorted_two hP
    obtain ⟨e, he, hkK, rfl⟩ := (mem_derived_iff hq hx).mp hT
    have hc : y.val * v + z.val ∈ pairCodesOfCode v (codeT v e) := by
      rw [pairCodesOfCode_codeT he]
      exact pairCode_mem he hyz (hPT (by simp)) (hPT (by simp))
    have hk := (hmem _).mp (List.mem_flatMap.mpr ⟨_, hkK, hc⟩)
    obtain ⟨p, q, -, hqv, -, -, hh, hpq⟩ := mem_pairListAt.mp hk
    obtain ⟨rfl, rfl⟩ := mul_add_inj hqv z.isLt hpq
    exact hh ⟨hall y (by simp), hall z (by simp)⟩

/-- The classes of a successful `colCheck`: every raw class passes `classOK`, no triple is listed
twice, the derived design is the set of listed triples, and it has one block per listed
triple. -/
theorem colCheck_spec {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {cls : List (List RawTriple)} (h : colCheck v bl x cls = true) :
    (∀ c ∈ cls, classOK v c = true) ∧ cls.flatten.Nodup ∧
      derivedBlocks (blockSet v bl) (pt v x) = tripleSet v cls ∧
      (tripleSet v cls).card = cls.flatten.length := by
  simp only [colCheck, Bool.and_eq_true, List.all_eq_true, beq_iff_eq] at h
  obtain ⟨hcls, hins⟩ := h
  obtain ⟨hLnd, hLmem⟩ := insertAll_zero_eq hins
  have hnd : cls.flatten.Nodup := List.Nodup.of_map _ hLnd
  have hfl : ∀ e ∈ cls.flatten, triOK v e = true := by
    intro e he
    obtain ⟨c, hc, hec⟩ := List.mem_flatten.mp he
    have h := hcls c hc
    simp only [classOK, Bool.and_eq_true, List.all_eq_true] at h
    exact h.1.2 e hec
  refine ⟨hcls, hnd, ?_, ?_⟩
  · ext T
    rw [mem_tripleSet, mem_derived_iff hq hx]
    constructor
    · rintro ⟨e, he, hk, rfl⟩
      have hk' : codeT v e ∈ cls.flatten.map (codeT v) := (hLmem _).mpr hk
      obtain ⟨e', he', hee⟩ := List.mem_map.mp hk'
      obtain rfl : e' = e := codeT_inj (hfl e' he') he hee
      exact ⟨e', he', rfl⟩
    · rintro ⟨e, he, rfl⟩
      have hk : codeT v e ∈ bl.filterMap (eraseCode v x) :=
        (hLmem _).mp (List.mem_map_of_mem he)
      exact ⟨e, hfl e he, hk, rfl⟩
  · rw [tripleSet, List.toFinset_card_of_nodup, List.length_map]
    exact List.Nodup.map_on (fun e he e' he' heq => tri_inj (hfl e he) (hfl e' he') heq) hnd

/-- The hole-free colour classes: their number is the number of hole-free raw classes. -/
theorem card_filter_classSet {cls : List (List RawTriple)} (hcls : ∀ c ∈ cls, classOK v c = true)
    (hnd : cls.flatten.Nodup) {hole : ℕ → Bool} {H : Finset (Fin v)}
    (hH : ∀ y : Fin v, y ∈ H ↔ hole y.val = true) :
    ((classSet v cls).filter fun P => ∀ T ∈ P, Disjoint T H).card =
      (cls.filter (holeFree hole)).length := by
  have hcard := (classes_spec hcls hnd).2.2
  rw [classSet] at hcard ⊢
  have hndmap : (cls.map fun c => (c.map (tri v)).toFinset).Nodup := by
    rw [List.card_toFinset] at hcard
    have := (List.dedup_sublist _).eq_of_length (by rw [hcard, List.length_map])
    rw [← this]
    exact List.nodup_dedup _
  have hkey : ∀ c ∈ cls, ((∀ T ∈ (c.map (tri v)).toFinset, Disjoint T H) ↔
      holeFree hole c = true) := by
    intro c hc
    have hok : ∀ e ∈ c, triOK v e = true := by
      have h := hcls c hc
      simp only [classOK, Bool.and_eq_true, List.all_eq_true] at h
      exact h.1.2
    simp only [holeFree, List.all_eq_true, pts, List.mem_cons, List.not_mem_nil, or_false,
      forall_eq_or_imp, forall_eq, Bool.not_eq_true', List.mem_toFinset, List.mem_map,
      forall_exists_index, and_imp, forall_apply_eq_imp_iff₂]
    refine forall₂_congr fun e he => ?_
    have hR := triOK_iff.mp (hok e he)
    rw [Finset.disjoint_left]
    constructor
    · intro hd
      have h1 := hd (a := pt v e.1) ((mem_tri (hok e he)).mpr (Or.inl (pt_val (by omega))))
      have h2 := hd (a := pt v e.2.1)
        ((mem_tri (hok e he)).mpr (Or.inr (Or.inl (pt_val (by omega)))))
      have h3 := hd (a := pt v e.2.2) ((mem_tri (hok e he)).mpr (Or.inr (Or.inr (pt_val hR.2.2))))
      rw [hH, pt_val (by omega), Bool.not_eq_true] at h1 h2
      rw [hH, pt_val hR.2.2, Bool.not_eq_true] at h3
      exact ⟨h1, h2, h3⟩
    · rintro ⟨h1, h2, h3⟩ y hy hyH
      rw [hH] at hyH
      rcases (mem_tri (hok e he)).mp hy with hy' | hy' | hy' <;> rw [hy'] at hyH <;> simp_all
  have hset : (cls.map fun c => (c.map (tri v)).toFinset).toFinset.filter
      (fun P => ∀ T ∈ P, Disjoint T H) =
      ((cls.filter (holeFree hole)).map fun c => (c.map (tri v)).toFinset).toFinset := by
    ext P
    simp only [Finset.mem_filter, List.mem_toFinset, List.mem_map, List.mem_filter]
    constructor
    · rintro ⟨⟨c, hc, rfl⟩, hP⟩
      exact ⟨c, ⟨hc, (hkey c hc).mp hP⟩, rfl⟩
    · rintro ⟨c, ⟨hc, hf⟩, rfl⟩
      exact ⟨⟨c, hc, rfl⟩, (hkey c hc).mpr hf⟩
  rw [hset, List.toFinset_card_of_nodup, List.length_map]
  exact hndmap.sublist (List.Sublist.map _ List.filter_sublist)

/-- **Soundness of the per-point checker.** -/
theorem pointCheck_sound {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {hole : ℕ → Bool} {r n : ℕ} {cls : List (List RawTriple)}
    (h : pointCheck v bl x hole r n cls = true) :
    IsColouring (derivedBlocks (blockSet v bl) (pt v x)) (classSet v cls) ∧
      (classSet v cls).card = r ∧ (derivedBlocks (blockSet v bl) (pt v x)).card = n ∧
      (∀ P : Finset (Fin v), P.card = 2 → pt v x ∉ P → (∃ y ∈ P, hole y.val = false) →
        ∃! T, T ∈ derivedBlocks (blockSet v bl) (pt v x) ∧ P ⊆ T) ∧
      (∀ P : Finset (Fin v), P.card = 2 → (∀ y ∈ P, hole y.val = true) →
        ∀ T ∈ derivedBlocks (blockSet v bl) (pt v x), ¬ P ⊆ T) := by
  simp only [pointCheck, Bool.and_eq_true, beq_iff_eq] at h
  obtain ⟨⟨⟨hcol, hhole⟩, hr⟩, hn⟩ := h
  obtain ⟨hc1, hc2⟩ := colouring_of_check hq hx hcol
  obtain ⟨-, -, hD, hcard⟩ := colCheck_spec hq hx hcol
  exact ⟨hc1, hc2.trans hr, by rw [hD, hcard, hn], holeCheck_sound hq hx hhole⟩

/-- **Soundness of the gc per-point checker**: in addition, exactly `s` colour classes avoid the
hole `H` named by `groupHole g x`. -/
theorem gcPointCheck_sound {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x g : ℕ}
    (hx : x < v) {r s n : ℕ} {cls : List (List RawTriple)}
    (h : gcPointCheck v g bl x r s n cls = true) {H : Finset (Fin v)}
    (hH : ∀ y : Fin v, y ∈ H ↔ groupHole g x y.val = true) :
    IsColouring (derivedBlocks (blockSet v bl) (pt v x)) (classSet v cls) ∧
      (classSet v cls).card = r ∧ (derivedBlocks (blockSet v bl) (pt v x)).card = n ∧
      (∀ P : Finset (Fin v), P.card = 2 → pt v x ∉ P → (∃ y ∈ P, groupHole g x y.val = false) →
        ∃! T, T ∈ derivedBlocks (blockSet v bl) (pt v x) ∧ P ⊆ T) ∧
      (∀ P : Finset (Fin v), P.card = 2 → (∀ y ∈ P, groupHole g x y.val = true) →
        ∀ T ∈ derivedBlocks (blockSet v bl) (pt v x), ¬ P ⊆ T) ∧
      ((classSet v cls).filter fun P => ∀ T ∈ P, Disjoint T H).card = s := by
  simp only [gcPointCheck, Bool.and_eq_true, beq_iff_eq] at h
  obtain ⟨hp, hs⟩ := h
  have hcol : colCheck v bl x cls = true := by
    simp only [pointCheck, Bool.and_eq_true] at hp
    exact hp.1.1.1
  obtain ⟨hcls, hnd, -, -⟩ := colCheck_spec hq hx hcol
  exact ⟨(pointCheck_sound hq hx hp).1, (pointCheck_sound hq hx hp).2.1,
    (pointCheck_sound hq hx hp).2.2.1, (pointCheck_sound hq hx hp).2.2.2.1,
    (pointCheck_sound hq hx hp).2.2.2.2, (card_filter_classSet hcls hnd hH).trans hs⟩

/-! ### Distinct blocks -/

theorem increasing_pairwise : ∀ {l : List ℕ}, increasing l = true → l.Pairwise (· < ·)
  | [], _ => List.Pairwise.nil
  | [_], _ => List.pairwise_singleton _ _
  | a :: b :: l, h => by
    simp only [increasing, Bool.and_eq_true, decide_eq_true_eq] at h
    have ih := increasing_pairwise h.2
    refine List.Pairwise.cons (fun c hc => ?_) ih
    rcases List.mem_cons.mp hc with rfl | hc
    · exact h.1
    · exact lt_trans h.1 (List.rel_of_pairwise_cons ih hc)

theorem quad_inj {b b' : RawQuad} (hb : quadOK v b = true) (hb' : quadOK v b' = true)
    (h : quad v b = quad v b') : b = b' := by
  have m : ∀ n, n < v → (n = b.1 ∨ n = b.2.1 ∨ n = b.2.2.1 ∨ n = b.2.2.2 ↔
      n = b'.1 ∨ n = b'.2.1 ∨ n = b'.2.2.1 ∨ n = b'.2.2.2) := by
    intro n hn
    have h1 := mem_quad hb (y := pt v n)
    have h2 := mem_quad hb' (y := pt v n)
    rw [pt_val hn] at h1 h2
    rw [← h1, ← h2, h]
  have hR := quadOK_iff.mp hb
  have hR' := quadOK_iff.mp hb'
  have m1 := (m b.1 (by omega)).mp (Or.inl rfl)
  have m2 := (m b.2.1 (by omega)).mp (Or.inr (Or.inl rfl))
  have m3 := (m b.2.2.1 (by omega)).mp (Or.inr (Or.inr (Or.inl rfl)))
  have m4 := (m b.2.2.2 (by omega)).mp (Or.inr (Or.inr (Or.inr rfl)))
  have m5 := (m b'.1 (by omega)).mpr (Or.inl rfl)
  have m6 := (m b'.2.1 (by omega)).mpr (Or.inr (Or.inl rfl))
  have m7 := (m b'.2.2.1 (by omega)).mpr (Or.inr (Or.inr (Or.inl rfl)))
  have m8 := (m b'.2.2.2 (by omega)).mpr (Or.inr (Or.inr (Or.inr rfl)))
  obtain ⟨a, b2, c, d⟩ := b
  obtain ⟨a', b2', c', d'⟩ := b'
  simp only at hR hR' m1 m2 m3 m4 m5 m6 m7 m8
  clear m h hb hb'
  have ha : a = a' := by clear m2 m3 m4 m6 m7 m8; omega
  subst ha
  have hb2 : b2 = b2' := by clear m1 m3 m4 m5 m7 m8; omega
  subst hb2
  have hc : c = c' := by clear m1 m2 m4 m5 m6 m8; omega
  subst hc
  have hd : d = d' := by clear m1 m2 m3 m5 m6 m7; omega
  subst hd
  rfl

/-- **Soundness of the block-list checker**: the blocks are `a < b < c < d < v`, and the block
set has `n` elements (the raw blocks name pairwise distinct 4-subsets). -/
theorem blockCheck_sound {bl : List RawQuad} {n : ℕ} (h : blockCheck v n bl = true) :
    (∀ b ∈ bl, quadOK v b = true) ∧ (blockSet v bl).card = n := by
  simp only [blockCheck, Bool.and_eq_true, List.all_eq_true, beq_iff_eq] at h
  obtain ⟨⟨hq, hinc⟩, hn⟩ := h
  refine ⟨hq, ?_⟩
  have hnd : (bl.map (code4 v)).Nodup := (increasing_pairwise hinc).imp (ne_of_lt)
  rw [blockSet, List.toFinset_card_of_nodup, List.length_map, hn]
  exact List.Nodup.map_on (fun b hb b' hb' heq => quad_inj (hq b hb) (hq b' hb') heq)
    (List.Nodup.of_map _ hnd)

end Soundness

end Mcd.Kernel
