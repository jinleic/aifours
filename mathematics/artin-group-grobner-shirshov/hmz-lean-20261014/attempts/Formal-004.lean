import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Shortlex
import Mathlib.Computability.DFA
import Mathlib.Order.Preorder.Finite
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
def FirstHit (T : ComplementTable S E) (e : E) : List S → Prop
  | [] => e = T.identity
  | y :: v => e ≠ T.identity ∧ FirstHit T (T.next e y) v

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
    simp only [next] at *
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

/-- A positive grading rules out nonidentity simple divisors of 1. -/
theorem simple_divides_one_iff {E M : Type*} [Monoid M]
    (identity : E) (value : E → M) (rank : E → ℕ) (degree : M → ℕ)
    (hidentity : value identity = 1)
    (hdegree_one : degree 1 = 0)
    (hdegree_mul : ∀ a b, degree (a * b) = degree a + degree b)
    (hdegree_value : ∀ e, degree (value e) = rank e)
    (hzero : ∀ e, rank e = 0 → e = identity) (e : E) :
    LeftDivides (value e) 1 ↔ e = identity := by
  constructor
  · rintro ⟨h, hh⟩
    have hd := congrArg degree hh
    rw [hdegree_one, hdegree_mul, hdegree_value] at hd
    exact hzero e (by omega)
  · rintro rfl
    exact ⟨1, by rw [hidentity, mul_one]⟩

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
    (wf : WellFounded r) : WellFounded (letterLT r) := by
  have hinv : Acc (letterLT r) (Letter.inverse : Letter S) := by
    refine Acc.intro _ ?_
    intro a h
    cases a <;> exact False.elim h
  have hdelta : Acc (letterLT r) (Letter.delta : Letter S) := by
    refine Acc.intro _ ?_
    intro a h
    cases a with
    | inverse => exact hinv
    | delta => exact False.elim h
    | atom s => exact False.elim h
  have hatom : ∀ s, Acc (letterLT r) (Letter.atom s) := by
    intro s
    induction s using wf.induction with
    | h s ih =>
      refine Acc.intro _ ?_
      intro a ha
      cases a with
      | inverse => exact hinv
      | delta => exact hdelta
      | atom t => exact ih t ha
  refine ⟨?_⟩
  intro a
  cases a with
  | inverse => exact hinv
  | delta => exact hdelta
  | atom s => exact hatom s

/- These two context proofs adapt OAI/Computability/FiniteCompiler/Rewriting.lean,
   lex_append_suffix and shortlex_context.  Here rules need not form a finite list. -/
theorem lex_append_suffix {S : Type*} {r : S → S → Prop} {u v : List S}
    (h : List.Lex r u v) (hlen : u.length = v.length) (w : List S) :
    List.Lex r (u ++ w) (v ++ w) := by
  induction h with
  | nil => simp at hlen
  | rel h => exact .rel h
  | cons h ih => exact .cons (ih (by simpa using hlen))

theorem shortlex_context {S : Type*} {r : S → S → Prop} {u v : List S}
    (h : List.Shortlex r u v) (p s : List S) :
    List.Shortlex r (p ++ u ++ s) (p ++ v ++ s) := by
  simp only [List.append_assoc]
  apply List.Shortlex.append_left (s := p)
  rcases List.shortlex_def.mp h with hl | ⟨hl, hx⟩
  · apply List.Shortlex.of_length_lt
    simpa using hl
  · exact List.Shortlex.of_lex (by simp [hl]) (lex_append_suffix hx hl s)

/-- Two-sided rewriting for a possibly infinite rule predicate. -/
inductive Step {S : Type*} (R : List S → List S → Prop) : List S → List S → Prop
  | apply {u v} (h : R u v) (p s : List S) : Step R (p ++ u ++ s) (p ++ v ++ s)

theorem step_decreases {S : Type*} {r : S → S → Prop}
    {R : List S → List S → Prop}
    (hR : ∀ u v, R u v → List.Shortlex r v u) {u v : List S}
    (h : Step R u v) : List.Shortlex r v u := by
  cases h with
  | apply h p s => exact shortlex_context (hR _ _ h) p s

theorem step_wellFounded {S : Type*} {r : S → S → Prop}
    {R : List S → List S → Prop} (wf : WellFounded r)
    (hR : ∀ u v, R u v → List.Shortlex r v u) :
    WellFounded (fun v u => Step R u v) :=
  (List.Shortlex.wf wf).mono (fun _ _ h => step_decreases hR h)

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
  · simpa only [ruleTail, atomWord, List.length_cons, List.length_map, hatom,
      Nat.add_comm] using hl
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
    List.Shortlex (letterLT r) v u := by
  cases h with
  | lex x t v hlt hne hhit =>
    exact T.atom_rule_decreases r rank hrho hatom hid hbalance x t v hlt
      (T.firstHit_residual hhit)
  | extract x v hne hhit =>
    exact T.delta_rule_decreases r rank hrho hatom hid hbalance d hN x v
      (T.firstHit_residual hhit)
  | twistDelta x => exact List.Shortlex.of_lex rfl (List.Lex.rel trivial)
  | twistInverse x => exact List.Shortlex.of_lex rfl (List.Lex.rel trivial)
  | cancelDelta => exact List.Shortlex.of_length_lt (by decide)
  | cancelInverse => exact List.Shortlex.of_length_lt (by decide)

theorem gStep_wellFounded {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d) (wf : WellFounded r) :
    WellFounded (fun v u => Step (GRule T d phi r) u v) :=
  step_wellFounded (letterLT_wellFounded wf)
    (fun _ _ h => gRule_decreases T d phi r rank hrho hatom hid hbalance hN h)

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
    (T.firstHitDFA start).evalFrom none v = none := by
  induction v with
  | nil => rfl
  | cons y v ih => exact ih

theorem firstHitDFA_correct_from (start e : E) (v : List S) :
    (T.firstHitDFA start).evalFrom (some e) v = some T.identity ↔ T.FirstHit e v := by
  induction v generalizing e with
  | nil => simp [DFA.evalFrom, FirstHit]
  | cons y v ih =>
    rw [DFA.evalFrom_cons]
    by_cases he : e = T.identity
    · simp only [firstHitDFA, he, if_pos, firstHitDFA_dead, FirstHit]
      simp [he]
    · simp only [firstHitDFA, he, if_neg, FirstHit]
      exact (ih (T.next e y)).trans (by simp [he])

theorem firstHitDFA_correct (e : E) (v : List S) :
    v ∈ (T.firstHitDFA e).accepts ↔ T.FirstHit e v := by
  exact T.firstHitDFA_correct_from e e v

end ComplementTable

end ArtinG
