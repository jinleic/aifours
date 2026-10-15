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
    ∃ u : ℕ, Nat.Coprime u n ∧ 8 * u % n = 4 % n := by
  obtain ⟨m, rfl⟩ := h4
  have hm : m % 2 = 1 := by
    by_contra hm
    apply h8
    exact ⟨m / 2, by omega⟩
  have hu0 : 2 * ((m + 1) / 2) = m + 1 := by omega
  rcases Nat.mod_two_eq_zero_or_one ((m + 1) / 2) with he | ho
  · -- `(m+1)/2` is even, so adding the odd number `m` makes it odd.
    refine ⟨(m + 1) / 2 + m, ?_, ?_⟩
    · have hodd : Odd ((m + 1) / 2 + m) := by
        rw [Nat.odd_iff]
        omega
      have h2 : Nat.Coprime ((m + 1) / 2 + m) 4 := by
        have : Nat.Coprime ((m + 1) / 2 + m) (2 ^ 2) :=
          Nat.Coprime.pow_right 2 (Nat.coprime_two_right.mpr hodd)
        simpa using this
      have hmc : Nat.Coprime ((m + 1) / 2 + m) m := by
        have key : 2 * ((m + 1) / 2 + m) = m * 3 + 1 := by omega
        have hd1 : Nat.gcd ((m + 1) / 2 + m) m ∣ 2 * ((m + 1) / 2 + m) :=
          Dvd.dvd.mul_left (Nat.gcd_dvd_left _ _) 2
        have hd2 : Nat.gcd ((m + 1) / 2 + m) m ∣ m * 3 :=
          Dvd.dvd.mul_right (Nat.gcd_dvd_right _ _) 3
        rw [key] at hd1
        exact Nat.dvd_one.mp ((Nat.dvd_add_right hd2).mp hd1)
      exact Nat.Coprime.mul_right h2 hmc
    · have : 8 * ((m + 1) / 2 + m) = 4 + 4 * m * 3 := by omega
      rw [this, Nat.add_mul_mod_self_left]
  · refine ⟨(m + 1) / 2, ?_, ?_⟩
    · have hodd : Odd ((m + 1) / 2) := Nat.odd_iff.mpr ho
      have h2 : Nat.Coprime ((m + 1) / 2) 4 := by
        have : Nat.Coprime ((m + 1) / 2) (2 ^ 2) :=
          Nat.Coprime.pow_right 2 (Nat.coprime_two_right.mpr hodd)
        simpa using this
      have hmc : Nat.Coprime ((m + 1) / 2) m := by
        have hd1 : Nat.gcd ((m + 1) / 2) m ∣ 2 * ((m + 1) / 2) :=
          Dvd.dvd.mul_left (Nat.gcd_dvd_left _ _) 2
        have hd2 : Nat.gcd ((m + 1) / 2) m ∣ m := Nat.gcd_dvd_right _ _
        rw [hu0] at hd1
        exact Nat.dvd_one.mp ((Nat.dvd_add_right hd2).mp hd1)
      exact Nat.Coprime.mul_right h2 hmc
    · have : 8 * ((m + 1) / 2) = 4 + 4 * m * 1 := by omega
      rw [this, Nat.add_mul_mod_self_left]

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
    (hproduct : p * r * t ∣ q) : 60 ≤ q := by
  by_contra h
  have hsmall : q < 60 := by omega
  have hcount : q.primeFactors.card ≤ 2 := by
    simpa using small_four_multiple_prime_count ⟨q, hsmall⟩ hq hfour
  obtain ⟨k, hk⟩ := hproduct
  have hpd : p ∣ q := ⟨r * t * k, by rw [hk]; ring⟩
  have hrd : r ∣ q := ⟨p * t * k, by rw [hk]; ring⟩
  have htd : t ∣ q := ⟨p * r * k, by rw [hk]; ring⟩
  have hsub : ({p, r, t} : Finset ℕ) ⊆ q.primeFactors := by
    intro z hz
    simp only [Finset.mem_insert, Finset.mem_singleton] at hz
    rcases hz with rfl | rfl | rfl
    · exact hp.mem_primeFactors hpd (by omega)
    · exact hr.mem_primeFactors hrd (by omega)
    · exact ht.mem_primeFactors htd (by omega)
  have hcard : ({p, r, t} : Finset ℕ).card = 3 := by
    simp [hpr, hpt, hrt]
  have hle := Finset.card_le_card hsub
  rw [hcard] at hle
  omega

/-- Arithmetic consequence only: Szabó's displayed divisibility and the code-theoretic
`8 ∣ n` are hypotheses here, not proved in Lean. -/
theorem combined_order_lower_bound
    (n p r t : ℕ) (hn : 0 < n) (height : 8 ∣ n)
    (hp : p.Prime) (hr : r.Prime) (ht : t.Prime)
    (hpr : p ≠ r) (hpt : p ≠ t) (hrt : r ≠ t)
    (hsource : 330 * p * r * t ∣ n) : 19800 ≤ n := by
  obtain ⟨k, hk⟩ := hsource
  have hnq : n = 330 * (p * r * t * k) := by rw [hk]; ring
  have hq : 0 < p * r * t * k := by
    rcases Nat.eq_zero_or_pos (p * r * t * k) with h0 | h0
    · rw [h0] at hnq
      omega
    · exact h0
  have hfour : 4 ∣ p * r * t * k := by
    obtain ⟨j, hj⟩ := height
    omega
  have hbound :=
    quotient_ge_sixty (p * r * t * k) p r t hq hfour hp hr ht hpr hpt hrt ⟨k, rfl⟩
  omega

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

#print exists_unit_eight_mul_eq_four
#print axioms exists_unit_eight_mul_eq_four
#print quotient_ge_sixty
#print axioms quotient_ge_sixty
#print combined_order_lower_bound
#print axioms combined_order_lower_bound

end ShorArithmetic
