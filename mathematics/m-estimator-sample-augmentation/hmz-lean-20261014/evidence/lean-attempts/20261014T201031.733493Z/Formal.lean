import Mathlib.Probability.Moments.Variance
import Mathlib.Analysis.Convex.Function
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
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

def rippleLoss (eta r : ℝ) : ℝ :=
  r ^ 2 / 2 + (eta / Real.pi) * (1 - Real.cos (Real.pi * r))

def rippleScore (eta r : ℝ) : ℝ := r + eta * Real.sin (Real.pi * r)

def rippleProfile (eta u v : ℝ) : ℝ :=
  4 * rippleLoss eta (u + v) + rippleLoss eta (2 * (u - v))

def rippleProfileScore (eta u v : ℝ) : ℝ :=
  4 * rippleScore eta (u + v) - 2 * rippleScore eta (2 * (u - v))

theorem ripple_loss_derivative (eta r : ℝ) :
    HasDerivAt (rippleLoss eta) (rippleScore eta r) r := by
  have hc := ((hasDerivAt_id r).const_mul Real.pi).cos
  have hq := ((hasDerivAt_id r).pow 2).div_const 2
  have hh := ((hasDerivAt_const r (1 : ℝ)).sub hc).const_mul (eta / Real.pi)
  convert hq.add hh using 1
  · rfl
  · dsimp [rippleScore]
    field_simp [Real.pi_ne_zero]
    ring

theorem ripple_score_derivative (eta r : ℝ) :
    HasDerivAt (rippleScore eta)
      (1 + eta * Real.pi * Real.cos (Real.pi * r)) r := by
  have hs := (((hasDerivAt_id r).const_mul Real.pi).sin).const_mul eta
  convert (hasDerivAt_id r).add hs using 1
  · funext x
    rfl
  · simp only [id_eq, mul_one]
    ring

theorem ripple_curvature_bounds (r : ℝ) :
    (3 / 4 : ℝ) ≤ 1 + (1 / (4 * Real.pi)) * Real.pi * Real.cos (Real.pi * r) ∧
    1 + (1 / (4 * Real.pi)) * Real.pi * Real.cos (Real.pi * r) ≤ (5 / 4 : ℝ) := by
  have hcoef : (1 / (4 * Real.pi) : ℝ) * Real.pi = 1 / 4 := by
    field_simp [Real.pi_ne_zero]
  rw [hcoef]
  constructor <;> nlinarith [Real.neg_one_le_cos (Real.pi * r), Real.cos_le_one (Real.pi * r)]

theorem ripple_profile_derivative (eta u v : ℝ) :
    HasDerivAt (rippleProfile eta u) (rippleProfileScore eta u v) v := by
  have hplus : HasDerivAt (fun w : ℝ => u + w) 1 v := by
    convert (hasDerivAt_const v u).add (hasDerivAt_id v) using 1
    · funext w
      rfl
    · norm_num
  have hminus : HasDerivAt (fun w : ℝ => 2 * (u - w)) (-2) v := by
    simpa using ((hasDerivAt_const v u).sub (hasDerivAt_id v)).const_mul 2
  have hleft := ((ripple_loss_derivative eta (u + v)).comp v hplus).const_mul 4
  have hright := (ripple_loss_derivative eta (2 * (u - v))).comp v hminus
  convert hleft.add hright using 1
  · funext w
    rfl
  · dsimp [rippleProfileScore]
    ring

theorem ripple_even_error_contrast (eta t : ℝ) (k : ℤ) :
    rippleLoss eta (2 * (k : ℝ) - t) - rippleLoss eta (2 * (k : ℝ)) =
      rippleLoss eta t - 2 * (k : ℝ) * t := by
  have harg : Real.pi * (2 * (k : ℝ) - t) =
      (k : ℝ) * (2 * Real.pi) - Real.pi * t := by ring
  have harg0 : Real.pi * (2 * (k : ℝ)) = (k : ℝ) * (2 * Real.pi) := by ring
  unfold rippleLoss
  rw [harg, harg0, Real.cos_int_mul_two_pi_sub, Real.cos_int_mul_two_pi]
  ring

theorem ripple_score_integer (eta : ℝ) (k : ℤ) :
    rippleScore eta k = k := by
  simp [rippleScore, mul_comm Real.pi (k : ℝ), Real.sin_int_mul_pi]

theorem ripple_profile_integer_stationary (eta : ℝ) (k : ℤ) :
    rippleProfileScore eta k 0 = 0 := by
  have htwo := ripple_score_integer eta (2 * k)
  simp only [Int.cast_mul, Int.cast_ofNat] at htwo
  simp only [rippleProfileScore, add_zero, sub_zero]
  rw [ripple_score_integer, htwo]
  ring

