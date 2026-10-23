import CpcwKernel.Audit

namespace ControlUnfoldedPositive

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

theorem t122k6 : S 122 6 4 1 := Cpcw.Kernel.exists_cpcw122k6
theorem t123k6 : S 123 6 4 1 := Cpcw.Kernel.exists_cpcw123k6
theorem t124k6 : S 124 6 4 1 := Cpcw.Kernel.exists_cpcw124k6
theorem t143k5 : S 143 5 7 1 := Cpcw.Kernel.exists_cpcw143k5
theorem t144k5 : S 144 5 7 1 := Cpcw.Kernel.exists_cpcw144k5
theorem t146k5 : S 146 5 7 1 := Cpcw.Kernel.exists_cpcw146k5
theorem t162k5 : S 162 5 8 1 := Cpcw.Kernel.exists_cpcw162k5
theorem t167k5 : S 167 5 8 1 := Cpcw.Kernel.exists_cpcw167k5

end ControlUnfoldedPositive

#print axioms ControlUnfoldedPositive.t122k6
#print axioms ControlUnfoldedPositive.t123k6
#print axioms ControlUnfoldedPositive.t124k6
#print axioms ControlUnfoldedPositive.t143k5
#print axioms ControlUnfoldedPositive.t144k5
#print axioms ControlUnfoldedPositive.t146k5
#print axioms ControlUnfoldedPositive.t162k5
#print axioms ControlUnfoldedPositive.t167k5
