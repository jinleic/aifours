import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts

theorem t1 : TargetCounts 52 := by
  have h1m : ((1, 1) : ℕ × ℕ) ∈ mults52 := by
    rw [mults52_eq]
    exact List.mem_cons_self
  have hres := fun x : Fin 52 => rdsqs52_resolutions x 1 1 h1m
  refine ⟨rdsqs52, isSQS_rdsqs52, ?_, ?_⟩
  · sorry
  · intro x
    refine ⟨fun T hT => derived_card_three isSQS_rdsqs52 hT, ?_, ?_⟩
    · sorry
    · refine ⟨resAt 52 data52 1 x, hres x, ?_, ?_⟩
      · sorry
      · sorry
end Rdsqs.Kernel
