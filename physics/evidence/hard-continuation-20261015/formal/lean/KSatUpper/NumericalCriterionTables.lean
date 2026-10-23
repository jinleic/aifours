import KSatUpper.NumericalCriterion

/-! Certificates from materialized tables.

`certUpper` evaluates the exponential table and the alternating vertex sums in one kernel
computation; one `decide` over it peaked at about 12 GB of memory at `T = 128`. These lemmas let a
certificate be checked in bounded pieces: if a literal list `tbl` agrees with the computed table on
the entries `j ≤ cutoff` (each checked by a small `decide`), then `certUpper` equals the same
expression with `tbl` in place of the computed table, and a rational bound for the edge term can
be substituted on either side. -/

namespace KSatUpper.NumericalCriterion

variable {p : ℕ} (T : TrialLaw p) (m : ℕ) (α : ℚ)

theorem table_getD (cutoff j : ℕ) (hj : j ≤ cutoff) :
    (table T m α cutoff).getD j (0, 0) = bounds T m α j := by
  simp [table, List.getD, List.getElem?_range (Nat.lt_succ_of_le hj)]

theorem momentLower_congr {l u l' u' : ℕ → ℚ} {k : ℕ}
    (hl : ∀ j, j ≤ k → l j = l' j) (hu : ∀ j, j ≤ k → u j = u' j) :
    VertexEnclosures.momentLower l u k = VertexEnclosures.momentLower l' u' k := by
  unfold VertexEnclosures.momentLower
  apply Finset.sum_congr rfl
  intro j hj
  have hjk : j ≤ k := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
  rw [hl j hjk, hu j hjk]

theorem vertexUpper_congr {K : ℕ} {l u l' u' : ℕ → ℚ}
    (hl : ∀ j, j ≤ K → l j = l' j) (hu : ∀ j, j ≤ K → u j = u' j) :
    VertexEnclosures.vertexUpper K l u = VertexEnclosures.vertexUpper K l' u' := by
  unfold VertexEnclosures.vertexUpper
  refine congrArg Neg.neg (Finset.sum_congr rfl fun k hk => ?_)
  have hk' : k + 1 ≤ K := Nat.succ_le_of_lt (Finset.mem_range.mp hk)
  rw [momentLower_congr (k := k + 1) (fun j hj => hl j (hj.trans hk'))
    (fun j hj => hu j (hj.trans hk'))]


/-- The vertex term computed from given values `M k` of the alternating lower moments. -/
def vertexOf (K : ℕ) (M : ℕ → ℚ) : ℚ :=
  -∑ k ∈ Finset.range K, (max 0 (M (k+1)))^2 / (k+1)

theorem vertexUpper_eq_vertexOf (K : ℕ) (l u M : ℕ → ℚ)
    (hM : ∀ k, k ≤ K → VertexEnclosures.momentLower l u k = M k) :
    VertexEnclosures.vertexUpper K l u = vertexOf K M := by
  unfold VertexEnclosures.vertexUpper vertexOf
  refine congrArg Neg.neg (Finset.sum_congr rfl fun k hk => ?_)
  rw [hM (k + 1) (Nat.succ_le_of_lt (Finset.mem_range.mp hk))]
theorem certUpper_eq_tables (cutoff N : ℕ) (u : ℚ) (tbl : List (ℚ × ℚ))
    (htbl : ∀ j, j ≤ cutoff → bounds T m α j = tbl.getD j (0, 0)) :
    certUpper T m α cutoff N u =
      VertexEnclosures.vertexUpper cutoff (lowerOf tbl) (upperOf tbl) +
        (-(m : ℚ)) * α * edgeLower T m N u := by
  have hl : ∀ j, j ≤ cutoff → lowerOf (table T m α cutoff) j = lowerOf tbl j := by
    intro j hj
    simp only [lowerOf]
    rw [table_getD T m α cutoff j hj, htbl j hj]
  have hu : ∀ j, j ≤ cutoff → upperOf (table T m α cutoff) j = upperOf tbl j := by
    intro j hj
    simp only [upperOf]
    rw [table_getD T m α cutoff j hj, htbl j hj]
  simp only [certUpper]
  rw [vertexUpper_congr hl hu]

/-- Upper bound for `certUpper` from a checked table and a lower bound `E` for the edge term. -/
theorem certUpper_le_of_tables (hα : 0 ≤ α) (cutoff N : ℕ) (u : ℚ) (tbl : List (ℚ × ℚ))
    (htbl : ∀ j, j ≤ cutoff → bounds T m α j = tbl.getD j (0, 0)) {E : ℚ}
    (hE : E ≤ edgeLower T m N u) :
    certUpper T m α cutoff N u ≤
      VertexEnclosures.vertexUpper cutoff (lowerOf tbl) (upperOf tbl) + (-(m : ℚ)) * α * E := by
  rw [certUpper_eq_tables T m α cutoff N u tbl htbl]
  have hmα : -(m : ℚ) * α ≤ 0 := by
    have := mul_nonneg (Nat.cast_nonneg m : (0 : ℚ) ≤ m) hα
    linarith
  have h := mul_le_mul_of_nonpos_left hE hmα
  linarith

/-- Lower bound for `certUpper` from a checked table and an upper bound `E` for the edge term. -/
theorem le_certUpper_of_tables (hα : 0 ≤ α) (cutoff N : ℕ) (u : ℚ) (tbl : List (ℚ × ℚ))
    (htbl : ∀ j, j ≤ cutoff → bounds T m α j = tbl.getD j (0, 0)) {E : ℚ}
    (hE : edgeLower T m N u ≤ E) :
    VertexEnclosures.vertexUpper cutoff (lowerOf tbl) (upperOf tbl) + (-(m : ℚ)) * α * E ≤
      certUpper T m α cutoff N u := by
  rw [certUpper_eq_tables T m α cutoff N u tbl htbl]
  have hmα : -(m : ℚ) * α ≤ 0 := by
    have := mul_nonneg (Nat.cast_nonneg m : (0 : ℚ) ≤ m) hα
    linarith
  have h := mul_le_mul_of_nonpos_left hE hmα
  linarith

end KSatUpper.NumericalCriterion
