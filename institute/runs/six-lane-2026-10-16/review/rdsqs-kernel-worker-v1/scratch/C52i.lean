import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
theorem e1 (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 := by
  exact (derived_card_three isSQS_rdsqs52 hT).1
theorem g1 (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 :=
  (derived_card_three isSQS_rdsqs52 hT).1
theorem f1 (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 := by
  have h : IsSQS rdsqs52 := isSQS_rdsqs52
  exact (derived_card_three h hT).1
theorem h1 (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 := by
  have h := isSQS_rdsqs52
  clear_value h
  exact (derived_card_three h hT).1
end Rdsqs.Kernel
