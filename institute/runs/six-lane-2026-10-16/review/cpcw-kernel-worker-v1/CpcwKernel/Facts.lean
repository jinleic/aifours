import CpcwKernel.Generic
import CpcwKernel.Optimality
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

/-!
# Generic consequences of the target definition (kernel-checked, data-free)

Nothing here is used by the roots `Cpcw.Kernel.exists_cpcw{v}k{k}`; these theorems only
document, in checked form, what `Cpcw.IsCPCW` means.

* `Cpcw.sub_eq_iff_modEq`: subtraction in `Fin v` is subtraction modulo `v`.
* `Cpcw.isCPCW_iff_diff_injective`: `Cpcw.IsCPCW B` says exactly that every codeword is injective
  and that distinct index triples `(i, j, l)` (`j ≠ l`) give distinct ordered differences.
* `Cpcw.isCPCW_iff_correlation`: `Cpcw.IsCPCW B` is equivalent to the correlation form of
  Definition 1 of Baicheva–Topalova (Axioms 15 (2026) 35): every codeword is a `k`-subset of
  `Fin v`; `|C_i ∩ (C_i + t)| ≤ 1` for `t ≠ 0`; `|C_i ∩ (C_j + t)| ≤ 1` for `i < j` and every `t`
  (`Cpcw.IsCorrelationCPCW`).
* `Cpcw.IsCPCW.codeword_injective`: for `2 ≤ k`, distinct indices give distinct codewords, so a
  family of `n` codewords is a collection of exactly `n` `k`-subsets.
* `Cpcw.IsCPCW.count_half`: if `2 * e = v`, the residue `e` (that is, `v / 2`) never occurs.
* `Cpcw.IsCPCW.packing`: for `2 ≤ k`, the development `{C_i + s}` is a strictly cyclic partial
  design (packing) on `Fin v` (`Cpcw.IsStrictlyCyclicPacking`).
* `Cpcw.bridge_of_target`: `Cpcw.Target v k` (with `2 ≤ k`) gives an optimal family with all of
  the above properties.
-/

namespace Cpcw

/-- Subtraction in `Fin v` is subtraction modulo `v`. -/
theorem sub_eq_iff_modEq {v : ℕ} (a b d : Fin v) :
    a - b = d ↔ ((d : ℕ) : ℤ) ≡ ((a : ℕ) : ℤ) - ((b : ℕ) : ℤ) [ZMOD v] := by
  have hb : (b : ℕ) < v := b.isLt
  have hd : (d : ℕ) < v := d.isLt
  rw [Fin.ext_iff, Fin.val_sub, Int.ModEq,
    Int.emod_eq_of_lt (Int.natCast_nonneg _) (by exact_mod_cast hd)]
  have key : (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)) % (v : ℤ) = (((v - b + a) % v : ℕ) : ℤ) := by
    rw [Int.natCast_emod, Nat.cast_add, Nat.cast_sub hb.le,
      show ((v : ℤ) - ((b : ℕ) : ℤ) + ((a : ℕ) : ℤ)) = (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)) + (v : ℤ) * 1
        by ring,
      Int.add_mul_emod_self_left]
  rw [key]
  constructor
  · intro h
    rw [h]
  · intro h
    exact_mod_cast h.symm

section Facts

variable {v k n : ℕ} [NeZero v]

/-! ## Difference form -/

