import Mathlib.Data.List.Basic

/-
A kernel-evaluated certificate for every minimal overlap of the seven
noncommutative tridendriform rules. This proves the finite symbolic calculation,
not the general diamond lemma, the order's admissibility, or the book-to-operad
translation. Those independent all-arity arguments are in ../proof.md.

Each polynomial is a list of signed integer multiples of labelled binary trees.
Equality checks every term in the union of both supports. No finite-field
arithmetic, external evaluator, or numerical approximation is used.
-/
namespace TrialgebraCritical

inductive Op where
  | dot | prec | succ
  deriving DecidableEq, Repr

inductive Tree where
  | leaf : Nat → Tree
  | node : Op → Tree → Tree → Tree
  deriving DecidableEq, Repr

abbrev Poly := List (Int × Tree)

open Op Tree

def ops : List Op := [dot, prec, succ]

def forbidden (outer inner : Op) : Bool :=
  match outer, inner with
  | prec, _ | dot, _ | succ, succ => true
  | _, _ => false

/-- These are precisely the seven book identities, oriented as in Lemma 6.1. -/
def rootRule : Tree → Option Poly
  | node prec (node prec a b) c =>
      some [(1, node prec a (node dot b c)),
            (1, node prec a (node prec b c)),
            (1, node prec a (node succ b c))]
  | node prec (node succ a b) c => some [(1, node succ a (node prec b c))]
  | node prec (node dot a b) c => some [(1, node dot a (node prec b c))]
  | node dot (node prec a b) c => some [(1, node dot a (node succ b c))]
  | node dot (node succ a b) c => some [(1, node succ a (node dot b c))]
  | node dot (node dot a b) c => some [(1, node dot a (node dot b c))]
  | node succ (node succ a b) c =>
      some [(1, node succ a (node succ b c)),
            (-1, node succ (node prec a b) c),
            (-1, node succ (node dot a b) c)]
  | _ => none

/-- One actual contextual reduction, prioritizing root then left then right. -/
def step : Tree → Option Poly
  | leaf _ => none
  | node op l r =>
      match rootRule (node op l r) with
      | some p => some p
      | none =>
          match step l with
          | some p => some (p.map fun (c, t) => (c, node op t r))
          | none =>
              match step r with
              | some p => some (p.map fun (c, t) => (c, node op l t))
              | none => none

/-- Bounded iteration only; successful checks also require irreducible output. -/
def reduce : Nat → Tree → Poly
  | 0, t => [(1, t)]
  | fuel + 1, t =>
      match step t with
      | none => [(1, t)]
      | some p => p.flatMap fun (c, u) =>
          (reduce fuel u).map fun (d, v) => (c*d, v)

def reducePoly (p : Poly) : Poly :=
  p.flatMap fun (c, t) => (reduce 20 t).map fun (d, u) => (c*d, u)

def coefficient (t : Tree) (p : Poly) : Int :=
  (p.map fun (c, u) => if t = u then c else 0).sum

def polyEq (p q : Poly) : Bool :=
  (p ++ q).all fun (_, t) => coefficient t p == coefficient t q

def irreducible (p : Poly) : Bool :=
  p.all fun (_, t) => (step t).isNone

/-- top, middle, bottom operation labels of a three-vertex left comb. -/
def criticalTriples : List (Op × Op × Op) :=
  ops.flatMap fun top => ops.flatMap fun middle =>
    (ops.filter fun bottom => forbidden top middle && forbidden middle bottom).map
      fun bottom => (top, middle, bottom)

/-- The two one-step branches followed by actual integer-linear reductions. -/
def checkTriple (triple : Op × Op × Op) : Bool :=
  let (top, middle, bottom) := triple
  let l := node middle (node bottom (leaf 0) (leaf 1)) (leaf 2)
  let t := node top l (leaf 3)
  match rootRule t, rootRule l with
  | some outerBranch, some inner =>
      let innerBranch := inner.map fun (c, u) => (c, node top u (leaf 3))
      let p := reducePoly outerBranch
      let q := reducePoly innerBranch
      polyEq p q && irreducible p && irreducible q
  | _, _ => false

set_option maxRecDepth 8192 in
set_option maxHeartbeats 8000000 in
/-- All fifteen symbolic minimal critical peaks join with irreducible output. -/
theorem all_critical_pairs_join :
    criticalTriples.length = 15 ∧ criticalTriples.all checkTriple = true := by
  decide

#print all_critical_pairs_join
#print axioms all_critical_pairs_join

end TrialgebraCritical