theorem ripple_profile_half_score (eta : ℝ) :
    rippleProfileScore eta (1 / 2) 0 = 4 * eta := by
  have hhalf : Real.pi * (1 / 2 : ℝ) = Real.pi / 2 := by ring
  norm_num [rippleProfileScore, rippleScore, hhalf, Real.sin_pi_div_two, Real.sin_pi]
  ring

theorem prefix_variance_ratio {b k : ℝ} (hb : 0 < b) (hk : 0 ≤ k) :
    k / (b + k) ^ 2 ≤ 1 / (4 * b) := by
  have hbk : 0 < (b + k) ^ 2 := sq_pos_of_pos (by linarith)
  apply (div_le_div_iff₀ hbk (by positivity : 0 < 4 * b)).mpr
  nlinarith [sq_nonneg (b - k)]

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
    rw [core, ite_eq_left he, (huber_quadratic het).1,
      (huber_quadratic he').1, (huber_quadratic he').2]
    nlinarith
  · have h := huber_support (e := e) (r := e - t) hk
    rw [core, ite_eq_right he]
    nlinarith

theorem huber_right_tail {k r : ℝ} (hk : 0 ≤ k) (hr : k ≤ r) :
    huber k r = k * r - k ^ 2 / 2 := by
  by_cases hleft : r < -k
  · unfold huber
    rw [ite_eq_left hleft]
    exfalso
    linarith
  · unfold huber
    rw [ite_eq_right hleft]
    by_cases hright : k < r
    · rw [ite_eq_left hright]
    · have heq : r = k := le_antisymm (le_of_not_gt hright) hr
      rw [ite_eq_right hright, heq]
      ring

theorem huber_left_tail {k r : ℝ} (hk : 0 ≤ k) (hr : r ≤ -k) :
    huber k r = -k * r - k ^ 2 / 2 := by
  by_cases hleft : r < -k
  · simp [huber, hleft]
  · have heq : r = -k := le_antisymm hr (le_of_not_gt hleft)
    subst r
    unfold huber
    have hright : ¬k < -k := by linarith
    simp [hright] <;> ring

theorem huber_pair_lower {k e f t : ℝ} (hk : 0 ≤ k) :
    k * (e - f) - k ^ 2 ≤ huber k (e - t) + huber k (f - t) := by
  have hright := huber_dual_lower (r := e - t) (s := k)
    (show -k ≤ k ∧ k ≤ k by constructor <;> linarith)
  have hleft := huber_dual_lower (r := f - t) (s := -k)
    (show -k ≤ -k ∧ -k ≤ k by constructor <;> linarith)
  nlinarith

theorem huber_pair_flat {k a e f t : ℝ} (hk : 0 ≤ k)
    (he : k + a ≤ e) (hf : f ≤ -k - a) (ht : |t| ≤ a) :
    huber k (e - t) + huber k (f - t) = k * (e - f) - k ^ 2 := by
  have htb := abs_le.mp ht
  rw [huber_right_tail hk (by linarith : k ≤ e - t),
    huber_left_tail hk (by linarith : f - t ≤ -k)]
  ring

theorem huber_pair_flat_minimizing {k a e f t : ℝ} (hk : 0 ≤ k)
    (he : k + a ≤ e) (hf : f ≤ -k - a) (ht : |t| ≤ a) :
    ∀ s : ℝ, huber k (e - t) + huber k (f - t) ≤
      huber k (e - s) + huber k (f - s) := by
  intro s
  rw [huber_pair_flat hk he hf ht]
  exact huber_pair_lower hk

theorem convex_minimizer_inside_ball {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℝ E] {f : E → ℝ} {b : E} {R : ℝ}
    (hf : ConvexOn ℝ Set.univ f) (hR : 0 < R)
    (hmin : ∀ x, f b ≤ f x)
    (hboundary : ∀ u, ‖u‖ = R → f 0 < f u) : ‖b‖ < R := by
  by_contra hnot
  have hRb : R ≤ ‖b‖ := le_of_not_gt hnot
  have hbpos : 0 < ‖b‖ := lt_of_lt_of_le hR hRb
  let t : ℝ := R / ‖b‖
  have ht0 : 0 ≤ t := div_nonneg hR.le (norm_nonneg b)
  have ht1 : t ≤ 1 := (div_le_one hbpos).mpr hRb
  have hnorm : ‖t • b‖ = R := by
    rw [norm_smul, Real.norm_of_nonneg ht0]
    exact div_mul_cancel₀ R hbpos.ne.symm
  have hconv := hf.2 (Set.mem_univ (0 : E)) (Set.mem_univ b)
    (sub_nonneg.mpr ht1) ht0 (show (1 - t) + t = 1 by ring)
  simp only [smul_zero, zero_add, smul_eq_mul] at hconv
  have hmin0 := hmin 0
  have hprod : 0 ≤ t * (f 0 - f b) := mul_nonneg ht0 (by linarith)
  have hstrict := hboundary (t • b) hnorm
  nlinarith

