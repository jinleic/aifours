# Stochastic H∞ preview control: necessary and sufficient conditions

Status of this file: derivation and proofs written 2026-10-14 (PT). The finite-horizon result
(Theorem 1) is proved in full below. The infinite-horizon result (Theorem 2) is proved at the
level of a detailed argument that cites standard facts (well-posedness and continuous dependence
of linear stochastic functional differential equations (SFDEs), positive renewal equations,
Perron–Frobenius for positive maps) without re-proving them; Section 6 lists exactly what is
cited. Numerical checks are in `../evidence/`.

**Literal-norm continuation (same date):** `literal_continuation.md` proves an
exact constant-matrix finite-horizon separation between the printed criterion
and this file's F1 substitute, including adapted disturbances and effective
control. Its control-noise corollary also has B0 != 0. Thus the necessity below
must not be transferred to the literal norm; none of the arguments in this
file establishes a general literal sufficiency theorem either. The original
finite- and infinite-horizon literal synthesis problems remain unresolved here.

## 0. Problem and formalization

**Book problem** (《10000个科学难题·信息科学卷》, pp. 674–676, 张焕水, 王宏霞). System (1):

    dx(t) = [A x(t) + B u(t) + C w(t-h)] dt + [A0 x(t) + B0 u(t)] dW(t),
    z(t)  = D0 x(t) + D1 u(t),

W a Brownian motion, h ≥ 0 the preview length. For given γ > 0 find a full-information
controller (2) u(t) = F(x(t), w(s) | t-h ≤ s ≤ t) with (3)
E‖z‖_{L2[a,b]} / E‖w‖_{L2[a,b-h]} < γ; finite horizon (a, b bounded) and infinite horizon
(b → ∞). The book asks for necessary and sufficient solvability conditions and the controller.

**Formalization used here.** Each item is labelled as an interpretation (I), a restriction (R) or a
substantive replacement (S) of the book's text. Nothing else is changed. All theorems below are
theorems about this formalization.

* **F1 (S) Mean-square norms.** ‖z‖ := (E∫_a^b |z|² dt)^{1/2} and ‖w‖ := (E∫_a^{b-h} |w|² dt)^{1/2}.
  The printed ratio E[(∫|z|²)^{1/2}] / E[(∫|w|²)^{1/2}] (pathwise L² norm, then expectation: an
  L¹(Ω; L²) quantity) is a different criterion, and it is **not** solved here. Reasons for the
  replacement: (a) on p. 676 the book identifies the stochastic H∞ problem with a *generalized
  Riccati equation*; that correspondence (stochastic bounded real lemma, Hinrichsen–Pritchard 1998)
  holds for the Hilbert-space norm; (b) the problem's proposers use exactly this criterion,
  E[‖z‖²]/E‖v‖² < γ², in their own 2014 paper on the same model (Wang, Zhang, Chen, Yu,
  J. Harbin Inst. Technol. 46(7), eq. (4); full text read by the main agent).
* **F2 (I) Disturbances** may be random: w ∈ 𝒲 := L²_𝔽(a, b-h; R^m), progressively measurable with
  respect to the augmented Brownian filtration 𝔽 = (𝔽_t). This is an assumption: the book's E‖w‖
  is consistent with random w but does not force it. Deterministic w form a subclass. Sufficiency
  covers them. Necessity uses random (feedback) worst-case disturbances, so the variant "sup over
  deterministic w only" is **not** covered. Independent extra randomisation is harmless (enlarge
  𝔽, W stays Brownian). Disturbance values outside the counted window are zero:
  w(s) := 0 for s ∈ [a-h, a) and for s > b-h. The latter do not reach the plant before b anyway;
  setting them to 0 stops a controller from reacting to uncounted inputs.
  If b-h<=a, the counted disturbance space is {0} and its energy integral is zero; its
  zero-start existence problem is trivial with u=0. In that case k=0 and (𝒫) is the
  ordinary positive stochastic LQ equation, whose bounded finite-horizon solution follows
  from Lemmas 3 and 5 and the cost bound obtained by choosing u=0.
