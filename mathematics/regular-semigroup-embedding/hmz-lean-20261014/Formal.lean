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
    ∃ y : S, InLocal e y ∧ (x * y) * x = x ∧ (y * x) * y = y := by
  obtain ⟨y, hy, hy'⟩ := hS x
  refine ⟨(e * y) * e, (inLocal_iff he).mpr ⟨y, rfl⟩, ?_, ?_⟩
  · calc
      (x * ((e * y) * e)) * x = ((x * e) * y) * (e * x) := by
        simp only [mul_assoc]
      _ = (x * y) * x := by rw [hx.1, hx.2]
      _ = x := hy
  · calc
      (((e * y) * e) * x) * ((e * y) * e) =
          ((e * y) * ((e * x) * e)) * (y * e) := by simp only [mul_assoc]
      _ = (e * ((y * x) * y)) * e := by rw [hx.1, hx.2]; simp only [mul_assoc]
      _ = (e * y) * e := by rw [hy']

theorem regular_iff_innerInverse {S : Type u} [Semigroup S] :
    Regular S ↔ ∀ a : S, ∃ b : S, (a * b) * a = a := by
  constructor
  · intro h a
    obtain ⟨b, hb, _⟩ := h a
    exact ⟨b, hb⟩
  · intro h a
    obtain ⟨b, hb⟩ := h a
    refine ⟨(b * a) * b, ?_, ?_⟩
    · calc
        (a * ((b * a) * b)) * a = (((a * b) * a) * b) * a := by simp only [mul_assoc]
        _ = a := by rw [hb, hb]
    · calc
        ((((b * a) * b) * a) * ((b * a) * b)) =
            (b * ((a * b) * a)) * ((b * a) * b) := by simp only [mul_assoc]
        _ = (b * a) * ((b * a) * b) := by rw [hb]
        _ = (b * ((a * b) * a)) * b := by simp only [mul_assoc]
        _ = (b * a) * b := by rw [hb]

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

theorem act_bijective (g : G) : Function.Bijective (α.act g) := by
  have left : ∀ b, α.act g⁻¹ (α.act g b) = b := by
    intro b
    rw [← α.mul_act, inv_mul_cancel, α.one_act]
  have right : ∀ b, α.act g (α.act g⁻¹ b) = b := by
    intro b
    rw [← α.mul_act, mul_inv_cancel, α.one_act]
  exact ⟨Function.LeftInverse.injective left,
    fun b => ⟨α.act g⁻¹ b, right b⟩⟩

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

theorem idem_iff (hB : Band B) (s : SD B G α) : Idem s ↔ s.grade = 1 := by
  constructor
  · intro hs
    have hg : s.grade * s.grade = s.grade := congrArg SD.grade hs
    exact mul_left_cancel (hg.trans (mul_one s.grade).symm)
  · intro hg
    apply ext
    · change s.base * α.act s.grade s.base = s.base
      rw [hg, α.one_act]
      exact hB s.base
    · change s.grade * s.grade = s.grade
      rw [hg, one_mul]

theorem regular (hB : Band B) : Regular (SD B G α) := by
  intro s
  refine ⟨⟨α.act s.grade⁻¹ s.base, s.grade⁻¹⟩, ?_, ?_⟩
  have hact : α.act s.grade (α.act s.grade⁻¹ s.base) = s.base := by
    rw [← α.mul_act, mul_inv_cancel, α.one_act]
  all_goals apply ext
  · simp only [base_mul, grade_mul, mul_inv_cancel, α.one_act, hact]
    rw [hB s.base, hB s.base]
  · simp only [grade_mul, mul_inv_cancel, one_mul]
  · simp only [base_mul, grade_mul, inv_mul_cancel, α.one_act]
    rw [hB (α.act s.grade⁻¹ s.base), hB (α.act s.grade⁻¹ s.base)]
  · simp only [grade_mul, inv_mul_cancel, one_mul]

theorem eUnitary (hB : Band B) : EUnitary (SD B G α) := by
  constructor
  · intro e a he hea
    apply (idem_iff α hB a).mpr
    have h1 := (idem_iff α hB e).mp he
    have h2 := (idem_iff α hB (e * a)).mp hea
    simpa only [grade_mul, h1, one_mul] using h2
  · intro e a he hae
    apply (idem_iff α hB a).mpr
    have h1 := (idem_iff α hB e).mp he
    have h2 := (idem_iff α hB (a * e)).mp hae
    simpa only [grade_mul, h1, mul_one] using h2

theorem weaklyEUnitary (hB : Band B) : WeaklyEUnitary (SD B G α) := by
  intro e a he hle
  obtain ⟨f, k, hf, _, hfa, _⟩ := hle
  apply (eUnitary α hB).1 f a hf
  rw [← hfa]
  exact he

/-- Local idempotents have precisely the base coordinates of bBb. -/
theorem local_idem_iff (hB : Band B) (b : B) (x : SD B G α) :
    Idem x ∧ InLocal (⟨b, 1⟩ : SD B G α) x ↔
      x.grade = 1 ∧ InLocal b x.base := by
  constructor
  · rintro ⟨hx, hl, hr⟩
    have hg := (idem_iff α hB x).mp hx
    refine ⟨hg, ?_, ?_⟩
    · have h := congrArg SD.base hl
      simpa only [base_mul, α.one_act] using h
    · have h := congrArg SD.base hr
      simpa only [base_mul, hg, α.one_act] using h
  · rintro ⟨hg, hl, hr⟩
    refine ⟨(idem_iff α hB x).mpr hg, ?_, ?_⟩
    · apply ext
      · simpa only [base_mul, α.one_act] using hl
      · simp only [grade_mul, one_mul]
    · apply ext
      · simpa only [base_mul, hg, α.one_act] using hr
      · simp only [grade_mul, mul_one]

theorem locallyROrthodox_iff (hB : Band B) :
    LocallyROrthodox (SD B G α) ↔ LocallyRegular B := by
  constructor
  · intro h e a x y ha hx hy
    let E : SD B G α := ⟨e, 1⟩
    let A : SD B G α := ⟨a, 1⟩
    let X : SD B G α := ⟨x, 1⟩
    let Y : SD B G α := ⟨y, 1⟩
    have hi (b : B) : Idem (⟨b, 1⟩ : SD B G α) := (idem_iff α hB _).mpr rfl
    have hA : InLocal E A := ((local_idem_iff α hB e A).mpr ⟨rfl, ha⟩).2
    have hX : InLocal E X := ((local_idem_iff α hB e X).mpr ⟨rfl, hx⟩).2
    have hY : InLocal E Y := ((local_idem_iff α hB e Y).mpr ⟨rfl, hy⟩).2
    have hid := (h.2 E (hi e)).2 A X Y hA hX hY (hi a) (hi x) (hi y)
    have hb := congrArg SD.base hid
    simpa only [base_mul, grade_mul, one_mul, α.one_act, E, A, X, Y] using hb
  · intro h
    refine ⟨regular α hB, ?_⟩
    intro e he
    have hg := (idem_iff α hB e).mp he
    have hE : e = (⟨e.base, 1⟩ : SD B G α) := ext α rfl hg
    constructor
    · intro x y _ _ hix hiy
      apply (idem_iff α hB (x * y)).mpr
      rw [grade_mul, (idem_iff α hB x).mp hix, (idem_iff α hB y).mp hiy, one_mul]
    · intro a x y ha hx hy hia hix hiy
      rw [hE] at ha hx hy
      have hla := ((local_idem_iff α hB e.base a).mp ⟨hia, ha⟩).2
      have hlx := ((local_idem_iff α hB e.base x).mp ⟨hix, hx⟩).2
      have hly := ((local_idem_iff α hB e.base y).mp ⟨hiy, hy⟩).2
      have hga := (idem_iff α hB a).mp hia
      have hgx := (idem_iff α hB x).mp hix
      have hgy := (idem_iff α hB y).mp hiy
      apply ext
      · simpa only [base_mul, grade_mul, hga, hgx, hgy, one_mul, α.one_act] using
          h e.base a.base x.base y.base hla hlx hly
      · simp only [grade_mul, hga, hgx, hgy, one_mul]

theorem embedding_necessary {S : Type w} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* SD B G α) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ EUnitary S ∧ LocallyROrthodox S := by
  have hE : EUnitary S := by
    constructor
    · intro e a he hea
      apply (idem_map_iff φ hinj a).mp
      apply (eUnitary α hB).1 (φ e) (φ a) ((idem_map_iff φ hinj e).mpr he)
      rw [← map_mul]
      exact (idem_map_iff φ hinj (e * a)).mpr hea
    · intro e a he hae
      apply (idem_map_iff φ hinj a).mp
      apply (eUnitary α hB).2 (φ e) (φ a) ((idem_map_iff φ hinj e).mpr he)
      rw [← map_mul]
      exact (idem_map_iff φ hinj (a * e)).mpr hae
  refine ⟨?_, hE, locallyROrthodox_of_injective hS
    ((locallyROrthodox_iff α hB).mpr hLR) φ hinj⟩
  intro e a he hle
  obtain ⟨f, k, hf, _, hfa, _⟩ := hle
  apply hE.1 f a hf
  rw [← hfa]
  exact he

