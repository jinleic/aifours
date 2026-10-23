import BTDKernel.Target
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# BTD(14,18;7,1,9;7,4) does not exist: the proof

Formalization of `notes/nonexistence-proof-r1.md` of lane
`information-science/evidence/six-lane-20261016/btd14-18`.  With `G = MᵀM` and `H = 63 I - 9 G + 28 J`:

* Step 1: `H * H = 63 • H`, `H * J = 0` (`HH`, `HJ`); `H j j = 28 - 18 c_j` (`H_diag`); off-diagonal entries are
  `1 mod 9` (`H_off_mod`).
* Step 2: positivity through `∑ₘ (H x)ₘ² = 63 xᵀHx` (`H_col_dot`): `H j j ≥ 0` (`H_diag_nonneg`), Cauchy–Schwarz
  `H j k ² ≤ H j j H k k` (`H_cs`), and the explicit sums of squares inside `eqcols`, `lemmaF` and `no_btd`.
* Step 3: `c_j ≤ 1`; 14 columns with one `2`, 4 columns without (`c_le_one`, `counts`).
* Step 4: next to a type-1 column all entries are `-8`, `1` or `10` (`type1_vals`); exactly three entries `10`
  (itself included) and five entries `-8` in its row (`card10`, `card_m8`).
* Step 5: (E) `H a k = 10` between type-1 columns makes the `H`-columns equal (`eqcols`); (F) two `-8` from a type-1
  column to type-1 columns force `10` between them (`lemmaF`).
* Step 6: Lemma D4, `729 d² = 7¹⁰ det H[{a,b,u,c}]` (`lemmaD4`), the 4 × 4 determinant (`det4_pattern`) and the
  two excluded values `3645`, `-2187` (`bad_det4`).
* Step 7: closure (`no_btd`).
-/

namespace BTD14

open Finset Matrix

/-- all-ones matrices -/
def J (m n : Type) : Matrix m n ℤ := Matrix.of fun _ _ => 1

lemma val_eq (x : ℤ) (hx : x = 0 ∨ x = 1 ∨ x = 2) :
    x = (if x = 1 then 1 else 0) + 2 * (if x = 2 then 1 else 0) := by
  rcases hx with h | h | h <;> subst h <;> norm_num

lemma sq_eq (x : ℤ) (hx : x = 0 ∨ x = 1 ∨ x = 2) :
    x * x = (if x = 1 then 1 else 0) + 4 * (if x = 2 then 1 else 0) := by
  rcases hx with h | h | h <;> subst h <;> norm_num

variable {M : Matrix (Fin 14) (Fin 18) ℤ}

lemma row_sq (hM : IsBTD M) (i : Fin 14) : ∑ j, M i j * M i j = 11 := by
  obtain ⟨hv, h1, h2, -, -⟩ := hM
  calc ∑ j, M i j * M i j
        = ∑ j, ((if M i j = 1 then (1 : ℤ) else 0) + 4 * (if M i j = 2 then 1 else 0)) :=
          Finset.sum_congr rfl fun j _ => sq_eq _ (hv i j)
    _ = ((univ.filter fun j => M i j = 1).card : ℤ) + 4 * (univ.filter fun j => M i j = 2).card := by
          rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]
    _ = 11 := by rw [h1 i, h2 i]; norm_num

lemma row_sum (hM : IsBTD M) (i : Fin 14) : ∑ j, M i j = 9 := by
  obtain ⟨hv, h1, h2, -, -⟩ := hM
  calc ∑ j, M i j
        = ∑ j, ((if M i j = 1 then (1 : ℤ) else 0) + 2 * (if M i j = 2 then 1 else 0)) :=
          Finset.sum_congr rfl fun j _ => val_eq _ (hv i j)
    _ = ((univ.filter fun j => M i j = 1).card : ℤ) + 2 * (univ.filter fun j => M i j = 2).card := by
          rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]
    _ = 9 := by rw [h1 i, h2 i]; norm_num

/-- number of entries `2` in column `j` -/
def c (M : Matrix (Fin 14) (Fin 18) ℤ) (j : Fin 18) : ℕ := (univ.filter fun i => M i j = 2).card

lemma col_sq (hM : IsBTD M) (j : Fin 18) : ∑ i, M i j * M i j = 7 + 2 * (c M j : ℤ) := by
  obtain ⟨hv, -, -, hc, -⟩ := hM
  have h1 : ∑ i, M i j = ((univ.filter fun i => M i j = 1).card : ℤ) + 2 * (c M j : ℤ) := by
    calc ∑ i, M i j
          = ∑ i, ((if M i j = 1 then (1 : ℤ) else 0) + 2 * (if M i j = 2 then 1 else 0)) :=
            Finset.sum_congr rfl fun i _ => val_eq _ (hv i j)
      _ = _ := by rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]; rfl
  have h2 : ∑ i, M i j * M i j = ((univ.filter fun i => M i j = 1).card : ℤ) + 4 * (c M j : ℤ) := by
    calc ∑ i, M i j * M i j
          = ∑ i, ((if M i j = 1 then (1 : ℤ) else 0) + 4 * (if M i j = 2 then 1 else 0)) :=
            Finset.sum_congr rfl fun i _ => sq_eq _ (hv i j)
      _ = _ := by rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]; rfl
  rw [hc j] at h1
  linarith

