import KSatUpper.Ground.Finite

/-! Ground-state insertions reduce to the degree-`(m+1)` log inequality.

Derived from `SatUpper/Ground/Insertion.lean` (yamelton/sat-upper-4268, Apache-2.0).
The new clause's indicator is the product of `m+1` per-literal backbone
indicators because the two universal quantifiers commute; repeated variables
cause no exception. -/

open MeasureTheory KSatUpper.DirectFinite KSatUpper.GroundFinite

namespace KSatUpper.GroundInsertion

variable {p : ℕ} (T : TrialLaw p) {m : ℕ}

/-- The exponential insertion with an arbitrary `[0,1]` indicator value `Z` that equals the
all-minimizers indicator; the decidability instance is matched by unification. -/
theorem exp_value_insert {Ω : Type*} [Fintype Ω] [Nonempty Ω] (H : Ω → ℕ) (P : Ω → Prop)
    {inst : DecidablePred P} (y Z : ℝ)
    (hZ1 : (∀ x, H x = GroundMinimum.value H → P x) → Z = 1)
    (hZ0 : ¬ (∀ x, H x = GroundMinimum.value H → P x) → Z = 0) :
    Real.exp (-y * GroundMinimum.value (fun x => H x + if P x then 1 else 0)) =
      Real.exp (-y * GroundMinimum.value H) * (1 - (1 - Real.exp (-y)) * Z) := by
  rw [GroundMinimum.insert]
  by_cases h : ∀ x, H x = GroundMinimum.value H → P x
  · rw [if_pos h, hZ1 h]
    push_cast
    rw [show -y * ((GroundMinimum.value H : ℝ) + 1) = -y * GroundMinimum.value H + -y by ring,
      Real.exp_add]
    ring
  · rw [if_neg h, hZ0 h]
    simp

theorem clause_factor {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (x : Fresh m n p) (a : Fields m L) :
    Real.exp (-y * energy (Fin.cons x c) s a) =
      Real.exp (-y * energy c s a) * (1-(1-Real.exp (-y))*∏ j, backbone c s (x j) a) := by
  classical
  have he : cost (Fin.cons x c) s a = fun σ =>
      cost c s a σ + if ∀ j, σ (x j).1.1 = (x j).1.2 then 1 else 0 := by
    funext σ
    simp only [cost, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]
    omega
  unfold energy
  rw [he]
  apply exp_value_insert
  · intro h
    apply Finset.prod_eq_one
    intro j _
    exact if_pos (fun σ hσ => h σ hσ j)
  · intro h
    push_neg at h
    obtain ⟨σ, hσ, j, hj⟩ := h
    apply Finset.prod_eq_zero (Finset.mem_univ j)
    exact if_neg (fun h' => hj (h' σ hσ))

theorem site_factor {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (x : Fresh m n p) (v : Fin (m + 1) → Bool) (a : Fields m L) :
    Real.exp (-y * energy c (Fin.cons x s) (Fin.cons v a)) =
      Real.exp (-y * energy c s a) *
        (1-(1-Real.exp (-y))*backbone c s (x 0) a *
          ∏ j : Fin m, (if v j.succ = true then 1 else 0)) := by
  classical
  have he : cost c (Fin.cons x s) (Fin.cons v a) = fun σ =>
      cost c s a σ + if σ (x 0).1.1 = (x 0).1.2 ∧ ∀ j : Fin m, v j.succ = true then 1 else 0 := by
    funext σ
    simp only [cost, Fin.sum_univ_succ, Fin.cons_zero, Fin.cons_succ]
    omega
  obtain ⟨σ₀,hσ₀⟩ := GroundMinimum.attained (cost c s a)
  rw [mul_assoc (1-Real.exp (-y))]
  unfold energy
  rw [he]
  apply exp_value_insert
  · intro h
    have hb : backbone c s (x 0) a = 1 := if_pos (fun σ hσ => (h σ hσ).1)
    have hw : (∏ j : Fin m, (if v j.succ = true then (1 : ℝ) else 0)) = 1 :=
      Finset.prod_eq_one (fun j _ => if_pos ((h σ₀ hσ₀).2 j))
    rw [hb, hw, one_mul]
  · intro h
    by_cases hall : ∀ j : Fin m, v j.succ = true
    · have hb : backbone c s (x 0) a = 0 :=
        if_neg (fun h' => h (fun σ hσ => ⟨h' σ hσ, hall⟩))
      rw [hb, zero_mul]
    · push_neg at hall
      obtain ⟨j, hj⟩ := hall
      have hw : (∏ j : Fin m, (if v j.succ = true then (1 : ℝ) else 0)) = 0 :=
        Finset.prod_eq_zero (Finset.mem_univ j) (if_neg hj)
      rw [hw, mul_zero]

