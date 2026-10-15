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
    evalWord a (u ++ v) = evalWord a u * evalWord a v := by
  simp [evalWord]

theorem evalWord_degree {S M : Type*} [Monoid M] (a : S → M) (degree : M → ℕ)
    (hone : degree 1 = 0)
    (hmul : ∀ u v, degree (u * v) = degree u + degree v)
    (hatom : ∀ s, degree (a s) = 1) (v : List S) :
    degree (evalWord a v) = v.length := by
  induction v with
  | nil => exact hone
  | cons y v ih =>
    change degree (a y * evalWord a v) = v.length + 1
    rw [hmul, hatom, ih, Nat.add_comm]

theorem evalWord_length_of_eq {S M : Type*} [Monoid M] (a : S → M) (degree : M → ℕ)
    (hone : degree 1 = 0)
    (hmul : ∀ u v, degree (u * v) = degree u + degree v)
    (hatom : ∀ s, degree (a s) = 1) {u v : List S}
    (h : evalWord a u = evalWord a v) : u.length = v.length := by
  have hd := congrArg degree h
  simpa only [evalWord_degree a degree hone hmul hatom] using hd

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
      lift v * lift (coxeterComplement join v u) := by
  have hu : rank (u * coxeterComplement join u v) =
      rank u + rank (coxeterComplement join u v) := by
    simpa only [coxeterComplement, mul_inv_cancel_left] using hprefix u v
  have hv : rank (v * coxeterComplement join v u) =
      rank v + rank (coxeterComplement join v u) := by
    simpa only [coxeterComplement, mul_inv_cancel_left] using hprefix v u
  calc
    lift u * lift (coxeterComplement join u v) = lift (join u v) := by
      rw [← hmul u _ hu, coxeterComplement, mul_inv_cancel_left]
    _ = lift (join v u) := congrArg lift (hcomm u v)
    _ = lift v * lift (coxeterComplement join v u) := by
      rw [← hmul v _ hv, coxeterComplement, mul_inv_cancel_left]

theorem join_complement_length {W : Type*} [Group W]
    (join : W → W → W) (rank : W → ℕ)
    (hcomm : ∀ u v, join u v = join v u)
    (hprefix : ∀ u v, rank (join u v) = rank u + rank (coxeterComplement join u v))
    (u v : W) :
    rank u + rank (coxeterComplement join u v) =
      rank v + rank (coxeterComplement join v u) := by
  rw [← hprefix, hcomm, hprefix]

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
        (tableOfJoin simple join rho).output (coxeterComplement join (simple x) q) v) :=
  (tableOfJoin simple join rho).accepted_output_equality a lift hrho hatom hone
    (join_complement_balance join rank lift hcomm hprefix hmul) x q v haccept

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
  | cancelDelta => exact List.Shortlex.of_length_lt (by simp)
  | cancelInverse => exact List.Shortlex.of_length_lt (by simp)

theorem gStep_wellFounded {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d) (wf : WellFounded r) :
    WellFounded (fun v u => Step (GRule T d phi r) u v) :=
  step_wellFounded (letterLT_wellFounded wf)
    (fun _ _ h => gRule_decreases T d phi r rank hrho hatom hid hbalance hN h)

theorem gStep_finite_wellFounded {S E : Type*} [Finite S] [LinearOrder S]
    (T : ComplementTable S E) (d : E) (phi : S → S) (rank : E → ℕ)
    (hrho : ∀ e, (T.rho e).length = rank e)
    (hatom : ∀ y, rank (T.atom y) = 1) (hid : rank T.identity = 0)
    (hbalance : ∀ u v, rank u + rank (T.complement u v) =
      rank v + rank (T.complement v u)) (hN : 2 ≤ rank d) :
    WellFounded (fun v u => Step (GRule T d phi (· < ·)) u v) :=
  gStep_wellFounded T d phi (· < ·) rank hrho hatom hid hbalance hN wellFounded_lt

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
    change ((T.firstHitDFA start).evalFrom
      (if e = T.identity then none else some (T.next e y)) v = some T.identity) ↔
      (e ≠ T.identity ∧ T.FirstHit (T.next e y) v)
    by_cases he : e = T.identity
    · rw [if_pos he, firstHitDFA_dead]
      simp [he]
    · rw [if_neg he, ih]
      simp [he]

theorem firstHitDFA_correct (e : E) (v : List S) :
    v ∈ (T.firstHitDFA e).accepts ↔ T.FirstHit e v := by
  exact T.firstHitDFA_correct_from e e v

end ComplementTable

def letterValue {S M : Type*} [Group M] (a : S → M) (delta : M) : Letter S → M
  | .inverse => delta⁻¹
  | .delta => delta
  | .atom s => a s

