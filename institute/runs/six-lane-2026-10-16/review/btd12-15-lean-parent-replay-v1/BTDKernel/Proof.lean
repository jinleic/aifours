import BTDKernel.Target
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# BTD(12,15;6,2,10;8,6) does not exist: the proof

Formalization of `notes/nonexistence-proof-r2.md` (frozen r2) of lane
`information-science/evidence/six-lane-20261016/btd12-15`.  With `G = MᵀM` and `H = 40 I - 5 G + 24 J`:

* Step 1: `H * H = 40 • H` and `H * J = 0` (`HH`, `HJ`); `H j j = 24 - 10 c_j` (`H_diag`), off-diagonal entries are
  `4 mod 5` (`H_off_mod`).
* Step 2: `0 ≤ H j j` and `H j k ^ 2 ≤ H j j * H k k` by Cauchy–Schwarz on rows of `H` (`H_diag_nonneg`, `H_cs`);
  hence `c_j ≤ 2` (`c_le_two`).
* Step 3: column-type counts (`counts`).
* Step 4: at most five columns `k` (itself included) have `H a k = 4` for a column `a` with two entries `2`
  (`class_le_five`), via `∑ₖ (H a k + 1)(H a k + 6) = 250` with nonnegative terms.
* Step 5/7 (only what is used): type-2 pairs have `H ∈ {-1, 4}` (`type2_pair`); three type-2 columns pairwise at
  `H = -1` are impossible; hence at most 10 type-2 columns and a type-1 column exists.
* Step 6 (Lemma D): `25 d² = 2²⁸ det H[{a,b,c}]` with `d` the determinant of the complementary `12 × 12` integer
  submatrix (`lemmaD`), by the matrix determinant lemma (`Matrix.det_one_sub_mul_comm`) over `ℚ`.
* Step 8: `det H[{a,b,k}] ∈ {-150, 50, 150, 200}` is incompatible with Lemma D (`bad_det`).
-/

namespace BTD12

open Finset Matrix

/-- all-ones matrices -/
def J (m n : Type) : Matrix m n ℤ := Matrix.of fun _ _ => 1

lemma val_eq (x : ℤ) (hx : x = 0 ∨ x = 1 ∨ x = 2) :
    x = (if x = 1 then 1 else 0) + 2 * (if x = 2 then 1 else 0) := by
  rcases hx with h | h | h <;> subst h <;> norm_num

lemma sq_eq (x : ℤ) (hx : x = 0 ∨ x = 1 ∨ x = 2) :
    x * x = (if x = 1 then 1 else 0) + 4 * (if x = 2 then 1 else 0) := by
  rcases hx with h | h | h <;> subst h <;> norm_num

variable {M : Matrix (Fin 12) (Fin 15) ℤ}

lemma row_sq (hM : IsBTD M) (i : Fin 12) : ∑ j, M i j * M i j = 14 := by
  obtain ⟨hv, h1, h2, -, -⟩ := hM
  calc ∑ j, M i j * M i j
        = ∑ j, ((if M i j = 1 then (1 : ℤ) else 0) + 4 * (if M i j = 2 then 1 else 0)) :=
          Finset.sum_congr rfl fun j _ => sq_eq _ (hv i j)
    _ = ((univ.filter fun j => M i j = 1).card : ℤ) + 4 * (univ.filter fun j => M i j = 2).card := by
          rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]
    _ = 14 := by rw [h1 i, h2 i]; norm_num

lemma row_sum (hM : IsBTD M) (i : Fin 12) : ∑ j, M i j = 10 := by
  obtain ⟨hv, h1, h2, -, -⟩ := hM
  calc ∑ j, M i j
        = ∑ j, ((if M i j = 1 then (1 : ℤ) else 0) + 2 * (if M i j = 2 then 1 else 0)) :=
          Finset.sum_congr rfl fun j _ => val_eq _ (hv i j)
    _ = ((univ.filter fun j => M i j = 1).card : ℤ) + 2 * (univ.filter fun j => M i j = 2).card := by
          rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole]
    _ = 10 := by rw [h1 i, h2 i]; norm_num

/-- number of entries `2` in column `j` -/
def c (M : Matrix (Fin 12) (Fin 15) ℤ) (j : Fin 15) : ℕ := (univ.filter fun i => M i j = 2).card

