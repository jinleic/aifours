import Mathlib.Algebra.Group.Hom.Basic
import Mathlib.Algebra.Group.Pi.Basic

/-!
Partial formalization for book Problem 1. No theorem below claims its sufficient direction.
All multiplication is associative via Mathlib's Semigroup; groups are Mathlib Group.
The explicit action permits a nonunital band as its carrier.
-/

namespace P1

universe u v w

def Idem {S : Type u} [Mul S] (x : S) : Prop := x * x = x

def Band (B : Type u) [Mul B] : Prop := ∀ x : B, Idem x

def Regular (S : Type u) [Mul S] : Prop :=
  ∀ x : S, ∃ y : S, (x * y) * x = x ∧ (y * x) * y = y

def NaturalLE {S : Type u} [Mul S] (x y : S) : Prop :=
  ∃ e f : S, Idem e ∧ Idem f ∧ x = e * y ∧ x = y * f

def WeaklyEUnitary (S : Type u) [Mul S] : Prop :=
  ∀ e a : S, Idem e → NaturalLE e a → Idem a

def EUnitary (S : Type u) [Mul S] : Prop :=
  (∀ e a : S, Idem e → Idem (e * a) → Idem a) ∧
  (∀ e a : S, Idem e → Idem (a * e) → Idem a)

/-- This is precisely membership in eSe when e is idempotent. -/
def InLocal {S : Type u} [Mul S] (e x : S) : Prop := e * x = x ∧ x * e = x

/-- The book regular-band identity, on an ambient band. -/
def RegularBand (B : Type u) [Mul B] : Prop :=
  Band B ∧ ∀ a x y : B, (((a * x) * a) * y) * a = ((a * x) * y) * a

/-- Every eBe obeys the book regular-band identity. Band B is separate. -/
def LocallyRegular (B : Type u) [Mul B] : Prop :=
  ∀ e a x y : B, InLocal e a → InLocal e x → InLocal e y →
    (((a * x) * a) * y) * a = ((a * x) * y) * a

/-- Regularity plus the two conditions on E(eSe), without a global orthodox assumption. -/
def LocallyROrthodox (S : Type u) [Mul S] : Prop :=
  Regular S ∧ ∀ e : S, Idem e →
    (∀ x y : S, InLocal e x → InLocal e y → Idem x → Idem y → Idem (x * y)) ∧
    (∀ a x y : S, InLocal e a → InLocal e x → InLocal e y →
      Idem a → Idem x → Idem y →
      (((a * x) * a) * y) * a = ((a * x) * y) * a)

theorem inLocal_iff {S : Type u} [Semigroup S] {e x : S} (he : Idem e) :
    InLocal e x ↔ ∃ z : S, (e * z) * e = x := by
  constructor
  · intro h
    exact ⟨x, by rw [h.1, h.2]⟩
  · rintro ⟨z, rfl⟩
    constructor
    · simp only [← mul_assoc]
      rw [he]
    · rw [mul_assoc (e * z) e e, he]

theorem regular_local {S : Type u} [Semigroup S] (hS : Regular S)
    {e x : S} (he : Idem e) (hx : InLocal e x) :
    ∃ y : S, InLocal e y ∧ (x * y) * x = x ∧ (y * x) * y = y := by sorry

theorem regular_iff_innerInverse {S : Type u} [Semigroup S] :
    Regular S ↔ ∀ a : S, ∃ b : S, (a * b) * a = a := by sorry

theorem idem_map_iff {S : Type u} {T : Type v} [Mul S] [Mul T]
    (φ : S →ₙ* T) (hinj : Function.Injective φ) (x : S) :
    Idem (φ x) ↔ Idem x := by
  constructor
  · intro h
    apply hinj
    rw [map_mul]
    exact h
  · intro h
    change φ x * φ x = φ x
    rw [← map_mul, h]

theorem inLocal_map {S : Type u} {T : Type v} [Mul S] [Mul T]
    (φ : S →ₙ* T) {e x : S} (hx : InLocal e x) : InLocal (φ e) (φ x) := by
  constructor
  · rw [← map_mul, hx.1]
  · rw [← map_mul, hx.2]

