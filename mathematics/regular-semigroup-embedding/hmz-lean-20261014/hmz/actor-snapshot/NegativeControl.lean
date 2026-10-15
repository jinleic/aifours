import Mathlib.Algebra.Group.Hom.Basic
import Mathlib.Algebra.Group.Pi.Basic
import Mathlib.Algebra.Group.PUnit
import Mathlib.Algebra.GroupWithZero.Nat

/-!
Semantic negative control for P1.SD.idem_iff. The Action and SD construction
below are copied verbatim from Formal.lean. The mutation drops Band B, then
specializes B to the multiplicative natural numbers and G to the trivial group.
The concrete element (2,1) has grade 1 but is not idempotent (4 differs from 2).
-/
namespace P1
universe u v w

def Idem {S : Type u} [Mul S] (x : S) : Prop := x * x = x

structure Action (B : Type u) (G : Type v) [Mul B] [Group G] where
  act : G → B → B
  one_act : ∀ b, act 1 b = b
  mul_act : ∀ g h b, act (g * h) b = act g (act h b)
  act_mul : ∀ g a b, act g (a * b) = act g a * act g b

structure SD (B : Type u) (G : Type v) [Mul B] [Group G] (α : Action B G) where
  base : B
  grade : G

namespace SD

variable {B : Type u} {G : Type v} [Semigroup B] [Group G] (α : Action B G)

@[ext] theorem ext {s t : SD B G α} (hb : s.base = t.base) (hg : s.grade = t.grade) :
    s = t := by
  cases s
  cases t
  cases hb
  cases hg
  rfl

instance : Mul (SD B G α) :=
  ⟨fun s t => ⟨s.base * α.act s.grade t.base, s.grade * t.grade⟩⟩

@[simp] theorem base_mul (s t : SD B G α) :
    (s * t).base = s.base * α.act s.grade t.base := rfl

@[simp] theorem grade_mul (s t : SD B G α) : (s * t).grade = s.grade * t.grade := rfl

instance : Semigroup (SD B G α) where
  mul_assoc s t r := by
    apply ext
    · simp only [base_mul, grade_mul, α.mul_act, α.act_mul, mul_assoc]
    · exact mul_assoc s.grade t.grade r.grade


end SD

def trivialAction : Action ℕ PUnit where
  act _ b := b
  one_act _ := rfl
  mul_act _ _ _ := rfl
  act_mul _ _ _ := rfl

def witness : SD ℕ PUnit trivialAction := ⟨2, 1⟩

-- This checked example establishes that the following mutation is actually false.
example : witness.grade = 1 ∧ ¬ Idem witness := by
  constructor
  · rfl
  · intro h
    have hnum : (2 : ℕ) * 2 = 2 := congrArg SD.base h
    have hfalse : ¬ ((2 : ℕ) * 2 = 2) := by decide
    exact hfalse hnum

-- Wrong conclusion after dropping the necessary band hypothesis.
theorem SD.idem_iff_without_band (s : SD ℕ PUnit trivialAction) :
    Idem s ↔ s.grade = 1 := by
  constructor
  · intro hs
    have hg : s.grade * s.grade = s.grade := congrArg SD.grade hs
    exact mul_left_cancel (hg.trans (mul_one s.grade).symm)
  · intro hg
    apply SD.ext
    · change s.base * s.base = s.base
      rfl
    · change s.grade * s.grade = s.grade
      rw [hg, one_mul]

end P1
