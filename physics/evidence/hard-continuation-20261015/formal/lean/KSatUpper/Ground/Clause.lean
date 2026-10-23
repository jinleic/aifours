import KSatUpper.Ground.Comparison
import KSatUpper.FiniteUniformLaw
import KSatUpper.Ground.Formula

/-! At the clause-only endpoint, ground entropy is exactly minus the mean energy.

Derived from `SatUpper/Ground/Clause.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory KSatUpper.DirectFinite KSatUpper.GroundFinite

namespace KSatUpper.GroundClause

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

instance (k n : ℕ) [NeZero n] : IsProbabilityMeasure (ClauseEndpoint.clauseLaw k n) := by
  unfold ClauseEndpoint.clauseLaw
  infer_instance

theorem forget_law (m n : ℕ) [NeZero n] :
    Measure.map (fun x : Fresh m n p => fun j => (x j).1) (freshLaw T m n) =
      ClauseEndpoint.clauseLaw (m + 1) n := by
  unfold freshLaw
  rw [Measure.pi_map_pi (fun _ => measurable_fst.aemeasurable)]
  simp only [seedLaw, Measure.map_fst_prod, measure_univ, one_smul]
  simp_rw [DirectProduct.uniform_eq_count]
  rfl

theorem entropy_eq {n K : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) :
    entropy T y c Fin.elim0 = -y * energy c Fin.elim0 (Fin.elim0 : Fields m 0) := by
  have he (a : Fields m 0) : a = Fin.elim0 := Subsingleton.elim _ _
  simp only [GroundFinite.entropy, GroundFinite.moment, he, integral_const,
    measureReal_univ_eq_one, one_smul, Real.log_exp]

theorem energy_eq {n K : ℕ} (c : Fin K → Fresh m n p) :
    energy c Fin.elim0 (Fin.elim0 : Fields m 0) = GroundFormula.energy (fun i j => (c i j).1) := by
  unfold energy GroundFormula.energy
  congr 1

theorem fixed_mean {n K : ℕ} [NeZero n] (y : ℝ) :
    GroundComparison.mean T m n y K 0 = -y * GroundFormula.mean (m + 1) n K := by
  have hp := Measure.pi_map_pi (μ := fun _ : Fin K => freshLaw T m n)
    (f := fun _ => fun x : Fresh m n p => fun j => (x j).1)
    (fun _ => (measurable_of_countable _).aemeasurable)
  simp only [forget_law T m n] at hp
  unfold GroundFormula.mean
  rw [← FiniteUniformLaw.clause_family_integral (m + 1) n K, ← hp,
    integral_map (measurable_of_countable _).aemeasurable
      (measurable_of_countable _).aestronglyMeasurable]
  have he (s : Fin 0 → Fresh m n p) : s = Fin.elim0 := Subsingleton.elim _ _
  simp only [GroundComparison.mean, he, integral_const, measureReal_univ_eq_one, one_smul,
    entropy_eq, energy_eq, integral_const_mul]

end KSatUpper.GroundClause
