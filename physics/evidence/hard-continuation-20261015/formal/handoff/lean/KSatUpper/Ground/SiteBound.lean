import KSatUpper.Direct.SiteProducts
import KSatUpper.Ground.Site
import KSatUpper.PoissonMixture

/-! Bound the site entropy by a finite polynomial, then evaluate its Poisson expectation.

Derived from `SatUpper/Ground/SiteBound.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory ProbabilityTheory KSatUpper.DirectFinite KSatUpper.GroundFinite
open KSatUpper.DirectSiteProducts KSatUpper.PoissonConfiguration
open scoped NNReal

namespace KSatUpper.GroundSiteBound

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

theorem product_surveys {n L : ℕ} (s : Fin L → Fresh m n p) (v : Fin n) (b : Bool) :
    (∏ i, T.mark (SiteSideLaw.surveys (fun i j => (s i j).1) v b
      (fun r => (s r.1 r.2).2) i)) = side T (v,b) ⟨L,s⟩ := by
  unfold side PoissonFunctional.productTest test
  rw [← Finset.prod_filter]
  symm
  exact Finset.prod_subtype _ (by simp [Prod.ext_iff]) _

theorem entropy_le {n L : ℕ} {y : ℝ} (hy : 0 ≤ y)
    (s : Fin L → Fresh m n p) (K : ℕ) :
    entropy T y Fin.elim0 s ≤ ∑ v : Fin n, upper T K (Real.exp (-y)) v ⟨L,s⟩ := by
  have he := GroundSite.entropy_le T hy (fun i j => (s i j).1) (fun r => (s r.1 r.2).2)
  change entropy T y Fin.elim0 s ≤ _ at he
  simp_rw [GroundSite.vertex_moment, product_surveys] at he
  refine he.trans (Finset.sum_le_sum (fun v _ => ?_))
  exact PoissonPair.log_majorant (side_bounds T (v,true) ⟨L,s⟩).1
    (side_bounds T (v,true) ⟨L,s⟩).2 (side_bounds T (v,false) ⟨L,s⟩).1
    (side_bounds T (v,false) ⟨L,s⟩).2 (Real.exp_pos (-y))
    (Real.exp_le_one_iff.mpr (neg_nonpos.mpr hy)) K

noncomputable def configEntropy {n : ℕ} (y : ℝ) (c : Configuration (Fresh m n p)) : ℝ :=
  entropy T y Fin.elim0 c.2

theorem measurable_configEntropy (n : ℕ) (y : ℝ) :
    Measurable (configEntropy T (m := m) (n := n) y) :=
  measurable_fromConfiguration (fun _ => measurable_of_countable _)

theorem integrable_entropy {n : ℕ} [NeZero n] {y : ℝ} (hy : 0 ≤ y)
    (r : ℝ≥0) : Integrable (configEntropy T (m := m) (n := n) y) (poisson r (freshLaw T m n)) := by
  apply ((CompoundPoissonMoments.integrable_size r (freshLaw T m n)).const_mul y).mono'
    (measurable_configEntropy T n y).aestronglyMeasurable
  filter_upwards [] with c
  have h := GroundFinite.entropy_bounds T hy (Fin.elim0 : Fin 0 → Fresh m n p) c.2
  simp only [Nat.cast_zero, zero_add] at h
  change ‖GroundFinite.entropy T y Fin.elim0 c.2‖ ≤ y*c.1
  rw [Real.norm_eq_abs, abs_of_nonpos h.2]
  change -entropy T y Fin.elim0 c.2 ≤ y*c.1
  linarith [h.1]

theorem fixed_mean {n : ℕ} [NeZero n] (y : ℝ) (L : ℕ) :
    GroundComparison.mean T m n y 0 L =
      ∫ s : Fin L → Fresh m n p, configEntropy T y ⟨L,s⟩ ∂Measure.pi (fun _ => freshLaw T m n) := by
  have he (c : Fin 0 → Fresh m n p) : c = Fin.elim0 := Subsingleton.elim _ _
  simp only [GroundComparison.mean, he, integral_const, measureReal_univ_eq_one, one_smul,
    configEntropy]

theorem endpoint {n : ℕ} [NeZero n] {y α : ℝ} (hy : 0 ≤ y)
    (r : ℝ≥0) (hr : (r : ℝ)/(2*n) = ((m : ℝ)+1)*α/2) (K : ℕ) :
    DirectPoisson.expectation (GroundComparison.mean T m n y) 0 r ≤
      n*(negativeMomentSum K (Criterion.noWarningMoment T m α) + K * Real.exp (-y)) := by
  have hc := DirectPoisson.integrable_row
    (GroundComparison.site_difference_bound T m (n := n) hy) r 0
  change Integrable (fun L => GroundComparison.mean T m n y 0 L) (poissonMeasure r) at hc
  simp_rw [fixed_mean] at hc
  rw [DirectPoisson.expectation, DirectPoisson.zero_law, integral_dirac]
  simp_rw [fixed_mean]
  rw [← PoissonMixture.integral_eq_count_integral r (freshLaw T m n)
    (measurable_configEntropy T n y) (integrable_entropy T (n := n) hy r) hc]
  have hs := integrable_finset_sum Finset.univ (fun (v : Fin n) _ =>
    integrable_upper (m := m) T r K (Real.exp (-y)) v)
  have h := integral_mono (integrable_entropy T (n := n) hy r) hs (fun c => entropy_le T hy c.2 K)
  rw [integral_finset_sum _ (fun v _ => integrable_upper (m := m) T r K (Real.exp (-y)) v)] at h
  simp only [integral_upper T r hr, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    nsmul_eq_mul] at h
  exact h

end KSatUpper.GroundSiteBound