end SD

/-- The wreath action shifts the argument on the right. It is a left group action. -/
def shiftAction {B : Type u} {G : Type v} [Mul B] [Group G] : Action (G → B) G where
  act h f := fun g => f (g * h)
  one_act f := by funext g; exact congrArg f (mul_one g)
  mul_act h k f := by funext g; exact congrArg f (mul_assoc g h k).symm
  act_mul h a b := rfl

theorem function_band {B : Type u} {I : Type v} [Mul B] (hB : Band B) : Band (I → B) := by
  intro f
  funext i
  exact hB (f i)

theorem function_locallyRegular {B : Type u} {I : Type v} [Mul B]
    (hLR : LocallyRegular B) : LocallyRegular (I → B) := by
  intro e a x y ha hx hy
  funext i
  apply hLR (e i) (a i) (x i) (y i)
  · exact ⟨congrFun ha.1 i, congrFun ha.2 i⟩
  · exact ⟨congrFun hx.1 i, congrFun hx.2 i⟩
  · exact ⟨congrFun hy.1 i, congrFun hy.2 i⟩

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
    Function.Injective (wreathHom σ F hF) := by
  intro s t heq
  apply hfaith s t
  · exact congrFun (congrArg SD.base heq) 1
  · exact congrArg SD.grade heq

