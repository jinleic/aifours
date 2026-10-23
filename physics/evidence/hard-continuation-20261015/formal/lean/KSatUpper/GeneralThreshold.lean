import KSatUpper.ModelTransfer

/-! The general-arity threshold theorem conditional on the finite criterion.

For every arity `k = m+1`, every finite trial warning law `T` (rational weights,
rates in `[0,1)`), density `α ≥ 0` and cutoff `cutoff`: if the finite criterion
`Psi_cutoff(T, m, α)` is negative, then `⌊α n⌋` iid uniform legal signed `k`-clauses on
`n` variables are unsatisfiable with probability tending to one.

This is the general-`k` form of the argument formalized for `k = 3` in
yamelton/sat-upper-4268 (`SatUpper/Threshold.lean`). -/

open Filter

namespace KSatUpper

theorem tendsto_zero_of_criterion {p : ℕ} (T : TrialLaw p) (m : ℕ) {α : ℝ} (hα : 0 ≤ α)
    (cutoff : ℕ) (hΨ : Criterion.finiteAnalyticBound T m α cutoff < 0) :
    Tendsto (fun n : ℕ => satisfiabilityProbability (m + 1) n ⌊α*n⌋₊) atTop (nhds 0) :=
  Formalization.upperBound_of_comparison (m + 1) (fun n => ⌊α*n⌋₊) hα
    (fun n => Nat.floor_le (by positivity)) hΨ cutoff
    (ModelTransfer.asymptoticComparison T m hα cutoff)

end KSatUpper
