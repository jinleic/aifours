import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
-- (a) term mode
example (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 ∧ x ∉ T :=
  derived_card_three isSQS_rdsqs52 hT
-- (c) abstract B
example (B : Finset (Finset (Fin 52))) (hB : IsSQS B) (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks B x) : T.card = 3 ∧ x ∉ T :=
  derived_card_three hB hT
-- (d) generic lemma with have
theorem tst (x : Fin 52) (T : Finset (Fin 52)) (hT : T ∈ derivedBlocks rdsqs52 x) : T.card = 3 := by
  have h := isSQS_rdsqs52
  exact (derived_card_three h hT).1
end Rdsqs.Kernel
