import KSatUpper.Trial
import KSatUpper.Local
import Mathlib.MeasureTheory.Constructions.Pi

/-! Conditional no-warning and no-conflict events under the actual finite trial laws.

Derived from `SatUpper/TrialFields.lean` and `SatUpper/TrialVertex.lean`
(yamelton/sat-upper-4268, Apache-2.0). A site's inner mark is now the vector of
its `m` incoming Bernoulli warnings, instead of a pair. -/

open MeasureTheory

namespace KSatUpper.TrialVertex

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

/-- The `m` incoming warnings of one site; `true` is an active warning. -/
abbrev InnerMark (m : ℕ) := Fin m → Bool

/-- The survey labels of one site's `m` incoming warnings. -/
abbrev Mark (m p : ℕ) := Fin m → Fin p

def allWarn (m : ℕ) : InnerMark m := fun _ => true

noncomputable def messageLaw (a : Mark m p) : Measure (InnerMark m) :=
  Measure.pi (fun j => T.stateLaw (a j))

instance (a : Mark m p) : IsProbabilityMeasure (messageLaw T a) := by
  unfold messageLaw
  infer_instance

theorem messageLaw_hard (a : Mark m p) :
    (messageLaw T a).real {allWarn m} = ∏ j, (T.rate (a j) : ℝ) := by
  have he : ({allWarn m} : Set (InnerMark m)) = Set.univ.pi (fun _ => {true}) := by
    ext x
    simp only [Set.mem_singleton_iff, Set.mem_pi, Set.mem_univ, forall_true_left]
    exact funext_iff
  rw [measureReal_def, messageLaw, he, Measure.pi_pi, ENNReal.toReal_prod]
  exact Finset.prod_congr rfl (fun j _ => by rw [← measureReal_def]; exact T.stateLaw_hard (a j))

theorem messageLaw_noWarning (a : Mark m p) :
    (messageLaw T a).real ({allWarn m}ᶜ) = T.mark a := by
  rw [measureReal_compl (measurableSet_singleton _), messageLaw_hard]
  simp [TrialLaw.mark]

variable {ι κ : Type*} [Fintype ι] [Fintype κ]

noncomputable def sideLaw (a : ι → Mark m p) : Measure (ι → InnerMark m) :=
  Measure.pi (fun i => messageLaw T (a i))

instance (a : ι → Mark m p) : IsProbabilityMeasure (sideLaw T a) := by
  unfold sideLaw
  infer_instance

def noWarning (ι : Type*) (m : ℕ) : Set (ι → InnerMark m) :=
  Set.univ.pi (fun _ => {allWarn m}ᶜ)

theorem measurable_noWarning (ι : Type*) [Fintype ι] (m : ℕ) : MeasurableSet (noWarning ι m) :=
  (Set.to_countable _).measurableSet

theorem noWarning_probability (a : ι → Mark m p) :
    (sideLaw T a).real (noWarning ι m) = ∏ i, T.mark (a i) := by
  rw [measureReal_def, sideLaw, noWarning, Measure.pi_pi, ENNReal.toReal_prod]
  exact Finset.prod_congr rfl (fun i _ => by
    rw [← measureReal_def]; exact messageLaw_noWarning T (a i))

noncomputable def innerLaw (a : ι → Mark m p) (b : κ → Mark m p) :
    Measure ((ι → InnerMark m) × (κ → InnerMark m)) :=
  (sideLaw T a).prod (sideLaw T b)

instance (a : ι → Mark m p) (b : κ → Mark m p) :
    IsProbabilityMeasure (innerLaw T a b) := by
  unfold innerLaw
  infer_instance

def goodEvent (ι κ : Type*) (m : ℕ) : Set ((ι → InnerMark m) × (κ → InnerMark m)) :=
  ((noWarning ι m)ᶜ ×ˢ (noWarning κ m)ᶜ)ᶜ

theorem measurable_goodEvent (ι κ : Type*) [Fintype ι] [Fintype κ] (m : ℕ) :
    MeasurableSet (goodEvent ι κ m) :=
  ((measurable_noWarning ι m).compl.prod (measurable_noWarning κ m).compl).compl

theorem bad_event_probability (a : ι → Mark m p) (b : κ → Mark m p) :
    (innerLaw T a b).real ((noWarning ι m)ᶜ ×ˢ (noWarning κ m)ᶜ) =
      (1-∏ i, T.mark (a i))*(1-∏ i, T.mark (b i)) := by
  rw [measureReal_def, innerLaw, Measure.prod_prod, ENNReal.toReal_mul]
  change (sideLaw T a).real ((noWarning ι m)ᶜ) * (sideLaw T b).real ((noWarning κ m)ᶜ) = _
  rw [measureReal_compl (measurable_noWarning ι m), measureReal_compl (measurable_noWarning κ m),
    noWarning_probability, noWarning_probability]
  simp

theorem good_event_probability (a : ι → Mark m p) (b : κ → Mark m p) :
    (innerLaw T a b).real (goodEvent ι κ m) =
      noConflict (∏ i, T.mark (a i)) (∏ i, T.mark (b i)) := by
  rw [goodEvent, measureReal_compl
    ((measurable_noWarning ι m).compl.prod (measurable_noWarning κ m).compl),
    bad_event_probability, noConflict_complement]
  simp

omit [Fintype ι] [Fintype κ] in
theorem bad_event_warnings {x : (ι → InnerMark m) × (κ → InnerMark m)}
    (hx : x ∉ goodEvent ι κ m) : (∃ i, x.1 i = allWarn m) ∧ (∃ j, x.2 j = allWarn m) := by
  classical
  simpa [goodEvent, noWarning, Set.mem_pi] using hx

end KSatUpper.TrialVertex
