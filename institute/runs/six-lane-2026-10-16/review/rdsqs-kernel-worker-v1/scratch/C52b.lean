import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts

example (x : Fin 52) : ∀ T ∈ derivedBlocks rdsqs52 x, T.card = 3 ∧ x ∉ T :=
  fun T hT => derived_card_three isSQS_rdsqs52 hT

example (x : Fin 52) : True := by
  have h1m : ((1, 1) : ℕ × ℕ) ∈ mults52 := by
    rw [mults52_eq]
    exact List.mem_cons_self
  have hres := rdsqs52_resolutions x (1, 1) h1m
  have h1 := card_resolution_mul isSQS_rdsqs52 hres
  have h2 := card_derived_mul isSQS_rdsqs52 x
  rw [Fintype.card_fin] at h1 h2
  trace_state
  trivial
end Rdsqs.Kernel
