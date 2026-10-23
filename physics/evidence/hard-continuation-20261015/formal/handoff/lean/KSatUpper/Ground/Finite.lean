import KSatUpper.Direct.Product
import KSatUpper.Ground.Minimum
import KSatUpper.GibbsInsertion
import KSatUpper.LogInsertion

/-! Conditional exponential moments of the integer minimum violation count, arity `m+1`.

Derived from `SatUpper/Ground/Finite.lean` (yamelton/sat-upper-4268, Apache-2.0).
A clause costs one when all `m+1` literals are falsified. A site costs one when
its head literal is falsified and all `m` of its incoming Bernoulli warnings are
active. The upstream fractional-moment bridge remark is not needed here and is
omitted. -/

open MeasureTheory KSatUpper.DirectFinite

namespace KSatUpper.GroundFinite

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

noncomputable def cost {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (a : Fields m L) (σ : Spin n) : ℕ :=
  (∑ i, if ∀ j, σ (c i j).1.1 = (c i j).1.2 then 1 else 0) +
    ∑ i, if σ (s i 0).1.1 = (s i 0).1.2 ∧ ∀ j : Fin m, a i j.succ = true then 1 else 0

noncomputable def energy {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (a : Fields m L) : ℕ := GroundMinimum.value (cost c s a)

noncomputable def moment {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p)
    (s : Fin L → Fresh m n p) : ℝ :=
  ∫ a, Real.exp (-y * energy c s a) ∂fieldLaw T s

noncomputable def entropy {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p)
    (s : Fin L → Fresh m n p) : ℝ :=
  Real.log (moment T y c s)

theorem moment_pos {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
    0 < moment T y c s := integral_exp_pos Integrable.of_finite

theorem energy_le {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (a : Fields m L) : energy c s a ≤ K + L := by
  refine (GroundMinimum.value_le _ (fun _ => false)).trans ?_
  have h (P : Prop) [Decidable P] : (if P then 1 else 0 : ℕ) ≤ 1 := by split <;> omega
  have h₁ := Finset.sum_le_sum (s := Finset.univ)
    (fun i _ => h (∀ j, (fun _ => false) (c i j).1.1 = (c i j).1.2))
  have h₂ := Finset.sum_le_sum (s := Finset.univ)
    (fun i _ => h ((fun _ => false) (s i 0).1.1 = (s i 0).1.2 ∧ ∀ j : Fin m, a i j.succ = true))
  simpa [cost] using Nat.add_le_add h₁ h₂

theorem entropy_bounds {n K L : ℕ} {y : ℝ} (hy : 0 ≤ y)
    (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
    -y*(K+L) ≤ entropy T y c s ∧ entropy T y c s ≤ 0 := by
  have hl : Real.exp (-y*(K+L)) ≤ moment T y c s := by
    have hb (a : Fields m L) : (energy c s a : ℝ) ≤ K+L := by
      exact_mod_cast energy_le c s a
    simpa [moment] using integral_mono (μ := fieldLaw T s)
      (integrable_const (Real.exp (-y*(K+L))))
      Integrable.of_finite (fun a => Real.exp_le_exp.mpr
        (mul_le_mul_of_nonpos_left (hb a) (neg_nonpos.mpr hy)))
  have hu : moment T y c s ≤ 1 := by
    simpa [moment] using integral_mono (μ := fieldLaw T s) Integrable.of_finite
      (integrable_const (1 : ℝ))
      (fun a => Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg
        (neg_nonpos.mpr hy) (Nat.cast_nonneg (energy c s a))))
  exact ⟨by simpa [entropy] using Real.log_le_log (Real.exp_pos _) hl,
    Real.log_nonpos (moment_pos T y c s).le hu⟩

noncomputable def tilted {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p)
    (s : Fin L → Fresh m n p) : Measure (Fields m L) :=
  (fieldLaw T s).tilted (fun a => -y * energy c s a)

instance {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
    IsProbabilityMeasure (tilted T y c s) := isProbabilityMeasure_tilted Integrable.of_finite

/-- One exactly when the literal is falsified by every minimizer. -/
noncomputable def backbone {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (x : Seed n p) (a : Fields m L) : ℝ :=
  if ∀ σ, cost c s a σ = energy c s a → σ x.1.1 = x.1.2 then 1 else 0

noncomputable def rate {n L : ℕ} (x : Seed n p) (_ : Fields m L) : ℝ := T.rate x.2

theorem backbone_bounds {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (x : Seed n p) (a : Fields m L) : 0 ≤ backbone c s x a ∧ backbone c s x a ≤ 1 := by
  unfold backbone
  split <;> norm_num

theorem rate_bounds {n L : ℕ} (x : Seed n p) (a : Fields m L) :
    0 ≤ rate T x a ∧ rate T x a ≤ 1 :=
  ⟨(T.rate_bounds x.2).1, (T.rate_bounds x.2).2.le⟩

theorem log_factor_bounds {y z : ℝ} (hy : 0 ≤ y) (hz0 : 0 ≤ z) (hz1 : z ≤ 1) :
    -y ≤ Real.log (1-(1-Real.exp (-y))*z) ∧ Real.log (1-(1-Real.exp (-y))*z) ≤ 0 := by
  have hb := factor_bounds (Real.exp_le_one_iff.mpr (neg_nonpos.mpr hy)) hz0 hz1
  exact ⟨by simpa using Real.log_le_log (Real.exp_pos _) hb.1,
    Real.log_nonpos ((Real.exp_pos _).le.trans hb.1) hb.2⟩

end KSatUpper.GroundFinite