theorem eval_atomWord {S M : Type*} [Group M] (a : S → M) (delta : M) (v : List S) :
    evalWord (letterValue a delta) (atomWord v) = evalWord a v := by
  simp [evalWord, atomWord, List.map_map, Function.comp_def, letterValue]

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
    evalWord (letterValue a (value d)) u = evalWord (letterValue a (value d)) v := by
  cases h with
  | lex x t v hlt hne hhit =>
    have hv := T.accepted_output_equality a value hrho hatom hid hbalance x (T.atom t) v
      (T.firstHit_residual hhit)
    rw [hatom] at hv
    simpa only [evalWord, List.map_cons, List.prod_cons, letterValue, atomWord,
      List.map_map, Function.comp_def, ComplementTable.ruleTail] using hv
  | extract x v hne hhit =>
    have hv := T.accepted_output_equality a value hrho hatom hid hbalance x d v
      (T.firstHit_residual hhit)
    simpa only [evalWord, List.map_cons, List.prod_cons, letterValue, atomWord,
      List.map_map, Function.comp_def, ComplementTable.ruleTail] using hv
  | twistDelta x => simpa [evalWord, letterValue] using htwist x
  | twistInverse x =>
    have hi : a x * (value d)⁻¹ = (value d)⁻¹ * a (phi x) := by
      calc
        a x * (value d)⁻¹ = ((value d)⁻¹ * (a (phi x) * value d)) * (value d)⁻¹ := by
          rw [htwist, hphi]
          simp [mul_assoc]
        _ = (value d)⁻¹ * a (phi x) := by simp [mul_assoc]
    simpa [evalWord, letterValue] using hi
  | cancelDelta => simp [evalWord, letterValue]
  | cancelInverse => simp [evalWord, letterValue]

theorem step_valid {S M : Type*} [Monoid M] (a : S → M)
    {R : List S → List S → Prop}
    (hR : ∀ u v, R u v → evalWord a u = evalWord a v) {u v : List S}
    (h : Step R u v) : evalWord a u = evalWord a v := by
  cases h with
  | apply h p s => simp only [evalWord_append, hR _ _ h]

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
    ∃ t, r t x ∧ LeftDivides (a t) (evalWord a (x :: v)) := by
  rcases List.shortlex_def.mp hlt with hl | ⟨_, hl⟩
  · omega
  cases hl with
  | nil => simp at hlen
  | @rel t u x v htx =>
    exact ⟨t, htx, evalWord a u, by simpa [evalWord] using heq.symm⟩
  | @cons x u v htail =>
    have he : evalWord a u = evalWord a v := by simpa [evalWord] using heq
    have hn : u.length = v.length := by simpa using hlen
    exact (hsuffix u he (List.Shortlex.of_lex hn htail)).elim

theorem normal_no_smaller_head {S M : Type*} [Monoid M]
    (a : S → M) (delta : M) (r : S → S → Prop)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (x t : S) (v : List S) (hlt : r t x)
    (hnormal : PositiveNormal a delta r (x :: v)) :
    ¬ LeftDivides (a t) (evalWord a (x :: v)) := by
  rintro ⟨h, he⟩
  obtain ⟨w, hw⟩ := hgenerated h
  have heq : evalWord a (t :: w) = evalWord a (x :: v) := by
    simpa [evalWord, ← hw] using he.symm
  exact hnormal.1 (t :: w) heq
    (List.Shortlex.of_lex (hhomogeneous _ _ heq) (List.Lex.rel hlt))

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
    ∃ o, GRule T d phi r (Letter.atom x :: atomWord v) o := by
  classical
  by_cases hd : LeftDivides (value d) (evalWord a (x :: v))
  · have hh := T.target_firstHit a value hatom hlcm hunit x d v hd
      (fun u w he hw => (hprefix u w he hw).2)
    exact ⟨_, GRule.extract x v hne hh⟩
  · have hlex : ¬ ∀ u, evalWord a u = evalWord a (x :: v) →
        ¬ List.Shortlex r u (x :: v) := fun h => hnot ⟨h, hd⟩
    push Not at hlex
    obtain ⟨u, heq, hlt⟩ := hlex
    obtain ⟨t, htx, ht⟩ := smaller_atom_target a r x v u hsuffix.1 heq
      (hhomogeneous _ _ heq) hlt
    have ht' : LeftDivides (value (T.atom t)) (evalWord a (x :: v)) := by
      simpa only [hatom] using ht
    have hh := T.target_firstHit a value hatom hlcm hunit x (T.atom t) v ht' (by
      intro u w he hw
      simpa only [hatom] using normal_no_smaller_head a (value d) r hgenerated
        hhomogeneous x t u htx (hprefix u w he hw))
    exact ⟨_, GRule.lex x t v htx hne hh⟩

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

theorem rho_value : ∀ e, evalWord atom (table.rho e) = value e := by decide
theorem atom_value : ∀ y, value (table.atom y) = atom y := by decide
theorem identity_value : value table.identity = 1 := by decide
theorem complement_balance : ∀ u v, value u * value (table.complement u v) =
    value v * value (table.complement v u) := by decide
theorem rho_length : ∀ e, (table.rho e).length = rank e := by decide
theorem atom_length : ∀ y, rank (table.atom y) = 1 := by decide
theorem identity_length : rank table.identity = 0 := by decide
theorem complement_length : ∀ u v, rank u + rank (table.complement u v) =
    rank v + rank (table.complement v u) := by decide

theorem loop_run (n : ℕ) :
    table.residual (false, true) (List.replicate n false ++ [true]) = table.identity ∧
    table.output (false, true) (List.replicate n false ++ [true]) = List.replicate n false ∧
    table.FirstHit (false, true) (List.replicate n false ++ [true]) := by
  induction n with
  | zero => simp [ComplementTable.residual, ComplementTable.output, ComplementTable.FirstHit,
      ComplementTable.next, ComplementTable.emit, table]
  | succ n ih =>
    simpa [List.replicate_succ, ComplementTable.residual, ComplementTable.output,
      ComplementTable.FirstHit, ComplementTable.next, ComplementTable.emit, table] using ih