lemma col_sq (hM : IsBTD M) (j : Fin 15) : ∑ i, M i j * M i j = 8 + 2 * (c M j : ℤ) := by
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

lemma MMt (hM : IsBTD M) : M * Mᵀ = (8 : ℤ) • (1 : Matrix (Fin 12) (Fin 12) ℤ) + (6 : ℤ) • J (Fin 12) (Fin 12) := by
  ext i k
  simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, J,
    Matrix.of_apply, smul_eq_mul]
  by_cases h : i = k
  · subst h; rw [row_sq hM i]; simp
  · rw [hM.2.2.2.2 i k h]; simp [h]

lemma MtJ (hM : IsBTD M) : Mᵀ * J (Fin 12) (Fin 15) = (8 : ℤ) • J (Fin 15) (Fin 15) := by
  ext j k
  simp only [Matrix.mul_apply, Matrix.transpose_apply, J, Matrix.of_apply, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 j]

lemma MJ (hM : IsBTD M) : M * J (Fin 15) (Fin 15) = (10 : ℤ) • J (Fin 12) (Fin 15) := by
  ext i k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [row_sum hM i]

lemma JM (hM : IsBTD M) : J (Fin 15) (Fin 12) * M = (8 : ℤ) • J (Fin 15) (Fin 15) := by
  ext j k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 k]

lemma JJ15 : J (Fin 15) (Fin 15) * J (Fin 15) (Fin 15) = (15 : ℤ) • J (Fin 15) (Fin 15) := by
  ext j k
  simp [Matrix.mul_apply, J]

lemma J12J12M (hM : IsBTD M) : J (Fin 12) (Fin 12) * M = (8 : ℤ) • J (Fin 12) (Fin 15) := by
  ext i k
  simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.smul_apply, smul_eq_mul]
  rw [hM.2.2.2.1 k]

lemma MtJ12 : (Mᵀ * J (Fin 12) (Fin 12)) = Mᵀ * J (Fin 12) (Fin 12) := rfl

/-- the column Gram matrix -/
def G (M : Matrix (Fin 12) (Fin 15) ℤ) : Matrix (Fin 15) (Fin 15) ℤ := Mᵀ * M

lemma GG (hM : IsBTD M) : G M * G M = (8 : ℤ) • G M + (384 : ℤ) • J (Fin 15) (Fin 15) := by
  have h1 : G M * G M = Mᵀ * (M * Mᵀ) * M := by simp only [G, Matrix.mul_assoc]
  rw [h1, MMt hM, Matrix.mul_add, Matrix.add_mul, Matrix.mul_smul, Matrix.mul_smul, Matrix.smul_mul,
    Matrix.smul_mul, Matrix.mul_one, Matrix.mul_assoc, J12J12M hM, Matrix.mul_smul, MtJ hM, smul_smul]
  simp only [G]
  module

lemma GJ (hM : IsBTD M) : G M * J (Fin 15) (Fin 15) = (80 : ℤ) • J (Fin 15) (Fin 15) := by
  simp only [G]
  rw [Matrix.mul_assoc, MJ hM, Matrix.mul_smul, MtJ hM, smul_smul]
  norm_num

lemma JG (hM : IsBTD M) : J (Fin 15) (Fin 15) * G M = (80 : ℤ) • J (Fin 15) (Fin 15) := by
  have h : J (Fin 15) (Fin 15) * Mᵀ = (10 : ℤ) • J (Fin 15) (Fin 12) := by
    ext j i
    simp only [Matrix.mul_apply, J, Matrix.of_apply, one_mul, mul_one, Matrix.transpose_apply, Matrix.smul_apply,
      smul_eq_mul]
    rw [row_sum hM i]
  simp only [G]
  rw [← Matrix.mul_assoc, h, Matrix.smul_mul, JM hM, smul_smul]
  norm_num

/-- `H = 40 I - 5 G + 24 J` -/
def H (M : Matrix (Fin 12) (Fin 15) ℤ) : Matrix (Fin 15) (Fin 15) ℤ :=
  (40 : ℤ) • (1 : Matrix (Fin 15) (Fin 15) ℤ) - (5 : ℤ) • G M + (24 : ℤ) • J (Fin 15) (Fin 15)

