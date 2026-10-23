import CdfKernel.Target

/-!
# A generic kernel-checkable certificate for cyclic `(v, 5, 1)` difference families

Raw certificate data is a list of raw blocks, each a list of natural numbers.  `blockOf v hv n d`
is the family of `n` base blocks whose entry `j` of block `i` is the residue of `rawAt d i j`
modulo `v`.

The Boolean side uses only `Nat` arithmetic, list recursion and bitwise `|||` on `Nat`, which
the Lean kernel evaluates on literals (with GMP).  `coverMask v n d` sets bit `x` for every
ordered difference `x` of the first `n` raw blocks (computed as `Fin.sub` computes it), and
`fullMask v` is the mask of bits `1, ..., v - 1`.

`isCDF_of_check` is the data-independent soundness theorem: from

* `20 * n + 1 = v` (a numeral identity), and
* `coverMask v n d = fullMask v` (one kernel evaluation),

it concludes the target property `Cdf.IsCDF (blockOf v hv n d)`.  The mask equality says that
the set of ordered differences is exactly the set of nonzero residues; that each nonzero residue
is hit only once then follows by counting (`20 * n` ordered differences, `v - 1` nonzero
residues), and distinctness of block entries follows from `0` never being a difference.
-/

namespace Cdf.Kernel

/-! ## Raw data and the semantic blocks it names -/

/-- Raw entry `j` of raw block `i` (`0` outside the data). -/
def rawAt (d : List (List ℕ)) (i j : ℕ) : ℕ := (d.getD i []).getD j 0

/-- The family of `n` base blocks named by raw data `d`: entry `j` of block `i` is the residue
of `rawAt d i j` modulo `v`. -/
def blockOf (v : ℕ) (hv : 0 < v) (n : ℕ) (d : List (List ℕ)) (i : Fin n) (j : Fin 5) : Fin v :=
  ⟨rawAt d i j % v, Nat.mod_lt _ hv⟩

/-! ## The Boolean checker -/

/-- The 20 ordered pairs `(j, k)` of distinct positions `j, k < 5`. -/
def posPairs : List (ℕ × ℕ) :=
  [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1),
   (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]

/-- The value of `a - b` in `Fin v` for `a, b < v`, written exactly as `Fin.sub` computes it. -/
def dnat (v a b : ℕ) : ℕ := (v - b + a) % v

/-- The ordered differences of the first `n` raw blocks, block by block. -/
def diffList (v n : ℕ) (d : List (List ℕ)) : List ℕ :=
  (List.range n).flatMap fun i =>
    posPairs.map fun p => dnat v (rawAt d i p.1 % v) (rawAt d i p.2 % v)

/-- Bitwise union of a list of naturals. -/
def orAll (l : List ℕ) : ℕ := l.foldl (· ||| ·) 0

/-- Bit `x` for every ordered difference `x` of the first `n` raw blocks. -/
def coverMask (v n : ℕ) (d : List (List ℕ)) : ℕ := orAll ((diffList v n d).map (2 ^ ·))

/-- Bits `1, ..., v - 1`: one bit per nonzero residue modulo `v`. -/
def fullMask (v : ℕ) : ℕ := orAll (((List.range v).filter (· != 0)).map (2 ^ ·))

/-! ## Bit lemmas -/

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

theorem testBit_fullMask (v k : ℕ) : (fullMask v).testBit k = true ↔ k ≠ 0 ∧ k < v := by
  rw [fullMask, testBit_orAll_pow]
  simp [List.mem_filter]
  tauto

theorem mem_diffList {v n : ℕ} {d : List (List ℕ)} {x : ℕ} :
    x ∈ diffList v n d ↔
      ∃ i < n, ∃ p ∈ posPairs, dnat v (rawAt d i p.1 % v) (rawAt d i p.2 % v) = x := by
  simp only [diffList, List.mem_flatMap, List.mem_range, List.mem_map]

/-- The coverage check says that the ordered differences are exactly the nonzero residues. -/
theorem mem_diffList_of_check {v n : ℕ} {d : List (List ℕ)}
    (h : coverMask v n d = fullMask v) (x : ℕ) :
    x ∈ diffList v n d ↔ x ≠ 0 ∧ x < v := by
  rw [← testBit_fullMask, ← h, coverMask, testBit_orAll_pow]

theorem posPairs_spec : ∀ p ∈ posPairs, p.1 < 5 ∧ p.2 < 5 ∧ p.1 ≠ p.2 := by decide

theorem posPairs_complete : ∀ j k : Fin 5, j ≠ k → (j.val, k.val) ∈ posPairs := by decide

/-! ## Counting -/

theorem card_offDiag_positions (n : ℕ) :
    ((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).card =
      n * 20 := by
  rw [← Finset.univ_product_univ, Finset.filter_product_right (fun p : Fin 5 × Fin 5 => p.1 ≠ p.2),
    Finset.card_product, Finset.card_univ, Fintype.card_fin]
  rfl

theorem card_nonzero (v : ℕ) (hv : 0 < v) :
    ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card = v - 1 := by
  have e : ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0) =
      Finset.univ.erase ⟨0, hv⟩ := by
    ext x
    simp [Fin.ext_iff]
  rw [e, Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]

/-! ## Soundness -/