theorem integrable_loss_contrast (ν : Measure ℝ) [IsProbabilityMeasure ν]
    (rho : ℝ → ℝ) (L : ℝ≥0) (hLip : LipschitzWith L rho) (t : ℝ) :
    Integrable (fun e => rho (e - t) - rho e) ν := by
  have hm : AEStronglyMeasurable (fun e => rho (e - t) - rho e) ν :=
    ((hLip.continuous.comp (continuous_id.sub continuous_const)).sub
      hLip.continuous).aestronglyMeasurable
  have hbound (e : ℝ) : ‖rho (e - t) - rho e‖ ≤ (L : ℝ) * |t| := by
    have hdist := hLip.dist_le_mul (e - t) e
    have heq : (e - t) - e = -t := by ring
    simpa only [Real.dist_eq, heq, abs_neg, Real.norm_eq_abs] using hdist
  have hlp : MemLp (fun e => rho (e - t) - rho e) 1 ν :=
    MemLp.of_bound hm ((L : ℝ) * |t|) (Eventually.of_forall hbound)
  exact hlp.integrable le_rfl

section Moments
variable {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]

theorem binary_memLp {B : Ω → ℝ} (hm : AEStronglyMeasurable B μ)
    (hbinary : ∀ᵐ ω ∂μ, B ω = 0 ∨ B ω = 1) : MemLp B 2 μ := by
  apply MemLp.of_bound hm 1
  filter_upwards [hbinary] with ω hω
  rcases hω with hω | hω <;> simp [hω]

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
  have hsum : MemLp (∑ i, Y i) 2 μ := by
    simpa using (memLp_finsetSum' Finset.univ (fun i _ => hY i))
  have hmean : ∫ ω, (∑ i, Y i) ω ∂μ = 0 := by
    simp only [Finset.sum_apply]
    rw [integral_finsetSum _ (fun i _ => (hY i).integrable (by norm_num))]
    simp [Y, integral_const_mul, hzero]
  have hv := IndepFun.variance_sum (μ := μ)
    (s := Finset.univ) (fun i _ => hY i) hindY
  rw [variance_eq_sub hsum, hmean, zero_pow (by norm_num : (2 : ℕ) ≠ 0), sub_zero] at hv
  simp only [Y, variance_const_mul] at hv
  simpa only [Pi.pow_apply, Finset.sum_apply] using hv

def rowSq {ι J : Type*} [Fintype J] (z : ι → J → ℝ) (i : ι) : ℝ :=
  ∑ j, z i j ^ 2

def centeredEntry {ι J : Type*} [Fintype ι] (B : ι → Ω → ℝ)
    (z : ι → J → ℝ) (q : ℝ) (ω : Ω) (j k : J) : ℝ :=
  ∑ i, (z i j * z i k) * (B i ω - q)

def frobeniusSq {ι J : Type*} [Fintype ι] [Fintype J]
    (B : ι → Ω → ℝ) (z : ι → J → ℝ) (q : ℝ) (ω : Ω) : ℝ :=
  ∑ j, ∑ k, centeredEntry B z q ω j k ^ 2

theorem bernoulli_frobenius_expectation {ι J : Type*} [Fintype ι] [Fintype J]
    (B : ι → Ω → ℝ) (z : ι → J → ℝ) {q : ℝ}
    (hB : ∀ i, MemLp (B i) 2 μ)
    (hbinary : ∀ i, ∀ᵐ ω ∂μ, B i ω = 0 ∨ B i ω = 1)
    (hind : Pairwise (fun i j => IndepFun (B i) (B j) μ))
    (hmean : ∀ i, ∫ ω, B i ω ∂μ = q) :
    (∫ ω, frobeniusSq B z q ω ∂μ) =
      q * (1 - q) * ∑ i, rowSq z i ^ 2 := by
  let X : ι → Ω → ℝ := fun i ω => B i ω - q
  have hX : ∀ i, MemLp (X i) 2 μ := fun i => (hB i).sub (memLp_const q)
  have hindX : Pairwise (fun i j => IndepFun (X i) (X j) μ) := by
    intro i j hij
    exact (hind hij).comp (measurable_id.sub_const q) (measurable_id.sub_const q)
  have hzero : ∀ i, ∫ ω, X i ω ∂μ = 0 := by
    intro i
    dsimp [X]
    rw [integral_sub ((hB i).integrable (by norm_num)) (integrable_const q),
      hmean i, integral_const]
    simp
  have hvar : ∀ i, variance (X i) μ = q * (1 - q) := by
    intro i
    rw [show variance (X i) μ = variance (B i) μ from
      variance_sub_const (hB i).aestronglyMeasurable q]
    exact binary_variance μ (hB i) (hbinary i) (hmean i)
  have hEntry (j k : J) :
      MemLp (fun ω => centeredEntry B z q ω j k) 2 μ := by
    unfold centeredEntry
    exact memLp_finsetSum Finset.univ (fun i _ => (hX i).const_mul (z i j * z i k))
  have hEntryInt (j k : J) :
      Integrable (fun ω => centeredEntry B z q ω j k ^ 2) μ :=
    (hEntry j k).integrable_sq
  have hEntryMean (j k : J) :
      (∫ ω, centeredEntry B z q ω j k ^ 2 ∂μ) =
        ∑ i, (z i j * z i k) ^ 2 * (q * (1 - q)) := by
    simpa only [centeredEntry, X, hvar] using
      centered_weighted_sum_second_moment μ X (fun i => z i j * z i k)
        hX hindX hzero
  unfold frobeniusSq
  rw [integral_finsetSum Finset.univ (fun j _ =>
    integrable_finsetSum Finset.univ (fun k _ => hEntryInt j k))]
  simp_rw [integral_finsetSum Finset.univ (fun k _ => hEntryInt _ k), hEntryMean]
  calc
    (∑ j, ∑ k, ∑ i, (z i j * z i k) ^ 2 * (q * (1 - q))) =
        ∑ j, ∑ i, ∑ k, (z i j * z i k) ^ 2 * (q * (1 - q)) := by
      apply Finset.sum_congr rfl
      intro j hj
      exact Finset.sum_comm
    _ = ∑ i, ∑ j, ∑ k, (z i j * z i k) ^ 2 * (q * (1 - q)) :=
      Finset.sum_comm
    _ = ∑ i, (rowSq z i ^ 2) * (q * (1 - q)) := by
      apply Finset.sum_congr rfl
      intro i hi
      simp only [mul_pow, ← Finset.sum_mul]
      have hrow : (∑ j, ∑ k, z i j ^ 2 * z i k ^ 2) = rowSq z i ^ 2 := by
        simp_rw [← Finset.mul_sum]
        rw [← Finset.sum_mul]
        change rowSq z i * rowSq z i = rowSq z i ^ 2
        ring
      rw [hrow]
    _ = q * (1 - q) * ∑ i, rowSq z i ^ 2 := by
      rw [← Finset.sum_mul]
      ring

theorem rowSq_nonneg {ι J : Type*} [Fintype J] (z : ι → J → ℝ) (i : ι) :
    0 ≤ rowSq z i := Finset.sum_nonneg (fun j _ => sq_nonneg (z i j))

theorem frobenius_integrable {ι J : Type*} [Fintype ι] [Fintype J]
    (B : ι → Ω → ℝ) (z : ι → J → ℝ) (q : ℝ)
    (hB : ∀ i, MemLp (B i) 2 μ) : Integrable (frobeniusSq B z q) μ := by
  unfold frobeniusSq
  apply integrable_finsetSum Finset.univ
  intro j hj
  apply integrable_finsetSum Finset.univ
  intro k hk
  have hentry : MemLp (fun ω => centeredEntry B z q ω j k) 2 μ := by
    unfold centeredEntry
    exact memLp_finsetSum Finset.univ (fun i _ =>
      ((hB i).sub (memLp_const q)).const_mul (z i j * z i k))
  exact hentry.integrable_sq

theorem bernoulli_frobenius_expectation_le {ι J : Type*} [Fintype ι] [Fintype J]
    (B : ι → Ω → ℝ) (z : ι → J → ℝ) {q d : ℝ}
    (hq : 0 ≤ q ∧ q ≤ 1)
    (hB : ∀ i, MemLp (B i) 2 μ)
    (hbinary : ∀ i, ∀ᵐ ω ∂μ, B i ω = 0 ∨ B i ω = 1)
    (hind : Pairwise (fun i j => IndepFun (B i) (B j) μ))
    (hmean : ∀ i, ∫ ω, B i ω ∂μ = q)
    (htrace : ∑ i, rowSq z i = (Fintype.card J : ℝ))
    (hleverage : ∀ i, rowSq z i ≤ d) :
    (∫ ω, frobeniusSq B z q ω ∂μ) ≤
      q * (1 - q) * d * (Fintype.card J : ℝ) := by
  rw [bernoulli_frobenius_expectation μ B z hB hbinary hind hmean]
  have hfour : (∑ i, rowSq z i ^ 2) ≤ d * (Fintype.card J : ℝ) := by
    rw [← htrace, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i hi
    have h := mul_le_mul_of_nonneg_right (hleverage i) (rowSq_nonneg z i)
    nlinarith
  have hqv : 0 ≤ q * (1 - q) := mul_nonneg hq.1 (by linarith [hq.2])
  exact (mul_le_mul_of_nonneg_left hfour hqv).trans_eq (by ring)

theorem bernoulli_frobenius_tail {ι J : Type*} [Fintype ι] [Fintype J]
    (B : ι → Ω → ℝ) (z : ι → J → ℝ) {q d t : ℝ}
    (hq : 0 ≤ q ∧ q ≤ 1) (ht : 0 < t)
    (hB : ∀ i, MemLp (B i) 2 μ)
    (hbinary : ∀ i, ∀ᵐ ω ∂μ, B i ω = 0 ∨ B i ω = 1)
    (hind : Pairwise (fun i j => IndepFun (B i) (B j) μ))
    (hmean : ∀ i, ∫ ω, B i ω ∂μ = q)
    (htrace : ∑ i, rowSq z i = (Fintype.card J : ℝ))
    (hleverage : ∀ i, rowSq z i ≤ d) :
    μ.real {ω | t ≤ frobeniusSq B z q ω} ≤
      q * (1 - q) * d * (Fintype.card J : ℝ) / t := by
  have hnonneg : 0 ≤ᵐ[μ] frobeniusSq B z q := by
    filter_upwards [] with ω
    exact Finset.sum_nonneg (fun j _ => Finset.sum_nonneg
      (fun k _ => sq_nonneg (centeredEntry B z q ω j k)))
  have hmarkov := mul_meas_ge_le_integral_of_nonneg hnonneg
    (frobenius_integrable μ B z q hB) t
  apply (le_div_iff₀ ht).mpr
  have hexpect := bernoulli_frobenius_expectation_le μ B z hq hB hbinary hind
    hmean htrace hleverage
  nlinarith

end Moments

end
end Replication

#print Replication.ripple_loss_derivative
#print axioms Replication.ripple_loss_derivative
#print Replication.ripple_score_derivative
#print axioms Replication.ripple_score_derivative
#print Replication.ripple_curvature_bounds
#print axioms Replication.ripple_curvature_bounds
#print Replication.ripple_profile_derivative
#print axioms Replication.ripple_profile_derivative
#print Replication.ripple_even_error_contrast
#print axioms Replication.ripple_even_error_contrast
#print Replication.ripple_score_integer
#print axioms Replication.ripple_score_integer
#print Replication.ripple_profile_integer_stationary
#print axioms Replication.ripple_profile_integer_stationary
#print Replication.ripple_profile_half_score
#print axioms Replication.ripple_profile_half_score
#print Replication.prefix_variance_ratio
#print axioms Replication.prefix_variance_ratio

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
#print Replication.huber_right_tail
#print axioms Replication.huber_right_tail
#print Replication.huber_left_tail
#print axioms Replication.huber_left_tail
#print Replication.huber_pair_lower
#print axioms Replication.huber_pair_lower
#print Replication.huber_pair_flat
#print axioms Replication.huber_pair_flat
#print Replication.huber_pair_flat_minimizing
#print axioms Replication.huber_pair_flat_minimizing
#print Replication.convex_minimizer_inside_ball
#print axioms Replication.convex_minimizer_inside_ball
#print Replication.integrable_loss_contrast
#print axioms Replication.integrable_loss_contrast
#print Replication.binary_variance
#print axioms Replication.binary_variance
#print Replication.binary_memLp
#print axioms Replication.binary_memLp
#print Replication.centered_weighted_sum_second_moment
#print axioms Replication.centered_weighted_sum_second_moment
#print Replication.bernoulli_frobenius_expectation
#print axioms Replication.bernoulli_frobenius_expectation
#print Replication.rowSq_nonneg
#print axioms Replication.rowSq_nonneg
#print Replication.frobenius_integrable
#print axioms Replication.frobenius_integrable
#print Replication.bernoulli_frobenius_expectation_le
#print axioms Replication.bernoulli_frobenius_expectation_le
#print Replication.bernoulli_frobenius_tail
#print axioms Replication.bernoulli_frobenius_tail
