import CdfKernel.Target
import CdfKernel.Cert321
import CdfKernel.Cert501
import CdfKernel.Cert621
import CdfKernel.Cert681

/-!
# Audit: the four roots prove the witness-independent target

`Cdf.diffs`, `Cdf.IsCDF` and `Cdf.Target` are defined in `CdfKernel.Target`, which imports no
certificate data.  Each theorem below has type `Cdf.Target v` and is proved by the root
`Cdf.Kernel.exists_cdf{v}`.
-/

namespace Cdf.Audit

theorem target321 : Cdf.Target 321 := ⟨16, Cdf.Kernel.exists_cdf321⟩

theorem target501 : Cdf.Target 501 := ⟨25, Cdf.Kernel.exists_cdf501⟩

theorem target621 : Cdf.Target 621 := ⟨31, Cdf.Kernel.exists_cdf621⟩

theorem target681 : Cdf.Target 681 := ⟨34, Cdf.Kernel.exists_cdf681⟩

end Cdf.Audit

#print Cdf.diffs
#print Cdf.IsCDF
#print Cdf.Target
set_option pp.explicit true in
#print Cdf.diffs
#print Fin.sub
#print Cdf.Kernel.rawAt
#print Cdf.Kernel.blockOf
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.isCDF_of_check
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf321
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf501
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf621
set_option pp.funBinderTypes true in
#check @Cdf.Kernel.exists_cdf681
#check @Cdf.Audit.target321
#check @Cdf.Audit.target501
#check @Cdf.Audit.target621
#check @Cdf.Audit.target681
#print axioms Cdf.Kernel.isCDF_of_check
#print axioms Cdf.Kernel.exists_cdf321
#print axioms Cdf.Kernel.exists_cdf501
#print axioms Cdf.Kernel.exists_cdf621
#print axioms Cdf.Kernel.exists_cdf681
#print axioms Cdf.Audit.target321
#print axioms Cdf.Audit.target501
#print axioms Cdf.Audit.target621
#print axioms Cdf.Audit.target681
