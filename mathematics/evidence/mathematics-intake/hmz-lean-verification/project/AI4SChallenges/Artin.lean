import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Group.Nat.Defs
import Mathlib.Algebra.Group.Prod
import Mathlib.Algebra.Group.TypeTags.Basic
import Mathlib.Data.List.Shortlex
import Mathlib.Computability.DFA
import Mathlib.Order.Preorder.Finite
import Mathlib.Tactic.Push
import Mathlib.GroupTheory.Perm.Fin

/-!
Partial formalization of Theorem G, proof.md Section 11.
`S` is the atom alphabet; `E` indexes simple residuals and is not an
algebra-generator alphabet.  The table contains data only.  Local correctness
conditions appear explicitly as theorem arguments, never as a GS-basis field.
No finite bound is imposed on input lists.
-/

namespace ArtinG

def evalWord {S M : Type*} [Monoid M] (a : S → M) (w : List S) : M :=
  (w.map a).prod

theorem evalWord_append {S M : Type*} [Monoid M] (a : S → M) (u v : List S) :
    evalWord a (u ++ v) = evalWord a u * evalWord a v := by sorry

theorem evalWord_degree {S M : Type*} [Monoid M] (a : S → M) (degree : M → ℕ)
    (hone : degree 1 = 0)
    (hmul : ∀ u v, degree (u * v) = degree u + degree v)
    (hatom : ∀ s, degree (a s) = 1) (v : List S) :
    degree (evalWord a v) = v.length := by sorry

theorem evalWord_length_of_eq {S M : Type*} [Monoid M] (a : S → M) (degree : M → ℕ)
    (hone : degree 1 = 0)
    (hmul : ∀ u v, degree (u * v) = degree u + degree v)
    (hatom : ∀ s, degree (a s) = 1) {u v : List S}
    (h : evalWord a u = evalWord a v) : u.length = v.length := by sorry

structure ComplementTable (S E : Type*) where
  identity : E
  atom : S → E
  complement : E → E → E
  rho : E → List S

namespace ComplementTable

variable {S E : Type*} (T : ComplementTable S E)

def next (e : E) (y : S) : E := T.complement (T.atom y) e
def emit (e : E) (y : S) : List S := T.rho (T.complement e (T.atom y))

def residual (T : ComplementTable S E) (e : E) : List S → E
  | [] => e
  | y :: v => residual T (T.next e y) v

def output (T : ComplementTable S E) (e : E) : List S → List S
  | [] => []
  | y :: v => T.emit e y ++ output T (T.next e y) v

/-- Both coordinates belong to the same path. -/
inductive Path : E → E → List S → List S → Prop
  | nil (e : E) : Path e e [] []
  | cons (e : E) (y : S) {z : E} {v o : List S}
      (h : Path (T.next e y) z v o) :
      Path e z (y :: v) (T.emit e y ++ o)

theorem path_iff (e z : E) (v o : List S) :
    T.Path e z v o ↔ z = T.residual e v ∧ o = T.output e v := by sorry

theorem residual_append (e : E) (u v : List S) :
    T.residual e (u ++ v) = T.residual (T.residual e u) v := by sorry

theorem output_append (e : E) (u v : List S) :
    T.output e (u ++ v) = T.output e u ++ T.output (T.residual e u) v := by sorry

/-- Arrival at the identity is allowed only at the end of the path. -/
def FirstHit (T : ComplementTable S E) (e : E) : List S → Prop
  | [] => e = T.identity
  | y :: v => e ≠ T.identity ∧ FirstHit T (T.next e y) v

theorem firstHit_residual {e : E} {v : List S} (h : T.FirstHit e v) :
    T.residual e v = T.identity := by sorry

theorem firstHit_of_proper_prefixes (e : E) (v : List S)
    (hend : T.residual e v = T.identity)
    (hproper : ∀ u w, v = u ++ w → w ≠ [] → T.residual e u ≠ T.identity) :
    T.FirstHit e v := by sorry

section Evaluation

variable {M : Type*} [Monoid M] (a : S → M) (value : E → M)

/-- The arbitrary-length telescoping bridge.  Its only algebraic assumptions
are representative evaluation and the local complement balance identity. -/
theorem telescoping
    (hrho : ∀ e, evalWord a (T.rho e) = value e)
    (hatom : ∀ y, value (T.atom y) = a y)
    (hbalance : ∀ u v, value u * value (T.complement u v) =
      value v * value (T.complement v u))
    (e : E) (v : List S) :
    value e * evalWord a (T.output e v) =
      evalWord a v * value (T.residual e v) := by sorry

