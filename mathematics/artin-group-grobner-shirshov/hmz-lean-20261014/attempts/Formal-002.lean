import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Shortlex
import Mathlib.Tactic

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
    evalWord a (u ++ v) = evalWord a u * evalWord a v := by
  simp [evalWord]

structure ComplementTable (S E : Type*) where
  identity : E
  atom : S → E
  complement : E → E → E
  rho : E → List S

namespace ComplementTable

variable {S E : Type*} (T : ComplementTable S E)

def next (e : E) (y : S) : E := T.complement (T.atom y) e
def emit (e : E) (y : S) : List S := T.rho (T.complement e (T.atom y))

def residual (e : E) : List S → E
  | [] => e
  | y :: v => T.residual (T.next e y) v

def output (e : E) : List S → List S
  | [] => []
  | y :: v => T.emit e y ++ T.output (T.next e y) v

/-- Both coordinates belong to the same path. -/
inductive Path : E → E → List S → List S → Prop
  | nil (e : E) : Path e e [] []
  | cons (e : E) (y : S) {z : E} {v o : List S}
      (h : Path (T.next e y) z v o) :
      Path e z (y :: v) (T.emit e y ++ o)

theorem path_iff (e z : E) (v o : List S) :
    T.Path e z v o ↔ z = T.residual e v ∧ o = T.output e v := by
  constructor
  · intro h
    induction h with
    | nil => exact ⟨rfl, rfl⟩
    | cons e y h ih =>
      exact ⟨ih.1, congrArg (T.emit e y ++ ·) ih.2⟩
  · rintro ⟨rfl, rfl⟩
    induction v generalizing e with
    | nil => exact .nil e
    | cons y v ih => exact .cons e y (ih (T.next e y))

theorem residual_append (e : E) (u v : List S) :
    T.residual e (u ++ v) = T.residual (T.residual e u) v := by
  induction u generalizing e with
  | nil => rfl
  | cons y u ih => exact ih (T.next e y)

theorem output_append (e : E) (u v : List S) :
    T.output e (u ++ v) = T.output e u ++ T.output (T.residual e u) v := by
  induction u generalizing e with
  | nil => rfl
  | cons y u ih =>
    simp only [List.cons_append, output, residual, ih, List.append_assoc]

/-- Arrival at the identity is allowed only at the end of the path. -/
def FirstHit (e : E) : List S → Prop
  | [] => e = T.identity
  | y :: v => e ≠ T.identity ∧ T.FirstHit (T.next e y) v

theorem firstHit_residual {e : E} {v : List S} (h : T.FirstHit e v) :
    T.residual e v = T.identity := by
  induction v generalizing e with
  | nil => exact h
  | cons y v ih => exact ih h.2

theorem firstHit_of_proper_prefixes (e : E) (v : List S)
    (hend : T.residual e v = T.identity)
    (hproper : ∀ u w, v = u ++ w → w ≠ [] → T.residual e u ≠ T.identity) :
    T.FirstHit e v := by
  induction v generalizing e with
  | nil => exact hend
  | cons y v ih =>
    refine ⟨hproper [] (y :: v) rfl (by simp), ih (T.next e y) hend ?_⟩
    intro u w huv hw
    exact hproper (y :: u) w (by simpa [huv]) hw

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
      evalWord a v * value (T.residual e v) := by
  induction v generalizing e with
  | nil => simp [output, residual, evalWord]
  | cons y v ih =>
    calc
      value e * evalWord a (T.output e (y :: v)) =
          (value e * value (T.complement e (T.atom y))) *
            evalWord a (T.output (T.next e y) v) := by
              rw [output, evalWord_append, emit, hrho, ← mul_assoc]
      _ = (a y * value (T.next e y)) *
            evalWord a (T.output (T.next e y) v) := by
              rw [hbalance, hatom]; rfl
      _ = a y * (evalWord a v * value (T.residual (T.next e y) v)) := by
              rw [mul_assoc, ih]
      _ = evalWord a (y :: v) * value (T.residual e (y :: v)) := by
              simp [evalWord, residual, mul_assoc]

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
        T.output (T.complement (T.atom x) q) v) := by
  have ht := T.telescoping a value hrho hatom hbalance (T.complement (T.atom x) q) v
  rw [haccept, hid, mul_one] at ht
  calc
    evalWord a (x :: v) = a x * evalWord a v := by simp [evalWord]
    _ = (value (T.atom x) * value (T.complement (T.atom x) q)) *
          evalWord a (T.output (T.complement (T.atom x) q) v) := by
            rw [hatom, mul_assoc, ht]
    _ = value q * evalWord a
          (T.rho (T.complement q (T.atom x)) ++
            T.output (T.complement (T.atom x) q) v) := by
            rw [hbalance, mul_assoc, evalWord_append, hrho]

end Evaluation

section Length

variable (rank : E → ℕ)

theorem output_length_balance
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (e : E) (v : List S) :
    rank e + (T.output e v).length = v.length + rank (T.residual e v) := by
  induction v generalizing e with
  | nil => simp [output, residual]
  | cons y v ih =>
    have hb := hbalance e (T.atom y)
    have hi := ih (T.next e y)
    simp only [hatom] at hb
    simp only [output, List.length_append, emit, hrho, residual, List.length_cons]
    dsimp [next] at hi
    omega

