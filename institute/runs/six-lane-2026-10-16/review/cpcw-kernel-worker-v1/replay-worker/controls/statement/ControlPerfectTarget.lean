import CpcwKernel.Audit

namespace ControlPerfectTarget

/-- Spelled out without any `Cpcw` definition: `n` injective maps `Fin k → Fin v` whose ordered
differences (subtraction in `Fin v`) give every nonzero residue at most `c` times and `0` never,
and `n = (v - 1) / (k * (k - 1))`.  Nested exactly as `Cpcw.IsOptimalCPCW`. -/
def S (v k n c : Nat) : Prop :=
  ∃ B : Fin n → Fin k → Fin v,
    ((∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
      (∀ d : Fin v, d.val ≠ 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d ≤ c) ∧
      (∀ d : Fin v, d.val = 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)) ∧
    n = (v - 1) / (k * (k - 1))

/-- The same with every nonzero residue exactly once (a perfect code / cyclic difference family). -/
def SPerfect (v k n : Nat) : Prop :=
  ∃ B : Fin n → Fin k → Fin v,
    ((∀ i : Fin n, ∀ j l : Fin k, B i j = B i l → j = l) ∧
      (∀ d : Fin v, d.val ≠ 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 1) ∧
      (∀ d : Fin v, d.val = 0 →
        (((Finset.univ : Finset (Fin n × Fin k × Fin k)).filter fun t => t.2.1 ≠ t.2.2).val.map
          fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)) ∧
    n = (v - 1) / (k * (k - 1))

theorem t : SPerfect 122 6 4 := Cpcw.Kernel.exists_cpcw122k6

end ControlPerfectTarget
