import Mathlib.Probability.Moments.Variance
import Mathlib.Analysis.Convex.Function
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Nlinarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FunProp

/-!
The bounded-score, diffuse-leverage Huber attempt is a partial result.
This file proves actual scalar Huber inequalities and a stochastic matrix
second-moment bound. It does not assert the full replication conjecture.
-/

open MeasureTheory ProbabilityTheory Filter Finset
open scoped BigOperators ENNReal NNReal Topology

set_option pp.proofs false
set_option maxRecDepth 1024

namespace Replication
noncomputable section

def huber (k r : ℝ) : ℝ :=
  if r < -k then -k * r - k ^ 2 / 2
  else if k < r then k * r - k ^ 2 / 2
  else r ^ 2 / 2

def huberScore (k r : ℝ) : ℝ :=
  if r < -k then -k else if k < r then k else r

theorem huber_dual_lower {k s r : ℝ} (hs : -k ≤ s ∧ s ≤ k) :
    s * r - s ^ 2 / 2 ≤ huber k r := by
  unfold huber
  split_ifs with hleft hright
  · have hprod : 0 ≤ (k + s) * (-r - k) :=
      mul_nonneg (by linarith [hs.1]) (by linarith)
    nlinarith [sq_nonneg (k + s)]
  · have hprod : 0 ≤ (k - s) * (r - k) :=
      mul_nonneg (by linarith [hs.2]) (by linarith)
    nlinarith [sq_nonneg (k - s)]
  · nlinarith [sq_nonneg (r - s)]

theorem huber_score_bounds {k e : ℝ} (hk : 0 ≤ k) :
    -k ≤ huberScore k e ∧ huberScore k e ≤ k := by
  unfold huberScore
  split_ifs <;> constructor <;> linarith

theorem huber_score_dual_eq (k e : ℝ) :
    huber k e = huberScore k e * e - (huberScore k e) ^ 2 / 2 := by
  unfold huber huberScore
  split_ifs <;> ring

theorem huber_support {k e r : ℝ} (hk : 0 ≤ k) :
    huber k e + huberScore k e * (r - e) ≤ huber k r := by
  have h := huber_dual_lower (r := r) (huber_score_bounds (e := e) hk)
  rw [huber_score_dual_eq k e]
  nlinarith

theorem huber_quadratic {k r : ℝ} (hr : |r| ≤ k) :
    huber k r = r ^ 2 / 2 ∧ huberScore k r = r := by
  have hbounds := abs_le.mp hr
  simp [huber, huberScore, not_lt.mpr hbounds.1, not_lt.mpr hbounds.2]

def core (k a e : ℝ) : ℝ := if |e| ≤ k - a then 1 else 0

theorem huber_core_remainder {k a e t : ℝ} (hk : 0 ≤ k)
    (ha : 0 ≤ a) (ht : |t| ≤ a) :
    core k a e * t ^ 2 / 2 ≤
      huber k (e - t) - huber k e + huberScore k e * t := by
  by_cases he : |e| ≤ k - a
  · have he' : |e| ≤ k := by linarith
    have het : |e - t| ≤ k :=
      (abs_sub e t).trans (by linarith)
    rw [core, if_pos he, (huber_quadratic het).1,
      (huber_quadratic he').1, (huber_quadratic he').2]
    nlinarith
  · have h := huber_support (e := e) (r := e - t) hk
    rw [core, if_neg he]
    nlinarith

section Moments
variable {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]

theorem binary_variance {B : Ω → ℝ} (hB : MemLp B 2 μ)
    (hbinary : ∀ᵐ ω ∂μ, B ω = 0 ∨ B ω = 1) {q : ℝ}
    (hmean : ∫ ω, B ω ∂μ = q) :
    variance B μ = q * (1 - q) := by
  have hsq : (fun ω => B ω ^ 2) =ᵐ[μ] B := by
    filter_upwards [hbinary] with ω hω
    rcases hω with hω | hω <;> simp [hω]
  rw [variance_eq_sub hB]
  change (∫ ω, B ω ^ 2 ∂μ) - (∫ ω, B ω ∂μ) ^ 2 = _
  rw [integral_congr_ae hsq, hmean]
  ring

theorem centered_weighted_sum_second_moment {ι : Type*} [Fintype ι]
    (X : ι → Ω → ℝ) (c : ι → ℝ) (hX : ∀ i, MemLp (X i) 2 μ)
    (hind : Pairwise (fun i j => IndepFun (X i) (X j) μ))
    (hzero : ∀ i, ∫ ω, X i ω ∂μ = 0) :
    (∫ ω, (∑ i, c i * X i ω) ^ 2 ∂μ) =
      ∑ i, c i ^ 2 * variance (X i) μ := by
  let Y : ι → Ω → ℝ := fun i ω => c i * X i ω
  have hY : ∀ i, MemLp (Y i) 2 μ := fun i => (hX i).const_mul (c i)
  have hindY : Set.Pairwise (↑(Finset.univ : Finset ι))
      (fun i j => IndepFun (Y i) (Y j) μ) := by
    intro i hi j hj hij
    exact (hind hij).comp (measurable_const.mul measurable_id)
      (measurable_const.mul measurable_id)
  have hsum : MemLp (∑ i, Y i) 2 μ := memLp_finset_sum _ (fun i _ => hY i)
  have hmean : ∫ ω, (∑ i, Y i) ω ∂μ = 0 := by
    rw [integral_finset_sum _ (fun i _ => (hY i).integrable (by norm_num))]
    simp [Y, integral_const_mul, hzero]
  have hv := IndepFun.variance_sum (μ := μ)
    (s := Finset.univ) (fun i _ => hY i) hindY
  rw [variance_eq_sub hsum, hmean, sq, zero_mul, sub_zero] at hv
  simp only [Y, variance_const_mul] at hv
  simpa only [Finset.sum_apply] using hv

end Moments

end
end Replication

#print Replication.huber_dual_lower
#print axioms Replication.huber_dual_lower
#print Replication.huber_score_bounds
#print axioms Replication.huber_score_bounds
#print Replication.huber_score_dual_eq
#print axioms Replication.huber_score_dual_eq
#print Replication.huber_support
#print axioms Replication.huber_support
#print Replication.huber_quadratic
#print axioms Replication.huber_quadratic
#print Replication.huber_core_remainder
#print axioms Replication.huber_core_remainder
#print Replication.binary_variance
#print axioms Replication.binary_variance
#print Replication.centered_weighted_sum_second_moment
#print axioms Replication.centered_weighted_sum_second_moment
