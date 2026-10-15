import Mathlib.Algebra.Lie.Ideal
import Mathlib.Algebra.Module.Torsion.Free
import Mathlib.Tactic.Ring
import Mathlib.Data.Nat.Find
import Mathlib.Data.Nat.Order.Lemmas

-- Serial elaboration keeps the frozen check within the computational-thread bound.
set_option Elab.async false

/-!
Checked partial results for the frozen universal Serre-equality task.
These results do not assert universal Serre equality.
The first section works for actual Lie modules, including the adjoint module.
The second section identifies a generator-bracket closure with a Lie ideal.
-/

namespace SerrePartial

section Strings

variable {K L M : Type*} [CommRing K] [LieRing L] [LieAlgebra K L]
  [AddCommGroup M] [Module K M] [LieRingModule L M] [LieModule K L M]

/-- Iteration of the genuine Lie action, with the initial vector at step zero. -/
def raise (e : L) (v : M) : ℕ → M
  | 0 => v
  | n + 1 => ⁅e, raise e v n⁆

/-- Jacobi induction gives the weight of every vector in a raising string. -/
theorem raising_weight (h e : L) (v : M) (a : K)
    (he : ⁅h, e⁆ = (2 : K) • e) (hv : ⁅h, v⁆ = a • v) (n : ℕ) :
    ⁅h, raise e v n⁆ = (a + 2 * (n : K)) • raise e v n := by sorry

/-- With the book's convention D = ad(f), the coefficient has a minus sign.
No irreducibility, dimension formula or Serre equality is assumed. -/
theorem lowering_recurrence (h e f : L) (v : M) (a : K)
    (he : ⁅h, e⁆ = (2 : K) • e) (fe : ⁅f, e⁆ = -h)
    (hv : ⁅h, v⁆ = a • v) (fv : ⁅f, v⁆ = 0) (n : ℕ) :
    ⁅f, raise e v (n + 1)⁆ =
      (-((n + 1 : ℕ) : K) * (a + (n : K))) • raise e v n := by sorry

/-- The i-lowering of the positive Serre string of exponent m+1 is zero
when its initial Cartan weight is -m. Other simple lowerings are not claimed here. -/
theorem serre_string_killed (h e f : L) (v : M) (m : ℕ)
    (he : ⁅h, e⁆ = (2 : K) • e) (fe : ⁅f, e⁆ = -h)
    (hv : ⁅h, v⁆ = -(m : K) • v) (fv : ⁅f, v⁆ = 0) :
    ⁅f, raise e v (m + 1)⁆ = 0 := by sorry

end Strings

section PrimitiveWeight

variable {K L M : Type*} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L]
  [AddCommGroup M] [Module K M] [LieRingModule L M] [LieModule K L M]

/-- Local nilpotence at one nonzero lowest vector forces its Cartan weight
to be the negative of a natural number. This is the sl2 step in A alpha ≤ 0.
Finite dimension and irreducibility of the ambient module are not hypotheses. -/
theorem primitive_weight_is_nonpositive_integer (h e f : L) (v : M) (a : K)
    (he : ⁅h, e⁆ = (2 : K) • e) (fe : ⁅f, e⁆ = -h)
    (hv : ⁅h, v⁆ = a • v) (fv : ⁅f, v⁆ = 0) (v_ne : v ≠ 0)
    (nilpotent_at_v : ∃ N : ℕ, raise e v N = 0) :
    ∃ t : ℕ, a = -(t : K) := by sorry

end PrimitiveWeight

section GradedRecurrence

variable {K L I P : Type*} [CommRing K] [LieRing L] [LieAlgebra K L]

/-- The exact recursive lowering kernels are Cartan-stable in all degrees.
P indexes every Cartan direction, not merely the simple coroots. W is an
explicit family of positive homogeneous subspaces in an ambient Lie algebra.
The recurrence itself is a hypothesis; this theorem proves its propagation. -/
theorem graded_kernel_cartan_stable
    (F : I → L) (H : P → L) (c : P → I → K)
    (W R : ℕ → Submodule K L)
    (r0 : R 0 = ⊥) (r1 : R 1 = ⊥)
    (recurrence : ∀ n x, x ∈ R (n + 2) ↔
      x ∈ W (n + 2) ∧ ∀ i, ⁅F i, x⁆ ∈ R (n + 1))
    (weight_stable : ∀ p n x, x ∈ W n → ⁅H p, x⁆ ∈ W n)
    (fh : ∀ i p, ⁅F i, H p⁆ = c p i • F i) :
    ∀ n p x, x ∈ R n → ⁅H p, x⁆ ∈ R n := by sorry

