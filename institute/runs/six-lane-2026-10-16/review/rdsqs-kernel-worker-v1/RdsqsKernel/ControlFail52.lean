import RdsqsKernel.Controls52

/-!
# Negative control: this module must FAIL to build

The full pipeline run on the corrupted seed `Controls.data52swap` (points `26` and `15` exchanged
between the first two triples of `CLASS 0`): the kernel evaluation of `seedCheck` returns
`false`, so `swap_seedCheck_true` is rejected, and nothing about the corrupted data can be
derived without `sorryAx`.  No root depends on this module.
-/

namespace Rdsqs.Kernel.Controls

open Rdsqs.Kernel

theorem swap_seedCheck_true : seedCheck 52 data52swap = true := by
  decide +kernel

theorem swap_isRDSQS : Rdsqs.IsRDSQS (blocks 52 data52swap) :=
  isRDSQS_of_check swap_seedCheck_true

end Rdsqs.Kernel.Controls

#print axioms Rdsqs.Kernel.Controls.swap_isRDSQS
