import CpcwKernel.Target

/-!
# A generic kernel-checkable certificate for `(v, k, 1)` CPCW codes

Raw certificate data is a list of raw codewords, each a list of natural numbers.
`blockOf v hv k n d` is the family of `n` codewords of weight `k` whose entry `j` of codeword `i`
is the residue of `rawAt d i j` modulo `v`.

The Boolean side uses only `Nat` arithmetic, list recursion and the bit operations `|||` and
`Nat.testBit` on `Nat`, which the Lean kernel evaluates on literals (with GMP).

* `triples n k` lists every index triple `(i, j, l)` with `i < n`, `j < k`, `l < k`, `j ≠ l`.
* `diffList v k n d` lists, for every such triple, the ordered difference of raw entries `j` and
  `l` of raw codeword `i`, computed exactly as `Fin.sub` computes it.
* `check v k n d` holds iff no entry of `diffList v k n d` is `0` and no entry occurs twice
  (`freshAll` scans the list once, keeping a bit mask of the entries seen so far).

`count_of_check` gives, from `check v k n d = true` (one kernel evaluation), the exact count of
every residue in `Cpcw.diffs (blockOf v hv k n d)`: `1` if its value is in `diffList v k n d`,
`0` otherwise.  Every residue is covered, not a sample: duplicate-freeness of the full list of all
`n * k * (k - 1)` ordered differences is what bounds every count by `1`.  The data-independent
soundness theorem `isCPCW_of_check` derives the target property `Cpcw.IsCPCW (blockOf v hv k n d)`
from it; `count_of_leaveCheck` (audit only) derives the exact multiset of differences from a
recorded leave.
-/

namespace Cpcw.Kernel

/-! ## Raw data and the semantic codewords it names -/

/-- Raw entry `j` of raw codeword `i` (`0` outside the data). -/
def rawAt (d : List (List ℕ)) (i j : ℕ) : ℕ := (d.getD i []).getD j 0

/-- The family of `n` codewords of weight `k` named by raw data `d`: entry `j` of codeword `i` is
the residue of `rawAt d i j` modulo `v`. -/
def blockOf (v : ℕ) (hv : 0 < v) (k n : ℕ) (d : List (List ℕ)) (i : Fin n) (j : Fin k) : Fin v :=
  ⟨rawAt d i j % v, Nat.mod_lt _ hv⟩

/-! ## The Boolean checker -/

/-- The ordered pairs `(j, l)` of distinct positions `j, l < k`. -/
def posPairs (k : ℕ) : List (ℕ × ℕ) :=
  (List.range k).flatMap fun j => ((List.range k).filter fun l => l != j).map fun l => (j, l)

/-- The index triples `(i, j, l)` with `i < n` and `(j, l)` an ordered pair of distinct positions
below `k`. -/
def triples (n k : ℕ) : List (ℕ × ℕ × ℕ) :=
  (List.range n).flatMap fun i => (posPairs k).map fun p => (i, p.1, p.2)

/-- The value of `a - b` in `Fin v` for `a, b < v`, written exactly as `Fin.sub` computes it. -/
def dnat (v a b : ℕ) : ℕ := (v - b + a) % v

/-- The ordered difference of raw entries `j` and `l` of raw codeword `i`, for `t = (i, j, l)`. -/
def dval (v : ℕ) (d : List (List ℕ)) (t : ℕ × ℕ × ℕ) : ℕ :=
  dnat v (rawAt d t.1 t.2.1 % v) (rawAt d t.1 t.2.2 % v)

/-- All ordered differences of the first `n` raw codewords (positions below `k`). -/
def diffList (v k n : ℕ) (d : List (List ℕ)) : List ℕ := (triples n k).map (dval v d)

/-- `freshAll l m`: no element of `l` is a bit of `m`, and no element of `l` occurs twice. -/
def freshAll : List ℕ → ℕ → Bool
  | [], _ => true
  | x :: l, m => !m.testBit x && freshAll l (m ||| 2 ^ x)

/-- The certificate check: every ordered difference is nonzero, and no ordered difference occurs
twice. -/
def check (v k n : ℕ) (d : List (List ℕ)) : Bool :=
  (diffList v k n d).all (· != 0) && freshAll (diffList v k n d) 0

