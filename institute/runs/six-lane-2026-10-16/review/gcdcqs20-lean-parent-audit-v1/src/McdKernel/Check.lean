import McdKernel.Target

/-!
# Kernel-checkable certificates for an SQS with coloured derived designs, and for a coloured STS

Raw data are lists of raw blocks `(a, b, c, d)` and raw triples `(a, b, c)` of natural numbers
(lines of the raw certificate).  The semantic objects they name, on the points `Fin v`:

* `pt v n`: the residue of `n` modulo `v`; `quad v (a, b, c, d) = {pt v a, ..., pt v d}`;
  `tri v (a, b, c) = {pt v a, pt v b, pt v c}`;
* `blockSet v bl`: the set of all `quad v b`, `b` a listed block;
* `classSet v cls`: the set of classes, class `j` being the set of `tri v e` for `e` in raw
  class `j`; `tripleSet v cls`: the set of all listed triples `tri v e`.

The Boolean checkers use only `Nat` arithmetic, list recursion and bitwise operations on `Nat`,
which the Lean kernel evaluates on literals:

* `sqsCheck v bl`: every block satisfies `a < b < c < d < v`; inserting the codes
  `(p * v + q) * v + r` of the four sub-triples `p < q < r` of every block one by one into a
  bitmask never meets a bit already set, and ends at the mask of the codes of all triples
  `p < q < r < v`.  (`isSQS_of_check`: every 3-subset lies in exactly one block.)
* `classOK v c`: the raw class is nonempty, every triple satisfies `a < b < c < v`, and inserting
  its points one by one into a bitmask never meets a bit already set (pairwise disjoint).
* `colCheck v bl x cls`: every class passes `classOK`, and inserting the codes of all listed
  triples never meets a set bit and ends at the mask of the codes of `X \ {x}` over the listed
  blocks `X ∋ x`.  (`colouring_of_check`: the classes form a colouring of the derived design at
  `x`, with as many colour classes as raw classes.)
* `stsColCheck v cls`: every class passes `classOK`, and inserting the codes `p * v + q` of the
  three pairs of every listed triple never meets a set bit and ends at the mask of all pairs
  `p < q < v`.  (`sts_of_check`: the listed triples form an STS on `Fin v` and the classes a
  colouring of it.)
-/

namespace Mcd.Kernel

/-- A raw block `(a, b, c, d)`: one block line `a b c d` of the raw certificate. -/
abbrev RawQuad := ℕ × ℕ × ℕ × ℕ

/-- A raw triple `(a, b, c)`: one triple line `a b c` of the raw certificate. -/
abbrev RawTriple := ℕ × ℕ × ℕ

/-! ## The semantic objects named by raw data -/

section Semantics

variable (v : ℕ) [NeZero v]

/-- The residue of the raw number `n` modulo `v`, as a point of `Fin v`. -/
def pt (n : ℕ) : Fin v := ⟨n % v, Nat.mod_lt _ (Nat.pos_of_neZero v)⟩

/-- The point set named by the raw block `(a, b, c, d)`. -/
def quad (b : RawQuad) : Finset (Fin v) := {pt v b.1, pt v b.2.1, pt v b.2.2.1, pt v b.2.2.2}

/-- The point set named by the raw triple `(a, b, c)`. -/
def tri (e : RawTriple) : Finset (Fin v) := {pt v e.1, pt v e.2.1, pt v e.2.2}

/-- The block set: all listed blocks.  (`blockSet`, `tripleSet` and `classSet` are irreducible,
so that elaboration never evaluates them on concrete data; proofs use their equation lemmas.) -/
@[irreducible] def blockSet (bl : List RawQuad) : Finset (Finset (Fin v)) :=
  (bl.map (quad v)).toFinset

/-- The set of all listed triples, over all raw classes. -/
@[irreducible] def tripleSet (cls : List (List RawTriple)) : Finset (Finset (Fin v)) :=
  (cls.flatten.map (tri v)).toFinset

/-- The colour classes: class `j` is the set of the triples listed in raw class `j`. -/
@[irreducible] def classSet (cls : List (List RawTriple)) : Finset (Finset (Finset (Fin v))) :=
  (cls.map fun c => (c.map (tri v)).toFinset).toFinset

end Semantics

/-! ## The Boolean checkers -/

section Checker

/-- Insert the codes of `l` one by one into the bitmask `m`; `none` as soon as a bit is already
set. -/
def insertAll : List ℕ → ℕ → Option ℕ
  | [], m => some m
  | c :: l, m => if m.testBit c then none else insertAll l (m ||| 2 ^ c)

/-- Bitwise union of a list of naturals. -/
def orAll (l : List ℕ) : ℕ := l.foldl (· ||| ·) 0

/-- `a < b < c < d < v`. -/
def quadOK (v : ℕ) (b : RawQuad) : Bool :=
  decide (b.1 < b.2.1) && decide (b.2.1 < b.2.2.1) && decide (b.2.2.1 < b.2.2.2) &&
    decide (b.2.2.2 < v)

