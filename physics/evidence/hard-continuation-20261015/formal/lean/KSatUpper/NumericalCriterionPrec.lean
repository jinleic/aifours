import KSatUpper.NumericalCriterion

/-! Precision-parameterized form of the certificate in `NumericalCriterion`.

At cutoff `T` the alternating sums amplify enclosure errors by up to `2^T`, so `T = 512`
needs a finer output grid than the fixed `2^-160` used at `T = 128`. Here the squaring grid
`2^-g`, the number of squarings `q` and the output grid `2^-r` are parameters. Soundness holds
for every choice; only the attainable sharpness depends on them. -/

namespace KSatUpper.NumericalCriterion

variable {p : ℕ} (T : TrialLaw p) (m : ℕ) (α : ℚ)

def boundsP (g q r : ℕ) (j : ℕ) : ℚ × ℚ :=
  let b := GridExponential.bounds (2^g) q (argument T m α j)
  (Enclosures.lowerOnGrid (2^r) b.1, Enclosures.upperOnGrid (2^r) b.2)

def tableP (g q r cutoff : ℕ) : List (ℚ × ℚ) :=
  (List.range (cutoff + 1)).map (boundsP T m α g q r)

theorem enclosuresP (hα : 0 ≤ α) (g q r cutoff j : ℕ) (hj : j ≤ cutoff) :
    (lowerOf (tableP T m α g q r cutoff) j : ℝ) ≤ Criterion.poissonProductMoment T m (α : ℝ) j ∧
    Criterion.poissonProductMoment T m (α : ℝ) j ≤ (upperOf (tableP T m α g q r cutoff) j : ℝ) := by
  have ht : (tableP T m α g q r cutoff).getD j (0, 0) = boundsP T m α g q r j := by
    simp [tableP, List.getD, List.getElem?_range (Nat.lt_succ_of_le hj)]
  have hx : argument T m α j < (2 : ℚ)^q :=
    (argument_nonpos T m α hα j).trans_lt (by positivity)
  have hb := GridExponential.bounds_correct (scale := 2^g) (by positivity) q
    (argument T m α j) hx
  have hr := Enclosures.rounded_enclosure (scale := 2^r) (by positivity) hb.1 hb.2
  rw [poissonProductMoment_eq]
  simpa only [lowerOf, upperOf, ht, boundsP] using hr

/-- The kernel-computable certificate value at precision `(g, q, r)`. -/
def certUpperP (g q r cutoff N : ℕ) (u : ℚ) : ℚ :=
  let tbl := tableP T m α g q r cutoff
  VertexEnclosures.vertexUpper cutoff (lowerOf tbl) (upperOf tbl) +
    (-(m : ℚ)) * α * edgeLower T m N u

theorem finiteAnalyticBound_le_certP (hα : 0 ≤ α) (g q r cutoff N : ℕ) {u : ℚ} (hu0 : 0 ≤ u)
    (hu : ∀ i, T.rate i ≤ u) (hu1 : u < 1) :
    Criterion.finiteAnalyticBound T m (α : ℝ) cutoff ≤
      (certUpperP T m α g q r cutoff N u : ℝ) := by
  have hv := VertexEnclosures.vertexUpper_correct (P := Criterion.poissonProductMoment T m α)
    (K := cutoff) (fun j hj => enclosuresP T m α hα g q r cutoff j hj)
  have he := edgeLower_le T m N hu0 hu hu1
  have hmα : -(m : ℝ) * (α : ℝ) ≤ 0 := by
    have := mul_nonneg (Nat.cast_nonneg m : (0 : ℝ) ≤ m) (by exact_mod_cast hα : (0 : ℝ) ≤ α)
    linarith
  have hprod := mul_le_mul_of_nonpos_left he hmα
  unfold Criterion.finiteAnalyticBound Criterion.edgeCorrection
  simp only [certUpperP]
  push_cast
  change negativeMomentSum cutoff (VertexEnclosures.alternating
    (Criterion.poissonProductMoment T m (α : ℝ))) + _ ≤ _
  linarith

end KSatUpper.NumericalCriterion
