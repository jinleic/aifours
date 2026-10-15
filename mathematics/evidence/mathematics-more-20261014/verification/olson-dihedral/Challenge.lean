import Mathlib

/- A reproduction of the known odd-dihedral lower bound, NOT a refutation
   of Olson's 2|G|-1 conjecture. The word below has length 2|G|-2. -/
namespace OlsonPartial

open DihedralGroup

def oddDihedralWord (m : ℕ) : List (DihedralGroup m) :=
  List.replicate (2 * m - 1) (r 1) ++ List.replicate (2 * m - 1) (sr 0)

private theorem two_block_product_ne_one (m : ℕ) [NeZero m] (hm : Odd m)
    (k l : ℕ) (hk : k ≤ 2 * m - 1) (hl : l ≤ 2 * m - 1)
    (hlen : k + l = 2 * m) :
    (r 1 : DihedralGroup m) ^ k * (sr 0) ^ l ≠ 1 := by
  intro hprod
  have mpos : 0 < m := NeZero.pos m
  have kpos : 0 < k := by omega
  have klimit : k < 2 * m := by omega
  have heven : l % 2 = 0 := by
    by_contra h
    have hmod : l % 2 = 1 := by omega
    have hspow : (sr 0 : DihedralGroup m) ^ l = sr 0 := by
      rw [← pow_mod_orderOf, orderOf_sr, hmod, pow_one]
    simp only [r_one_pow, hspow, r_mul_sr, one_def] at hprod
    cases hprod
  have hspow : (sr 0 : DihedralGroup m) ^ l = 1 := by
    rw [← pow_mod_orderOf, orderOf_sr, heven, pow_zero]
  have hrpow : (r 1 : DihedralGroup m) ^ k = 1 := by
    simpa only [hspow, mul_one] using hprod
  have hdiv : m ∣ k := by
    simpa only [orderOf_r_one] using orderOf_dvd_of_pow_eq_one hrpow
  obtain ⟨d, hd⟩ := hdiv
  have dpos : 0 < d := by
    by_contra h
    have dzero : d = 0 := by omega
    simp only [dzero, mul_zero] at hd
    omega
  have dle : d ≤ 1 := by nlinarith
  have deq : d = 1 := by omega
  have keq : k = m := by simpa only [deq, mul_one] using hd
  have hodd : m % 2 = 1 := Nat.odd_iff.mp hm
  omega

/-- For every odd m, the dihedral group of order 2m has a word of length
    2|G|-2 with no |G|-term identity-product ordered sublist. This is a sharp
    lower-bound witness, one term shorter than the conjecture's premise. -/
theorem odd_dihedral_sharp_lower_bound (m : ℕ) [NeZero m] (hm : Odd m) :
    Fintype.card (DihedralGroup m) = 2 * m ∧
    (oddDihedralWord m).length = 2 * Fintype.card (DihedralGroup m) - 2 ∧
    ∀ ys : List (DihedralGroup m), ys.Sublist (oddDihedralWord m) →
      ys.length = Fintype.card (DihedralGroup m) → ys.prod ≠ 1 := by sorry

end OlsonPartial
