-- SUPERSEDED DRAFT (2026-10-14 PT): replaced by work/ShorArithmetic.lean. Retained only as
-- history for evidence/quotient-bound-lean*.log; not a delivered root.
import Mathlib.Data.Nat.PrimeFin
import Mathlib.Tactic.Simproc.Factors
import Mathlib.Tactic

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

namespace ShorArithmetic

private theorem small_four_multiple_prime_count :
    ∀ q : Fin 60, 0 < q.val → 4 ∣ q.val → q.val.primeFactors.card ≤ 2 := by
  intro q hpos hfour
  fin_cases q <;> simp [Nat.primeFactors, -Nat.toFinset_factors, Nat.primeFactorsList_ofNat] at *

/-- The three primes may equal 2, 3, 5, or 11; only pairwise distinctness is assumed. -/
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
  have hpd : p ∣ q := by
    refine ⟨r * t * k, ?_⟩
    rw [hk]
    ring
  have hrd : r ∣ q := by
    refine ⟨p * t * k, ?_⟩
    rw [hk]
    ring
  have htd : t ∣ q := by
    refine ⟨p * r * k, ?_⟩
    rw [hk]
    ring
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

/-- Arithmetic consequence only: the source theorem and the code-theoretic 8-divisor
are hypotheses, not formalized here. No assumption that the primes are new is made. -/
theorem combined_order_lower_bound
    (n p r t : ℕ) (hn : 0 < n) (height : 8 ∣ n)
    (hp : p.Prime) (hr : r.Prime) (ht : t.Prime)
    (hpr : p ≠ r) (hpt : p ≠ t) (hrt : r ≠ t)
    (hsource : 330 * p * r * t ∣ n) : 19800 ≤ n := by
  obtain ⟨k, hk⟩ := hsource
  let q := p * r * t * k
  have hnq : n = 330 * q := by
    dsimp [q]
    rw [hk]
    ring
  have hq : 0 < q := by omega
  have hfour : 4 ∣ q := by
    obtain ⟨j, hj⟩ := height
    omega
  have hproduct : p * r * t ∣ q := ⟨k, rfl⟩
  have hbound := quotient_ge_sixty q p r t hq hfour hp hr ht hpr hpt hrt hproduct
  omega

#print quotient_ge_sixty
#print axioms quotient_ge_sixty
#print combined_order_lower_bound
#print axioms combined_order_lower_bound

end ShorArithmetic
