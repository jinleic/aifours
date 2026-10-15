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
    ⁅h, raise e v n⁆ = (a + 2 * (n : K)) • raise e v n := by
  induction n with
  | zero => simpa [raise] using hv
  | succ n ih =>
    simp only [raise, leibniz_lie, he, smul_lie, ih, lie_smul]
    rw [← add_smul]
    congr 1
    push_cast
    ring

/-- With the book's convention D = ad(f), the coefficient has a minus sign.
No irreducibility, dimension formula or Serre equality is assumed. -/
theorem lowering_recurrence (h e f : L) (v : M) (a : K)
    (he : ⁅h, e⁆ = (2 : K) • e) (fe : ⁅f, e⁆ = -h)
    (hv : ⁅h, v⁆ = a • v) (fv : ⁅f, v⁆ = 0) (n : ℕ) :
    ⁅f, raise e v (n + 1)⁆ =
      (-((n + 1 : ℕ) : K) * (a + (n : K))) • raise e v n := by
  induction n with
  | zero =>
    simp [raise, leibniz_lie, fe, hv, fv]
  | succ n ih =>
    change ⁅f, ⁅e, raise e v (n + 1)⁆⁆ = _
    rw [leibniz_lie, fe, neg_lie, raising_weight h e v a he hv, ih, lie_smul]
    change -((a + 2 * ((n + 1 : ℕ) : K)) • raise e v (n + 1)) +
      (-((n + 1 : ℕ) : K) * (a + (n : K))) • raise e v (n + 1) = _
    rw [← neg_smul, ← add_smul]
    congr 1
    push_cast
    ring

/-- The i-lowering of the positive Serre string of exponent m+1 is zero
when its initial Cartan weight is -m. Other simple lowerings are not claimed here. -/
theorem serre_string_killed (h e f : L) (v : M) (m : ℕ)
    (he : ⁅h, e⁆ = (2 : K) • e) (fe : ⁅f, e⁆ = -h)
    (hv : ⁅h, v⁆ = -(m : K) • v) (fv : ⁅f, v⁆ = 0) :
    ⁅f, raise e v (m + 1)⁆ = 0 := by
  rw [lowering_recurrence h e f v (-(m : K)) he fe hv fv]
  simp

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
    ∃ t : ℕ, a = -(t : K) := by
  obtain ⟨t, ht, ht1⟩ := Nat.exists_not_and_succ_of_not_zero_of_exists
    (show ¬ raise e v 0 = 0 from v_ne) nilpotent_at_v
  have hz := lowering_recurrence h e f v a he fe hv fv t
  rw [ht1, lie_zero, eq_comm, smul_eq_zero_iff_left ht, mul_eq_zero] at hz
  have hn : -((t + 1 : ℕ) : K) ≠ 0 := by
    exact neg_ne_zero.mpr (by simpa using Nat.cast_add_one_ne_zero (R := K) t)
  have hsum : a + (t : K) = 0 := hz.resolve_left hn
  exact ⟨t, eq_neg_of_add_eq_zero_left hsum⟩

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
    ∀ n p x, x ∈ R n → ⁅H p, x⁆ ∈ R n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro p x hx
    cases n with
    | zero =>
      have hx0 : x = 0 := by simpa [r0] using hx
      simp [hx0]
    | succ n =>
      cases n with
      | zero =>
        have hx0 : x = 0 := by simpa [r1] using hx
        simp [hx0]
      | succ n =>
        have hparts := (recurrence n x).mp hx
        apply (recurrence n ⁅H p, x⁆).mpr
        refine ⟨weight_stable p (n + 2) x hparts.1, ?_⟩
        intro i
        rw [leibniz_lie, fh, smul_lie]
        exact (R (n + 1)).add_mem
          ((R (n + 1)).smul_mem (c p i) (hparts.2 i))
          (ih (n + 1) (by omega) p ⁅F i, x⁆ (hparts.2 i))

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
    ∀ n j x, x ∈ R n → ⁅E j, x⁆ ∈ R (n + 1) := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro j x hx
    cases n with
    | zero =>
      have hx0 : x = 0 := by simpa [r0] using hx
      simp [hx0]
    | succ n =>
      cases n with
      | zero =>
        have hx0 : x = 0 := by simpa [r1] using hx
        simp [hx0]
      | succ n =>
        have hparts := (recurrence n x).mp hx
        apply (recurrence (n + 1) ⁅E j, x⁆).mpr
        refine ⟨raising j (n + 2) x hparts.1, ?_⟩
        intro i
        have hr := ih (n + 1) (by omega) j ⁅F i, x⁆ (hparts.2 i)
        rw [leibniz_lie, fe]
        split_ifs with hij
        · rw [neg_lie]
          exact (R (n + 2)).add_mem
            ((R (n + 2)).neg_mem (cartan_stable (n + 2) (coroot i) x hx)) hr
        · simpa using hr