/-- Audit check of a recorded leave (not used by any root): a value `x < v` is an ordered
difference iff `x` is neither `0` nor in `leave`. -/
def leaveCheck (v k n : ℕ) (d : List (List ℕ)) (leave : List ℕ) : Bool :=
  (List.range v).all fun x => (diffList v k n d).contains x == !(x == 0 || leave.contains x)

/-! ## Lemmas about the checker -/

theorem mem_posPairs {k j l : ℕ} : (j, l) ∈ posPairs k ↔ j < k ∧ l < k ∧ j ≠ l := by
  simp only [posPairs, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_filter,
    bne_iff_ne, ne_eq, Prod.mk.injEq]
  constructor
  · rintro ⟨a, ha, b, ⟨hb, hba⟩, rfl, rfl⟩
    exact ⟨ha, hb, fun h => hba h.symm⟩
  · rintro ⟨hj, hl, hjl⟩
    exact ⟨j, hj, l, ⟨hl, fun h => hjl h.symm⟩, rfl, rfl⟩

theorem mem_triples {n k i j l : ℕ} :
    (i, j, l) ∈ triples n k ↔ i < n ∧ j < k ∧ l < k ∧ j ≠ l := by
  simp only [triples, List.mem_flatMap, List.mem_range, List.mem_map, Prod.mk.injEq]
  constructor
  · rintro ⟨a, ha, ⟨p1, p2⟩, hp, rfl, rfl, rfl⟩
    exact ⟨ha, mem_posPairs.1 hp⟩
  · rintro ⟨hi, hjl⟩
    exact ⟨i, hi, (j, l), mem_posPairs.2 hjl, rfl, rfl, rfl⟩

theorem freshAll_spec : ∀ (l : List ℕ) (m : ℕ), freshAll l m = true →
    l.Nodup ∧ ∀ x ∈ l, m.testBit x = false
  | [], _, _ => ⟨List.nodup_nil, by simp⟩
  | x :: l, m, h => by
    simp only [freshAll, Bool.and_eq_true, Bool.not_eq_true'] at h
    obtain ⟨hx, hl⟩ := h
    obtain ⟨hnd, hfresh⟩ := freshAll_spec l _ hl
    refine ⟨List.nodup_cons.2 ⟨fun hmem => ?_, hnd⟩, ?_⟩
    · have hbit := hfresh x hmem
      rw [Nat.testBit_or, Nat.testBit_two_pow_self, Bool.or_true] at hbit
      exact Bool.noConfusion hbit
    · intro y hy
      rcases List.mem_cons.1 hy with rfl | hy
      · exact hx
      · have hbit := hfresh y hy
        rw [Nat.testBit_or, Bool.or_eq_false_iff] at hbit
        exact hbit.1

/-! ## Soundness -/

theorem blockOf_sub_val (v : ℕ) (hv : 0 < v) (k n : ℕ) (d : List (List ℕ)) (i : Fin n)
    (j l : Fin k) :
    ((blockOf v hv k n d i j - blockOf v hv k n d i l : Fin v) : ℕ) =
      dval v d (i.val, j.val, l.val) := by
  rw [Fin.val_sub]
  rfl

/-- The count of a residue in `Cpcw.diffs` is the number of index triples producing it. -/
theorem count_diffs {v k n : ℕ} (B : Fin n → Fin k → Fin v) (e : Fin v) :
    (Cpcw.diffs B).count e =
      (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).filter
        fun t => e = B t.1 t.2.1 - B t.1 t.2.2).card := by
  rw [Cpcw.diffs, Multiset.count_map, ← Finset.filter_val]
  rfl