theorem locallyROrthodox_of_injective {S : Type u} {T : Type v}
    [Semigroup S] [Semigroup T] (hS : Regular S) (hT : LocallyROrthodox T)
    (φ : S →ₙ* T) (hinj : Function.Injective φ) : LocallyROrthodox S := by
  refine ⟨hS, ?_⟩
  intro e he
  have he' := (idem_map_iff φ hinj e).mpr he
  obtain ⟨hclose, hreg⟩ := hT.2 (φ e) he'
  constructor
  · intro x y hx hy hix hiy
    apply (idem_map_iff φ hinj (x * y)).mp
    rw [map_mul]
    exact hclose (φ x) (φ y) (inLocal_map φ hx) (inLocal_map φ hy)
      ((idem_map_iff φ hinj x).mpr hix) ((idem_map_iff φ hinj y).mpr hiy)
  · intro a x y ha hx hy hia hix hiy
    apply hinj
    simp only [map_mul]
    exact hreg (φ a) (φ x) (φ y) (inLocal_map φ ha) (inLocal_map φ hx)
      (inLocal_map φ hy) ((idem_map_iff φ hinj a).mpr hia)
      ((idem_map_iff φ hinj x).mpr hix) ((idem_map_iff φ hinj y).mpr hiy)

theorem weaklyEUnitary_of_injective {S : Type u} {T : Type v} [Mul S] [Mul T]
    (hT : WeaklyEUnitary T) (φ : S →ₙ* T) (hinj : Function.Injective φ) :
    WeaklyEUnitary S := by
  intro e a he hle
  obtain ⟨f, k, hf, hk, hleft, hright⟩ := hle
  apply (idem_map_iff φ hinj a).mp
  apply hT (φ e) (φ a) ((idem_map_iff φ hinj e).mpr he)
  refine ⟨φ f, φ k, (idem_map_iff φ hinj f).mpr hf,
    (idem_map_iff φ hinj k).mpr hk, ?_, ?_⟩
  · rw [← map_mul, ← hleft]
  · rw [← map_mul, ← hright]

theorem band_regular {B : Type u} [Mul B] (hB : Band B) : Regular B := by
  intro b
  exact ⟨b, by rw [hB b, hB b], by rw [hB b, hB b]⟩

theorem band_locallyROrthodox_iff {B : Type u} [Mul B] (hB : Band B) :
    LocallyROrthodox B ↔ LocallyRegular B := by
  constructor
  · intro h e a x y ha hx hy
    exact (h.2 e (hB e)).2 a x y ha hx hy (hB a) (hB x) (hB y)
  · intro h
    exact ⟨band_regular hB, fun e _ => ⟨fun x y _ _ _ _ => hB (x * y),
      fun a x y ha hx hy _ _ _ => h e a x y ha hx hy⟩⟩

/-- An actual group action by multiplicative bijections; bijectivity is derived below. -/
structure Action (B : Type u) (G : Type v) [Mul B] [Group G] where
  act : G → B → B
  one_act : ∀ b, act 1 b = b
  mul_act : ∀ g h b, act (g * h) b = act g (act h b)
  act_mul : ∀ g a b, act g (a * b) = act g a * act g b

namespace Action

variable {B : Type u} {G : Type v} [Mul B] [Group G] (α : Action B G)

theorem act_bijective (g : G) : Function.Bijective (α.act g) := by sorry

end Action

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

theorem idem_iff (hB : Band B) (s : SD B G α) : Idem s ↔ s.grade = 1 := by sorry

theorem regular (hB : Band B) : Regular (SD B G α) := by sorry

theorem eUnitary (hB : Band B) : EUnitary (SD B G α) := by sorry

theorem weaklyEUnitary (hB : Band B) : WeaklyEUnitary (SD B G α) := by sorry

/-- Local idempotents have precisely the base coordinates of bBb. -/
theorem local_idem_iff (hB : Band B) (b : B) (x : SD B G α) :
    Idem x ∧ InLocal (⟨b, 1⟩ : SD B G α) x ↔
      x.grade = 1 ∧ InLocal b x.base := by sorry