theorem blockOf_sub_val (v : ℕ) (hv : 0 < v) (n : ℕ) (d : List (List ℕ)) (i : Fin n)
    (j k : Fin 5) :
    ((blockOf v hv n d i j - blockOf v hv n d i k : Fin v) : ℕ) =
      dnat v (rawAt d i j % v) (rawAt d i k % v) := by
  rw [Fin.val_sub]
  rfl

/-- **Soundness of the checker.**  No hypothesis is a semantic property of the family. -/
theorem isCDF_of_check (v n : ℕ) (hv : 0 < v) (d : List (List ℕ))
    (hn : 20 * n + 1 = v) (hcov : coverMask v n d = fullMask v) :
    Cdf.IsCDF (blockOf v hv n d) := by
  let B := blockOf v hv n d
  let D : Fin n × Fin 5 × Fin 5 → Fin v := fun t => B t.1 t.2.1 - B t.1 t.2.2
  have hD : ∀ t, (D t : ℕ) = dnat v (rawAt d t.1 t.2.1 % v) (rawAt d t.1 t.2.2 % v) :=
    fun t => blockOf_sub_val v hv n d t.1 t.2.1 t.2.2
  -- Every ordered difference of distinct positions is a nonzero residue.
  have hnz : ∀ t : Fin n × Fin 5 × Fin 5, t.2.1 ≠ t.2.2 → (D t : ℕ) ≠ 0 := by
    intro t ht
    have hmem : (D t : ℕ) ∈ diffList v n d :=
      mem_diffList.2 ⟨t.1, t.1.isLt, (t.2.1.val, t.2.2.val), posPairs_complete _ _ ht, (hD t).symm⟩
    exact ((mem_diffList_of_check hcov _).1 hmem).1
  -- Every nonzero residue is an ordered difference of distinct positions.
  have hsurj : ∀ e : Fin v, (e : ℕ) ≠ 0 →
      ∃ t : Fin n × Fin 5 × Fin 5, t.2.1 ≠ t.2.2 ∧ D t = e := by
    intro e he
    obtain ⟨i, hi, p, hp, hpe⟩ := mem_diffList.1 ((mem_diffList_of_check hcov _).2 ⟨he, e.isLt⟩)
    obtain ⟨h1, h2, h12⟩ := posPairs_spec p hp
    refine ⟨(⟨i, hi⟩, ⟨p.1, h1⟩, ⟨p.2, h2⟩), fun h => h12 (congrArg Fin.val h), Fin.ext ?_⟩
    rw [hD]
    exact hpe
  -- Counting: `20 * n` ordered differences onto `v - 1` nonzero residues, hence injective.
  let S : Finset (Fin n × Fin 5 × Fin 5) := Finset.univ.filter fun t => t.2.1 ≠ t.2.2
  let N : Finset (Fin v) := Finset.univ.filter fun e => e.val ≠ 0
  have hinj : ∀ t₁ ∈ S, ∀ t₂ ∈ S, D t₁ = D t₂ → t₁ = t₂ := by
    have key := Finset.inj_on_of_surj_on_of_card_le (s := S) (t := N) (fun t _ => D t)
      (fun t ht => by
        simp only [S, Finset.mem_filter, Finset.mem_univ, true_and] at ht
        simp only [N, Finset.mem_filter, Finset.mem_univ, true_and]
        exact hnz t ht)
      (fun e he => by
        simp only [N, Finset.mem_filter, Finset.mem_univ, true_and] at he
        obtain ⟨t, ht, hte⟩ := hsurj e he
        exact ⟨t, by simp only [S, Finset.mem_filter, Finset.mem_univ, true_and]; exact ht, hte⟩)
      (by rw [card_offDiag_positions, card_nonzero v hv]; omega)
    intro t₁ h₁ t₂ h₂ h
    exact key h₁ h₂ h
  -- The count of each residue in the multiset of ordered differences.
  have hcount : ∀ e : Fin v, (Cdf.diffs B).count e = (S.filter fun t => e = D t).card := by
    intro e
    show Multiset.count e (S.val.map D) = _
    rw [Multiset.count_map, ← Finset.filter_val]
    rfl
  refine ⟨?_, ?_, ?_⟩
  · -- The five entries of each block are distinct.
    intro i j k hjk
    by_contra hne
    apply hnz (i, j, k) hne
    have hjk' : B i j = B i k := hjk
    show ((B i j - B i k : Fin v) : ℕ) = 0
    rw [hjk', Fin.val_sub]
    have hk := (B i k).isLt
    rw [Nat.sub_add_cancel hk.le, Nat.mod_self]
  · -- Every nonzero residue occurs exactly once.
    intro e he
    obtain ⟨t₀, ht₀, hte⟩ := hsurj e he
    rw [hcount, Finset.card_eq_one]
    refine ⟨t₀, Finset.ext fun t => ?_⟩
    simp only [S, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    constructor
    · rintro ⟨ht, het⟩
      exact hinj t (by simp only [S, Finset.mem_filter, Finset.mem_univ, true_and]; exact ht)
        t₀ (by simp only [S, Finset.mem_filter, Finset.mem_univ, true_and]; exact ht₀)
        (het.symm.trans hte.symm)
    · rintro rfl
      exact ⟨ht₀, hte.symm⟩
  · -- The residue `0` never occurs.
    intro e he
    rw [hcount, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
    intro t ht het
    simp only [S, Finset.mem_filter, Finset.mem_univ, true_and] at ht
    exact hnz t ht (het ▸ he)

end Cdf.Kernel