/-- **Exact counts.**  If the check passes, the residue `e` occurs once in `Cpcw.diffs` when its
value is in `diffList`, and never otherwise. -/
theorem count_of_check (v k n : ℕ) (hv : 0 < v) (d : List (List ℕ))
    (hc : check v k n d = true) (e : Fin v) :
    (Cpcw.diffs (blockOf v hv k n d)).count e =
      if e.val ∈ diffList v k n d then 1 else 0 := by
  simp only [check, Bool.and_eq_true] at hc
  have hnd : ((triples n k).map (dval v d)).Nodup := (freshAll_spec _ _ hc.2).1
  have hmem : ∀ t : Fin n × Fin k × Fin k, t.2.1 ≠ t.2.2 →
      (t.1.val, t.2.1.val, t.2.2.val) ∈ triples n k := fun t ht =>
    mem_triples.2 ⟨t.1.isLt, t.2.1.isLt, t.2.2.isLt, fun h => ht (Fin.ext h)⟩
  rw [count_diffs]
  split_ifs with he
  · obtain ⟨⟨i, j, l⟩, ht, hte⟩ := List.mem_map.1 he
    obtain ⟨hi, hj, hl, hjl⟩ := mem_triples.1 ht
    rw [Finset.card_eq_one]
    refine ⟨(⟨i, hi⟩, ⟨j, hj⟩, ⟨l, hl⟩), Finset.ext fun t => ?_⟩
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    constructor
    · rintro ⟨ht', het⟩
      have e1 : dval v d (t.1.val, t.2.1.val, t.2.2.val) = dval v d (i, j, l) := by
        rw [← blockOf_sub_val v hv k n d, ← het, ← hte]
      have e2 := List.inj_on_of_nodup_map hnd (hmem t ht') ht e1
      simp only [Prod.mk.injEq] at e2
      obtain ⟨e3, e4, e5⟩ := e2
      exact Prod.ext (Fin.ext e3) (Prod.ext (Fin.ext e4) (Fin.ext e5))
    · rintro rfl
      refine ⟨fun h => hjl (congrArg Fin.val h), Fin.ext ?_⟩
      rw [blockOf_sub_val]
      exact hte.symm
  · rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
    intro t ht het
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ht
    apply he
    rw [het, blockOf_sub_val]
    exact List.mem_map.2 ⟨_, hmem t ht, rfl⟩

/-- **Soundness of the checker.**  No hypothesis is a semantic property of the family. -/
theorem isCPCW_of_check (v k n : ℕ) (hv : 0 < v) (d : List (List ℕ))
    (hc : check v k n d = true) : Cpcw.IsCPCW (blockOf v hv k n d) := by
  have hnz : ∀ x ∈ diffList v k n d, x ≠ 0 := by
    simp only [check, Bool.and_eq_true, List.all_eq_true, bne_iff_ne] at hc
    exact hc.1
  have hcount := count_of_check v k n hv d hc
  refine ⟨?_, ?_, ?_⟩
  · -- The `k` entries of each codeword are distinct.
    intro i j l hjl
    by_contra hne
    have hpos : (Cpcw.diffs (blockOf v hv k n d)).count
        (blockOf v hv k n d i j - blockOf v hv k n d i l) ≠ 0 := by
      rw [Multiset.count_ne_zero, Cpcw.diffs, Multiset.mem_map]
      exact ⟨(i, j, l), by simp [hne], rfl⟩
    rw [hcount] at hpos
    have hmem : ((blockOf v hv k n d i j - blockOf v hv k n d i l : Fin v) : ℕ) ∈
        diffList v k n d := by
      by_contra h
      exact hpos (ite_eq_right h)
    apply hnz _ hmem
    rw [hjl, Fin.val_sub]
    have hl := (blockOf v hv k n d i l).isLt
    rw [Nat.sub_add_cancel hl.le, Nat.mod_self]
  · -- Every nonzero residue occurs at most once.
    intro e _
    rw [hcount]
    split_ifs <;> omega
  · -- The residue `0` never occurs.
    intro e he
    rw [hcount, ite_eq_right]
    intro hmem
    exact hnz _ hmem he

/-- **Audited leave.**  If both checks pass, every residue outside `{0} ∪ leave` occurs exactly
once in `Cpcw.diffs`, and every residue in `{0} ∪ leave` never occurs. -/
theorem count_of_leaveCheck (v k n : ℕ) (hv : 0 < v) (d : List (List ℕ)) (leave : List ℕ)
    (hc : check v k n d = true) (hl : leaveCheck v k n d leave = true) (e : Fin v) :
    (Cpcw.diffs (blockOf v hv k n d)).count e = if e.val = 0 ∨ e.val ∈ leave then 0 else 1 := by
  rw [count_of_check v k n hv d hc]
  simp only [leaveCheck, List.all_eq_true, List.mem_range] at hl
  have hx : e.val ∈ diffList v k n d ↔ ¬ (e.val = 0 ∨ e.val ∈ leave) := by
    have h := hl e.val e.isLt
    rw [beq_iff_eq] at h
    rw [← List.contains_iff_mem, h]
    simp
  by_cases hm : e.val ∈ diffList v k n d
  · rw [ite_eq_left hm, ite_eq_right (hx.1 hm)]
  · rw [ite_eq_right hm, ite_eq_left (not_not.1 (mt hx.2 hm))]

end Cpcw.Kernel
