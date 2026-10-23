import CdfKernel.Target
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

/-!
# Generic consequences of the target definition (kernel-checked, data-free)

Nothing here is used by the roots `Cdf.Kernel.exists_cdf{v}`; these theorems only document, in
checked form, what `Cdf.IsCDF` means.

* `Cdf.sub_eq_iff_modEq`: subtraction in `Fin v` is subtraction modulo `v`.
* `Cdf.IsCDF.existsUnique`: every nonzero residue is `B i j - B i k` for exactly one block `i` and
  ordered pair of distinct positions `(j, k)`.
* `Cdf.IsCDF.card_eq`: a family satisfying `Cdf.IsCDF` has exactly `(v - 1) / 20` blocks
  (`20 * n = v - 1`).
* `Cdf.IsCDF.steiner`: the development `{B i + s}` is a strictly cyclic Steiner system
  `S(2, 5, v)` on the points `Fin v` (`Cdf.IsStrictlyCyclicSteiner`).
* `Cdf.IsCDF.ooc`: the base blocks form a perfect `(v, 5, 1)` optical orthogonal code: weight 5,
  periodic auto- and cross-correlation at most `1`, and `20 * n = v - 1` (`Cdf.IsPerfectOOC`).
* `Cdf.bridge_of_target`: `Cdf.Target v` gives a family with all three properties.
-/

namespace Cdf

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

