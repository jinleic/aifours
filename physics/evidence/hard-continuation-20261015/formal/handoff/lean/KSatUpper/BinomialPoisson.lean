import KSatUpper.PoissonExpectation
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Data.Nat.Choose.Cast
import Mathlib.Analysis.Normed.Ring.InfiniteSum

/-! A finite binomial replacement proves the Poisson clause/site comparison, arity `m+1`.

Derived from `SatUpper/BinomialPoisson.lean` (yamelton/sat-upper-4268, Apache-2.0),
where the coefficients were `1, 2, 3`. Here they are `1, m, m+1`: one slot of a
row of `m+1` becomes a clause, the other `m` stay empty. This is (H) and (I) of
the written proof. The Cauchy product performs the Poisson averaging. -/

namespace KSatUpper.BinomialPoisson

open Finset MeasureTheory ProbabilityTheory
open scoped NNReal

/-- Unnormalized binomial mixture of clause insertions and empty slots. -/
noncomputable def mixture (m : ℕ) (f : ℕ → ℕ → ℝ) (N K L : ℕ) : ℝ :=
  ∑ j ∈ range (N+1), (N.choose j : ℝ)*(m : ℝ)^(N-j)*f (K+j) L

theorem mixture_zero (m : ℕ) (f : ℕ → ℕ → ℝ) (K L : ℕ) : mixture m f 0 K L = f K L := by
  simp [mixture]

theorem mixture_succ (m : ℕ) (f : ℕ → ℕ → ℝ) (N K L : ℕ) :
    mixture m f (N+1) K L = mixture m f N (K+1) L + (m : ℝ)*mixture m f N K L := by
  unfold mixture
  have h := Finset.sum_choose_succ_mul (fun j l => (m : ℝ)^l*f (K+j) L) N
  simp only [mul_assoc] at *
  rw [h, add_comm]
  simp only [Finset.mul_sum]
  congr 1
  · apply sum_congr rfl
    intro j hj
    simp only [Nat.add_assoc, Nat.add_comm 1 j]
  · apply sum_congr rfl
    intro j hj
    have hj : j ≤ N := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
    have he : N+1-j = N-j+1 := by omega
    rw [he, pow_succ]
    ring

/-- (H) of the written proof, multiplied by `m+1` to avoid division. -/
theorem mixture_le_mul {m : ℕ} {f : ℕ → ℕ → ℝ} {d : ℝ}
    (h : ∀ K L, f (K+1) L - ((m : ℝ)+1)*f K (L+1) + (m : ℝ)*f K L + (m : ℝ)*d ≤ 0)
    (N K L : ℕ) :
    ((m : ℝ)+1)*mixture m f N K L ≤ ((m : ℝ)+1)^N*(((m : ℝ)+1)*f K (L+N) - (m : ℝ)*N*d) := by
  induction N generalizing K L with
  | zero => simp [mixture_zero]
  | succ N ih =>
    rw [mixture_succ]
    have hP : (0 : ℝ) ≤ ((m : ℝ)+1)^N := by positivity
    have hm : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
    have h₁ := ih (K+1) L
    have h₂ := mul_le_mul_of_nonneg_left (ih K L) hm
    have h₃ := mul_le_mul_of_nonneg_left (h K (L+N))
      (mul_nonneg hP (by positivity : (0 : ℝ) ≤ (m : ℝ)+1))
    have he : L+(N+1) = L+N+1 := by omega
    rw [he, pow_succ]
    push_cast
    nlinarith [h₁, h₂, h₃]

theorem mixture_le {m : ℕ} {f : ℕ → ℕ → ℝ} {d : ℝ}
    (h : ∀ K L, f (K+1) L - ((m : ℝ)+1)*f K (L+1) + (m : ℝ)*f K L + (m : ℝ)*d ≤ 0)
    (N K L : ℕ) :
    mixture m f N K L ≤ ((m : ℝ)+1)^N*(f K (L+N) - (m : ℝ)*N*d/((m : ℝ)+1)) := by
  have hm1 : (0 : ℝ) < (m : ℝ)+1 := by positivity
  have hh := mixture_le_mul h N K L
  have he : ((m : ℝ)+1)^N*(f K (L+N) - (m : ℝ)*N*d/((m : ℝ)+1)) =
      ((m : ℝ)+1)^N*(((m : ℝ)+1)*f K (L+N) - (m : ℝ)*N*d)/((m : ℝ)+1) := by
    field_simp
  rw [he, le_div_iff₀ hm1]
  linarith