lemma HH (hM : IsBTD M) : H M * H M = (40 : ℤ) • H M := by
  simp only [H, Matrix.add_mul, Matrix.mul_add, Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.one_mul, Matrix.mul_one, GG hM, GJ hM, JG hM, JJ15, smul_smul, smul_add, smul_sub]
  module

lemma HJ (hM : IsBTD M) : H M * J (Fin 15) (Fin 15) = 0 := by
  simp only [H, Matrix.add_mul, Matrix.sub_mul, Matrix.smul_mul, Matrix.one_mul, GJ hM, JJ15, smul_smul]
  module

lemma H_apply (j k : Fin 15) :
    H M j k = (if j = k then 40 else 0) - 5 * ∑ i, M i j * M i k + 24 := by
  simp only [H, G, Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.mul_apply,
    Matrix.transpose_apply, J, Matrix.of_apply, smul_eq_mul]
  split_ifs <;> ring

lemma H_symm (j k : Fin 15) : H M j k = H M k j := by
  rw [H_apply, H_apply]
  have : ∑ i, M i j * M i k = ∑ i, M i k * M i j := Finset.sum_congr rfl fun i _ => mul_comm _ _
  rw [this]
  by_cases h : j = k
  · subst h; rfl
  · rw [if_neg h, if_neg (Ne.symm h)]

lemma H_row_sum (hM : IsBTD M) (j : Fin 15) : ∑ k, H M j k = 0 := by
  have h := congrFun (congrFun (HJ hM) j) j
  simpa [Matrix.mul_apply, J] using h

lemma H_sq_entry (hM : IsBTD M) (j k : Fin 15) : ∑ l, H M j l * H M l k = 40 * H M j k := by
  have h := congrFun (congrFun (HH hM) j) k
  simpa [Matrix.mul_apply] using h

lemma H_diag (hM : IsBTD M) (j : Fin 15) : H M j j = 24 - 10 * (c M j : ℤ) := by
  rw [H_apply, if_pos rfl, col_sq hM j]
  ring

lemma H_off_mod (j k : Fin 15) (h : j ≠ k) : H M j k % 5 = 4 := by
  rw [H_apply, if_neg h]
  omega

lemma H_sq_sum (hM : IsBTD M) (j : Fin 15) : ∑ l, H M j l ^ 2 = 40 * H M j j := by
  rw [← H_sq_entry hM j j]
  exact Finset.sum_congr rfl fun l _ => by rw [sq, H_symm l j]

lemma H_diag_nonneg (hM : IsBTD M) (j : Fin 15) : 0 ≤ H M j j := by
  have h := H_sq_sum hM j
  have : 0 ≤ ∑ l, H M j l ^ 2 := Finset.sum_nonneg fun l _ => sq_nonneg _
  linarith

lemma c_le_two (hM : IsBTD M) (j : Fin 15) : c M j ≤ 2 := by
  have h1 := H_diag_nonneg hM j
  rw [H_diag hM j] at h1
  omega

lemma H_cs (hM : IsBTD M) (j k : Fin 15) : H M j k ^ 2 ≤ H M j j * H M k k := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset (Fin 15)) (fun l => H M j l) (fun l => H M k l)
  have e1 : ∑ l, H M j l * H M k l = 40 * H M j k := by
    rw [← H_sq_entry hM j k]
    exact Finset.sum_congr rfl fun l _ => by rw [H_symm k l]
  rw [e1, H_sq_sum hM j, H_sq_sum hM k] at hcs
  nlinarith

/-- the number of entries `2` in all columns together is `24` -/
lemma sum_c (hM : IsBTD M) : ∑ j, (c M j : ℤ) = 24 := by
  have h2 := hM.2.2.1
  have e : ∀ j, (c M j : ℤ) = ∑ i, (if M i j = 2 then (1 : ℤ) else 0) := by
    intro j
    rw [Finset.sum_boole]
    rfl
  simp_rw [e]
  rw [Finset.sum_comm]
  have e2 : ∀ i, ∑ j, (if M i j = 2 then (1 : ℤ) else 0) = 2 := by
    intro i
    rw [Finset.sum_boole, h2 i]
    norm_num
  simp_rw [e2]
  simp

/-- every column has 0, 1 or 2 entries `2`; counts of the three column types -/
def ncols (M : Matrix (Fin 12) (Fin 15) ℤ) (t : ℕ) : ℕ := (univ.filter fun j => c M j = t).card

