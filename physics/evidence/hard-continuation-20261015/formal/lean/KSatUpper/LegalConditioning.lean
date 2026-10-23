import KSatUpper.Ground.Formula
import KSatUpper.FiniteVariance
import Mathlib.Data.Fintype.CardEmbedding

/-! Conditioning on distinct variables costs only a constant factor in probability.

Derived from `SatUpper/LegalConditioning.lean` (yamelton/sat-upper-4268, Apache-2.0),
where the arity-three ratio `n^2/((n-1)(n-2)) ≤ exp(6/n)` was used. For arity `k`
the ratio `n^k / (n(n-1)⋯(n-k+1))` is at most `exp(k^2/n)` once `2k ≤ n`. -/

namespace KSatUpper.LegalConditioning

theorem card_clause (k n : ℕ) : Fintype.card (Clause k n) = n.descFactorial k * 2^k := by
  let e : {v : Fin k → Fin n // Function.Injective v} ≃ (Fin k ↪ Fin n) :=
    ⟨fun v => ⟨v.val,v.property⟩, fun v => ⟨v.toFun,v.injective⟩, fun _ => rfl, fun _ => rfl⟩
  simp only [Clause, Fintype.card_prod, Fintype.card_congr e,
    Fintype.card_embedding_eq, Fintype.card_fin, Fintype.card_fun, Fintype.card_bool]

theorem card_repeated (k n : ℕ) : Fintype.card (ClauseEndpoint.Clause k n) = (n*2)^k := by
  simp [ClauseEndpoint.Clause, Fintype.card_prod]

/-- `n^k ≤ exp(k^2/n) · n(n-1)⋯(n-k+1)` whenever `2k ≤ n`. -/
theorem pow_le_exp_mul_descFactorial (n : ℕ) (hn : 0 < n) : ∀ k : ℕ, 2*k ≤ n →
    (n : ℝ)^k ≤ Real.exp ((k : ℝ)^2/n) * (n.descFactorial k : ℝ)
  | 0, _ => by simp
  | k+1, hk => by
    have ih := pow_le_exp_mul_descFactorial n hn k (by omega)
    have hkn : k < n := by omega
    have hnr : (0 : ℝ) < n := by exact_mod_cast hn
    have hkr : (k : ℝ) < n := by exact_mod_cast hkn
    have hk2 : 2*(k : ℝ) + 2 ≤ n := by exact_mod_cast hk
    rw [Nat.descFactorial_succ, Nat.cast_mul, Nat.cast_sub hkn.le, pow_succ]
    have h1 : (1 : ℝ) + (2*k)/n ≤ Real.exp ((2*k+1 : ℝ)/n) := by
      have h := Real.add_one_le_exp ((2*k+1 : ℝ)/n)
      have h2 : (2*k : ℝ)/n ≤ (2*k+1)/n := div_le_div_of_nonneg_right (by linarith) hnr.le
      linarith
    have h3 : (n : ℝ) ≤ (1 + (2*k)/n) * ((n : ℝ) - k) := by
      have hq : (k : ℝ) ≤ (2*k)*((n : ℝ) - k)/n := by
        rw [le_div_iff₀ hnr]
        nlinarith [mul_nonneg (Nat.cast_nonneg k : (0 : ℝ) ≤ k) (by linarith : (0 : ℝ) ≤ n - 2*k)]
      have he : (1 + (2*k)/n) * ((n : ℝ) - k) = (n - k) + (2*k)*((n : ℝ) - k)/n := by ring
      rw [he]
      linarith
    have hstep : (n : ℝ) ≤ Real.exp ((2*k+1 : ℝ)/n) * ((n : ℝ) - k) :=
      h3.trans (mul_le_mul_of_nonneg_right h1 (by linarith))
    have hexp : Real.exp (((k+1 : ℕ) : ℝ)^2/n) =
        Real.exp ((k : ℝ)^2/n) * Real.exp ((2*k+1 : ℝ)/n) := by
      rw [← Real.exp_add]
      congr 1
      push_cast
      field_simp
      ring
    rw [hexp]
    calc (n : ℝ)^k * n ≤ (Real.exp ((k : ℝ)^2/n) * (n.descFactorial k : ℝ)) *
          (Real.exp ((2*k+1 : ℝ)/n) * ((n : ℝ) - k)) :=
          mul_le_mul ih hstep hnr.le (by positivity)
      _ = _ := by ring

theorem clause_ratio_le (k n : ℕ) (hn : 2*k ≤ n) (hn0 : 0 < n) :
    (Fintype.card (ClauseEndpoint.Clause k n) : ℝ) / Fintype.card (Clause k n) ≤
      Real.exp ((k : ℝ)^2/n) := by
  rw [card_repeated, card_clause]
  have hd : (0 : ℝ) < n.descFactorial k := by exact_mod_cast Nat.descFactorial_pos.mpr (by omega)
  have h := pow_le_exp_mul_descFactorial n hn0 k hn
  push_cast
  rw [mul_pow, div_le_iff₀ (by positivity)]
  have h2 : (0 : ℝ) < 2^k := by positivity
  nlinarith [mul_le_mul_of_nonneg_right h h2.le]

theorem formula_ratio_le {k n M : ℕ} (hn : 2*k ≤ n) (hn0 : 0 < n) {α : ℝ} (hM : (M : ℝ) ≤ α*n) :
    (Fintype.card (GroundFormula.Formula k n M) : ℝ) / Fintype.card (Formula k n M) ≤
      Real.exp ((k : ℝ)^2*α) := by
  have hn0' : (n : ℝ) ≠ 0 := by exact_mod_cast hn0.ne'
  calc
    _ = ((Fintype.card (ClauseEndpoint.Clause k n) : ℝ) / Fintype.card (Clause k n))^M := by
      simp only [GroundFormula.Formula, Formula, Fintype.card_fun, Fintype.card_fin,
        Nat.cast_pow, div_pow]
    _ ≤ (Real.exp ((k : ℝ)^2/n))^M :=
      pow_le_pow_left₀ (by positivity) (clause_ratio_le k n hn hn0) M
    _ = Real.exp ((M : ℝ)*((k : ℝ)^2/n)) := (Real.exp_nat_mul _ _).symm
    _ ≤ Real.exp ((k : ℝ)^2*α) := by
      apply Real.exp_le_exp.mpr
      have h := mul_le_mul_of_nonneg_right hM (by positivity : 0 ≤ (k : ℝ)^2/n)
      have he : (α*n)*((k : ℝ)^2/n) = (k : ℝ)^2*α := by field_simp
      rwa [he] at h

theorem satisfiabilityProbability_le_variance {k n M : ℕ} (hn : 2*k ≤ n) (hn0 : 0 < n) {α : ℝ}
    (hM : (M : ℝ) ≤ α*n) (hmean : 0 < GroundFormula.mean k n M) :
    satisfiabilityProbability k n M ≤
      Real.exp ((k : ℝ)^2*α) * (GroundFormula.variance k n M / (GroundFormula.mean k n M)^2) := by
  classical
  letI : NeZero n := ⟨by omega⟩
  let event := Finset.univ.filter (fun F : Formula k n M => Satisfiable F)
  let zero := Finset.univ.filter (fun F : GroundFormula.Formula k n M => GroundFormula.energy F = 0)
  have hi : event.image GroundFormula.clauses ⊆ zero := by
    intro F hF
    obtain ⟨G,hG,rfl⟩ := Finset.mem_image.mp hF
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,
      GroundFormula.energy_zero_of_satisfiable (Finset.mem_filter.mp hG).2⟩
  have hcard : (event.card : ℝ) ≤ zero.card := by
    exact_mod_cast (by
      simpa only [Finset.card_image_of_injective _ GroundFormula.clauses_injective] using
        Finset.card_le_card hi)
  have hz := finite_event_chebyshev
    (fun F : GroundFormula.Formula k n M => (GroundFormula.energy F : ℝ))
    zero hmean.ne' (fun F hF => by simp only [(Finset.mem_filter.mp hF).2, Nat.cast_zero])
  have hnonneg : 0 ≤ (zero.card : ℝ) / Fintype.card (GroundFormula.Formula k n M) := by positivity
  calc
    satisfiabilityProbability k n M ≤ (zero.card : ℝ) / Fintype.card (Formula k n M) :=
      div_le_div_of_nonneg_right hcard (Nat.cast_nonneg _)
    _ = ((Fintype.card (GroundFormula.Formula k n M) : ℝ) / Fintype.card (Formula k n M)) *
        ((zero.card : ℝ) / Fintype.card (GroundFormula.Formula k n M)) := by
      have hc : (Fintype.card (GroundFormula.Formula k n M) : ℝ) ≠ 0 := by
        exact_mod_cast Fintype.card_ne_zero
      field_simp
    _ ≤ Real.exp ((k : ℝ)^2*α) * ((zero.card : ℝ) / Fintype.card (GroundFormula.Formula k n M)) :=
      mul_le_mul_of_nonneg_right (formula_ratio_le hn hn0 hM) hnonneg
    _ ≤ _ := mul_le_mul_of_nonneg_left hz (Real.exp_pos _).le

/-- A positive linear minimum-energy mean and linear variance force unsatisfiability,
even after conditioning every clause to use distinct variables. -/
theorem candidate_of_mean_and_variance_bounds (k : ℕ) (M : ℕ → ℕ) (α c V : ℝ)
    (hc : 0 < c) (hV : 0 ≤ V)
    (hcount : ∀ n, (M n : ℝ) ≤ α*n)
    (hmean : ∀ᶠ n in Filter.atTop, c*n ≤ GroundFormula.mean k n (M n))
    (hvar : ∀ᶠ n in Filter.atTop, GroundFormula.variance k n (M n) ≤ V*n) :
    Filter.Tendsto (fun n => satisfiabilityProbability k n (M n)) Filter.atTop (nhds 0) := by
  apply squeeze_zero' (Filter.Eventually.of_forall (fun n => by
    unfold satisfiabilityProbability
    positivity))
  · filter_upwards [hmean, hvar, Filter.eventually_ge_atTop (2*k+1)] with n hm hv hn
    have hn0 : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
    have hcn : 0 < c*n := mul_pos hc hn0
    have hm0 : 0 < GroundFormula.mean k n (M n) := hcn.trans_le hm
    have hsq := pow_le_pow_left₀ hcn.le hm 2
    calc
      satisfiabilityProbability k n (M n) ≤
          Real.exp ((k : ℝ)^2*α) * (GroundFormula.variance k n (M n) /
            (GroundFormula.mean k n (M n))^2) :=
        satisfiabilityProbability_le_variance (by omega) (by omega) (hcount n) hm0
      _ ≤ Real.exp ((k : ℝ)^2*α) * (V*n / (c*n)^2) := by
        apply mul_le_mul_of_nonneg_left _ (Real.exp_pos _).le
        exact (div_le_div_of_nonneg_right hv (sq_nonneg _)).trans
          (div_le_div_of_nonneg_left (mul_nonneg hV hn0.le) (sq_pos_of_pos hcn) hsq)
      _ = (Real.exp ((k : ℝ)^2*α)*V/c^2)/(n : ℝ) := by field_simp
  · exact tendsto_const_div_atTop_nhds_zero_nat (Real.exp ((k : ℝ)^2*α)*V/c^2)

end KSatUpper.LegalConditioning
