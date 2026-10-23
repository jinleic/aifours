import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-! Elementary inequalities used by the interpolation argument, for every arity.

Derived from `SatUpper/Local.lean` of yamelton/sat-upper-4268 (Apache-2.0), where
the arity-three cubic `B^3 - 3 B C^2 + 2 C^3` appears. Here the arity is `m+1`
and the remainder is the degree-`(m+1)` Lelarge–Oulamara polynomial
`B^(m+1) - (m+1) B C^m + m C^(m+1)`. These theorems do not establish the
probabilistic interpolation inequality by themselves. -/

namespace KSatUpper

/-- The degree-`(m+1)` remainder: `B^(m+1) - (m+1) B C^m + m C^(m+1)`. -/
def polyRemainder (m : ℕ) (B C : ℝ) : ℝ :=
  B ^ (m + 1) - (m + 1) * B * C ^ m + m * C ^ (m + 1)

theorem polyRemainder_zero (B C : ℝ) : polyRemainder 0 B C = 0 := by
  simp [polyRemainder]

/-- One-step recursion; it proves the sign for every arity by induction. -/
theorem polyRemainder_succ (m : ℕ) (B C : ℝ) :
    polyRemainder (m + 1) B C = B * polyRemainder m B C + (m + 1) * C ^ m * (B - C) ^ 2 := by
  unfold polyRemainder
  push_cast
  ring

theorem polyRemainder_nonneg (m : ℕ) {B C : ℝ} (hB : 0 ≤ B) (hC : 0 ≤ C) :
    0 ≤ polyRemainder m B C := by
  induction m with
  | zero => simp [polyRemainder_zero]
  | succ m ih =>
    rw [polyRemainder_succ]
    exact add_nonneg (mul_nonneg hB ih) (by positivity)

/-- The closed factorization stated as (F) in the written proof:
`B^(m+2) - (m+2) B C^(m+1) + (m+1) C^(m+2) = (B-C)^2 Σ_{l≤m} (l+1) B^(m-l) C^l`. -/
theorem polyRemainder_factorization (m : ℕ) (B C : ℝ) :
    polyRemainder (m + 1) B C =
      (B - C) ^ 2 * ∑ l ∈ Finset.range (m + 1), ((l : ℝ) + 1) * B ^ (m - l) * C ^ l := by
  induction m with
  | zero =>
    simp [polyRemainder]
    ring
  | succ m ih =>
    rw [polyRemainder_succ, ih, Finset.sum_range_succ (n := m + 1)]
    have hs : B * ∑ l ∈ Finset.range (m + 1), ((l : ℝ) + 1) * B ^ (m - l) * C ^ l =
        ∑ l ∈ Finset.range (m + 1), ((l : ℝ) + 1) * B ^ (m + 1 - l) * C ^ l := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro l hl
      have hl' : l ≤ m := Nat.le_of_lt_succ (Finset.mem_range.mp hl)
      rw [show m + 1 - l = (m - l) + 1 by omega, pow_succ]
      ring
    rw [show m + 1 - (m + 1) = 0 by omega, pow_zero]
    calc
      B * ((B - C) ^ 2 * ∑ l ∈ Finset.range (m + 1), ((l : ℝ) + 1) * B ^ (m - l) * C ^ l) +
          ((m + 1 : ℕ) + 1 : ℝ) * C ^ (m + 1) * (B - C) ^ 2
          = (B - C) ^ 2 * (B * ∑ l ∈ Finset.range (m + 1), ((l : ℝ) + 1) * B ^ (m - l) * C ^ l) +
            ((m + 1 : ℕ) + 1 : ℝ) * C ^ (m + 1) * (B - C) ^ 2 := by ring
      _ = _ := by rw [hs]; push_cast; ring

/-- The arity-three member is exactly the upstream cubic remainder. -/
theorem polyRemainder_two (B C : ℝ) :
    polyRemainder 2 B C = B ^ 3 - 3 * B * C ^ 2 + 2 * C ^ 3 := by
  unfold polyRemainder
  norm_num

def noConflict (A B : ℝ) : ℝ := A + B - A * B

theorem noConflict_complement (A B : ℝ) :
    noConflict A B = 1 - (1 - A) * (1 - B) := by
  unfold noConflict
  ring

theorem factor_bounds {t : ℝ} (ht1 : t ≤ 1) {z : ℝ} (hz0 : 0 ≤ z) (hz1 : z ≤ 1) :
    t ≤ 1-(1-t)*z ∧ 1-(1-t)*z ≤ 1 := by
  constructor <;> nlinarith [mul_nonneg (sub_nonneg.mpr ht1) hz0,
    mul_nonneg (sub_nonneg.mpr ht1) (sub_nonneg.mpr hz1)]

end KSatUpper