theorem derived_embedding {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (σ : S →ₙ* G)
    (hB : Band B) (hLR : LocallyRegular B) (F : G → S → B)
    (hF : FunctorLaw σ F) (hfaith : HomFaithful σ F) :
    Band (G → B) ∧ LocallyRegular (G → B) ∧
      ∃ φ : S →ₙ* SD (G → B) G shiftAction,
        Function.Injective φ ∧ ∀ s, (φ s).grade = σ s := by
  exact ⟨function_band hB, function_locallyRegular hLR,
    wreathHom σ F hF, wreathHom_injective σ F hF hfaith, fun _ => rfl⟩

/-- Converse: every embedding over σ produces F(g,s)=g acting on the base of φ(s). -/
theorem derived_from_embedding {S : Type u} {G : Type v} {B : Type w}
    [Semigroup S] [Semigroup B] [Group G] (α : Action B G) (σ : S →ₙ* G)
    (φ : S →ₙ* SD B G α) (hinj : Function.Injective φ)
    (hgrade : ∀ s, (φ s).grade = σ s) :
    ∃ F : G → S → B, FunctorLaw σ F ∧ HomFaithful σ F := by
  refine ⟨fun g s => α.act g (φ s).base, ?_, ?_⟩
  · intro g s t
    change α.act g (φ s).base * α.act (g * σ s) (φ t).base =
      α.act g (φ (s * t)).base
    rw [map_mul, SD.base_mul, α.act_mul, α.mul_act, hgrade]
  · intro s t hbase hgr
    apply hinj
    apply SD.ext
    · simpa only [α.one_act] using hbase
    · rw [hgrade, hgrade, hgr]

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

theorem idem_iff (s : Rees G I L p) : Idem s ↔ s.grade * p s.col s.row = 1 := by
  constructor
  · intro h
    have hg : (s.grade * p s.col s.row) * s.grade = s.grade := congrArg Rees.grade h
    exact mul_right_cancel (hg.trans (one_mul s.grade).symm)
  · intro h
    apply ext p
    · rfl
    · change (s.grade * p s.col s.row) * s.grade = s.grade
      rw [h, one_mul]
    · rfl

/-- Natural order in a completely simple Rees semigroup is equality. -/
theorem naturalLE_eq {s t : Rees G I L p} (hle : NaturalLE s t) : s = t := by
  obtain ⟨e, f, he, _, hleft, hright⟩ := hle
  have hi : s.row = t.row := by rw [hright, row_mul]
  have hl : s.col = t.col := by rw [hleft, col_mul]
  have hie : t.row = e.row := by
    calc
      t.row = s.row := hi.symm
      _ = e.row := by rw [hleft, row_mul]
  apply ext p hi _ hl
  calc
    s.grade = (e.grade * p e.col t.row) * t.grade := congrArg Rees.grade hleft
    _ = t.grade := by rw [hie, (idem_iff p e).mp he, one_mul]

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
    Idem s ↔ Idem s.rees := by
  constructor
  · intro h
    exact congrArg Pastijn.rees h
  · intro h
    apply ext
    · change s.base * α.act (s.rees.grade * p s.rees.col s.rees.row) s.base = s.base
      rw [(Rees.idem_iff p s.rees).mp h, α.one_act]
      exact hB s.base
    · exact h

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
    Idem x ∧ InLocal e x ↔ x.rees = e.rees ∧ InLocal e.base x.base := by
  have her := (idem_iff p α hB e).mp he
  have hcoeff := (Rees.idem_iff p e.rees).mp her
  constructor
  · rintro ⟨hx, hl, hr⟩
    have hxr := (idem_iff p α hB x).mp hx
    have hle : NaturalLE x.rees e.rees :=
      ⟨x.rees, x.rees, hxr, hxr,
        (congrArg Pastijn.rees hr).symm, (congrArg Pastijn.rees hl).symm⟩
    have heq := Rees.naturalLE_eq p hle
    refine ⟨heq, ?_, ?_⟩
    · have hb := congrArg Pastijn.base hl
      simpa only [base_mul, heq, hcoeff, α.one_act] using hb
    · have hb := congrArg Pastijn.base hr
      simpa only [base_mul, heq, hcoeff, α.one_act] using hb
  · rintro ⟨heq, hl, hr⟩
    refine ⟨(idem_iff p α hB x).mpr (heq.symm ▸ her), ?_, ?_⟩
    · apply ext
      · simpa only [base_mul, heq, hcoeff, α.one_act] using hl
      · change e.rees * x.rees = x.rees
        rw [heq]
        exact her
    · apply ext
      · simpa only [base_mul, heq, hcoeff, α.one_act] using hr
      · change x.rees * e.rees = x.rees
        rw [heq]
        exact her

theorem regular (hB : Band B) : Regular (Pastijn B G I L p α) := by
  intro s
  let k := s.rees.grade * p s.rees.col s.rees.row
  let t : Pastijn B G I L p α :=
    ⟨α.act k⁻¹ s.base, ⟨s.rees.row, k⁻¹ * (p s.rees.col s.rees.row)⁻¹, s.rees.col⟩⟩
  refine ⟨t, ?_, ?_⟩
  · apply ext
    · simp only [base_mul, rees_mul, Rees.row_mul, t, k, mul_inv_rev, mul_assoc,
        mul_one, inv_mul_cancel]
      rw [hB (α.act ((p s.rees.col s.rees.row)⁻¹ * s.rees.grade⁻¹) s.base),
        ← mul_inv_rev, ← α.mul_act, mul_inv_cancel, α.one_act]
      exact hB s.base
    · apply Rees.ext p
      · rfl
      · simp only [rees_mul, Rees.grade_mul, Rees.row_mul, t, k, mul_inv_rev, mul_assoc,
          mul_one, mul_inv_cancel, inv_mul_cancel]
      · rfl
  · apply ext
    · simp only [base_mul, rees_mul, Rees.row_mul, t, k, mul_inv_rev, mul_assoc,
        mul_inv_cancel_left, mul_one, mul_inv_cancel, inv_mul_cancel, ← α.mul_act, α.one_act]
      rw [hB s.base]
      exact hB (α.act ((p s.rees.col s.rees.row)⁻¹ * s.rees.grade⁻¹) s.base)
    · apply Rees.ext p
      · rfl
      · simp only [rees_mul, Rees.grade_mul, Rees.row_mul, t, k, mul_inv_rev, mul_assoc,
          mul_inv_cancel_left, mul_one, inv_mul_cancel]
      · rfl

theorem locallyROrthodox (hB : Band B) (hLR : LocallyRegular B) :
    LocallyROrthodox (Pastijn B G I L p α) := by
  refine ⟨regular p α hB, ?_⟩
  intro e he
  have her := (idem_iff p α hB e).mp he
  have hmul : e.rees * e.rees = e.rees := her
  have hcoeff := (Rees.idem_iff p e.rees).mp her
  constructor
  · intro x y hx hy hix hiy
    have hX := (local_idem_iff p α hB e x he).mp ⟨hix, hx⟩
    have hY := (local_idem_iff p α hB e y he).mp ⟨hiy, hy⟩
    apply (idem_iff p α hB (x * y)).mpr
    change (x.rees * y.rees) * (x.rees * y.rees) = x.rees * y.rees
    rw [hX.1, hY.1, hmul]
    exact hmul
  · intro a x y ha hx hy hia hix hiy
    have hA := (local_idem_iff p α hB e a he).mp ⟨hia, ha⟩
    have hX := (local_idem_iff p α hB e x he).mp ⟨hix, hx⟩
    have hY := (local_idem_iff p α hB e y he).mp ⟨hiy, hy⟩
    apply ext
    · simpa only [base_mul, rees_mul, hA.1, hX.1, hY.1, hmul, hcoeff, α.one_act] using
        hLR e.base a.base x.base y.base hA.2 hX.2 hY.2
    · simp only [rees_mul, hA.1, hX.1, hY.1, hmul]

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
    LocallyROrthodox (Pastijn B G I L p α) ↔ LocallyRegular B := by
  constructor
  · intro h
    apply (band_locallyROrthodox_iff hB).mp
    apply locallyROrthodox_of_injective (band_regular hB) h (baseHom p α i l)
    intro a b heq
    exact congrArg Pastijn.base heq
  · exact locallyROrthodox p α hB

/-- Lemma 0 for reading (P), with actual Rees/Pastijn coordinates. -/
theorem embedding_necessary {S : Type*} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* Pastijn B G I L p α) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ LocallyROrthodox S := by
  exact ⟨weaklyEUnitary_of_injective (weaklyEUnitary p α hB) φ hinj,
    locallyROrthodox_of_injective hS (locallyROrthodox p α hB hLR) φ hinj⟩

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
    θ.act (x * y) a = a ↔ θ.act (Rees.unitOf p x) a = a := by
  have hxy : Idem (x * y) := by
    change (x * y) * (x * y) = x * y
    rw [← mul_assoc, hxyx]
  have hunit := Rees.unitOf_eq_of_idem p hxy
  constructor
  · intro h
    have h' : θ.act (Rees.unitOf p (x * y)) a = a := by rw [hunit]; exact h
    have h'' := fixed_sameRow p θ h' x.col
    simpa only [Rees.row_mul, Rees.unitOf] using h''
  · intro h
    have h' := fixed_sameRow p θ h y.col
    have heq : Rees.localUnit p x.row y.col = x * y := hunit
    rw [heq] at h'
    exact h'

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
    Idem s ↔ Idem (rees p θ s) := by
  constructor
  · intro h
    exact congrArg (rees p θ) h
  · intro h
    apply ext
    · change base p θ s * θ.act (rees p θ s) (base p θ s) = base p θ s
      rw [act_fix p θ h]
      exact hB (base p θ s)
    · exact h

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

