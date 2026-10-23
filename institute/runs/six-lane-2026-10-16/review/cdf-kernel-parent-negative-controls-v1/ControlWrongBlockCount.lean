import CdfKernel.Cert321
import CdfKernel.Cert801
import CdfKernel.Cert901

namespace NegControlWrongBlockCount

def S (v n : Nat) (c : Nat) : Prop :=
  ∃ B : Fin n → Fin 5 → Fin v,
    (∀ i : Fin n, ∀ j k : Fin 5, B i j = B i k → j = k) ∧
    (∀ d : Fin v, d.val ≠ 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = c) ∧
    (∀ d : Fin v, d.val = 0 →
      (((Finset.univ : Finset (Fin n × Fin 5 × Fin 5)).filter fun t => t.2.1 ≠ t.2.2).val.map
        fun t => B t.1 t.2.1 - B t.1 t.2.2).count d = 0)

theorem t : S 321 17 1 := Cdf.Kernel.exists_cdf321

end NegControlWrongBlockCount