lemma MMt (hM : IsBTD M) : M * Mᵀ = (7 : ℤ) • (1 : Matrix (Fin 14) (Fin 14) ℤ) + (4 : ℤ) • J (Fin 14) (Fin 14) := by
  ext i k
  simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, J,
    Matrix.of_apply, smul_eq_mul]
  by_cases h : i = k
  · subst h; rw [row_sq hM i]; simp
  · rw [hM.2.2.2.2 i k h]; simp [h]

lemma MtJ (hM : IsBTD M) : Mᵀ * J (Fin 14) (Fin 18) = (7 : ℤ) • J (Fin 18) (Fin 18) := by
  ext j k
  simp only [Matrix.mul_apply, Matrix.transpose_apply, J, Matrix.of_apply, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 j]

lemma MJ (hM : IsBTD M) : M * J (Fin 18) (Fin 18) = (9 : ℤ) • J (Fin 14) (Fin 18) := by
  ext i k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [row_sum hM i]

lemma JM (hM : IsBTD M) : J (Fin 18) (Fin 14) * M = (7 : ℤ) • J (Fin 18) (Fin 18) := by
  ext j k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 k]

lemma JJ18 : J (Fin 18) (Fin 18) * J (Fin 18) (Fin 18) = (18 : ℤ) • J (Fin 18) (Fin 18) := by
  ext j k
  simp [Matrix.mul_apply, J]

lemma J14M (hM : IsBTD M) : J (Fin 14) (Fin 14) * M = (7 : ℤ) • J (Fin 14) (Fin 18) := by
  ext i k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 k]

/-- the column Gram matrix -/
def G (M : Matrix (Fin 14) (Fin 18) ℤ) : Matrix (Fin 18) (Fin 18) ℤ := Mᵀ * M

lemma GG (hM : IsBTD M) : G M * G M = (7 : ℤ) • G M + (196 : ℤ) • J (Fin 18) (Fin 18) := by
  have h1 : G M * G M = Mᵀ * (M * Mᵀ) * M := by simp only [G, Matrix.mul_assoc]
  rw [h1, MMt hM, Matrix.mul_add, Matrix.add_mul, Matrix.mul_smul, Matrix.mul_smul, Matrix.smul_mul,
    Matrix.smul_mul, Matrix.mul_one, Matrix.mul_assoc, J14M hM, Matrix.mul_smul, MtJ hM, smul_smul]
  simp only [G]
  module

lemma GJ (hM : IsBTD M) : G M * J (Fin 18) (Fin 18) = (63 : ℤ) • J (Fin 18) (Fin 18) := by
  simp only [G]
  rw [Matrix.mul_assoc, MJ hM, Matrix.mul_smul, MtJ hM, smul_smul]
  norm_num

lemma JG (hM : IsBTD M) : J (Fin 18) (Fin 18) * G M = (63 : ℤ) • J (Fin 18) (Fin 18) := by
  have h : J (Fin 18) (Fin 18) * Mᵀ = (9 : ℤ) • J (Fin 18) (Fin 14) := by
    ext j i
    simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.transpose_apply, Matrix.smul_apply,
      smul_eq_mul]
    rw [row_sum hM i]
  simp only [G]
  rw [← Matrix.mul_assoc, h, Matrix.smul_mul, JM hM, smul_smul]
  norm_num

/-- `H = 63 I - 9 G + 28 J` -/
def H (M : Matrix (Fin 14) (Fin 18) ℤ) : Matrix (Fin 18) (Fin 18) ℤ :=
  (63 : ℤ) • (1 : Matrix (Fin 18) (Fin 18) ℤ) - (9 : ℤ) • G M + (28 : ℤ) • J (Fin 18) (Fin 18)

lemma HH (hM : IsBTD M) : H M * H M = (63 : ℤ) • H M := by
  simp only [H, Matrix.add_mul, Matrix.mul_add, Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.one_mul, Matrix.mul_one, GG hM, GJ hM, JG hM, JJ18, smul_smul, smul_add, smul_sub]
  module

lemma HJ (hM : IsBTD M) : H M * J (Fin 18) (Fin 18) = 0 := by
  simp only [H, Matrix.add_mul, Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul, GJ hM, JJ18, smul_smul]
  module

lemma H_apply (j k : Fin 18) :
    H M j k = (if j = k then 63 else 0) - 9 * ∑ i, M i j * M i k + 28 := by
  simp only [H, G, Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.mul_apply,
    Matrix.transpose_apply, J, Matrix.of_apply, smul_eq_mul]
  split_ifs <;> ring

lemma H_symm (j k : Fin 18) : H M j k = H M k j := by
  rw [H_apply, H_apply]
  have : ∑ i, M i j * M i k = ∑ i, M i k * M i j := Finset.sum_congr rfl fun i _ => mul_comm _ _
  rw [this]
  by_cases h : j = k
  · subst h; rfl
  · rw [if_neg h, if_neg (Ne.symm h)]

