import LktsKernel.PriorFormal
import Mathlib.Data.Fintype.Powerset

/-!
# Generic kernel-checkable certificates for large sets of Kirkman triple systems

`LktsKernel.PriorFormal` is a byte-identical copy of the frozen
`review/lkts57-construction-snapshot-v1/PriorFormal.lean`
(SHA-256 a39613c93506390e52b75b4fb355d6a0d69160ea2f8a3bfe5e0ebd30ff3f2dee).  Its definitions
`Kirkman.IsSTS`, `IsParallelClass`, `IsResolution`, `IsKTS` and `IsLKTS` are used unchanged.

A certificate is a list of systems; a system is a list of classes; a class is a list of
rows `(a, b, c)` of natural numbers.  `blocksOf v d i` is the set of genuine triples whose
point set is exactly `{a, b, c}` for some row of system `i`, and `classesOf v d i c` is the
same for class `c` of system `i`.

The Boolean checks below use only `Nat` arithmetic and bitwise operations, which the Lean
kernel evaluates on literals with GMP.  `isLKTS_of_check` is the data-independent soundness
theorem: from the hypotheses below it concludes the frozen semantic `Kirkman.IsLKTS` for
`blocksOf v d`.  No hypothesis is a semantic design property:

* `d.length = v - 2`;
* `sysOK v (fullPairs v) s = true` for every system `s`: `(v - 1) / 2` classes of `v / 3`
  rows, every row strictly increasing below `v`, the point masks of each class pairwise
  disjoint with union `{0, ..., v - 1}`, and the pair masks of the classes pairwise disjoint
  with union equal to the mask of all pairs `x < y < v`;
* `(allRows d).Nodup`: no row occurs twice in the whole certificate.  Concrete certificates
  prove it with `nodup_of_rankFold`, a bitmask fold over colexicographic row ranks that may be
  split into kernel-checked segments with `rankFold_append`;
* `(v - 2) * ((v - 1) / 2 * (v / 3)) = choose v 3`, a numeral identity.

Coverage of every triple is not checked by a scan: it follows by counting, because the
injective row map has `(v - 2) * ((v - 1) / 2) * (v / 3) = choose v 3` arguments.
-/

namespace Kirkman.KernelCert

open Kirkman

/-- A raw certificate row `(a, b, c)`. -/
abbrev Row := ℕ × ℕ × ℕ

/-! ## The Boolean checker -/

/-- A row is strictly increasing and below `v`. -/
def rowOK (v : ℕ) (t : Row) : Bool := decide (t.1 < t.2.1 ∧ t.2.1 < t.2.2 ∧ t.2.2 < v)

/-- Bits `a`, `b`, `c`. -/
def ptMask (t : Row) : ℕ := 2 ^ t.1 ||| 2 ^ t.2.1 ||| 2 ^ t.2.2

/-- Bit `v * x + y` for each of the three pairs `x < y` of a sorted row. -/
def pairMask (v : ℕ) (t : Row) : ℕ :=
  2 ^ (v * t.1 + t.2.1) ||| 2 ^ (v * t.1 + t.2.2) ||| 2 ^ (v * t.2.1 + t.2.2)

/-- Bitwise union of a list of masks. -/
def orAll (l : List ℕ) : ℕ := l.foldl (· ||| ·) 0

/-- `accOK acc ms tgt`: each mask is disjoint from `acc` and from all earlier masks, and the
final union is exactly `tgt`. -/
def accOK : ℕ → List ℕ → ℕ → Bool
  | acc, [], tgt => acc == tgt
  | acc, m :: ms, tgt => (acc &&& m == 0) && accOK (acc ||| m) ms tgt

/-- The mask of all pairs `x < y < v`, i.e. bits `v * x + y`. -/
def fullPairs (v : ℕ) : ℕ :=
  orAll ((List.range v).flatMap fun x =>
    ((List.range v).filter fun y => x < y).map fun y => 2 ^ (v * x + y))

/-- A class has `v / 3` valid rows whose point sets partition `{0, ..., v - 1}`. -/
def classOK (v : ℕ) (cls : List Row) : Bool :=
  cls.length == v / 3 && cls.all (rowOK v) && accOK 0 (cls.map ptMask) (2 ^ v - 1)

/-- Union of the pair masks of the rows of a class. -/
def classPairs (v : ℕ) (cls : List Row) : ℕ := orAll (cls.map (pairMask v))

/-- A system has `(v - 1) / 2` valid classes whose pair sets partition all pairs `fp`. -/
def sysOK (v fp : ℕ) (s : List (List Row)) : Bool :=
  s.length == (v - 1) / 2 && s.all (classOK v) && accOK 0 (s.map (classPairs v)) fp

