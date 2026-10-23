import CpcwKernel.Target
import CpcwKernel.Optimality
import CpcwKernel.Cert122k6
import CpcwKernel.Cert123k6
import CpcwKernel.Cert124k6
import CpcwKernel.Cert143k5
import CpcwKernel.Cert144k5
import CpcwKernel.Cert146k5
import CpcwKernel.Cert162k5
import CpcwKernel.Cert167k5

/-!
# Audit: the eight roots prove the witness-independent optimal-code target

`Cpcw.diffs`, `Cpcw.IsCPCW`, `Cpcw.IsOptimalCPCW`, `Cpcw.Target` and `Cpcw.OptimalTarget` are
defined in `CpcwKernel.Target`, which imports no certificate data.  Each theorem
`Cpcw.Audit.target{v}k{k}` has type `Cpcw.OptimalTarget v k`:

* existence at the bound is the root `Cpcw.Kernel.exists_cpcw{v}k{k}`
  (`∃ B : Fin n → Fin k → Fin v, Cpcw.IsOptimalCPCW B` with `n = (v - 1) / (k * (k - 1))`);
* the upper bound for every family is the data-free counting theorem `Cpcw.IsCPCW.le_bound`
  (`CpcwKernel.Optimality`).

`Cpcw.Audit.allEight` is the conjunction of the eight.
-/

namespace Cpcw.Audit

theorem target122k6 : Cpcw.OptimalTarget 122 6 :=
  ⟨⟨4, Cpcw.Kernel.exists_cpcw122k6⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target123k6 : Cpcw.OptimalTarget 123 6 :=
  ⟨⟨4, Cpcw.Kernel.exists_cpcw123k6⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target124k6 : Cpcw.OptimalTarget 124 6 :=
  ⟨⟨4, Cpcw.Kernel.exists_cpcw124k6⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target143k5 : Cpcw.OptimalTarget 143 5 :=
  ⟨⟨7, Cpcw.Kernel.exists_cpcw143k5⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target144k5 : Cpcw.OptimalTarget 144 5 :=
  ⟨⟨7, Cpcw.Kernel.exists_cpcw144k5⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target146k5 : Cpcw.OptimalTarget 146 5 :=
  ⟨⟨7, Cpcw.Kernel.exists_cpcw146k5⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target162k5 : Cpcw.OptimalTarget 162 5 :=
  ⟨⟨8, Cpcw.Kernel.exists_cpcw162k5⟩, fun _ _ h => h.le_bound (by decide)⟩

theorem target167k5 : Cpcw.OptimalTarget 167 5 :=
  ⟨⟨8, Cpcw.Kernel.exists_cpcw167k5⟩, fun _ _ h => h.le_bound (by decide)⟩

/-- **All eight frozen cases.** -/
theorem allEight :
    Cpcw.OptimalTarget 122 6 ∧ Cpcw.OptimalTarget 123 6 ∧ Cpcw.OptimalTarget 124 6 ∧
      Cpcw.OptimalTarget 143 5 ∧ Cpcw.OptimalTarget 144 5 ∧ Cpcw.OptimalTarget 146 5 ∧
      Cpcw.OptimalTarget 162 5 ∧ Cpcw.OptimalTarget 167 5 :=
  ⟨target122k6, target123k6, target124k6, target143k5, target144k5, target146k5, target162k5,
    target167k5⟩

end Cpcw.Audit

#print Cpcw.diffs
#print Cpcw.IsCPCW
#print Cpcw.IsOptimalCPCW
#print Cpcw.Target
#print Cpcw.OptimalTarget
set_option pp.explicit true in
#print Cpcw.diffs
#print Fin.sub
#print Cpcw.Kernel.rawAt
#print Cpcw.Kernel.blockOf
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.isCPCW_of_check
set_option pp.funBinderTypes true in
#check @Cpcw.IsCPCW.card_mul_le
set_option pp.funBinderTypes true in
#check @Cpcw.IsCPCW.le_bound
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw122k6
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw123k6
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw124k6
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw143k5
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw144k5
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw146k5
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw162k5
set_option pp.funBinderTypes true in
#check @Cpcw.Kernel.exists_cpcw167k5
#check @Cpcw.Audit.target122k6
#check @Cpcw.Audit.target123k6
#check @Cpcw.Audit.target124k6
#check @Cpcw.Audit.target143k5
#check @Cpcw.Audit.target144k5
#check @Cpcw.Audit.target146k5
#check @Cpcw.Audit.target162k5
#check @Cpcw.Audit.target167k5
#check @Cpcw.Audit.allEight
#print axioms Cpcw.Kernel.isCPCW_of_check
#print axioms Cpcw.IsCPCW.card_mul_le
#print axioms Cpcw.IsCPCW.le_bound
#print axioms Cpcw.Kernel.exists_cpcw122k6
#print axioms Cpcw.Kernel.exists_cpcw123k6
#print axioms Cpcw.Kernel.exists_cpcw124k6
#print axioms Cpcw.Kernel.exists_cpcw143k5
#print axioms Cpcw.Kernel.exists_cpcw144k5
#print axioms Cpcw.Kernel.exists_cpcw146k5
#print axioms Cpcw.Kernel.exists_cpcw162k5
#print axioms Cpcw.Kernel.exists_cpcw167k5
#print axioms Cpcw.Audit.target122k6
#print axioms Cpcw.Audit.target123k6
#print axioms Cpcw.Audit.target124k6
#print axioms Cpcw.Audit.target143k5
#print axioms Cpcw.Audit.target144k5
#print axioms Cpcw.Audit.target146k5
#print axioms Cpcw.Audit.target162k5
#print axioms Cpcw.Audit.target167k5
#print axioms Cpcw.Audit.allEight
