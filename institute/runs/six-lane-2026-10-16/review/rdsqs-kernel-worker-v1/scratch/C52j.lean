import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
set_option diagnostics true in
set_option diagnostics.threshold 20 in
theorem e1 (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 := by
  exact (derived_card_three isSQS_rdsqs52 hT).1
end Rdsqs.Kernel