theorem loop_tail (n : ℕ) :
    table.ruleTail false (true, true) (List.replicate n false ++ [true]) =
      List.replicate n false := by
  change [] ++ table.output (false, true) (List.replicate n false ++ [true]) = _
  exact (loop_run n).2.1

theorem loop_rule_valid (n : ℕ) :
    evalWord atom (false :: (List.replicate n false ++ [true])) =
      value (true, true) * evalWord atom (List.replicate n false) := by
  have ht := table.accepted_output_equality atom value rho_value atom_value identity_value
    complement_balance false (true, true) (List.replicate n false ++ [true]) (loop_run n).1
  change evalWord atom (false :: (List.replicate n false ++ [true])) =
    value (true, true) * evalWord atom
      (table.ruleTail false (true, true) (List.replicate n false ++ [true])) at ht
  rwa [loop_tail] at ht

theorem loop_rule_decreases (n : ℕ) :
    List.Shortlex (letterLT (fun s t : Bool => s = false ∧ t = true))
      (Letter.delta :: atomWord (List.replicate n false))
      (Letter.atom false :: atomWord (List.replicate n false ++ [true])) := by
  have ht := table.delta_rule_decreases (fun s t : Bool => s = false ∧ t = true)
    rank rho_length atom_length identity_length
    complement_length (true, true) (by decide) false
    (List.replicate n false ++ [true]) (loop_run n).1
  simpa only [loop_tail] using ht

theorem lost_loop_output_is_wrong :
    evalWord atom [false, false, true] ≠ value (true, true) * evalWord atom [] := by decide

end CommutingExample

namespace EmptySystem

/-- In rank zero, Delta and its inverse both represent the identity. -/
def Rule : List (Letter PEmpty) → List (Letter PEmpty) → Prop
  | u, v => (u = [.delta] ∧ v = []) ∨ (u = [.inverse] ∧ v = [])

theorem rule_decreases (u v : List (Letter PEmpty)) (h : Rule u v) :
    List.Shortlex (letterLT (fun _ _ => False)) v u := by
  rcases h with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ <;>
    exact List.Shortlex.of_length_lt (by simp)

theorem step_wellFounded : WellFounded (fun v u => Step Rule u v) :=
  ArtinG.step_wellFounded (letterLT_wellFounded ⟨fun a => nomatch a⟩) rule_decreases

theorem reduces_to_nil (w : List (Letter PEmpty)) :
    Relation.ReflTransGen (Step Rule) w [] := by
  induction w with
  | nil => exact .refl
  | cons a w ih =>
    have hs : Step Rule (a :: w) w := by
      cases a with
      | delta =>
        simpa only [List.nil_append, List.singleton_append] using
          (Step.apply (R := Rule) (Or.inl ⟨rfl, rfl⟩) [] w)
      | inverse =>
        simpa only [List.nil_append, List.singleton_append] using
          (Step.apply (R := Rule) (Or.inr ⟨rfl, rfl⟩) [] w)
      | atom a => exact nomatch a
    exact (Relation.ReflTransGen.single hs).trans ih

theorem irreducible_iff_nil (w : List (Letter PEmpty)) :
    (∀ v, ¬ Step Rule w v) ↔ w = [] := by
  constructor
  · intro hn
    cases w with
    | nil => rfl
    | cons a w =>
      have hs : Step Rule (a :: w) w := by
        cases a with
        | delta =>
          simpa only [List.nil_append, List.singleton_append] using
            (Step.apply (R := Rule) (Or.inl ⟨rfl, rfl⟩) [] w)
        | inverse =>
          simpa only [List.nil_append, List.singleton_append] using
            (Step.apply (R := Rule) (Or.inr ⟨rfl, rfl⟩) [] w)
        | atom a => exact nomatch a
      exact (hn w hs).elim
  · rintro rfl v hv
    exact List.not_shortlex_nil_right (step_decreases rule_decreases hv)

theorem confluent {w u v : List (Letter PEmpty)}
    (_hu : Relation.ReflTransGen (Step Rule) w u)
    (_hv : Relation.ReflTransGen (Step Rule) w v) :
    ∃ z, Relation.ReflTransGen (Step Rule) u z ∧ Relation.ReflTransGen (Step Rule) v z :=
  ⟨[], reduces_to_nil u, reduces_to_nil v⟩

end EmptySystem

end ArtinG

namespace ArtinG
namespace Completeness

def Irreducible {A : Type*} (R : List A → List A → Prop) (w : List A) : Prop :=
  ∀ v, ¬ Step R w v

theorem irreducible_factor {A : Type*} {R : List A → List A → Prop}
    (p u s : List A) (h : Irreducible R (p ++ u ++ s)) : Irreducible R u := by
  intro v hv
  cases hv with
  | apply hr a b =>
    apply h (p ++ (a ++ _ ++ b) ++ s)
    simpa only [List.append_assoc] using Step.apply hr (p ++ a) (b ++ s)

/-- Existence by termination only; no joining hypothesis. Adapted from the
audited OAI FiniteCompiler exists_irreducible argument. -/
theorem exists_irreducible {A : Type*} (R : List A → List A → Prop)
    (wf : WellFounded (fun v u => Step R u v)) (w : List A) :
    ∃ z, Relation.ReflTransGen (Step R) w z ∧ Irreducible R z := by
  classical
  induction w using wf.induction with
  | h w ih =>
    by_cases hw : Irreducible R w
    · exact ⟨w, .refl, hw⟩
    · obtain ⟨v, hv⟩ := not_forall.mp hw
      have hv : Step R w v := Classical.not_not.mp hv
      obtain ⟨z, hvz, hz⟩ := ih v hv
      exact ⟨z, (Relation.ReflTransGen.single hv).trans hvz, hz⟩