theorem mixture_series (m : ℕ) {f : ℕ → ℕ → ℝ} {A B : ℝ}
    (hg : ∀ n, ‖f n 0‖ ≤ A+B*n) (a : ℝ) :
    HasSum (fun n => mixture m f n 0 0 * a^n / (n.factorial : ℝ))
      ((∑' n, f n 0 * a^n / (n.factorial : ℝ))*Real.exp ((m : ℝ)*a)) := by
  have hf : Summable (fun n => ‖f n 0 * a^n / (n.factorial : ℝ)‖) := by
    simpa only [norm_div, norm_mul, norm_pow, Real.norm_eq_abs a, Real.norm_natCast] using
      PoissonExpectation.summable_exp_series_of_linear_growth
        (f := fun n => ‖f n 0‖) (by simpa only [norm_norm] using hg) |a|
  have hg' : Summable (fun n => ‖((m : ℝ)*a)^n / (n.factorial : ℝ)‖) := by
    simpa only [norm_div, norm_pow, Real.norm_eq_abs ((m : ℝ)*a), Real.norm_natCast] using
      (NormedSpace.expSeries_div_hasSum_exp ℝ |(m : ℝ)*a|).summable
  have he := NormedSpace.expSeries_div_hasSum_exp ℝ ((m : ℝ)*a)
  have hc := hasSum_sum_range_mul_of_summable_norm hf hg'
  rw [he.tsum_eq, ← Real.exp_eq_exp_ℝ] at hc
  convert hc using 1
  funext n
  unfold mixture
  simp only [zero_add, Finset.sum_mul, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro k hk
  have hk : k ≤ n := Nat.le_of_lt_succ (Finset.mem_range.mp hk)
  have hp : a^n = a^k*a^(n-k) := by rw [← pow_add, Nat.add_sub_of_le hk]
  have hfac (n : ℕ) : (n.factorial : ℝ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero n
  rw [Nat.cast_choose ℝ hk, mul_pow, hp]
  field_simp

/-- A finite binomial replacement followed by a Poisson average.
The Poisson Cauchy product absorbs the empty slots. No differentiation is used. -/
theorem comparison {m : ℕ} {f : ℕ → ℕ → ℝ} {C d : ℝ}
    (hC : ∀ K L, ‖f (K+1) L-f K L‖ ≤ C)
    (hS : ∀ K L, ‖f K (L+1)-f K L‖ ≤ C)
    (h : ∀ K L, f (K+1) L - ((m : ℝ)+1)*f K (L+1) + (m : ℝ)*f K L + (m : ℝ)*d ≤ 0)
    (a : ℝ≥0) :
    PoissonExpectation.poissonExpectation (fun K => f K 0) a ≤
      PoissonExpectation.poissonExpectation (f 0) (((m : ℝ≥0)+1)*a) - (m : ℝ)*a*d := by
  have hgC := PoissonExpectation.linear_growth_of_bounded_increments (f := fun K => f K 0)
    (fun K => hC K 0)
  have hgS := PoissonExpectation.linear_growth_of_bounded_increments (hS 0)
  have hm1 : (0 : ℝ) < (m : ℝ)+1 := by positivity
  have hl := (mixture_series m hgC (a : ℝ)).mul_left (Real.exp (-((m : ℝ)+1)*(a : ℝ)))
  have hr := ((PoissonExpectation.summable_exp_series_of_linear_growth hgS
    (((m : ℝ)+1)*a)).hasSum).mul_left (Real.exp (-((m : ℝ)+1)*(a : ℝ)))
  have hm := (Campbell.poisson_mean_series (((m : ℝ≥0)+1)*a)).mul_left
    ((m : ℝ)*d/((m : ℝ)+1))
  have hb := hasSum_le (fun n => ?_) hl (hr.sub hm)
  · have he : Real.exp (-((m : ℝ)+1)*(a : ℝ))*Real.exp ((m : ℝ)*a) = Real.exp (-(a : ℝ)) := by
      rw [← Real.exp_add]
      congr 1
      ring
    convert hb using 1
    · unfold PoissonExpectation.poissonExpectation
      rw [← he]
      ring
    · simp only [NNReal.coe_mul, NNReal.coe_add, NNReal.coe_natCast, NNReal.coe_one]
      unfold PoissonExpectation.poissonExpectation
      field_simp
  · have hh := mul_le_mul_of_nonneg_left (mixture_le h n 0 0)
      (by positivity : 0 ≤ Real.exp (-((m : ℝ)+1)*(a : ℝ)) * (a : ℝ)^n / (n.factorial : ℝ))
    convert hh using 1
    · ring
    · simp only [zero_add, poissonPMFReal, NNReal.coe_mul, NNReal.coe_add, NNReal.coe_natCast,
        NNReal.coe_one, mul_pow, neg_mul]
      field_simp

end KSatUpper.BinomialPoisson