lemma H_row_sum (hM : IsBTD M) (j : Fin 18) : ∑ k, H M j k = 0 := by
  have h := congrFun (congrFun (HJ hM) j) j
  simpa [Matrix.mul_apply, J] using h

lemma H_col_sum (hM : IsBTD M) (j : Fin 18) : ∑ k, H M k j = 0 := by
  rw [← H_row_sum hM j]
  exact Finset.sum_congr rfl fun k _ => H_symm k j

lemma H_sq_entry (hM : IsBTD M) (j k : Fin 18) : ∑ l, H M j l * H M l k = 63 * H M j k := by
  have h := congrFun (congrFun (HH hM) j) k
  simpa [Matrix.mul_apply] using h

/-- `∑ₘ H m j * H m k = 63 H j k` (columns version) -/
lemma H_col_dot (hM : IsBTD M) (j k : Fin 18) : ∑ m, H M m j * H M m k = 63 * H M j k := by
  rw [← H_sq_entry hM j k]
  exact Finset.sum_congr rfl fun m _ => by rw [H_symm m j]

lemma H_diag (hM : IsBTD M) (j : Fin 18) : H M j j = 28 - 18 * (c M j : ℤ) := by
  rw [H_apply, if_pos rfl, col_sq hM j]
  ring

lemma H_off_mod (j k : Fin 18) (h : j ≠ k) : H M j k % 9 = 1 := by
  rw [H_apply, if_neg h]
  omega

lemma H_diag_nonneg (hM : IsBTD M) (j : Fin 18) : 0 ≤ H M j j := by
  have h := H_col_dot hM j j
  have : 0 ≤ ∑ m, H M m j * H M m j := Finset.sum_nonneg fun m _ => mul_self_nonneg _
  linarith

lemma c_le_one (hM : IsBTD M) (j : Fin 18) : c M j ≤ 1 := by
  have h1 := H_diag_nonneg hM j
  rw [H_diag hM j] at h1
  omega

lemma H_cs (hM : IsBTD M) (j k : Fin 18) : H M j k ^ 2 ≤ H M j j * H M k k := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset (Fin 18)) (fun m => H M m j) (fun m => H M m k)
  rw [H_col_dot hM j k] at hcs
  have e1 : ∑ m, H M m j ^ 2 = 63 * H M j j := by
    rw [← H_col_dot hM j j]; exact Finset.sum_congr rfl fun m _ => sq _
  have e2 : ∑ m, H M m k ^ 2 = 63 * H M k k := by
    rw [← H_col_dot hM k k]; exact Finset.sum_congr rfl fun m _ => sq _
  rw [e1, e2] at hcs
  nlinarith

/-- total number of entries `2` is 14 -/
lemma sum_c (hM : IsBTD M) : ∑ j, (c M j : ℤ) = 14 := by
  have h2 := hM.2.2.1
  have e : ∀ j, (c M j : ℤ) = ∑ i, (if M i j = 2 then (1 : ℤ) else 0) := by
    intro j
    rw [Finset.sum_boole]
    rfl
  simp_rw [e]
  rw [Finset.sum_comm]
  have e2 : ∀ i, ∑ j, (if M i j = 2 then (1 : ℤ) else 0) = 1 := by
    intro i
    rw [Finset.sum_boole, h2 i]
    norm_num
  simp_rw [e2]
  simp

/-- columns with one entry `2` (type-1) -/
def T1 (M : Matrix (Fin 14) (Fin 18) ℤ) : Finset (Fin 18) := univ.filter fun j => c M j = 1
/-- columns without entries `2` (type-0) -/
def T0 (M : Matrix (Fin 14) (Fin 18) ℤ) : Finset (Fin 18) := univ.filter fun j => c M j = 0

lemma counts (hM : IsBTD M) : (T1 M).card = 14 ∧ (T0 M).card = 4 := by
  have hle := c_le_one hM
  have e : ∀ j, (c M j : ℤ) = (if c M j = 1 then (1 : ℤ) else 0) := by
    intro j
    have := hle j
    interval_cases h : c M j <;> simp
  have h := sum_c hM
  simp_rw [e] at h
  rw [Finset.sum_boole] at h
  have h1 : (T1 M).card = 14 := by
    simp only [T1]
    exact_mod_cast h
  refine ⟨h1, ?_⟩
  have hdis : T0 M = univ \ T1 M := by
    ext j
    simp only [T0, T1, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_sdiff]
    have := hle j
    omega
  rw [hdis, Finset.card_sdiff_of_subset (Finset.subset_univ _), h1]
  simp

lemma diag_t1 (hM : IsBTD M) {a : Fin 18} (ha : a ∈ T1 M) : H M a a = 10 := by
  rw [H_diag hM a, (Finset.mem_filter.mp ha).2]; norm_num

lemma diag_t0 (hM : IsBTD M) {a : Fin 18} (ha : a ∈ T0 M) : H M a a = 28 := by
  rw [H_diag hM a, (Finset.mem_filter.mp ha).2]; norm_num

lemma diag_le (hM : IsBTD M) (k : Fin 18) : H M k k ≤ 28 := by
  rw [H_diag hM k]; omega