/-- Equality of the actual accepted rule, with the target still evaluated in M. -/
theorem accepted_output_equality
    (hrho : ∀ e, evalWord a (T.rho e) = value e)
    (hatom : ∀ y, value (T.atom y) = a y)
    (hid : value T.identity = 1)
    (hbalance : ∀ u v, value u * value (T.complement u v) =
      value v * value (T.complement v u))
    (x : S) (q : E) (v : List S)
    (haccept : T.residual (T.complement (T.atom x) q) v = T.identity) :
    evalWord a (x :: v) = value q * evalWord a
      (T.rho (T.complement q (T.atom x)) ++
        T.output (T.complement (T.atom x) q) v) := by sorry

end Evaluation

section Length

variable (rank : E → ℕ)

theorem output_length_balance
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (e : E) (v : List S) :
    rank e + (T.output e v).length = v.length + rank (T.residual e v) := by sorry

theorem accepted_output_length
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1)
    (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (x : S) (q : E) (v : List S)
    (haccept : T.residual (T.complement (T.atom x) q) v = T.identity) :
    rank q + (T.rho (T.complement q (T.atom x)) ++
      T.output (T.complement (T.atom x) q) v).length = (x :: v).length := by sorry

end Length

end ComplementTable

/-- The actual Coxeter-group formula u⁻¹(u ∨ v).  The join is supplied as
finite table data; its local weak-order length laws are explicit below. -/
def coxeterComplement {W : Type*} [Group W] (join : W → W → W) (u v : W) : W :=
  u⁻¹ * join u v

def tableOfJoin {S W : Type*} [Group W] (simple : S → W)
    (join : W → W → W) (rho : W → List S) : ComplementTable S W where
  identity := 1
  atom := simple
  complement := coxeterComplement join
  rho := rho

/-- Local balance is proved from reduced-lift multiplicativity and the
weak-order prefix length identity; it is not assumed as an output equality. -/
theorem join_complement_balance {W M : Type*} [Group W] [Monoid M]
    (join : W → W → W) (rank : W → ℕ) (lift : W → M)
    (hcomm : ∀ u v, join u v = join v u)
    (hprefix : ∀ u v, rank (join u v) = rank u + rank (coxeterComplement join u v))
    (hmul : ∀ u v, rank (u * v) = rank u + rank v → lift (u * v) = lift u * lift v)
    (u v : W) :
    lift u * lift (coxeterComplement join u v) =
      lift v * lift (coxeterComplement join v u) := by sorry

theorem join_complement_length {W : Type*} [Group W]
    (join : W → W → W) (rank : W → ℕ)
    (hcomm : ∀ u v, join u v = join v u)
    (hprefix : ∀ u v, rank (join u v) = rank u + rank (coxeterComplement join u v))
    (u v : W) :
    rank u + rank (coxeterComplement join u v) =
      rank v + rank (coxeterComplement join v u) := by sorry

theorem join_accepted_output_equality {S W M : Type*} [Group W] [Monoid M]
    (simple : S → W) (join : W → W → W) (rho : W → List S)
    (rank : W → ℕ) (lift : W → M) (a : S → M)
    (hrho : ∀ w, evalWord a (rho w) = lift w)
    (hatom : ∀ s, lift (simple s) = a s) (hone : lift 1 = 1)
    (hcomm : ∀ u v, join u v = join v u)
    (hprefix : ∀ u v, rank (join u v) = rank u + rank (coxeterComplement join u v))
    (hmul : ∀ u v, rank (u * v) = rank u + rank v → lift (u * v) = lift u * lift v)
    (x : S) (q : W) (v : List S)
    (haccept : (tableOfJoin simple join rho).residual
      (coxeterComplement join (simple x) q) v = 1) :
    evalWord a (x :: v) = lift q * evalWord a
      (rho (coxeterComplement join q (simple x)) ++
        (tableOfJoin simple join rho).output (coxeterComplement join (simple x) q) v) := by sorry

/-- Left divisibility: the witness multiplies on the right. -/
def LeftDivides {M : Type*} [Monoid M] (a b : M) : Prop := ∃ h, b = a * h

/-- An actual universal lcm specification, not an assumed normal-form theorem. -/
def LeftLCM {M : Type*} [Monoid M] (a b z : M) : Prop :=
  LeftDivides a z ∧ LeftDivides b z ∧
    ∀ w, LeftDivides a w → LeftDivides b w → LeftDivides z w

theorem complement_divides_iff {M : Type*} [LeftCancelMonoid M]
    {a b c : M} (hlcm : LeftLCM a b (a * c)) (h : M) :
    LeftDivides b (a * h) ↔ LeftDivides c h := by sorry

namespace ComplementTable

variable {S E M : Type*} [LeftCancelMonoid M] (T : ComplementTable S E)
  (a : S → M) (value : E → M)

theorem residual_divisibility
    (hlcm : ∀ e y, LeftLCM (a y) (value e) (a y * value (T.next e y)))
    (e : E) (v : List S) (h : M) :
    LeftDivides (value e) (evalWord a v * h) ↔
      LeftDivides (value (T.residual e v)) h := by sorry

theorem acceptance_iff_divides
    (hlcm : ∀ e y, LeftLCM (a y) (value e) (a y * value (T.next e y)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (e : E) (v : List S) :
    T.residual e v = T.identity ↔ LeftDivides (value e) (evalWord a v) := by sorry

theorem target_firstHit
    (hatom : ∀ y, value (T.atom y) = a y)
    (hlcm : ∀ u v, LeftLCM (value u) (value v)
      (value u * value (T.complement u v)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (x : S) (q : E) (v : List S)
    (hdiv : LeftDivides (value q) (evalWord a (x :: v)))
    (hproper : ∀ u w, v = u ++ w → w ≠ [] →
      ¬ LeftDivides (value q) (evalWord a (x :: u))) :
    T.FirstHit (T.complement (T.atom x) q) v := by sorry

end ComplementTable

/-- A positive grading rules out nonidentity simple divisors of 1. -/
theorem simple_divides_one_iff {E M : Type*} [Monoid M]
    (identity : E) (value : E → M) (rank : E → ℕ) (degree : M → ℕ)
    (hidentity : value identity = 1)
    (hdegree_one : degree 1 = 0)
    (hdegree_mul : ∀ a b, degree (a * b) = degree a + degree b)
    (hdegree_value : ∀ e, degree (value e) = rank e)
    (hzero : ∀ e, rank e = 0 → e = identity) (e : E) :
    LeftDivides (value e) 1 ↔ e = identity := by sorry

/-- The actual Artin--Garside generator alphabet. -/
inductive Letter (S : Type*)
  | inverse
  | delta
  | atom (s : S)
  deriving DecidableEq

def letterLT {S : Type*} (r : S → S → Prop) : Letter S → Letter S → Prop
  | .inverse, .delta => True
  | .inverse, .atom _ => True
  | .delta, .atom _ => True
  | .atom s, .atom t => r s t
  | _, _ => False

def atomWord {S : Type*} (w : List S) : List (Letter S) := w.map Letter.atom

theorem letterLT_wellFounded {S : Type*} {r : S → S → Prop}
    (wf : WellFounded r) : WellFounded (letterLT r) := by sorry

theorem lex_append_suffix {S : Type*} {r : S → S → Prop} {u v : List S}
    (h : List.Lex r u v) (hlen : u.length = v.length) (w : List S) :
    List.Lex r (u ++ w) (v ++ w) := by sorry

theorem shortlex_context {S : Type*} {r : S → S → Prop} {u v : List S}
    (h : List.Shortlex r u v) (p s : List S) :
    List.Shortlex r (p ++ u ++ s) (p ++ v ++ s) := by sorry

/-- Two-sided rewriting for a possibly infinite rule predicate. -/
inductive Step {S : Type*} (R : List S → List S → Prop) : List S → List S → Prop
  | apply {u v} (h : R u v) (p s : List S) : Step R (p ++ u ++ s) (p ++ v ++ s)

theorem step_decreases {S : Type*} {r : S → S → Prop}
    {R : List S → List S → Prop}
    (hR : ∀ u v, R u v → List.Shortlex r v u) {u v : List S}
    (h : Step R u v) : List.Shortlex r v u := by sorry

theorem step_wellFounded {S : Type*} {r : S → S → Prop}
    {R : List S → List S → Prop} (wf : WellFounded r)
    (hR : ∀ u v, R u v → List.Shortlex r v u) :
    WellFounded (fun v u => Step R u v) := by sorry

namespace ComplementTable

variable {S E : Type*} (T : ComplementTable S E)

def ruleTail (x : S) (q : E) (v : List S) : List S :=
  T.rho (T.complement q (T.atom x)) ++ T.output (T.complement (T.atom x) q) v

theorem atom_rule_decreases (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (x t : S) (v : List S) (hlt : r t x)
    (haccept : T.residual (T.complement (T.atom x) (T.atom t)) v = T.identity) :
    List.Shortlex (letterLT r)
      (Letter.atom t :: atomWord (T.ruleTail x (T.atom t) v))
      (Letter.atom x :: atomWord v) := by sorry

theorem delta_rule_decreases (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (d : E) (hN : 2 ≤ rank d) (x : S) (v : List S)
    (haccept : T.residual (T.complement (T.atom x) d) v = T.identity) :
    List.Shortlex (letterLT r)
      (Letter.delta :: atomWord (T.ruleTail x d v))
      (Letter.atom x :: atomWord v) := by sorry

end ComplementTable

/-- The exact positive transducer rules plus twists and cancellations. -/
inductive GRule {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) : List (Letter S) → List (Letter S) → Prop
  | lex (x t : S) (v : List S) (hlt : r t x) (hne : v ≠ [])
      (hhit : T.FirstHit (T.complement (T.atom x) (T.atom t)) v) :
      GRule T d phi r (Letter.atom x :: atomWord v)
        (Letter.atom t :: atomWord (T.ruleTail x (T.atom t) v))
  | extract (x : S) (v : List S) (hne : v ≠ [])
      (hhit : T.FirstHit (T.complement (T.atom x) d) v) :
      GRule T d phi r (Letter.atom x :: atomWord v)
        (Letter.delta :: atomWord (T.ruleTail x d v))
  | twistDelta (x : S) : GRule T d phi r [.atom x, .delta] [.delta, .atom (phi x)]
  | twistInverse (x : S) : GRule T d phi r [.atom x, .inverse] [.inverse, .atom (phi x)]
  | cancelDelta : GRule T d phi r [.delta, .inverse] []
  | cancelInverse : GRule T d phi r [.inverse, .delta] []

theorem gRule_decreases {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d)
    {u v : List (Letter S)} (h : GRule T d phi r u v) :
    List.Shortlex (letterLT r) v u := by sorry

theorem gStep_wellFounded {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d) (wf : WellFounded r) :
    WellFounded (fun v u => Step (GRule T d phi r) u v) := by sorry

theorem gStep_finite_wellFounded {S E : Type*} [Finite S] [LinearOrder S]
    (T : ComplementTable S E) (d : E) (phi : S → S) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d) :
    WellFounded (fun v u => Step (GRule T d phi (· < ·)) u v) := by sorry

namespace ComplementTable

variable {S E : Type*} [DecidableEq E] (T : ComplementTable S E)

/-- Accepting residuals have no outgoing live edges; `none` is the dead state.
If E is finite this is an actual finite-state machine with |E|+1 states. -/
def firstHitDFA (start : E) : DFA S (Option E) where
  start := some start
  accept := {some T.identity}
  step
    | none, _ => none
    | some e, y => if e = T.identity then none else some (T.next e y)

theorem firstHitDFA_dead (start : E) (v : List S) :
    (T.firstHitDFA start).evalFrom none v = none := by sorry

theorem firstHitDFA_correct_from (start e : E) (v : List S) :
    (T.firstHitDFA start).evalFrom (some e) v = some T.identity ↔ T.FirstHit e v := by sorry

theorem firstHitDFA_correct (e : E) (v : List S) :
    v ∈ (T.firstHitDFA e).accepts ↔ T.FirstHit e v := by sorry

end ComplementTable

def letterValue {S M : Type*} [Group M] (a : S → M) (delta : M) : Letter S → M
  | .inverse => delta⁻¹
  | .delta => delta
  | .atom s => a s

theorem eval_atomWord {S M : Type*} [Group M] (a : S → M) (delta : M) (v : List S) :
    evalWord (letterValue a delta) (atomWord v) = evalWord a v := by sorry

theorem gRule_valid {S E M : Type*} [Group M]
    (T : ComplementTable S E) (d : E) (phi : S → S) (r : S → S → Prop)
    (a : S → M) (value : E → M)
    (hrho : ∀ e, evalWord a (T.rho e) = value e)
    (hatom : ∀ y, value (T.atom y) = a y) (hid : value T.identity = 1)
    (hbalance : ∀ u v, value u * value (T.complement u v) =
      value v * value (T.complement v u))
    (hphi : ∀ x, phi (phi x) = x)
    (htwist : ∀ x, a x * value d = value d * a (phi x))
    {u v : List (Letter S)} (h : GRule T d phi r u v) :
    evalWord (letterValue a (value d)) u = evalWord (letterValue a (value d)) v := by sorry

theorem step_valid {S M : Type*} [Monoid M] (a : S → M)
    {R : List S → List S → Prop}
    (hR : ∀ u v, R u v → evalWord a u = evalWord a v) {u v : List S}
    (h : Step R u v) : evalWord a u = evalWord a v := by sorry

/-- Positive normality is defined by actual least words and Delta divisibility. -/
def PositiveNormal {S M : Type*} [Monoid M] (a : S → M) (delta : M)
    (r : S → S → Prop) (v : List S) : Prop :=
  (∀ u, evalWord a u = evalWord a v → ¬ List.Shortlex r u v) ∧
    ¬ LeftDivides delta (evalWord a v)

theorem smaller_atom_target {S M : Type*} [LeftCancelMonoid M]
    (a : S → M) (r : S → S → Prop) (x : S) (v u : List S)
    (hsuffix : ∀ w, evalWord a w = evalWord a v → ¬ List.Shortlex r w v)
    (heq : evalWord a u = evalWord a (x :: v))
    (hlen : u.length = (x :: v).length) (hlt : List.Shortlex r u (x :: v)) :
    ∃ t, r t x ∧ LeftDivides (a t) (evalWord a (x :: v)) := by sorry

theorem normal_no_smaller_head {S M : Type*} [Monoid M]
    (a : S → M) (delta : M) (r : S → S → Prop)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (x t : S) (v : List S) (hlt : r t x)
    (hnormal : PositiveNormal a delta r (x :: v)) :
    ¬ LeftDivides (a t) (evalWord a (x :: v)) := by sorry

/-- Conditional minimal-positive-factor coverage, derived rather than stored
as a table field.  Prefix/suffix normality is the minimal-factor hypothesis.
The hypotheses still need an all-finite-type Artin instantiation. -/
theorem minimal_positive_rule_coverage {S E M : Type*} [LeftCancelMonoid M]
    (T : ComplementTable S E) (d : E) (phi : S → S) (r : S → S → Prop)
    (a : S → M) (value : E → M)
    (hatom : ∀ y, value (T.atom y) = a y)
    (hlcm : ∀ u v, LeftLCM (value u) (value v)
      (value u * value (T.complement u v)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (x : S) (v : List S) (hne : v ≠ [])
    (hnot : ¬ PositiveNormal a (value d) r (x :: v))
    (hsuffix : PositiveNormal a (value d) r v)
    (hprefix : ∀ u w, v = u ++ w → w ≠ [] → PositiveNormal a (value d) r (x :: u)) :
    ∃ o, GRule T d phi r (Letter.atom x :: atomWord v) o := by sorry

namespace CommutingExample

/- A concrete positive A1 × A1 model.  Its four simple states are subsets of
   {a,b}; complements are set differences.  All local identities below are
   kernel computations, and the loop theorem covers arbitrary path lengths. -/
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
def rank (e : E) : ℕ := (if e.1 then 1 else 0) + (if e.2 then 1 else 0)

theorem rho_value : ∀ e, evalWord atom (table.rho e) = value e := by sorry

theorem atom_value : ∀ y, value (table.atom y) = atom y := by sorry

theorem identity_value : value table.identity = 1 := by sorry

theorem complement_balance : ∀ u v, value u * value (table.complement u v) =
    value v * value (table.complement v u) := by sorry

theorem rho_length : ∀ e, (table.rho e).length = rank e := by sorry

theorem atom_length : ∀ y, rank (table.atom y) = 1 := by sorry

theorem identity_length : rank table.identity = 0 := by sorry

theorem complement_length : ∀ u v, rank u + rank (table.complement u v) =
    rank v + rank (table.complement v u) := by sorry

theorem loop_run (n : ℕ) :
    table.residual (false, true) (List.replicate n false ++ [true]) = table.identity ∧
    table.output (false, true) (List.replicate n false ++ [true]) = List.replicate n false ∧
    table.FirstHit (false, true) (List.replicate n false ++ [true]) := by sorry

theorem loop_tail (n : ℕ) :
    table.ruleTail false (true, true) (List.replicate n false ++ [true]) =
      List.replicate n false := by sorry

theorem loop_rule_valid (n : ℕ) :
    evalWord atom (false :: (List.replicate n false ++ [true])) =
      value (true, true) * evalWord atom (List.replicate n false) := by sorry

theorem loop_rule_decreases (n : ℕ) :
    List.Shortlex (letterLT (fun s t : Bool => s = false ∧ t = true))
      (Letter.delta :: atomWord (List.replicate n false))
      (Letter.atom false :: atomWord (List.replicate n false ++ [true])) := by sorry

theorem lost_loop_output_is_wrong :
    evalWord atom [false, false, true] ≠ value (true, true) * evalWord atom [] := by sorry

end CommutingExample

namespace EmptySystem

/-- In rank zero, Delta and its inverse both represent the identity. -/
def Rule : List (Letter PEmpty) → List (Letter PEmpty) → Prop
  | u, v => (u = [.delta] ∧ v = []) ∨ (u = [.inverse] ∧ v = [])

theorem rule_decreases (u v : List (Letter PEmpty)) (h : Rule u v) :
    List.Shortlex (letterLT (fun _ _ => False)) v u := by sorry

theorem step_wellFounded : WellFounded (fun v u => Step Rule u v) := by sorry

theorem reduces_to_nil (w : List (Letter PEmpty)) :
    Relation.ReflTransGen (Step Rule) w [] := by sorry

theorem irreducible_iff_nil (w : List (Letter PEmpty)) :
    (∀ v, ¬ Step Rule w v) ↔ w = [] := by sorry

theorem confluent {w u v : List (Letter PEmpty)}
    (_hu : Relation.ReflTransGen (Step Rule) w u)
    (_hv : Relation.ReflTransGen (Step Rule) w v) :
    ∃ z, Relation.ReflTransGen (Step Rule) u z ∧ Relation.ReflTransGen (Step Rule) v z := by sorry

end EmptySystem

end ArtinG

namespace ArtinG
namespace Completeness

def Irreducible {A : Type*} (R : List A → List A → Prop) (w : List A) : Prop :=
  ∀ v, ¬ Step R w v

theorem irreducible_factor {A : Type*} {R : List A → List A → Prop}
    (p u s : List A) (h : Irreducible R (p ++ u ++ s)) : Irreducible R u := by sorry

/-- Existence by termination only; no joining hypothesis. Adapted from the
audited OAI FiniteCompiler exists_irreducible argument. -/
theorem exists_irreducible {A : Type*} (R : List A → List A → Prop)
    (wf : WellFounded (fun v u => Step R u v)) (w : List A) :
    ∃ z, Relation.ReflTransGen (Step R) w z ∧ Irreducible R z := by sorry

theorem steps_valid {A M : Type*} [Monoid M] (a : A → M)
    {R : List A → List A → Prop}
    (hR : ∀ u v, R u v → evalWord a u = evalWord a v) {u v : List A}
    (h : Relation.ReflTransGen (Step R) u v) : evalWord a u = evalWord a v := by sorry

theorem no_return {A : Type*} (R : List A → List A → Prop)
    (wf : WellFounded (fun v u => Step R u v)) (w : List A) :
    ∀ v, Step R w v → ¬ Relation.ReflTransGen (Step R) v w := by sorry

theorem twist_word {S M : Type*} [Monoid M] (a : S → M) (D : M) (phi : S → S)
    (htwist : ∀ x, a x * D = D * a (phi x)) (p : List S) :
    evalWord a p * D = D * evalWord a (p.map phi) := by sorry

theorem positiveNormal_factor {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (phi : S → S) (r : S → S → Prop)
    (htwist : ∀ x, a x * D = D * a (phi x)) (p u s : List S)
    (hn : PositiveNormal a D r (p ++ u ++ s)) : PositiveNormal a D r u := by sorry

theorem delta_not_divides_short {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (rhoD : List S)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (p : List S) (hp : p.length ≤ 1) : ¬ LeftDivides D (evalWord a p) := by sorry

theorem positiveNormal_nil {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (rhoD : List S) (r : S → S → Prop)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length) :
    PositiveNormal a D r [] := by sorry

theorem positiveNormal_atom {S M : Type*} [Finite S] [LinearOrder S] [Monoid M]
    (a : S → M) (D : M) (rhoD : List S)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (hinj : Function.Injective a) (x : S) : PositiveNormal a D (· < ·) [x] := by sorry

theorem positive_normal_of_irreducible {S E M : Type*}
    [Finite S] [LinearOrder S] [LeftCancelMonoid M]
    (T : ComplementTable S E) (d : E) (phi : S → S)
    (a : S → M) (value : E → M)
    (hrho : ∀ e, evalWord a (T.rho e) = value e)
    (hatom : ∀ y, value (T.atom y) = a y)
    (hlcm : ∀ u v, LeftLCM (value u) (value v)
      (value u * value (T.complement u v)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (hinj : Function.Injective a) (hN : 2 ≤ (T.rho d).length) (w : List S)
    (hw : Irreducible (GRule T d phi (· < ·)) (atomWord w)) :
    PositiveNormal a (value d) (· < ·) w := by sorry

def signLetter {S : Type*} (s : Bool) : Letter S := if s then .delta else .inverse

/-- The twists and cancellations alone force a uniform signed prefix followed
by a genuine atom word. This does not assume a group normal form. -/
theorem irreducible_shape {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (w : List (Letter S))
    (hw : Irreducible (GRule T d phi r) w) :
    ∃ s n p, w = List.replicate n (signLetter s) ++ atomWord p := by sorry

def deltaPower {S : Type*} (k : ℤ) : List (Letter S) :=
  if 0 ≤ k then List.replicate k.toNat .delta else List.replicate (-k).toNat .inverse

theorem deltaPower_nat {S : Type*} (n : ℕ) :
    deltaPower (S := S) (n : ℤ) = List.replicate n .delta := by sorry

theorem deltaPower_neg_nat {S : Type*} (n : ℕ) :
    deltaPower (S := S) (-(n : ℤ)) = List.replicate n .inverse := by sorry

def NF {S M : Type*} [Monoid M] (a : S → M) (D : M) (r : S → S → Prop)
    (w : List (Letter S)) : Prop :=
  ∃ k p, w = deltaPower k ++ atomWord p ∧ PositiveNormal a D r p

theorem irreducible_normalForm {S E M : Type*}
    [Finite S] [LinearOrder S] [LeftCancelMonoid M]
    (T : ComplementTable S E) (d : E) (phi : S → S)
    (a : S → M) (value : E → M)
    (hrho : ∀ e, evalWord a (T.rho e) = value e)
    (hatom : ∀ y, value (T.atom y) = a y)
    (hlcm : ∀ u v, LeftLCM (value u) (value v)
      (value u * value (T.complement u v)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (hinj : Function.Injective a) (hN : 2 ≤ (T.rho d).length)
    (w : List (Letter S)) (hw : Irreducible (GRule T d phi (· < ·)) w) :
    NF a (value d) (· < ·) w := by sorry

theorem evalWord_map {S M G : Type*} [Monoid M] [Monoid G]
    (iota : M →* G) (a : S → M) (p : List S) :
    iota (evalWord a p) = evalWord (fun s => iota (a s)) p := by sorry

theorem eval_deltaPower {S G : Type*} [Group G] (a : S → G) (D : G) (k : ℤ) :
    evalWord (letterValue a D) (deltaPower k) = D ^ k := by sorry

theorem positiveNormal_injective {S M : Type*} [LinearOrder S] [Monoid M]
    (a : S → M) (D : M) {p q : List S}
    (hp : PositiveNormal a D (· < ·) p) (hq : PositiveNormal a D (· < ·) q)
    (he : evalWord a p = evalWord a q) : p = q := by sorry

theorem normalForm_value_injective {S M G : Type*} [LinearOrder S] [Monoid M] [Group G]
    (iota : M →* G) (a : S → M) (D : M)
    (hG5 : ∀ (k k' : ℤ) (p p' : M), ¬ LeftDivides D p → ¬ LeftDivides D p' →
      (iota D) ^ k * iota p = (iota D) ^ k' * iota p' → k = k' ∧ p = p')
    {u v : List (Letter S)} (hu : NF a D (· < ·) u) (hv : NF a D (· < ·) v)
    (he : evalWord (letterValue (fun s => iota (a s)) (iota D)) u =
      evalWord (letterValue (fun s => iota (a s)) (iota D)) v) : u = v := by sorry

theorem embedding_left_cancel {M G : Type*} [Monoid M] [Group G]
    (iota : M →* G) (hi : Function.Injective iota) (a b c : M) (h : a * b = a * c) : b = c := by sorry

def leftCancelOfEmbedding {M G : Type*} [Monoid M] [Group G]
    (iota : M →* G) (hi : Function.Injective iota) : LeftCancelMonoid M where
  __ := (inferInstance : Monoid M)
  mul_left_cancel := embedding_left_cancel iota hi

section Conditional

variable {S E M G : Type*} [Finite S] [LinearOrder S] [LeftCancelMonoid M] [Group G]
  (T : ComplementTable S E) (d : E) (phi : S → S)
  (a : S → M) (value : E → M) (rank : E → ℕ) (iota : M →* G)
  (hrho : ∀ e, evalWord a (T.rho e) = value e)
  (hatom : ∀ y, value (T.atom y) = a y) (hid : value T.identity = 1)
  (hbalance : ∀ u v, value u * value (T.complement u v) =
    value v * value (T.complement v u))
  (hrank : ∀ e, (T.rho e).length = rank e)
  (hatomrank : ∀ y, rank (T.atom y) = 1) (hidrank : rank T.identity = 0)
  (hbalanceRank : ∀ u v, rank u + rank (T.complement u v) =
    rank v + rank (T.complement v u)) (hN : 2 ≤ rank d)
  (hlcm : ∀ u v, LeftLCM (value u) (value v)
    (value u * value (T.complement u v)))
  (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
  (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
  (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
  (hinj : Function.Injective a) (hphi : ∀ x, phi (phi x) = x)
  (htwist : ∀ x, a x * value d = value d * a (phi x))
  (hG5 : ∀ (k k' : ℤ) (p p' : M), ¬ LeftDivides (value d) p →
    ¬ LeftDivides (value d) p' →
    (iota (value d)) ^ k * iota p = (iota (value d)) ^ k' * iota p' →
    k = k' ∧ p = p')

include hrho hatom hid hbalance hrank hatomrank hidrank hbalanceRank hN
  hlcm hunit hgenerated hhomogeneous hinj hphi htwist hG5

/-- All hypotheses are local table laws or explicit Garside background properties.
This proves completeness of this specific infinite rule family, not its instantiation
in every finite-type Artin group and not polynomial composition triviality. -/
theorem conditional_equal_iff_join (u v : List (Letter S)) :
    evalWord (letterValue (fun s => iota (a s)) (iota (value d))) u =
      evalWord (letterValue (fun s => iota (a s)) (iota (value d))) v ↔
    ∃ z, Relation.ReflTransGen (Step (GRule T d phi (· < ·))) u z ∧
      Relation.ReflTransGen (Step (GRule T d phi (· < ·))) v z := by sorry

theorem conditional_irreducible_iff_nf (w : List (Letter S)) :
    Irreducible (GRule T d phi (· < ·)) w ↔ NF a (value d) (· < ·) w := by sorry

theorem conditional_confluent {w u v : List (Letter S)}
    (hu : Relation.ReflTransGen (Step (GRule T d phi (· < ·))) w u)
    (hv : Relation.ReflTransGen (Step (GRule T d phi (· < ·))) w v) :
    ∃ z, Relation.ReflTransGen (Step (GRule T d phi (· < ·))) u z ∧
      Relation.ReflTransGen (Step (GRule T d phi (· < ·))) v z := by sorry

end Conditional

end Completeness
end ArtinG

namespace ArtinG.NoncommutingControl

/-- A genuine noncommutative quotient of the type-A2 Artin group. -/
def atom (y : Bool) : Equiv.Perm (Fin 3) :=
  if y then Equiv.swap 1 2 else Equiv.swap 0 1

theorem braid_relation :
    evalWord atom [false, true, false] = evalWord atom [true, false, true] := by sorry

/-- The A2 complement path has residuals ab,b,ba,ba,a,1 and emits
epsilon,ab,b,epsilon,epsilon after initial output aba. -/
theorem accepted_output :
    evalWord atom [true, false, false, false, true, false] =
      evalWord atom [false, true, false, false, true, true] := by sorry

theorem reversed_blocks_wrong :
    evalWord atom [true, false, false, false, true, false] ≠
      evalWord atom [false, true, false, true, false, true] := by sorry

end ArtinG.NoncommutingControl

set_option pp.proofs false
set_option pp.universes false

