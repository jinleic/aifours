import LktsKernel.PriorFormal

/- The target is elaborated before importing either generated certificate module. -/
namespace Kirkman.Audit

def Target (v : Nat) : Prop :=
  ∃ B : Fin (v - 2) → Kirkman.Blocks v, Kirkman.IsLKTS B

end Kirkman.Audit
