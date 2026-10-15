import Mathlib

namespace SemifilterElimination

universe u v

variable {Alphabet : Type u} {State : Type v}

/-- Follow a deterministic state path, consuming letters from the left. -/
def runState (step : State → Alphabet → State) : State → List Alphabet → State
  | q, [] => q
  | q, a :: w => runState step (step q a) w

/-- Exact residual mismatch at one transition, with F₂ addition as Boolean XOR. -/
def transitionError (S : State → List Alphabet → Bool)
    (step : State → Alphabet → State) (q : State) (a : Alphabet)
    (w : List Alphabet) : Bool :=
  Bool.xor (S q (a :: w)) (S (step q a) w)

/-- Sum the transition mismatches evaluated on their remaining suffixes. -/
def pathError (S : State → List Alphabet → Bool)
    (step : State → Alphabet → State) : State → List Alphabet → Bool
  | _, [] => false
  | q, a :: w => Bool.xor (transitionError S step q a w)
      (pathError S step (step q a) w)

private theorem xor_eliminate (s t f e : Bool) (h : t = Bool.xor f e) :
    s = Bool.xor f (Bool.xor (Bool.xor s t) e) := by
  cases s <;> cases t <;> cases f <;> cases e <;> simp_all

/-- Eliminate the exact inhomogeneous residual recurrence for every word length. -/
private theorem eliminate (S : State → List Alphabet → Bool)
    (step : State → Alphabet → State) (q : State) (w : List Alphabet) :
    S q w = Bool.xor (S (runState step q w) []) (pathError S step q w) := by
  induction w generalizing q with
  | nil => simp [runState, pathError]
  | cons a w ih =>
      exact xor_eliminate (S q (a :: w)) (S (step q a) w)
        (S (runState step (step q a) w) []) (pathError S step (step q a) w)
        (ih (step q a))

/-- For an arbitrary language T, arbitrary state representatives and transitions,
choosing the initial representative to be the empty word gives the exact
all-word elimination identity. No regularity or normal-form theorem is assumed.

This is the coefficient-level elimination used in proof.md (5)–(6). It does not
assert finiteness of State, membership of the errors in a semifilter complement,
or the regularity/saturation conclusions; those are separate obligations. -/
theorem residual_elimination (T : List Alphabet → Bool)
    (representative : State → List Alphabet) (step : State → Alphabet → State)
    (q₀ : State) (initial_empty : representative q₀ = []) (w : List Alphabet) :
    T w = Bool.xor (T (representative (runState step q₀ w)))
      (pathError (fun q suffix => T (representative q ++ suffix)) step q₀ w) := by
  simpa [initial_empty] using
    eliminate (fun q suffix => T (representative q ++ suffix)) step q₀ w

#print residual_elimination
#print axioms residual_elimination

end SemifilterElimination