/-- next to a type-1 column every entry of `H` is `-8`, `1` or `10` -/
lemma type1_vals (hM : IsBTD M) {a : Fin 18} (ha : a ∈ T1 M) (k : Fin 18) :
    H M a k = -8 ∨ H M a k = 1 ∨ H M a k = 10 := by
  by_cases hk : a = k
  · subst hk; right; right; exact diag_t1 hM ha
  · have h1 := H_cs hM a k
    rw [diag_t1 hM ha] at h1
    have h2 := diag_le hM k
    have h3 := H_diag_nonneg hM k
    have h4 := H_off_mod (M := M) a k hk
    have h5 : -16 ≤ H M a k ∧ H M a k ≤ 16 := by constructor <;> nlinarith
    omega

lemma sum_row_sq (hM : IsBTD M) (a : Fin 18) : ∑ k, H M a k ^ 2 = 63 * H M a a := by
  rw [← H_sq_entry hM a a]
  exact Finset.sum_congr rfl fun k _ => by rw [sq, H_symm k a]

/-- exactly three entries `10` in the row of a type-1 column (itself included) -/
lemma card10 (hM : IsBTD M) {a : Fin 18} (ha : a ∈ T1 M) : (univ.filter fun k => H M a k = 10).card = 3 := by
  have hpt : ∀ k, (H M a k - 1) * (H M a k + 8) = 162 * (if H M a k = 10 then 1 else 0) := by
    intro k
    rcases type1_vals hM ha k with h | h | h <;> rw [h] <;> norm_num
  have hs : ∑ k, (H M a k - 1) * (H M a k + 8) = 486 := by
    have e : ∀ k, (H M a k - 1) * (H M a k + 8) = H M a k ^ 2 + 7 * H M a k - 8 := fun k => by ring
    simp_rw [e]
    rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, sum_row_sq hM a, H_row_sum hM a,
      diag_t1 hM ha]
    simp
  simp_rw [hpt] at hs
  rw [← Finset.mul_sum, Finset.sum_boole] at hs
  have : ((univ.filter fun k => H M a k = 10).card : ℤ) = 3 := by linarith
  exact_mod_cast this

/-- exactly five entries `-8` in the row of a type-1 column -/
lemma card_m8 (hM : IsBTD M) {a : Fin 18} (ha : a ∈ T1 M) : (univ.filter fun k => H M a k = -8).card = 5 := by
  have hpt : ∀ k, (H M a k - 1) * (H M a k - 10) = 162 * (if H M a k = -8 then 1 else 0) := by
    intro k
    rcases type1_vals hM ha k with h | h | h <;> rw [h] <;> norm_num
  have hs : ∑ k, (H M a k - 1) * (H M a k - 10) = 810 := by
    have e : ∀ k, (H M a k - 1) * (H M a k - 10) = H M a k ^ 2 - 11 * H M a k + 10 := fun k => by ring
    simp_rw [e]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum, sum_row_sq hM a, H_row_sum hM a,
      diag_t1 hM ha]
    simp
  simp_rw [hpt] at hs
  rw [← Finset.mul_sum, Finset.sum_boole] at hs
  have : ((univ.filter fun k => H M a k = -8).card : ℤ) = 5 := by linarith
  exact_mod_cast this

/-- (E): `H a k = 10` between type-1 columns forces equal `H`-columns -/
lemma eqcols (hM : IsBTD M) {a k : Fin 18} (ha : a ∈ T1 M) (hk : k ∈ T1 M) (hak : H M a k = 10) (l : Fin 18) :
    H M l a = H M l k := by
  have hsum : ∑ m, (H M m a - H M m k) ^ 2 = 0 := by
    have e : ∀ m, (H M m a - H M m k) ^ 2 = H M m a * H M m a - 2 * (H M m a * H M m k) + H M m k * H M m k :=
      fun m => by ring
    simp_rw [e]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum, H_col_dot hM a a, H_col_dot hM a k,
      H_col_dot hM k k, diag_t1 hM ha, diag_t1 hM hk, hak]
    norm_num
  have h0 := (Finset.sum_eq_zero_iff_of_nonneg (fun m _ => sq_nonneg (H M m a - H M m k))).mp hsum l
    (Finset.mem_univ _)
  have := pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h0
  linarith

/-- (F): two entries `-8` from a type-1 column to two other type-1 columns force `10` between them -/
lemma lemmaF (hM : IsBTD M) {a k l : Fin 18} (ha : a ∈ T1 M) (hk : k ∈ T1 M) (hl : l ∈ T1 M)
    (hak : H M a k = -8) (hal : H M a l = -8) (_hkl : k ≠ l) : H M k l = 10 := by
  have hsum : ∑ m, (2 * H M m a + H M m k + H M m l) ^ 2 = 63 * (2 * H M k l - 4) := by
    have e : ∀ m, (2 * H M m a + H M m k + H M m l) ^ 2 =
        4 * (H M m a * H M m a) + H M m k * H M m k + H M m l * H M m l + 4 * (H M m a * H M m k)
        + 4 * (H M m a * H M m l) + 2 * (H M m k * H M m l) := fun m => by ring
    simp_rw [e]
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib,
      Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum,
      H_col_dot hM a a, H_col_dot hM k k, H_col_dot hM l l, H_col_dot hM a k, H_col_dot hM a l, H_col_dot hM k l,
      diag_t1 hM ha, diag_t1 hM hk, diag_t1 hM hl, hak, hal]
    ring
  have hnn : 0 ≤ ∑ m, (2 * H M m a + H M m k + H M m l) ^ 2 := Finset.sum_nonneg fun m _ => sq_nonneg _
  have hge : 2 ≤ H M k l := by linarith
  rcases type1_vals hM hk l with h | h | h <;> [linarith; linarith; exact h]

