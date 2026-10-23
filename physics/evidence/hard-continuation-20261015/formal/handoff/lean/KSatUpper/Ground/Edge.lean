import KSatUpper.Ground.Insertion
import KSatUpper.Criterion

/-! Average the energetic correction over the finite warning-rate distribution.

Derived from `SatUpper/Ground/Edge.lean` (yamelton/sat-upper-4268, Apache-2.0). The
finite-temperature correction is bounded by the zero-temperature one, `d_y ≥ d_∞`. -/

open MeasureTheory KSatUpper.DirectFinite KSatUpper.GroundInsertion

namespace KSatUpper.GroundEdge

variable {p : ℕ} (T : TrialLaw p)

theorem survey_law (m n : ℕ) [NeZero n] :
    Measure.map (fun x : Fresh m n p => fun j => (x j).2) (freshLaw T m n) =
      Measure.pi (fun _ : Fin (m + 1) => T.law) := by
  unfold freshLaw
  rw [Measure.pi_map_pi (fun _ => measurable_snd.aemeasurable)]
  simp only [seedLaw, Measure.map_snd_prod, measure_univ, one_smul]

theorem edgeMean_eq (m n : ℕ) [NeZero n] (y : ℝ) :
    edgeMean T m n y = ∫ t : Fin (m + 1) → Fin p,
      Real.log (1-(1-Real.exp (-y))*∏ j, (T.rate (t j) : ℝ)) ∂Measure.pi (fun _ => T.law) := by
  unfold GroundInsertion.edgeMean
  rw [← survey_law T m n, integral_map (measurable_of_countable _).aemeasurable
    (measurable_of_countable _).aestronglyMeasurable]

theorem prod_rate_lt_one {m : ℕ} (t : Fin (m + 1) → Fin p) : ∏ j, (T.rate (t j) : ℝ) < 1 := by
  rw [Fin.prod_univ_succ]
  have h0 := T.rate_bounds (t 0)
  have hr := T.prod_rate_bounds (fun j : Fin m => t j.succ)
  calc (T.rate (t 0) : ℝ) * ∏ j : Fin m, (T.rate (t j.succ) : ℝ) ≤ (T.rate (t 0) : ℝ) * 1 :=
        mul_le_mul_of_nonneg_left hr.2 h0.1
    _ < 1 := by linarith [h0.2]

theorem correction_bound (m n : ℕ) [NeZero n] {α y : ℝ} (hα : 0 ≤ α) :
    -(m : ℝ) * α * edgeMean T m n y ≤ Criterion.edgeCorrection T m α := by
  have h : Criterion.edgeExpectation T m ≤ edgeMean T m n y := by
    rw [edgeMean_eq]
    apply integral_mono Integrable.of_finite Integrable.of_finite
    intro t
    have hX := T.prod_rate_bounds t
    have hX1 := prod_rate_lt_one T t
    have hq : 0 ≤ Real.exp (-y) := (Real.exp_pos _).le
    apply Real.log_le_log (by linarith)
    nlinarith [mul_nonneg hq hX.1]
  unfold Criterion.edgeCorrection
  have hmα : -(m : ℝ) * α ≤ 0 := by
    have := mul_nonneg (Nat.cast_nonneg m : (0 : ℝ) ≤ m) hα
    linarith
  exact mul_le_mul_of_nonpos_left h hmα

end KSatUpper.GroundEdge