/-- Colexicographic rank `choose c 3 + choose b 2 + a` of a sorted row `(a, b, c)`, used only
as a bit position.  Soundness never uses its injectivity: equal rows have equal ranks. -/
def rank (t : Row) : ℕ := t.2.2 * (t.2.2 - 1) * (t.2.2 - 2) / 6 + t.2.1 * (t.2.1 - 1) / 2 + t.1

/-- Sets bit `rank t` for each row in turn, failing (`none`) if the bit is already set.
`rankFold acc l = some b` therefore shows that no rank, hence no row, repeats in `l`. -/
def rankFold : ℕ → List Row → Option ℕ
  | acc, [] => some acc
  | acc, t :: ts => if acc &&& 2 ^ rank t = 0 then rankFold (acc ||| 2 ^ rank t) ts else none

/-- All rows of a certificate, system by system. -/
def allRows (d : List (List (List Row))) : List Row := (d.map List.flatten).flatten

/-! ## The semantic objects named by a certificate -/

/-- The point set `{a, b, c}` of a row, as a finset of `Fin v`. -/
def rowSet (v : ℕ) (t : Row) : Finset (Fin v) :=
  Finset.univ.filter fun x => x.val = t.1 ∨ x.val = t.2.1 ∨ x.val = t.2.2

/-- Row `r` of class `c` of system `i` (with a dummy default outside the list). -/
def rowAt (d : List (List (List Row))) (i c r : ℕ) : Row :=
  ((d.getD i []).getD c []).getD r (0, 0, 0)

/-- Constituent `i`: all genuine triples whose point set is a row of system `i`. -/
def blocksOf (v : ℕ) (d : List (List (List Row))) (i : Fin (v - 2)) : Blocks v :=
  {T | ∃ c : Fin ((v - 1) / 2), ∃ r : Fin (v / 3), T.val = rowSet v (rowAt d i c r)}

/-- Class `c` of constituent `i`. -/
def classesOf (v : ℕ) (d : List (List (List Row))) (i : Fin (v - 2))
    (c : Fin ((v - 1) / 2)) : Blocks v :=
  {T | ∃ r : Fin (v / 3), T.val = rowSet v (rowAt d i c r)}

/-! ## Bit lemmas -/

theorem land_eq_zero_iff {a b : ℕ} :
    a &&& b = 0 ↔ ∀ k, ¬ (a.testBit k = true ∧ b.testBit k = true) := by
  constructor
  · intro h k hk
    have h2 := congrArg (fun n => n.testBit k) h
    simp [Nat.testBit_and, hk.1, hk.2] at h2
  · intro h
    apply Nat.eq_of_testBit_eq
    intro k
    rw [Nat.testBit_and, Nat.zero_testBit]
    cases ha : a.testBit k <;> cases hb : b.testBit k <;>
      first | rfl | exact absurd ⟨ha, hb⟩ (h k)

theorem testBit_foldl_or (l : List ℕ) (a k : ℕ) :
    (l.foldl (· ||| ·) a).testBit k = true ↔
      a.testBit k = true ∨ ∃ m ∈ l, m.testBit k = true := by
  induction l generalizing a with
  | nil => simp
  | cons m l ih =>
    rw [List.foldl_cons, ih, Nat.testBit_or, Bool.or_eq_true]
    simp only [List.mem_cons, exists_eq_or_imp]
    tauto

theorem testBit_orAll (l : List ℕ) (k : ℕ) :
    (orAll l).testBit k = true ↔ ∃ m ∈ l, m.testBit k = true := by
  rw [orAll, testBit_foldl_or]
  simp

theorem accOK_sound : ∀ (ms : List ℕ) (acc tgt : ℕ), accOK acc ms tgt = true →
    List.Pairwise (fun x y => x &&& y = 0) ms ∧ (∀ m ∈ ms, acc &&& m = 0) ∧
    ∀ k, tgt.testBit k = true ↔ (acc.testBit k = true ∨ ∃ m ∈ ms, m.testBit k = true)
  | [], acc, tgt, h => by
    have e : acc = tgt := by simpa [accOK] using h
    subst e
    simp
  | m :: ms, acc, tgt, h => by
    simp only [accOK, Bool.and_eq_true, beq_iff_eq] at h
    obtain ⟨h0, h1⟩ := h
    obtain ⟨hp, hd, hc⟩ := accOK_sound ms (acc ||| m) tgt h1
    have hsplit : ∀ m' ∈ ms, acc &&& m' = 0 ∧ m &&& m' = 0 := by
      intro m' hm'
      have h2 := land_eq_zero_iff.mp (hd m' hm')
      constructor
      · refine land_eq_zero_iff.mpr fun k hk => h2 k ?_
        simp [Nat.testBit_or, hk.1, hk.2]
      · refine land_eq_zero_iff.mpr fun k hk => h2 k ?_
        simp [Nat.testBit_or, hk.1, hk.2]
    refine ⟨List.Pairwise.cons (fun m' hm' => (hsplit m' hm').2) hp, ?_, ?_⟩
    · intro m' hm'
      rcases List.mem_cons.mp hm' with rfl | hm'
      · exact h0
      · exact (hsplit m' hm').1
    · intro k
      rw [hc k, Nat.testBit_or, Bool.or_eq_true]
      simp only [List.mem_cons, exists_eq_or_imp]
      tauto

