import KSatUpper.FiniteCoordinateSelection

/-! The `m` used cavity coordinates at each site have the trial message law.

Derived from `SatUpper/SiteMessageLaw.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory

namespace KSatUpper.SiteMessageLaw

variable {p : ℕ} (T : TrialLaw p) {L m : ℕ}

def coordinate (j : Fin L × Fin m) : Fin L × Fin (m + 1) := (j.1, j.2.succ)

theorem coordinate_injective : Function.Injective (coordinate (L := L) (m := m)) := by
  intro a b h
  have h1 := congrArg Prod.fst h
  have h2 := congrArg Prod.snd h
  exact Prod.ext h1 (Fin.succ_injective _ h2)

theorem message_arrays_law (q : (Fin L × Fin (m + 1)) → Fin p) :
    Measure.map (fun x : (Fin L × Fin (m + 1)) → Bool => fun i (j : Fin m) => x (i, j.succ))
      (Measure.pi (fun j => T.stateLaw (q j))) =
      Measure.pi (fun i => TrialVertex.messageLaw T (fun j => q (i, j.succ))) := by
  have hs := FiniteCoordinateSelection.select_law (fun j => T.stateLaw (q j))
    coordinate coordinate_injective
  have hc := FiniteCoordinateSelection.curry_law
    (fun (i : Fin L) (j : Fin m) => T.stateLaw (q (coordinate (i, j))))
  rw [← hs, Measure.map_map (by fun_prop) (by fun_prop)] at hc
  exact hc

end KSatUpper.SiteMessageLaw
