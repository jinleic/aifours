import KSatUpper.Series
import KSatUpper.Enclosures

/-! Signed interval arithmetic for the alternating vertex moments, for any real sequence.

Derived from `SatUpper/VertexEnclosures.lean` (yamelton/sat-upper-4268, Apache-2.0),
where the sequence was the fixed arity-three Poisson product moment. -/

namespace KSatUpper.VertexEnclosures

def coefficient (k j : ℕ) : ℚ :=
  (-1 : ℚ)^j * (k.factorial / (j.factorial * (k-j).factorial) : ℕ)

theorem coefficient_cast {k j : ℕ} (hj : j ≤ k) :
    (coefficient k j : ℝ) = (-1 : ℝ)^j * (Nat.choose k j : ℝ) := by
  rw [Nat.choose_eq_factorial_div_factorial hj]
  simp [coefficient]

def signedLower (c l u : ℚ) : ℚ := if 0 ≤ c then c*l else c*u

theorem signedLower_le {c l u : ℚ} {x : ℝ}
    (hl : (l : ℝ) ≤ x) (hu : x ≤ (u : ℝ)) :
    (signedLower c l u : ℝ) ≤ (c : ℝ)*x := by
  unfold signedLower
  split_ifs with hc
  · push_cast
    exact mul_le_mul_of_nonneg_left hl (by exact_mod_cast hc)
  · push_cast
    exact mul_le_mul_of_nonpos_left hu (by exact_mod_cast le_of_not_ge hc)

def momentLower (l u : ℕ → ℚ) (k : ℕ) : ℚ :=
  ∑ j ∈ Finset.range (k+1), signedLower (coefficient k j) (l j) (u j)

/-- The alternating binomial transform of any enclosed sequence. -/
noncomputable def alternating (P : ℕ → ℝ) (k : ℕ) : ℝ :=
  ∑ j ∈ Finset.range (k+1), (-1 : ℝ)^j * (Nat.choose k j : ℝ) * P j

theorem momentLower_le {P : ℕ → ℝ} {l u : ℕ → ℚ} {k : ℕ}
    (hb : ∀ j, j ≤ k → (l j : ℝ) ≤ P j ∧ P j ≤ (u j : ℝ)) :
    (momentLower l u k : ℝ) ≤ alternating P k := by
  unfold momentLower alternating
  push_cast
  apply Finset.sum_le_sum
  intro j hj
  have hjk : j ≤ k := by simpa only [Finset.mem_range, Nat.lt_succ_iff] using hj
  have h := signedLower_le (c := coefficient k j) (hb j hjk).1 (hb j hjk).2
  rwa [coefficient_cast hjk] at h

/-- Squaring a clamped lower endpoint needs no sign assumption on the target. -/
theorem clamped_square_le {l x : ℝ} (h : l ≤ x) : (max 0 l)^2 ≤ x^2 := by
  by_cases hl : 0 ≤ l
  · rw [max_eq_right hl]
    nlinarith
  · rw [max_eq_left (le_of_not_ge hl)]
    simpa using sq_nonneg x

def vertexUpper (K : ℕ) (l u : ℕ → ℚ) : ℚ :=
  -∑ k ∈ Finset.range K, (max 0 (momentLower l u (k+1)))^2 / (k+1)

theorem vertexUpper_correct {P : ℕ → ℝ} {K : ℕ} {l u : ℕ → ℚ}
    (hb : ∀ j, j ≤ K → (l j : ℝ) ≤ P j ∧ P j ≤ (u j : ℝ)) :
    negativeMomentSum K (alternating P) ≤ (vertexUpper K l u : ℝ) := by
  unfold negativeMomentSum vertexUpper
  push_cast
  apply neg_le_neg
  apply Finset.sum_le_sum
  intro k hk
  apply div_le_div_of_nonneg_right _ (by positivity)
  apply clamped_square_le
  apply momentLower_le
  intro j hj
  apply hb j
  have hk' := Finset.mem_range.mp hk
  omega

end KSatUpper.VertexEnclosures
