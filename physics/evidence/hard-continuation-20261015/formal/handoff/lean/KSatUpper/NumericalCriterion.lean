import KSatUpper.GridExponential
import KSatUpper.VertexEnclosures
import KSatUpper.Criterion
import KSatUpper.Trial

/-! A sound rational upper bound for the criterion `Psi_T`, computable in the kernel.

The construction follows `SatUpper/NumericalMoments.lean`, `NumericalLogs.lean` and
`NumericalEnclosure.lean` of yamelton/sat-upper-4268 (Apache-2.0): exponential enclosures
by the tangent bound and repeated squaring with outward rounding, signed interval
arithmetic for the alternating moments, and a logarithmic series with a proved
remainder. Differences: the trial law, arity and density are parameters; the edge
expectation uses exact moments `E (R_1 ⋯ R_{m+1})^h = C_h^{m+1}` and a uniform
geometric remainder; the argument bound `argument ≤ 0` is proved, not computed. -/

open MeasureTheory

namespace KSatUpper.NumericalCriterion

variable {p : ℕ} (T : TrialLaw p) (m : ℕ) (α : ℚ)

/-- `λ (ν_j - 1)` with `λ = (m+1) α / 2`. -/
def argument (j : ℕ) : ℚ := ((m + 1 : ℚ) * α / 2) * (T.markMoment m j - 1)

theorem argument_nonpos (hα : 0 ≤ α) (j : ℕ) : argument T m α j ≤ 0 := by
  unfold argument
  have h1 := T.markMoment_le_one m j
  have h2 : (0 : ℚ) ≤ (m + 1 : ℚ) * α / 2 := by positivity
  nlinarith

theorem poissonProductMoment_eq (j : ℕ) :
    Criterion.poissonProductMoment T m (α : ℝ) j = Real.exp ((argument T m α j : ℚ) : ℝ) := by
  unfold Criterion.poissonProductMoment argument
  push_cast
  ring_nf

/-- Outward-rounded enclosure of `exp (argument j)` on the grid `2^-160`. -/
def bounds (j : ℕ) : ℚ × ℚ :=
  let b := GridExponential.bounds (2^320) 160 (argument T m α j)
  (Enclosures.lowerOnGrid (2^160) b.1, Enclosures.upperOnGrid (2^160) b.2)

def table (cutoff : ℕ) : List (ℚ × ℚ) := (List.range (cutoff + 1)).map (bounds T m α)

def lowerOf (tbl : List (ℚ × ℚ)) (j : ℕ) : ℚ := (tbl.getD j (0, 0)).1

def upperOf (tbl : List (ℚ × ℚ)) (j : ℕ) : ℚ := (tbl.getD j (0, 0)).2

theorem enclosures (hα : 0 ≤ α) (cutoff j : ℕ) (hj : j ≤ cutoff) :
    (lowerOf (table T m α cutoff) j : ℝ) ≤ Criterion.poissonProductMoment T m (α : ℝ) j ∧
    Criterion.poissonProductMoment T m (α : ℝ) j ≤ (upperOf (table T m α cutoff) j : ℝ) := by
  have ht : (table T m α cutoff).getD j (0, 0) = bounds T m α j := by
    simp [table, List.getD, List.getElem?_range (Nat.lt_succ_of_le hj)]
  have hx : argument T m α j < (2 : ℚ)^160 :=
    (argument_nonpos T m α hα j).trans_lt (by positivity)
  have hb := GridExponential.bounds_correct (scale := 2^320) (by norm_num) 160
    (argument T m α j) hx
  have hr := Enclosures.rounded_enclosure (scale := 2^160) (by norm_num) hb.1 hb.2
  rw [poissonProductMoment_eq]
  simpa only [lowerOf, upperOf, ht, bounds] using hr