theorem steps_valid {A M : Type*} [Monoid M] (a : A → M)
    {R : List A → List A → Prop}
    (hR : ∀ u v, R u v → evalWord a u = evalWord a v) {u v : List A}
    (h : Relation.ReflTransGen (Step R) u v) : evalWord a u = evalWord a v := by
  induction h with
  | refl => rfl
  | tail h hs ih => exact ih.trans (step_valid a hR hs)

theorem no_return {A : Type*} (R : List A → List A → Prop)
    (wf : WellFounded (fun v u => Step R u v)) (w : List A) :
    ∀ v, Step R w v → ¬ Relation.ReflTransGen (Step R) v w := by
  induction w using wf.induction with
  | h w ih =>
    intro v hwv hvw
    rcases hvw.cases_head with he | ⟨z, hvz, hzw⟩
    · subst v
      exact wf.irrefl.irrefl w hwv
    · exact ih v hwv z hvz (hzw.trans (Relation.ReflTransGen.single hwv))

theorem twist_word {S M : Type*} [Monoid M] (a : S → M) (D : M) (phi : S → S)
    (htwist : ∀ x, a x * D = D * a (phi x)) (p : List S) :
    evalWord a p * D = D * evalWord a (p.map phi) := by
  induction p with
  | nil => simp [evalWord]
  | cons x p ih =>
    change (a x * evalWord a p) * D = D * (a (phi x) * evalWord a (p.map phi))
    rw [mul_assoc, ih, ← mul_assoc, htwist, mul_assoc]