* **F3 (I) Initial state** x(a) = 0 (the book's ratio has no initial-state term).
* **F4 (I) Controllers.** Admissible rules are nonanticipative measurable path functionals,
  possibly nonlinear and history-dependent, with strong existence and pathwise uniqueness
  for every w in 𝒲 and u in L²_𝔽. They are event-local: when two disturbance paths agree
  up to t on an event, their state and control paths agree there up to t, with the same
  Brownian path and random seed. Necessity allows the full past Brownian information;
  sufficiency supplies the book's more restricted controller (2).
* **F5 (I) Strict bound** = induced norm with a uniform margin: sup_{w ≠ 0} ‖z‖/‖w‖ < γ. Requiring
  only ‖z‖ < γ‖w‖ separately for each w ≠ 0 changes the solvable set of γ at most at the single
  point γ_opt: such a controller has ‖T‖ ≤ γ, and γ ≥ inf_𝒦 ‖T_𝒦‖ = γ_opt.
* **F6 (R) Regularity.** D1(t)ᵀD1(t) ⪰ r0 I for some r0 > 0 uniformly in t, and all data are bounded
  measurable on [a, b]. Constant data with D1 of full column rank (the book's setting) satisfy this.
  For the infinite horizon the data are constant. The deterministic results the book calls solved
  (Tadmor–Mirkin 2005; Kojima–Ishijima 2006) also assume a full-rank D1. Uniformity matters: the
  external referee (Codex, `../evidence/codex-referee-reply.md`, objection 1) gave time-varying data
  with D1(t)ᵀD1(t) > 0 pointwise but inf = 0, for which a controller exists while (𝒫) cannot be
  continued across the singular time. W is scalar, as in the book; for vector W = (W_1, …, W_d),
  replace A0ᵀPA0, B0ᵀPB0, B0ᵀPA0 by sums over i.
* **F7 (I) Infinite horizon.** a = 0, b = ∞; the controller must also make the closed loop
  internally mean-square stable (Section 5). The book is silent; this is the standard requirement.
* **F8 (R) Infinite-horizon data assumptions.** The mean-square stabilizability and
  detectability assumptions (A2)–(A3) are additional restrictions, imposed on the
  transformed data after the feedback substitution in (A1). Detectability of the original
  data does not automatically imply detectability of those transformed data.

Write v(t) := w(t-h) for the disturbance acting on the plant at time t. Then v = 0 on [a, a+h),
v(t) is 𝔽_{t-h}-measurable, and the controller at time t knows the *preview segment*
v_t := v|[t, t+h] = w|[t-h, t]. The cost is

    J(u, w) := E∫_a^b |z|² dt − γ² E∫_a^{b-h} |w|² dt = E∫_a^b |z|² dt − γ² E∫_{a+h}^{b} |v|² dt,

For a nonempty counted input interval, ‖T‖<γ is equivalent to J(u,w)<=−ε‖w‖²
for every w in 𝒲, including zero: Lemma 5a below supplies the nontrivial zero-input step.
For the empty-input convention in F2, existence is handled directly by u=0 and the plain LQ equation.

## 1. Objects built from P

For symmetric P with R̂(P) ≻ 0 define (in particular for every P ⪰ 0, where R̂ ⪰ r0 I by F6)

    R̂(P) = D1ᵀD1 + B0ᵀPB0,     S(P) = B0ᵀPA0 + D1ᵀD0,     L(P) = BᵀP + S(P),
    Ã(P) = A − B R̂⁻¹ S,         Q̃(P) = A0ᵀPA0 + D0ᵀD0 − Sᵀ R̂⁻¹ S   (⪰ 0 when P ⪰ 0),
    H0(P) = [ Ã    −B R̂⁻¹ Bᵀ ]
            [ −Q̃   −Ãᵀ       ].

When P ⪰ 0, Q̃ ⪰ 0 because it is the Schur complement of R̂ in [A0 B0]ᵀP[A0 B0] + [D0 D1]ᵀ[D0 D1] ⪰ 0.
H0(P) is Hamiltonian, the Hamiltonian of a deterministic LQ problem whose weights carry the Itô
corrections. Given a continuous P(·) on an interval, let Φ(t, s) (2n × 2n) be the transition
matrix of r ↦ H0(P(r)): ∂_t Φ(t, s) = H0(P(t)) Φ(t, s), Φ(s, s) = I. Φ is symplectic, so
Φ(t, s)⁻¹ = Φ(s, t) = [[Φ22ᵀ, −Φ12ᵀ], [−Φ21ᵀ, Φ11ᵀ]](t, s). For a ≤ t ≤ s, r ≤ min(t+h, b):

    K(t, s) := [P(t), −I] Φ(t, s) [C(s); 0] = (P(t) Φ11(t, s) − Φ21(t, s)) C(s),
    k(t)    := K(t, t+h) if t + h ≤ b,  k(t) := 0 if t + h > b,
    m(t, s) := k(t)ᵀ Φ11(t, s) C(s),
    M(t, s, r) := C(s)ᵀ Φ22(s, t) K(t, r) + 1{r < s} C(s)ᵀ Φ21(s, r) C(r),

and K(t, s) := 0, M(t, s, r) := 0 when s > b or r > b.

**The advanced generalized Riccati differential equation (𝒫).**

    −Ṗ(t) = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − L(P)ᵀ R̂(P)⁻¹ L(P) + γ⁻² k(t) k(t)ᵀ,   t ∈ [a, b],   P(b) = 0.

The right side at time t depends on P on the whole window [t, min(t+h, b)] (through Φ), so (𝒫) is
a backward functional differential equation of advanced type. It is integrated backward from b.
For t ∈ (b−h, b] it is the plain stochastic LQ Riccati equation (k = 0). For h = 0 it is the
classical stochastic H∞ generalized Riccati equation (k = PC). (Section 4 covers both reductions.)

**Feedback laws.** Along a trajectory,

    u*(t) = −R̂⁻¹ [ L x(t) + Bᵀ g(t) ],   g(t) := ∫_t^{min(t+h,b)} K(t, s) v(s) ds = ∫_{t−h}^{min(t,b−h)} K(t, r+h) w(r) dr,
    w*(t) = γ⁻² [ k(t)ᵀ x(t) + μ(t) ],    μ(t) := ∫_t^{t+h} m(t, s) v(s) ds          (t ≤ b − h).

u*(t) uses only x(t) and w on [t−h, t]: it has the book's form (2). w*(t) is 𝔽_t-measurable.
The value functional is

    V(t, x, v_t) := xᵀP(t)x + 2xᵀ∫ K(t, s) v(s) ds + ∫∫ v(s)ᵀ M(t, s, r) v(r) ds dr   (window [t, min(t+h,b)]).

## 2. Theorem 1 (finite horizon)

**Theorem 1.** Assume F1–F6, in particular all progressive adapted disturbances (including feedback disturbances correlated with W), γ > 0 and h ≥ 0. The following are equivalent.

1. There is an admissible controller with sup_{w ≠ 0} ‖z‖/‖w‖ < γ.
2. (𝒫) has a solution on all of [a, b]: its maximal backward solution from P(b) = 0 does not
   escape to infinity on [a, b].

When (2) holds, P(t) ≥ 0 on [a, b], the controller u* above is admissible, has the book's form
(2), and attains sup ‖z‖/‖w‖ < γ. Moreover, for every admissible u and every w ∈ 𝒲,

    J(u, w) = E∫_a^b |R̂^{1/2}(u − u*)|² dt − γ² E∫_a^{b−h} |w − w*|² dt     (u*, w* evaluated along the trajectory).

Consequently γ_opt := inf{γ : (𝒫) has a solution on [a, b]} = inf over admissible controllers of
sup ‖z‖/‖w‖. No controller is *strictly* feasible at γ = γ_opt (solvability of (𝒫) on the compact
interval is an open condition in γ). Whether some controller attains the induced gain γ_opt exactly
is not addressed.

## 3. Proof of Theorem 1

### 3.1 Lemma 1 (kernel identities)

Let P be an absolutely continuous solution of (𝒫) on [t0, b] (Carathéodory sense: (𝒫) holds for
a.e. t) with R̂(P(t)) ⪰ δI for some δ > 0. No sign condition on P is assumed. Then for
t0 ≤ t ≤ s, r ≤ min(t+h, b), and for a.e. t:

* (K1) K(t, t) = P(t) C(t).
* (K2) ∂_t K(t, s) = −A_c(t)ᵀ K(t, s) − γ⁻² k(t) m(t, s), where A_c := A − B R̂⁻¹ L = Ã − B R̂⁻¹ Bᵀ P.
* (M0) M(t, s, r)ᵀ = M(t, r, s); M(t, t, r) = C(t)ᵀ K(t, r); M(t, s, t+h) = m(t, s)ᵀ when t + h ≤ b.
* (M1) ∂_t M(t, s, r) = K(t, s)ᵀ B R̂⁻¹ Bᵀ K(t, r) − γ⁻² m(t, s)ᵀ m(t, r).

*Proof.* (K1): Φ(t, t) = I. (K2): ∂_tΦ(t, s) = H0(t)Φ(t, s) and [P, −I]H0 = [PÃ + Q̃, −PBR̂⁻¹Bᵀ + Ãᵀ], so

    ∂_t K = (Ṗ + PÃ + Q̃) Φ11 C + (Ãᵀ − P B R̂⁻¹ Bᵀ) Φ21 C,
    −A_cᵀ K = −(Ãᵀ − P B R̂⁻¹ Bᵀ)(P Φ11 − Φ21) C.

The difference is (Ṗ + ÃᵀP + PÃ + Q̃ − P B R̂⁻¹ Bᵀ P) Φ11 C. Since
ÃᵀP + PÃ + Q̃ − PBR̂⁻¹BᵀP = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − LᵀR̂⁻¹L (expand L = BᵀP + S), (𝒫)
makes it −γ⁻² k kᵀ Φ11(t, s) C(s) = −γ⁻² k(t) m(t, s).

(M0): Symmetry needs Φ22(s, t)Φ21(r, t)ᵀ + Φ21(s, r) = Φ21(s, t)Φ22(r, t)ᵀ for t ≤ r < s. Expand
Φ(s, t) = Φ(s, r)Φ(r, t); the difference of the two sides is
Φ21(s, r)[Φ11Φ22ᵀ − Φ12Φ21ᵀ](r, t) + Φ22(s, r)[Φ21Φ22ᵀ − Φ22Φ21ᵀ](r, t) − Φ21(s, r). By
symplecticity (ΦJΦᵀ = J) the brackets are I and 0, so the difference vanishes. M(t, t, r) = C(t)ᵀK(t, r)
because Φ22(t, t) = I. Finally M(t, s, t+h) = C(s)ᵀΦ22(s, t)k(t), and
k(t)ᵀΦ11(t, s)C(s) = C(t+h)ᵀ[Φ21(t+h, t) + Φ22(t+h, t)P(t)]Φ11(t, s)C(s); the semigroup property
gives m(t, s) = M(t, t+h, s), and symmetry gives M(t, s, t+h) = m(t, s)ᵀ.

(M1): ∂_tΦ(s, t) = −Φ(s, t)H0(t), so ∂_tΦ22(s, t) = Φ21(s, t)BR̂⁻¹Bᵀ + Φ22(s, t)Ãᵀ. With (K2),

    ∂_t M = Cᵀ[Φ21(s,t) + Φ22(s,t) P] B R̂⁻¹ Bᵀ K(t, r) − γ⁻² Cᵀ Φ22(s,t) k(t) m(t, r).

The first factor is K(t, s)ᵀ (symplectic inverse) and Cᵀ Φ22(s,t) k(t) = m(t, s)ᵀ by (M0). The
indicator term does not depend on t. ∎

### 3.2 Lemma 2 (completion of squares)

Let P be as in Lemma 1 on [t0, b]. Take any 𝔽_{t0}-measurable square-integrable initial data
(x(t0), v_{t0}), any adapted u ∈ L²_𝔽, and any w ∈ L²_𝔽(t0, b−h) (extended by 0 after b−h, F2).
Then

    E∫_{t0}^b |z|² − γ² E∫_{t0}^{b−h} |w|²
      = E V(t0, x(t0), v_{t0}) + E∫_{t0}^b |R̂^{1/2}(u − u*)|² − γ² E∫_{t0}^{b−h} |w − w*|².

*Proof.* Write g(t) = ∫K(t, s)v(s)ds and N(t) = ∫∫ v(s)ᵀM(t, s, r)v(r) ds dr over the window. Both are
absolutely continuous in t with no dW part. For a.e. t (Lebesgue points of v), the incoming value
v(t+h) = w(t) and the outgoing value v(t) give

    ġ = k w − K(t,t) v(t) + ∫ ∂_tK v ds,      Ṅ = 2 w ᵀ∫ M(t, t+h, r) v(r) dr − 2 v(t)ᵀ ∫ M(t, t, r) v(r) dr + ∫∫ vᵀ ∂_tM v.

For t > b−h, k = 0 and M(t, t+h, ·) = 0. Itô's formula for xᵀPx, plus the product rule for xᵀg
(no covariation term), gives the drift of V(t) := V(t, x(t), v_t):

    xᵀṖx + 2xᵀP(Ax + Bu + Cv(t)) + (A0x + B0u)ᵀP(A0x + B0u)
      + 2(Ax + Bu + Cv(t))ᵀ g + 2xᵀ ġ + Ṅ.

Add |z|² − γ²|w|² and group terms.

* Terms in v(t): 2xᵀ(PC − K(t,t))v(t) + 2v(t)ᵀ(Cᵀg − ∫M(t,t,r)v(r)dr). These vanish by (K1) and (M0).
* Terms in u: uᵀR̂u + 2uᵀ(Lx + Bᵀg) = |R̂^{1/2}(u − u*)|² − (Lx + Bᵀg)ᵀR̂⁻¹(Lx + Bᵀg).
* Terms in w: 2wᵀ(kᵀx + μ) − γ²|w|² = −γ²|w − w*|² + γ⁻²|kᵀx + μ|². Here μ = ∫M(t,t+h,s)v(s)ds by (M0).

The remaining terms are quadratic in (x, v_t): the x–x block is (𝒫); the x–v(s) block is (K2);
the v(s)–v(r) block is (M1). They cancel identically. Hence

    dV + (|z|² − γ²|w|²)dt = (|R̂^{1/2}(u − u*)|² − γ²|w − w*|²)dt + dM_t,

where M_t = ∫ 2(Px + g)ᵀ(A0x + B0u) dW. The integrand need not be square integrable (fourth
moments may be infinite), but bounded coefficients give E sup|x|² < ∞, E sup|g|² < ∞ and
σ := A0x + B0u ∈ L²_𝔽. Hence E(∫|(Px + g)ᵀσ|² dt)^{1/2} ≤ (E sup|Px + g|²)^{1/2}(E∫|σ|²)^{1/2} < ∞,
and by the Burkholder–Davis–Gundy inequality M is a uniformly integrable martingale with E M_b = 0.
Integrate, take expectations, and use V(b, ·) = 0 (P(b) = 0 and an empty window). ∎

### 3.3 Sufficiency (2 ⇒ 1)

*Lemma 3 (P ⪰ 0).* Let P solve (𝒫) on [t0, b] with R̂(P) ≻ 0 there. Apply Lemma 2 with x(t0) = x,
v_{t0} = 0, u = u*, w = 0. This gives xᵀP(t0)x = E∫|z|² + γ²E∫|w*|² ≥ 0, so P(t0) ⪰ 0. Hence on
any interval of existence inside the open set 𝒟 := {P : R̂(P) ≻ 0}, P ⪰ 0, and therefore
R̂(P) ⪰ D1ᵀD1 ⪰ r0 I (F6). The solution therefore stays a uniform distance away from ∂𝒟; it can leave
𝒟 only by becoming unbounded. ∎

*Lemma 4 (bounded inverse).* Under u*, define η := w − w*. The map η ↦ w is well defined and
bounded on L²_𝔽: ‖w‖ ≤ c‖η‖.

*Proof.* The closed loop is the linear SFDE

    dx = (A_c x − BR̂⁻¹Bᵀ g + C v) dt + ((A0 + B0F) x − B0R̂⁻¹Bᵀ g) dW,      F := −R̂⁻¹L,
    w(t) = γ⁻²[k(t)ᵀ x(t) + ∫_{t−h}^{t} m(t, r+h) w(r) dr] + η(t),

where g and v are linear in the past of w with bounded kernels. Picard iteration gives existence
and uniqueness. Let φ(t) = E|x(t)|² and ψ(t) = E|w(t)|². Then
ψ(t) ≤ c1 φ(t) + c2 ∫_a^t ψ + 3E|η(t)|² and φ(t) ≤ c3 ∫_a^t (φ + ψ). Gronwall gives
∫_a^{b−h} ψ ≤ c E∫|η|². ∎

*Proof of 2 ⇒ 1.* At t0 = a, x(a) = 0 and v_a = 0, so V(a) = 0. Lemma 2 with u = u* gives
J(u*, w) = −γ²‖w − w*‖² ≤ −(γ²/c²)‖w‖² by Lemma 4. Hence E∫|z|² ≤ γ²(1 − c⁻²)‖w‖² (necessarily
c ≥ 1), so sup ‖z‖/‖w‖ ≤ γ(1 − c⁻²)^{1/2} < γ. ∎

### 3.4 Necessity (1 ⇒ 2)

Assume a controller 𝒦 is admissible with E∫|z|² ≤ γ1²E∫|w|² for all w ∈ 𝒲, where γ1 < γ.
Put ε := γ² − γ1².

*Lemma 5 (local existence and continuation).* (𝒫) is a backward functional differential equation
whose right side at t is a function of t and of P on [t, min(t+h, b)]. Work on the open
neighbourhood 𝒩 := {P symmetric : R̂(P) ≻ (r0/2) I} ⊃ {P ⪰ 0}. On histories with values in a bounded
subset of 𝒩 the right side is measurable in t and Lipschitz in the sup norm, uniformly in t:
‖R̂⁻¹‖ ≤ 2/r0, and Φ depends Lipschitz-continuously on the bounded coefficients of H0.
Carathéodory–Picard iteration in 𝒩 therefore gives a unique absolutely continuous solution on a
maximal interval (t*, b] with values in 𝒩. By Lemma 3 these values lie in {P ⪰ 0}, which is a
uniform distance inside 𝒩. If t* ≥ a, then sup_{(t*, b]} |P| = ∞: a bounded solution has a bounded
derivative, so it has a limit at t* (still in {P ⪰ 0}) and can be continued. ∎

*Lemma 5a (zero-input output).* On b-h>a, a strongly well-posed event-local controller
with a gain bound γ1<γ for every nonzero adapted w also has zero output at w=0.
Choose t0 in (a,b-h) and A in 𝔽_t0 with 0<Pr(A)<1, available from Brownian non-atomicity.
For wε=ε1_A1_[t0,b-h], event locality makes its output on A-complement equal the
zero-input output z0. Thus E[1_(A-complement)∫|z0|²]<=γ1² ε²Pr(A)(b-h-t0).
Let ε decrease to zero. Repeating with A-complement in place of A makes z0 vanish
on A as well, hence on the whole space. No continuity of the controller in w is assumed.
This step is false for a deterministic-only disturbance class: a controller can add a
nonzero final-tail output only when the entire counted input history is zero.

*Lemma 6 (uniform concavity transfers to subintervals).* For t ∈ [a, b−h] and w ∈ L²_𝔽(t, b−h),
define W_t(w) := inf_u J_t(u, w; 0, 0). Here the infimum is over all adapted u ∈ L²_𝔽(t, b), and
J_t is the cost on [t, b] from x(t) = 0, v_t = 0. Then W_t(w) ≤ −ε‖w‖².

*Proof.* Extend w by 0 on [a,t). Strong nonanticipation and event locality identify the
trajectory there with the w≡0 trajectory. Lemma 5a shows that the latter has z≡0
on [a,b]. Let x̄(t) be its state at t and ū its control on [t,b]; let u_𝒦 be the
controller's control on [t,b] for the extended w. The
plant is linear. So the response from zero data at t to (u_𝒦 − ū, w) equals the response from
x̄(t) to (u_𝒦, w) minus the response from x̄(t) to (ū, 0). The second response has z ≡ 0. Hence
J_t(u_𝒦 − ū, w; 0, 0) = J(𝒦, w) ≤ −ε‖w‖², and u_𝒦 − ū is adapted. ∎

*Lemma 7 (uniform upper bound).* For t ∈ [a, b], x ∈ R^n and every w ∈ L²_𝔽(t, b−h),

    inf_u J_t(u, w; x, 0) ≤ c_*|x|² − (ε²/γ²)‖w‖²,     c_* := (1 + γ²/ε) c_0,
    c_0 := sup_{t, |x|=1} E∫_t^b |D0 Ξ(s, t) x|² ds,

where Ξ(·, t)x solves dξ = Aξ ds + A0ξ dW with ξ(t) = x. In particular sup_w inf_u J_t ≤ c_*|x|².

*Proof.* Fix w, and choose u0 adapted with J_t(u0, w; 0, 0) ≤ W_t(w) + δ (u0 := 0 if t > b−h). The
response from x to (u0, w) is z0 + z_x, where z_x = D0Ξx. Take ρ = ε/γ² in
|z0 + z_x|² ≤ (1+ρ)|z0|² + (1+ρ⁻¹)|z_x|², then use Lemma 6:

    J_t(u0, w; x, 0) ≤ (1+ρ)(W_t(w) + δ + γ²‖w‖²) − γ²‖w‖² + (1+ρ⁻¹)‖z_x‖²
                     ≤ −(ε²/γ²)‖w‖² + (1+ρ)δ + (1 + γ²/ε) c_0|x|².

Let δ → 0. (The free response z_x may be replaced by the response of any fixed linear feedback
u = F0ξ, with Ξ replaced by the corresponding closed-loop fundamental matrix; the decomposition
z = z0 + z_x stays exact because the plant is linear. This is used in Section 5.) ∎

*Lemma 8 (the value is attained against the worst-case disturbance).* Let t ∈ (t*, b] and
x ∈ R^n. Run the closed loop (u*, w*) from x(t) = x, v_t = 0; call the trajectory (x°, u°, w°).
Then xᵀP(t)x = inf_u J_t(u, w°; x, 0). Here w° is a fixed process and u is arbitrary adapted.

*Proof.* Put p := P x° + g° and q := P(A0 x° + B0 u°). The (K2) identity and (𝒫) give

    dp = −(Aᵀp + A0ᵀq + D0ᵀz°) dt + q dW,     p(b) = 0,

so (p, q) is the adjoint of the convex problem min_u J_t(u, w°; x, 0). By the definition of u°,
Bᵀp + B0ᵀq + D1ᵀz° = 0. Expanding the drift of p reproduces the computation in Lemma 2: the
v(t) terms cancel by (K1), and the w-term kw° combines with ∫∂_tK v through (K2). For any other
adapted u, let δx solve the homogeneous equation with input δu = u − u°. Duality on d(pᵀδx) gives
E∫z°ᵀD0δx = E∫(Bᵀp + B0ᵀq)ᵀδu. Hence J_t(u) − J_t(u°) = E∫|δz|² ≥ 0, and u° is optimal. Lemma 2
evaluated at (u°, w°) gives J_t(u°, w°) = V(t, x, 0) = xᵀP(t)x. ∎

*Proof of 1 ⇒ 2.* On (t*, b], Lemmas 3, 8 and 7 give
0 ≤ xᵀP(t)x = inf_u J_t(u, w°; x, 0) ≤ sup_w inf_u J_t(u, w; x, 0) ≤ c_*|x|². The bound c_* does
not depend on t, so P is bounded on (t*, b]. Lemma 5 then forces t* < a. ∎

**Remarks.** (i) The necessity proof never assumes that the given controller is linear or of the
form (2). (ii) Lemmas 7 and 8 also show that, on any interval where (𝒫) has a solution,
xᵀP(t)x = max_w min_u J_t from (x, 0). This is the lower value, and it equals the upper value
because u* attains it. (iii) A terminal penalty x(b)ᵀP_b x(b) is covered by setting
P(b)=P_b>=0 and adding that penalty to J. With P_b≠0, k may jump at b-h; the
equations remain valid in the Carathéodory sense. With P_b=0, K(t,b)=0 on the
last preview window, so k is continuous at b-h.

## 4. Reductions and structure

* **h = 0.** Then Φ(t, t) = I, so k = PC, and (𝒫) is −Ṗ = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − LᵀR̂⁻¹L
  + γ⁻²PCCᵀP. This is the generalized Riccati equation of full-information stochastic H∞ control
  with state- and control-dependent noise. Theorem 1 contains that case.
* **Deterministic case (A0 = 0, B0 = 0).** H0 no longer depends on P. Let [X; Y](t) solve
  d/dt[X; Y] = H_eff(t)[X; Y] backward from [X; Y](b) = [I; 0], where

      H_eff(t) := H0(t) + 1{t+h ≤ b} Φ(t, t+h) [[0, γ⁻²C(t+h)C(t+h)ᵀ], [0, 0]] Φ(t+h, t).

  Then P = Y X⁻¹ (direct computation of the Riccati equation of H_eff, whose γ-part equals
  γ⁻²(Φ21 + Φ22P)ᵀCCᵀ(Φ21 + Φ22P)). (𝒫) is solvable iff X(t) stays invertible. For constant data,
  H_eff=e^{−H0h}H_γe^{H0h} on t<=b-h, with H_γ:=H0+[[0,γ⁻²CCᵀ],[0,0]].
  On (b-h,b], H_eff=H0: no new counted disturbance enters the preview window.
  Thus the Hamiltonian transport formula must not be applied to the terminal window.
* **Stochastic case.** H0 depends on the unknown P(s) on the window through the Itô terms. So (𝒫)
  is genuinely nonlocal, and no fixed Hamiltonian matrix represents it. This is exactly where the
  book's third obstacle ("no Hamiltonian stable-subspace correspondence for the generalized
  Riccati equation") enters. The obstacle is bypassed rather than removed: the Hamiltonian over
  the window is frozen at the true P(s), and existence of P is characterized by (𝒫) itself (and,
  in Section 5, by a fixed-point equation).
* **Worst-case disturbance and prediction.** Along the closed loop (u*, w*), the identity
  w*(t) = γ⁻² C(t+h)ᵀ E[p(t+h) | 𝔽_t] holds, with p = Px + g. The conditional means
  E[(x, p)(s) | 𝔽_t], s ≥ t, solve the deterministic system [ξ; π]' = H0(P(s))[ξ; π] + [Cv(s); 0]
  on the known window, and [ξ; π]' = H_γ(P(s))[ξ; π] beyond it. This is how the stochastic
  forward–backward system is decoupled without Kalman-filter/LQR duality (the book's first
  obstacle).

## 5. Infinite horizon

Constant data, a = 0, b = ∞. Admissible controllers (F4) must in addition give internal
mean-square stability (IS): with w ≡ 0 and any x(0), E∫_0^∞|x|² ≤ c|x(0)|². The performance
requirement is sup_{w ∈ L²_𝔽(0,∞), w ≠ 0} ‖z‖/‖w‖ < γ from x(0) = 0.

Assumptions:

* (A1) D1ᵀD1 > 0 and D1ᵀD0 = 0. This is without loss of generality: the substitution
  u = ũ − (D1ᵀD1)⁻¹D1ᵀD0 x replaces (A, A0, D0) by (A − BΣ, A0 − B0Σ, (I − D1(D1ᵀD1)⁻¹D1ᵀ)D0),
  where Σ := (D1ᵀD1)⁻¹D1ᵀD0.
* (A2) **Restriction:** (A,B;A0,B0), after (A1)'s substitution, is mean-square stabilizable.
* (A3) **Restriction:** (D0;A,A0), after that same substitution, is mean-square detectable:
  some H,H0 make (A+HD0,A0+H0D0) mean-square stable. For untransformed data this
  assumption is specifically on ((I−D1(D1ᵀD1)⁻¹D1ᵀ)D0; A−BΣ, A0−B0Σ).

For P ≥ 0 put H0 := H0(P), H_γ := H0 + [[0, γ⁻²CCᵀ], [0, 0]], E := e^{H0 h},
k := [P, −I]E⁻¹[C; 0], F := −R̂⁻¹L,

    A_P := A + BF + γ⁻² E22ᵀ C kᵀ,      Γσ := [A0 − B0R̂⁻¹S, −B0R̂⁻¹Bᵀ],
    Ψ(τ) := e^{H0 τ}[I; P] (0 ≤ τ ≤ h),     Ψ(τ) := E[I; P] e^{A_P(τ−h)} (τ > h),
    𝒯_P(Σ) := ∫_0^∞ Γσ Ψ(τ) Σ Ψ(τ)ᵀ Γσᵀ dτ   (a positive linear map on n×n symmetric matrices).

**Stationary advanced GARE (𝒜):** 0 = AᵀP + PA + A0ᵀPA0 + D0ᵀD0 − LᵀR̂⁻¹L + γ⁻²kkᵀ. Equivalently,
graph(P) = Im[I; P] is invariant under H_eff(P) := E⁻¹H_γE, and A_P is the matrix of H_eff(P)
restricted to graph(P), i.e. H_eff(P)[I; P] = [I; P]A_P. (Same algebra as in Section 4. The
blocks of E⁻¹[[0, CCᵀ], [0, 0]]E are [E22ᵀ; −E21ᵀ]CCᵀ[E21, E22].)

**Definition.** P is a *stabilizing solution* if P>=0 solves (𝒜), A_P is Hurwitz (T1),
and then the well-defined positive map 𝒯_P has spectral radius below one (T2).

**Theorem 2.** Under F1–F8 and (A1)–(A3), for all progressive adapted disturbances,
the infinite-horizon problem is solvable iff (𝒜) has a stabilizing solution P.
That solution is unique and equals lim_{T→∞}P_T(0). The stationary controller u*,
with kernels K(t,t+τ)=[P,−I]e^{−H0τ}[C;0], supplies the book's information pattern.
This argument remains conditional on the standard facts listed in Section 6.

For h = 0, (T1)–(T2) say exactly that the worst-case loop (A + BF + γ⁻²CCᵀP, A0 + B0F) is
mean-square stable. Indeed, then Ψ(τ) = [I; P]e^{A_P τ} and Γσ[I; P] = A0 + B0F. So Theorem 2
reduces to the standard stabilizing-solution condition of stochastic H∞ control.

### 5.1 Lemma 9 (finite-dimensional test for the worst-case loop)

Let P ⪰ 0 solve (𝒜). Consider the worst-case closed loop (u*, w*) with history state
ξ_t := (x(t), v_t) ∈ ℋ := R^n × L²(0, h; R^m). It is exponentially mean-square stable
(E‖ξ_t‖²_ℋ ≤ M e^{−λt} E‖ξ_0‖²_ℋ) iff (T1) and (T2) hold.

*Argument.*

1. *Prediction.* Section 4 shows that the conditional means E[(x; p)(s) | 𝔽_t] solve
   [ξ; π]' = H0[ξ; π] + [Cv; 0] on [t, t+h] and [ξ; π]' = H_γ[ξ; π] after t+h, starting from
   (x(t), p(t)), p = Px + g.
2. *Consistency.* For the consistent worst-case conditional-mean trajectories, the
   relation π(s)=Pξ(s)+ĝ(s), with ĝ built from predicted v̂=γ⁻²Cᵀπ, implies
   y(s+h) in 𝒮:=E·graph(P). Write the variation-of-constants formula on [s,s+h] and use
   K(s, r) = [P, −I]e^{−H0(r−s)}[C; 0]. 𝒮 is H_γ-invariant, and H_γ restricted to 𝒮 is similar to
   A_P. So beyond the first window the means evolve by e^{A_P(·)}, and the means decay for all
   initial data iff (T1) holds. (E[I; P] has full column rank, and initial data (x0, 0) span 𝒮.)
3. *Innovations.* M(r) := E[(x; p)(s) | 𝔽_r] is a martingale in r. Its only innovation is the
   dW-part of (x, p), namely [σ; Pσ]dW with σ = A0x + B0u* = Γσ(x; p). Its sensitivity is the
   composite flow applied to [I; P], which is Ψ(s − r). Hence

       (x; p)(s) = E[(x; p)(s) | 𝔽_0] + ∫_0^s Ψ(s − r) σ(r) dW(r).

   By the Itô isometry, Σ(s) := E[σσᵀ](s) satisfies the positive renewal equation
   Σ(s) = Γσ E[m0(s)m0(s)ᵀ] Γσᵀ + ∫_0^s 𝒦_{s−r}(Σ(r)) dr, with 𝒦_τ(Σ) = ΓσΨ(τ)ΣΨ(τ)ᵀΓσᵀ and
   m0(s) := E[(x; p)(s) | 𝔽_0]. For deterministic initial data (x0, v_0), m0 is the full forced
   mean: on [0, h], ȳ(s) = e^{H0 s}[x0; Px0 + g0] + ∫_0^s e^{H0(s−r)}[Cv_0(r); 0] dr, which gives
   ȳ(h) = E[I; P](x0 + ∫_0^h (e^{−H0 r})11 C v_0(r) dr) ∈ 𝒮; after h it follows H_γ inside 𝒮.
   Replacing m0 by Ψ(s)x0 is correct only when v_0 = 0. (Referee round 2.)
4. *Renewal theory.* Under (T1), 𝒦_τ decays exponentially. If ρ(∫𝒦_τ) < 1, then by continuity
   ρ(∫e^{λτ}𝒦_τ dτ) < 1 for some λ > 0, so Σ, and hence E|(x, p)|², decays exponentially. If
   ρ ≥ 1, the Perron–Frobenius (Krein–Rutman) eigenvector Λ ≥ 0 of the adjoint map pairs
   positively with the forcing summed over a basis of initial states, so ∫⟨Λ, Σ⟩ = ∞ for some
   initial state.

### 5.2 Proof of Theorem 2

The stationary version of Lemma 2 on a finite interval [t, t'] reads
J_{[t,t']}(u, w) = E V(t) − E V(t') + E∫|R̂^{1/2}(u − u*)|² − γ²E∫|w − w*|². It holds for any P ⪰ 0
solving (𝒜), with V built from P and the time-invariant kernels.

*(⇐) Let P be stabilizing.*

0. **V ⪰ 0.** Fix (x, v_t). Use u = u* with incoming w ≡ 0 on [t, t+h]. At t+h the window is empty,
   so E V(t) = E x(t+h)ᵀPx(t+h) + E∫_t^{t+h}(|z|² + γ²|w*|²) ≥ 0. (Referee's fix.)
1. **Internal stability.** With w ≡ 0 the window empties after h, and u* = Fx. Step 0 and the
   identity give E∫_0^T(|z|² + γ²|w*|²) ≤ x0ᵀPx0 for all T. With (A1), |z|² = |D0x|² + |D1Fx|²,
   so D0x ∈ L² and Fx ∈ L². Write dx = ((A + HD0)x − HD0x + BFx)dt + ((A0 + H0D0)x − H0D0x + B0Fx)dW.
   By (A3) this is a mean-square stable system driven by L² inputs, so x ∈ L². For a linear
   time-invariant SDE that implies exponential mean-square stability of (A + BF, A0 + B0F).
2. **Worst-case loop.** It is exponentially mean-square stable in ℋ by Lemma 9.
3. **Bounded inverse (block argument; referee's fix).** Take zero initial data, u = u*,
   w = w* + η with η ∈ L²_𝔽(0, ∞). Fix a block length ℓ := h if h > 0 and ℓ := 1 if h = 0 (round 2:
   zero-length blocks would prove nothing). On each block I_n := [nℓ, (n+1)ℓ]:
   (i) the Gronwall estimate of Lemma 4 gives
   E‖ξ_{(n+1)ℓ}‖² + E∫_{I_n}(|x|² + |w|²) ≤ c1(E‖ξ_{nℓ}‖² + E∫_{I_n}|η|²);
   (ii) by linearity ξ_{(n+1)ℓ} = 𝒮_n ξ_{nℓ} + β_n. Here 𝒮_n is the homogeneous one-block
   propagator. It depends only on the increments of W on I_n, so it is independent of 𝔽_{nℓ}. β_n
   is the block response to η from zero data, with E‖β_n‖² ≤ c1E∫_{I_n}|η|²;
   (iii) by step 2 and independence, E‖𝒮_{n+j−1}⋯𝒮_n ζ‖² ≤ M e^{−λjℓ}E‖ζ‖² for every
   𝔽_{nℓ}-measurable ζ;
   (iv) ξ_{Nℓ} = Σ_{n<N} 𝒮_{N−1}⋯𝒮_{n+1}β_n. Minkowski's inequality gives
   (E‖ξ_{Nℓ}‖²)^{1/2} ≤ Σ_n (M e^{−λ(N−1−n)ℓ} c1 E∫_{I_n}|η|²)^{1/2}, and Young's inequality for
   discrete convolutions gives Σ_N E‖ξ_{Nℓ}‖² ≤ c2‖η‖²;
   (v) summing (i) over blocks gives ‖x‖² + ‖w‖² ≤ c3‖η‖².
4. **Conclusion.** Let w ∈ L²_𝔽 be arbitrary and u = u*. The u*-loop driven by w is L²-stable by
   step 1, because the window terms are L² inputs. So η := w − w* ∈ L², and ‖w‖² ≤ c3‖η‖² by
   step 3. The identity on [0, T] with V ⪰ 0 gives J_T(u*, w) ≤ −γ²‖η‖²_{[0,T]}. Since z ∈ L²,
   letting T → ∞ gives J_∞(u*, w) ≤ −(γ²/c3)‖w‖². With step 1, u* solves the problem.

*(⇒) Let 𝒦 solve the problem with margin ε = γ² − γ1².*

5. **The limit P_∞.**
   (i) Take w supported on decision times [0, T−h]. Then E∫_0^T|z|² ≤ E∫_0^∞|z|² ≤ γ1²‖w‖², so 𝒦
   solves the problem on [0, T] and P_T exists by Theorem 1.
   (ii) *Monotonicity.* Let w°_T be the T-saddle disturbance from (x, 0), extended by 0. For any
   u, J_{T'}(u, w°_T) = J_T(u, w°_T) + E∫_T^{T'}|z|² ≥ x ᵀP_T(0)x (Lemma 8). Hence
   xᵀP_{T'}(0)x ≥ inf_u J_{T'}(u, w°_T) ≥ xᵀP_T(0)x. (Here Lemmas 7–8 give
   xᵀP_{T'}(0)x = max_w min_u J_{T'}.) This uses the referee's support-restriction fix.
   (iii) *Uniform bound.* By (A2) fix a linear gain F0 with (A + BF0, A0 + B0F0) mean-square stable,
   and use Lemma 7 with the F0-closed-loop response z_x = (D0 + D1F0)ξ in place of D0Ξx. This
   keeps the decomposition exact for any 𝒦 (referee's fix for a nonlinear 𝒦), and
   E∫_0^∞|z_x|² ≤ c0|x|². Hence P_T(0) ⪯ c_* I for all T.
   (iv) *Convergence.* By time invariance P_T(t) = Π(T − t), with Π nondecreasing and bounded, so
   Π(τ) → P_∞. For τ ≥ h, Π'(τ) is a continuous function of the history window Π|[τ−h, τ]. That
   window converges uniformly to the constant P_∞, so Π'(τ) converges to the stationary right side
   at P_∞. A convergent function with a convergent derivative has derivative limit 0, so P_∞
   solves (𝒜).
6. **(T1) and (T2) at P_∞.**
   (i) Lemmas 7 (with F0) and 8 give 0 ≤ xᵀP_T(0)x ≤ c_*|x|² − (ε²/γ²)‖w°_T‖², so
   ‖w°_T‖² ≤ (γ²c_*/ε²)|x|² uniformly in T.
   (ii) On every [0, S], the T-feedback laws converge uniformly to the stationary P_∞-laws as
   T → ∞ (the kernels are continuous functions of P on the window). The trajectories converge in
   L²(Ω × [0, S]) by continuous dependence of linear SFDEs on bounded coefficients. Hence the P_∞
   worst-case disturbance from (x, 0) satisfies ‖w°_∞‖² ≤ (γ²c_*/ε²)|x|².
   (iii) The identity with V ⪰ 0 (step 0 applies to P_∞) gives
   E∫_0^S|z|² ≤ xᵀP_∞x + γ²‖w°_∞‖² for all S, so z ∈ L².
   (iv) By (A1) and (A3), x ∈ L², and then p = P_∞x + g ∈ L².
   (v) So the P_∞ worst-case loop is L²-stable from every (x, 0). By Lemma 9, steps 2 and 4,
   (T1) and (T2) hold.
7. **Uniqueness.** Let P be stabilizing.
   (a) For w ∈ L², J_∞(u*, w) ≤ xᵀPx: use the identity, and E V(T) → 0 along a sequence because
   ∫E‖ξ_t‖² dt < ∞.
   (b) Against the fixed L² process w° (the worst-case loop trajectory), every u with finite cost
   has x^u ∈ L² by (A3). Duality with the L² adjoint p = Px° + g°, using E[p(T)ᵀδx(T)] → 0 along a
   sequence (transversality), gives J_∞(u, w°) ≥ J_∞(u°, w°) = xᵀPx.
   Hence xᵀPx = max_w inf_u J_∞ from (x, 0). This value does not depend on P, so P is unique.

∎ (modulo the cited standard facts; see Section 6.)

## 6. What is proved, and what is cited

| Item | Status |
|---|---|
| Theorem 1, both directions | Proved here (Lemmas 1–8): Itô calculus, BDG, Gronwall, Carathéodory–Picard. Codex gpt-6.1-sol refereed it twice on 2026-10-14. Round 1: correct-with-fixes. Round 2, on the revised text: "correct under revised F6. No remaining substantive mathematical error found." |
| Explicit kernels K, M, the controller, the worst-case disturbance | Proved (Lemma 1). The referee re-derived K2, M0, M1 and the γ-term independently, including time-varying C. |
| Reduction h = 0 and the deterministic Hamiltonian form | Proved (algebra). The referee confirmed the h = 0 reduction of (T1)–(T2). |
| Theorem 2 (⇐) | Argument complete. Round 2: "the main N&S argument now works, modulo legitimate standard facts"; its two minor corrections (h = 0 block length; the random-history renewal forcing) are applied. Cited, not re-proved: well-posedness of linear SFDEs; renewal theory for positive convolution (Volterra) equations, used in Lemma 9. |
| Theorem 2 (⇒) | Argument complete; round 2 found steps 5–7 sound. Cited: continuous dependence of linear SFDE solutions on coefficients (step 6(ii)); Krein–Rutman for positive maps on the finite-dimensional PSD cone (Lemma 9, converse). Round 2 judged both citations legitimate in the form used. |
| F1–F8 | Formalization choices (Section 0). F1 replaces the printed norm; F8 explicitly records the transformed-data infinite-horizon restrictions. |

## 7. Referee record (Codex gpt-6.1-sol, max effort; prompt and reply in `../evidence/`)

| # | Objection (severity) | Resolution |
|---|---|---|
| 1 | Pointwise D1ᵀD1 > 0 with piecewise-continuous data is insufficient. Counterexample: D1(t) = (0, \|t−½\|)ᵀ, where a controller exists but (𝒫) cannot be continued (fatal as stated) | Accepted. F6 now requires D1ᵀD1 ⪰ r0 I uniformly and bounded data. The book's constant data satisfy this. |
| 2 | Lemma 1 assumed P ⪰ 0, which is circular with Lemma 3; solutions are only absolutely continuous (minor) | Accepted. Lemmas 1–3 and 5 now assume R̂ ≻ 0 only and hold a.e. (Carathéodory). |
| 3 | The martingale in Lemma 2 need not be square integrable (minor) | Accepted. BDG/H¹ argument added. |
| 4 | Disturbance values after b−h are undefined; a controller could react to them (minor) | Accepted. F2 sets them to 0. |
| 5 | F1 is a different norm from the printed one (major, fidelity) | Accepted. F1 is relabelled a substantive replacement; all claims are scoped to the mean-square problem. |
| 6 | Theorem 2 (⇒): the comparison with a nonlinear 𝒦 is not additive (major) | Accepted. Uses a linear stabilizing F0 from (A2), step 5(iii). |
| 7 | Theorem 2 (⇐): the impulse/Minkowski input bound was informal (major) | Accepted. Replaced by the block argument, step 3. |
| 8 | V ⪰ 0 and transversality were used without proof; monotonicity and Π' convergence needed detail (major/minor) | Accepted. Steps 0, 5(ii), 5(iv) and 7 added. |

Round 2 (`../evidence/codex-referee2-reply.md`): objections 1–6 and 8 judged resolved; objection 7
"partly", because the block argument was empty for h = 0 (now fixed with block length ℓ = 1 when
h = 0). New minor items, applied: explicit Picard neighbourhood (Lemma 5); "not attained" means no
strictly feasible controller at γ_opt; renewal forcing Γσ E[m0 m0ᵀ] Γσᵀ for random initial
histories. New evidential item: the infinite-horizon numerical "brackets" measure convergence of
P_T within T_max = 400, not solvability. The README reports them as time-budget-limited upper
estimates and uses the closed form 1.72152 at h = 0. Round 3 was not run.

## 8. Independent Claude mean-square review (continuation)

The no-tools `claude-opus-5-5`/max review in
[`../../evidence/information-science-push-20261014/meansquare-referee-findings.json`](../../evidence/information-science-push-20261014/meansquare-referee-findings.json)
returned **correct-with-fixes** for both theorems, with Theorem 2 conditional on cited facts.
R-01/R-02 are resolved by strong event-local admissibility and Lemma 5a; R-03 retains
the all-adapted disturbance quantifier and explicitly excludes deterministic-only necessity;
R-04 makes transformed-data detectability a restriction; R-05 retains the external-fact
qualifier and uses only the consistency inclusion; R-06 distinguishes the terminal window
and possible terminal-penalty jump. R-07 treats source/numerical/model-review claims as
provenance, not mathematical proof. R-08/R-09 rederived the central identities and supplied
an independently derived scalar delay benchmark. The review did not execute code or establish
novelty; these exposition/localization repairs were parent-checked, not submitted for a
further model re-review.