lemma counts (hM : IsBTD M) : (ncols M 1 : ℤ) + 2 * ncols M 2 = 24 ∧ ncols M 0 + ncols M 1 + ncols M 2 = 15 := by
  have hle := c_le_two hM
  have e : ∀ j, (c M j : ℤ) = (if c M j = 1 then (1 : ℤ) else 0) + 2 * (if c M j = 2 then 1 else 0) := by
    intro j
    have := hle j
    interval_cases h : c M j <;> simp
  have e1 : ∀ j, (1 : ℕ) = (if c M j = 0 then 1 else 0) + (if c M j = 1 then 1 else 0) + (if c M j = 2 then 1 else 0) := by
    intro j
    have := hle j
    interval_cases h : c M j <;> simp
  constructor
  · have h := sum_c hM
    simp_rw [e] at h
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole, Finset.sum_boole] at h
    simpa [ncols] using h
  · have h : ∑ j : Fin 15, ((if c M j = 0 then 1 else 0) + (if c M j = 1 then 1 else 0)
        + (if c M j = 2 then 1 else 0) : ℕ) = 15 := by
      rw [Finset.sum_congr rfl fun j _ => (e1 j).symm]
      simp
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_boole, Finset.sum_boole, Finset.sum_boole] at h
    simpa [ncols] using h

/-- for a column with two entries `2`, at most five columns `k` (itself included) have `H a k = 4` -/
lemma class_le_five (hM : IsBTD M) (a : Fin 15) (ha : c M a = 2) :
    (univ.filter fun k => H M a k = 4).card ≤ 5 := by
  have haa : H M a a = 4 := by rw [H_diag hM a, ha]; norm_num
  have hnn : ∀ k, 0 ≤ (H M a k + 1) * (H M a k + 6) := by
    intro k
    by_cases hk : a = k
    · subst hk; rw [haa]; norm_num
    · have hm := H_off_mod (M := M) a k hk
      obtain ⟨t, ht⟩ : ∃ t, H M a k = 5 * t - 1 := ⟨(H M a k + 1) / 5, by omega⟩
      rw [ht]
      have : 0 ≤ t * (t + 1) := by
        rcases le_or_gt 0 t with h | h
        · positivity
        · nlinarith
      nlinarith
  have htot : ∑ k, (H M a k + 1) * (H M a k + 6) = 250 := by
    have e : ∀ k, (H M a k + 1) * (H M a k + 6) = H M a k ^ 2 + 7 * H M a k + 6 := fun k => by ring
    simp_rw [e]
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, H_sq_sum hM a, H_row_sum hM a, haa]
    simp
  have hsub : ∑ k ∈ univ.filter (fun k => H M a k = 4), (H M a k + 1) * (H M a k + 6)
      ≤ ∑ k, (H M a k + 1) * (H M a k + 6) :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _) fun k _ _ => hnn k
  have hval : ∑ k ∈ univ.filter (fun k => H M a k = 4), (H M a k + 1) * (H M a k + 6)
      = 50 * ((univ.filter fun k => H M a k = 4).card : ℤ) := by
    rw [Finset.sum_congr rfl (g := fun _ => (50 : ℤ)) (fun k hk => by
      rw [(Finset.mem_filter.mp hk).2]; norm_num)]
    simp [mul_comm]
  rw [hval, htot] at hsub
  have : ((univ.filter fun k => H M a k = 4).card : ℤ) ≤ 5 := by linarith
  exact_mod_cast this

/-- two distinct columns with two entries `2` each have `H a b = -1` or `H a b = 4` -/
lemma type2_pair (hM : IsBTD M) (a b : Fin 15) (ha : c M a = 2) (hb : c M b = 2) (hab : a ≠ b) :
    H M a b = -1 ∨ H M a b = 4 := by
  have h1 := H_cs hM a b
  rw [H_diag hM a, H_diag hM b, ha, hb] at h1
  norm_num at h1
  have h2 := H_off_mod (M := M) a b hab
  have h3 : -4 ≤ H M a b ∧ H M a b ≤ 4 := by constructor <;> nlinarith
  omega

