import LktsKernel.Generic
import LktsKernel.Control.Data57Swap

/-!
# Diagnostics for the swap control (altered certificate, invalid on purpose)

`controls/lkts57_control_swap.txt` changes KTS 0, CLASS 0 rows `0 19 38`, `1 7 11` of the frozen
certificate into `0 11 19`, `1 7 38`.  These kernel evaluations locate the failure, and
`swap_not_sts` proves the intended mathematical violation semantically: KTS 0 of the altered
certificate is not a Steiner triple system, because two different blocks contain the pair {0, 11}.
-/

namespace Kirkman.KernelCert.Control

open Kirkman Kirkman.KernelCert

theorem swap_rows : rowAt data57swap 0 0 0 = (0, 11, 19) ∧ rowAt data57swap 0 0 1 = (1, 7, 38) ∧
    rowAt data57swap 0 1 0 = (0, 11, 14) := by
  decide +kernel

/-- Every class of the altered KTS 0 is still a partition of the 57 points. -/
theorem swap_sys0_classes_ok : data57swapSys0.all (classOK 57) = true := by decide +kernel

/-- The class pair masks of the altered KTS 0 are not a partition of all pairs. -/
theorem swap_sys0_pairs_fail :
    accOK 0 (data57swapSys0.map (classPairs 57)) (fullPairs 57) = false := by
  decide +kernel

theorem swap_sys0_fail : sysOK 57 (fullPairs 57) data57swapSys0 = false := by decide +kernel

/-- The swapped triple `0 11 19` also occurs in another system (KTS 43), so the row fold fails. -/
theorem swap_rankFold_fails : rankFold 0 (allRows data57swap) = none := by decide +kernel

theorem swap_ok1 : rowOK 57 (0, 11, 19) = true := by decide
theorem swap_ok2 : rowOK 57 (0, 11, 14) = true := by decide
theorem swap_sub1 : ({0, 11} : Finset (Fin 57)) ⊆ rowSet 57 (0, 11, 19) := by decide
theorem swap_sub2 : ({0, 11} : Finset (Fin 57)) ⊆ rowSet 57 (0, 11, 14) := by decide

theorem swap_mem1 : (⟨rowSet 57 (0, 11, 19), card_rowSet swap_ok1⟩ : Triple 57) ∈
    blocksOf 57 data57swap ⟨0, by decide⟩ :=
  ⟨⟨0, by decide⟩, ⟨0, by decide⟩, by
    show _ = rowSet 57 (rowAt data57swap 0 0 0)
    rw [swap_rows.1]⟩

theorem swap_mem2 : (⟨rowSet 57 (0, 11, 14), card_rowSet swap_ok2⟩ : Triple 57) ∈
    blocksOf 57 data57swap ⟨0, by decide⟩ :=
  ⟨⟨1, by decide⟩, ⟨0, by decide⟩, by
    show _ = rowSet 57 (rowAt data57swap 0 1 0)
    rw [swap_rows.2.2]⟩

/-- **Intended violation.** Two different blocks of the altered KTS 0 contain the pair {0, 11}. -/
theorem swap_not_sts : ¬ IsSTS (blocksOf 57 data57swap ⟨0, by decide⟩) := by
  intro h
  have e := congrArg Subtype.val
    (sts_pair_unique _ h ⟨{0, 11}, by decide⟩ _ _ swap_mem1 swap_mem2 swap_sub1 swap_sub2)
  exact absurd (row_eq_of_rowSet_eq swap_ok1 swap_ok2 e) (by decide)

theorem swap_not_lkts : ¬ IsLKTS (blocksOf 57 data57swap) :=
  fun h => swap_not_sts (h.2.1 _).1

end Kirkman.KernelCert.Control

#print axioms Kirkman.KernelCert.Control.swap_sys0_fail
#print axioms Kirkman.KernelCert.Control.swap_rankFold_fails
#print axioms Kirkman.KernelCert.Control.swap_not_sts
#print axioms Kirkman.KernelCert.Control.swap_not_lkts
