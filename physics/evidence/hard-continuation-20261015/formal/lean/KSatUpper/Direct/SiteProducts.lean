import KSatUpper.Ground.Site
import KSatUpper.PoissonPair
import KSatUpper.Criterion

/-! The site endpoint needs only products of no-warning probabilities.
Evaluate their mixed moments directly on the original Poisson sites.

Derived from `SatUpper/Direct/SiteProducts.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory KSatUpper.DirectFinite
open KSatUpper.PoissonConfiguration KSatUpper.PoissonFunctional
open scoped NNReal

namespace KSatUpper.DirectSiteProducts

variable {p : ℕ} (T : TrialLaw p) {m n : ℕ}

/-- The law of a site's `m` incoming labels. -/
noncomputable def markLaw (m : ℕ) : Measure (TrialVertex.Mark m p) :=
  Measure.pi (fun _ => T.law)

instance (m : ℕ) : IsProbabilityMeasure (markLaw T m) := by
  unfold markLaw
  infer_instance

noncomputable def test (a : Fin n × Bool) (x : Fresh m n p) : ℝ :=
  if (x 0).1 = a then T.mark (fun j : Fin m => (x j.succ).2) else 1

theorem test_bounds (a : Fin n × Bool) (x : Fresh m n p) :
    0 ≤ test T a x ∧ test T a x ≤ 1 := by
  unfold test
  split
  · exact T.mark_bounds _
  · norm_num

theorem test_disjoint (v : Fin n) (x : Fresh m n p) :
    test T (v,true) x = 1 ∨ test T (v,false) x = 1 := by
  by_cases h : (x 0).1 = (v,true)
  · right
    simp [test, h]
  · left
    simp [test, h]

variable [NeZero n]

theorem projection_law :
    Measure.map (fun x : Fresh m n p => ((x 0).1, fun j : Fin m => (x j.succ).2))
      (freshLaw T m n) = (uniform (Fin n × Bool)).prod (markLaw T m) := by
  have hcomp : (fun x : Fresh m n p => ((x 0).1, fun j : Fin m => (x j.succ).2)) =
      (Prod.map Prod.fst (fun t : Fin m → Seed n p => fun j => (t j).2)) ∘
        (fun v : Fresh m n p => (v 0, fun j : Fin m => v j.succ)) := rfl
  rw [hcomp, ← Measure.map_map (by fun_prop) (by fun_prop), freshLaw,
    DirectProduct.head_tail_law, ← Measure.map_prod_map _ _ measurable_fst (by fun_prop)]
  congr 1
  · simp [seedLaw, Measure.map_fst_prod]
  · rw [Measure.pi_map_pi (fun _ => measurable_snd.aemeasurable)]
    simp [seedLaw, Measure.map_snd_prod, markLaw]

theorem integral_test (a : Fin n × Bool) (F : ℝ → ℝ) (hF : F 1 = 1) :
    (∫ x, F (test T a x) ∂freshLaw T m n) =
      1 + ((∫ z, F (T.mark z) ∂markLaw T m)-1)/(2*n) := by
  have he : (fun x : Fresh m n p => F (test T a x)) =
      (fun z : (Fin n × Bool) × TrialVertex.Mark m p => if z.1 = a then F (T.mark z.2) else 1) ∘
        (fun x => ((x 0).1, fun j : Fin m => (x j.succ).2)) := by
    funext x
    simp only [Function.comp_apply, test]
    split <;> simp_all
  rw [he]
  change (∫ x, (if (x 0).1 = a then F (T.mark (fun j : Fin m => (x j.succ).2)) else 1)
    ∂freshLaw T m n) = _
  rw [← integral_map (measurable_of_countable
    (fun x : Fresh m n p => ((x 0).1, fun j : Fin m => (x j.succ).2))).aemeasurable
    (measurable_of_countable (fun z : (Fin n × Bool) × TrialVertex.Mark m p =>
      if z.1 = a then F (T.mark z.2) else 1)).aestronglyMeasurable, projection_law,
    integral_prod _ Integrable.of_finite]
  have hi (b : Fin n × Bool) :
      (∫ z, (if b = a then F (T.mark z) else 1) ∂markLaw T m) =
        1 + Set.indicator {a} (fun _ : Fin n × Bool => (∫ z, F (T.mark z) ∂markLaw T m)-1) b := by
    by_cases h : b = a <;> simp [h]
  simp_rw [hi]
  rw [integral_add (integrable_const _) Integrable.of_finite,
    integral_const, measureReal_univ_eq_one, one_smul,
    integral_indicator_const _ (measurableSet_singleton _)]
  rw [DirectProduct.uniform_eq_count]
  simp [measureReal_def, Measure.smul_apply, smul_eq_mul, ENNReal.toReal_inv,
    div_eq_mul_inv, mul_comm]

noncomputable def side (a : Fin n × Bool) : Configuration (Fresh m n p) → ℝ :=
  productTest (test T a)

omit [NeZero n] in
theorem side_bounds (a : Fin n × Bool) (c : Configuration (Fresh m n p)) :
    0 ≤ side T a c ∧ side T a c ≤ 1 :=
  productTest_bounds (fun x => (test_bounds T a x).1) (fun x => (test_bounds T a x).2) c

theorem mixed_moment {α : ℝ} (r : ℝ≥0) (hr : (r : ℝ)/(2*n) = ((m : ℝ)+1)*α/2)
    (v : Fin n) (j k : ℕ) :
    (∫ c, side T (v,true) c ^ j * side T (v,false) c ^ k ∂poisson r (freshLaw T m n)) =
      Criterion.poissonProductMoment T m α j * Criterion.poissonProductMoment T m α k := by
  rw [side, side, PoissonPair.mixed_moment r (freshLaw T m n)
    (fun x => (test_bounds T (v,true) x).1) (fun x => (test_bounds T (v,true) x).2)
    (fun x => (test_bounds T (v,false) x).1) (fun x => (test_bounds T (v,false) x).2)
    (test_disjoint T v)]
  rw [integral_test T _ (fun z => z ^ j) (one_pow j), integral_test T _ (fun z => z ^ k) (one_pow k)]
  simp only [markLaw, TrialLaw.integral_mark_pow]
  unfold Criterion.poissonProductMoment
  congr 1 <;> congr 1 <;> rw [add_sub_cancel_left, mul_div_assoc', ← div_mul_eq_mul_div, hr]

theorem integrable_complement (r : ℝ≥0) (v : Fin n) (k : ℕ) :
    Integrable (fun c => ((1-side T (v,true) c)*(1-side T (v,false) c))^k)
      (poisson r (freshLaw T m n)) := by
  apply ReplicaMoments.integrable_unit_interval _
    (((measurable_const.sub (measurable_productTest (measurable_of_countable _))).mul
      (measurable_const.sub (measurable_productTest (measurable_of_countable _)))).pow_const k)
  · intro c
    exact pow_nonneg (mul_nonneg (sub_nonneg.mpr (side_bounds T _ c).2)
      (sub_nonneg.mpr (side_bounds T _ c).2)) k
  · intro c
    have hA := side_bounds T (v,true) c
    have hB := side_bounds T (v,false) c
    dsimp only [side] at hA hB
    apply pow_le_one₀ (mul_nonneg (by linarith) (by linarith))
    exact mul_le_one₀ (by linarith) (by linarith) (by linarith)

noncomputable def upper (K : ℕ) (δ : ℝ) (v : Fin n) (c : Configuration (Fresh m n p)) : ℝ :=
  PoissonPair.majorant K δ (side T (v,true) c) (side T (v,false) c)

theorem integrable_upper (r : ℝ≥0) (K : ℕ) (δ : ℝ) (v : Fin n) :
    Integrable (upper T K δ v) (poisson r (freshLaw T m n)) := by
  simpa only [upper, PoissonPair.majorant] using
    (integrable_finset_sum (Finset.range K) (fun k _ =>
      (integrable_complement (m := m) T r v (k+1)).div_const (k+1 : ℝ))).neg.add
      (integrable_const (K*δ))

theorem integral_upper {α : ℝ} (r : ℝ≥0) (hr : (r : ℝ)/(2*n) = ((m : ℝ)+1)*α/2)
    (K : ℕ) (δ : ℝ) (v : Fin n) :
    (∫ c, upper T K δ v c ∂poisson r (freshLaw T m n)) =
      negativeMomentSum K (Criterion.noWarningMoment T m α) + K*δ := by
  have he (k : ℕ) :
      (∫ c, ((1-side T (v,true) c)*(1-side T (v,false) c))^k ∂poisson r (freshLaw T m n)) =
        (Criterion.noWarningMoment T m α k)^2 :=
    PoissonPair.complement_moment _ (measurable_productTest (measurable_of_countable _))
      (measurable_productTest (measurable_of_countable _))
      (fun c => (side_bounds T _ c).1) (fun c => (side_bounds T _ c).2)
      (fun c => (side_bounds T _ c).1) (fun c => (side_bounds T _ c).2)
      (Criterion.poissonProductMoment T m α) (mixed_moment T r hr v) k
  unfold upper PoissonPair.majorant
  have hi := integral_add (integrable_finset_sum (Finset.range K) (fun k _ =>
    (integrable_complement (m := m) T r v (k+1)).div_const (k+1 : ℝ))).neg (integrable_const (K*δ))
  simp only [Pi.neg_apply] at hi
  rw [hi,
    integral_neg, integral_finset_sum _ (fun k _ =>
      (integrable_complement (m := m) T r v (k+1)).div_const (k+1 : ℝ)),
    integral_const, measureReal_univ_eq_one, one_smul]
  simp_rw [integral_div, he]
  rfl

end KSatUpper.DirectSiteProducts
