import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts

example : TargetCounts 52 := by
  refine ⟨rdsqs52, isSQS_rdsqs52, ?_, ?_⟩
  · sorry
  · intro x
    constructor
    · intro T hT
      have := derived_card_three isSQS_rdsqs52 hT
      exact this
    · sorry
end Rdsqs.Kernel
