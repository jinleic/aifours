import LktsKernel.AuditTarget
import LktsKernel.Cert57
import LktsKernel.Cert87

namespace Kirkman.Audit

theorem exists57 : Target 57 := Kirkman.KernelCert.exists_lkts57

theorem exists87 : Target 87 := Kirkman.KernelCert.exists_lkts87

end Kirkman.Audit

#print Kirkman.Audit.Target
#check @Kirkman.Audit.exists57
#check @Kirkman.Audit.exists87
#print axioms Kirkman.Audit.exists57
#print axioms Kirkman.Audit.exists87
