import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Group.Nat.Defs
import Mathlib.Algebra.Group.Prod
import Mathlib.Algebra.Group.TypeTags.Basic
import Mathlib.GroupTheory.Perm.Fin

/-!
Concrete rejection control for Formal.lean's accepted-output bridge.
The four states, atom embeddings, complements, representatives, evaluation,
and residual recursion below are the same A1 × A1 construction as Formal.lean.
The deliberate mutation is `lostOutput`: it discards every emitted block.
The accepted two-edge path starts at b and reads a,b.  Its first transition
must emit a; therefore aab = Delta a, whereas the corrupted output claims
aab = Delta.  The final theorem must be rejected by the kernel.
-/

namespace ArtinNegative

def evalWord {S M : Type*} [Monoid M] (a : S → M) (w : List S) : M :=
  (w.map a).prod

structure ComplementTable (S E : Type*) where
  identity : E
  atom : S → E
  complement : E → E → E
  rho : E → List S

namespace ComplementTable
variable {S E : Type*}
def next (T : ComplementTable S E) (e : E) (y : S) : E := T.complement (T.atom y) e
def emit (T : ComplementTable S E) (e : E) (y : S) : List S :=
  T.rho (T.complement e (T.atom y))
def residual (T : ComplementTable S E) (e : E) : List S → E
  | [] => e
  | y :: v => residual T (T.next e y) v
def output (T : ComplementTable S E) (e : E) : List S → List S
  | [] => []
  | y :: v => T.emit e y ++ output T (T.next e y) v
def lostOutput (T : ComplementTable S E) (e : E) : List S → List S
  | [] => []
  | y :: v => lostOutput T (T.next e y) v
end ComplementTable

abbrev E := Bool × Bool
abbrev M := Multiplicative (ℕ × ℕ)
def table : ComplementTable Bool E where
  identity := (false, false)
  atom y := if y then (false, true) else (true, false)
  complement u v := (v.1 && !u.1, v.2 && !u.2)
  rho e := (if e.1 then [false] else []) ++ (if e.2 then [true] else [])
def value (e : E) : M := Multiplicative.ofAdd
  ((if e.1 then 1 else 0), (if e.2 then 1 else 0))
def atom (y : Bool) : M := if y then Multiplicative.ofAdd (0, 1)
  else Multiplicative.ofAdd (1, 0)

theorem local_balance_is_valid : ∀ u v, value u * value (table.complement u v) =
    value v * value (table.complement v u) := by
  rintro ⟨u₁, u₂⟩ ⟨v₁, v₂⟩
  cases u₁ <;> cases u₂ <;> cases v₁ <;> cases v₂ <;> decide

theorem actual_path_accepts :
    table.residual (table.complement (table.atom false) (true, true)) [false, true] =
      table.identity := by decide

theorem correct_output_is_valid :
    evalWord atom [false, false, true] = value (true, true) * evalWord atom
      (table.rho (table.complement (true, true) (table.atom false)) ++
        table.output (table.complement (table.atom false) (true, true)) [false, true]) := by decide

set_option pp.proofs false
#print ArtinNegative.local_balance_is_valid
#print axioms ArtinNegative.local_balance_is_valid
#print ArtinNegative.actual_path_accepts
#print axioms ArtinNegative.actual_path_accepts
#print ArtinNegative.correct_output_is_valid
#print axioms ArtinNegative.correct_output_is_valid

/-- Deliberately false: the accepted rule's essential loop output has vanished. -/
theorem dropped_output_valid :
    evalWord atom [false, false, true] = value (true, true) * evalWord atom
      (table.rho (table.complement (true, true) (table.atom false)) ++
        table.lostOutput (table.complement (table.atom false) (true, true)) [false, true]) := by decide

end ArtinNegative

namespace ArtinNegativeOrder

def atom (y : Bool) : Equiv.Perm (Fin 3) :=
  if y then Equiv.swap 1 2 else Equiv.swap 0 1

theorem actual_braid_relation :
    ArtinNegative.evalWord atom [false, true, false] =
      ArtinNegative.evalWord atom [true, false, true] := by decide

theorem actual_accepted_output :
    ArtinNegative.evalWord atom [true, false, false, false, true, false] =
      ArtinNegative.evalWord atom [false, true, false, false, true, true] := by decide

#print ArtinNegativeOrder.actual_braid_relation
#print axioms ArtinNegativeOrder.actual_braid_relation
#print ArtinNegativeOrder.actual_accepted_output
#print axioms ArtinNegativeOrder.actual_accepted_output

/-- Deliberately wrong: reverse the two nonempty emissions ab,b to b,ab.
The initial output aba is unchanged. The two words have the same total length. -/
theorem reversed_blocks_valid :
    ArtinNegative.evalWord atom [true, false, false, false, true, false] =
      ArtinNegative.evalWord atom [false, true, false, true, false, true] := by decide

end ArtinNegativeOrder