/-- Under `Cdf.IsCDF`, every nonzero residue is an ordered difference of distinct positions of a
base block in exactly one way. -/
theorem IsCDF.existsUnique {v n : ℕ} {B : Fin n → Fin 5 → Fin v} (h : IsCDF B) (d : Fin v)
    (hd : d.val ≠ 0) :
    ∃! t : Fin n × Fin 5 × Fin 5, t.2.1 ≠ t.2.2 ∧ B t.1 t.2.1 - B t.1 t.2.2 = d := by
  have h1 := h.2.1 d hd
  rw [diffs, Multiset.count_map, ← Finset.filter_val] at h1
  obtain ⟨t, ht⟩ := Finset.card_eq_one.1 h1
  have mem : ∀ t' : Fin n × Fin 5 × Fin 5,
      (t'.2.1 ≠ t'.2.2 ∧ B t'.1 t'.2.1 - B t'.1 t'.2.2 = d) ↔ t' = t := by
    intro t'
    have e := Finset.ext_iff.1 ht t'
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton] at e
    rw [← e]
    exact and_congr_right fun _ => eq_comm
  exact ⟨t, (mem t).2 rfl, fun t' ht' => (mem t').1 ht'⟩

theorem card_positions (n : ℕ) :
    ((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).card =
      n * 20 := by
  rw [← Finset.univ_product_univ, Finset.filter_product_right (fun p : Fin 5 × Fin 5 => p.1 ≠ p.2),
    Finset.card_product, Finset.card_univ, Fintype.card_fin]
  rfl

theorem card_nonzero (v : ℕ) :
    ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card = v - 1 := by
  rcases Nat.eq_zero_or_pos v with rfl | hv
  · simp
  · have e : ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0) =
        Finset.univ.erase ⟨0, hv⟩ := by
      ext x
      simp [Fin.ext_iff]
    rw [e, Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]

/-- Under `Cdf.IsCDF` there are exactly `(v - 1) / 20` base blocks. -/
theorem IsCDF.card_eq {v n : ℕ} {B : Fin n → Fin 5 → Fin v} (h : IsCDF B) : 20 * n = v - 1 := by
  have hcard : Multiset.card (diffs B) = n * 20 := by
    rw [diffs, Multiset.card_map]
    exact card_positions n
  have hsum : ∑ e : Fin v, (diffs B).count e = Multiset.card (diffs B) :=
    Multiset.sum_count_eq_card fun a _ => Finset.mem_univ a
  have hsum' : ∑ e : Fin v, (diffs B).count e =
      ((Finset.univ : Finset (Fin v)).filter fun e => e.val ≠ 0).card := by
    rw [Finset.card_filter]
    refine Finset.sum_congr rfl fun e _ => ?_
    by_cases he : e.val = 0
    · rw [h.2.2 e he]
      simp [he]
    · rw [h.2.1 e he]
      simp [he]
  rw [card_nonzero] at hsum'
  omega

/-! ## The development: a strictly cyclic Steiner system `S(2, 5, v)` -/

section Development

variable {v n : ℕ} {B : Fin n → Fin 5 → Fin v}

/-- Block `p = (i, s)` of the development of `B`: the translate `B i + s` of base block `i`, as a
set of points of `Fin v`. -/
def devBlock (B : Fin n → Fin 5 → Fin v) (p : Fin n × Fin v) : Finset (Fin v) :=
  Finset.univ.image fun j => B p.1 j + p.2

theorem mem_devBlock {x : Fin v} {p : Fin n × Fin v} :
    x ∈ devBlock B p ↔ ∃ j, B p.1 j + p.2 = x := by
  simp [devBlock]

theorem IsCDF.card_devBlock (h : IsCDF B) (p : Fin n × Fin v) : (devBlock B p).card = 5 := by
  rw [devBlock, Finset.card_image_of_injective _ fun j k hjk => h.1 p.1 (add_right_cancel hjk),
    Finset.card_univ, Fintype.card_fin]

variable [NeZero v]

theorem val_sub_ne_zero {x y : Fin v} (hxy : x ≠ y) : (x - y).val ≠ 0 := by
  rw [Ne, Fin.val_eq_zero_iff, sub_eq_zero]
  exact hxy

/-- Any two distinct points lie in exactly one block of the development. -/
theorem IsCDF.existsUnique_block (h : IsCDF B) {x y : Fin v} (hxy : x ≠ y) :
    ∃! p : Fin n × Fin v, x ∈ devBlock B p ∧ y ∈ devBlock B p := by
  obtain ⟨⟨i, j, k⟩, ⟨-, hd⟩, huniq⟩ := h.existsUnique (x - y) (val_sub_ne_zero hxy)
  dsimp only at hd
  refine ⟨(i, x - B i j), ⟨mem_devBlock.2 ⟨j, ?_⟩, mem_devBlock.2 ⟨k, ?_⟩⟩, ?_⟩
  · show B i j + (x - B i j) = x
    abel
  · have hy : y = x - (B i j - B i k) := by
      rw [hd]
      abel
    show B i k + (x - B i j) = y
    rw [hy]
    abel
  · rintro ⟨i', s'⟩ ⟨hx, hy⟩
    obtain ⟨j', hj'⟩ := mem_devBlock.1 hx
    obtain ⟨k', hk'⟩ := mem_devBlock.1 hy
    dsimp only at hj' hk'
    have hne : j' ≠ k' := by
      rintro rfl
      exact hxy (hj'.symm.trans hk')
    have hd' : B i' j' - B i' k' = x - y := by
      rw [← hj', ← hk']
      abel
    have e := huniq (i', j', k') ⟨hne, hd'⟩
    simp only [Prod.mk.injEq] at e
    obtain ⟨rfl, rfl, rfl⟩ := e
    rw [Prod.mk.injEq]
    refine ⟨rfl, ?_⟩
    rw [← hj']
    abel

/-- Distinct indices give distinct blocks of the development. -/
theorem IsCDF.devBlock_injective (h : IsCDF B) : Function.Injective (devBlock B) := by
  intro p q hpq
  have h2 : 1 < (devBlock B p).card := by
    rw [h.card_devBlock p]
    decide
  obtain ⟨x, hx, y, hy, hxy⟩ := Finset.one_lt_card.1 h2
  obtain ⟨r, -, hr⟩ := h.existsUnique_block hxy
  exact (hr p ⟨hx, hy⟩).trans (hr q ⟨hpq ▸ hx, hpq ▸ hy⟩).symm

/-- Translation by `t` maps block `(i, s)` of the development to block `(i, s + t)`. -/
theorem devBlock_translate (p : Fin n × Fin v) (t : Fin v) :
    (devBlock B p).image (· + t) = devBlock B (p.1, p.2 + t) := by
  ext x
  simp only [devBlock, Finset.mem_image, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨y, ⟨j, rfl⟩, rfl⟩
    refine ⟨j, ?_⟩
    show B p.1 j + (p.2 + t) = B p.1 j + p.2 + t
    abel
  · rintro ⟨j, rfl⟩
    refine ⟨B p.1 j + p.2, ⟨j, rfl⟩, ?_⟩
    show B p.1 j + p.2 + t = B p.1 j + (p.2 + t)
    abel

/-- The development of `B` is a strictly cyclic Steiner system `S(2, 5, v)` on the point set
`Fin v`: its `n * v` blocks `devBlock B p` (`p : Fin n × Fin v`) have five points each; any two
distinct points lie in exactly one block; distinct indices give distinct blocks; and translation
by any `t` maps block `(i, s)` to block `(i, s + t)`.  So `x ↦ x + 1` is an automorphism of order
`v` permuting the blocks, and (by injectivity) each of its `n` block orbits
`{(i, s + t) | t : Fin v}` has full length `v`. -/
def IsStrictlyCyclicSteiner {v n : ℕ} (B : Fin n → Fin 5 → Fin v) : Prop :=
  (∀ p, (devBlock B p).card = 5) ∧
    (∀ x y : Fin v, x ≠ y → ∃! p : Fin n × Fin v, x ∈ devBlock B p ∧ y ∈ devBlock B p) ∧
    Function.Injective (devBlock B) ∧
    (∀ p t, (devBlock B p).image (· + t) = devBlock B (p.1, p.2 + t))

/-- The base blocks of `B` form a perfect `(v, 5, 1)` optical orthogonal code: the codewords
`devBlock B (i, 0) = {B i 0, ..., B i 4}` have weight `5`; for every pair `(i, i')` and shift
`τ` other than the trivial `i = i'`, `τ = 0`, codeword `i` meets the `τ`-translate of codeword
`i'` in at most one point (periodic auto-correlation for `i = i'`, `τ ≠ 0`, and cross-correlation
for `i ≠ i'`, at most `1`); and the number of codewords meets the Johnson bound with equality,
`20 * n = v - 1`. -/
def IsPerfectOOC {v n : ℕ} [NeZero v] (B : Fin n → Fin 5 → Fin v) : Prop :=
  (∀ i, (devBlock B (i, 0)).card = 5) ∧
    (∀ i i' : Fin n, ∀ τ : Fin v, (i, (0 : Fin v)) ≠ (i', τ) →
      (devBlock B (i, 0) ∩ devBlock B (i', τ)).card ≤ 1) ∧
    20 * n = v - 1

/-- **Semantic bridge: CDF ⇒ strictly cyclic `S(2, 5, v)`.** -/
theorem IsCDF.steiner (h : IsCDF B) : IsStrictlyCyclicSteiner B :=
  ⟨h.card_devBlock, fun _ _ hxy => h.existsUnique_block hxy, h.devBlock_injective,
    devBlock_translate⟩

/-- **Semantic bridge: CDF ⇒ perfect `(v, 5, 1)` optical orthogonal code.** -/
theorem IsCDF.ooc (h : IsCDF B) : IsPerfectOOC B := by
  refine ⟨fun i => h.card_devBlock (i, 0),
    fun i i' τ hne => Finset.card_le_one.2 fun a ha b hb => ?_, h.card_eq⟩
  by_contra hab
  rw [Finset.mem_inter] at ha hb
  obtain ⟨r, -, hr⟩ := h.existsUnique_block hab
  exact hne ((hr _ ⟨ha.1, hb.1⟩).trans (hr _ ⟨ha.2, hb.2⟩).symm)

/-- Existence form of both bridges. -/
theorem bridge_of_target (h : Target v) :
    ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin v, IsCDF B ∧ IsStrictlyCyclicSteiner B ∧ IsPerfectOOC B := by
  obtain ⟨n, B, hB⟩ := h
  exact ⟨n, B, hB, hB.steiner, hB.ooc⟩

end Development

end Cdf