theorem integral_warnings {n : ℕ} (x : Fresh m n p) :
    (∫ v, ∏ j : Fin m, (if v j.succ = true then 1 else 0 : ℝ) ∂rowLaw T x) =
      ∏ j : Fin m, (T.rate (x j.succ).2 : ℝ) := by
  have he : (fun v : Fin (m + 1) → Bool => ∏ j : Fin m, (if v j.succ = true then 1 else 0 : ℝ)) =
      fun v => ∏ i, (Fin.cases (fun _ => (1 : ℝ)) (fun _ b => if b = true then 1 else 0) :
        Fin (m + 1) → Bool → ℝ) i (v i) := by
    funext v
    rw [Fin.prod_univ_succ]
    simp
  rw [he, rowLaw, integral_fintype_prod_eq_prod, Fin.prod_univ_succ]
  simp only [Fin.cases_zero, Fin.cases_succ, integral_const, measureReal_univ_eq_one, one_smul,
    one_mul, innerLaw]
  exact Finset.prod_congr rfl (fun j _ => T.integral_warning _)

theorem site_moment {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (x : Fresh m n p) :
    moment T y c (Fin.cons x s) = ∫ a, Real.exp (-y * energy c s a) *
      (1-(1-Real.exp (-y))*∏ j, ReplicaPoly.mixedFamily (backbone c s) (rate T) j (x j) a)
        ∂fieldLaw T s := by
  have he : fieldLaw T (Fin.cons x s) =
      Measure.pi (Fin.cons (rowLaw T x) (fun i => rowLaw T (s i))) := by
    unfold fieldLaw
    congr 1
    funext i
    exact Fin.cases rfl (fun _ => rfl) i
  rw [GroundFinite.moment, he, DirectProduct.integral_cons]
  simp_rw [site_factor]
  apply integral_congr_ae
  filter_upwards [] with a
  rw [ReplicaPoly.prod_mixedFamily (backbone c s) (rate T) (fun f j => f (x j) a)]
  simp only [rate]
  rw [integral_const_mul]
  congr 1
  rw [integral_sub (integrable_const _) Integrable.of_finite, integral_const,
    measureReal_univ_eq_one, one_smul, integral_const_mul, integral_warnings]
  ring

theorem log_ratio {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    {Z : Fields m L → ℝ} (h0 : ∀ a, 0 ≤ Z a) (h1 : ∀ a, Z a ≤ 1)
    {M : ℝ} (hM : 0 < M)
    (he : M = ∫ a, Real.exp (-y * energy c s a)*(1-(1-Real.exp (-y))*Z a) ∂fieldLaw T s) :
    Real.log M - Real.log (moment T y c s) =
      Real.log (1-(1-Real.exp (-y))*(∫ a, Z a ∂tilted T y c s)) := by
  rw [← Real.log_div hM.ne' (moment_pos T y c s).ne', he]
  exact congrArg Real.log (GibbsInsertion.partition_ratio (fieldLaw T s) Integrable.of_finite
    (measurable_of_countable _) h0 h1 (1-Real.exp (-y)))

theorem product_bounds {n L : ℕ} (f : Fin (m + 1) → Seed n p → Fields m L → ℝ)
    (hb : ∀ j x a, 0 ≤ f j x a ∧ f j x a ≤ 1) (x : Fresh m n p) (a : Fields m L) :
    0 ≤ ∏ j, f j (x j) a ∧ (∏ j, f j (x j) a) ≤ 1 :=
  ⟨Finset.prod_nonneg (fun j _ => (hb j (x j) a).1),
    Finset.prod_le_one (fun j _ => (hb j (x j) a).1) (fun j _ => (hb j (x j) a).2)⟩

theorem mixed_bounds {n K L : ℕ} (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (j : Fin (m + 1)) (x : Seed n p) (a : Fields m L) :
    0 ≤ ReplicaPoly.mixedFamily (backbone c s) (rate T) j x a ∧
      ReplicaPoly.mixedFamily (backbone c s) (rate T) j x a ≤ 1 :=
  ReplicaPoly.mixedFamily_cases (P := fun f => 0 ≤ f x a ∧ f x a ≤ 1)
    (backbone_bounds c s x a) (rate_bounds T x a) j

theorem clause_increment {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p)
    (s : Fin L → Fresh m n p) (x : Fresh m n p) :
    entropy T y (Fin.cons x c) s - entropy T y c s =
      Real.log (1-(1-Real.exp (-y))*LogInsertion.meanProduct (tilted T y c s) (m + 1)
        (fun _ => backbone c s) x) := by
  have hb := product_bounds (fun _ => backbone c s) (fun _ => backbone_bounds c s) x
  exact log_ratio T y c s (fun a => (hb a).1) (fun a => (hb a).2)
    (moment_pos T y (Fin.cons x c) s) (by simp_rw [GroundFinite.moment, clause_factor])

theorem site_increment {n K L : ℕ} (y : ℝ) (c : Fin K → Fresh m n p)
    (s : Fin L → Fresh m n p) (x : Fresh m n p) :
    entropy T y c (Fin.cons x s) - entropy T y c s =
      Real.log (1-(1-Real.exp (-y))*LogInsertion.meanProduct (tilted T y c s) (m + 1)
        (ReplicaPoly.mixedFamily (backbone c s) (rate T)) x) := by
  have hb := product_bounds _ (mixed_bounds T c s) x
  exact log_ratio T y c s (fun a => (hb a).1) (fun a => (hb a).2)
    (moment_pos T y c (Fin.cons x s)) (site_moment T y c s x)

/-- `d_y = E log(1 - (1 - e^{-y}) R_1 ⋯ R_{m+1})` under the fresh row law. -/
noncomputable def edgeMean (m n : ℕ) [NeZero n] (y : ℝ) : ℝ :=
  ∫ x : Fresh m n p, Real.log (1-(1-Real.exp (-y))*∏ j, (T.rate (x j).2 : ℝ)) ∂freshLaw T m n

/-- The averaged comparison `E ΔC - (m+1) E ΔS + m d_y ≤ 0`, i.e. (G) of the proof. -/
theorem poly_nonpos {n K L : ℕ} [NeZero n] {y : ℝ} (hy : 0 ≤ y)
    (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) :
    (∫ x, entropy T y (Fin.cons x c) s - entropy T y c s ∂freshLaw T m n) -
      ((m : ℝ) + 1)*(∫ x, entropy T y c (Fin.cons x s) - entropy T y c s ∂freshLaw T m n) +
        (m : ℝ)*edgeMean T m n y ≤ 0 := by
  have h := LogInsertion.poly_log_insertion_nonpos (seedLaw T n) (tilted T y c s) m
    (b := backbone c s) (c := rate T) (measurable_of_countable _) (measurable_of_countable _)
    (fun x a => (backbone_bounds c s x a).1) (fun x a => (backbone_bounds c s x a).2)
    (fun x a => (rate_bounds T x a).1) (fun x a => (rate_bounds T x a).2)
    (q := 1-Real.exp (-y)) (by linarith [Real.exp_le_one_iff.mpr (neg_nonpos.mpr hy)])
    (by linarith [Real.exp_pos (-y)])
  simp_rw [clause_increment, site_increment]
  simpa only [LogInsertion.insertionLog, LogInsertion.meanProduct, rate, integral_const,
    measureReal_univ_eq_one, one_smul, edgeMean, freshLaw] using h

theorem increment_bound {n K L : ℕ} {y : ℝ} (hy : 0 ≤ y)
    (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p)
    (f : Fin (m + 1) → Seed n p → Fields m L → ℝ)
    (hb : ∀ j x a, 0 ≤ f j x a ∧ f j x a ≤ 1) (x : Fresh m n p) :
    ‖Real.log (1-(1-Real.exp (-y))*LogInsertion.meanProduct (tilted T y c s) (m + 1) f x)‖ ≤ y := by
  have hz := LogInsertion.meanProduct_bounds (tilted T y c s) (m + 1)
    (fun _ => measurable_of_countable _)
    (fun j x a => (hb j x a).1) (fun j x a => (hb j x a).2) x
  have h := log_factor_bounds hy hz.1 hz.2
  rw [Real.norm_eq_abs, abs_of_nonpos h.2]
  linarith [h.1]

theorem clause_increment_bound {n K L : ℕ} {y : ℝ} (hy : 0 ≤ y)
    (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) (x : Fresh m n p) :
    ‖entropy T y (Fin.cons x c) s - entropy T y c s‖ ≤ y := by
  rw [clause_increment]
  exact increment_bound T hy c s _ (fun _ => backbone_bounds c s) x

theorem site_increment_bound {n K L : ℕ} {y : ℝ} (hy : 0 ≤ y)
    (c : Fin K → Fresh m n p) (s : Fin L → Fresh m n p) (x : Fresh m n p) :
    ‖entropy T y c (Fin.cons x s) - entropy T y c s‖ ≤ y := by
  rw [site_increment]
  exact increment_bound T hy c s _ (mixed_bounds T c s) x

end KSatUpper.GroundInsertion
