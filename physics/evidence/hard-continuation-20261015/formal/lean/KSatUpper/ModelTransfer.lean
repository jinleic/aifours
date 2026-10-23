import KSatUpper.ReplacementAsymptotic
import KSatUpper.Obligations

/-! Transfer the Poisson comparison to the fixed clause count `⌊α n⌋`.
Distinct variables are handled by `LegalConditioning` at the probability level.

Derived from `SatUpper/ModelTransfer.lean` (yamelton/sat-upper-4268, Apache-2.0). -/

open Filter
open scoped Topology

namespace KSatUpper.ModelTransfer

theorem asymptoticComparison {p : ℕ} (T : TrialLaw p) (m : ℕ) {α : ℝ} (hα : 0 ≤ α)
    (cutoff : ℕ) :
    Formalization.AsymptoticComparison (m + 1) (fun n => ⌊α*n⌋₊)
      (Criterion.finiteAnalyticBound T m α cutoff) cutoff := by
  intro y hy δ hδ
  have ht := (ReplacementAsymptotic.countError_tendsto hα).const_mul y
  simp only [mul_zero] at ht
  filter_upwards [ht.eventually_le_const hδ, eventually_ge_atTop 1] with n he hn
  letI : NeZero n := ⟨by omega⟩
  have h := ReplacementPoissonMean.scaled_fixed_floor_le T m n hα hy.le cutoff
  change y*(Real.sqrt (α*n+1)/n) ≤ δ at he
  linarith

end KSatUpper.ModelTransfer
