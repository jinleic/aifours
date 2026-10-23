import Mathlib.Probability.ProbabilityMassFunction.Constructions
import Mathlib.Probability.ProbabilityMassFunction.Integrals
import Mathlib.MeasureTheory.Integral.Pi
import KSatUpper.TrialSpec
import KSatUpper.CompoundPoissonMoments

/-! Measure-theoretic facts about finite trial warning laws (`KSatUpper.TrialSpec`).

Every expectation used by the criterion is an integral against the actual product law; the
rational moment formulas of `TrialSpec` are proved equal to those integrals here. -/

open MeasureTheory
open scoped ENNReal

namespace KSatUpper

namespace TrialLaw

variable {p : ℕ} (T : TrialLaw p)

theorem rate_bounds (i : Fin p) : 0 ≤ (T.rate i : ℝ) ∧ (T.rate i : ℝ) < 1 :=
  ⟨by exact_mod_cast T.rate_nonneg i, by exact_mod_cast T.rate_lt_one i⟩

theorem integral_law (f : Fin p → ℝ) : (∫ i, f i ∂T.law) = ∑ i, (T.weight i : ℝ) * f i := by
  rw [law, PMF.integral_eq_sum]
  apply Finset.sum_congr rfl
  intro i _
  simp [pmf, PMF.ofFintype_apply, ENNReal.toReal_ofReal (T.weight_nonneg_real i)]

/-- Bernoulli warning with the label's rate; `true` means a warning. -/
noncomputable def stateLaw (i : Fin p) : Measure Bool :=
  (PMF.bernoulli ⟨(T.rate i : ℝ), (T.rate_bounds i).1⟩
    (by change (T.rate i : ℝ) ≤ 1; exact (T.rate_bounds i).2.le)).toMeasure

instance (i : Fin p) : IsProbabilityMeasure (T.stateLaw i) := by
  unfold stateLaw
  infer_instance

theorem stateLaw_hard (i : Fin p) : (T.stateLaw i).real {true} = (T.rate i : ℝ) := by
  rw [measureReal_def, stateLaw, PMF.toMeasure_apply_singleton _ _ (measurableSet_singleton _)]
  simp

theorem integral_warning (i : Fin p) :
    (∫ b : Bool, (if b = true then 1 else 0 : ℝ) ∂T.stateLaw i) = (T.rate i : ℝ) := by
  have h := integral_indicator_const (1 : ℝ) (measurableSet_singleton true)
    (μ := T.stateLaw i)
  simpa [Set.indicator, T.stateLaw_hard] using h

theorem integral_rate_pow (h : ℕ) : (∫ i, (T.rate i : ℝ) ^ h ∂T.law) = (T.moment h : ℝ) := by
  rw [integral_law]
  simp [moment]

/-- `E (∏_{j<r} R_j)^h = C_h^r` for `r` independent labels. -/
theorem integral_prod_rate_pow (r h : ℕ) :
    (∫ a : Fin r → Fin p, (∏ j, (T.rate (a j) : ℝ)) ^ h ∂Measure.pi (fun _ => T.law)) =
      (T.moment h : ℝ) ^ r := by
  simp_rw [← Finset.prod_pow]
  rw [integral_fintype_prod_eq_pow (fun i => (T.rate i : ℝ) ^ h), integral_rate_pow,
    Fintype.card_fin]

/-- The no-warning probability of a site's `m` incoming warnings: `1 - ∏ R_j`. -/
noncomputable def mark {m : ℕ} (a : Fin m → Fin p) : ℝ := 1 - ∏ j, (T.rate (a j) : ℝ)

theorem prod_rate_bounds {m : ℕ} (a : Fin m → Fin p) :
    0 ≤ ∏ j, (T.rate (a j) : ℝ) ∧ ∏ j, (T.rate (a j) : ℝ) ≤ 1 :=
  ⟨Finset.prod_nonneg (fun j _ => (T.rate_bounds (a j)).1),
    Finset.prod_le_one (fun j _ => (T.rate_bounds (a j)).1) (fun j _ => (T.rate_bounds (a j)).2.le)⟩

theorem mark_bounds {m : ℕ} (a : Fin m → Fin p) : 0 ≤ T.mark a ∧ T.mark a ≤ 1 := by
  have h := T.prod_rate_bounds a
  unfold mark
  constructor <;> linarith [h.1, h.2]

theorem binom_eq_choose {j t : ℕ} (h : t ≤ j) : binom j t = Nat.choose j t :=
  (Nat.choose_eq_factorial_div_factorial h).symm

theorem integral_mark_pow (m j : ℕ) :
    (∫ a : Fin m → Fin p, T.mark a ^ j ∂Measure.pi (fun _ => T.law)) = (T.markMoment m j : ℝ) := by
  simp_rw [mark, CompoundPoissonMoments.complement_pow_expansion]
  rw [integral_finset_sum _ (fun t _ => Integrable.of_finite)]
  simp_rw [integral_const_mul, integral_prod_rate_pow]
  unfold markMoment
  push_cast
  apply Finset.sum_congr rfl
  intro t ht
  rw [binom_eq_choose (Nat.le_of_lt_succ (Finset.mem_range.mp ht))]

theorem markMoment_le_one (m j : ℕ) : T.markMoment m j ≤ 1 := by
  have hle : (∫ a : Fin m → Fin p, T.mark a ^ j ∂Measure.pi (fun _ => T.law)) ≤ 1 := by
    have h := integral_mono (μ := Measure.pi (fun _ : Fin m => T.law)) Integrable.of_finite
      (integrable_const (1 : ℝ)) (fun a => pow_le_one₀ (n := j) (T.mark_bounds a).1 (T.mark_bounds a).2)
    simpa using h
  rw [integral_mark_pow] at hle
  exact_mod_cast hle

/-- The product of `r` warning rates is at most `u^r` when every rate is at most `u`. -/
theorem prod_rate_le {u : ℚ} (hu : ∀ i, T.rate i ≤ u) {r : ℕ} (a : Fin r → Fin p) :
    ∏ j, (T.rate (a j) : ℝ) ≤ (u : ℝ) ^ r := by
  have h := Finset.prod_le_prod (s := Finset.univ) (fun j _ => (T.rate_bounds (a j)).1)
    (fun j _ => (show (T.rate (a j) : ℝ) ≤ u by exact_mod_cast hu (a j)))
  simpa [Finset.prod_const, Finset.card_univ, Fintype.card_fin] using h

end TrialLaw

end KSatUpper