theorem regular (hB : Band B) : Regular (Restricted B G I L p θ) := by
  intro s
  let x := rees p θ s
  let a := base p θ s
  let y := Rees.inverse p x
  have hlaws := Rees.inverse_laws p x
  have hxyx : (x * y) * x = x := hlaws.1
  have hyxy : (y * x) * y = y := hlaws.2
  let t : Restricted B G I L p θ := ⟨(θ.act y a, y), by
    change θ.act (Rees.unitOf p y) (θ.act y a) = θ.act y a
    rw [← θ.mul_act, Rees.unitOf_mul]⟩
  have hfix : θ.act (x * y) a = a := by
    rw [Rees.mul_inverse]
    exact s.property
  refine ⟨t, ?_, ?_⟩
  · apply ext
    · change (a * θ.act x (θ.act y a)) * θ.act (x * y) a = a
      rw [← θ.mul_act, hfix, hB a]
      exact hB a
    · exact hxyx
  · apply ext
    · change (θ.act y a * θ.act y a) * θ.act (y * x) (θ.act y a) = θ.act y a
      rw [hB (θ.act y a), ← θ.mul_act, hyxy]
      exact hB (θ.act y a)
    · exact hyxy

theorem local_idem_iff (hB : Band B) (e x : Restricted B G I L p θ) (he : Idem e) :
    Idem x ∧ InLocal e x ↔
      rees p θ x = rees p θ e ∧ InLocal (base p θ e) (base p θ x) := by
  have her := (idem_iff p θ hB e).mp he
  have hefix := act_fix p θ her
  constructor
  · rintro ⟨hx, hl, hr⟩
    have hxr := (idem_iff p θ hB x).mp hx
    have hle : NaturalLE (rees p θ x) (rees p θ e) :=
      ⟨rees p θ x, rees p θ x, hxr, hxr,
        (congrArg (rees p θ) hr).symm, (congrArg (rees p θ) hl).symm⟩
    have heq := Rees.naturalLE_eq p hle
    have hxfix : θ.act (rees p θ e) (base p θ x) = base p θ x := by
      rw [← heq]
      exact act_fix p θ hxr
    refine ⟨heq, ?_, ?_⟩
    · have hb := congrArg (base p θ) hl
      simpa only [base_mul, hxfix] using hb
    · have hb := congrArg (base p θ) hr
      simpa only [base_mul, heq, hefix] using hb
  · rintro ⟨heq, hl, hr⟩
    have hxr : Idem (rees p θ x) := heq.symm ▸ her
    have hxfix : θ.act (rees p θ e) (base p θ x) = base p θ x := by
      rw [← heq]
      exact act_fix p θ hxr
    refine ⟨(idem_iff p θ hB x).mpr hxr, ?_, ?_⟩
    · apply ext
      · simpa only [base_mul, hxfix] using hl
      · change rees p θ e * rees p θ x = rees p θ x
        rw [heq]
        exact her
    · apply ext
      · simpa only [base_mul, heq, hefix] using hr
      · change rees p θ x * rees p θ e = rees p θ x
        rw [heq]
        exact her

