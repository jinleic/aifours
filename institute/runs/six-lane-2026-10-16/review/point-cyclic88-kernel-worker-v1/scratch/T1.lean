import Mathlib.Data.ZMod.Basic

abbrev G := ZMod 88

example : Decidable (∀ d : G, d = d) := inferInstance
example : Decidable (∀ i < 5, ∀ j < 5, i ≠ j → i = i) := inferInstance
example (d : G) : Decidable (∀ i < 5, ∀ j < 5, i ≠ j → ((i : ℕ) : G) * d = ((j : ℕ) : G) * d → d = 0) := inferInstance
example : Decidable (∀ d : G, ∀ i : Fin 5, ∀ j : Fin 5, i ≠ j → ((i : ℕ) : G) * d = ((j : ℕ) : G) * d → d = 0 ∨ d = 22 ∨ d = 44 ∨ d = 66) := inferInstance

set_option profiler true in
theorem t1 : ∀ d : G, ∀ i : Fin 5, ∀ j : Fin 5, i ≠ j → ((i : ℕ) : G) * d = ((j : ℕ) : G) * d → d = 0 ∨ d = 22 ∨ d = 44 ∨ d = 66 := by
  decide
