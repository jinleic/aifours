import KSatUpper.Ground.Insertion
import KSatUpper.Direct.Poisson

/-! Average the finite insertion inequality, then compare the two Poisson endpoints.

Derived from `SatUpper/Ground/Comparison.lean` (yamelton/sat-upper-4268, Apache-2.0),
which specializes the clause/site Poisson interpolation of Franz–Leone,
Section III.B (51)–(54), https://arxiv.org/pdf/cond-mat/0208280, to integer
minimum costs. Here the arity is `m+1`. -/

open MeasureTheory KSatUpper.DirectFinite KSatUpper.GroundFinite KSatUpper.GroundInsertion
open scoped NNReal

namespace KSatUpper.GroundComparison

variable {p : ℕ} (T : TrialLaw p) (m : ℕ)

noncomputable def mean (n : ℕ) [NeZero n] (y : ℝ) (K L : ℕ) : ℝ :=
  ∫ c : Fin K → Fresh m n p, ∫ s : Fin L → Fresh m n p, entropy T y c s
    ∂Measure.pi (fun _ => freshLaw T m n) ∂Measure.pi (fun _ => freshLaw T m n)

variable {n : ℕ} [NeZero n]

theorem clause_difference (y : ℝ) (K L : ℕ) :
    mean T m n y (K+1) L-mean T m n y K L =
      ∫ c : Fin K → Fresh m n p, ∫ s : Fin L → Fresh m n p,
        ∫ x, entropy T y (Fin.cons x c) s-entropy T y c s ∂freshLaw T m n
        ∂Measure.pi (fun _ => freshLaw T m n) ∂Measure.pi (fun _ => freshLaw T m n) := by
  have he (c : Fin K → Fresh m n p) :
      (∫ x, ∫ s : Fin L → Fresh m n p, entropy T y (Fin.cons x c) s
        ∂Measure.pi (fun _ => freshLaw T m n) ∂freshLaw T m n) =
      ∫ s : Fin L → Fresh m n p, ∫ x, entropy T y (Fin.cons x c) s
        ∂freshLaw T m n ∂Measure.pi (fun _ => freshLaw T m n) :=
    integral_integral_swap Integrable.of_finite
  unfold mean
  rw [DirectProduct.integral_iid_cons]
  simp_rw [he, integral_sub Integrable.of_finite Integrable.of_finite,
    integral_const, measureReal_univ_eq_one, one_smul]

theorem site_difference (y : ℝ) (K L : ℕ) :
    mean T m n y K (L+1)-mean T m n y K L =
      ∫ c : Fin K → Fresh m n p, ∫ s : Fin L → Fresh m n p,
        ∫ x, entropy T y c (Fin.cons x s)-entropy T y c s ∂freshLaw T m n
        ∂Measure.pi (fun _ => freshLaw T m n) ∂Measure.pi (fun _ => freshLaw T m n) := by
  unfold mean
  simp_rw [DirectProduct.integral_iid_cons,
    integral_sub Integrable.of_finite Integrable.of_finite,
    integral_const, measureReal_univ_eq_one, one_smul]

theorem clause_difference_bound {y : ℝ} (hy : 0 ≤ y) (K L : ℕ) :
    ‖mean T m n y (K+1) L-mean T m n y K L‖ ≤ y := by
  rw [clause_difference]
  have h1 (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
      ‖∫ x, entropy T y (Fin.cons x c) s-entropy T y c s ∂freshLaw T m n‖ ≤ y := by
    simpa using norm_integral_le_of_norm_le_const (μ := freshLaw T m n)
      (Filter.Eventually.of_forall (clause_increment_bound T hy c s))
  have h2 (c : Fin K → Fresh m n p) :
      ‖∫ s : Fin L → Fresh m n p, ∫ x, entropy T y (Fin.cons x c) s-entropy T y c s
        ∂freshLaw T m n ∂Measure.pi (fun _ => freshLaw T m n)‖ ≤ y := by
    simpa using norm_integral_le_of_norm_le_const
      (μ := Measure.pi (fun _ : Fin L => freshLaw T m n)) (Filter.Eventually.of_forall (h1 c))
  simpa using norm_integral_le_of_norm_le_const
    (μ := Measure.pi (fun _ : Fin K => freshLaw T m n)) (Filter.Eventually.of_forall h2)

theorem site_difference_bound {y : ℝ} (hy : 0 ≤ y) (K L : ℕ) :
    ‖mean T m n y K (L+1)-mean T m n y K L‖ ≤ y := by
  rw [site_difference]
  have h1 (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
      ‖∫ x, entropy T y c (Fin.cons x s)-entropy T y c s ∂freshLaw T m n‖ ≤ y := by
    simpa using norm_integral_le_of_norm_le_const (μ := freshLaw T m n)
      (Filter.Eventually.of_forall (site_increment_bound T hy c s))
  have h2 (c : Fin K → Fresh m n p) :
      ‖∫ s : Fin L → Fresh m n p, ∫ x, entropy T y c (Fin.cons x s)-entropy T y c s
        ∂freshLaw T m n ∂Measure.pi (fun _ => freshLaw T m n)‖ ≤ y := by
    simpa using norm_integral_le_of_norm_le_const
      (μ := Measure.pi (fun _ : Fin L => freshLaw T m n)) (Filter.Eventually.of_forall (h1 c))
  simpa using norm_integral_le_of_norm_le_const
    (μ := Measure.pi (fun _ : Fin K => freshLaw T m n)) (Filter.Eventually.of_forall h2)

/-- (G) of the written proof, averaged over all old rows. -/
theorem difference_sign {y : ℝ} (hy : 0 ≤ y) (K L : ℕ) :
    mean T m n y (K+1) L-mean T m n y K L - ((m : ℝ)+1)*(mean T m n y K (L+1)-mean T m n y K L) +
      (m : ℝ)*edgeMean T m n y ≤ 0 := by
  have hi (c : Fin K → Fresh m n p) := integral_nonpos
    (μ := Measure.pi (fun _ : Fin L => freshLaw T m n)) (fun s => poly_nonpos T hy c s)
  have h := integral_nonpos (μ := Measure.pi (fun _ : Fin K => freshLaw T m n)) hi
  rw [clause_difference T m y K L, site_difference T m y K L]
  simpa only [integral_add Integrable.of_finite Integrable.of_finite,
    integral_sub Integrable.of_finite Integrable.of_finite, integral_const_mul,
    integral_const, measureReal_univ_eq_one, one_smul] using h

theorem endpoint_comparison {y : ℝ} (hy : 0 ≤ y) (a : ℝ≥0) :
    DirectPoisson.expectation (mean T m n y) a 0 ≤
      DirectPoisson.expectation (mean T m n y) 0 (((m : ℝ≥0)+1)*a) -
        (m : ℝ)*a*edgeMean T m n y :=
  DirectPoisson.comparison (clause_difference_bound T m hy)
    (site_difference_bound T m hy) (difference_sign T m hy) a

end KSatUpper.GroundComparison
