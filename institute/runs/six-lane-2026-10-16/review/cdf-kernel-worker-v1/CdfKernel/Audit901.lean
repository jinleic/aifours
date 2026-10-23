import CdfKernel.Target
import CdfKernel.Cert901

/-!
# Audit: the separate 901 root proves the witness-independent target

Same target and generic checker as the four original orders (`CdfKernel.Audit`); the 901 data and
certificate modules were added afterwards and change no earlier module.
-/

namespace Cdf.Audit

theorem target901 : Cdf.Target 901 := ⟨45, Cdf.Kernel.exists_cdf901⟩

end Cdf.Audit

#print Cdf.IsCDF
#print Cdf.Target
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf901
#check @Cdf.Audit.target901
#print axioms Cdf.Kernel.exists_cdf901
#print axioms Cdf.Audit.target901
