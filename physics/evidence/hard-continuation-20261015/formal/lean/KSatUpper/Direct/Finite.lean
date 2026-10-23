import KSatUpper.Trial
import Mathlib.Probability.Distributions.Uniform
import Mathlib.Probability.ProbabilityMassFunction.Integrals

/-! Finite sampling laws for arity `m+1`.

Derived from `SatUpper/Direct/Finite.lean` (yamelton/sat-upper-4268, Apache-2.0),
where rows had three seeds and labels were uniform on `Fin 4`. A seed records a
signed variable and a trial label with the weighted label law; each row then
samples `m+1` independent Bernoulli warnings with the labels' rates. -/

open MeasureTheory
open scoped ENNReal

namespace KSatUpper.DirectFinite

abbrev Spin (n : ℕ) := Fin n → Bool
abbrev Seed (n p : ℕ) := (Fin n × Bool) × Fin p
abbrev Fresh (m n p : ℕ) := Fin (m + 1) → Seed n p
abbrev Fields (m L : ℕ) := Fin L → Fin (m + 1) → Bool

noncomputable def uniform (A : Type*) [Fintype A] [Nonempty A] [MeasurableSpace A] : Measure A :=
  (PMF.uniformOfFintype A).toMeasure

instance (A : Type*) [Fintype A] [Nonempty A] [MeasurableSpace A] :
    IsProbabilityMeasure (uniform A) := by unfold uniform; infer_instance

theorem integral_uniform {A : Type*} [Fintype A] [Nonempty A] [MeasurableSpace A]
    [MeasurableSingletonClass A] (f : A → ℝ) :
    (∫ a, f a ∂uniform A) = (∑ a, f a) / Fintype.card A := by
  rw [uniform, PMF.integral_eq_tsum _ _ Integrable.of_finite, tsum_fintype]
  simp only [PMF.uniformOfFintype_apply, ENNReal.toReal_inv, ENNReal.toReal_natCast,
    smul_eq_mul, ← Finset.mul_sum, div_eq_mul_inv]
  ring

variable {p : ℕ} (T : TrialLaw p)

noncomputable def seedLaw (n : ℕ) [NeZero n] : Measure (Seed n p) :=
  (uniform (Fin n × Bool)).prod T.law

instance (n : ℕ) [NeZero n] : IsProbabilityMeasure (seedLaw T n) := by
  unfold seedLaw; infer_instance

noncomputable def freshLaw (m n : ℕ) [NeZero n] : Measure (Fresh m n p) :=
  Measure.pi (fun _ => seedLaw T n)

instance (m n : ℕ) [NeZero n] : IsProbabilityMeasure (freshLaw T m n) := by
  unfold freshLaw; infer_instance

noncomputable def innerLaw {n : ℕ} (x : Seed n p) : Measure Bool := T.stateLaw x.2

instance {n : ℕ} (x : Seed n p) : IsProbabilityMeasure (innerLaw T x) := by
  unfold innerLaw; infer_instance

noncomputable def rowLaw {m n : ℕ} (x : Fresh m n p) : Measure (Fin (m + 1) → Bool) :=
  Measure.pi (fun j => innerLaw T (x j))

instance {m n : ℕ} (x : Fresh m n p) : IsProbabilityMeasure (rowLaw T x) := by
  unfold rowLaw; infer_instance

noncomputable def fieldLaw {m n L : ℕ} (s : Fin L → Fresh m n p) : Measure (Fields m L) :=
  Measure.pi (fun i => rowLaw T (s i))

instance {m n L : ℕ} (s : Fin L → Fresh m n p) : IsProbabilityMeasure (fieldLaw T s) := by
  unfold fieldLaw
  infer_instance

end KSatUpper.DirectFinite
