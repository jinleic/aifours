import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
set_option maxRecDepth 3000 in
set_option trace.Meta.isDefEq true in
example (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ @derivedBlocks (Fin 52) (instDecidableEqFin 52) rdsqs52 x) : T.card = 3 ∧ x ∉ T := by
  exact @derived_card_three (Fin 52) (instDecidableEqFin 52) _ isSQS_rdsqs52 x T hT
end Rdsqs.Kernel