/-! ### Lemma D4 -/

/-- all-ones matrices over `ℚ` -/
def Jq (m n : Type) : Matrix m n ℚ := Matrix.of fun _ _ => 1

lemma Jq14_sq : Jq (Fin 14) (Fin 14) * Jq (Fin 14) (Fin 14) = (14 : ℚ) • Jq (Fin 14) (Fin 14) := by
  ext i k
  simp [Matrix.mul_apply, Jq]

/-- `A = 7 I + 4 J` (14 x 14) and its explicit inverse -/
def Aq : Matrix (Fin 14) (Fin 14) ℚ := (7 : ℚ) • (1 : Matrix (Fin 14) (Fin 14) ℚ) + (4 : ℚ) • Jq (Fin 14) (Fin 14)
def Bq : Matrix (Fin 14) (Fin 14) ℚ := (1 / 7 : ℚ) • ((1 : Matrix (Fin 14) (Fin 14) ℚ) - (4 / 63 : ℚ) • Jq (Fin 14) (Fin 14))

lemma AB : Aq * Bq = 1 := by
  simp only [Aq, Bq, Matrix.add_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one,
    Jq14_sq, smul_sub, smul_add, smul_smul]
  module

lemma det_Aq : Aq.det = 7 ^ 14 * 9 := by
  have h1 : Aq = (7 : ℚ) • ((1 : Matrix (Fin 14) (Fin 14) ℚ) +
      Matrix.replicateCol (Fin 1) (fun _ => (4 / 7 : ℚ)) * Matrix.replicateRow (Fin 1) (fun _ => (1 : ℚ))) := by
    ext i k
    simp only [Aq, Jq, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.of_apply, Matrix.mul_apply,
      Matrix.replicateCol_apply, Matrix.replicateRow_apply, smul_eq_mul, Finset.univ_unique, Finset.sum_singleton]
    split_ifs <;> ring
  rw [h1, Matrix.det_smul, Matrix.det_one_add_mul_comm, Matrix.det_unique]
  simp [Matrix.mul_apply, Matrix.replicateRow_apply, Matrix.replicateCol_apply]
  norm_num

section lemmaD4

