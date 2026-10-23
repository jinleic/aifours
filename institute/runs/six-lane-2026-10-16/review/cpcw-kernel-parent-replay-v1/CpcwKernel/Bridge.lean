import CpcwKernel.Facts
import CpcwKernel.Audit

/-!
# Kernel-checked bridges for the eight concrete cases

Corollaries only: each theorem applies the data-free `Cpcw.bridge_of_target` (`CpcwKernel.Facts`)
to an audited root.  For each case the family is an optimal `(v, k, 1)` CPCW code in the difference
form (`Cpcw.IsOptimalCPCW`), satisfies the correlation form of Definition 1 of the primary source
(`Cpcw.IsCorrelationCPCW`), has pairwise distinct codewords, never uses the difference `v / 2` (for
even `v`), and develops into a strictly cyclic packing (`Cpcw.IsStrictlyCyclicPacking`).
-/

namespace Cpcw.Bridge

open Cpcw

theorem bridge122k6 : ∃ n : ℕ, ∃ B : Fin n → Fin 6 → Fin 122,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 122, 2 * e.val = 122 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target122k6.1

theorem bridge123k6 : ∃ n : ℕ, ∃ B : Fin n → Fin 6 → Fin 123,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 123, 2 * e.val = 123 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target123k6.1

theorem bridge124k6 : ∃ n : ℕ, ∃ B : Fin n → Fin 6 → Fin 124,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 124, 2 * e.val = 124 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target124k6.1

theorem bridge143k5 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 143,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 143, 2 * e.val = 143 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target143k5.1

theorem bridge144k5 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 144,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 144, 2 * e.val = 144 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target144k5.1

theorem bridge146k5 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 146,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 146, 2 * e.val = 146 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target146k5.1

theorem bridge162k5 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 162,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 162, 2 * e.val = 162 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target162k5.1

theorem bridge167k5 : ∃ n : ℕ, ∃ B : Fin n → Fin 5 → Fin 167,
    IsOptimalCPCW B ∧ IsCorrelationCPCW B ∧ Function.Injective (codeword B) ∧
      (∀ e : Fin 167, 2 * e.val = 167 → (diffs B).count e = 0) ∧ IsStrictlyCyclicPacking B :=
  bridge_of_target (by decide) Cpcw.Audit.target167k5.1

end Cpcw.Bridge

#print Cpcw.codeword
#print Cpcw.translate
#print Cpcw.IsCorrelationCPCW
#print Cpcw.devBlock
#print Cpcw.IsStrictlyCyclicPacking
#check @Cpcw.sub_eq_iff_modEq
#check @Cpcw.isCPCW_iff_diff_injective
#check @Cpcw.isCPCW_iff_correlation
#check @Cpcw.IsCPCW.codeword_injective
#check @Cpcw.IsCPCW.count_half
#check @Cpcw.IsCPCW.packing
#check @Cpcw.bridge_of_target
#check @Cpcw.not_exists_of_bound_lt
#check @Cpcw.card_mul_eq_of_perfect
#print axioms Cpcw.sub_eq_iff_modEq
#print axioms Cpcw.isCPCW_iff_diff_injective
#print axioms Cpcw.isCPCW_iff_correlation
#print axioms Cpcw.IsCPCW.codeword_injective
#print axioms Cpcw.IsCPCW.count_half
#print axioms Cpcw.IsCPCW.packing
#print axioms Cpcw.bridge_of_target
#print axioms Cpcw.not_exists_of_bound_lt
#print axioms Cpcw.card_mul_eq_of_perfect
#print axioms Cpcw.Bridge.bridge122k6
#print axioms Cpcw.Bridge.bridge123k6
#print axioms Cpcw.Bridge.bridge124k6
#print axioms Cpcw.Bridge.bridge143k5
#print axioms Cpcw.Bridge.bridge144k5
#print axioms Cpcw.Bridge.bridge146k5
#print axioms Cpcw.Bridge.bridge162k5
#print axioms Cpcw.Bridge.bridge167k5