/-- a column with one entry `2` against a column with two: `H` is `-6`, `-1` or `4` -/
lemma type12_pair (hM : IsBTD M) (k a : Fin 15) (hk : c M k = 1) (ha : c M a = 2) (hka : k ≠ a) :
    H M k a = -6 ∨ H M k a = -1 ∨ H M k a = 4 := by
  have h1 := H_cs hM k a
  rw [H_diag hM k, H_diag hM a, hk, ha] at h1
  norm_num at h1
  have h2 := H_off_mod (M := M) k a hka
  have h3 : -7 ≤ H M k a ∧ H M k a ≤ 7 := by constructor <;> nlinarith
  omega

/-! ### Lemma D -/

/-- all-ones matrices over `ℚ` -/
def Jq (m n : Type) : Matrix m n ℚ := Matrix.of fun _ _ => 1

lemma Jq12_sq : Jq (Fin 12) (Fin 12) * Jq (Fin 12) (Fin 12) = (12 : ℚ) • Jq (Fin 12) (Fin 12) := by
  ext i k
  simp [Matrix.mul_apply, Jq]

/-- `A = 8 I + 6 J` (12 x 12) and its explicit inverse -/
def Aq : Matrix (Fin 12) (Fin 12) ℚ := (8 : ℚ) • (1 : Matrix (Fin 12) (Fin 12) ℚ) + (6 : ℚ) • Jq (Fin 12) (Fin 12)
def Bq : Matrix (Fin 12) (Fin 12) ℚ := (1 / 8 : ℚ) • ((1 : Matrix (Fin 12) (Fin 12) ℚ) - (3 / 40 : ℚ) • Jq (Fin 12) (Fin 12))

lemma AB : Aq * Bq = 1 := by
  simp only [Aq, Bq, Matrix.add_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one,
    Jq12_sq, smul_sub, smul_add, smul_smul]
  module

lemma det_Aq : Aq.det = 8 ^ 12 * 10 := by
  have h1 : Aq = (8 : ℚ) • ((1 : Matrix (Fin 12) (Fin 12) ℚ) +
      Matrix.replicateCol (Fin 1) (fun _ => (3 / 4 : ℚ)) * Matrix.replicateRow (Fin 1) (fun _ => (1 : ℚ))) := by
    ext i k
    simp only [Aq, Jq, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.of_apply, Matrix.mul_apply,
      Matrix.replicateCol_apply, Matrix.replicateRow_apply, smul_eq_mul, Finset.univ_unique, Finset.sum_singleton]
    split_ifs <;> ring
  rw [h1, Matrix.det_smul, Matrix.det_one_add_mul_comm, Matrix.det_unique]
  simp [Matrix.mul_apply, Matrix.replicateRow_apply, Matrix.replicateCol_apply]
  norm_num

section lemmaD