/-- For `0 ≤ x ≤ xb < 1`: `log(1-x) ≥ -Σ_{k<N} x^(k+1)/(k+1) - xb^(N+1)/(1-xb)`. -/
theorem log_one_sub_lower {x xb : ℝ} (hx0 : 0 ≤ x) (hxb : x ≤ xb) (hxb1 : xb < 1) (N : ℕ) :
    -(∑ k ∈ Finset.range N, x^(k+1)/(k+1)) - xb^(N+1)/(1-xb) ≤ Real.log (1 - x) := by
  have hx1 : x < 1 := lt_of_le_of_lt hxb hxb1
  have he := Real.abs_log_sub_add_sum_range_le (show |x| < 1 by rwa [abs_of_nonneg hx0]) N
  rw [abs_of_nonneg hx0] at he
  have hl := (abs_le.mp he).1
  have htail : x^(N+1)/(1-x) ≤ xb^(N+1)/(1-xb) :=
    div_le_div₀ (pow_nonneg (hx0.trans hxb) _) (pow_le_pow_left₀ hx0 hxb _) (by linarith)
      (by linarith)
  linarith

/-- Rational lower bound for `d_∞ = E log(1 - R_1 ⋯ R_{m+1})`, given `rate ≤ u < 1`. -/
def edgeLower (N : ℕ) (u : ℚ) : ℚ :=
  -(∑ k ∈ Finset.range N, T.moment (k+1) ^ (m+1) / (k+1)) - (u^(m+1))^(N+1)/(1 - u^(m+1))

theorem edgeLower_le (N : ℕ) {u : ℚ} (hu0 : 0 ≤ u) (hu : ∀ i, T.rate i ≤ u) (hu1 : u < 1) :
    (edgeLower T m N u : ℝ) ≤ Criterion.edgeExpectation T m := by
  have hxb1 : (u : ℝ)^(m+1) < 1 :=
    pow_lt_one₀ (by exact_mod_cast hu0) (by exact_mod_cast hu1) (by omega)
  have hpt (t : Fin (m+1) → Fin p) :
      -(∑ k ∈ Finset.range N, (∏ j, (T.rate (t j) : ℝ))^(k+1)/(k+1)) -
        ((u : ℝ)^(m+1))^(N+1)/(1 - (u : ℝ)^(m+1)) ≤ Real.log (1 - ∏ j, (T.rate (t j) : ℝ)) :=
    log_one_sub_lower (T.prod_rate_bounds t).1 (T.prod_rate_le hu t) hxb1 N
  have hint := integral_mono (μ := Measure.pi (fun _ : Fin (m+1) => T.law))
    Integrable.of_finite Integrable.of_finite hpt
  rw [integral_sub Integrable.of_finite (integrable_const _), integral_neg,
    integral_finset_sum _ (fun _ _ => Integrable.of_finite)] at hint
  simp_rw [integral_div, T.integral_prod_rate_pow] at hint
  simp only [integral_const, measureReal_univ_eq_one, one_smul] at hint
  unfold edgeLower Criterion.edgeExpectation
  push_cast
  exact hint

/-- The kernel-computable certificate value; the exponential table is computed once. -/
def certUpper (cutoff N : ℕ) (u : ℚ) : ℚ :=
  let tbl := table T m α cutoff
  VertexEnclosures.vertexUpper cutoff (lowerOf tbl) (upperOf tbl) +
    (-(m : ℚ)) * α * edgeLower T m N u

theorem finiteAnalyticBound_le_cert (hα : 0 ≤ α) (cutoff N : ℕ) {u : ℚ} (hu0 : 0 ≤ u)
    (hu : ∀ i, T.rate i ≤ u) (hu1 : u < 1) :
    Criterion.finiteAnalyticBound T m (α : ℝ) cutoff ≤ (certUpper T m α cutoff N u : ℝ) := by
  have hv := VertexEnclosures.vertexUpper_correct (P := Criterion.poissonProductMoment T m α)
    (K := cutoff) (fun j hj => enclosures T m α hα cutoff j hj)
  have he := edgeLower_le T m N hu0 hu hu1
  have hmα : -(m : ℝ) * (α : ℝ) ≤ 0 := by
    have := mul_nonneg (Nat.cast_nonneg m : (0 : ℝ) ≤ m) (by exact_mod_cast hα : (0 : ℝ) ≤ α)
    linarith
  have hprod := mul_le_mul_of_nonpos_left he hmα
  unfold Criterion.finiteAnalyticBound Criterion.edgeCorrection
  simp only [certUpper]
  push_cast
  change negativeMomentSum cutoff (VertexEnclosures.alternating
    (Criterion.poissonProductMoment T m (α : ℝ))) + _ ≤ _
  linarith

end KSatUpper.NumericalCriterion