theorem locallyROrthodox_iff (hB : Band B) :
    LocallyROrthodox (SD B G α) ↔ LocallyRegular B := by sorry

theorem embedding_necessary {S : Type w} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* SD B G α) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ EUnitary S ∧ LocallyROrthodox S := by sorry

end SD

/-- The wreath action shifts the argument on the right. It is a left group action. -/
def shiftAction {B : Type u} {G : Type v} [Mul B] [Group G] : Action (G → B) G where
  act h f := fun g => f (g * h)
  one_act f := by funext g; exact congrArg f (mul_one g)
  mul_act h k f := by funext g; exact congrArg f (mul_assoc g h k).symm
  act_mul h a b := rfl

theorem function_band {B : Type u} {I : Type v} [Mul B] (hB : Band B) : Band (I → B) := by sorry

theorem function_locallyRegular {B : Type u} {I : Type v} [Mul B]
    (hLR : LocallyRegular B) : LocallyRegular (I → B) := by sorry

def FunctorLaw {S : Type u} {G : Type v} {B : Type w}
    [Mul S] [Mul B] [Group G] (σ : S →ₙ* G) (F : G → S → B) : Prop :=
  ∀ g s t, F g s * F (g * σ s) t = F g (s * t)

def HomFaithful {S : Type u} {G : Type v} {B : Type w}
    [Mul S] [Group G] (σ : S →ₙ* G) (F : G → S → B) : Prop :=
  ∀ s t, F 1 s = F 1 t → σ s = σ t → s = t