variable (a b c' : Fin 15)

/-- the three chosen columns -/
def v3 : Fin 3 → Fin 15 := ![a, b, c']

/-- the 3 x 3 principal submatrix of `H` on the chosen columns -/
def H3 (M : Matrix (Fin 12) (Fin 15) ℤ) : Matrix (Fin 3) (Fin 3) ℤ := Matrix.of fun s t => H M (v3 a b c' s) (v3 a b c' t)

end lemmaD

lemma lemmaD (hM : IsBTD M) (a b c' : Fin 15) (hab : a ≠ b) (hac : a ≠ c') (hbc : b ≠ c') :
    ∃ d : ℤ, 25 * d ^ 2 = 2 ^ 28 * (H3 a b c' M).det := by
  classical
  set S : Finset (Fin 15) := {a, b, c'} with hS
  have hcardS : S.card = 3 := by
    rw [hS, Finset.card_insert_of_notMem, Finset.card_insert_of_notMem, Finset.card_singleton]
    · simpa using hbc
    · simp [hab, hac]
  have hcardC : Fintype.card {j // j ∈ Sᶜ} = 12 := by
    rw [Fintype.card_coe, Finset.card_compl, hcardS]; rfl
  let e : Fin 12 ≃ {j // j ∈ Sᶜ} := (Fintype.equivFinOfCardEq hcardC).symm
  let v := v3 a b c'
  -- integer and rational versions of the two submatrices
  let Nz : Matrix (Fin 12) (Fin 12) ℤ := Matrix.of fun i u => M i (e u).1
  let Nq : Matrix (Fin 12) (Fin 12) ℚ := Matrix.of fun i u => (M i (e u).1 : ℚ)
  let Pq : Matrix (Fin 12) (Fin 3) ℚ := Matrix.of fun i t => (M i (v t) : ℚ)
  -- split of the row Gram matrix over the columns
  have hsplit : ∀ i k : Fin 12, ∑ j, (M i j : ℚ) * M k j = ∑ u, Nq i u * Nq k u + ∑ t, Pq i t * Pq k t := by
    intro i k
    rw [← Finset.sum_compl_add_sum S]
    congr 1
    · rw [← Finset.sum_coe_sort Sᶜ]
      exact (Equiv.sum_comp e (fun x : {j // j ∈ Sᶜ} => (M i x.1 : ℚ) * M k x.1)).symm
    · rw [hS, Finset.sum_insert (by simp [hab, hac]), Finset.sum_insert (by simpa using hbc), Finset.sum_singleton,
        Fin.sum_univ_three]
      simp [Pq, v, v3, add_assoc]
  have hNN : Nq * Nqᵀ = Aq - Pq * Pqᵀ := by
    ext i k
    have h := hsplit i k
    have hrow : ∑ j, (M i j : ℚ) * M k j = (if i = k then 8 else 0) + 6 := by
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
  -- the determinant lemma
  have hdet1 : (Nq * Nqᵀ).det = Aq.det * (1 - Pqᵀ * (Bq * Pq)).det := by
    have : Aq - Pq * Pqᵀ = Aq * (1 - (Bq * Pq) * Pqᵀ) := by
      rw [Matrix.mul_sub, Matrix.mul_one, ← Matrix.mul_assoc, ← Matrix.mul_assoc, AB, Matrix.one_mul]
    rw [hNN, this, Matrix.det_mul, Matrix.det_one_sub_mul_comm]
  -- column sums of the chosen columns are 8
  have hcol : ∀ t, ∑ i, Pq i t = 8 := by
    intro t
    have := hM.2.2.2.1 (v t)
    simp only [Pq, Matrix.of_apply]
    exact_mod_cast this
  have hJP : ∀ i t, (Jq (Fin 12) (Fin 12) * Pq) i t = 8 := by
    intro i t
    simp only [Matrix.mul_apply, Jq, Matrix.of_apply, one_mul]
    exact hcol t
  have hBP : ∀ i t, (Bq * Pq) i t = (1 / 8) * (Pq i t - 3 / 5) := by
    intro i t
    rw [Bq, Matrix.smul_mul, Matrix.sub_mul, Matrix.one_mul, Matrix.smul_mul, Matrix.smul_apply, Matrix.sub_apply,
      Matrix.smul_apply, hJP i t, smul_eq_mul, smul_eq_mul]
    ring
  have hv : Function.Injective (v3 a b c') := by
    intro x y hxy
    fin_cases x <;> fin_cases y <;> simp_all [v3, eq_comm]
  have hinner : 1 - Pqᵀ * (Bq * Pq) = (1 / 40 : ℚ) • (H3 a b c' M).map (Int.cast : ℤ → ℚ) := by
    ext s t
    have hsum : (Pqᵀ * (Bq * Pq)) s t = (1 / 8) * (∑ i, Pq i s * Pq i t) - (1 / 8) * (3 / 5) * (∑ i, Pq i s) := by
      simp only [Matrix.mul_apply, Matrix.transpose_apply, hBP]
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [Matrix.sub_apply, hsum, hcol s, Matrix.smul_apply, Matrix.map_apply, H3, Matrix.of_apply, H_apply,
      Matrix.one_apply, smul_eq_mul]
    simp only [Pq, Matrix.of_apply, v]
    by_cases hst : s = t
    · subst hst
      rw [if_pos rfl, if_pos rfl]
      push_cast
      ring
    · have hne : v3 a b c' s ≠ v3 a b c' t := fun h => hst (hv h)
      rw [if_neg hst, if_neg hne]
      push_cast
      ring
  -- assemble
  have hNz : Nq = Nz.map (Int.cast : ℤ → ℚ) := by ext i u; simp [Nq, Nz]
  have hcastN : ((Nz.det : ℤ) : ℚ) = (Nz.map (Int.cast : ℤ → ℚ)).det := by
    have := RingHom.map_det (Int.castRingHom ℚ) Nz
    simpa [RingHom.mapMatrix_apply] using this
  have hdetN : (Nq * Nqᵀ).det = ((Nz.det : ℤ) : ℚ) ^ 2 := by
    rw [Matrix.det_mul, Matrix.det_transpose, hNz, ← hcastN, sq]
  have hdetH : ((H3 a b c' M).map (Int.cast : ℤ → ℚ)).det = (((H3 a b c' M).det : ℤ) : ℚ) := by
    have := RingHom.map_det (Int.castRingHom ℚ) (H3 a b c' M)
    simpa [RingHom.mapMatrix_apply] using this.symm
  refine ⟨Nz.det, ?_⟩
  have key := hdet1
  rw [hdetN, hinner, Matrix.det_smul, hdetH, det_Aq] at key
  simp only [Fintype.card_fin] at key
  have : (25 : ℚ) * ((Nz.det : ℤ) : ℚ) ^ 2 = 2 ^ 28 * (((H3 a b c' M).det : ℤ) : ℚ) := by
    rw [key]
    ring
  exact_mod_cast this

/-! ### Closing arithmetic -/

lemma H3_det_formula (a b c' : Fin 15) : (H3 a b c' M).det =
    H M a a * H M b b * H M c' c' - H M a a * H M b c' * H M c' b - H M a b * H M b a * H M c' c'
    + H M a b * H M b c' * H M c' a + H M a c' * H M b a * H M c' b - H M a c' * H M b b * H M c' a := by
  rw [Matrix.det_fin_three]
  simp [H3, v3]

lemma sq_mod3 (d : ℤ) : d ^ 2 % 3 = 0 ∨ d ^ 2 % 3 = 1 := by
  rcases (by omega : d % 3 = 0 ∨ d % 3 = 1 ∨ d % 3 = 2) with h | h | h <;>
    simp [pow_two, Int.mul_emod, h]

lemma sq_mod7 (d : ℤ) : d ^ 2 % 7 = 0 ∨ d ^ 2 % 7 = 1 ∨ d ^ 2 % 7 = 2 ∨ d ^ 2 % 7 = 4 := by
  rcases (by omega : d % 7 = 0 ∨ d % 7 = 1 ∨ d % 7 = 2 ∨ d % 7 = 3 ∨ d % 7 = 4 ∨ d % 7 = 5 ∨ d % 7 = 6) with
    h | h | h | h | h | h | h <;> simp [pow_two, Int.mul_emod, h]

/-- `25 d^2 = 2^28 D` has no integer solution for `D` in `{50, 150, 200, -150}` -/
lemma bad_det (d D : ℤ) (h : 25 * d ^ 2 = 2 ^ 28 * D) (hD : D = 50 ∨ D = 150 ∨ D = 200 ∨ D = -150) : False := by
  rcases hD with rfl | rfl | rfl | rfl
  · have h2 : d ^ 2 = 2 ^ 29 := by linarith
    have h3 := sq_mod3 d
    rw [h2] at h3
    norm_num at h3
  · have h2 : d ^ 2 = 6 * 2 ^ 28 := by linarith
    have h3 := sq_mod7 d
    rw [h2] at h3
    norm_num at h3
  · have h2 : d ^ 2 = 2 ^ 31 := by linarith
    have h3 := sq_mod3 d
    rw [h2] at h3
    norm_num at h3
  · nlinarith [sq_nonneg d]

/-! ### The theorem -/

/-- **No BTD(12,15;6,2,10;8,6) exists**: there is no `12 × 15` matrix with entries in `{0, 1, 2}` such that every row
has exactly six entries `1` and exactly two entries `2`, every column sums to `8`, and any two distinct rows have
inner product `6`.  (Repeated columns are allowed; nothing else is assumed.) -/
theorem no_btd : Statement := by
  unfold Statement
  rintro ⟨M, hM⟩
  obtain ⟨hc1, hc2⟩ := counts hM
  set T2 := univ.filter fun j => c M j = 2 with hT2
  have hn2 : T2.card = ncols M 2 := rfl
  have hdiag2 : ∀ j ∈ T2, H M j j = 4 := fun j hj => by
    rw [H_diag hM j, (Finset.mem_filter.mp hj).2]; norm_num
  have hclass : ∀ j ∈ T2, (univ.filter fun k => H M j k = 4).card ≤ 5 :=
    fun j hj => class_le_five hM j (Finset.mem_filter.mp hj).2
  have partner : ∀ a ∈ T2, 5 < T2.card → ∃ b ∈ T2, a ≠ b ∧ H M a b = -1 := by
    intro a ha hcard
    obtain ⟨b, hb, hbn⟩ := Finset.exists_mem_notMem_of_card_lt_card (lt_of_le_of_lt (hclass a ha) hcard)
    have hab : a ≠ b := by
      rintro rfl
      exact hbn (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hdiag2 a ha⟩)
    have hne4 : H M a b ≠ 4 := fun h => hbn (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩)
    rcases type2_pair hM a b (Finset.mem_filter.mp ha).2 (Finset.mem_filter.mp hb).2 hab with h | h
    · exact ⟨b, hb, hab, h⟩
    · exact absurd h hne4
  -- at most two classes: n2 <= 10
  have hle10 : T2.card ≤ 10 := by
    by_contra hgt
    push_neg at hgt
    obtain ⟨a, ha⟩ : T2.Nonempty := Finset.card_pos.mp (by omega)
    obtain ⟨b, hb, hab, habv⟩ := partner a ha (by omega)
    have hunion : ((univ.filter fun k => H M a k = 4) ∪ (univ.filter fun k => H M b k = 4)).card < T2.card := by
      have h1 := Finset.card_union_le (univ.filter fun k => H M a k = 4) (univ.filter fun k => H M b k = 4)
      have h2 := hclass a ha
      have h3 := hclass b hb
      omega
    obtain ⟨c', hc', hcn⟩ := Finset.exists_mem_notMem_of_card_lt_card hunion
    rw [Finset.mem_union, not_or] at hcn
    have hac4 : H M a c' ≠ 4 := fun h => hcn.1 (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩)
    have hbc4 : H M b c' ≠ 4 := fun h => hcn.2 (Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩)
    have hac : a ≠ c' := by
      rintro rfl
      exact hac4 (hdiag2 a ha)
    have hbc : b ≠ c' := by
      rintro rfl
      exact hbc4 (hdiag2 b hb)
    have hac1 : H M a c' = -1 :=
      (type2_pair hM a c' (Finset.mem_filter.mp ha).2 (Finset.mem_filter.mp hc').2 hac).resolve_right hac4
    have hbc1 : H M b c' = -1 :=
      (type2_pair hM b c' (Finset.mem_filter.mp hb).2 (Finset.mem_filter.mp hc').2 hbc).resolve_right hbc4
    obtain ⟨d, hd⟩ := lemmaD hM a b c' hab hac hbc
    rw [H3_det_formula, H_symm b a, H_symm c' a, H_symm c' b, hdiag2 a ha, hdiag2 b hb, hdiag2 c' hc', habv,
      hac1, hbc1] at hd
    exact bad_det d _ hd (by norm_num)
  -- hence a column with exactly one entry 2 exists
  have hn1 : 0 < ncols M 1 := by omega
  obtain ⟨k, hk⟩ : (univ.filter fun j => c M j = 1).Nonempty := Finset.card_pos.mp hn1
  have hk1 : c M k = 1 := (Finset.mem_filter.mp hk).2
  obtain ⟨a, ha⟩ : T2.Nonempty := Finset.card_pos.mp (by omega)
  obtain ⟨b, hb, hab, habv⟩ := partner a ha (by omega)
  have ha2 : c M a = 2 := (Finset.mem_filter.mp ha).2
  have hb2 : c M b = 2 := (Finset.mem_filter.mp hb).2
  have hka : k ≠ a := by
    rintro rfl
    rw [hk1] at ha2
    exact absurd ha2 (by norm_num)
  have hkb : k ≠ b := by
    rintro rfl
    rw [hk1] at hb2
    exact absurd hb2 (by norm_num)
  have hkk : H M k k = 14 := by rw [H_diag hM k, hk1]; norm_num
  have hx := type12_pair hM k a hk1 ha2 hka
  have hy := type12_pair hM k b hk1 hb2 hkb
  rw [H_symm k a] at hx
  rw [H_symm k b] at hy
  obtain ⟨d, hd⟩ := lemmaD hM a b k hab (Ne.symm hka) (Ne.symm hkb)
  rw [H3_det_formula, H_symm b a, H_symm k a, H_symm k b, hdiag2 a ha, hdiag2 b hb, hkk, habv] at hd
  rcases hx with hx | hx | hx <;> rcases hy with hy | hy | hy <;> rw [hx, hy] at hd <;>
    exact bad_det d _ hd (by norm_num)

end BTD12
