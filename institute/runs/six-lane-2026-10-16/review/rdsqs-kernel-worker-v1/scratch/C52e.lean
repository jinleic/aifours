import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
set_option pp.explicit true
#print Rdsqs.TargetCounts
#check @isSQS_rdsqs52
#check @derived_card_three
#check @Rdsqs.IsSQS
example : TargetCounts 52 := by
  refine ⟨rdsqs52, isSQS_rdsqs52, ?_, ?_⟩
  · sorry
  · intro x
    constructor
    · intro T hT
      trace_state
      sorry
    · sorry
end Rdsqs.Kernel
