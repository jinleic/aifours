import KSatUpper.Ground.Comparison
import KSatUpper.SiteSideLaw

/-! A conflicting pair of warning sides costs at least one violation.
Independent vertex sides then give the site endpoint bound.

Derived from `SatUpper/Ground/Site.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory KSatUpper.DirectFinite KSatUpper.GroundFinite KSatUpper.SiteVertexIdentity

namespace KSatUpper.GroundSite

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

abbrev Locations (m n L : ℕ) := Fin L → Fin (m + 1) → Fin n × Bool
abbrev Surveys (m L p : ℕ) := (Fin L × Fin (m + 1)) → Fin p

def pack {n L : ℕ} (u : Locations m n L) (q : Surveys m L p) : Fin L → Fresh m n p :=
  fun i j => (u i j, q (i,j))

noncomputable def conflict {ι κ : Type*} [Fintype ι] [Fintype κ]
    (x : (ι → TrialVertex.InnerMark m) × (κ → TrialVertex.InnerMark m)) : ℕ := by
  classical
  exact if x ∈ TrialVertex.goodEvent ι κ m then 0 else 1

noncomputable def localCost {n L : ℕ} (u : Locations m n L) (x : (Fin L × Fin (m + 1)) → Bool)
    (v : Fin n) (b : Bool) : ℕ :=
  ∑ i, if (u i 0).1 = v then
    if b = (u i 0).2 ∧ ∀ j : Fin m, x (i, j.succ) = true then 1 else 0 else 0

theorem cost_eq_sum {n L : ℕ} (u : Locations m n L) (q : Surveys m L p)
    (x : (Fin L × Fin (m + 1)) → Bool) (σ : Spin n) :
    cost Fin.elim0 (pack u q) (Function.curry x) σ = ∑ v, localCost u x v (σ v) := by
  classical
  unfold localCost
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
  simp [cost, pack, Function.curry]

theorem conflict_le {n L : ℕ} (u : Locations m n L) (x : (Fin L × Fin (m + 1)) → Bool)
    (v : Fin n) (b : Bool) :
    conflict (messages u v true x, messages u v false x) ≤ localCost u x v b := by
  classical
  unfold conflict
  split
  · exact Nat.zero_le _
  · rename_i h
    obtain ⟨ht,hf⟩ := TrialVertex.bad_event_warnings h
    have hw : ∃ i : Side u v b, messages u v b x i = TrialVertex.allWarn m := by
      cases b <;> assumption
    obtain ⟨i,hi⟩ := hw
    have hs := Finset.single_le_sum (f := fun i : Fin L =>
      if (u i 0).1 = v then if b = (u i 0).2 ∧ ∀ j : Fin m, x (i, j.succ) = true
        then 1 else 0 else 0) (fun _ _ => Nat.zero_le _) (Finset.mem_univ i.val)
    have hall : ∀ j : Fin m, x (i.val, j.succ) = true := fun j => congrFun hi j
    simpa [localCost, i.property.1, i.property.2, hall] using hs

theorem conflicts_le_energy {n L : ℕ} (u : Locations m n L) (q : Surveys m L p)
    (x : (Fin L × Fin (m + 1)) → Bool) :
    (∑ v, conflict (messages u v true x, messages u v false x)) ≤
      energy Fin.elim0 (pack u q) (Function.curry x) := by
  apply GroundMinimum.le_value
  intro σ
  rw [cost_eq_sum]
  exact Finset.sum_le_sum (fun v _ => conflict_le u x v (σ v))

theorem vertex_moment {ι κ : Type*} [Fintype ι] [Fintype κ]
    (y : ℝ) (a : ι → TrialVertex.Mark m p) (b : κ → TrialVertex.Mark m p) :
    (∫ x, Real.exp (-y * conflict x) ∂TrialVertex.innerLaw T a b) =
      noConflict (∏ i, T.mark (a i)) (∏ i, T.mark (b i)) +
      (1-noConflict (∏ i, T.mark (a i)) (∏ i, T.mark (b i)))*Real.exp (-y) := by
  classical
  have he (x : (ι → TrialVertex.InnerMark m) × (κ → TrialVertex.InnerMark m)) :
      Real.exp (-y * conflict x) = Real.exp (-y) +
        (1-Real.exp (-y)) * (TrialVertex.goodEvent ι κ m).indicator (fun _ => (1 : ℝ)) x := by
    by_cases h : x ∈ TrialVertex.goodEvent ι κ m <;> simp [conflict, h]
  simp_rw [he]
  rw [integral_add (integrable_const _) Integrable.of_finite, integral_const_mul,
    integral_indicator_const _ (TrialVertex.measurable_goodEvent ι κ m),
    integral_const, measureReal_univ_eq_one, one_smul, smul_eq_mul, mul_one,
    TrialVertex.good_event_probability]
  ring

theorem entropy_le {n L : ℕ} {y : ℝ} (hy : 0 ≤ y) (u : Locations m n L) (q : Surveys m L p) :
    entropy T y Fin.elim0 (pack u q) ≤ ∑ v : Fin n,
      Real.log (∫ x, Real.exp (-y * conflict x) ∂TrialVertex.innerLaw T
        (SiteSideLaw.surveys u v true q) (SiteSideLaw.surveys u v false q)) := by
  have hb (x : (Fin L × Fin (m + 1)) → Bool) :
      Real.exp (-y * energy Fin.elim0 (pack u q) (Function.curry x)) ≤
      ∏ v, Real.exp (-y * conflict (messages u v true x, messages u v false x)) := by
    rw [← Real.exp_sum]
    simp only [← Finset.mul_sum, ← Nat.cast_sum]
    exact Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left
      (by exact_mod_cast conflicts_le_energy u q x) (neg_nonpos.mpr hy))
  have he : moment T y Fin.elim0 (pack u q) = ∫ x,
      Real.exp (-y * energy Fin.elim0 (pack u q) (Function.curry x))
        ∂Measure.pi (fun r => T.stateLaw (q r)) := by
    rw [← ProductMeasures.uncurry (fun i j => T.stateLaw (q (i,j))),
      integral_map (measurable_of_countable _).aemeasurable
        (measurable_of_countable _).aestronglyMeasurable]
    rfl
  have h := integral_mono (μ := Measure.pi (fun r => T.stateLaw (q r)))
    Integrable.of_finite Integrable.of_finite hb
  rw [← he] at h
  have hf : (∫ x : (Fin L × Fin (m + 1)) → Bool,
      ∏ v, Real.exp (-y * conflict (messages u v true x, messages u v false x))
        ∂Measure.pi (fun r => T.stateLaw (q r))) =
      ∏ v, ∫ x, Real.exp (-y * conflict x) ∂TrialVertex.innerLaw T
        (SiteSideLaw.surveys u v true q) (SiteSideLaw.surveys u v false q) := by
    rw [← integral_fintype_prod_eq_prod, ← SiteSideLaw.joint_law T u q,
      integral_map (measurable_of_countable _).aemeasurable
        (measurable_of_countable _).aestronglyMeasurable]
  rw [hf] at h
  have hl := Real.log_le_log (moment_pos T y Fin.elim0 (pack u q)) h
  rwa [Real.log_prod _ _ (fun v _ => (integral_exp_pos (μ := TrialVertex.innerLaw T
    (SiteSideLaw.surveys u v true q) (SiteSideLaw.surveys u v false q))
      Integrable.of_finite).ne')] at hl

end KSatUpper.GroundSite
