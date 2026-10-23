import KSatUpper.InterpolationLaw

/-! Uniform `k`-clauses sampled with replacement (repeated variables allowed).

Derived from `SatUpper/ClauseEndpoint.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open MeasureTheory

namespace KSatUpper.ClauseEndpoint

abbrev Clause (k n : ℕ) := Fin k → Fin n × Bool

noncomputable def clauseLaw (k n : ℕ) : Measure (Clause k n) :=
  Measure.pi (fun _ : Fin k => InterpolationLaw.signedVariableLaw n)

end KSatUpper.ClauseEndpoint
