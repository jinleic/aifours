import RdsqsKernel.Cert52
namespace Rdsqs.Kernel
open Rdsqs.Generic Rdsqs.Counts
set_option maxRecDepth 2000 in
/-- The existence statement with every forced count written out. -/
theorem counts_rdsqs52 : TargetCounts 52 := by
  have h1m : ((1, 1) : ℕ × ℕ) ∈ mults52 := by
    rw [mults52_eq]
    exact List.mem_cons_self
  have hres := fun x : Fin 52 => rdsqs52_resolutions x (1, 1) h1m
  refine ⟨rdsqs52, isSQS_rdsqs52, ?_, fun x => ⟨fun T hT => derived_card_three isSQS_rdsqs52 hT,
    ?_, resAt 52 data52 1 x, hres x, ?_, ?_⟩⟩
  · have h := card_blocks_mul isSQS_rdsqs52
    rw [Fintype.card_fin] at h
    have hc : Nat.choose 52 3 = 22100 := by decide +kernel
    omega
  · have h := card_derived_mul isSQS_rdsqs52 x
    rw [Fintype.card_fin] at h
    have hc : Nat.choose (52 - 1) 2 = 1275 := by decide +kernel
    omega
  · have h1 := card_resolution_mul isSQS_rdsqs52 (hres x)
    have h2 := card_derived_mul isSQS_rdsqs52 x
    rw [Fintype.card_fin] at h1 h2
    have hc : Nat.choose (52 - 1) 2 = 1275 := by decide +kernel
    omega
  · intro P hP
    have h := card_class_mul isSQS_rdsqs52 ((hres x).1 P hP)
    rw [Fintype.card_fin] at h
    omega

end Rdsqs.Kernel