/-- `a < b < c < v`. -/
def triOK (v : ℕ) (e : RawTriple) : Bool :=
  decide (e.1 < e.2.1) && decide (e.2.1 < e.2.2) && decide (e.2.2 < v)

/-- The three raw points of a raw triple. -/
def pts (e : RawTriple) : List ℕ := [e.1, e.2.1, e.2.2]

/-- The code of an ordered triple of numbers. -/
def code3 (v a b c : ℕ) : ℕ := (a * v + b) * v + c

/-- The code of a raw triple. -/
def codeT (v : ℕ) (e : RawTriple) : ℕ := code3 v e.1 e.2.1 e.2.2

/-- The codes of the four sub-triples of a raw block `a < b < c < d`. -/
def subCodes (v : ℕ) (b : RawQuad) : List ℕ :=
  [code3 v b.1 b.2.1 b.2.2.1, code3 v b.1 b.2.1 b.2.2.2, code3 v b.1 b.2.2.1 b.2.2.2,
    code3 v b.2.1 b.2.2.1 b.2.2.2]

/-- The codes of all triples `a < b < c < v`. -/
def tripleList (v : ℕ) : List ℕ :=
  (List.range v).flatMap fun a => (List.range' (a + 1) (v - (a + 1))).flatMap fun b =>
    (List.range' (b + 1) (v - (b + 1))).map fun c => code3 v a b c

/-- Bits of all triples `a < b < c < v`. -/
def allTripleMask (v : ℕ) : ℕ := orAll ((tripleList v).map (2 ^ ·))

/-- The SQS checker. -/
def sqsCheck (v : ℕ) (bl : List RawQuad) : Bool :=
  bl.all (quadOK v) && insertAll (bl.flatMap (subCodes v)) 0 == some (allTripleMask v)

/-- The code of `X \ {x}` for a raw block `X` containing `x`; `none` if `x ∉ X`. -/
def eraseCode (v x : ℕ) (b : RawQuad) : Option ℕ :=
  if b.1 = x then some (code3 v b.2.1 b.2.2.1 b.2.2.2)
  else if b.2.1 = x then some (code3 v b.1 b.2.2.1 b.2.2.2)
  else if b.2.2.1 = x then some (code3 v b.1 b.2.1 b.2.2.2)
  else if b.2.2.2 = x then some (code3 v b.1 b.2.1 b.2.2.1)
  else none

/-- Bits of the codes of the derived triples `X \ {x}`, `x ∈ X` a listed block. -/
def derivedMask (v : ℕ) (bl : List RawQuad) (x : ℕ) : ℕ :=
  orAll ((bl.filterMap (eraseCode v x)).map (2 ^ ·))

/-- A raw class: nonempty, triples `a < b < c < v`, pairwise disjoint. -/
def classOK (v : ℕ) (c : List RawTriple) : Bool :=
  !c.isEmpty && c.all (triOK v) && (insertAll (c.flatMap pts) 0).isSome

/-- The colouring checker at the point `x`. -/
def colCheck (v : ℕ) (bl : List RawQuad) (x : ℕ) (cls : List (List RawTriple)) : Bool :=
  cls.all (classOK v) && insertAll (cls.flatten.map (codeT v)) 0 == some (derivedMask v bl x)

/-- The codes `p * v + q` of the three pairs of a raw triple `a < b < c`. -/
def pairCodes (v : ℕ) (e : RawTriple) : List ℕ :=
  [e.1 * v + e.2.1, e.1 * v + e.2.2, e.2.1 * v + e.2.2]

/-- The codes of all pairs `p < q < v`. -/
def pairList (v : ℕ) : List ℕ :=
  (List.range v).flatMap fun p => (List.range' (p + 1) (v - (p + 1))).map fun q => p * v + q

/-- Bits of all pairs `p < q < v`. -/
def allPairMask (v : ℕ) : ℕ := orAll ((pairList v).map (2 ^ ·))

/-- The coloured-STS checker. -/
def stsColCheck (v : ℕ) (cls : List (List RawTriple)) : Bool :=
  cls.all (classOK v) && insertAll (cls.flatten.flatMap (pairCodes v)) 0 == some (allPairMask v)

end Checker

/-! ## List, bit and arithmetic lemmas -/

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

theorem nodup_of_insertAll_isSome {l : List ℕ} (h : (insertAll l 0).isSome = true) : l.Nodup := by
  obtain ⟨m, hm⟩ := Option.isSome_iff_exists.mp h
  exact (insertAll_spec l 0 m hm).1

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

theorem code3_inj {v a b c a' b' c' : ℕ} (hb : b < v) (hc : c < v) (hb' : b' < v) (hc' : c' < v)
    (h : code3 v a b c = code3 v a' b' c') : a = a' ∧ b = b' ∧ c = c' := by
  unfold code3 at h
  obtain ⟨h1, h2⟩ := mul_add_inj hc hc' h
  obtain ⟨h3, h4⟩ := mul_add_inj hb hb' h1
  exact ⟨h3, h4, h2⟩

theorem mem_tripleList {v k : ℕ} :
    k ∈ tripleList v ↔ ∃ a b c, a < b ∧ b < c ∧ c < v ∧ code3 v a b c = k := by
  simp only [tripleList, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_range'_1]
  constructor
  · rintro ⟨a, ha, b, ⟨hb1, hb2⟩, c, ⟨hc1, hc2⟩, rfl⟩
    exact ⟨a, b, c, by omega, by omega, by omega, rfl⟩
  · rintro ⟨a, b, c, hab, hbc, hcv, rfl⟩
    exact ⟨a, by omega, b, ⟨by omega, by omega⟩, c, ⟨by omega, by omega⟩, rfl⟩

theorem mem_pairList {v k : ℕ} : k ∈ pairList v ↔ ∃ p q, p < q ∧ q < v ∧ p * v + q = k := by
  simp only [pairList, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_range'_1]
  constructor
  · rintro ⟨p, hp, q, ⟨hq1, hq2⟩, rfl⟩
    exact ⟨p, q, by omega, by omega, rfl⟩
  · rintro ⟨p, q, hpq, hqv, rfl⟩
    exact ⟨p, by omega, q, ⟨by omega, by omega⟩, rfl⟩

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
      nodup_of_nodup_flatMap (fun a ha => hne a (List.mem_cons_of_mem _ ha)) hnd'⟩
    obtain ⟨c, hc⟩ := List.exists_mem_of_ne_nil _ (hne x List.mem_cons_self)
    exact hdisj c hc c (List.mem_flatMap.mpr ⟨x, hx, hc⟩) rfl

/-- Every 3-subset of `Fin v` is `{a, b, c}` with `a < b < c`. -/
theorem exists_sorted_three {v : ℕ} {T : Finset (Fin v)} (h : T.card = 3) :
    ∃ a b c : Fin v, a.val < b.val ∧ b.val < c.val ∧ T = {a, b, c} := by
  obtain ⟨x, y, z, hxy, hxz, hyz, rfl⟩ := Finset.card_eq_three.mp h
  have hxy' := Fin.val_ne_of_ne hxy
  have hxz' := Fin.val_ne_of_ne hxz
  have hyz' := Fin.val_ne_of_ne hyz
  have hset : ∀ a b c : Fin v, ({a, b, c} : Finset (Fin v)) = {b, a, c} ∧
      ({a, b, c} : Finset (Fin v)) = {a, c, b} ∧ ({a, b, c} : Finset (Fin v)) = {c, a, b} ∧
      ({a, b, c} : Finset (Fin v)) = {b, c, a} ∧ ({a, b, c} : Finset (Fin v)) = {c, b, a} := by
    intro a b c
    refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;>
      · ext w
        simp only [Finset.mem_insert, Finset.mem_singleton]
        tauto
  rcases Nat.lt_or_gt_of_ne hxy' with h1 | h1 <;> rcases Nat.lt_or_gt_of_ne hxz' with h2 | h2 <;>
    rcases Nat.lt_or_gt_of_ne hyz' with h3 | h3
  · exact ⟨x, y, z, h1, h3, rfl⟩
  · exact ⟨x, z, y, h2, h3, (hset x y z).2.1⟩
  · exact absurd h3 (by omega)
  · exact ⟨z, x, y, h2, h1, (hset x y z).2.2.1⟩
  · exact ⟨y, x, z, h1, h2, (hset x y z).1⟩
  · exact absurd h3 (by omega)
  · exact ⟨y, z, x, h3, h2, (hset x y z).2.2.2.1⟩
  · exact ⟨z, y, x, h3, h1, (hset x y z).2.2.2.2⟩

end Lemmas

/-! ## Soundness -/

section Soundness

variable {v : ℕ} [NeZero v]

theorem pt_val {n : ℕ} (h : n < v) : (pt v n).val = n := Nat.mod_eq_of_lt h

theorem pt_val_self (y : Fin v) : pt v y.val = y := Fin.ext (Nat.mod_eq_of_lt y.isLt)

omit [NeZero v] in
theorem quadOK_iff {b : RawQuad} :
    quadOK v b = true ↔ b.1 < b.2.1 ∧ b.2.1 < b.2.2.1 ∧ b.2.2.1 < b.2.2.2 ∧ b.2.2.2 < v := by
  simp [quadOK, and_assoc]

omit [NeZero v] in
theorem triOK_iff {e : RawTriple} :
    triOK v e = true ↔ e.1 < e.2.1 ∧ e.2.1 < e.2.2 ∧ e.2.2 < v := by
  simp [triOK, and_assoc]

theorem mem_quad {b : RawQuad} (hb : quadOK v b = true) {y : Fin v} :
    y ∈ quad v b ↔ y.val = b.1 ∨ y.val = b.2.1 ∨ y.val = b.2.2.1 ∨ y.val = b.2.2.2 := by
  obtain ⟨h1, h2, h3, h4⟩ := quadOK_iff.mp hb
  simp only [quad, Finset.mem_insert, Finset.mem_singleton, Fin.ext_iff,
    pt_val (show b.1 < v by omega), pt_val (show b.2.1 < v by omega),
    pt_val (show b.2.2.1 < v by omega), pt_val h4]

theorem mem_tri {e : RawTriple} (he : triOK v e = true) {y : Fin v} :
    y ∈ tri v e ↔ y.val = e.1 ∨ y.val = e.2.1 ∨ y.val = e.2.2 := by
  obtain ⟨h1, h2, h3⟩ := triOK_iff.mp he
  simp only [tri, Finset.mem_insert, Finset.mem_singleton, Fin.ext_iff,
    pt_val (show e.1 < v by omega), pt_val (show e.2.1 < v by omega), pt_val h3]

theorem quad_card {b : RawQuad} (hb : quadOK v b = true) : (quad v b).card = 4 := by
  obtain ⟨h1, h2, h3, h4⟩ := quadOK_iff.mp hb
  have hv1 : (pt v b.1).val = b.1 := pt_val (by omega)
  have hv2 : (pt v b.2.1).val = b.2.1 := pt_val (by omega)
  have hv3 : (pt v b.2.2.1).val = b.2.2.1 := pt_val (by omega)
  have hv4 : (pt v b.2.2.2).val = b.2.2.2 := pt_val h4
  rw [quad, Finset.card_insert_of_notMem, Finset.card_insert_of_notMem, Finset.card_pair]
  · intro h
    have := congrArg Fin.val h
    omega
  · simp only [Finset.mem_insert, Finset.mem_singleton, Fin.ext_iff]
    omega
  · simp only [Finset.mem_insert, Finset.mem_singleton, Fin.ext_iff]
    omega

theorem tri_card {e : RawTriple} (he : triOK v e = true) : (tri v e).card = 3 := by
  obtain ⟨h1, h2, h3⟩ := triOK_iff.mp he
  rw [Finset.card_eq_three]
  refine ⟨pt v e.1, pt v e.2.1, pt v e.2.2, ?_, ?_, ?_, rfl⟩ <;>
    simp only [ne_eq, Fin.ext_iff, pt_val (show e.1 < v by omega),
      pt_val (show e.2.1 < v by omega), pt_val h3] <;> omega

theorem tri_inj {e e' : RawTriple} (he : triOK v e = true) (he' : triOK v e' = true)
    (h : tri v e = tri v e') : e = e' := by
  have hR := triOK_iff.mp he
  have hR' := triOK_iff.mp he'
  have m : ∀ n, n < v → (n = e.1 ∨ n = e.2.1 ∨ n = e.2.2 ↔ n = e'.1 ∨ n = e'.2.1 ∨ n = e'.2.2) := by
    intro n hn
    have h1 := mem_tri he (y := pt v n)
    have h2 := mem_tri he' (y := pt v n)
    rw [pt_val hn] at h1 h2
    rw [← h1, ← h2, h]
  have m1 := (m e.1 (by omega)).mp (Or.inl rfl)
  have m2 := (m e.2.1 (by omega)).mp (Or.inr (Or.inl rfl))
  have m3 := (m e.2.2 (by omega)).mp (Or.inr (Or.inr rfl))
  have m4 := (m e'.1 (by omega)).mpr (Or.inl rfl)
  have m5 := (m e'.2.1 (by omega)).mpr (Or.inr (Or.inl rfl))
  have m6 := (m e'.2.2 (by omega)).mpr (Or.inr (Or.inr rfl))
  obtain ⟨a, b, c⟩ := e
  obtain ⟨a', b', c'⟩ := e'
  simp only at *
  have ha : a = a' := by omega
  have hb : b = b' := by omega
  have hc : c = c' := by omega
  rw [ha, hb, hc]

theorem ne_pt_iff {x : ℕ} (hx : x < v) (y : Fin v) : y ≠ pt v x ↔ y.val ≠ x := by
  rw [Ne, Fin.ext_iff, pt_val hx]

/-! ### The SQS -/

theorem mem_blockSet {bl : List RawQuad} {X : Finset (Fin v)} :
    X ∈ blockSet v bl ↔ ∃ b ∈ bl, quad v b = X := by
  rw [blockSet]
  simp only [List.mem_toFinset, List.mem_map]

/-- Three points `a < b < c` of a raw block give the code of one of its four sub-triples. -/
theorem subCode_of_subset {b : RawQuad} (hb : quadOK v b = true) {a1 a2 a3 : Fin v}
    (h12 : a1.val < a2.val) (h23 : a2.val < a3.val)
    (hsub : ({a1, a2, a3} : Finset (Fin v)) ⊆ quad v b) :
    code3 v a1.val a2.val a3.val ∈ subCodes v b := by
  have hR := quadOK_iff.mp hb
  have m1 := (mem_quad hb).mp (hsub (Finset.mem_insert_self a1 _))
  have m2 := (mem_quad hb).mp (hsub (Finset.mem_insert_of_mem (Finset.mem_insert_self a2 _)))
  have m3 := (mem_quad hb).mp
    (hsub (Finset.mem_insert_of_mem (Finset.mem_insert_of_mem (Finset.mem_singleton_self a3))))
  simp only [subCodes, List.mem_cons, List.not_mem_nil, or_false]
  rcases m1 with h1 | h1 | h1 | h1 <;> rcases m2 with h2 | h2 | h2 | h2 <;>
    rcases m3 with h3 | h3 | h3 | h3 <;>
    first
    | (exfalso; omega)
    | simp [h1, h2, h3]

omit [NeZero v] in
theorem quadOK_of_sqsCheck {bl : List RawQuad} (h : sqsCheck v bl = true) :
    ∀ b ∈ bl, quadOK v b = true := by
  simp only [sqsCheck, Bool.and_eq_true, List.all_eq_true] at h
  exact h.1

/-- **Soundness of the SQS checker.** -/
theorem isSQS_of_check {bl : List RawQuad} (h : sqsCheck v bl = true) : IsSQS (blockSet v bl) := by
  simp only [sqsCheck, Bool.and_eq_true, List.all_eq_true, beq_iff_eq] at h
  obtain ⟨hq, hins⟩ := h
  obtain ⟨hnd, hmem⟩ := insertAll_zero_eq hins
  refine ⟨?_, ?_⟩
  · intro X hX
    obtain ⟨b, hb, rfl⟩ := mem_blockSet.mp hX
    exact quad_card (hq b hb)
  · intro T hT
    obtain ⟨a1, a2, a3, h12, h23, rfl⟩ := exists_sorted_three hT
    have hk : code3 v a1.val a2.val a3.val ∈ tripleList v :=
      mem_tripleList.mpr ⟨_, _, _, h12, h23, a3.isLt, rfl⟩
    obtain ⟨b, hb, hkb⟩ := List.mem_flatMap.mp ((hmem _).mpr hk)
    have hR := quadOK_iff.mp (hq b hb)
    have hsub : ({a1, a2, a3} : Finset (Fin v)) ⊆ quad v b := by
      simp only [subCodes, List.mem_cons, List.not_mem_nil, or_false] at hkb
      intro y hy
      rw [mem_quad (hq b hb)]
      simp only [Finset.mem_insert, Finset.mem_singleton] at hy
      rcases hkb with h' | h' | h' | h' <;>
        obtain ⟨e1, e2, e3⟩ := code3_inj a2.isLt a3.isLt (by omega) (by omega) h' <;>
        rcases hy with rfl | rfl | rfl <;> omega
    refine ⟨quad v b, ⟨mem_blockSet.mpr ⟨b, hb, rfl⟩, hsub⟩, ?_⟩
    rintro Y ⟨hY, hTY⟩
    obtain ⟨b', hb', rfl⟩ := mem_blockSet.mp hY
    have h1 := subCode_of_subset (hq b hb) h12 h23 hsub
    have h2 := subCode_of_subset (hq b' hb') h12 h23 hTY
    rw [eq_of_mem_of_nodup_flatMap hnd hb' hb h2 h1]

/-! ### Colour classes -/

theorem mem_tripleSet {cls : List (List RawTriple)} {T : Finset (Fin v)} :
    T ∈ tripleSet v cls ↔ ∃ e ∈ cls.flatten, tri v e = T := by
  rw [tripleSet]
  simp only [List.mem_toFinset, List.mem_map]

theorem mem_classSet {cls : List (List RawTriple)} {P : Finset (Finset (Fin v))} :
    P ∈ classSet v cls ↔ ∃ c ∈ cls, (c.map (tri v)).toFinset = P := by
  rw [classSet]
  simp only [List.mem_toFinset, List.mem_map]

/-- Classes passing `classOK` whose concatenation lists no triple twice: each is a nonempty set
of pairwise disjoint listed triples, every listed triple lies in exactly one class, and there
are as many classes as raw classes. -/
theorem classes_spec {cls : List (List RawTriple)} (hcls : ∀ c ∈ cls, classOK v c = true)
    (hnd : cls.flatten.Nodup) :
    (∀ P ∈ classSet v cls, P.Nonempty ∧ P ⊆ tripleSet v cls ∧
      ∀ T ∈ P, ∀ T' ∈ P, T ≠ T' → Disjoint T T') ∧
    (∀ T ∈ tripleSet v cls, ∃! P, P ∈ classSet v cls ∧ T ∈ P) ∧
    (classSet v cls).card = cls.length := by
  have hOK : ∀ c ∈ cls, c ≠ [] ∧ (∀ e ∈ c, triOK v e = true) ∧ (c.flatMap pts).Nodup := by
    intro c hc
    have h := hcls c hc
    simp only [classOK, Bool.and_eq_true, Bool.not_eq_true', List.isEmpty_eq_false_iff,
      List.all_eq_true] at h
    exact ⟨h.1.1, h.1.2, nodup_of_insertAll_isSome h.2⟩
  have hfl : ∀ e ∈ cls.flatten, triOK v e = true := by
    intro e he
    obtain ⟨c, hc, hec⟩ := List.mem_flatten.mp he
    exact (hOK c hc).2.1 e hec
  have hnd' : (cls.flatMap id).Nodup := by rwa [List.flatMap_id]
  have hclsnd : cls.Nodup := nodup_of_nodup_flatMap (f := id) (fun c hc => (hOK c hc).1) hnd'
  -- a triple determines its raw class
  have hcl_unique : ∀ c ∈ cls, ∀ c' ∈ cls, ∀ e ∈ c, ∀ e' ∈ c', tri v e = tri v e' → c = c' := by
    intro c hc c' hc' e he e' he' heq
    have hfe := List.mem_flatten.mpr ⟨c, hc, he⟩
    have hfe' := List.mem_flatten.mpr ⟨c', hc', he'⟩
    obtain rfl : e = e' := tri_inj (hfl e hfe) (hfl e' hfe') heq
    exact eq_of_mem_of_nodup_flatMap (f := id) hnd' hc hc' he he'
  refine ⟨?_, ?_, ?_⟩
  · intro P hP
    obtain ⟨c, hc, rfl⟩ := mem_classSet.mp hP
    obtain ⟨hne, hok, hpts⟩ := hOK c hc
    refine ⟨?_, ?_, ?_⟩
    · obtain ⟨e, he⟩ := List.exists_mem_of_ne_nil c hne
      exact ⟨tri v e, List.mem_toFinset.mpr (List.mem_map_of_mem he)⟩
    · intro T hT
      obtain ⟨e, he, rfl⟩ := List.mem_map.mp (List.mem_toFinset.mp hT)
      exact mem_tripleSet.mpr ⟨e, List.mem_flatten.mpr ⟨c, hc, he⟩, rfl⟩
    · intro T hT T' hT' hne'
      obtain ⟨e, he, rfl⟩ := List.mem_map.mp (List.mem_toFinset.mp hT)
      obtain ⟨e', he', rfl⟩ := List.mem_map.mp (List.mem_toFinset.mp hT')
      rw [Finset.disjoint_left]
      intro y hy hy'
      have hy1 : y.val ∈ pts e := by
        rw [mem_tri (hok e he)] at hy
        simp only [pts, List.mem_cons, List.not_mem_nil, or_false]
        exact hy
      have hy2 : y.val ∈ pts e' := by
        rw [mem_tri (hok e' he')] at hy'
        simp only [pts, List.mem_cons, List.not_mem_nil, or_false]
        exact hy'
      exact hne' (congrArg (tri v) (eq_of_mem_of_nodup_flatMap hpts he he' hy1 hy2))
  · intro T hT
    obtain ⟨e, he, rfl⟩ := mem_tripleSet.mp hT
    obtain ⟨c, hc, hec⟩ := List.mem_flatten.mp he
    refine ⟨(c.map (tri v)).toFinset,
      ⟨mem_classSet.mpr ⟨c, hc, rfl⟩, List.mem_toFinset.mpr (List.mem_map_of_mem hec)⟩, ?_⟩
    rintro P ⟨hP, hTP⟩
    obtain ⟨c', hc', rfl⟩ := mem_classSet.mp hP
    obtain ⟨e', he', heq⟩ := List.mem_map.mp (List.mem_toFinset.mp hTP)
    rw [hcl_unique c' hc' c hc e' he' e hec heq]
  · rw [classSet, List.toFinset_card_of_nodup, List.length_map]
    refine List.Nodup.map_on ?_ hclsnd
    intro c hc c' hc' heq
    obtain ⟨e, he⟩ := List.exists_mem_of_ne_nil c (hOK c hc).1
    have hmem : tri v e ∈ (c'.map (tri v)).toFinset := by
      rw [← heq]
      exact List.mem_toFinset.mpr (List.mem_map_of_mem he)
    obtain ⟨e', he', heq'⟩ := List.mem_map.mp (List.mem_toFinset.mp hmem)
    exact hcl_unique c hc c' hc' e he e' he' heq'.symm

theorem isColouring_of_classes {cls : List (List RawTriple)} {D : Finset (Finset (Fin v))}
    (hcls : ∀ c ∈ cls, classOK v c = true) (hnd : cls.flatten.Nodup) (hD : tripleSet v cls = D) :
    IsColouring D (classSet v cls) ∧ (classSet v cls).card = cls.length := by
  obtain ⟨h1, h2, h3⟩ := classes_spec hcls hnd
  subst hD
  exact ⟨⟨fun P hP => ⟨(h1 P hP).1, (h1 P hP).2.1, (h1 P hP).2.2⟩, h2⟩, h3⟩

/-! ### Colourings of derived designs -/

theorem eraseCode_spec {b : RawQuad} (hb : quadOK v b = true) {x : ℕ} (hx : x < v) :
    (eraseCode v x b = none ∧ pt v x ∉ quad v b) ∨
    ∃ e : RawTriple, eraseCode v x b = some (codeT v e) ∧ triOK v e = true ∧
      pt v x ∈ quad v b ∧ (quad v b).erase (pt v x) = tri v e := by
  have hR := quadOK_iff.mp hb
  unfold eraseCode
  split_ifs with h1 h2 h3 h4
  · right
    have he : triOK v (b.2.1, b.2.2.1, b.2.2.2) = true := by
      rw [triOK_iff]
      dsimp only
      omega
    refine ⟨(b.2.1, b.2.2.1, b.2.2.2), rfl, he, ?_, ?_⟩
    · rw [mem_quad hb, pt_val hx]
      omega
    · ext y
      rw [Finset.mem_erase, mem_quad hb, mem_tri he, ne_pt_iff hx]
      dsimp only
      constructor <;> intro h <;> omega
  · right
    have he : triOK v (b.1, b.2.2.1, b.2.2.2) = true := by
      rw [triOK_iff]
      dsimp only
      omega
    refine ⟨(b.1, b.2.2.1, b.2.2.2), rfl, he, ?_, ?_⟩
    · rw [mem_quad hb, pt_val hx]
      omega
    · ext y
      rw [Finset.mem_erase, mem_quad hb, mem_tri he, ne_pt_iff hx]
      dsimp only
      constructor <;> intro h <;> omega
  · right
    have he : triOK v (b.1, b.2.1, b.2.2.2) = true := by
      rw [triOK_iff]
      dsimp only
      omega
    refine ⟨(b.1, b.2.1, b.2.2.2), rfl, he, ?_, ?_⟩
    · rw [mem_quad hb, pt_val hx]
      omega
    · ext y
      rw [Finset.mem_erase, mem_quad hb, mem_tri he, ne_pt_iff hx]
      dsimp only
      constructor <;> intro h <;> omega
  · right
    have he : triOK v (b.1, b.2.1, b.2.2.1) = true := by
      rw [triOK_iff]
      dsimp only
      omega
    refine ⟨(b.1, b.2.1, b.2.2.1), rfl, he, ?_, ?_⟩
    · rw [mem_quad hb, pt_val hx]
      omega
    · ext y
      rw [Finset.mem_erase, mem_quad hb, mem_tri he, ne_pt_iff hx]
      dsimp only
      constructor <;> intro h <;> omega
  · left
    refine ⟨rfl, ?_⟩
    rw [mem_quad hb, pt_val hx]
    omega

omit [NeZero v] in
theorem codeT_inj {e e' : RawTriple} (he : triOK v e = true) (he' : triOK v e' = true)
    (h : codeT v e = codeT v e') : e = e' := by
  have hR := triOK_iff.mp he
  have hR' := triOK_iff.mp he'
  obtain ⟨h1, h2, h3⟩ := code3_inj (by omega) hR.2.2 (by omega) hR'.2.2 h
  obtain ⟨a, b, c⟩ := e
  obtain ⟨a', b', c'⟩ := e'
  simp only at h1 h2 h3
  rw [h1, h2, h3]

/-- **Soundness of the colouring checker at `x`.** -/
theorem colouring_of_check {bl : List RawQuad} (hq : ∀ b ∈ bl, quadOK v b = true) {x : ℕ}
    (hx : x < v) {cls : List (List RawTriple)} (h : colCheck v bl x cls = true) :
    IsColouring (derivedBlocks (blockSet v bl) (pt v x)) (classSet v cls) ∧
      (classSet v cls).card = cls.length := by
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
  refine isColouring_of_classes hcls hnd ?_
  ext T
  rw [mem_tripleSet]
  simp only [derivedBlocks, Finset.mem_image, Finset.mem_filter]
  constructor
  · rintro ⟨e, he, rfl⟩
    have hk : codeT v e ∈ bl.filterMap (eraseCode v x) :=
      (hLmem _).mp (List.mem_map_of_mem he)
    obtain ⟨b, hb, hbk⟩ := List.mem_filterMap.mp hk
    rcases eraseCode_spec (hq b hb) hx with ⟨hnone, -⟩ | ⟨e', hsome, he', hxb, herase⟩
    · rw [hnone] at hbk
      exact absurd hbk (by simp)
    · rw [hsome, Option.some.injEq] at hbk
      obtain rfl : e' = e := codeT_inj he' (hfl e he) hbk
      exact ⟨quad v b, ⟨mem_blockSet.mpr ⟨b, hb, rfl⟩, hxb⟩, herase⟩
  · rintro ⟨X, ⟨hX, hxX⟩, rfl⟩
    obtain ⟨b, hb, rfl⟩ := mem_blockSet.mp hX
    rcases eraseCode_spec (hq b hb) hx with ⟨-, hnot⟩ | ⟨e', hsome, he', -, herase⟩
    · exact absurd hxX hnot
    · have hk : codeT v e' ∈ cls.flatten.map (codeT v) :=
        (hLmem _).mpr (List.mem_filterMap.mpr ⟨b, hb, hsome⟩)
      obtain ⟨e, he, hee⟩ := List.mem_map.mp hk
      obtain rfl : e = e' := codeT_inj (hfl e he) he' hee
      exact ⟨e, he, herase.symm⟩

/-! ### Coloured Steiner triple systems -/

/-- Two points `y < z` of a listed triple give the code of one of its three pairs. -/
theorem pairCode_mem {e : RawTriple} (he : triOK v e = true) {y z : Fin v} (hyz : y.val < z.val)
    (hy : y ∈ tri v e) (hz : z ∈ tri v e) : y.val * v + z.val ∈ pairCodes v e := by
  have hR := triOK_iff.mp he
  rw [mem_tri he] at hy hz
  simp only [pairCodes, List.mem_cons, List.not_mem_nil, or_false]
  rcases hy with hy | hy | hy <;> rcases hz with hz | hz | hz <;>
    first
    | (exfalso; omega)
    | simp [hy, hz]

/-- **Soundness of the coloured-STS checker.** -/
theorem sts_of_check {cls : List (List RawTriple)} (h : stsColCheck v cls = true) :
    IsSTS (tripleSet v cls) ∧ IsColouring (tripleSet v cls) (classSet v cls) ∧
      (classSet v cls).card = cls.length := by
  simp only [stsColCheck, Bool.and_eq_true, List.all_eq_true, beq_iff_eq] at h
  obtain ⟨hcls, hins⟩ := h
  obtain ⟨hPnd, hPmem⟩ := insertAll_zero_eq hins
  have hnd : cls.flatten.Nodup :=
    nodup_of_nodup_flatMap (f := pairCodes v) (fun e _ => by simp [pairCodes]) hPnd
  have hfl : ∀ e ∈ cls.flatten, triOK v e = true := by
    intro e he
    obtain ⟨c, hc, hec⟩ := List.mem_flatten.mp he
    have h := hcls c hc
    simp only [classOK, Bool.and_eq_true, List.all_eq_true] at h
    exact h.1.2 e hec
  refine ⟨⟨?_, ?_⟩, isColouring_of_classes hcls hnd rfl⟩
  · intro T hT
    obtain ⟨e, he, rfl⟩ := mem_tripleSet.mp hT
    exact tri_card (hfl e he)
  · -- every 2-subset lies in exactly one listed triple
    have key : ∀ y z : Fin v, y.val < z.val →
        ∃! T, T ∈ tripleSet v cls ∧ ({y, z} : Finset (Fin v)) ⊆ T := by
      intro y z hyz
      have hk : y.val * v + z.val ∈ pairList v := mem_pairList.mpr ⟨y.val, z.val, hyz, z.isLt, rfl⟩
      obtain ⟨e, he, hke⟩ := List.mem_flatMap.mp ((hPmem _).mpr hk)
      have hR := triOK_iff.mp (hfl e he)
      have hyz_e : y ∈ tri v e ∧ z ∈ tri v e := by
        rw [mem_tri (hfl e he), mem_tri (hfl e he)]
        simp only [pairCodes, List.mem_cons, List.not_mem_nil, or_false] at hke
        rcases hke with h' | h' | h'
        · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
          exact ⟨Or.inl h1, Or.inr (Or.inl h2)⟩
        · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
          exact ⟨Or.inl h1, Or.inr (Or.inr h2)⟩
        · obtain ⟨h1, h2⟩ := mul_add_inj z.isLt (by omega) h'
          exact ⟨Or.inr (Or.inl h1), Or.inr (Or.inr h2)⟩
      have hsub : ({y, z} : Finset (Fin v)) ⊆ tri v e := by
        intro w hw
        simp only [Finset.mem_insert, Finset.mem_singleton] at hw
        rcases hw with rfl | rfl
        · exact hyz_e.1
        · exact hyz_e.2
      refine ⟨tri v e, ⟨mem_tripleSet.mpr ⟨e, he, rfl⟩, hsub⟩, ?_⟩
      rintro T ⟨hT, hsubT⟩
      obtain ⟨e', he', rfl⟩ := mem_tripleSet.mp hT
      have h1 := pairCode_mem (hfl e he) hyz hyz_e.1 hyz_e.2
      have h2 := pairCode_mem (hfl e' he') hyz (hsubT (by simp)) (hsubT (by simp))
      rw [eq_of_mem_of_nodup_flatMap hPnd he' he h2 h1]
    intro P hP
    obtain ⟨y, z, hyz, rfl⟩ := Finset.card_eq_two.mp hP
    rcases Nat.lt_or_gt_of_ne (Fin.val_ne_of_ne hyz) with hlt | hlt
    · exact key y z hlt
    · rw [Finset.pair_comm]
      exact key z y hlt

end Soundness

end Mcd.Kernel