theorem accepted_output_length
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1)
    (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (x : S) (q : E) (v : List S)
    (haccept : T.residual (T.complement (T.atom x) q) v = T.identity) :
    rank q + (T.rho (T.complement q (T.atom x)) ++
      T.output (T.complement (T.atom x) q) v).length = (x :: v).length := by
  have hb := hbalance (T.atom x) q
  have ht := T.output_length_balance rank hrho hatom hbalance
    (T.complement (T.atom x) q) v
  rw [haccept, hid] at ht
  simp only [hatom] at hb
  simp only [List.length_append, hrho, List.length_cons]
  omega

end Length

end ComplementTable

/-- Left divisibility: the witness multiplies on the right. -/
def LeftDivides {M : Type*} [Monoid M] (a b : M) : Prop := ∃ h, b = a * h

/-- An actual universal lcm specification, not an assumed normal-form theorem. -/
def LeftLCM {M : Type*} [Monoid M] (a b z : M) : Prop :=
  LeftDivides a z ∧ LeftDivides b z ∧
    ∀ w, LeftDivides a w → LeftDivides b w → LeftDivides z w

theorem complement_divides_iff {M : Type*} [LeftCancelMonoid M]
    {a b c : M} (hlcm : LeftLCM a b (a * c)) (h : M) :
    LeftDivides b (a * h) ↔ LeftDivides c h := by
  constructor
  · intro hb
    obtain ⟨d, hd⟩ := hlcm.2.2 (a * h) ⟨h, rfl⟩ hb
    refine ⟨d, ?_⟩
    exact mul_left_cancel (by simpa only [mul_assoc] using hd)
  · rintro ⟨d, rfl⟩
    obtain ⟨k, hk⟩ := hlcm.2.1
    refine ⟨k * d, ?_⟩
    rw [← mul_assoc, hk, mul_assoc]

namespace ComplementTable

variable {S E M : Type*} [LeftCancelMonoid M] (T : ComplementTable S E)
  (a : S → M) (value : E → M)

theorem residual_divisibility
    (hlcm : ∀ e y, LeftLCM (a y) (value e) (a y * value (T.next e y)))
    (e : E) (v : List S) (h : M) :
    LeftDivides (value e) (evalWord a v * h) ↔
      LeftDivides (value (T.residual e v)) h := by
  induction v generalizing e with
  | nil => simp [evalWord, residual]
  | cons y v ih =>
    have hc := complement_divides_iff (hlcm e y) (evalWord a v * h)
    simpa only [evalWord, List.map_cons, List.prod_cons, mul_assoc, residual] using
      hc.trans (ih (T.next e y))

theorem acceptance_iff_divides
    (hlcm : ∀ e y, LeftLCM (a y) (value e) (a y * value (T.next e y)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (e : E) (v : List S) :
    T.residual e v = T.identity ↔ LeftDivides (value e) (evalWord a v) := by
  have hd := T.residual_divisibility a value hlcm e v 1
  rw [mul_one, hunit] at hd
  exact hd.symm

theorem target_firstHit
    (hatom : ∀ y, value (T.atom y) = a y)
    (hlcm : ∀ u v, LeftLCM (value u) (value v)
      (value u * value (T.complement u v)))
    (hunit : ∀ e, LeftDivides (value e) 1 ↔ e = T.identity)
    (x : S) (q : E) (v : List S)
    (hdiv : LeftDivides (value q) (evalWord a (x :: v)))
    (hproper : ∀ u w, v = u ++ w → w ≠ [] →
      ¬ LeftDivides (value q) (evalWord a (x :: u))) :
    T.FirstHit (T.complement (T.atom x) q) v := by
  have localLCM : ∀ e y, LeftLCM (a y) (value e) (a y * value (T.next e y)) := by
    intro e y
    simpa only [hatom, next] using hlcm (T.atom y) e
  have target (u : List S) : LeftDivides (value q) (evalWord a (x :: u)) ↔
      T.residual (T.complement (T.atom x) q) u = T.identity := by
    have hc := complement_divides_iff (hlcm (T.atom x) q) (evalWord a u)
    simpa only [hatom, evalWord, List.map_cons, List.prod_cons] using
      hc.trans (T.acceptance_iff_divides a value localLCM hunit _ u).symm
  apply T.firstHit_of_proper_prefixes _ v ((target v).mp hdiv)
  intro u w huv hw he
  exact hproper u w huv hw ((target u).mpr he)

end ComplementTable

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
      (Letter.atom x :: atomWord v) := by
  have hl := T.accepted_output_length rank hrho hatom hid hbalance x (T.atom t) v haccept
  apply List.Shortlex.of_lex
  · simpa only [ruleTail, atomWord, List.length_cons, List.length_map, hatom] using hl
  · exact List.Lex.rel hlt

theorem delta_rule_decreases (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u))
    (d : E) (hN : 2 ≤ rank d) (x : S) (v : List S)
    (haccept : T.residual (T.complement (T.atom x) d) v = T.identity) :
    List.Shortlex (letterLT r)
      (Letter.delta :: atomWord (T.ruleTail x d v))
      (Letter.atom x :: atomWord v) := by
  have hl := T.accepted_output_length rank hrho hatom hid hbalance x d v haccept
  apply List.Shortlex.of_length_lt
  simp only [atomWord, List.length_cons, List.length_map]
  change rank d + (T.ruleTail x d v).length = (x :: v).length at hl
  simp only [List.length_cons] at hl
  omega

end ComplementTable

end ArtinG
