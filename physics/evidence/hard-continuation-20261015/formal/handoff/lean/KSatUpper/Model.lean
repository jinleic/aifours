import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Prod
import Mathlib.Topology.Order.Basic

/-! The uniform random k-SAT model with distinct variables in every clause.

Derived from `SatUpper/Model.lean` of yamelton/sat-upper-4268 (Apache-2.0), whose
clauses have the hard-coded arity three. Here the arity `k` is a parameter.

A clause has `k` ordered, distinct variable positions and independent Boolean
falsifying signs. Every unordered legal signed clause has exactly `k!` such
representations, so the uniform law on this type is the uniform law on legal
signed clauses. Formulas are ordered lists of independently chosen clauses;
repeated clauses are allowed. Probability is a ratio of finite cardinalities,
avoiding any implicit choice of probability measure.

For `n < k` there are no legal clauses. The ratio then uses Lean's convention
for division by zero; these finitely many indices do not affect a limit. -/

namespace KSatUpper

abbrev Assignment (n : ℕ) := Fin n → Bool

abbrev Clause (k n : ℕ) :=
  {v : Fin k → Fin n // Function.Injective v} × (Fin k → Bool)

abbrev Formula (k n M : ℕ) := Fin M → Clause k n

/-- `σ` violates the clause iff every literal is falsified: the clause stores the
falsifying value of each of its variables. -/
def Violates {k n : ℕ} (σ : Assignment n) (c : Clause k n) : Prop :=
  ∀ j : Fin k, σ (c.1.val j) = c.2 j

def Satisfies {k n M : ℕ} (σ : Assignment n) (F : Formula k n M) : Prop :=
  ∀ i : Fin M, ¬ Violates σ (F i)

def Satisfiable {k n M : ℕ} (F : Formula k n M) : Prop :=
  ∃ σ : Assignment n, Satisfies σ F

/-- The probability that `M` iid uniform legal signed `k`-clauses on `n` variables
form a satisfiable formula. -/
noncomputable def satisfiabilityProbability (k n M : ℕ) : ℝ := by
  classical
  exact ((Finset.univ.filter (fun F : Formula k n M => Satisfiable F)).card : ℝ) /
    (Fintype.card (Formula k n M) : ℝ)

end KSatUpper