theorem locallyROrthodox (hB : Band B) (hLR : LocallyRegular B) :
    LocallyROrthodox (Restricted B G I L p θ) := by
  refine ⟨regular p θ hB, ?_⟩
  intro e he
  have her := (idem_iff p θ hB e).mp he
  have hmul : rees p θ e * rees p θ e = rees p θ e := her
  constructor
  · intro x y hx hy hix hiy
    have hX := (local_idem_iff p θ hB e x he).mp ⟨hix, hx⟩
    have hY := (local_idem_iff p θ hB e y he).mp ⟨hiy, hy⟩
    apply (idem_iff p θ hB (x * y)).mpr
    change (rees p θ x * rees p θ y) * (rees p θ x * rees p θ y) = rees p θ x * rees p θ y
    rw [hX.1, hY.1, hmul]
    exact hmul
  · intro a x y ha hx hy hia hix hiy
    have hA := (local_idem_iff p θ hB e a he).mp ⟨hia, ha⟩
    have hX := (local_idem_iff p θ hB e x he).mp ⟨hix, hx⟩
    have hY := (local_idem_iff p θ hB e y he).mp ⟨hiy, hy⟩
    have haFix : θ.act (rees p θ e) (base p θ a) = base p θ a := by
      rw [← hA.1]; exact act_fix p θ ((idem_iff p θ hB a).mp hia)
    have hxFix : θ.act (rees p θ e) (base p θ x) = base p θ x := by
      rw [← hX.1]; exact act_fix p θ ((idem_iff p θ hB x).mp hix)
    have hyFix : θ.act (rees p θ e) (base p θ y) = base p θ y := by
      rw [← hY.1]; exact act_fix p θ ((idem_iff p θ hB y).mp hiy)
    apply ext
    · simpa only [base_mul, rees_mul, hA.1, hX.1, hY.1, hmul,
        θ.act_mul, haFix, hxFix, hyFix] using
        hLR (base p θ e) (base p θ a) (base p θ x) (base p θ y) hA.2 hX.2 hY.2
    · simp only [rees_mul, hA.1, hX.1, hY.1, hmul]