variable (a b u c' : Fin 18)

/-- the four chosen columns -/
def v4 : Fin 4 → Fin 18 := ![a, b, u, c']

/-- the 4 x 4 principal submatrix of `H` on the chosen columns -/
def H4 (M : Matrix (Fin 14) (Fin 18) ℤ) : Matrix (Fin 4) (Fin 4) ℤ :=
  Matrix.of fun s t => H M (v4 a b u c' s) (v4 a b u c' t)

end lemmaD4

lemma v4_inj {a b u c' : Fin 18} (hab : a ≠ b) (hau : a ≠ u) (hac : a ≠ c') (hbu : b ≠ u) (hbc : b ≠ c')
    (huc : u ≠ c') : Function.Injective (v4 a b u c') := by
  intro x y hxy
  fin_cases x <;> fin_cases y <;> simp [v4] at hxy ⊢ <;> simp_all

lemma lemmaD4 (hM : IsBTD M) (a b u c' : Fin 18) (hab : a ≠ b) (hau : a ≠ u) (hac : a ≠ c') (hbu : b ≠ u)
    (hbc : b ≠ c') (huc : u ≠ c') :
    ∃ d : ℤ, 729 * d ^ 2 = 7 ^ 10 * (H4 a b u c' M).det := by
  classical
  set S : Finset (Fin 18) := {a, b, u, c'} with hS
  have hcardS : S.card = 4 := by
    rw [hS, Finset.card_insert_of_notMem, Finset.card_insert_of_notMem, Finset.card_insert_of_notMem,
      Finset.card_singleton]
    · simpa using huc
    · simp [hbu, hbc]
    · simp [hab, hau, hac]
  have hcardC : Fintype.card {j // j ∈ Sᶜ} = 14 := by
    rw [Fintype.card_coe, Finset.card_compl, hcardS]; rfl
  let e : Fin 14 ≃ {j // j ∈ Sᶜ} := (Fintype.equivFinOfCardEq hcardC).symm
  let v := v4 a b u c'
  let Nz : Matrix (Fin 14) (Fin 14) ℤ := Matrix.of fun i w => M i (e w).1
  let Nq : Matrix (Fin 14) (Fin 14) ℚ := Matrix.of fun i w => (M i (e w).1 : ℚ)
  let Pq : Matrix (Fin 14) (Fin 4) ℚ := Matrix.of fun i t => (M i (v t) : ℚ)
  have hsplit : ∀ i k : Fin 14, ∑ j, (M i j : ℚ) * M k j = ∑ w, Nq i w * Nq k w + ∑ t, Pq i t * Pq k t := by
    intro i k
    rw [← Finset.sum_compl_add_sum S]
    congr 1
    · rw [← Finset.sum_coe_sort Sᶜ]
      exact (Equiv.sum_comp e (fun x : {j // j ∈ Sᶜ} => (M i x.1 : ℚ) * M k x.1)).symm
    · rw [hS, Finset.sum_insert (by simp [hab, hau, hac]), Finset.sum_insert (by simp [hbu, hbc]),
        Finset.sum_insert (by simpa using huc), Finset.sum_singleton, Fin.sum_univ_four]
      simp [Pq, v, v4, add_assoc]
  have hNN : Nq * Nqᵀ = Aq - Pq * Pqᵀ := by
    ext i k
    have h := hsplit i k
    have hrow : ∑ j, (M i j : ℚ) * M k j = (if i = k then 7 else 0) + 4 := by
      have := congrFun (congrFun (MMt hM) i) k
      simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
        J, Matrix.of_apply, smul_eq_mul] at this
      have hc : ((∑ j, M i j * M k j : ℤ) : ℚ) = ∑ j, (M i j : ℚ) * M k j := by push_cast; rfl
      rw [← hc, this]
      split_ifs <;> push_cast <;> ring
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.sub_apply, Aq, Jq, Matrix.add_apply,
      Matrix.smul_apply, Matrix.one_apply, Matrix.of_apply, smul_eq_mul]
    rw [hrow] at h
    split_ifs at h ⊢ <;> linarith
  have hdet1 : (Nq * Nqᵀ).det = Aq.det * (1 - Pqᵀ * (Bq * Pq)).det := by
    have : Aq - Pq * Pqᵀ = Aq * (1 - (Bq * Pq) * Pqᵀ) := by
      rw [Matrix.mul_sub, Matrix.mul_one, ← Matrix.mul_assoc, ← Matrix.mul_assoc, AB, Matrix.one_mul]
    rw [hNN, this, Matrix.det_mul, Matrix.det_one_sub_mul_comm]
  have hcol : ∀ t, ∑ i, Pq i t = 7 := by
    intro t
    have := hM.2.2.2.1 (v t)
    simp only [Pq, Matrix.of_apply]
    exact_mod_cast this
  have hJP : ∀ i t, (Jq (Fin 14) (Fin 14) * Pq) i t = 7 := by
    intro i t
    simp only [Matrix.mul_apply, Jq, Matrix.of_apply, one_mul]
    exact hcol t
  have hBP : ∀ i t, (Bq * Pq) i t = (1 / 7) * (Pq i t - 4 / 9) := by
    intro i t
    rw [Bq, Matrix.smul_mul, Matrix.sub_mul, Matrix.one_mul, Matrix.smul_mul, Matrix.smul_apply, Matrix.sub_apply,
      Matrix.smul_apply, hJP i t, smul_eq_mul, smul_eq_mul]
    ring
  have hv : Function.Injective (v4 a b u c') := v4_inj hab hau hac hbu hbc huc
  have hinner : 1 - Pqᵀ * (Bq * Pq) = (1 / 63 : ℚ) • (H4 a b u c' M).map (Int.cast : ℤ → ℚ) := by
    ext s t
    have hsum : (Pqᵀ * (Bq * Pq)) s t = (1 / 7) * (∑ i, Pq i s * Pq i t) - (1 / 7) * (4 / 9) * (∑ i, Pq i s) := by
      simp only [Matrix.mul_apply, Matrix.transpose_apply, hBP]
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [Matrix.sub_apply, hsum, hcol s, Matrix.smul_apply, Matrix.map_apply, H4, Matrix.of_apply, H_apply,
      Matrix.one_apply, smul_eq_mul]
    simp only [Pq, Matrix.of_apply, v]
    by_cases hst : s = t
    · subst hst
      rw [if_pos rfl, if_pos rfl]
      push_cast
      ring
    · have hne : v4 a b u c' s ≠ v4 a b u c' t := fun h => hst (hv h)
      rw [if_neg hst, if_neg hne]
      push_cast
      ring
  have hNz : Nq = Nz.map (Int.cast : ℤ → ℚ) := by ext i w; simp [Nq, Nz]
  have hcastN : ((Nz.det : ℤ) : ℚ) = (Nz.map (Int.cast : ℤ → ℚ)).det := by
    have := RingHom.map_det (Int.castRingHom ℚ) Nz
    simpa [RingHom.mapMatrix_apply] using this
  have hdetN : (Nq * Nqᵀ).det = ((Nz.det : ℤ) : ℚ) ^ 2 := by
    rw [Matrix.det_mul, Matrix.det_transpose, hNz, ← hcastN, sq]
  have hdetH : ((H4 a b u c' M).map (Int.cast : ℤ → ℚ)).det = (((H4 a b u c' M).det : ℤ) : ℚ) := by
    have := RingHom.map_det (Int.castRingHom ℚ) (H4 a b u c' M)
    simpa [RingHom.mapMatrix_apply] using this.symm
  refine ⟨Nz.det, ?_⟩
  have key := hdet1
  rw [hdetN, hinner, Matrix.det_smul, hdetH, det_Aq] at key
  simp only [Fintype.card_fin] at key
  have : (729 : ℚ) * ((Nz.det : ℤ) : ℚ) ^ 2 = 7 ^ 10 * (((H4 a b u c' M).det : ℤ) : ℚ) := by
    rw [key]
    ring
  exact_mod_cast this

/-! ### Closing arithmetic -/

lemma det4_pattern (x y w : ℤ) :
    (Matrix.of ![![(10 : ℤ), -8, 1, x], ![-8, 10, 1, y], ![1, 1, 10, w], ![x, y, w, 28]]).det =
      9072 - 99 * x ^ 2 - 99 * y ^ 2 - 162 * x * y + 36 * x * w + 36 * y * w - 36 * w ^ 2 := by
  rw [Matrix.det_succ_row_zero]
  simp [Fin.sum_univ_succ, Matrix.det_fin_three, Matrix.submatrix_apply, Fin.succAbove]
  ring

lemma sq_mod3 (d : ℤ) : d ^ 2 % 3 = 0 ∨ d ^ 2 % 3 = 1 := by
  rcases (by omega : d % 3 = 0 ∨ d % 3 = 1 ∨ d % 3 = 2) with h | h | h <;>
    simp [pow_two, Int.mul_emod, h]

/-- `729 d^2 = 7^10 D` has no integer solution for `D = 3645` or `D = -2187` -/
lemma bad_det4 (d D : ℤ) (h : 729 * d ^ 2 = 7 ^ 10 * D) (hD : D = 3645 ∨ D = -2187) : False := by
  rcases hD with rfl | rfl
  · have h2 : d ^ 2 = 5 * 7 ^ 10 := by linarith
    have h3 := sq_mod3 d
    rw [h2] at h3
    norm_num at h3
  · nlinarith [sq_nonneg d]

lemma ne_of_types (_hM : IsBTD M) {p q : Fin 18} (hp : p ∈ T1 M) (hq : q ∈ T0 M) : p ≠ q := by
  rintro rfl
  simp only [T1, T0, Finset.mem_filter, Finset.mem_univ, true_and] at hp hq
  omega

/-! ### The theorem -/

/-- **No BTD(14,18;7,1,9;7,4) exists**: there is no `14 × 18` matrix with entries in `{0, 1, 2}` such that every
row has exactly seven entries `1` and exactly one entry `2`, every column sums to `7`, and any two distinct rows have
inner product `4`.  (Repeated columns are allowed; nothing else is assumed.) -/
theorem no_btd : Statement := by
  unfold Statement
  rintro ⟨M, hM⟩
  obtain ⟨hT1, hT0⟩ := counts hM
  obtain ⟨a, ha⟩ : (T1 M).Nonempty := Finset.card_pos.mp (by omega)
  -- a type-1 column `b` with `H a b = -8`
  have hlt : (T0 M).card < (univ.filter fun k => H M a k = -8).card := by
    rw [hT0, card_m8 hM ha]; norm_num
  obtain ⟨b, hb8, hbT0⟩ := Finset.exists_mem_notMem_of_card_lt_card hlt
  have hab : H M a b = -8 := (Finset.mem_filter.mp hb8).2
  have hb : b ∈ T1 M := by
    have hle := c_le_one hM b
    simp only [T1, T0, Finset.mem_filter, Finset.mem_univ, true_and] at hbT0 ⊢
    omega
  have hab' : a ≠ b := by
    rintro rfl
    rw [diag_t1 hM ha] at hab
    norm_num at hab
  have hba : H M b a = -8 := by rw [H_symm]; exact hab
  -- (i) every type-1 column `q` has `H q a + H q b = 2`
  have key1 : ∀ q ∈ T1 M, H M q a + H M q b = 2 := by
    intro q hq
    by_cases hqa : q = a
    · subst hqa; rw [diag_t1 hM hq, hab]; norm_num
    by_cases hqb : q = b
    · subst hqb; rw [diag_t1 hM hq, hba]; norm_num
    rw [H_symm q a, H_symm q b]
    rcases type1_vals hM ha q with h1 | h1 | h1
    · have h2 := lemmaF hM ha hb hq hab h1 (fun h => hqb h.symm)
      rw [h1, h2]; norm_num
    · rcases type1_vals hM hb q with h2 | h2 | h2
      · have h3 := lemmaF hM hb ha hq hba h2 (fun h => hqa h.symm)
        rw [h1] at h3; norm_num at h3
      · rw [h1, h2]; norm_num
      · have h3 := eqcols hM hb hq h2 a
        rw [hab, h1] at h3; norm_num at h3
    · have h3 := eqcols hM ha hq h1 b
      rw [hba] at h3
      rw [h1, ← h3]; norm_num
  -- (ii) a type-1 column `u` with `H a u = H b u = 1`
  have hlt2 : ((univ.filter fun k => H M a k = 10) ∪ (univ.filter fun k => H M b k = 10)).card < (T1 M).card := by
    have h1 := Finset.card_union_le (univ.filter fun k => H M a k = 10) (univ.filter fun k => H M b k = 10)
    rw [card10 hM ha, card10 hM hb] at h1
    omega
  obtain ⟨u, hu, hun⟩ := Finset.exists_mem_notMem_of_card_lt_card hlt2
  rw [Finset.mem_union, not_or] at hun
  have hau10 : H M a u ≠ 10 := fun h => hun.1 (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩)
  have hbu10 : H M b u ≠ 10 := fun h => hun.2 (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩)
  have hau : a ≠ u := by
    rintro rfl
    exact hau10 (diag_t1 hM ha)
  have hbu : b ≠ u := by
    rintro rfl
    exact hbu10 (diag_t1 hM hb)
  have hsu := key1 u hu
  rw [H_symm u a, H_symm u b] at hsu
  have hva := type1_vals hM ha u
  have hvb := type1_vals hM hb u
  have hau1 : H M a u = 1 := by omega
  have hbu1 : H M b u = 1 := by omega
  have hua1 : H M u a = 1 := by rw [H_symm]; exact hau1
  have hub1 : H M u b = 1 := by rw [H_symm]; exact hbu1
  -- (iii)-(iv) every type-0 column `q` has `H q a + H q b = 2`
  have key0 : ∀ q ∈ T0 M, H M q a + H M q b = 2 := by
    intro q hq
    have hqq : H M q q = 28 := diag_t0 hM hq
    have haq : a ≠ q := ne_of_types hM ha hq
    have hbq : b ≠ q := ne_of_types hM hb hq
    have huq : u ≠ q := ne_of_types hM hu hq
    have hx := type1_vals hM ha q
    have hy := type1_vals hM hb q
    have hw := type1_vals hM hu q
    have hcs : (H M a q + H M b q) ^ 2 ≤ 112 := by
      have hcs0 := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset (Fin 18)) (fun m => H M m a + H M m b)
        (fun m => H M m q)
      have e1 : ∑ m, (H M m a + H M m b) * H M m q = 63 * (H M a q + H M b q) := by
        simp_rw [add_mul]
        rw [Finset.sum_add_distrib, H_col_dot hM a q, H_col_dot hM b q]
        ring
      have e2 : ∑ m, (H M m a + H M m b) ^ 2 = 63 * 4 := by
        have e : ∀ m, (H M m a + H M m b) ^ 2 =
            H M m a * H M m a + 2 * (H M m a * H M m b) + H M m b * H M m b := fun m => by ring
        simp_rw [e]
        rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, H_col_dot hM a a, H_col_dot hM a b,
          H_col_dot hM b b, diag_t1 hM ha, diag_t1 hM hb, hab]
        norm_num
      have e3 : ∑ m, H M m q ^ 2 = 63 * 28 := by
        rw [← hqq, ← H_col_dot hM q q]
        exact Finset.sum_congr rfl fun m _ => sq _
      rw [e1, e2, e3] at hcs0
      nlinarith
    rw [H_symm q a, H_symm q b]
    by_contra hne
    have hbd : -10 ≤ H M a q + H M b q ∧ H M a q + H M b q ≤ 10 := by constructor <;> nlinarith
    have hm7 : H M a q + H M b q = -7 := by omega
    obtain ⟨d, hd⟩ := lemmaD4 hM a b u q hab' hau haq hbu hbq huq
    have hqa : H M q a = H M a q := H_symm q a
    have hqb : H M q b = H M b q := H_symm q b
    have hqu : H M q u = H M u q := H_symm q u
    have hH4 : H4 a b u q M = Matrix.of ![![(10 : ℤ), -8, 1, H M a q], ![-8, 10, 1, H M b q], ![1, 1, 10, H M u q],
        ![H M a q, H M b q, H M u q, 28]] := by
      ext s t
      fin_cases s <;> fin_cases t <;>
        simp [H4, v4, diag_t1 hM ha, diag_t1 hM hb, diag_t1 hM hu, hqq, hab, hba, hau1, hbu1, hua1, hub1, hqa, hqb,
          hqu]
    rw [hH4, det4_pattern] at hd
    refine bad_det4 d _ hd ?_
    have hxy : (H M a q = -8 ∧ H M b q = 1) ∨ (H M a q = 1 ∧ H M b q = -8) := by omega
    rcases hxy with ⟨h, h'⟩ | ⟨h, h'⟩ <;> rcases hw with h'' | h'' | h'' <;> rw [h, h', h''] <;> norm_num
  -- (v) the column sums of `H` at `a` and `b` are zero, but every column contributes 2
  have hall : ∀ q, H M q a + H M q b = 2 := by
    intro q
    have hle := c_le_one hM q
    by_cases h1 : c M q = 1
    · exact key1 q (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h1⟩)
    · exact key0 q (Finset.mem_filter.mpr ⟨Finset.mem_univ _, by omega⟩)
  have htot : ∑ q, (H M q a + H M q b) = 36 := by
    rw [Finset.sum_congr rfl fun q _ => hall q]
    simp
  rw [Finset.sum_add_distrib, H_col_sum hM a, H_col_sum hM b] at htot
  norm_num at htot

end BTD14