theorem getD_of_lt {α : Type} {l : List α} {i : ℕ} (dflt : α) (h : i < l.length) :
    l.getD i dflt = l[i] := by
  simp [List.getD_eq_getElem?_getD, h]

/-- Two positions of a pairwise-disjoint mask list sharing a bit are equal. -/
theorem eq_of_pairwise_map {α : Type} {f : α → ℕ} {xs : List α} (dflt : α)
    (h : List.Pairwise (fun x y => x &&& y = 0) (xs.map f))
    {i j : ℕ} (hi : i < xs.length) (hj : j < xs.length) {k : ℕ}
    (hik : (f (xs.getD i dflt)).testBit k = true)
    (hjk : (f (xs.getD j dflt)).testBit k = true) : i = j := by
  rw [getD_of_lt dflt hi] at hik
  rw [getD_of_lt dflt hj] at hjk
  have hpw := List.pairwise_iff_getElem.mp h
  rcases Nat.lt_trichotomy i j with hij | hij | hij
  · have e := hpw i j (by simpa using hi) (by simpa using hj) hij
    simp only [List.getElem_map] at e
    exact absurd ⟨hik, hjk⟩ (land_eq_zero_iff.mp e k)
  · exact hij
  · have e := hpw j i (by simpa using hj) (by simpa using hi) hij
    simp only [List.getElem_map] at e
    exact absurd ⟨hjk, hik⟩ (land_eq_zero_iff.mp e k)

/-- Membership in a list gives a position with that `getD` value. -/
theorem exists_getD_of_mem {α : Type} {l : List α} {a : α} (dflt : α) (h : a ∈ l) :
    ∃ i, i < l.length ∧ l.getD i dflt = a := by
  obtain ⟨i, hi, e⟩ := List.mem_iff_getElem.mp h
  exact ⟨i, hi, by rw [getD_of_lt dflt hi, e]⟩