/-- Lemma 0 for reading (R). -/
theorem embedding_necessary {S : Type*} [Semigroup S] (hS : Regular S)
    (hB : Band B) (hLR : LocallyRegular B)
    (φ : S →ₙ* Restricted B G I L p θ) (hinj : Function.Injective φ) :
    WeaklyEUnitary S ∧ LocallyROrthodox S := by
  exact ⟨weaklyEUnitary_of_injective (weaklyEUnitary p θ hB) φ hinj,
    locallyROrthodox_of_injective hS (locallyROrthodox p θ hB hLR) φ hinj⟩

end Restricted

end P1

/-! Auditable definitions, root statements, and transitive standard axioms. -/
set_option pp.proofs false
#print P1.Idem
#print P1.Band
#print P1.Regular
#print P1.NaturalLE
#print P1.WeaklyEUnitary
#print P1.EUnitary
#print P1.InLocal
#print P1.RegularBand
#print P1.LocallyRegular
#print P1.LocallyROrthodox
#print P1.Action
#print P1.SD
#print P1.Rees
#print P1.Pastijn
#print P1.EndAction
#print P1.Restricted
#print P1.FunctorLaw
#print P1.HomFaithful
#print P1.shiftAction
#print P1.wreathHom
#print P1.regular_iff_innerInverse
#print axioms P1.regular_iff_innerInverse
#print P1.regular_local
#print axioms P1.regular_local
#print P1.Action.act_bijective
#print axioms P1.Action.act_bijective
#print P1.SD.instSemigroup
#print axioms P1.SD.instSemigroup
#print P1.SD.idem_iff
#print axioms P1.SD.idem_iff
#print P1.SD.regular
#print axioms P1.SD.regular
#print P1.SD.eUnitary
#print axioms P1.SD.eUnitary
#print P1.SD.weaklyEUnitary
#print axioms P1.SD.weaklyEUnitary
#print P1.SD.local_idem_iff
#print axioms P1.SD.local_idem_iff
#print P1.SD.locallyROrthodox_iff
#print axioms P1.SD.locallyROrthodox_iff
#print P1.SD.embedding_necessary
#print axioms P1.SD.embedding_necessary
#print P1.function_band
#print axioms P1.function_band
#print P1.function_locallyRegular
#print axioms P1.function_locallyRegular
#print P1.wreathHom_injective
#print axioms P1.wreathHom_injective
#print P1.derived_embedding
#print axioms P1.derived_embedding
#print P1.derived_from_embedding
#print axioms P1.derived_from_embedding
#print P1.Rees.idem_iff
#print axioms P1.Rees.idem_iff
#print P1.Rees.naturalLE_eq
#print axioms P1.Rees.naturalLE_eq
#print P1.Pastijn.instSemigroup
#print axioms P1.Pastijn.instSemigroup
#print P1.Pastijn.idem_iff
#print axioms P1.Pastijn.idem_iff
#print P1.Pastijn.regular
#print axioms P1.Pastijn.regular
#print P1.Pastijn.local_idem_iff
#print axioms P1.Pastijn.local_idem_iff
#print P1.Pastijn.locallyROrthodox
#print axioms P1.Pastijn.locallyROrthodox
#print P1.Pastijn.locallyROrthodox_iff
#print axioms P1.Pastijn.locallyROrthodox_iff
#print P1.Pastijn.embedding_necessary
#print axioms P1.Pastijn.embedding_necessary
#print P1.Restricted.carrier_iff_for_inverse
#print axioms P1.Restricted.carrier_iff_for_inverse
#print P1.Restricted.instSemigroup
#print axioms P1.Restricted.instSemigroup
#print P1.Restricted.idem_iff
#print axioms P1.Restricted.idem_iff
#print P1.Restricted.regular
#print axioms P1.Restricted.regular
#print P1.Restricted.local_idem_iff
#print axioms P1.Restricted.local_idem_iff
#print P1.Restricted.locallyROrthodox
#print axioms P1.Restricted.locallyROrthodox
#print P1.Restricted.embedding_necessary
#print axioms P1.Restricted.embedding_necessary
