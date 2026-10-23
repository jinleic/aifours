import CdfKernel.Cert321
import CdfKernel.Cert501
import CdfKernel.Cert621
import CdfKernel.Cert681
import CdfKernel.Cert801
import CdfKernel.Cert901

/-! Parent-authored audit statements (written by the integration parent, 2026-10-17).
The proposition is spelled out from the definition of a cyclic (v,5,1) difference family:
n maps Fin 5 → Fin v that are injective, whose ordered within-block differences (subtraction in
Fin v, i.e. modulo v) contain every nonzero residue exactly once and the residue 0 never.
It does not mention `Cdf.IsCDF`, `Cdf.diffs` or `Cdf.Target`; the kernel must unfold those to accept
each worker root as a proof of this statement. -/

namespace ParentCdfAudit

def ParentStatement (v n : Nat) : Prop :=
  ∃ B : Fin n → Fin 5 → Fin v,
    (∀ i : Fin n, ∀ j k : Fin 5, B i j = B i k → j = k) ∧
    (∀ d : Fin v, d.val ≠ 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 1) ∧
    (∀ d : Fin v, d.val = 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)

theorem cdf321 : ParentStatement 321 16 := Cdf.Kernel.exists_cdf321
theorem cdf501 : ParentStatement 501 25 := Cdf.Kernel.exists_cdf501
theorem cdf621 : ParentStatement 621 31 := Cdf.Kernel.exists_cdf621
theorem cdf681 : ParentStatement 681 34 := Cdf.Kernel.exists_cdf681
theorem cdf801 : ParentStatement 801 40 := Cdf.Kernel.exists_cdf801
theorem cdf901 : ParentStatement 901 45 := Cdf.Kernel.exists_cdf901

end ParentCdfAudit

#print axioms ParentCdfAudit.cdf321
#print axioms ParentCdfAudit.cdf501
#print axioms ParentCdfAudit.cdf621
#print axioms ParentCdfAudit.cdf681
#print axioms ParentCdfAudit.cdf801
#print axioms ParentCdfAudit.cdf901