theorem rankFold_sound : ∀ (acc : ℕ) (l : List Row) (b : ℕ), rankFold acc l = some b →
    l.Nodup ∧ ∀ t ∈ l, acc.testBit (rank t) = false
  | _, [], _, _ => by simp
  | acc, t :: ts, b, h => by
    by_cases h0 : acc &&& 2 ^ rank t = 0
    · simp only [rankFold, h0, ↓reduceIte] at h
      obtain ⟨hnd, hacc⟩ := rankFold_sound _ ts b h
      refine ⟨List.nodup_cons.mpr ⟨fun ht => ?_, hnd⟩, ?_⟩
      · have := hacc t ht
        simp [Nat.testBit_or] at this
      · intro t' ht'
        rcases List.mem_cons.mp ht' with rfl | ht'
        · have := land_eq_zero_iff.mp h0 (rank t')
          simp only [Nat.testBit_two_pow, decide_true, and_true] at this
          simpa using this
        · have := hacc t' ht'
          simp only [Nat.testBit_or, Bool.or_eq_false_iff] at this
          exact this.1
    · simp [rankFold, h0] at h

/-- A successful rank fold certifies that the rows are pairwise distinct. -/
theorem nodup_of_rankFold {acc b : ℕ} {l : List Row} (h : rankFold acc l = some b) : l.Nodup :=
  (rankFold_sound acc l b h).1

/-- Rank folds compose, so one fold can be checked in kernel segments. -/
theorem rankFold_append : ∀ (a : ℕ) (l₁ l₂ : List Row) (b c : ℕ),
    rankFold a l₁ = some b → rankFold b l₂ = some c → rankFold a (l₁ ++ l₂) = some c
  | a, [], l₂, b, c, h1, h2 => by
    simp only [rankFold, Option.some.injEq] at h1
    subst h1
    simpa using h2
  | a, t :: ts, l₂, b, c, h1, h2 => by
    by_cases h0 : a &&& 2 ^ rank t = 0
    · simp only [rankFold, h0, ↓reduceIte] at h1
      simp only [List.cons_append, rankFold, h0, ↓reduceIte]
      exact rankFold_append _ ts l₂ b c h1 h2
    · simp [rankFold, h0] at h1

theorem allRows_append (d₁ d₂ : List (List (List Row))) :
    allRows (d₁ ++ d₂) = allRows d₁ ++ allRows d₂ := by
  simp [allRows]

/-! ## Row lemmas -/

theorem rowOK_iff {v : ℕ} {t : Row} :
    rowOK v t = true ↔ t.1 < t.2.1 ∧ t.2.1 < t.2.2 ∧ t.2.2 < v := by
  simp [rowOK]

theorem mem_rowSet {v : ℕ} {t : Row} {x : Fin v} :
    x ∈ rowSet v t ↔ x.val = t.1 ∨ x.val = t.2.1 ∨ x.val = t.2.2 := by
  simp [rowSet]

theorem card_rowSet {v : ℕ} {t : Row} (h : rowOK v t = true) : (rowSet v t).card = 3 := by
  obtain ⟨h1, h2, h3⟩ := rowOK_iff.mp h
  rw [Finset.card_eq_three]
  refine ⟨⟨t.1, by omega⟩, ⟨t.2.1, by omega⟩, ⟨t.2.2, h3⟩, ?_, ?_, ?_, ?_⟩
  · simp only [ne_eq, Fin.ext_iff]; omega
  · simp only [ne_eq, Fin.ext_iff]; omega
  · simp only [ne_eq, Fin.ext_iff]; omega
  · ext x
    simp [rowSet, Fin.ext_iff]

theorem testBit_ptMask (t : Row) (k : ℕ) :
    (ptMask t).testBit k = true ↔ t.1 = k ∨ t.2.1 = k ∨ t.2.2 = k := by
  simp [ptMask, Nat.testBit_or, Nat.testBit_two_pow, or_assoc]

theorem testBit_pairMask (v : ℕ) (t : Row) (k : ℕ) :
    (pairMask v t).testBit k = true ↔
      v * t.1 + t.2.1 = k ∨ v * t.1 + t.2.2 = k ∨ v * t.2.1 + t.2.2 = k := by
  simp [pairMask, Nat.testBit_or, Nat.testBit_two_pow, or_assoc]

theorem base_eq {v x y a b : ℕ} (hy : y < v) (hb : b < v) (h : v * x + y = v * a + b) :
    x = a ∧ y = b := by
  have hv : 0 < v := by omega
  have h1 : (v * x + y) / v = x := by rw [Nat.mul_add_div hv, Nat.div_eq_of_lt hy, Nat.add_zero]
  have h2 : (v * a + b) / v = a := by rw [Nat.mul_add_div hv, Nat.div_eq_of_lt hb, Nat.add_zero]
  have h3 : (v * x + y) % v = y := by rw [Nat.mul_add_mod, Nat.mod_eq_of_lt hy]
  have h4 : (v * a + b) % v = b := by rw [Nat.mul_add_mod, Nat.mod_eq_of_lt hb]
  exact ⟨by rw [← h1, ← h2, h], by rw [← h3, ← h4, h]⟩

/-- Two points `x < y` of a valid row give a bit of its pair mask. -/
theorem pairMask_bit {v : ℕ} {t : Row} (ht : rowOK v t = true) {x y : ℕ}
    (hx : x = t.1 ∨ x = t.2.1 ∨ x = t.2.2) (hy : y = t.1 ∨ y = t.2.1 ∨ y = t.2.2)
    (hxy : x < y) : (pairMask v t).testBit (v * x + y) = true := by
  obtain ⟨h1, h2, _⟩ := rowOK_iff.mp ht
  rw [testBit_pairMask]
  rcases hx with rfl | rfl | rfl <;> rcases hy with rfl | rfl | rfl <;>
    first | (simp; done) | (exfalso; omega)

/-- A bit `v * x + y` (with `y < v`) of the pair mask of a valid row names two of its points. -/
theorem mem_of_pairMask_bit {v : ℕ} {t : Row} (ht : rowOK v t = true) {x y : ℕ} (hy : y < v)
    (h : (pairMask v t).testBit (v * x + y) = true) :
    (x = t.1 ∨ x = t.2.1 ∨ x = t.2.2) ∧ (y = t.1 ∨ y = t.2.1 ∨ y = t.2.2) := by
  obtain ⟨h1, h2, h3⟩ := rowOK_iff.mp ht
  rw [testBit_pairMask] at h
  rcases h with h | h | h
  · obtain ⟨e1, e2⟩ := base_eq (by omega) hy h
    exact ⟨Or.inl e1.symm, Or.inr (Or.inl e2.symm)⟩
  · obtain ⟨e1, e2⟩ := base_eq h3 hy h
    exact ⟨Or.inl e1.symm, Or.inr (Or.inr e2.symm)⟩
  · obtain ⟨e1, e2⟩ := base_eq h3 hy h
    exact ⟨Or.inr (Or.inl e1.symm), Or.inr (Or.inr e2.symm)⟩

/-- Valid rows with the same point set are equal. -/
theorem row_eq_of_rowSet_eq {v : ℕ} {t t' : Row} (ht : rowOK v t = true)
    (ht' : rowOK v t' = true) (h : rowSet v t = rowSet v t') : t = t' := by
  obtain ⟨h1, h2, h3⟩ := rowOK_iff.mp ht
  obtain ⟨h1', h2', h3'⟩ := rowOK_iff.mp ht'
  have m : ∀ n (hn : n < v),
      (n = t.1 ∨ n = t.2.1 ∨ n = t.2.2) ↔ (n = t'.1 ∨ n = t'.2.1 ∨ n = t'.2.2) := by
    intro n hn
    have := Finset.ext_iff.mp h ⟨n, hn⟩
    simpa [mem_rowSet] using this
  have e1 := (m t.1 (by omega)).mp (Or.inl rfl)
  have e2 := (m t.2.1 (by omega)).mp (Or.inr (Or.inl rfl))
  have e3 := (m t.2.2 (by omega)).mp (Or.inr (Or.inr rfl))
  have f1 := (m t'.1 (by omega)).mpr (Or.inl rfl)
  have f2 := (m t'.2.1 (by omega)).mpr (Or.inr (Or.inl rfl))
  have f3 := (m t'.2.2 (by omega)).mpr (Or.inr (Or.inr rfl))
  obtain ⟨a, b, c⟩ := t
  obtain ⟨a', b', c'⟩ := t'
  simp only at *
  have ha : a = a' := by omega
  have hb : b = b' := by omega
  have hc : c = c' := by omega
  rw [ha, hb, hc]

theorem testBit_fullPairs {v x y : ℕ} (hxy : x < y) (hy : y < v) :
    (fullPairs v).testBit (v * x + y) = true := by
  rw [fullPairs, testBit_orAll]
  refine ⟨2 ^ (v * x + y), ?_, by simp⟩
  simp only [List.mem_flatMap, List.mem_range, List.mem_map, List.mem_filter,
    decide_eq_true_eq]
  exact ⟨x, by omega, y, ⟨hy, hxy⟩, rfl⟩

/-! ## Soundness -/

/-- **Soundness.**  If every system passes the kernel-evaluated `sysOK` check and no row is
repeated, the certificate names a large set of Kirkman triple systems in the frozen semantic
sense. -/
theorem isLKTS_of_check (v : ℕ) (d : List (List (List Row)))
    (hlen : d.length = v - 2)
    (hsys : ∀ s ∈ d, sysOK v (fullPairs v) s = true)
    (hnodup : (allRows d).Nodup)
    (hcard : (v - 2) * ((v - 1) / 2 * (v / 3)) = v.choose 3) :
    IsLKTS (blocksOf v d) := by
  -- abbreviations for systems and classes
  set S : ℕ → List (List Row) := fun i => d.getD i [] with hS
  set C : ℕ → ℕ → List Row := fun i c => (S i).getD c [] with hC
  have hrowAt : ∀ i c r, rowAt d i c r = (C i c).getD r (0, 0, 0) := fun _ _ _ => rfl
  have S_mem : ∀ i, i < v - 2 → S i ∈ d := by
    intro i hi
    simp only [hS]
    rw [getD_of_lt [] (by omega)]
    exact List.getElem_mem _
  have S_ok : ∀ i, i < v - 2 → (S i).length = (v - 1) / 2 ∧
      (∀ cls ∈ S i, classOK v cls = true) ∧
      accOK 0 ((S i).map (classPairs v)) (fullPairs v) = true := by
    intro i hi
    have := hsys (S i) (S_mem i hi)
    simpa only [sysOK, Bool.and_eq_true, beq_iff_eq, List.all_eq_true, and_assoc] using this
  have cls_ok : ∀ cls, classOK v cls = true → cls.length = v / 3 ∧
      (∀ t ∈ cls, rowOK v t = true) ∧ accOK 0 (cls.map ptMask) (2 ^ v - 1) = true := by
    intro cls h
    simpa only [classOK, Bool.and_eq_true, beq_iff_eq, List.all_eq_true, and_assoc] using h
  have C_mem : ∀ i c, i < v - 2 → c < (v - 1) / 2 → C i c ∈ S i := by
    intro i c hi hc
    simp only [hC]
    rw [getD_of_lt [] (by rw [(S_ok i hi).1]; exact hc)]
    exact List.getElem_mem _
  have C_ok : ∀ i c, i < v - 2 → c < (v - 1) / 2 → (C i c).length = v / 3 ∧
      (∀ t ∈ C i c, rowOK v t = true) ∧ accOK 0 ((C i c).map ptMask) (2 ^ v - 1) = true :=
    fun i c hi hc => cls_ok _ ((S_ok i hi).2.1 _ (C_mem i c hi hc))
  have row_mem : ∀ i c r, i < v - 2 → c < (v - 1) / 2 → r < v / 3 →
      rowAt d i c r ∈ C i c := by
    intro i c r hi hc hr
    rw [hrowAt, getD_of_lt _ (by rw [(C_ok i c hi hc).1]; exact hr)]
    exact List.getElem_mem _
  have row_ok : ∀ (i : Fin (v - 2)) (c : Fin ((v - 1) / 2)) (r : Fin (v / 3)),
      rowOK v (rowAt d i c r) = true :=
    fun i c r => (C_ok i c i.2 c.2).2.1 _ (row_mem i c r i.2 c.2 r.2)
  -- uniqueness of rows of a class sharing a point
  have pt_unique : ∀ i c r r', i < v - 2 → c < (v - 1) / 2 → r < v / 3 → r' < v / 3 →
      ∀ k, (ptMask (rowAt d i c r)).testBit k = true →
        (ptMask (rowAt d i c r')).testBit k = true → r = r' := by
    intro i c r r' hi hc hr hr' k h1 h2
    have hlen' := (C_ok i c hi hc).1
    have hp := (accOK_sound _ _ _ (C_ok i c hi hc).2.2).1
    exact eq_of_pairwise_map (f := ptMask) (0, 0, 0) hp (by omega) (by omega) h1 h2
  -- uniqueness of classes of a system sharing a pair
  have pair_unique : ∀ i c c', i < v - 2 → c < (v - 1) / 2 → c' < (v - 1) / 2 →
      ∀ t t' k, t ∈ C i c → t' ∈ C i c' → (pairMask v t).testBit k = true →
        (pairMask v t').testBit k = true → c = c' := by
    intro i c c' hi hc hc' t t' k ht ht' h1 h2
    have hlen' := (S_ok i hi).1
    have hp := (accOK_sound _ _ _ (S_ok i hi).2.2).1
    have b1 : (classPairs v (C i c)).testBit k = true :=
      (testBit_orAll _ _).mpr ⟨_, List.mem_map_of_mem ht, h1⟩
    have b2 : (classPairs v (C i c')).testBit k = true :=
      (testBit_orAll _ _).mpr ⟨_, List.mem_map_of_mem ht', h2⟩
    exact eq_of_pairwise_map (f := classPairs v) [] hp (by omega) (by omega) b1 b2
  -- uniqueness of systems containing the same row
  have sys_unique : ∀ i i' c c', i < v - 2 → i' < v - 2 → c < (v - 1) / 2 →
      c' < (v - 1) / 2 → ∀ t, t ∈ C i c → t ∈ C i' c' → i = i' := by
    intro i i' c c' hi hi' hc hc' t ht ht'
    have hpw := hnodup
    rw [List.Nodup, allRows, List.pairwise_flatten] at hpw
    have hsys2 := List.pairwise_iff_getElem.mp hpw.2
    have memi : ∀ j, j < v - 2 → ∀ cc, cc < (v - 1) / 2 → t ∈ C j cc →
        ∃ hj : j < (d.map List.flatten).length, t ∈ (d.map List.flatten)[j] := by
      intro j hj cc hcc htj
      refine ⟨by simp; omega, ?_⟩
      simp only [List.getElem_map]
      have : d[j]'(by omega) = S j := by simp only [hS]; rw [getD_of_lt [] (by omega)]
      rw [this, List.mem_flatten]
      exact ⟨C j cc, C_mem j cc hj hcc, htj⟩
    obtain ⟨hj1, m1⟩ := memi i hi c hc ht
    obtain ⟨hj2, m2⟩ := memi i' hi' c' hc' ht'
    rcases Nat.lt_trichotomy i i' with hlt | heq | hgt
    · exact absurd rfl (hsys2 i i' hj1 hj2 hlt t m1 t m2)
    · exact heq
    · exact absurd rfl (hsys2 i' i hj2 hj1 hgt t m2 t m1)
  -- the row map
  let F : Fin (v - 2) × Fin ((v - 1) / 2) × Fin (v / 3) → Triple v := fun p =>
    ⟨rowSet v (rowAt d p.1 p.2.1 p.2.2), card_rowSet (row_ok p.1 p.2.1 p.2.2)⟩
  have F_val : ∀ p, (F p).val = rowSet v (rowAt d p.1 p.2.1 p.2.2) := fun _ => rfl
  have F_inj : Function.Injective F := by
    rintro ⟨i, c, r⟩ ⟨i', c', r'⟩ h
    have hset : rowSet v (rowAt d i c r) = rowSet v (rowAt d i' c' r') := by
      simpa only [F_val] using congrArg Subtype.val h
    have hrow := row_eq_of_rowSet_eq (row_ok i c r) (row_ok i' c' r') hset
    have hii : i = i' := Fin.ext <| sys_unique i i' c c' i.2 i'.2 c.2 c'.2 _
      (row_mem i c r i.2 c.2 r.2) (hrow ▸ row_mem i' c' r' i'.2 c'.2 r'.2)
    subst hii
    have hbit : (pairMask v (rowAt d i c r)).testBit
        (v * (rowAt d i c r).1 + (rowAt d i c r).2.1) = true :=
      (testBit_pairMask _ _ _).mpr (Or.inl rfl)
    have hcc : c = c' := Fin.ext <| pair_unique i c c' i.2 c.2 c'.2 _ _ _
      (row_mem i c r i.2 c.2 r.2) (row_mem i c' r' i.2 c'.2 r'.2) hbit (hrow ▸ hbit)
    subst hcc
    have pbit : (ptMask (rowAt d i c r)).testBit (rowAt d i c r).1 = true :=
      (testBit_ptMask _ _).mpr (Or.inl rfl)
    have hrr : r = r' := Fin.ext <| pt_unique i c r r' i.2 c.2 r.2 r'.2 _ pbit (hrow ▸ pbit)
    subst hrr
    rfl
  have F_surj : Function.Surjective F := by
    have hb := (Fintype.bijective_iff_injective_and_card F).mpr ⟨F_inj, by
      rw [Fintype.card_prod, Fintype.card_prod, Fintype.card_fin, Fintype.card_fin,
        Fintype.card_fin, Fintype.card_finset_len, Fintype.card_fin]
      exact hcard⟩
    exact hb.2
  have mem_blocks : ∀ (i : Fin (v - 2)) (T : Triple v), T ∈ blocksOf v d i ↔
      ∃ c r, F (i, c, r) = T := by
    intro i T
    constructor
    · rintro ⟨c, r, hT⟩
      exact ⟨c, r, Subtype.ext (by rw [F_val]; exact hT.symm)⟩
    · rintro ⟨c, r, rfl⟩
      exact ⟨c, r, rfl⟩
  have mem_classes : ∀ (i : Fin (v - 2)) (c : Fin ((v - 1) / 2)) (T : Triple v),
      T ∈ classesOf v d i c ↔ ∃ r, F (i, c, r) = T := by
    intro i c T
    constructor
    · rintro ⟨r, hT⟩
      exact ⟨r, Subtype.ext (by rw [F_val]; exact hT.symm)⟩
    · rintro ⟨r, rfl⟩
      exact ⟨r, rfl⟩
  -- indices of a row from membership
  have row_index : ∀ (i : Fin (v - 2)) (c : Fin ((v - 1) / 2)) t, t ∈ C i c →
      ∃ r : Fin (v / 3), rowAt d i c r = t := by
    intro i c t ht
    obtain ⟨r, hr, e⟩ := exists_getD_of_mem (0, 0, 0) ht
    exact ⟨⟨r, by rw [← (C_ok i c i.2 c.2).1]; exact hr⟩, by rw [hrowAt]; exact e⟩
  have class_index : ∀ (i : Fin (v - 2)) cls, cls ∈ S i →
      ∃ c : Fin ((v - 1) / 2), C i c = cls := by
    intro i cls hcls
    obtain ⟨c, hc, e⟩ := exists_getD_of_mem [] hcls
    exact ⟨⟨c, by rw [← (S_ok i i.2).1]; exact hc⟩, e⟩
  refine ⟨Fintype.card_fin _, fun i => ?_, ?_, ?_⟩
  · -- each constituent is a KTS
    refine ⟨?_, classesOf v d i, ?_, ?_, ?_⟩
    · -- pair coverage with uniqueness
      have sts_ord : ∀ x y : Fin v, x.val < y.val →
          ∃! T : Triple v, T ∈ blocksOf v d i ∧ ({x, y} : Finset (Fin v)) ⊆ T.val := by
        intro x y hxy
        have hbit := testBit_fullPairs hxy y.2
        obtain ⟨-, -, hc⟩ := accOK_sound _ _ _ (S_ok i i.2).2.2
        obtain ⟨m, hm, hmb⟩ := ((hc _).mp hbit).resolve_left (by simp)
        obtain ⟨cls, hcls, rfl⟩ := List.mem_map.mp hm
        obtain ⟨m', hm', hm'b⟩ := (testBit_orAll _ _).mp hmb
        obtain ⟨t, ht, rfl⟩ := List.mem_map.mp hm'
        obtain ⟨c, rfl⟩ := class_index i cls hcls
        obtain ⟨r, rfl⟩ := row_index i c t ht
        obtain ⟨hx, hy⟩ := mem_of_pairMask_bit (row_ok i c r) y.2 hm'b
        refine ⟨F (i, c, r), ⟨(mem_blocks i _).mpr ⟨c, r, rfl⟩, ?_⟩, ?_⟩
        · intro z hz
          rw [F_val, mem_rowSet]
          rcases Finset.mem_insert.mp hz with rfl | hz
          · exact hx
          · rw [Finset.mem_singleton.mp hz]; exact hy
        · rintro T ⟨hT, hsub⟩
          obtain ⟨c', r', rfl⟩ := (mem_blocks i T).mp hT
          have hx' := mem_rowSet.mp (by rw [← F_val]; exact hsub (Finset.mem_insert_self x {y}))
          have hy' := mem_rowSet.mp (by
            rw [← F_val]; exact hsub (Finset.mem_insert_of_mem (Finset.mem_singleton_self y)))
          have b1 := pairMask_bit (row_ok i c r) hx hy hxy
          have b2 := pairMask_bit (row_ok i c' r') hx' hy' hxy
          have hcc : c' = c := Fin.ext <| pair_unique i c' c i.2 c'.2 c.2 _ _ _
            (row_mem i c' r' i.2 c'.2 r'.2) (row_mem i c r i.2 c.2 r.2) b2 b1
          subst hcc
          have p1 : (ptMask (rowAt d i c' r)).testBit x.val = true := by
            rw [testBit_ptMask]; rcases hx with h | h | h <;> simp [h]
          have p2 : (ptMask (rowAt d i c' r')).testBit x.val = true := by
            rw [testBit_ptMask]; rcases hx' with h | h | h <;> simp [h]
          have hrr : r' = r := Fin.ext <| pt_unique i c' r' r i.2 c'.2 r'.2 r.2 _ p2 p1
          rw [hrr]
      intro p
      obtain ⟨x, y, hxy, hp⟩ := Finset.card_eq_two.mp p.property
      rw [hp]
      rcases Nat.lt_or_gt_of_ne (Fin.val_ne_of_ne hxy) with h | h
      · exact sts_ord x y h
      · rw [Finset.pair_comm]; exact sts_ord y x h
    · -- parallel classes
      intro c x
      have hbit : (2 ^ v - 1).testBit x.val = true := by
        rw [Nat.testBit_two_pow_sub_one]; simp
      obtain ⟨-, -, hc⟩ := accOK_sound _ _ _ (C_ok i c i.2 c.2).2.2
      obtain ⟨m, hm, hmb⟩ := ((hc _).mp hbit).resolve_left (by simp)
      obtain ⟨t, ht, rfl⟩ := List.mem_map.mp hm
      obtain ⟨r, rfl⟩ := row_index i c t ht
      refine ⟨F (i, c, r), ⟨(mem_classes i c _).mpr ⟨r, rfl⟩, ?_⟩, ?_⟩
      · rw [F_val, mem_rowSet]
        rcases (testBit_ptMask _ _).mp hmb with h | h | h
        · exact Or.inl h.symm
        · exact Or.inr (Or.inl h.symm)
        · exact Or.inr (Or.inr h.symm)
      · rintro T ⟨hT, hxT⟩
        obtain ⟨r', rfl⟩ := (mem_classes i c T).mp hT
        rw [F_val, mem_rowSet] at hxT
        have p2 : (ptMask (rowAt d i c r')).testBit x.val = true := by
          rw [testBit_ptMask]; rcases hxT with h | h | h <;> simp [h]
        have hrr : r' = r := Fin.ext <| pt_unique i c r' r i.2 c.2 r'.2 r.2 _ p2 hmb
        rw [hrr]
    · -- distinct classes are disjoint
      intro c c' hcc
      apply Set.disjoint_left.mpr
      intro T h1 h2
      obtain ⟨r, rfl⟩ := (mem_classes i c T).mp h1
      obtain ⟨r', hr'⟩ := (mem_classes i c' _).mp h2
      have := F_inj hr'
      exact hcc (congrArg (fun p => p.2.1) this).symm
    · -- the classes exactly cover the constituent
      ext T
      simp only [Set.mem_iUnion]
      constructor
      · rintro ⟨c, hT⟩
        obtain ⟨r, rfl⟩ := (mem_classes i c T).mp hT
        exact (mem_blocks i _).mpr ⟨c, r, rfl⟩
      · intro hT
        obtain ⟨c, r, rfl⟩ := (mem_blocks i T).mp hT
        exact ⟨c, (mem_classes i c _).mpr ⟨r, rfl⟩⟩
  · -- distinct constituents are disjoint
    intro i j hij
    apply Set.disjoint_left.mpr
    intro T h1 h2
    obtain ⟨c, r, rfl⟩ := (mem_blocks i T).mp h1
    obtain ⟨c', r', hr'⟩ := (mem_blocks j _).mp h2
    have := F_inj hr'
    exact hij (congrArg (fun p => p.1) this).symm
  · -- every triple is covered
    apply Set.eq_univ_of_forall
    intro T
    obtain ⟨⟨i, c, r⟩, rfl⟩ := F_surj T
    exact Set.mem_iUnion.mpr ⟨i, (mem_blocks i _).mpr ⟨c, r, rfl⟩⟩

end Kirkman.KernelCert
