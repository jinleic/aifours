import KSatUpper.SiteVertexIdentity
import KSatUpper.ProductMeasures
import Mathlib.Probability.Independence.InfinitePi

/-! Selecting distinct coordinates preserves their possibly different finite laws.

Derived from `SatUpper/FiniteCoordinateSelection.lean` (yamelton/sat-upper-4268,
Apache-2.0). The arity-two `pair_law` is replaced by `curry_law` for any index type. -/

open MeasureTheory ProbabilityTheory

namespace KSatUpper.FiniteCoordinateSelection

variable {I J B : Type*} [Fintype I] [Fintype J] [MeasurableSpace B]

theorem select_law (μ : J → Measure B) [∀ j, IsProbabilityMeasure (μ j)]
    (f : I → J) (hf : Function.Injective f) :
    Measure.map (fun a : J → B => fun i => a (f i)) (Measure.pi μ) =
      Measure.pi (fun i => μ (f i)) := by
  have h := iIndepFun_infinitePi (μ := μ) (X := fun _ => (id : B → B))
    (fun _ => measurable_id)
  have hi := iIndepFun.precomp hf h
  have he := (iIndepFun_iff_map_fun_eq_infinitePi_map
    (fun i => measurable_pi_apply (f i))).mp hi
  have heval (j : J) : Measure.map (fun a : J → B => a j) (Measure.pi μ) = μ j :=
    (measurePreserving_eval μ j).map_eq
  simp only [heval, Measure.infinitePi_eq_pi] at he
  exact he

/-- Currying a product indexed by pairs preserves the product law. -/
theorem curry_law {K : Type*} [Fintype K] (μ : I → K → Measure B)
    [∀ i k, IsProbabilityMeasure (μ i k)] :
    Measure.map (fun a : I × K → B => fun i k => a (i, k))
      (Measure.pi (fun q : I × K => μ q.1 q.2)) =
      Measure.pi (fun i => Measure.pi (μ i)) := by
  rw [← ProductMeasures.uncurry μ, Measure.map_map (by fun_prop) (by fun_prop)]
  have he : ((fun a : I × K → B => fun i k => a (i, k)) ∘
      (fun a : I → K → B => fun q : I × K => a q.1 q.2)) = id := by
    funext a
    rfl
  rw [he, Measure.map_id]

end KSatUpper.FiniteCoordinateSelection
