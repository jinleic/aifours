import KSatChallenge.TrialSpec
import KSatChallenge.Series
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Constructions.Pi

/-! The finite criterion `Psi_T` of the written proof, for arity `m+1`.

For a trial law with warning rates `R`, put `λ = (m+1) α / 2`,
`ν_j = E (1 - R_1 ⋯ R_m)^j`, `M_j = exp(λ (ν_j - 1))`,
`μ_k = Σ_{j ≤ k} (-1)^j C(k,j) M_j` and `d_∞ = E log(1 - R_1 ⋯ R_{m+1})`. Then
`Psi_T = -Σ_{k=1}^T μ_k^2 / k - m α d_∞`.

This generalizes `Formalization.finiteAnalyticBound` of `SatUpper/Obligations.lean`
(yamelton/sat-upper-4268, Apache-2.0), which is the case `m = 2` with four equally
likely labels. Every expectation is the exact expectation under the trial law. -/

open MeasureTheory

namespace KSatUpper.Criterion

variable {p : ℕ} (T : TrialLaw p) (m : ℕ) (α : ℝ)

noncomputable def poissonProductMoment (j : ℕ) : ℝ :=
  Real.exp ((((m : ℝ) + 1) * α / 2) * ((T.markMoment m j : ℝ) - 1))

noncomputable def noWarningMoment (k : ℕ) : ℝ :=
  ∑ j ∈ Finset.range (k + 1), (-1 : ℝ) ^ j * (Nat.choose k j : ℝ) * poissonProductMoment T m α j

noncomputable def edgeExpectation : ℝ :=
  ∫ t : Fin (m + 1) → Fin p, Real.log (1 - ∏ j, (T.rate (t j) : ℝ)) ∂Measure.pi (fun _ => T.law)

noncomputable def edgeCorrection : ℝ := -(m : ℝ) * α * edgeExpectation T m

/-- `Psi_T`. -/
noncomputable def finiteAnalyticBound (cutoff : ℕ) : ℝ :=
  negativeMomentSum cutoff (noWarningMoment T m α) + edgeCorrection T m α

end KSatUpper.Criterion
