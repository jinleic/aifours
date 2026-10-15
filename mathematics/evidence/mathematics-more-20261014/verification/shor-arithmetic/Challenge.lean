import Mathlib.Data.Nat.PrimeFin
import Mathlib.Tactic.Simproc.Factors
import Mathlib.Tactic

/-!
Arithmetic roots used by the Shor finite-completion dossier.

These are kernel-checked arithmetic facts only. They do not formalize the
code-theoretic bridge, the multiplier lemmas, or Szabó's theorem; those enter
`combined_order_lower_bound` only as explicit hypotheses.
-/

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

namespace ShorArithmetic

/-- Arithmetic heart of the 8-divisor argument: if `4 ∣ n` but `8 ∤ n`, some unit
`u` modulo `n` has `8u ≡ 4`. -/
theorem exists_unit_eight_mul_eq_four (n : ℕ) (h4 : 4 ∣ n) (h8 : ¬ 8 ∣ n) :
    ∃ u : ℕ, Nat.Coprime u n ∧ 8 * u % n = 4 % n := by sorry

/-- Finite check: every positive multiple of 4 below 60 has at most two prime factors. -/
theorem small_four_multiple_prime_count :
    ∀ q : Fin 60, 0 < q.val → 4 ∣ q.val → q.val.primeFactors.card ≤ 2 := by
  intro q hpos hfour
  fin_cases q <;> simp [Nat.primeFactors, -Nat.toFinset_factors, Nat.primeFactorsList_ofNat] at *

/-- If `4 ∣ q` and three pairwise distinct primes divide `q`, then `q ≥ 60`.
The primes may be 2, 3, 5 or 11; no novelty or disjointness from 330 is assumed. -/
theorem quotient_ge_sixty
    (q p r t : ℕ) (hq : 0 < q) (hfour : 4 ∣ q)
    (hp : p.Prime) (hr : r.Prime) (ht : t.Prime)
    (hpr : p ≠ r) (hpt : p ≠ t) (hrt : r ≠ t)
    (hproduct : p * r * t ∣ q) : 60 ≤ q := by sorry

/-- Arithmetic consequence only: Szabó's displayed divisibility and the code-theoretic
`8 ∣ n` are hypotheses here, not proved in Lean. -/
theorem combined_order_lower_bound
    (n p r t : ℕ) (hn : 0 < n) (height : 8 ∣ n)
    (hp : p.Prime) (hr : r.Prime) (ht : t.Prime)
    (hpr : p ≠ r) (hpt : p ≠ t) (hrt : r ≠ t)
    (hsource : 330 * p * r * t ∣ n) : 19800 ≤ n := by sorry

/-! False-proposition controls: each negated statement is a mutation of a root. -/

/-- Dropping `8 ∣ n` from `combined_order_lower_bound` is false (`n = 9900`). -/
example : ¬ (∀ n : ℕ, 0 < n → 330 * 2 * 3 * 5 ∣ n → 19800 ≤ n) := by
  intro h
  have := h 9900 (by norm_num) (by norm_num)
  omega

/-- The combined bound is attained arithmetically, so the hypotheses are satisfiable. -/
example : 8 ∣ 19800 ∧ 330 * 2 * 3 * 5 ∣ 19800 ∧ Nat.Prime 2 ∧ Nat.Prime 3 ∧ Nat.Prime 5 := by
  norm_num

/-- Dropping distinctness from `quotient_ge_sixty` is false (`q = 8`, all primes equal 2). -/
example : ¬ (∀ q p r t : ℕ, 0 < q → 4 ∣ q → p.Prime → r.Prime → t.Prime →
    p * r * t ∣ q → 60 ≤ q) := by
  intro h
  have := h 8 2 2 2 (by norm_num) (by norm_num) Nat.prime_two Nat.prime_two Nat.prime_two
    (by norm_num)
  omega

/-- Without `¬ 8 ∣ n`, the unit can fail to exist (`n = 8`). -/
example : ¬ ∃ u : ℕ, Nat.Coprime u 8 ∧ 8 * u % 8 = 4 % 8 := by
  rintro ⟨u, -, hu⟩
  omega

end ShorArithmetic