/-- `Cpcw.IsCPCW B` says exactly: every codeword is injective, and distinct index triples
`(i, j, l)` with `j ≠ l` give distinct ordered differences `B i j - B i l`. -/
theorem isCPCW_iff_diff_injective (B : Fin n → Fin k → Fin v) :
    IsCPCW B ↔ (∀ i, Function.Injective (B i)) ∧
      ∀ t₁ t₂ : Fin n × Fin k × Fin k, t₁.2.1 ≠ t₁.2.2 → t₂.2.1 ≠ t₂.2.2 →
        B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2 = B t₂.1 t₂.2.1 - B t₂.1 t₂.2.2 → t₁ = t₂ := by
  constructor
  · rintro ⟨hinj, h1, h0⟩
    refine ⟨hinj, fun t₁ t₂ h₁ h₂ he => ?_⟩
    have hm₁ : t₁ ∈ ((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter
        fun t => t.2.1 ≠ t.2.2).filter
        fun t => B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2 = B t.1 t.2.1 - B t.1 t.2.2 := by
      simp [h₁]
    have hm₂ : t₂ ∈ ((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter
        fun t => t.2.1 ≠ t.2.2).filter
        fun t => B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2 = B t.1 t.2.1 - B t.1 t.2.2 := by
      simp [h₂, he]
    have hcount := Kernel.count_diffs B (B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2)
    by_cases hz : (B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2).val = 0
    · have h := h0 _ hz
      rw [hcount, Finset.card_eq_zero] at h
      rw [h] at hm₁
      simp at hm₁
    · have h := h1 _ hz
      rw [hcount, Finset.card_le_one] at h
      exact h t₁ hm₁ t₂ hm₂
  · rintro ⟨hinj, hdi⟩
    refine ⟨hinj, fun e _ => ?_, fun e he => ?_⟩
    · rw [Kernel.count_diffs, Finset.card_le_one]
      intro a ha b hb
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ha hb
      exact hdi a b ha.1 hb.1 (ha.2.symm.trans hb.2)
    · rw [Kernel.count_diffs, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
      intro t ht hte
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ht
      apply ht
      apply hinj t.1
      have he0 : e = 0 := Fin.val_eq_zero_iff.1 he
      rw [he0, eq_comm, sub_eq_zero] at hte
      exact hte

/-! ## Correlation form (Definition 1 of the primary source) -/

/-- Codeword `i` of `B` as a subset of `Fin v`. -/
def codeword (B : Fin n → Fin k → Fin v) (i : Fin n) : Finset (Fin v) :=
  Finset.univ.image (B i)

/-- The translate `C + t = {c + t | c ∈ C}`. -/
def translate (C : Finset (Fin v)) (t : Fin v) : Finset (Fin v) :=
  C.image (· + t)

omit [NeZero v] in
theorem mem_codeword {B : Fin n → Fin k → Fin v} {i : Fin n} {x : Fin v} :
    x ∈ codeword B i ↔ ∃ j, B i j = x := by
  simp [codeword]

omit [NeZero v] in
theorem mem_translate {C : Finset (Fin v)} {t x : Fin v} :
    x ∈ translate C t ↔ ∃ y ∈ C, y + t = x := by
  simp [translate]

omit [NeZero v] in
theorem card_codeword_iff (B : Fin n → Fin k → Fin v) (i : Fin n) :
    (codeword B i).card = k ↔ Function.Injective (B i) := by
  constructor
  · intro h
    have h' : (Finset.univ.image (B i)).card = (Finset.univ : Finset (Fin k)).card := by
      rw [Finset.card_univ, Fintype.card_fin]
      exact h
    rw [Finset.card_image_iff, Finset.coe_univ, Set.injOn_univ] at h'
    exact h'
  · intro h
    rw [codeword, Finset.card_image_of_injective _ h, Finset.card_univ, Fintype.card_fin]

/-- Definition 1 of Baicheva–Topalova (Axioms 15 (2026) 35, p. 1) for the codewords
`C_i = codeword B i`: each `C_i` is a `k`-subset of `Fin v`, and
(1) `|C_i ∩ (C_i + t)| ≤ 1` for `1 ≤ t ≤ v - 1`,
(2) `|C_i ∩ (C_j + t)| ≤ 1` for `i < j` and `0 ≤ t ≤ v - 1`. -/
def IsCorrelationCPCW (B : Fin n → Fin k → Fin v) : Prop :=
  (∀ i, (codeword B i).card = k) ∧
    (∀ i, ∀ t : Fin v, t ≠ 0 → (codeword B i ∩ translate (codeword B i) t).card ≤ 1) ∧
    (∀ i j : Fin n, i < j → ∀ t : Fin v, (codeword B i ∩ translate (codeword B j) t).card ≤ 1)

theorem corr_of_diff_injective {B : Fin n → Fin k → Fin v}
    (hdi : ∀ t₁ t₂ : Fin n × Fin k × Fin k, t₁.2.1 ≠ t₁.2.2 → t₂.2.1 ≠ t₂.2.2 →
        B t₁.1 t₁.2.1 - B t₁.1 t₁.2.2 = B t₂.1 t₂.2.1 - B t₂.1 t₂.2.2 → t₁ = t₂)
    (i i' : Fin n) (t : Fin v) (hne : (i, (0 : Fin v)) ≠ (i', t)) :
    (codeword B i ∩ translate (codeword B i') t).card ≤ 1 := by
  rw [Finset.card_le_one]
  intro a ha b hb
  by_contra hab
  rw [Finset.mem_inter, mem_codeword, mem_translate] at ha hb
  obtain ⟨⟨j, hj⟩, y, hy, hya⟩ := ha
  obtain ⟨⟨l, hl⟩, z, hz, hzb⟩ := hb
  obtain ⟨j', rfl⟩ := mem_codeword.1 hy
  obtain ⟨l', rfl⟩ := mem_codeword.1 hz
  have hjl : j ≠ l := by
    rintro rfl
    exact hab (hj.symm.trans hl)
  have hjl' : j' ≠ l' := by
    rintro rfl
    exact hab (hya.symm.trans hzb)
  have hd : B i j - B i l = B i' j' - B i' l' := by
    rw [hj, hl, ← hya, ← hzb]
    abel
  have e := hdi (i, j, l) (i', j', l') hjl hjl' hd
  simp only [Prod.mk.injEq] at e
  obtain ⟨rfl, rfl, rfl⟩ := e
  apply hne
  have h2 : B i j + t = B i j + 0 := by
    rw [add_zero, hya, hj]
  rw [add_left_cancel h2]

/-- **Difference form ⇔ correlation form (Definition 1).** -/
theorem isCPCW_iff_correlation (B : Fin n → Fin k → Fin v) : IsCPCW B ↔ IsCorrelationCPCW B := by
  rw [isCPCW_iff_diff_injective]
  constructor
  · rintro ⟨hinj, hdi⟩
    refine ⟨fun i => (card_codeword_iff B i).2 (hinj i),
      fun i t ht => corr_of_diff_injective hdi i i t ?_,
      fun i j hij t => corr_of_diff_injective hdi i j t ?_⟩
    · intro h
      simp only [Prod.mk.injEq] at h
      exact ht h.2.symm
    · intro h
      simp only [Prod.mk.injEq] at h
      exact (ne_of_lt hij) h.1
  · rintro ⟨hcard, h1, h2⟩
    have hinj : ∀ i, Function.Injective (B i) := fun i => (card_codeword_iff B i).1 (hcard i)
    refine ⟨hinj, ?_⟩
    rintro ⟨i, j, l⟩ ⟨i', j', l'⟩ h₁ h₂ hd
    simp only at h₁ h₂ hd
    have ha : B i j ∈ codeword B i ∩ translate (codeword B i') (B i j - B i' j') := by
      rw [Finset.mem_inter, mem_codeword, mem_translate]
      exact ⟨⟨j, rfl⟩, B i' j', mem_codeword.2 ⟨j', rfl⟩, by abel⟩
    have hb : B i l ∈ codeword B i ∩ translate (codeword B i') (B i j - B i' j') := by
      rw [Finset.mem_inter, mem_codeword, mem_translate]
      refine ⟨⟨l, rfl⟩, B i' l', mem_codeword.2 ⟨l', rfl⟩, ?_⟩
      have hl : B i l = B i j - (B i' j' - B i' l') := by
        rw [← hd]
        abel
      rw [hl]
      abel
    have hab : B i j ≠ B i l := fun h => h₁ (hinj i h)
    have hlt : 1 < (codeword B i ∩ translate (codeword B i') (B i j - B i' j')).card :=
      Finset.one_lt_card.2 ⟨_, ha, _, hb, hab⟩
    rcases lt_trichotomy i i' with hii | rfl | hii
    · exact absurd (h2 i i' hii (B i j - B i' j')) (by omega)
    · by_cases hτ : B i j - B i j' = 0
      · rw [sub_eq_zero] at hτ
        have hj : j = j' := hinj i hτ
        subst hj
        have hl : B i l = B i l' := by
          have e : B i l = B i j - (B i j - B i l') := by
            rw [← hd]
            abel
          rw [e]
          abel
        rw [hinj i hl]
      · exact absurd (h1 i _ hτ) (by omega)
    · have ha' : B i' j' ∈ codeword B i' ∩ translate (codeword B i) (-(B i j - B i' j')) := by
        rw [Finset.mem_inter, mem_codeword, mem_translate]
        exact ⟨⟨j', rfl⟩, B i j, mem_codeword.2 ⟨j, rfl⟩, by abel⟩
      have hb' : B i' l' ∈ codeword B i' ∩ translate (codeword B i) (-(B i j - B i' j')) := by
        rw [Finset.mem_inter, mem_codeword, mem_translate]
        refine ⟨⟨l', rfl⟩, B i l, mem_codeword.2 ⟨l, rfl⟩, ?_⟩
        have hl : B i l = B i j - (B i' j' - B i' l') := by
          rw [← hd]
          abel
        rw [hl]
        abel
      have hab' : B i' j' ≠ B i' l' := fun h => h₂ (hinj i' h)
      have hlt' := Finset.one_lt_card.2 ⟨_, ha', _, hb', hab'⟩
      exact absurd (h2 i' i hii (-(B i j - B i' j'))) (by omega)

/-- For `2 ≤ k`, distinct indices give distinct codewords: a family of `n` codewords is a
collection of exactly `n` distinct `k`-subsets. -/
theorem IsCPCW.codeword_injective (hk : 2 ≤ k) {B : Fin n → Fin k → Fin v} (h : IsCPCW B) :
    Function.Injective (codeword B) := by
  intro i j hij
  by_contra hne
  obtain ⟨hcard, -, h2⟩ := (isCPCW_iff_correlation B).1 h
  have htr : ∀ C : Finset (Fin v), translate C 0 = C := fun C => by
    simp [translate]
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · have h' := h2 i j hlt 0
    rw [htr, ← hij, Finset.inter_self, hcard] at h'
    omega
  · have h' := h2 j i hlt 0
    rw [htr, hij, Finset.inter_self, hcard] at h'
    omega

/-- If `2 * e = v` (so `e = v / 2` with `v` even), the residue `e` is never an ordered difference
of a `(v, k, 1)` CPCW code. -/
theorem IsCPCW.count_half {B : Fin n → Fin k → Fin v} (h : IsCPCW B) (e : Fin v)
    (he : 2 * e.val = v) : (diffs B).count e = 0 := by
  obtain ⟨-, hdi⟩ := (isCPCW_iff_diff_injective B).1 h
  rw [Kernel.count_diffs, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
  intro t ht hte
  simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ht
  have hee : e + e = 0 := Fin.ext (by rw [Fin.val_add, Fin.val_zero, ← two_mul, he, Nat.mod_self])
  have hneg : B t.1 t.2.2 - B t.1 t.2.1 = B t.1 t.2.1 - B t.1 t.2.2 := by
    rw [← neg_sub, ← hte, neg_eq_of_add_eq_zero_left hee]
  have e' := hdi (t.1, t.2.2, t.2.1) t (Ne.symm ht) ht hneg
  exact ht (congrArg (fun s : Fin n × Fin k × Fin k => s.2.1) e').symm

/-! ## The development: a strictly cyclic partial design (packing) -/

/-- Block `p = (i, s)` of the development of `B`: the translate `C_i + s`. -/
def devBlock (B : Fin n → Fin k → Fin v) (p : Fin n × Fin v) : Finset (Fin v) :=
  Finset.univ.image fun j => B p.1 j + p.2

omit [NeZero v] in
theorem mem_devBlock {B : Fin n → Fin k → Fin v} {x : Fin v} {p : Fin n × Fin v} :
    x ∈ devBlock B p ↔ ∃ j, B p.1 j + p.2 = x := by
  simp [devBlock]

/-- The development of `B` is a strictly cyclic partial design (packing) `2-(v, k, 1)` on the
point set `Fin v`: its `n * v` blocks `devBlock B p` (`p : Fin n × Fin v`) have `k` points each;
any two distinct points lie together in at most one block; distinct indices give distinct blocks;
and translation by any `t` maps block `(i, s)` to block `(i, s + t)`.  So `x ↦ x + 1` is an
automorphism permuting the points in one cycle, and (by injectivity) each of the `n` block orbits
`{(i, s + t) | t : Fin v}` has full length `v`. -/
def IsStrictlyCyclicPacking (B : Fin n → Fin k → Fin v) : Prop :=
  (∀ p, (devBlock B p).card = k) ∧
    (∀ x y : Fin v, x ≠ y → ∀ p q : Fin n × Fin v,
      x ∈ devBlock B p → y ∈ devBlock B p → x ∈ devBlock B q → y ∈ devBlock B q → p = q) ∧
    Function.Injective (devBlock B) ∧
    (∀ p t, (devBlock B p).image (· + t) = devBlock B (p.1, p.2 + t))

theorem devBlock_translate (B : Fin n → Fin k → Fin v) (p : Fin n × Fin v) (t : Fin v) :
    (devBlock B p).image (· + t) = devBlock B (p.1, p.2 + t) := by
  ext x
  simp only [devBlock, Finset.mem_image, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨y, ⟨j, rfl⟩, rfl⟩
    exact ⟨j, by abel⟩
  · rintro ⟨j, rfl⟩
    exact ⟨B p.1 j + p.2, ⟨j, rfl⟩, by abel⟩

/-- **Semantic bridge: CPCW ⇒ strictly cyclic packing of the development.** -/
theorem IsCPCW.packing (hk : 2 ≤ k) {B : Fin n → Fin k → Fin v} (h : IsCPCW B) :
    IsStrictlyCyclicPacking B := by
  obtain ⟨hinj, hdi⟩ := (isCPCW_iff_diff_injective B).1 h
  have hcard : ∀ p, (devBlock B p).card = k := fun p => by
    rw [devBlock, Finset.card_image_of_injective _ fun j l hjl => hinj p.1 (add_right_cancel hjl),
      Finset.card_univ, Fintype.card_fin]
  have hpair : ∀ x y : Fin v, x ≠ y → ∀ p q : Fin n × Fin v,
      x ∈ devBlock B p → y ∈ devBlock B p → x ∈ devBlock B q → y ∈ devBlock B q → p = q := by
    rintro x y hxy ⟨i, s⟩ ⟨i', s'⟩ hxp hyp hxq hyq
    obtain ⟨j, hj⟩ := mem_devBlock.1 hxp
    obtain ⟨l, hl⟩ := mem_devBlock.1 hyp
    obtain ⟨j', hj'⟩ := mem_devBlock.1 hxq
    obtain ⟨l', hl'⟩ := mem_devBlock.1 hyq
    dsimp only at hj hl hj' hl'
    have hjl : j ≠ l := by
      rintro rfl
      exact hxy (hj.symm.trans hl)
    have hjl' : j' ≠ l' := by
      rintro rfl
      exact hxy (hj'.symm.trans hl')
    have hd : B i j - B i l = B i' j' - B i' l' := by
      have e1 : B i j - B i l = x - y := by
        rw [← hj, ← hl]
        abel
      have e2 : B i' j' - B i' l' = x - y := by
        rw [← hj', ← hl']
        abel
      rw [e1, e2]
    have e := hdi (i, j, l) (i', j', l') hjl hjl' hd
    simp only [Prod.mk.injEq] at e
    obtain ⟨rfl, rfl, rfl⟩ := e
    rw [← hj'] at hj
    rw [add_left_cancel hj]
  refine ⟨hcard, hpair, fun p q hpq => ?_, devBlock_translate B⟩
  have h2 : 1 < (devBlock B p).card := by
    rw [hcard p]
    omega
  obtain ⟨x, hx, y, hy, hxy⟩ := Finset.one_lt_card.1 h2
  exact hpair x y hxy p q hx hy (hpq ▸ hx) (hpq ▸ hy)

/-- Existence form of the bridges: `Cpcw.Target v k` (with `2 ≤ k`) gives an optimal family that
satisfies Definition 1, has `n` distinct codewords, never uses the difference `v / 2` (for even
`v`), and develops into a strictly cyclic packing. -/
theorem bridge_of_target (hk : 2 ≤ k) (h : Target v k) :
    ∃ n : ℕ, ∃ B : Fin n → Fin k → Fin v, IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧
      Function.Injective (codeword B) ∧ (∀ e : Fin v, 2 * e.val = v → (diffs B).count e = 0) ∧
      IsStrictlyCyclicPacking B := by
  obtain ⟨n, B, hB, hn⟩ := h
  exact ⟨n, B, ⟨hB, hn⟩, (isCPCW_iff_correlation B).1 hB, hB.codeword_injective hk,
    hB.count_half, hB.packing hk⟩

end Facts

end Cpcw
