import KSatUpper.Direct.Finite
import KSatUpper.ProductMeasures
import Mathlib.MeasureTheory.Integral.Prod

/-! Splitting a finite product at its first coordinate, with distinct laws.

Derived from `SatUpper/Direct/Product.lean` (yamelton/sat-upper-4268, Apache-2.0).
The arity-three `triple_law` is replaced by `head_tail_law` for any arity `m+1`. -/

open MeasureTheory
open scoped ENNReal

namespace KSatUpper.DirectProduct

variable {A : Type*} [Fintype A] [MeasurableSpace A] [MeasurableSingletonClass A]

theorem integral_cons {L : ℕ} (ν : Measure A) (μ : Fin L → Measure A)
    [IsProbabilityMeasure ν] [∀ i, IsProbabilityMeasure (μ i)]
    (f : (Fin (L+1) → A) → ℝ) :
    (∫ a, f a ∂Measure.pi (Fin.cons ν μ)) =
      ∫ a, ∫ v, f (Fin.cons v a) ∂ν ∂Measure.pi μ := by
  letI : ∀ i : Fin (L+1), IsProbabilityMeasure ((Fin.cons ν μ : Fin (L+1) → Measure A) i) := by
    intro i
    cases i using Fin.cases with
    | zero => change IsProbabilityMeasure ν; infer_instance
    | succ i => change IsProbabilityMeasure (μ i); infer_instance
  let e := MeasurableEquiv.piFinSuccAbove (fun _ : Fin (L+1) => A) 0
  have h := (measurePreserving_piFinSuccAbove (Fin.cons ν μ) 0).symm e
  have he : (fun z : A × (Fin L → A) => (Fin.cons z.1 z.2 : Fin (L+1) → A)) = e.symm := by
    funext z j
    simp [e, MeasurableEquiv.piFinSuccAbove_symm_apply, Fin.insertNthEquiv]
  have hi := h.integral_comp e.symm.measurableEmbedding f
  simp only [Fin.cons_zero, Fin.succAbove_zero, Fin.cons_succ, ← he] at hi
  rw [← hi, integral_prod _ Integrable.of_finite]
  exact integral_integral_swap Integrable.of_finite

theorem integral_iid_cons (ν : Measure A) [IsProbabilityMeasure ν] (L : ℕ)
    (f : (Fin (L+1) → A) → ℝ) :
    (∫ a, f a ∂Measure.pi (fun _ => ν)) =
      ∫ a, ∫ v, f (Fin.cons v a) ∂ν ∂Measure.pi (fun _ => ν) := by
  have he : (Fin.cons ν (fun _ : Fin L => ν) : Fin (L+1) → Measure A) = fun _ => ν := by
    funext i
    exact Fin.cases rfl (fun _ => rfl) i
  rw [← he, integral_cons]

theorem uniform_eq_count (A : Type*) [Fintype A] [Nonempty A] [MeasurableSpace A]
    [MeasurableSingletonClass A] :
    DirectFinite.uniform A = (Fintype.card A : ℝ≥0∞)⁻¹ • Measure.count := by
  apply Measure.ext_of_singleton
  intro a
  rw [DirectFinite.uniform, PMF.toMeasure_apply_singleton _ _ (measurableSet_singleton a),
    PMF.uniformOfFintype_apply]
  simp [Measure.smul_apply, smul_eq_mul]

/-- The first coordinate and the remaining `m` coordinates are independent. -/
theorem head_tail_law {B : Type*} [MeasurableSpace B] {m : ℕ} (μ : Fin (m + 1) → Measure B)
    [∀ j, IsProbabilityMeasure (μ j)] :
    Measure.map (fun v : Fin (m + 1) → B => (v 0, fun j : Fin m => v j.succ)) (Measure.pi μ) =
      (μ 0).prod (Measure.pi (fun j : Fin m => μ j.succ)) := by
  have h := (measurePreserving_piFinSuccAbove μ 0).map_eq
  have he : (MeasurableEquiv.piFinSuccAbove (fun _ : Fin (m + 1) => B) 0 :
      (Fin (m + 1) → B) → B × (Fin m → B)) = (fun v => (v 0, fun j : Fin m => v j.succ)) := by
    funext v
    simp [MeasurableEquiv.piFinSuccAbove_apply]
    rfl
  rw [he] at h
  simpa only [Fin.succAbove_zero] using h

end KSatUpper.DirectProduct
