import CpcwKernel.Audit

namespace Probe
open Cpcw.Kernel

def dataMut : List (List Nat) := [[0, 1, 3, 21, 59, 112], [0, 4, 10, 27, 40, 75], [0, 5, 34, 42, 67, 83], [0, 7, 22, 31, 50, 76]]

theorem mut_check : check 122 6 4 dataMut = true := by decide +kernel

def hdr : Nat × Nat := (123, 6)
theorem hdr_ok : hdr = (122, 6) := rfl

def S (v k n : Nat) : Prop :=
  ∃ B : Fin n → Fin k → Fin v,
    ((∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
      (∀ d : Fin v, d.val ≠ 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d ≤ 1) ∧
      (∀ d : Fin v, d.val = 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)) ∧
    n = (v - 1) / (k * (k - 1))

theorem pos : S 122 6 4 := Cpcw.Kernel.exists_cpcw122k6
theorem neg : S 123 6 4 := Cpcw.Kernel.exists_cpcw122k6

end Probe