/-- The nontrivial upward-ideal step in the maximal-ideal recurrence.
Jacobi and induction convert stability under lowering into stability under
raising. Cartan stability is explicit; the preceding theorem proves it under
the homogeneous-weight hypotheses, including all extra Cartan directions. -/
theorem graded_kernel_raising_stable [DecidableEq I]
    (E F : I → L) (H : P → L) (coroot : I → P)
    (W R : ℕ → Submodule K L)
    (r0 : R 0 = ⊥) (r1 : R 1 = ⊥)
    (recurrence : ∀ n x, x ∈ R (n + 2) ↔
      x ∈ W (n + 2) ∧ ∀ i, ⁅F i, x⁆ ∈ R (n + 1))
    (raising : ∀ i n x, x ∈ W n → ⁅E i, x⁆ ∈ W (n + 1))
    (cartan_stable : ∀ n p x, x ∈ R n → ⁅H p, x⁆ ∈ R n)
    (fe : ∀ i j, ⁅F i, E j⁆ = if i = j then -H (coroot i) else 0) :
    ∀ n j x, x ∈ R n → ⁅E j, x⁆ ∈ R (n + 1) := by sorry

end GradedRecurrence

section GeneratorClosure

variable {K L : Type*} [CommRing K] [LieRing L] [LieAlgebra K L]

/-- Stability under brackets with a generating set propagates through all
Lie brackets by Jacobi; this is the step used in the positive Serre-span recurrence. -/
theorem lieSpan_stability (s : Set L) (W : Submodule K L)
    (hs : ∀ x ∈ s, ∀ y ∈ W, ⁅x, y⁆ ∈ W) :
    ∀ x ∈ LieSubalgebra.lieSpan K L s, ∀ y ∈ W, ⁅x, y⁆ ∈ W := by sorry

/-- The explicit span of seeds and repeated brackets with simple generators. -/
inductive GeneratorClosure (s t : Set L) : L → Prop
  | zero : GeneratorClosure s t 0
  | seed {x : L} : x ∈ t → GeneratorClosure s t x
  | add {x y : L} : GeneratorClosure s t x → GeneratorClosure s t y →
      GeneratorClosure s t (x + y)
  | smul (r : K) {x : L} : GeneratorClosure s t x → GeneratorClosure s t (r • x)
  | bracket {x y : L} : x ∈ s → GeneratorClosure s t y →
      GeneratorClosure s t ⁅x, y⁆

def generatorClosure (s t : Set L) : Submodule K L where
  carrier := GeneratorClosure (K := K) s t
  zero_mem' := GeneratorClosure.zero
  add_mem' := GeneratorClosure.add
  smul_mem' := GeneratorClosure.smul

/-- An actual ideal, constructed from generator stability, without assuming
stability under arbitrary elements of the Lie algebra as a structure field. -/
def idealOfGeneratorStable (s : Set L)
    (hgen : LieSubalgebra.lieSpan K L s = ⊤) (W : Submodule K L)
    (hs : ∀ x ∈ s, ∀ y ∈ W, ⁅x, y⁆ ∈ W) : LieIdeal K L :=
  { W with
    lie_mem := by
      intro x y hy
      apply lieSpan_stability s W hs x _ y hy
      rw [hgen]
      trivial }

/-- The global generator-span recurrence is exactly the Lie ideal generated
by the seeds. This concerns positive ideal generation, not the maximal ideal. -/
theorem generatorClosure_eq_lieIdeal (s t : Set L)
    (hgen : LieSubalgebra.lieSpan K L s = ⊤) :
    generatorClosure (K := K) s t =
      (LieSubmodule.lieSpan K L t : Submodule K L) := by sorry

end GeneratorClosure

end SerrePartial