theorem positiveNormal_factor {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (phi : S → S) (r : S → S → Prop)
    (htwist : ∀ x, a x * D = D * a (phi x)) (p u s : List S)
    (hn : PositiveNormal a D r (p ++ u ++ s)) : PositiveNormal a D r u := by
  constructor
  · intro v heq hlt
    apply hn.1 (p ++ v ++ s)
    · simp only [evalWord_append, heq]
    · exact shortlex_context hlt p s
  · rintro ⟨h, hh⟩
    apply hn.2
    refine ⟨evalWord a (p.map phi) * h * evalWord a s, ?_⟩
    rw [evalWord_append, evalWord_append, hh, ← mul_assoc (evalWord a p),
      twist_word a D phi htwist p]
    simp only [mul_assoc]

theorem delta_not_divides_short {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (rhoD : List S)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (p : List S) (hp : p.length ≤ 1) : ¬ LeftDivides D (evalWord a p) := by
  rintro ⟨h, hh⟩
  obtain ⟨w, hw⟩ := hgenerated h
  have he : evalWord a (rhoD ++ w) = evalWord a p := by
    rw [evalWord_append, hrhoD, hw, ← hh]
  have hl := hhomogeneous _ _ he
  simp only [List.length_append] at hl
  omega

theorem positiveNormal_nil {S M : Type*} [Monoid M]
    (a : S → M) (D : M) (rhoD : List S) (r : S → S → Prop)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length) :
    PositiveNormal a D r [] :=
  ⟨fun _ _ => List.not_shortlex_nil_right,
    delta_not_divides_short a D rhoD hrhoD hN hgenerated hhomogeneous [] (by simp)⟩

theorem positiveNormal_atom {S M : Type*} [Finite S] [LinearOrder S] [Monoid M]
    (a : S → M) (D : M) (rhoD : List S)
    (hrhoD : evalWord a rhoD = D) (hN : 2 ≤ rhoD.length)
    (hgenerated : ∀ h : M, ∃ w, evalWord a w = h)
    (hhomogeneous : ∀ u v, evalWord a u = evalWord a v → u.length = v.length)
    (hinj : Function.Injective a) (x : S) : PositiveNormal a D (· < ·) [x] := by
  constructor
  · intro u he hlt
    have hl : u.length = 1 := by simpa using hhomogeneous u [x] he
    cases u with
    | nil => simp at hl
    | cons t u =>
      have hu : u = [] := by
        cases u with
        | nil => rfl
        | cons y v => simp at hl
      subst u
      have ht : t = x := hinj (by simpa [evalWord] using he)
      subst t
      exact (List.Shortlex.wf wellFounded_lt).irrefl.irrefl [x] hlt
  · exact delta_not_divides_short a D rhoD hrhoD hN hgenerated hhomogeneous [x] (by simp)

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
    PositiveNormal a (value d) (· < ·) w := by
  classical
  induction w using (measure List.length).wf.induction with
  | h w ih =>
    cases w with
    | nil =>
      exact positiveNormal_nil a (value d) (T.rho d) (· < ·)
        (hrho d) hN hgenerated hhomogeneous
    | cons x v =>
      cases v with
      | nil =>
        exact positiveNormal_atom a (value d) (T.rho d)
          (hrho d) hN hgenerated hhomogeneous hinj x
      | cons y v =>
        by_contra hn
        have hs : PositiveNormal a (value d) (· < ·) (y :: v) := by
          apply ih (y :: v) (by change (y :: v).length < (x :: y :: v).length; simp)
          simpa [atomWord] using irreducible_factor [Letter.atom x] (atomWord (y :: v)) []
            (by simpa [atomWord] using hw)
        have hp : ∀ u s, y :: v = u ++ s → s ≠ [] →
            PositiveNormal a (value d) (· < ·) (x :: u) := by
          intro u s he hne
          apply ih (x :: u) (by
            change (x :: u).length < (x :: y :: v).length
            have hslen : 0 < s.length := List.length_pos_iff.mpr hne
            have helen := congrArg List.length he
            simp only [List.length_cons, List.length_append] at *
            omega)
          apply irreducible_factor [] (atomWord (x :: u)) (atomWord s)
          simpa [atomWord, ← List.map_append, he] using hw
        obtain ⟨o, ho⟩ := minimal_positive_rule_coverage T d phi (· < ·) a value
          hatom hlcm hunit hgenerated hhomogeneous x (y :: v) (by simp) hn hs hp
        exact hw o (by simpa [atomWord] using Step.apply ho [] [])

def signLetter {S : Type*} (s : Bool) : Letter S := if s then .delta else .inverse

/-- The twists and cancellations alone force a uniform signed prefix followed
by a genuine atom word. This does not assume a group normal form. -/
theorem irreducible_shape {S E : Type*} (T : ComplementTable S E) (d : E)
    (phi : S → S) (r : S → S → Prop) (w : List (Letter S))
    (hw : Irreducible (GRule T d phi r) w) :
    ∃ s n p, w = List.replicate n (signLetter s) ++ atomWord p := by
  induction w with
  | nil => exact ⟨true, 0, [], rfl⟩
  | cons c w ih =>
    have htail : Irreducible (GRule T d phi r) w := by
      simpa using irreducible_factor [c] w [] (by simpa using hw)
    obtain ⟨s, n, p, he⟩ := ih htail
    subst w
    have forbidden (l : List (Letter S)) (o : List (Letter S))
        (hl : GRule T d phi r l o) (tail : List (Letter S))
        (he : c :: (List.replicate n (signLetter s) ++ atomWord p) = l ++ tail) : False := by
      apply hw (o ++ tail)
      simpa only [List.nil_append, he] using Step.apply hl [] tail
    cases n with
    | zero =>
      cases c with
      | delta => exact ⟨true, 1, p, rfl⟩
      | inverse => exact ⟨false, 1, p, rfl⟩
      | atom x => exact ⟨true, 0, x :: p, rfl⟩
    | succ n =>
      cases s with
      | false =>
        cases c with
        | inverse => exact ⟨false, n + 2, p, rfl⟩
        | delta => exact (forbidden _ _ GRule.cancelDelta
            (List.replicate n Letter.inverse ++ atomWord p) rfl).elim
        | atom x => exact (forbidden _ _ (GRule.twistInverse x)
            (List.replicate n Letter.inverse ++ atomWord p) rfl).elim
      | true =>
        cases c with
        | delta => exact ⟨true, n + 2, p, rfl⟩
        | inverse => exact (forbidden _ _ GRule.cancelInverse
            (List.replicate n Letter.delta ++ atomWord p) rfl).elim
        | atom x => exact (forbidden _ _ (GRule.twistDelta x)
            (List.replicate n Letter.delta ++ atomWord p) rfl).elim

def deltaPower {S : Type*} (k : ℤ) : List (Letter S) :=
  if 0 ≤ k then List.replicate k.toNat .delta else List.replicate (-k).toNat .inverse

theorem deltaPower_nat {S : Type*} (n : ℕ) :
    deltaPower (S := S) (n : ℤ) = List.replicate n .delta := by simp [deltaPower]

theorem deltaPower_neg_nat {S : Type*} (n : ℕ) :
    deltaPower (S := S) (-(n : ℤ)) = List.replicate n .inverse := by
  cases n with
  | zero => simp [deltaPower]
  | succ n =>
    have hn : ¬ (0 : ℤ) ≤ -((n + 1 : ℕ) : ℤ) := by omega
    simp only [deltaPower, if_neg hn, neg_neg, Int.toNat_natCast]

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
    NF a (value d) (· < ·) w := by
  obtain ⟨s, n, p, he⟩ := irreducible_shape T d phi (· < ·) w hw
  have hp : Irreducible (GRule T d phi (· < ·)) (atomWord p) := by
    apply irreducible_factor (List.replicate n (signLetter s)) (atomWord p) []
    simpa [← he] using hw
  have hn := positive_normal_of_irreducible T d phi a value hrho hatom hlcm hunit
    hgenerated hhomogeneous hinj hN p hp
  cases s with
  | true => exact ⟨(n : ℤ), p, by simpa [deltaPower_nat, signLetter] using he, hn⟩
  | false => exact ⟨-(n : ℤ), p, by simpa [deltaPower_neg_nat, signLetter] using he, hn⟩

theorem evalWord_map {S M G : Type*} [Monoid M] [Monoid G]
    (iota : M →* G) (a : S → M) (p : List S) :
    iota (evalWord a p) = evalWord (fun s => iota (a s)) p := by
  induction p with
  | nil => exact map_one iota
  | cons s p ih =>
    change iota (a s * evalWord a p) = iota (a s) * evalWord (fun s => iota (a s)) p
    rw [map_mul, ih]

theorem eval_deltaPower {S G : Type*} [Group G] (a : S → G) (D : G) (k : ℤ) :
    evalWord (letterValue a D) (deltaPower k) = D ^ k := by
  cases k with
  | ofNat n => simp [deltaPower, evalWord, letterValue]
  | negSucc n => simp [deltaPower, evalWord, letterValue, zpow_negSucc]

theorem positiveNormal_injective {S M : Type*} [LinearOrder S] [Monoid M]
    (a : S → M) (D : M) {p q : List S}
    (hp : PositiveNormal a D (· < ·) p) (hq : PositiveNormal a D (· < ·) q)
    (he : evalWord a p = evalWord a q) : p = q := by
  rcases trichotomous_of (List.Shortlex (· < ·)) p q with h | h | h
  · exact (hq.1 p he h).elim
  · exact h
  · exact (hp.1 q he.symm h).elim

theorem normalForm_value_injective {S M G : Type*} [LinearOrder S] [Monoid M] [Group G]
    (iota : M →* G) (a : S → M) (D : M)
    (hG5 : ∀ (k k' : ℤ) (p p' : M), ¬ LeftDivides D p → ¬ LeftDivides D p' →
      (iota D) ^ k * iota p = (iota D) ^ k' * iota p' → k = k' ∧ p = p')
    {u v : List (Letter S)} (hu : NF a D (· < ·) u) (hv : NF a D (· < ·) v)
    (he : evalWord (letterValue (fun s => iota (a s)) (iota D)) u =
      evalWord (letterValue (fun s => iota (a s)) (iota D)) v) : u = v := by
  obtain ⟨k, p, hu, hp⟩ := hu
  obtain ⟨k', q, hv, hq⟩ := hv
  have hev : (iota D) ^ k * iota (evalWord a p) =
      (iota D) ^ k' * iota (evalWord a q) := by
    simpa only [hu, hv, evalWord_append, eval_deltaPower, eval_atomWord, ← evalWord_map] using he
  obtain ⟨hk, hpq⟩ := hG5 k k' (evalWord a p) (evalWord a q) hp.2 hq.2 hev
  have hpq := positiveNormal_injective a D hp hq hpq
  subst k'
  subst q
  exact hu.trans hv.symm

theorem embedding_left_cancel {M G : Type*} [Monoid M] [Group G]
    (iota : M →* G) (hi : Function.Injective iota) (a b c : M) (h : a * b = a * c) : b = c := by
  apply hi
  have hh := congrArg iota h
  simpa only [map_mul, mul_left_cancel_iff] using hh

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
      Relation.ReflTransGen (Step (GRule T d phi (· < ·))) v z := by
  let F := letterValue (fun s => iota (a s)) (iota (value d))
  have valid : ∀ u v, GRule T d phi (· < ·) u v → evalWord F u = evalWord F v := by
    intro u v h
    apply gRule_valid T d phi (· < ·) (fun s => iota (a s)) (fun e => iota (value e))
      (fun e => by rw [← evalWord_map, hrho])
      (fun y => by rw [hatom]) (by rw [hid, map_one])
      (fun u v => by simpa only [map_mul] using congrArg iota (hbalance u v))
      hphi (fun x => by simpa only [map_mul] using congrArg iota (htwist x)) h
  have wf := gStep_finite_wellFounded T d phi rank hrank hatomrank hidrank hbalanceRank hN
  have covered := irreducible_normalForm T d phi a value hrho hatom hlcm hunit
    hgenerated hhomogeneous hinj (by simpa only [hrank] using hN)
  constructor
  · intro he
    obtain ⟨p, hup, hp⟩ := exists_irreducible (GRule T d phi (· < ·)) wf u
    obtain ⟨q, hvq, hq⟩ := exists_irreducible (GRule T d phi (· < ·)) wf v
    have hpq : p = q := normalForm_value_injective iota a (value d) hG5
      (covered p hp) (covered q hq)
      ((steps_valid F valid hup).symm.trans (he.trans (steps_valid F valid hvq)))
    exact ⟨p, hup, hpq ▸ hvq⟩
  · rintro ⟨z, huz, hvz⟩
    exact (steps_valid F valid huz).trans (steps_valid F valid hvz).symm

theorem conditional_irreducible_iff_nf (w : List (Letter S)) :
    Irreducible (GRule T d phi (· < ·)) w ↔ NF a (value d) (· < ·) w := by
  have wf := gStep_finite_wellFounded T d phi rank hrank hatomrank hidrank hbalanceRank hN
  have covered := irreducible_normalForm T d phi a value hrho hatom hlcm hunit
    hgenerated hhomogeneous hinj (by simpa only [hrank] using hN)
  constructor
  · exact covered w
  · intro hn v hwv
    obtain ⟨z, hvz, hz⟩ := exists_irreducible (GRule T d phi (· < ·)) wf v
    have hwz := (Relation.ReflTransGen.single hwv).trans hvz
    have he := (conditional_equal_iff_join T d phi a value rank iota hrho hatom hid
      hbalance hrank hatomrank hidrank hbalanceRank hN hlcm hunit hgenerated hhomogeneous
      hinj hphi htwist hG5 w z).mpr ⟨z, hwz, .refl⟩
    have heq := normalForm_value_injective iota a (value d) hG5 hn (covered z hz) he
    exact no_return (GRule T d phi (· < ·)) wf w v hwv (heq ▸ hvz)

theorem conditional_confluent {w u v : List (Letter S)}
    (hu : Relation.ReflTransGen (Step (GRule T d phi (· < ·))) w u)
    (hv : Relation.ReflTransGen (Step (GRule T d phi (· < ·))) w v) :
    ∃ z, Relation.ReflTransGen (Step (GRule T d phi (· < ·))) u z ∧
      Relation.ReflTransGen (Step (GRule T d phi (· < ·))) v z := by
  have equiv := conditional_equal_iff_join T d phi a value rank iota hrho hatom hid
    hbalance hrank hatomrank hidrank hbalanceRank hN hlcm hunit hgenerated hhomogeneous
    hinj hphi htwist hG5
  exact (equiv u v).mp (((equiv w u).mpr ⟨u, hu, .refl⟩).symm.trans
    ((equiv w v).mpr ⟨v, hv, .refl⟩))

end Conditional

end Completeness
end ArtinG

namespace ArtinG.NoncommutingControl

/-- A genuine noncommutative quotient of the type-A2 Artin group. -/
def atom (y : Bool) : Equiv.Perm (Fin 3) :=
  if y then Equiv.swap 1 2 else Equiv.swap 0 1

theorem braid_relation :
    evalWord atom [false, true, false] = evalWord atom [true, false, true] := by decide

/-- The A2 complement path has residuals ab,b,ba,ba,a,1 and emits
epsilon,ab,b,epsilon,epsilon after initial output aba. -/
theorem accepted_output :
    evalWord atom [true, false, false, false, true, false] =
      evalWord atom [false, true, false, false, true, true] := by decide

theorem reversed_blocks_wrong :
    evalWord atom [true, false, false, false, true, false] ≠
      evalWord atom [false, true, false, true, false, true] := by decide

end ArtinG.NoncommutingControl

set_option pp.proofs false
set_option pp.universes false

#print ArtinG.ComplementTable
#print ArtinG.coxeterComplement
#print ArtinG.tableOfJoin
#print ArtinG.ComplementTable.residual
#print ArtinG.ComplementTable.output
#print ArtinG.GRule
#print ArtinG.PositiveNormal
#print ArtinG.evalWord_append
#print axioms ArtinG.evalWord_append
#print ArtinG.evalWord_degree
#print axioms ArtinG.evalWord_degree
#print ArtinG.evalWord_length_of_eq
#print axioms ArtinG.evalWord_length_of_eq
#print ArtinG.ComplementTable.path_iff
#print axioms ArtinG.ComplementTable.path_iff
#print ArtinG.ComplementTable.residual_append
#print axioms ArtinG.ComplementTable.residual_append
#print ArtinG.ComplementTable.output_append
#print axioms ArtinG.ComplementTable.output_append
#print ArtinG.ComplementTable.firstHit_residual
#print axioms ArtinG.ComplementTable.firstHit_residual
#print ArtinG.ComplementTable.firstHit_of_proper_prefixes
#print axioms ArtinG.ComplementTable.firstHit_of_proper_prefixes
#print ArtinG.ComplementTable.telescoping
#print axioms ArtinG.ComplementTable.telescoping
#print ArtinG.ComplementTable.accepted_output_equality
#print axioms ArtinG.ComplementTable.accepted_output_equality
#print ArtinG.ComplementTable.output_length_balance
#print axioms ArtinG.ComplementTable.output_length_balance
#print ArtinG.ComplementTable.accepted_output_length
#print axioms ArtinG.ComplementTable.accepted_output_length
#print ArtinG.join_complement_balance
#print axioms ArtinG.join_complement_balance
#print ArtinG.join_complement_length
#print axioms ArtinG.join_complement_length
#print ArtinG.join_accepted_output_equality
#print axioms ArtinG.join_accepted_output_equality
#print ArtinG.complement_divides_iff
#print axioms ArtinG.complement_divides_iff
#print ArtinG.ComplementTable.residual_divisibility
#print axioms ArtinG.ComplementTable.residual_divisibility
#print ArtinG.ComplementTable.acceptance_iff_divides
#print axioms ArtinG.ComplementTable.acceptance_iff_divides
#print ArtinG.ComplementTable.target_firstHit
#print axioms ArtinG.ComplementTable.target_firstHit
#print ArtinG.simple_divides_one_iff
#print axioms ArtinG.simple_divides_one_iff
#print ArtinG.letterLT_wellFounded
#print axioms ArtinG.letterLT_wellFounded
#print ArtinG.lex_append_suffix
#print axioms ArtinG.lex_append_suffix
#print ArtinG.shortlex_context
#print axioms ArtinG.shortlex_context
#print ArtinG.step_decreases
#print axioms ArtinG.step_decreases
#print ArtinG.step_wellFounded
#print axioms ArtinG.step_wellFounded
#print ArtinG.ComplementTable.atom_rule_decreases
#print axioms ArtinG.ComplementTable.atom_rule_decreases
#print ArtinG.ComplementTable.delta_rule_decreases
#print axioms ArtinG.ComplementTable.delta_rule_decreases
#print ArtinG.gRule_decreases
#print axioms ArtinG.gRule_decreases
#print ArtinG.gStep_wellFounded
#print axioms ArtinG.gStep_wellFounded
#print ArtinG.gStep_finite_wellFounded
#print axioms ArtinG.gStep_finite_wellFounded
#print ArtinG.ComplementTable.firstHitDFA_dead
#print axioms ArtinG.ComplementTable.firstHitDFA_dead
#print ArtinG.ComplementTable.firstHitDFA_correct_from
#print axioms ArtinG.ComplementTable.firstHitDFA_correct_from
#print ArtinG.ComplementTable.firstHitDFA_correct
#print axioms ArtinG.ComplementTable.firstHitDFA_correct
#print ArtinG.eval_atomWord
#print axioms ArtinG.eval_atomWord
#print ArtinG.gRule_valid
#print axioms ArtinG.gRule_valid
#print ArtinG.step_valid
#print axioms ArtinG.step_valid
#print ArtinG.smaller_atom_target
#print axioms ArtinG.smaller_atom_target
#print ArtinG.normal_no_smaller_head
#print axioms ArtinG.normal_no_smaller_head
#print ArtinG.minimal_positive_rule_coverage
#print axioms ArtinG.minimal_positive_rule_coverage
#print ArtinG.CommutingExample.rho_value
#print axioms ArtinG.CommutingExample.rho_value
#print ArtinG.CommutingExample.atom_value
#print axioms ArtinG.CommutingExample.atom_value
#print ArtinG.CommutingExample.identity_value
#print axioms ArtinG.CommutingExample.identity_value
#print ArtinG.CommutingExample.complement_balance
#print axioms ArtinG.CommutingExample.complement_balance
#print ArtinG.CommutingExample.rho_length
#print axioms ArtinG.CommutingExample.rho_length
#print ArtinG.CommutingExample.atom_length
#print axioms ArtinG.CommutingExample.atom_length
#print ArtinG.CommutingExample.identity_length
#print axioms ArtinG.CommutingExample.identity_length
#print ArtinG.CommutingExample.complement_length
#print axioms ArtinG.CommutingExample.complement_length
#print ArtinG.CommutingExample.loop_run
#print axioms ArtinG.CommutingExample.loop_run
#print ArtinG.CommutingExample.loop_tail
#print axioms ArtinG.CommutingExample.loop_tail
#print ArtinG.CommutingExample.loop_rule_valid
#print axioms ArtinG.CommutingExample.loop_rule_valid
#print ArtinG.CommutingExample.loop_rule_decreases
#print axioms ArtinG.CommutingExample.loop_rule_decreases
#print ArtinG.CommutingExample.lost_loop_output_is_wrong
#print axioms ArtinG.CommutingExample.lost_loop_output_is_wrong
#print ArtinG.EmptySystem.rule_decreases
#print axioms ArtinG.EmptySystem.rule_decreases
#print ArtinG.EmptySystem.step_wellFounded
#print axioms ArtinG.EmptySystem.step_wellFounded
#print ArtinG.EmptySystem.reduces_to_nil
#print axioms ArtinG.EmptySystem.reduces_to_nil
#print ArtinG.EmptySystem.irreducible_iff_nil
#print axioms ArtinG.EmptySystem.irreducible_iff_nil
#print ArtinG.EmptySystem.confluent
#print axioms ArtinG.EmptySystem.confluent
#print ArtinG.Completeness.irreducible_factor
#print axioms ArtinG.Completeness.irreducible_factor
#print ArtinG.Completeness.exists_irreducible
#print axioms ArtinG.Completeness.exists_irreducible
#print ArtinG.Completeness.steps_valid
#print axioms ArtinG.Completeness.steps_valid
#print ArtinG.Completeness.no_return
#print axioms ArtinG.Completeness.no_return
#print ArtinG.Completeness.twist_word
#print axioms ArtinG.Completeness.twist_word
#print ArtinG.Completeness.positiveNormal_factor
#print axioms ArtinG.Completeness.positiveNormal_factor
#print ArtinG.Completeness.delta_not_divides_short
#print axioms ArtinG.Completeness.delta_not_divides_short
#print ArtinG.Completeness.positiveNormal_nil
#print axioms ArtinG.Completeness.positiveNormal_nil
#print ArtinG.Completeness.positiveNormal_atom
#print axioms ArtinG.Completeness.positiveNormal_atom
#print ArtinG.Completeness.positive_normal_of_irreducible
#print axioms ArtinG.Completeness.positive_normal_of_irreducible
#print ArtinG.Completeness.irreducible_shape
#print axioms ArtinG.Completeness.irreducible_shape
#print ArtinG.Completeness.deltaPower_nat
#print axioms ArtinG.Completeness.deltaPower_nat
#print ArtinG.Completeness.deltaPower_neg_nat
#print axioms ArtinG.Completeness.deltaPower_neg_nat
#print ArtinG.Completeness.irreducible_normalForm
#print axioms ArtinG.Completeness.irreducible_normalForm
#print ArtinG.Completeness.evalWord_map
#print axioms ArtinG.Completeness.evalWord_map
#print ArtinG.Completeness.eval_deltaPower
#print axioms ArtinG.Completeness.eval_deltaPower
#print ArtinG.Completeness.positiveNormal_injective
#print axioms ArtinG.Completeness.positiveNormal_injective
#print ArtinG.Completeness.normalForm_value_injective
#print axioms ArtinG.Completeness.normalForm_value_injective
#print ArtinG.Completeness.embedding_left_cancel
#print axioms ArtinG.Completeness.embedding_left_cancel
#print ArtinG.Completeness.conditional_equal_iff_join
#print axioms ArtinG.Completeness.conditional_equal_iff_join
#print ArtinG.Completeness.conditional_irreducible_iff_nf
#print axioms ArtinG.Completeness.conditional_irreducible_iff_nf
#print ArtinG.Completeness.conditional_confluent
#print axioms ArtinG.Completeness.conditional_confluent
#print ArtinG.NoncommutingControl.braid_relation
#print axioms ArtinG.NoncommutingControl.braid_relation
#print ArtinG.NoncommutingControl.accepted_output
#print axioms ArtinG.NoncommutingControl.accepted_output
#print ArtinG.NoncommutingControl.reversed_blocks_wrong
#print axioms ArtinG.NoncommutingControl.reversed_blocks_wrong
