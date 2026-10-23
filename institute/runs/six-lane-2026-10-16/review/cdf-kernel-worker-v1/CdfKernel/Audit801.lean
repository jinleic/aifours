import CdfKernel.Target
import CdfKernel.Cert801

/-!
# Audit: the separate 801 root proves the witness-independent target

Same target and generic checker as the four original orders (`CdfKernel.Audit`); the 801 data and
certificate modules were added afterwards and change no earlier module.
-/

namespace Cdf.Audit

theorem target801 : Cdf.Target 801 := ⟨40, Cdf.Kernel.exists_cdf801⟩

end Cdf.Audit

#print Cdf.IsCDF
#print Cdf.Target
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf801
#check @Cdf.Audit.target801
#print axioms Cdf.Kernel.exists_cdf801
#print axioms Cdf.Audit.target801
