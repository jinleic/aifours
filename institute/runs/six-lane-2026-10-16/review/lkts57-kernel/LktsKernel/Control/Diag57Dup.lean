import LktsKernel.Generic
import LktsKernel.Control.Data57Dup

/-!
# Diagnostics for the duplicated-system control (altered certificate, invalid on purpose)

`controls/lkts57_control_dupsys.txt` replaces the classes of KTS 54 of the frozen certificate by a
verbatim copy of those of KTS 0.  The copied system still passes the per-system check, the row fold
rejects the certificate, and `dup_not_lkts` proves the intended mathematical violation: the
constituents are not pairwise disjoint.
-/

namespace Kirkman.KernelCert.Control

open Kirkman Kirkman.KernelCert

theorem dup_rows : rowAt data57dup 0 0 0 = (0, 19, 38) ∧ rowAt data57dup 54 0 0 = (0, 19, 38) := by
  decide +kernel

/-- The copied KTS 54 is still a genuine KTS(57) as far as the per-system check is concerned. -/
theorem dup_sys54_ok : sysOK 57 (fullPairs 57) data57dupSys54 = true := by decide +kernel

/-- The row fold over the whole altered certificate fails. -/
theorem dup_rankFold_fails : rankFold 0 (allRows data57dup) = none := by decide +kernel

theorem dup_ok : rowOK 57 (0, 19, 38) = true := by decide

theorem dup_mem0 : (⟨rowSet 57 (0, 19, 38), card_rowSet dup_ok⟩ : Triple 57) ∈
    blocksOf 57 data57dup ⟨0, by decide⟩ :=
  ⟨⟨0, by decide⟩, ⟨0, by decide⟩, by
    show _ = rowSet 57 (rowAt data57dup 0 0 0)
    rw [dup_rows.1]⟩

theorem dup_mem54 : (⟨rowSet 57 (0, 19, 38), card_rowSet dup_ok⟩ : Triple 57) ∈
    blocksOf 57 data57dup ⟨54, by decide⟩ :=
  ⟨⟨0, by decide⟩, ⟨0, by decide⟩, by
    show _ = rowSet 57 (rowAt data57dup 54 0 0)
    rw [dup_rows.2]⟩

/-- **Intended violation.** Constituents 0 and 54 share a block. -/
theorem dup_not_disjoint :
    ¬ Disjoint (blocksOf 57 data57dup ⟨0, by decide⟩) (blocksOf 57 data57dup ⟨54, by decide⟩) :=
  fun h => Set.disjoint_left.mp h dup_mem0 dup_mem54

theorem dup_not_lkts : ¬ IsLKTS (blocksOf 57 data57dup) :=
  fun h => dup_not_disjoint (h.2.2.1 (by decide))

end Kirkman.KernelCert.Control

#print axioms Kirkman.KernelCert.Control.dup_sys54_ok
#print axioms Kirkman.KernelCert.Control.dup_rankFold_fails
#print axioms Kirkman.KernelCert.Control.dup_not_lkts