/-- Lemma 3: the multiplication-preserving map is constructed, not assumed. -/
def wreathHom {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (σ : S →ₙ* G)
    (F : G → S → B) (hF : FunctorLaw σ F) : S →ₙ* SD (G → B) G shiftAction where
  toFun s := ⟨fun g => F g s, σ s⟩
  map_mul' s t := by
    apply SD.ext
    · funext g
      exact (hF g s t).symm
    · exact map_mul σ s t

theorem wreathHom_injective {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (σ : S →ₙ* G)
    (F : G → S → B) (hF : FunctorLaw σ F) (hfaith : HomFaithful σ F) :
    Function.Injective (wreathHom σ F hF) := by sorry

theorem derived_embedding {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (σ : S →ₙ* G)
    (hB : Band B) (hLR : LocallyRegular B) (F : G → S → B)
    (hF : FunctorLaw σ F) (hfaith : HomFaithful σ F) :
    Band (G → B) ∧ LocallyRegular (G → B) ∧
      ∃ φ : S →ₙ* SD (G → B) G shiftAction,
        Function.Injective φ ∧ ∀ s, (φ s).grade = σ s := by sorry

/-- Converse: every embedding over σ produces F(g,s)=g acting on the base of φ(s). -/
theorem derived_from_embedding {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (α : Action B G) (σ : S →ₙ* G)
    (φ : S →ₙ* SD B G α) (hinj : Function.Injective φ)
    (hgrade : ∀ s, (φ s).grade = σ s) :
    ∃ F : G → S → B, FunctorLaw σ F ∧ HomFaithful σ F := by sorry

/-- Rees coordinates for the completely simple factor. No zero is adjoined. -/
structure Rees (G : Type u) (I : Type v) (L : Type w) (p : L → I → G) where
  row : I
  grade : G
  col : L

namespace Rees

variable {G : Type u} {I : Type v} {L : Type w} [Group G] (p : L → I → G)

omit [Group G] in
@[ext] theorem ext {s t : Rees G I L p} (hi : s.row = t.row)
    (hg : s.grade = t.grade) (hl : s.col = t.col) : s = t := by
  cases s; cases t; cases hi; cases hg; cases hl; rfl

instance : Mul (Rees G I L p) :=
  ⟨fun s t => ⟨s.row, (s.grade * p s.col t.row) * t.grade, t.col⟩⟩

@[simp] theorem row_mul (s t : Rees G I L p) : (s * t).row = s.row := rfl
@[simp] theorem grade_mul (s t : Rees G I L p) :
    (s * t).grade = (s.grade * p s.col t.row) * t.grade := rfl
@[simp] theorem col_mul (s t : Rees G I L p) : (s * t).col = t.col := rfl

instance : Semigroup (Rees G I L p) where
  mul_assoc s t r := by
    apply ext p
    · rfl
    · simp only [grade_mul, col_mul, row_mul, mul_assoc]
    · rfl

theorem idem_iff (s : Rees G I L p) : Idem s ↔ s.grade * p s.col s.row = 1 := by sorry

/-- Natural order in a completely simple Rees semigroup is equality. -/
theorem naturalLE_eq {s t : Rees G I L p} (hle : NaturalLE s t) : s = t := by sorry

def localUnit (i : I) (l : L) : Rees G I L p := ⟨i, (p l i)⁻¹, l⟩

def unitOf (s : Rees G I L p) : Rees G I L p := localUnit p s.row s.col

theorem unit_mul (s : Rees G I L p) (l : L) : localUnit p s.row l * s = s := by
  apply ext p
  · rfl
  · simp only [grade_mul, localUnit, inv_mul_cancel, one_mul]
  · rfl

theorem unitOf_mul (s : Rees G I L p) : unitOf p s * s = s := unit_mul p s s.col

theorem mul_unit (s : Rees G I L p) (i : I) : s * localUnit p i s.col = s := by
  apply ext p
  · rfl
  · simp only [grade_mul, localUnit, mul_assoc, mul_inv_cancel, mul_one]
  · rfl

theorem unitOf_eq_of_idem {s : Rees G I L p} (hs : Idem s) : unitOf p s = s := by
  apply ext p
  · rfl
  · change (p s.col s.row)⁻¹ = s.grade
    apply mul_right_cancel (b := p s.col s.row)
    rw [inv_mul_cancel, (idem_iff p s).mp hs]
  · rfl

def inverse (s : Rees G I L p) : Rees G I L p :=
  ⟨s.row, (p s.col s.row)⁻¹ * s.grade⁻¹ * (p s.col s.row)⁻¹, s.col⟩

theorem mul_inverse (s : Rees G I L p) : s * inverse p s = unitOf p s := by
  apply ext p
  · rfl
  · simp only [grade_mul, inverse, unitOf, localUnit, mul_assoc,
      mul_inv_cancel_left]
  · rfl

theorem inverse_laws (s : Rees G I L p) :
    (s * inverse p s) * s = s ∧ (inverse p s * s) * inverse p s = inverse p s := by
  constructor
  · rw [mul_inverse]
    exact unit_mul p s s.col
  · apply ext p
    · rfl
    · simp only [grade_mul, row_mul, inverse, mul_assoc,
        inv_mul_cancel_left, mul_inv_cancel_left]
    · rfl

end Rees

universe z

/-- The fixed Pastijn reading (P), with the sandwich coefficient in the action. -/
structure Pastijn (B : Type u) (G : Type v) (I : Type w) (L : Type z)
    [Mul B] [Group G] (p : L → I → G) (α : Action B G) where
  base : B
  rees : Rees G I L p

namespace Pastijn

variable {B : Type u} {G : Type v} {I : Type w} {L : Type z}
  [Semigroup B] [Group G] (p : L → I → G) (α : Action B G)

@[ext] theorem ext {s t : Pastijn B G I L p α} (hb : s.base = t.base)
    (hr : s.rees = t.rees) : s = t := by
  cases s; cases t; cases hb; cases hr; rfl

instance : Mul (Pastijn B G I L p α) :=
  ⟨fun s t => ⟨s.base * α.act (s.rees.grade * p s.rees.col t.rees.row) t.base,
    s.rees * t.rees⟩⟩

@[simp] theorem base_mul (s t : Pastijn B G I L p α) :
    (s * t).base = s.base * α.act (s.rees.grade * p s.rees.col t.rees.row) t.base := rfl

@[simp] theorem rees_mul (s t : Pastijn B G I L p α) :
    (s * t).rees = s.rees * t.rees := rfl

instance : Semigroup (Pastijn B G I L p α) where
  mul_assoc s t r := by
    apply ext
    · simp only [base_mul, rees_mul, Rees.grade_mul, Rees.col_mul, Rees.row_mul,
        α.act_mul, ← α.mul_act, mul_assoc]
    · exact mul_assoc s.rees t.rees r.rees

def projection : Pastijn B G I L p α →ₙ* Rees G I L p where
  toFun s := s.rees
  map_mul' _ _ := rfl

theorem idem_iff (hB : Band B) (s : Pastijn B G I L p α) :
    Idem s ↔ Idem s.rees := by sorry

theorem weaklyEUnitary (hB : Band B) : WeaklyEUnitary (Pastijn B G I L p α) := by
  intro e a he hle
  obtain ⟨f, k, hf, hk, hleft, hright⟩ := hle
  have hle' : NaturalLE e.rees a.rees :=
    ⟨f.rees, k.rees, (idem_iff p α hB f).mp hf, (idem_iff p α hB k).mp hk,
      congrArg Pastijn.rees hleft, congrArg Pastijn.rees hright⟩
  have heq := Rees.naturalLE_eq p hle'
  apply (idem_iff p α hB a).mpr
  rw [← heq]
  exact (idem_iff p α hB e).mp he

theorem local_idem_iff (hB : Band B) (e x : Pastijn B G I L p α) (he : Idem e) :
    Idem x ∧ InLocal e x ↔ x.rees = e.rees ∧ InLocal e.base x.base := by sorry

theorem regular (hB : Band B) : Regular (Pastijn B G I L p α) := by sorry

theorem locallyROrthodox (hB : Band B) (hLR : LocallyRegular B) :
    LocallyROrthodox (Pastijn B G I L p α) := by sorry

/-- Each chosen Rees idempotent gives an embedded copy of the base band. -/
def baseHom (i : I) (l : L) : B →ₙ* Pastijn B G I L p α where
  toFun b := ⟨b, ⟨i, (p l i)⁻¹, l⟩⟩
  map_mul' a b := by
    apply ext
    · change a * b = a * α.act ((p l i)⁻¹ * p l i) b
      rw [inv_mul_cancel, α.one_act]
    · apply Rees.ext p
      · rfl
      · change (p l i)⁻¹ = ((p l i)⁻¹ * p l i) * (p l i)⁻¹
        rw [inv_mul_cancel, one_mul]
      · rfl

theorem locallyROrthodox_iff (hB : Band B) (i : I) (l : L) :
    LocallyROrthodox (Pastijn B G I L p α) ↔ LocallyRegular B := by sorry

/-- Lemma 0 for reading (P), with actual Rees/Pastijn coordinates. -/
theorem embedding_necessary {S : Type*} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* Pastijn B G I L p α) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ LocallyROrthodox S := by sorry

end Pastijn

/-- An endomorphism action of a semigroup, without a unit preservation requirement. -/
structure EndAction (B : Type u) (C : Type v) [Mul B] [Mul C] where
  act : C → B → B
  mul_act : ∀ x y b, act (x * y) b = act x (act y b)
  act_mul : ∀ x a b, act x (a * b) = act x a * act x b

/-- Canonical inverse carrier condition for the fixed restricted reading (R). -/
def Restricted (B : Type u) (G : Type v) (I : Type w) (L : Type z)
    [Mul B] [Group G] (p : L → I → G) (θ : EndAction B (Rees G I L p)) :=
  {s : B × Rees G I L p // θ.act (Rees.unitOf p s.2) s.1 = s.1}

namespace Restricted

variable {B : Type u} {G : Type v} {I : Type w} {L : Type z}
    [Semigroup B] [Group G] (p : L → I → G) (θ : EndAction B (Rees G I L p))

def base (s : Restricted B G I L p θ) : B := s.val.1
def rees (s : Restricted B G I L p θ) : Rees G I L p := s.val.2

@[ext] theorem ext {s t : Restricted B G I L p θ} (hb : base p θ s = base p θ t)
    (hr : rees p θ s = rees p θ t) : s = t := Subtype.ext (Prod.ext hb hr)

theorem fixed_sameRow {a : B} {x : Rees G I L p}
    (ha : θ.act (Rees.unitOf p x) a = a) (l : L) :
    θ.act (Rees.localUnit p x.row l) a = a := by
  calc
    θ.act (Rees.localUnit p x.row l) a =
        θ.act (Rees.localUnit p x.row l) (θ.act (Rees.unitOf p x) a) := by rw [ha]
    _ = θ.act (Rees.localUnit p x.row l * Rees.unitOf p x) a := (θ.mul_act _ _ _).symm
    _ = θ.act (Rees.unitOf p x) a := by
      have hu : Rees.localUnit p x.row l * Rees.unitOf p x = Rees.unitOf p x :=
        Rees.unit_mul p (Rees.unitOf p x) l
      rw [hu]
    _ = a := ha

/-- The chosen carrier agrees with the adopted restricted carrier for every inverse of x. -/
theorem carrier_iff_for_inverse (a : B) (x y : Rees G I L p)
    (hxyx : (x * y) * x = x) :
    θ.act (x * y) a = a ↔ θ.act (Rees.unitOf p x) a = a := by sorry

instance : Mul (Restricted B G I L p θ) := ⟨fun s t =>
  ⟨(s.val.1 * θ.act s.val.2 t.val.1, s.val.2 * t.val.2), by
    change θ.act (Rees.localUnit p s.val.2.row t.val.2.col)
      (s.val.1 * θ.act s.val.2 t.val.1) = s.val.1 * θ.act s.val.2 t.val.1
    rw [θ.act_mul, fixed_sameRow p θ s.property t.val.2.col,
      ← θ.mul_act, Rees.unit_mul]⟩⟩

@[simp] theorem base_mul (s t : Restricted B G I L p θ) :
    base p θ (s * t) = base p θ s * θ.act (rees p θ s) (base p θ t) := rfl

@[simp] theorem rees_mul (s t : Restricted B G I L p θ) :
    rees p θ (s * t) = rees p θ s * rees p θ t := rfl

instance : Semigroup (Restricted B G I L p θ) where
  mul_assoc s t r := by
    apply ext
    · simp only [base_mul, rees_mul, θ.mul_act, θ.act_mul, mul_assoc]
    · exact mul_assoc _ _ _

theorem act_fix {s : Restricted B G I L p θ} (hs : Idem (rees p θ s)) :
    θ.act (rees p θ s) (base p θ s) = base p θ s := by
  have h := s.property
  change θ.act (Rees.unitOf p (rees p θ s)) (base p θ s) = base p θ s at h
  rw [Rees.unitOf_eq_of_idem p hs] at h
  exact h

theorem idem_iff (hB : Band B) (s : Restricted B G I L p θ) :
    Idem s ↔ Idem (rees p θ s) := by sorry

theorem weaklyEUnitary (hB : Band B) : WeaklyEUnitary (Restricted B G I L p θ) := by
  intro e a he hle
  obtain ⟨f, k, hf, hk, hleft, hright⟩ := hle
  have hle' : NaturalLE (rees p θ e) (rees p θ a) :=
    ⟨rees p θ f, rees p θ k, (idem_iff p θ hB f).mp hf, (idem_iff p θ hB k).mp hk,
      congrArg (rees p θ) hleft, congrArg (rees p θ) hright⟩
  have heq := Rees.naturalLE_eq p hle'
  apply (idem_iff p θ hB a).mpr
  rw [← heq]
  exact (idem_iff p θ hB e).mp he

theorem regular (hB : Band B) : Regular (Restricted B G I L p θ) := by sorry

theorem local_idem_iff (hB : Band B) (e x : Restricted B G I L p θ) (he : Idem e) :
    Idem x ∧ InLocal e x ↔
      rees p θ x = rees p θ e ∧ InLocal (base p θ e) (base p θ x) := by sorry

theorem locallyROrthodox (hB : Band B) (hLR : LocallyRegular B) :
    LocallyROrthodox (Restricted B G I L p θ) := by sorry

/-- Lemma 0 for reading (R). -/
theorem embedding_necessary {S : Type*} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* Restricted B G I L p θ) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ LocallyROrthodox S := by sorry

end Restricted

end P1

/-! Auditable definitions, root statements, and transitive standard axioms. -/
set_option pp.proofs false
