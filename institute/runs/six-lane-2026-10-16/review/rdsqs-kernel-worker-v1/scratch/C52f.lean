import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
#synth DecidableEq (Fin 52)
set_option pp.explicit true in
#check @rdsqs52
set_option pp.explicit true in
#print rdsqs52
example (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ @derivedBlocks (Fin 52) (instDecidableEqFin 52) rdsqs52 x) : T.card = 3 ∧ x ∉ T := by
  exact @derived_card_three (Fin 52) (instDecidableEqFin 52) _ isSQS_rdsqs52 x T hT
end Rdsqs.Kernel