end GradedRecurrence

section GeneratorClosure

variable {K L : Type*} [CommRing K] [LieRing L] [LieAlgebra K L]

/-- Stability under brackets with a generating set propagates through all
Lie brackets by Jacobi; this is the step used in the positive Serre-span recurrence. -/
theorem lieSpan_stability (s : Set L) (W : Submodule K L)
    (hs : ∀ x ∈ s, ∀ y ∈ W, ⁅x, y⁆ ∈ W) :
    ∀ x ∈ LieSubalgebra.lieSpan K L s, ∀ y ∈ W, ⁅x, y⁆ ∈ W := by
  intro x hx
  induction hx using LieSubalgebra.lieSpan_induction K with
  | mem x hx => exact hs x hx
  | zero => intro y hy; simp
  | add x y _ _ hx hy =>
    intro z hz
    rw [add_lie]
    exact W.add_mem (hx z hz) (hy z hz)
  | smul r x _ hx =>
    intro z hz
    rw [smul_lie]
    exact W.smul_mem r (hx z hz)
  | lie x y _ _ hx hy =>
    intro z hz
    rw [lie_lie]
    exact W.sub_mem (hx _ (hy z hz)) (hy _ (hx z hz))

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
      (LieSubmodule.lieSpan K L t : Submodule K L) := by
  apply le_antisymm
  · intro x hx
    change GeneratorClosure (K := K) s t x at hx
    induction hx with
    | zero => exact (LieSubmodule.lieSpan K L t).zero_mem
    | seed ht => exact LieSubmodule.subset_lieSpan ht
    | add _ _ hx hy => exact (LieSubmodule.lieSpan K L t).add_mem hx hy
    | smul r _ hx => exact (LieSubmodule.lieSpan K L t).smul_mem r hx
    | bracket _ _ hy => exact (LieSubmodule.lieSpan K L t).lie_mem hy
  · let I := idealOfGeneratorStable s hgen (generatorClosure (K := K) s t)
      (fun x hx y hy => GeneratorClosure.bracket hx hy)
    have hI : LieSubmodule.lieSpan K L t ≤ I := by
      rw [LieSubmodule.lieSpan_le]
      intro x hx
      exact GeneratorClosure.seed hx
    exact hI

end GeneratorClosure

end SerrePartial

#print SerrePartial.raising_weight
#print axioms SerrePartial.raising_weight
#print SerrePartial.lowering_recurrence
#print axioms SerrePartial.lowering_recurrence
#print SerrePartial.serre_string_killed
#print axioms SerrePartial.serre_string_killed
#print SerrePartial.primitive_weight_is_nonpositive_integer
#print axioms SerrePartial.primitive_weight_is_nonpositive_integer
#print SerrePartial.graded_kernel_cartan_stable
#print axioms SerrePartial.graded_kernel_cartan_stable
#print SerrePartial.graded_kernel_raising_stable
#print axioms SerrePartial.graded_kernel_raising_stable
#print SerrePartial.lieSpan_stability
#print axioms SerrePartial.lieSpan_stability
#print SerrePartial.generatorClosure_eq_lieIdeal
#print axioms SerrePartial.generatorClosure_eq_lieIdeal
