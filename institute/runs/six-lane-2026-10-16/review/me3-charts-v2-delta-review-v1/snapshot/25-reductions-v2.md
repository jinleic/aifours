# ME(≤3) minimum SCV — reduction lemmas L1–L6 (v2)

Subtree `reductions/` of lane `mathematics/evidence/six-lane-20261016/me3-minimum-scv`; written by worker
`MathPhaseType3.ME3Reductions` for the integration owner `MathPhaseType3` on 2026-10-18 (host-clock times are in
`../STATUS-v2.md`). **Correctness only; no novelty, priority or "first" claim.** The global D2 bound is **not** in this
file (it is the integration owner's part); §7 states exactly what this file reduces the full problem to. This v2
supersedes `reductions-v1.md`, which is kept unchanged (sha256 ad6c5091…5536).

Every computation cited is a lane-launcher run `reductions/runs/<run>/` with pre/post receipts in
`reductions/receipts/<run>-{pre,post}.json`. Labels used in v2:
* **EXACT**: a finite identity or comparison of rationals or rational polynomials. It can be checked by hand, and it is
  re-checked by `code/exact_certs_v1.py` (run `exact-certs-v1`: decisions in `fractions.Fraction`, exact SymPy
  cross-checks, no floats).
* **COMPUTATIONAL (conditional)**: a python-flint Arb/Acb ball computation, or a SymPy root count, resultant or
  simplification. It is conditional on correct execution and semantics of that library.
* **EXPLORATORY**: floating point or non-rigorous search. It is never used as a proof step.

Outline correction (§2.5): the untrusted outline says lower-order densities "embed as faces". That is false in
general (explicit counterexample in Lemma 2.5). Only the cone *inclusion* is true, and only the inclusion is used.
Every other outline step was re-derived and holds as stated, with the precise forms given below.

**Changes from v1.** These follow the hostile review
`institute/runs/six-lane-2026-10-16/review/me3-reductions-codex-v1.note.md` (sha256 a6d34ecb…1328; disposition
ACCEPT-WITH-FIXES, no fatal defect).
1. (MINOR, review item 2) §0.2 and Lemma 2.3 now require positive mass, 0 < ∫f. Pointwise "f ≢ 0" is no longer used.
   Every exponential-polynomial application already satisfies the repaired hypothesis (Remark 2.3a).
2. (MINOR, review item 3) The contract-band check of `ctl-c-v2` is relabelled EXPLORATORY, and its actual stop
   behaviour is stated (§5, "Contract band").
3. (Review audit notes) Exact certificates replace computations on the proof path:
   * The upper separation is now v_cos ≤ 773/3844 < 0.2014 < 11/50 = T, with 773/3844 < Δ3 (Theorem 5.6). It uses the
     exact point ω = 1, cos φ = 35/37, sin φ = 12/37. The Arb point bound U is now a supplementary conditional
     computation.
   * Δ3 > 553/2000 = 0.2765 now follows from the cubic h (Lemma 4.2), replacing the Sturm run. Δ3 = s(x1) now follows
     from exact root isolation (Theorem L4(3)), replacing the ball values of s(x_i).
   * Both are verified by `exact-certs-v1`: 47/47 checks, including 5 wrong controls that fail as required.
4. (MAJOR optional, review item 1) The optional lower bound v_cos ≥ 0.20090156350055 (Theorem 5.8): the acceptance
   logic of its program was audited (runs `audit-bnb-v2` and `ctl-f-mut-cap-v1`). Decision: **KEEP** it as an optional
   COMPUTATIONAL (conditional) result with pinned files (§5, Theorem 5.8). **No lemma and no part of the theorem uses
   it.**

---

## 0. Conventions and imports

**0.1 Exponential polynomials.** An *exponential polynomial* (e.p.) is f(t) = Σ_{λ∈Λ} p_λ(t) e^{λt} with Λ ⊂ ℂ
finite and p_λ ∈ ℂ[t]∖{0}. Λ is the set of *contributing exponents*, ord f := Σ_λ (deg p_λ + 1) is the *order*, and
E(f) := {λ with multiplicity deg p_λ + 1} is the *exponent multiset*. By (I1) the representation is unique. Hence a
real-valued e.p. has Λ = Λ̄ and p_{λ̄} = conj(p_λ).

**0.2 Moments.** Densities live on [0, ∞). Take a measurable f ≥ 0 on [0, ∞) with **0 < ∫_0^∞ f** and
∫_0^∞ (1 + t²) f < ∞ (positive mass, i.e. f ≠ 0 in L¹; pointwise f ≢ 0 is NOT enough, e.g. f = 𝟙_{{0}}), and put
m_k := ∫_0^∞ t^k f(t) dt (k = 0, 1, 2), SCV(f) := m0 m2 / m1² − 1, and S(f) := SCV/(1 + SCV) = 1 − m1²/(m0 m2).
Here m0 > 0, and m1 > 0 because {f > 0} has positive measure while {0} is null. SCV ≥ 0 by Cauchy–Schwarz
(m1² ≤ m0 m2). An e.p. defined on ℝ is restricted to [0, ∞) for moments.

**0.3 Imports (ordinary background only).**
* (I1) The functions t^k e^{λt} (distinct pairs (k, λ)) are linearly independent over ℂ on every interval of positive
  length. A nonzero e.p. is an entire function, so its real zeros are isolated and have finite multiplicity.
* (I2) Jordan/spectral form of e^{At}; Cayley–Hamilton; existence and uniqueness for linear constant-coefficient ODE
  initial value problems; companion matrices.
* (I3) Rolle's theorem.
* (I4) Hermite–Genocchi formula, including coincident (confluent) nodes. For ϕ ∈ C²(ℝ) and nodes x1 ≤ x2 ≤ x3,
  ϕ[x1,x2,x3] = ∫_Σ ϕ''(u1x1 + u2x2 + u3x3) du2 du3, where Σ := {(u2,u3) : u2, u3 ≥ 0, u2 + u3 ≤ 1} and
  u1 := 1 − u2 − u3. The (confluent) divided difference ϕ[x1,x2,x3] is a linear combination, with coefficients
  depending only on the nodes, of the values ϕ^{(j)}(x_i), j < multiplicity of x_i.
* (I5) Minkowski's theorem (finite-dimensional Krein–Milman) with Carathéodory: every point of a compact convex set
  in ℝ^n is a finite convex combination of extreme points.
* (I6) Extreme value theorem, intermediate value theorem, Tonelli's theorem.
* (I7) Implicit function theorem (C¹).
* (I8) For ν ∈ ℝ∖{0}, (1/L)∫_0^L e^{iνt} dt → 0 as L → ∞.

---

## 1. L1 — structure of ME(≤3)

**Lemma 1.1 (decay).** If an e.p. G satisfies G(t) → 0 as t → +∞, then every contributing exponent of G has negative
real part.

*Proof.* Let G ≢ 0, σ := max_{λ∈Λ} Re λ, d := max{deg p_λ : Re λ = σ}, Λ* := {λ : Re λ = σ, deg p_λ = d}, and let
c_λ ≠ 0 be the leading coefficient of p_λ. For t ≥ 1, t^{−d} e^{−σt} G(t) = T(t) + ε(t), where
T(t) := Σ_{λ∈Λ*} c_λ e^{i(Im λ)t} and ε(t) → 0. Each remaining term has either a lower polynomial degree or a smaller
real part. The numbers Im λ (λ ∈ Λ*) are distinct, so by (I8)
(1/L)∫_0^L |T|² = Σ|c_λ|² + Σ_{λ≠λ'} c_λ conj(c_{λ'}) (1/L)∫_0^L e^{i(Im λ − Im λ')t} dt → Σ|c_λ|² > 0.
If σ ≥ 0, then |t^{−d} e^{−σt} G(t)| ≤ |G(t)| → 0 for t ≥ 1. This forces T(t) → 0, hence (1/L)∫_0^L |T|² → 0, a
contradiction. So σ < 0. ∎

**Lemma 1.2 (dominant real exponent).** Let f ≢ 0 be a real-valued e.p. with f(t) ≥ 0 for all t ≥ t0. Then
σ := max Re λ over the contributing exponents is itself a contributing exponent (in particular real). Consequently, a
contributing non-real λ forces a contributing real λ0 ≥ Re λ. The case λ0 = Re λ is allowed: it is D1.

*Proof.* Suppose σ ∉ Λ. Define d, Λ*, c_λ, T, ε as in 1.1. Every λ ∈ Λ* is now non-real and Λ* = conj(Λ*), so T is
real-valued. T has no zero frequency, so the mean M(T) := lim (1/L)∫_0^L T is 0. Also M(T²) = Σ_{Λ*} |c_λ|² > 0.
For t ≥ max(t0, 1) we have t^{−d} e^{−σt} f(t) ≥ 0, so T ≥ −ε and T⁻ := max(−T, 0) ≤ |ε| → 0. Hence M(T⁻) = 0. Then
|T| = T + 2T⁻ gives M(|T|) = 0, and T² ≤ ‖T‖_∞ |T| gives M(T²) = 0, a contradiction. ∎

**Theorem L1(a) (structure).** Let X be continuous with an ME representation (α, A) of order n ≤ 3 (HSTZ Def. 1–2):
F(t) = Pr(X < t) = 1 − α e^{At} 𝟙 for t ≥ 0, with α real 1×n and A real n×n. Put G(t) := α e^{At} 𝟙 and
f(t) := −α A e^{At} 𝟙. Then:
1. α𝟙 = 1, and G(t) = Pr(X ≥ t) for t ≥ 0.
2. G is a real e.p. with ord G ≤ n. Its contributing exponents are eigenvalues of A, all with Re < 0.
3. f = −G' is a density of X: f ≥ 0 on [0, ∞), ∫_0^∞ f = 1, E(f) = E(G), ord f ≤ 3, all moments finite.
4. If f has a contributing non-real exponent, then E(f) = {λ0, λ, λ̄} with λ0 real, λ0 ≥ Re λ, all simple.

*Proof.* (1) F(0) = Pr(X < 0) = 0 gives α𝟙 = 1, and G = 1 − F.
(2) By (I2), e^{At} = Σ_{λ∈spec A} e^{λt} Σ_{k<N_λ} (t^k/k!)(A − λ)^k P_λ, where P_λ are the spectral projectors and
N_λ the algebraic multiplicities. So G = Σ e^{λt} q_λ with deg q_λ ≤ N_λ − 1, and dropping the zero q_λ gives
ord G ≤ Σ N_λ = n. G(t) = Pr(X ≥ t) → 0 (X is a.s. finite), so Lemma 1.1 applies.
(3) d/dt e^{At} = A e^{At}, so f = −G'. F = 1 − G is C¹ on [0, ∞) and nondecreasing with F(0) = 0. So
F(t) = ∫_0^t f, f = F' ≥ 0 (one-sided at 0), and ∫_0^∞ f = lim F = 1. Every contributing λ satisfies λ ≠ 0, and
(q e^{λt})' = (q' + λq) e^{λt} with deg(q' + λq) = deg q; hence E(f) = E(G). Moments are finite by exponential decay.
(4) Lemma 1.2 gives a real contributing λ0 ≥ Re λ. λ̄ also contributes because f is real, so ord f ≤ 3 forces
E(f) = {λ0, λ, λ̄} with all multiplicities 1. ∎

**Theorem L1(b) (converse).** Let f be a real e.p. whose contributing exponents all have Re < 0, with ord f = N ≤ 3,
f ≥ 0 on [0, ∞) and ∫_0^∞ f = 1. Then f is the density of a continuous X ∈ ME(N) ⊆ ME(3), with an explicit real
representation of order N, and f = −α A e^{At} 𝟙.

*Proof.* Put G(t) := ∫_t^∞ f. For Re λ < 0, ∫_t^∞ p(s) e^{λs} ds = q(t) e^{λt} with
q = −Σ_{j=0}^{deg p} (−1)^j λ^{−j−1} p^{(j)}, and deg q = deg p. So G is a real e.p. with E(G) = E(f) and G(0) = 1.
Let χ(s) := Π_{λ∈Λ} (s − λ)^{m_λ} with m_λ := deg p_λ + 1. χ is real, monic and of degree N, and χ(D)G = 0. Put
x(t) := (G, G', …, G^{(N−1)})ᵀ. Then x' = Cx with C the companion matrix of χ, so
G(t) = e1ᵀ e^{Ct} x(0) = x(0)ᵀ e^{Cᵀt} e1. Let S := [𝟙, e2, …, eN] (det S = 1, S e1 = 𝟙), A := S Cᵀ S^{−1} and
α := x(0)ᵀ S^{−1}. Then α e^{At} 𝟙 = x(0)ᵀ e^{Cᵀt} S^{−1} 𝟙 = x(0)ᵀ e^{Cᵀt} e1 = G(t). If X has density f, then
Pr(X < t) = 1 − G(t) = 1 − α e^{At} 𝟙 for t ≥ 0, and −α A e^{At} 𝟙 = −G' = f. ∎
*Control:* run `ctl-a-v1` (a4) checks this construction exactly for f = 2e^{−t}(1 − cos t). It gives
A = [[2,0,−2],[7,0,−6],[4,1,−5]] and α = (1,0,0), and verifies α𝟙 = 1, charpoly(A) = (s+1)(s²+2s+2),
αA^k𝟙 = G^{(k)}(0) and −αA^{k+1}𝟙 = f^{(k)}(0) for k = 0, 1, 2. ODE uniqueness then gives αe^{At}𝟙 = G.

**Corollary 1.3.** For ω > 0 and φ ∈ ℝ, e^{−t}(1 − cos(ωt − φ)), normalized, is the density of a continuous
X ∈ ME(3): it has exponents −1 and −1 ± iω, it is ≥ 0, and m0 > 0 because it is continuous, ≥ 0 and ≢ 0. Erlang-3:
α = (1,0,0) and the bidiagonal A = −I + N give f = t²e^{−t}/2 and SCV = 1/3 exactly (`ctl-a-v1` (a1), exact sympy;
E(t) = e^{−t}(I + Nt + N²t²/2) is verified to satisfy E(0) = I and E' = AE).

**Lemma 1.4 (invariance).** SCV(cf) = SCV(f) for c > 0. Also SCV(f(c·)) = SCV(f), because m_k(f(c·)) = c^{−k−1} m_k(f).
The time change t ↦ t/μ sends an exponent λ to λ/μ.

**Normal forms.** By L1(a)(4) and Lemma 1.4, the density of every continuous X ∈ ME(≤3) is of one of two types.
* (R) All contributing exponents are real, and E(f) is a real multiset of size ≤ 3.
* (D) E(f) = {−μ, −μ' ± iν} with μ > 0, ν > 0, μ' ≥ μ. Then g(t) := f(t/μ) has E(g) = {−1, −(1 + δ) ± iω} with
  δ := μ'/μ − 1 ≥ 0 and ω := ν/μ > 0, and SCV(g) = SCV(f). **D1:** δ = 0. **D2:** δ > 0.

---

## 2. L2 — cones, ratio form, mixtures, extreme rays, bookkeeping

**Definitions.** An *admissible* multiset E is a conjugation-closed multiset in {Re < 0} with |E| ≤ 3. V_E is the real
vector space of real e.p. whose exponent multiset is contained in E, together with 0. It has dim V_E = |E|, with basis
t^k e^{λt} (λ real, k < mult λ) and e^{(Re λ)t} cos((Im λ)t), e^{(Re λ)t} sin((Im λ)t) for a non-real pair (whose
multiplicity is 1 when |E| ≤ 3). K_E := {f ∈ V_E : f(t) ≥ 0 ∀ t ≥ 0} and B_E := {f ∈ K_E : ∫_0^∞ f = 1}.
By L1(a)–(b), the densities of continuous ME(≤3) laws are exactly ∪_E B_E over admissible E.

**Lemma 2.1 (cone).** K_E is a closed, convex, pointed cone. ℓ(f) := ∫_0^∞ f and m1(f) are > 0 on K_E∖{0}, and B_E is
compact and convex.

*Proof.* Each evaluation f ↦ f(t) is a linear functional on the finite-dimensional V_E, so K_E is an intersection of
closed half-spaces. If ±f ∈ K_E then f = 0 on [0, ∞), so f = 0 by (I1). For f ∈ K_E∖{0}, f ≥ 0 is continuous and
≢ 0 on [0, ∞) by (I1), so ℓ(f) > 0 and m1(f) > 0. Fix a norm. ℓ is continuous and positive on the compact set
K_E ∩ {‖f‖ = 1}, so ℓ ≥ c > 0 there. Hence B_E ⊆ {‖f‖ ≤ 1/c}, which is closed and bounded. ∎

**Lemma 2.2 (ratio form).** For f as in 0.2, S(f) = min_{θ>0} R_θ(f), where
R_θ(f) := ∫_0^∞ (t − θ)² f / (θ² ∫_0^∞ f). The minimum is attained at θ = m2/m1.

*Proof.* With x := 1/θ > 0, R_θ = 1 − 2(m1/m0)x + (m2/m0)x². This is minimized at x = m1/m2 > 0, with value
1 − m1²/(m0 m2) = S(f). ∎

**Lemma 2.3 (mixtures).** Let ν be a finite positive measure on M with ν(M) > 0, and g : M × [0, ∞) → [0, ∞)
measurable. Assume each g_μ := g(μ, ·) satisfies 0.2 (in particular 0 < ∫ g_μ), ∫_M ∫_0^∞ (1 + t²) g_μ dt dν < ∞,
and SCV(g_μ) ≥ c ≥ 0 for ν-a.e. μ. Then f := ∫_M g_μ dν(μ) satisfies 0.2 and SCV(f) ≥ c. In particular,
SCV(f1 + … + fk) ≥ min_i SCV(f_i) whenever every f_i satisfies 0.2 (positive mass).

*Proof.* x ↦ x/(1 + x) is increasing, so S(g_μ) ≥ c' := c/(1 + c). Fix θ > 0. By 2.2,
∫(t − θ)² g_μ ≥ c' θ² ∫ g_μ for a.e. μ. Integrate over ν (Tonelli) to get ∫(t − θ)² f ≥ c' θ² ∫ f, i.e. R_θ(f) ≥ c'.
f satisfies 0.2: ∫ f = ∫_M (∫ g_μ) dν > 0, because the inner integral is > 0 for every μ and ν(M) > 0; and
∫(1 + t²) f < ∞ by hypothesis and Tonelli. Minimizing over θ gives S(f) ≥ c', i.e. SCV(f) ≥ c. ∎

**Remark 2.3a (every application satisfies 0.2).**
1. Every f ∈ K_E∖{0} is a nonnegative continuous e.p. whose exponents have negative real part. So ∫(1 + t²) f < ∞,
   and ∫ f > 0 by Lemma 2.1 (f ≢ 0 on [0, ∞) by (I1), and f is continuous).
2. The Hermite–Genocchi components g_u(t) = (t − τ)² e^{−μ_u(t−τ)} of Lemma 3.4(5) are continuous and nonnegative,
   and vanish only at t = τ, so 0 < ∫ g_u. Here μ_u ∈ [μ_min, μ_max] := [min λ_i, max λ_i] ⊂ (0, ∞), so
   (1 + t²) g_u(t) ≤ (1 + t²)(t − τ)² e^{μ_max|τ|} e^{−μ_min t} uniformly in u, and ∫_Σ ∫_0^∞ (1 + t²) g_u dt du < ∞.

Hence no application uses the pointwise reading of "nonzero".

**Lemma 2.4 (extreme rays).** Let E be admissible with K_E ≠ {0}.
1. min_{K_E∖0} SCV exists.
2. Every f ∈ K_E∖0 has finitely many f_i on extreme rays of K_E with SCV(f) ≥ min_i SCV(f_i).
3. The minimum in (1) is attained on an extreme ray.

Hence inf_{K_E∖0} SCV = inf over the extreme rays of K_E.

*Proof.* SCV is scale-invariant and continuous on K_E∖0: the m_k are linear on V_E, and m0, m1 > 0 there. So it
attains its minimum on the compact B_E (2.1, I6). Extreme points of B_E lie on extreme rays: if e = x + y with
x, y ∈ K_E∖0, then e = ℓ(x)·x/ℓ(x) + ℓ(y)·y/ℓ(y) with ℓ(x) + ℓ(y) = 1, so x/ℓ(x) = y/ℓ(y) = e. By (I5),
f/ℓ(f) = Σ c_i e_i with e_i extreme in B_E and c_i > 0; apply 2.3. Applying (2) to a minimizer gives (3). ∎

**Lemma 2.5 (bookkeeping; correction of the outline).** If E ⊆ E' (both admissible), then V_E ⊆ V_{E'} and
K_E = K_{E'} ∩ V_E ⊆ K_{E'}. Hence inf_{K_{E'}∖0} SCV ≤ inf_{K_E∖0} SCV. Every real admissible E with |E| ≤ 2 lies in
a real admissible E' with |E'| = 3: add real negative numbers outside E, or repeat one.
**K_E need not be a face of K_{E'}.** Counterexample: E = {−1} and E' = {−1, −2, −3}. Then x := e^{−t} − e^{−3t} and
y := e^{−t} + e^{−3t} lie in K_{E'} (e^{−t} ≥ e^{−3t} on [0, ∞)), and x + y = 2e^{−t} ∈ K_E, but x, y ∉ V_E. Only the
inclusion is used below. K_E *is* a face when E' ∖ E is the asymptotically dominant basis element (Lemma 3.2).

**Corollary 2.6 (assembly).** Define three infima of SCV:
* I_R over K_E∖0 with E real admissible;
* I_1 over the D1 cones K_{{−1, −1±iω}}, ω > 0;
* I_2 over the D2 cones K_{{−1, −(1+δ)±iω}}, δ, ω > 0.

Then inf{SCV(X) : X ∈ ME(≤3) continuous} = min(I_R, I_1, I_2), and each of the three infima is an infimum over the
extreme rays of the respective cones.

*Proof.* A density f lies in B_{E(f)}. E(f) is of type R or D, and SCV is invariant under the time change (normal
forms). Type R with |E(f)| < 3 is padded (2.5). Conversely, every nonzero cone element, normalized, is an ME(≤3)
density (L1(b)). A complex E whose pair is not dominated by the real exponent has K_E = K_{{λ0}} by Lemma 1.2, which is
contained in the real case. Finally apply 2.4. ∎

---

## 3. L3 — real exponents (cases A, B, C)

**Setting.** E is a real admissible multiset with |E| = 3, written with positive *rates*. The basis φ1, φ2, φ3 is
ordered by decreasing dominance at +∞:
* (A) E = {−λ1, −λ2, −λ3}, 0 < λ1 < λ2 < λ3: φ1 = e^{−λ1t}, φ2 = e^{−λ2t}, φ3 = e^{−λ3t}.
* (B1) E = {−λ, −λ, −μ}, 0 < λ < μ: φ1 = t e^{−λt}, φ2 = e^{−λt}, φ3 = e^{−μt}.
* (B2) E = {−λ, −μ, −μ}, 0 < λ < μ: φ1 = e^{−λt}, φ2 = t e^{−μt}, φ3 = e^{−μt}.
* (C) E = {−λ, −λ, −λ}: φ1 = t² e^{−λt}, φ2 = t e^{−λt}, φ3 = e^{−λt}.

For f = a1φ1 + a2φ2 + a3φ3 put a1(f) := a1. Let λ_* be the smallest rate, m_* its multiplicity, and
ψ(t) := (1 + t)^{m_*−1} e^{−λ_* t} > 0. Two facts follow by inspection of each type: (F1) sup_{t≥0} |g|/ψ < ∞ for
every g ∈ V_E; (F2) f(t)/ψ(t) → a1(f) as t → ∞.

**Lemma 3.1 (zero count; Chebyshev property).** Let E be any real multiset of size N ≥ 1. Every nonzero g ∈ V_E has at
most N − 1 real zeros counted with multiplicity.

*Proof.* Induction on N; N = 1 is trivial. Write g = Σ_{i=1}^r p_i(t) e^{κ_i t} with κ_i the distinct elements of E,
multiplicities m_i and deg p_i ≤ m_i − 1 (some p_i may be 0). If at most one p_i ≠ 0, then g = p_i e^{κ_i t} has
≤ m_i − 1 ≤ N − 1 zeros. Otherwise let p_j ≠ 0 for some j ≥ 2. Put h := e^{−κ1 t} g; it has the same zeros with the
same multiplicities. Then h^{(m1)} = Σ_{i≥2} p̃_i e^{(κ_i−κ1)t} with deg p̃_i = deg p_i, because κ_i − κ1 ≠ 0 and
(D + c) preserves degree for c ≠ 0. So h^{(m1)} ≠ 0 lies in a real e.p. space of size N − m1 and, by induction, has
≤ N − m1 − 1 zeros. Rolle with multiplicities (I3) says: if h has zeros x1 < … < xs of multiplicities k_j with
Σ k_j = Z, then h' has a zero of multiplicity ≥ k_j − 1 at each x_j and a zero in each (x_j, x_{j+1}), so ≥ Z − 1
zeros. If h had ≥ N zeros (choose finitely many), h^{(m1)} would have ≥ N − m1 zeros, a contradiction. ∎

**Lemma 3.2 (dominant coefficient; face).** a1(f) ≥ 0 for f ∈ K_E. K' := K_E ∩ {a1 = 0} is an exposed face of K_E.
It is the nonnegative cone of V' := span(φ2, φ3) = V_{E''} for a real multiset E'' of size 2:
* (A) {e^{−λ2t}, e^{−λ3t}};
* (B1) {e^{−λt}, e^{−μt}};
* (B2) {t e^{−μt}, e^{−μt}};
* (C) {t e^{−λt}, e^{−λt}}.

The extreme rays of K_E inside K' are exactly the extreme rays of K'.

*Proof.* By (F2), a1(f) = lim f/ψ ≥ 0. If x + y ∈ K' with x, y ∈ K_E, then a1(x) + a1(y) = 0 with both ≥ 0, so
x, y ∈ K'. An extreme ray of K' is therefore extreme in K_E, and conversely. ∎

**Lemma 3.3 (face rays).**
1. For 0 < κ1 < κ2, a e^{−κ1t} + b e^{−κ2t} ≥ 0 on [0, ∞) iff a ≥ 0 and a + b ≥ 0. The extreme rays are e^{−κ2t} and
   e^{−κ1t} − e^{−κ2t}.
2. For κ > 0, (a + bt) e^{−κt} ≥ 0 on [0, ∞) iff a, b ≥ 0. The extreme rays are e^{−κt} and t e^{−κt}.
3. SCV(e^{−κt}) = 1, SCV(t e^{−κt}) = 1/2, and SCV(e^{−κ1t} − e^{−κ2t}) = (κ1² + κ2²)/(κ1 + κ2)² ∈ [1/2, 1). So every
   face ray has SCV ≥ 1/2.

*Proof.* (1) e^{κ1t} f = a + b x, where x = e^{−(κ2−κ1)t} ranges over (0, 1]. An affine function is ≥ 0 on (0, 1] iff
it is ≥ 0 as x → 0+ and at x = 1. The planar cone {a ≥ 0, a + b ≥ 0} has extreme rays (0, 1) and (1, −1).
(2) t = 0 gives a ≥ 0 and t → ∞ gives b ≥ 0; the converse is clear.
(3) m_k(e^{−κt}) = k!/κ^{k+1}, m_k(t e^{−κt}) = (k+1)!/κ^{k+2} and m_k(e^{−κ1t} − e^{−κ2t}) = k!(κ1^{−k−1} − κ2^{−k−1}).
For the last, m0m2/m1² = 2(κ1² + κ1κ2 + κ2²)/(κ1 + κ2)². Finally 2(κ1² + κ2²) ≥ (κ1 + κ2)². ∎

**Lemma 3.4 (double-zero rays; Hermite–Genocchi).** Let (λ1, λ2, λ3) list the rates of E with multiplicity. For τ ∈ ℝ
define F_τ(t) := (t − τ)² ∫_Σ e^{−(t−τ)(u1λ1 + u2λ2 + u3λ3)} du2 du3. Then:
1. F_τ = ϕ_{t−τ}[λ1, λ2, λ3] with ϕ_s(x) := e^{−sx}, so F_τ ∈ V_E. For type A,
   F_τ(t) = Σ_i e^{−λ_i(t−τ)} / Π_{j≠i}(λ_i − λ_j).
2. F_τ > 0 on ℝ∖{τ}, F_τ(τ) = F_τ'(τ) = 0 and F_τ''(τ) = 1.
3. Every g ∈ V_E with g(τ) = g'(τ) = 0 is a real multiple of F_τ.
4. a1(F_τ) > 0.
5. SCV(F_τ) ≥ Δ3 := inf_{σ∈ℝ} SCV((t − σ)² e^{−t}) for every τ ∈ ℝ.

*Proof.*
1. (I4) with ϕ_s'' = s² e^{−sx}. The divided difference is a node-dependent combination of
   ϕ_s^{(j)}(λ_i) = (−s)^j e^{−sλ_i} with j < mult λ_i. With s = t − τ each such term equals
   e^{λ_iτ} (τ − t)^j e^{−λ_i t} ∈ V_E.
2. F_τ = (t − τ)² k(t), where k := ∫_Σ e^{−(t−τ)⟨u,λ⟩} > 0 is C^∞ and k(τ) = area Σ = 1/2.
3. g ↦ (g(τ), g'(τ)) has kernel W ∋ F_τ with dim W ≥ 1. If dim W ≥ 2, then for any t1 ≠ τ some 0 ≠ g ∈ W has
   g(t1) = 0. That is three zeros counted with multiplicity, contradicting 3.1 (N = 3).
4. If a1(F_τ) = 0, then F_τ would be a nonzero element of the size-2 space V' with a double zero, contradicting 3.1
   (N = 2). So a1(F_τ) ≥ 0 by (F2), and a1(F_τ) ≠ 0.
5. F_τ = ∫_Σ g_u du with g_u(t) := (t − τ)² e^{−μ_u(t−τ)} and μ_u := ⟨u, λ⟩ ∈ [min λ_i, max λ_i] ⊂ (0, ∞). By 1.4
   (t ↦ t/μ_u), SCV(g_u) = SCV((t − μ_uτ)² e^{−t}) ≥ Δ3. The integrability in 2.3 holds because the integrand is
   continuous in u on the compact Σ. ∎

`ctl-a-v1` (a3) checks exactly (sympy) that s²∫_Σ e^{−s⟨u,λ⟩} equals the (confluent) divided difference for the node
triples (1,2,3), (1,1,2), (1,2,2) and (1,1,1), with quotient by s² → 1/2 at s = 0.

**Lemma 3.5 (classification of extreme rays).** Every extreme ray of K_E (E real, |E| = 3) is one of:
* (a) the ray of F_τ for some τ ≥ 0;
* (b) one of the two face rays of 3.3. These are e^{−λ3t} and e^{−λ2t} − e^{−λ3t} (A); e^{−μt} and e^{−λt} − e^{−μt}
  (B1); e^{−μt} and t e^{−μt} (B2); e^{−λt} and t e^{−λt} (C).

Conversely, every F_τ with τ ≥ 0 spans an extreme ray.

*Proof.* Let f ∈ K_E∖0 span an extreme ray. If a1(f) = 0, use 3.2 and 3.3. Let a1(f) > 0. By 3.1, f has ≤ 2 real
zeros counted with multiplicity. Zeros in (0, ∞) have even multiplicity (≥ 2), since f ≥ 0 nearby and f is analytic.
So on [0, ∞) exactly one of the following holds:
* (P0) no zero;
* (P1) only t = 0, with multiplicity 1;
* (P2) only t = 0, with multiplicity 2;
* (P3) only one τ > 0, with multiplicity 2.

* (P0) f/ψ is continuous and positive on [0, ∞), and → a1 > 0 (F2), so f ≥ cψ with c > 0. Every g ∈ V_E has
  |g| ≤ Mψ (F1). Choose g ∉ span f (dim 3). Then f ± (c/M)g ∈ K_E, so f = ½(f + εg) + ½(f − εg) is not extreme.
* (P1) f(0) = 0 < f'(0). Put ψ0 := (t/(1 + t))ψ. f/ψ0 → f'(0) > 0 at 0+ and → a1 > 0 at ∞, and it is positive in
  between, so f ≥ cψ0 with c > 0. Choose g ∉ span f with g(0) = 0 (a 2-dimensional subspace). Then |g| ≤ Mψ0: near 0,
  |g(t)| ≤ t·sup|g'|; near ∞ use (F1). As in (P0), f is not extreme.
* (P2), (P3) f(τ) = f'(τ) = 0 with τ ≥ 0, so f = c F_τ with c > 0 (3.4(3), and F_τ > 0 off τ).

Converse: let F_τ = x + y with x, y ∈ K_E. Then x(τ) = y(τ) = 0. If τ > 0, τ is an interior minimum of x, y ≥ 0, so
x'(τ) = y'(τ) = 0. If τ = 0, then x'(0), y'(0) ≥ 0 and x'(0) + y'(0) = 0, so both vanish. By 3.4(3) x and y are
nonnegative multiples of F_τ. ∎

**Theorem L3.** Every continuous X ∈ ME(≤3) whose density has only real contributing exponents has SCV(X) ≥ Δ3. The
bound is attained: for E = {−1, −1, −1}, F_{x1} = ½ (t − x1)² e^{−(t − x1)} has SCV = Δ3, where x1 ≈ 0.41577 > 0 is
the smallest zero of the Laguerre polynomial L3 (L4). Hence I_R = Δ3.

*Proof.* Pad to |E| = 3 (2.5). Then 2.4, 3.5, 3.4(5) and 3.3(3) give SCV ≥ min(Δ3, 1/2) = Δ3, because
Δ3 ≤ SCV(t² e^{−t}) = 1/3 < 1/2. For type C, F_τ = ½ (t − τ)² e^{−(t−τ)}, so SCV(F_τ) = s(τ), and s(x1) = Δ3 by L4. ∎

---

## 4. L4 — the constant Δ3

Let s(τ) := SCV((t − τ)² e^{−t}), the density taken on [0, ∞).

**Theorem L4.**
1. 1 + s(τ) = P(τ)/Q(τ)², with P := (τ² − 2τ + 2)(2τ² − 12τ + 24) and Q := τ² − 4τ + 6 = (τ − 2)² + 2 > 0.
2. 4(P − (5/4)Q²) = 3(τ² − 4τ + 2)² + 8τ² > 0 for all real τ. Hence s(τ) > 1/4 on ℝ, and Δ3 > 1/4 (the infimum is
   attained by (3)).
3. s'(τ) = 8q(τ)/Q³, with q(τ) := τ³ − 9τ² + 18τ − 6 = −6 L3(τ) (so s' = −48 L3/Q³), where L3(x) = 1 − 3x + 3x²/2 − x³/6
   is the Laguerre polynomial; and s → 1 at ±∞.
   * q has exactly one root in each of (0, 1/2), (2, 3) and (6, 7); call them x1 < x2 < x3 (the zeros of L3).
   * Δ3 = min_ℝ s = s(x1) ∈ (1/4, 1/3).
   * Δ3 = (x1(9 − x1)² − 24)/24 = (x3 − x2)²/(4 x2 x3).

   The last form is the "relative gap of the Laguerre L3 zeros" of Battagliola–Peralta (arXiv:2608.29143); this agrees
   exactly, and is not used as a premise.
4. Δ3 is a root of h(y) := 32y³ − 144y² + 135y − 27, and h is irreducible over ℚ.
   * COMPUTATIONAL (conditional; run `ctl-b-v1`; supplementary, used by no proof): lo = 0.2765825307809456 < Δ3 <
     hi = 0.2765825307809457 (the lower bracket relies on a SymPy Sturm count); the Arb enclosure
     Δ3 = 0.27658253078094566646323160988256346700325763105135079308086826963083 ± 2.41·10⁻⁷¹;
     x1 = 0.41577455678347908331153387312827… and 1/Δ3 = 3.61555734260022193537328283351….
   * EXACT (Lemma 4.2 and its run): Δ3 > 553/2000, and the 18-digit bracket Δ3 = 0.276582530780945666….

*Proof.*
1. m_k = (k+2)! − 2τ(k+1)! + τ² k!, so m0 = τ² − 2τ + 2, m1 = Q and m2 = 2τ² − 12τ + 24.
2. Expansion: both sides equal 3τ⁴ − 24τ³ + 68τ² − 48τ + 12. The sum of squares vanishes only if τ = 0 and
   τ² − 4τ + 2 = 0 simultaneously, which is impossible.
3. d/dτ(P/Q²) = (P'Q − 2PQ')/Q³. Expansion gives P'Q − 2PQ' = (8τ⁵ − 80τ⁴ + 344τ³ − 776τ² + 912τ − 432) −
   (8τ⁵ − 80τ⁴ + 336τ³ − 704τ² + 768τ − 384) = 8q.
   * Root isolation: q(0) = −6, q(1/2) = 7/8, q(2) = 2, q(3) = −6, q(6) = −6 and q(7) = 22. So q has a root in each of
     (0, 1/2), (2, 3) and (6, 7). A cubic has no more roots, so these three roots are all simple, q < 0 on
     (−∞, x1) ∪ (x2, x3), and q > 0 on (x1, x2) ∪ (x3, ∞).
   * Monotonicity: s decreases on (−∞, x1], increases on [x1, x2], decreases on [x2, x3] and increases on [x3, ∞).
     Since deg P = deg Q² = 4 with leading coefficients 2 and 1, s → 1 at ±∞. So min_ℝ s exists and equals
     min(s(x1), s(x3)).
   * Since 0 < x1 and s is strictly decreasing on (−∞, x1], s(x1) < s(0) = 48/36 − 1 = 1/3.
   * For τ ≥ 6, s(τ) − 1/2 = (2P − 3Q²)/(2Q²), with 2P − 3Q² = τ⁴ − 8τ³ + 20τ² − 12 = τ²((τ − 4)² + 4) − 12 ≥
     36·4 − 12 > 0. So s(x3) > 1/2.
   * Thus Δ3 = s(x1) < 1/3, and Δ3 > 1/4 by (2): s > 1/4 pointwise and the minimum is attained.
   * The closed forms: the numerator of s − (x(9 − x)² − 24)/24 has remainder exactly 0 modulo q. Vieta
     (x2 + x3 = 9 − x1, x2x3 = 6/x1) turns (x3 − x2)²/(4x2x3) into ((9 − x1)² − 24/x1)/(24/x1) =
     (x1(9 − x1)² − 24)/24.
4. Since s = (P − Q²)/Q², the polynomial Q⁶·h(s) = 32(P − Q²)³ − 144(P − Q²)²Q² + 135(P − Q²)Q⁴ − 27Q⁶ has
   remainder exactly 0 modulo q. So h(s(x)) = 0 at every root x of q (Q(x) > 0); in particular h(Δ3) = 0.
   Equivalently, h/32 is the resultant in x of q(x) and 24y − x(9 − x)² + 24.
   Irreducibility: a rational root of h has denominator dividing 32, hence prime to 5, so it would give a root of
   h ≡ 2y³ + y² + 3 (mod 5). That polynomial has the values 3, 1, 3, 1, 2 at y = 0, …, 4, so it has no root. ∎

**Lemma 4.2 (exact lower bound; replaces the v1 Sturm certificate).** Δ3 > 553/2000 = 0.2765.

*Proof.* h'(y) = 96y² − 288y + 135 = 96(y − 3/2)² − 81. For y ∈ [1/4, 1/3] we have 3/2 − y ≥ 7/6, so
h'(y) ≥ 96·(7/6)² − 81 = 149/3 > 0; this is h'(1/3), the minimum of h' on the interval. Hence h is strictly increasing
on [1/4, 1/3], and Δ3 ∈ (1/4, 1/3) is its unique root there (L4(3)–(4); consistently, h(1/4) = −7/4 < 0 <
86/27 = h(1/3)). Since 553/2000 ∈ [1/4, 1/3] and h(553/2000) = −1293623/250000000 < 0 = h(Δ3), we get 553/2000 < Δ3. ∎

*EXACT certificate (run `exact-certs-v1`).*
* Checks C2a–C2g and the SymPy cross-checks X_* verify:
  * the moment polynomials and Q = (τ − 2)² + 2;
  * the SOS identity (no common zero);
  * P'Q − 2PQ' = 8q and the six q values;
  * the leading coefficients, s(0) = 1/3, and the identity for 2P − 3Q²;
  * Q⁶h(s) ≡ 0 and s ≡ (x(9 − x)² − 24)/24 modulo q;
  * the h' identity and the bound 149/3;
  * h(1/4), h(1/3) and h(553/2000).
* 60 exact bisection steps on [1/4, 1/3] give the EXACT bracket
  Δ3 ∈ (478316921303906167/1729382256910270464, 1275511790143749779/4611686018427387904), i.e.
  Δ3 = 0.276582530780945666… (18 digits).
* Wrong controls that fail as required:
  * h(2766/10000) = 4277637/3906250000 > 0, so it does not certify Δ3 > 0.2766 (it certifies Δ3 < 0.2766);
  * the point 1/5 lies outside the monotonicity window and is refused.
* h(552/2000) = −142803/3906250 < 0 certifies only the weaker, true bound Δ3 > 0.276, so it is not a failing control.

*Supplementary computation (COMPUTATIONAL, conditional on SymPy/Arb semantics; used by no proof):* run `ctl-b-v1`
(exact sympy + arb, 512 bits), 24/24 checks. Four mutations were each rejected for the intended reason:
* claim s > 0.2766 everywhere: 2 real roots, with the exact witness s(21/50) = 11650027/42120027 < 0.2766;
* SOS coefficient 8 → 7: residual τ²;
* upper bound lo − 10⁻¹⁶: positive at τ0, with a Sturm proof that s exceeds it everywhere;
* wrong root box x2: s(x2) lies outside the bracket.

---

## 5. L5 — common damping D1 and attainment of v_cos

**Setting.** E = {−1, −1 ± iω} with ω > 0 (after the time change). V = span{e^{−t}, e^{−t} cos ωt, e^{−t} sin ωt}.
Put f_{ω,φ}(t) := e^{−t}(1 − cos(ωt − φ)).

**Lemma 5.1 (cone, extreme rays).** K = {e^{−t}(a + b cos ωt + c sin ωt) : a ≥ √(b² + c²)}. Its extreme rays are
exactly the rays of f_{ω,φ}, φ ∈ ℝ mod 2π, with distinct φ giving distinct rays. Hence I_1 = inf_{ω>0, φ} SCV(f_{ω,φ}).

*Proof.* Write R := √(b² + c²) and b cos ωt + c sin ωt = R cos(ωt − χ). If a ≥ R, then f ≥ (a − R)e^{−t} ≥ 0.
Conversely, evaluating at t_k := (χ + π + 2πk)/ω ≥ 0 gives a − R ≥ 0. For extreme rays of {a ≥ |v|}, v ∈ ℝ²: let
(|v|, v) = (a1, v1) + (a2, v2) with a_i ≥ |v_i| and v ≠ 0. Then |v| = a1 + a2 ≥ |v1| + |v2| ≥ |v|, so a_i = |v_i|
and v1, v2 are nonnegative multiples of v. If a > |v|, then
(a, v) = (a − |v|)(1, 0) + (|v|, v) (or, when v = 0, (a/2)(1, e) + (a/2)(1, −e)) is not extreme. Finally
R e^{−t}(1 + cos(ωt − χ)) = R f_{ω, χ+π}. ∎

**Lemma 5.2 (closed form).** m_k(f_{ω,φ}) = k!(1 − Re[e^{−iφ}(1 − iω)^{−(k+1)}]) = k!(1 − ρ^{k+1} cos((k+1)β − φ)),
with ρ := (1 + ω²)^{−1/2} ∈ (0, 1) and β := arctan ω ∈ (0, π/2). In particular m0, m1, m2 > 0.

*Proof.* cos(ωt − φ) = Re e^{i(ωt−φ)}, and ∫_0^∞ t^k e^{−(1−iω)t} dt = k!(1 − iω)^{−(k+1)}; also 1/(1 − iω) = ρe^{iβ}. ∎

**Lemma 5.3 (algebraic form).** Put ψ := φ − 2β, C := cos ψ, S := sin ψ, u := 1 − C ∈ [0, 2], X := ω² + u,
a := ω²(1 + ω²) and Y := ωS, so that Y² = ω²u(2 − u). Then m0 = (X + Y)/(1 + ω²), m1 = X/(1 + ω²),
m2 = 2(X + a − Y)/(1 + ω²)², and
  1 + SCV(f_{ω,φ}) = 2(X + Y)(X + a − Y)/((1 + ω²)X²) = 2(X² + aX + aY − Y²)/((1 + ω²)X²).

*Proof.* e^{−iφ}(1 − iω)^{−(k+1)} = ρ^{k+1} e^{−iψ} e^{i(k−1)β}, with ρe^{iβ} = q(1 + iω), ρe^{−iβ} = q(1 − iω) and
ρ² = q := 1/(1 + ω²). The real parts are q(C − ωS), qC and q²(C + ωS) for k = 0, 1, 2. Then 1 − q(C − ωS) =
(X + Y)q, 1 − qC = Xq and 1 − q²(C + ωS) = ((1 + ω²)² − 1 + u − Y)q² = (X + a − Y)q². ∎
(`ctl-c-v2` c5 checks the identity with arb at 1056 rational sample points; the maximum ball radius of the difference
is 5.3·10⁻⁹², and every ball contains 0.)

**Lemma 5.4 (uniform bound).** For all ω > 0 and φ ∈ ℝ: 1 + SCV(f_{ω,φ}) ≥ (1 + Δ3)/(1 + ω²), i.e.
SCV ≥ (Δ3 − ω²)/(1 + ω²). In particular, for ω ≤ 1/4, SCV ≥ (16Δ3 − 1)/17 > (16·553/2000 − 1)/17 = 428/2125 =
0.2014117… > 0.2014 (by Lemma 4.2; EXACT).

*Proof.*
1. Put Y_m := ω√(u(2 − u)) ≥ 0. Then Y² = Y_m² and Y ≥ −Y_m, so with a > 0,
   X² + aX + aY − Y² ≥ X² + aX − aY_m − Y_m².
2. Write u = ω²v with v ∈ [0, 2/ω²]. Then X = ω²(1 + v), a = ω²(1 + ω²), Y_m = ω²√(v(2 − ω²v)), and the right side of
   step 1 equals ω⁴ N(ω, v), where
   N(ω, v) := (1 + v)² + (1 + ω²)(1 + v − √(v(2 − ω²v))) − v(2 − ω²v).
3. 0 ≤ v(2 − ω²v) ≤ 2v and √(2v) ≤ 1 + v, so 1 + v − √(v(2 − ω²v)) ≥ 1 + v − √(2v) ≥ 0. Hence
   N(ω, v) ≥ N0(v) := (1 + v)² + 1 + v − √(2v) − 2v.
4. Let σ := √(2v). Then 2N0/(1 + v)² = 2(σ⁴ + 2σ² − 4σ + 8)/(σ² + 2)² = P(2 − σ)/Q(2 − σ)² = 1 + s(2 − σ) ≥ 1 + Δ3.
   This uses P(2 − σ) = (σ² − 2σ + 2)·2(σ² + 2σ + 4) = 2(σ⁴ + 2σ² − 4σ + 8) and Q(2 − σ) = σ² + 2.
5. So 1 + SCV ≥ 2ω⁴N/((1 + ω²)ω⁴(1 + v)²) ≥ (1 + Δ3)/(1 + ω²). The bound (Δ3 − ω²)/(1 + ω²) decreases in ω. ∎

The bound is sharp as ω → 0 (EXPLORATORY `ctl-c-v2` c5: at ω = 10⁻², min_φ SCV ≈ 0.276563 against the bound
0.276455). It also holds with certified margin at all 1056 arb sample points (minimum gap 0.0446 at ω = 1/5).

**Lemma 5.5 (large ω).** For all ω > 0 and φ: 1 + SCV ≥ 2(1 − ρ)(1 − ρ³)/(1 + ρ²)², and the right side decreases in
ρ ∈ [0, 1). For ω ≥ 4: ρ ≤ 17^{−1/2} < ρ̄ := 0.2426, since ρ̄² = 0.05885476 > 1/17. Hence
SCV ≥ 2(1 − ρ̄)(1 − ρ̄³)/(1 + ρ̄²)² − 1 = 232498770764161/700733376734161 = 0.33179… > 0.33 (EXACT; ρ̄² = 1471369/25000000;
re-checked in `exact-certs-v1`, C1).

*Proof.* From 5.2: m0 ≥ 1 − ρ > 0, m1 ≤ 1 + ρ² and m2 ≥ 2(1 − ρ³) > 0. The numerator factors are positive and
decreasing in ρ, and the denominator is increasing. ∎

**Theorem 5.6 (attainment; exact upper separation).** Let φ_e ∈ (0, π/2) be the angle with cos φ_e = 35/37 and
sin φ_e = 12/37; it exists since 35² + 12² = 37². Then (EXACT) f_{1,φ_e} has moments
  (m0, m1, m2) = (27/74, 62/74, 171/74),  SCV(f_{1,φ_e}) = 773/3844 = 0.20109261…,
so **v_cos ≤ 773/3844 < 1007/5000 = 0.2014 < 11/50 = T**, and 773/3844 < 553/2000 < Δ3. Moreover v_cos is attained,
every minimizer has 1/4 < ω* < 4, and every (ω, φ) with ω ≤ 1/4 or ω ≥ 4 has SCV > 0.2014.

*Proof.*
* Moments, by Lemma 5.2 with ω = 1: (1 − i)^{−1} = (1 + i)/2, (1 − i)^{−2} = i/2, (1 − i)^{−3} = (−1 + i)/4, and
  e^{−iφ_e} = (35 − 12i)/37. The real parts of the three products are 47/74, 12/74 and −23/148. So m0 = 1 − 47/74 =
  27/74, m1 = 1 − 12/74 = 62/74 and m2 = 2(1 + 23/148) = 171/74, and SCV = 27·171/62² − 1 = 4617/3844 − 1 = 773/3844.
* Comparisons: 773·5000 = 3865000 < 3870908 = 1007·3844, and 1007/5000 < 11/50.
* Attainment: SCV is continuous on (0, ∞) × ℝ (5.2, m1 > 0) and 2π-periodic in φ. So its minimum m* over the
  compact set [1/4, 4] × [0, 2π] is attained, and m* ≤ SCV(1, φ_e) = 773/3844.
* Tails: by Lemma 5.4 with Lemma 4.2, every point with ω ≤ 1/4 has SCV ≥ 428/2125 > 773/3844 (773·2125 = 1642625 <
  1645232 = 428·3844). By Lemma 5.5, every point with ω ≥ 4 has SCV > 0.33 > 773/3844.
* Hence m* = v_cos, it is attained, and every minimizer has 1/4 < ω* < 4. ∎

*EXACT certificate (run `exact-certs-v1`, checks C1_*).*
* Verified: the Pythagorean identity; the moments from Lemma 5.2; the same moments independently from Lemma 5.3's
  algebraic form and from exact SymPy integration of ∫_0^∞ t^k e^{−t}(1 − (35/37) cos t − (12/37) sin t) dt;
  SCV = 773/3844; and every comparison above.
* Wrong controls that fail as required: swapped (cos, sin) = (12/37, 35/37) gives SCV = 206/169; the phase-sign
  mutation e^{+iφ} gives 2549/7396; and (35/37, 13/37) violates c² + s² = 1.

Hence the definition "v_cos := min" in the contract is well posed.

*Supplementary (COMPUTATIONAL, conditional on python-flint Arb/Acb semantics; used by no proof).* At the rational
point ω_U = 517966477543/500000000000, φ_U = 674076484769/2000000000000, the Arb ball (`ctl-c-v2` c3, prec 320) is
SCV ∈ 0.200901563500556958801380682455159321656863180 ± 2.1·10⁻⁴⁶. So v_cos < U := 0.2009015635005569588013806824561593216569.

**Numerical value (EXPLORATORY, `ctl-c-v2` c1; Newton at 80 digits from the parent point, Hessian positive definite
with eigenvalues 0.26860 and 1.29634).** The stationary point is:
* ω* = 1.0359329550858567909065869278226347339723…
* φ* = 0.3370382423844937614264527712363442589648…
* v_cos = 0.200901563500556958801380678959513327689390751533559694715965
* 1/v_cos = 4.977562058630906090494547025747273…

Sign check: at the stationary point ψ* = −1.26905…, S = sin ψ* < 0, which is the minimizing sign of Lemma 5.4's
proof. Global minimality of this stationary point is not certified here. What is proved is attainment and
v_cos ≤ 773/3844 (EXACT); v_cos < U is conditional. A float grid (1501 × 2400 points on [1/4, 4] × [0, 2π)) shows no
other basin within 10⁻⁴ of the minimum.

**Contract band (EXPLORATORY; relabelled in v2).**
* What it is: the check `c1_v_cos_in_contract_band_[0.20090144,0.20090185]` of `ctl-c-v2` (code
  `ctl_c_vcos_v2.py` LF102–103; output `ctl_c.json` LF122–125) compares the *Newton stationary value* with the band.
* Why it is not a certificate: a stationary value is not known to be the global minimum, so the check cannot
  establish the lower band endpoint. The code docstring (LF10–15) wrongly lists the band check under CERTIFIED.
* Actual stop behaviour: if the value were outside the band, LF126–127 only print "STOP: …" and the script continues.
  The failure would reach the exit code only through `all_pass` (exit 1).
* What is certified about the band:
  * the upper endpoint, conditionally, via U < 0.20090185 (Arb, supplementary);
  * the lower endpoint only via the optional Theorem 5.8 (COMPUTATIONAL, conditional);
  * the exact upper bound 773/3844 = 0.20109… lies above the band, so it certifies neither endpoint.
* The theorem needs neither endpoint.

**Corollary 5.7.** Every continuous X ∈ ME(≤3) of type D1 has SCV(X) ≥ v_cos, with equality for f_{ω*,φ*}, so
I_1 = v_cos. Every type-R law has SCV ≥ Δ3 > 553/2000 > 1007/5000 > 773/3844 ≥ v_cos (all EXACT: Lemma 4.2 and
Theorem 5.6).

**Convention control (`ctl-d-v1`, arb, 12/12 checks).** The literal reading of HSTZ eq. (4) with the Table 2 numbers,
e^{−t} cos²(1.03593t − 0.337037), has SCV = 1.5757069924266101935 ± 4·10⁻²⁰. That is inconsistent with Table 1
(cv = 0.20090), so the reading is rejected as a convention error. The reading e^{−t}(1 − cos(1.03593t − 0.337037))
gives SCV = 0.20090156350197712143 ± 4·10⁻²¹ (1/SCV = 4.97756205859572), equal to v_cos + 1.4·10⁻¹² because the table
values are rounded. The identity 1 − cos x = 2 cos²(x/2 − π/2) means the cos² form with half frequency ω/2 and phase
φ/2 + π/2 is the same family; arb gives the identical SCV ball and moments in ratio exactly 1/2. Independent mpmath
quadrature agrees to 25 digits.

**Theorem 5.8 (OPTIONAL; COMPUTATIONAL, conditional; used by no proof).** 0.20090156350055 ≤ v_cos. The method and
proof are in `vcos-lower-bound-v1.md` (unchanged).

**Independent certification (parent primal desk).**
* Record: `institute/runs/six-lane-2026-10-16/review/me3-parent-primal-reductions-v1/RESULT-v1.json`, sha256
  9a72e3e7133de30301785af96604b31838b9726d94055717291f3111744c65e3; re-hashed by this worker, 2026-10-18 06:10 PDT.
* It records run `d1b-lower-worker-L` as "CERTIFIED v_cos >= 0.20090156350055 (OPTIONAL)", with RESULT.json sha256
  aac0149d…395f, and run `d1a-lower-band` as "CERTIFIED v_cos >= 0.20090144 (OPTIONAL)".
* Its own stated limitation: the D1 decimal lower certificate reuses the parent primal evaluator at r = 0.

**Decision after the v2 audit (review item 1): KEEP as optional and conditional.** The result is conditional on
python-flint 0.9.0 Arb/Acb outward rounding and comparison semantics, and on SymPy `simplify` returning 0 for the
gradient identities of `ctl-f-gradsym-v1`. The acceptance logic of the pinned program `code/ctl_f_d1bnb_v1.py`
(sha256 508b1488…41b7) was audited statically and against the library (run `audit-bnb-v2`, 27/27 checks):
* **Completion is an EMPTY unresolved stack, not a count.** The only success flag is
  `certified = bool(middle_certified and tails_ok)` (LF166), with
  `middle_certified = (not aborted) and (refuted is None) and not stack` (LF165).
* **No box leaves the stack uncertified.** Every `continue` in the loop is guarded by a certain ball comparison:
  `F_ball(W, U) > La` (LF135) or `(Fc − err) > La` (LF149, tried only when 0 < u_lo and u_hi < 2, LF146). Every other
  box is either bisected into both exact halves (LF156–163) or ends the loop with `aborted = True` (box cap LF129–131,
  depth cap LF152–155) or a refutation (LF143–145).
* **A cap, limit or indeterminate evaluation can never be reported as success.**
  * Aborted runs and refutations make `middle_certified` false.
  * python-flint comparisons are True only when certain. Undecided, NaN and infinite comparisons return False
    (audit C1). So an indeterminate enclosure is split, never certified: the full middle box gives F_ball = NaN
    (audit C4), and a gradient ball touching u = 0 gives NaN (audit C6).
  * Demonstrated by `ctl-f-mut-cap-v1`: box cap 1000, then aborted with 6 boxes left on the stack, outcome reject.
    The earlier mutations also reject: a refuted L, and a failed tail.
* **The tails are exact** (LF55–57). The tail input Δ3 > 2765/10000 is now also the EXACT Lemma 4.2.
* **Run evidence.** `ctl-f-main-v1` has aborted = false, refutation = null, remaining_stack = 0 and tails OK. Its
  processed-box count is 38439 = 2·19220 − 1, consistent with a complete binary tree with 19220 certified leaves.
* `audit-bnb-v1` (exit 1) is kept as a failed attempt. It wrongly expected a finite enclosure on the full middle box,
  an audit-expectation error; v2 checks the property that matters, namely that the box is not certified.

Pinned files are listed in `../STATUS-v2.md` §3.

---

## 6. L6 — the D2 cone (real pole strictly dominant)

**Setting.** E = {−1, −(1 + δ) ± iω} with δ > 0, ω > 0, and r := δ/ω. Elements of V are e^{−t}H with
H(t) = a + e^{−δt}(b cos ωt + c sin ωt). For τ ∈ ℝ put
  h_τ(t) := 1 − e^{−δ(t−τ)}(cos ω(t − τ) + r sin ω(t − τ)),  g_r(u) := e^{ru}(cos u − r sin u).

**Lemma 6.1.** a > 0 for every f = e^{−t}H ∈ K∖0.
*Proof.* H → a as t → ∞, so a ≥ 0. If a = 0, then e^{−δt}R cos(ωt − χ) ≥ 0 on [0, ∞), which forces R = 0 and f = 0. ∎

**Lemma 6.2 (double zero ⇒ unique ray).** h_τ ∈ span{1, e^{−δt} cos ωt, e^{−δt} sin ωt}, and
h_τ'(t) = ((ω² + δ²)/ω) e^{−δ(t−τ)} sin ω(t − τ), so h_τ(τ) = h_τ'(τ) = 0. The set {g ∈ V : g(τ) = g'(τ) = 0} is
the line spanned by e^{−t}h_τ.
*Proof.* Write g = e^{−t}G; then g(τ) = g'(τ) = 0 iff G(τ) = G'(τ) = 0.
G' = e^{−δt}[(−δb + ωc) cos ωt + (−ωb − δc) sin ωt]. The map (b, c) ↦ (−δb + ωc, −ωb − δc) has determinant
δ² + ω² > 0, so G'(τ) = 0 is one nontrivial linear condition on (b, c), and G(τ) = 0 then fixes a. The formula for
h_τ' and the span membership are direct computations (`ctl-e-v1` e0, exact sympy). ∎

**Lemma 6.3 (extreme rays).** The extreme rays of K are exactly the rays of e^{−t}h_τ for the *feasible* τ ≥ 0, i.e.
those with h_τ ≥ 0 on [0, ∞).
*Proof.* Let f = e^{−t}H ∈ K∖0, so a > 0. The following cases are exhaustive.
* (a) H > 0 on [0, ∞). Since H → a > 0, inf H > 0, while |G| ≤ M for every g = e^{−t}G ∈ V. So f ± εg ∈ K and f is
  interior, not extreme.
* (b) H(0) = 0, H'(0) > 0 and H > 0 on (0, ∞). Then H ≥ c·t/(1 + t) with c > 0. Choose g ∉ span f with G(0) = 0;
  then |G| ≤ M t/(1 + t). So f is not extreme. *This is the outline's "boundary τ = 0 needs h'(0) = 0".*
* (c) H(0) = H'(0) = 0. Then f is a positive multiple of e^{−t}h_0 (6.2).
* (d) H(τ) = 0 for some τ > 0. Then H'(τ) = 0 (interior minimum), so f is a positive multiple of e^{−t}h_τ.

H(0) = 0 forces H'(0) ≥ 0. In (c) and (d), extremality follows exactly as in 3.5: if f = x + y with x, y ∈ K, then
x and y vanish to second order at τ, and 6.2 applies. ∎

**Lemma 6.4 (feasibility).** h_τ(0) = 1 − g_r(ωτ). For τ ≥ 0: τ is feasible iff φ := ωτ ∈ [0, θ1(r)], where θ1(r)
is the unique solution in (π, 2π) of g_r(u) = 1. Equivalently, for τ < 2π/ω, feasibility ⟺ h_τ(0) ≥ 0.
*Proof.* First, h_τ(0) = 1 − e^{δτ}(cos ωτ − r sin ωτ) = 1 − g_r(φ), since δτ = rφ.
g_r'(u) = −(1 + r²) e^{ru} sin u. So g_r decreases strictly on [0, π] and increases strictly on [π, 2π], with
g_r(0) = 1, g_r(π) = −e^{rπ} and g_r(2π) = e^{2πr} > 1. Hence θ1 exists and is unique, g_r < 1 on (0, θ1) and g_r > 1
on (θ1, 2π].

Put s := t − τ. By 6.2, h_τ' has the sign of sin ωs.
* On s ≥ 0, the local minima of h_τ are at s = 2πk/ω, with values 1 − e^{−2πkδ/ω} ≥ 0. So h_τ ≥ 0 on [τ, ∞).
* If τ ≥ 2π/ω, then t = τ − 2π/ω ≥ 0 gives h_τ = 1 − e^{2πr} < 0: infeasible (and φ ≥ 2π > θ1).
* If τ < 2π/ω: on s ∈ (−π/ω, 0), h_τ decreases to h_τ(τ) = 0, so h_τ > 0 there. On s ∈ (−2π/ω, −π/ω], h_τ is
  nondecreasing. Hence φ ≤ π is feasible, and for φ ∈ (π, 2π) the minimum over [0, τ) is h_τ(0): feasible ⟺
  g_r(φ) ≤ 1 ⟺ φ ≤ θ1. ∎

**Lemma 6.5 (θ1).** θ1 : (0, ∞) → (π, 2π) is C¹ and strictly decreasing, with θ1(0+) = 2π and θ1(∞) = π.
*Proof.* At the root, ∂_u g_r = −(1 + r²)e^{ru} sin u > 0 and ∂_r g_r = u g_r − e^{ru} sin u = u − e^{ru} sin u > 0,
because g_r = 1 there and sin u < 0 on (π, 2π). By (I7), θ1' = −∂_r g/∂_u g < 0. Fix u ∈ (π, 2π).
* As r → 0+, g_r(u) → cos u < 1, so θ1(r) > u for small r. Hence θ1 → 2π.
* g_r(u) = e^{ru}(cos u + r|sin u|) → ∞ as r → ∞, so θ1(r) < u for large r. Hence θ1 → π. ∎

*Certified samples (`ctl-e-v1` e1, arb 256 bits, bisection width 2.4·10⁻³³; the signs of g_r − 1 are certified at the
rational endpoints).*

| r | θ1(r) | 2π − θ1 | θ1 − π |
|---|---|---|---|
| 10⁻⁵ | 6.27197544171877006440 | 0.0112099 | |
| 10⁻³ | 6.17119870886673768129 | 0.111987 | |
| 10⁻² | 5.93199833544080813409 | | |
| 0.1 | 5.24260899869797037610 | | |
| 0.3 | 4.65987805685937520612 | | |
| 1 | 3.94073313569291492508 | | |
| 3 | 3.46335292772992627540 | | |
| 10 | 3.24126130608095609995 | | |
| 100 | 3.15159232027645847667 | | 0.00999967 |

The values are strictly decreasing (certified), and ∂_r g, ∂_u g > 0 hold on every enclosure.

**Lemma 6.6 (moments).** For φ = ωτ: m_k(e^{−t}h_τ) = k!(1 − Re[c ζ^{k+1}]), with c := (1 − ir)e^{(r−i)φ} and
ζ := 1/(1 + δ − iω) = 1/(1 + rω − iω). δ = 0 recovers Lemma 5.2.
*Proof.* h_τ(t) = 1 − Re[(1 − ir)e^{(δ−iω)τ}e^{(−δ+iω)t}], ∫_0^∞ t^k e^{−(1+δ−iω)t} dt = k!ζ^{k+1}, and
e^{(δ−iω)τ} = e^{(r−i)φ}. ∎
(`ctl-e-v1` e4: the arb closed form and 40-digit quadrature agree to 4.6·10⁻⁴¹ on a feasible ray.)

**Remark 6.7 (geometry; not used).** K ∩ {a = 1} is the set {v : ⟨−v, z⟩ ≤ 1 ∀ z ∈ Z̄}, where
Z̄ := {e^{−δt}(cos ωt, sin ωt) : t ≥ 0} ∪ {0}. This is minus the polar of conv(Z̄); K is the epigraph cone of the
support function. ∂conv(Z̄) consists of the spiral arc t ∈ [0, τ1], τ1 := θ1(r)/ω, followed by the segment from z(τ1)
back to z(0). The double zero at τ is the touching point of the supporting line, i.e. the maximizer of ⟨−v, z(t)⟩.
Supporting lines through the corner z(0) that are not tangent to either edge give the non-extreme case (b).

**Controls (`ctl-e-v1`, 24/24).**
* Infeasible rays are detected as negative somewhere:
  * at r = 3/10, ω = 1, φ = θ1 + 1/100: h(0) = −0.0441279542429187 ± 1.3·10⁻¹⁷;
  * at τ = 2π + 1/10: h(1/10) = 1 − e^{0.6π} = −5.58606196269472;
  * at r = 1, ω = 2, φ = θ1(1) + 10⁻³: h(0) = −0.07384.
* Feasible ray at φ = θ1 − 1/100: h(0) = 0.0439727 > 0, and h > 0 is certified at every grid point j/64,
  j = 0…2560 (t ∈ [0, 40]). The minimum, 2.21·10⁻⁵, is at t = 298/64, next to the double zero τ ≈ 4.65. The
  all-t statement is Lemma 6.4, not the grid.
* The phases φ ∈ {0, 1.57, 3, 4} at r = 0.3 give h(0) = 0 (exact; the double zero at 0) or h(0) > 0.
* Mutations: the enclosure shifted by +1/100 is rejected (g(lo') − 1 = +0.0441 > 0), and the claim "θ1 + 1/100 is
  feasible" is rejected (h(0) < 0).

---

## 7. What these lemmas reduce the problem to (for the integration owner)

**Corollary 7.1 (exact reduction).** Put
  S_2(r, ω, φ) := SCV(e^{−t}h_{φ/ω}) with δ = rω, computed by Lemma 6.6,
  I_2 := inf{S_2(r, ω, φ) : r > 0, ω > 0, 0 ≤ φ ≤ θ1(r)}.
Then:
1. inf{SCV(X) : X ∈ ME(≤3) continuous} = min(Δ3, v_cos, I_2) = min(v_cos, I_2).
2. **I_2 ≤ v_cos.** Hence the infimum over ME(≤3) equals I_2.
3. The conjecture "SCV ≥ v_cos on ME(≤3)" is equivalent to I_2 ≥ v_cos, i.e. to I_2 = v_cos.

*Proof.* (1) is 2.6, 3.5, L3, 5.1, 6.3 and 6.4, with Δ3 > 553/2000 > 773/3844 ≥ v_cos (Lemma 4.2 and Theorem 5.6;
EXACT). For (2), take a D1 minimizer
(ω*, φ*) with φ* reduced to [0, 2π). By 6.5, θ1(r) > φ* for all small r > 0, so (r, ω*, φ*) is feasible. The moments
of 6.6 are continuous in r at r = 0 with value 5.2, so S_2(r, ω*, φ*) → v_cos. ∎

**Status of the parts.** L1–L6 are proved above in full: written proofs, in which every number on the proof path is
EXACT and re-checked by `exact-certs-v1`. The D2 lower bound I_2 ≥ v_cos is *not* addressed here.

**Constants for the D2 work:**
* EXACT:
  * Δ3 > 553/2000, and Δ3 ∈ (478316921303906167/1729382256910270464, 1275511790143749779/4611686018427387904), i.e.
    0.276582530780945666…;
  * v_cos ≤ 773/3844 < 1007/5000 < 11/50 = T.
* EXACT (written lemmas):
  * the D1 uniform bound 1 + SCV ≥ (1 + Δ3)/(1 + ω²);
  * the D1 tails: SCV ≥ 428/2125 > 0.2014 for ω ≤ 1/4, and SCV > 0.33 for ω ≥ 4.
* COMPUTATIONAL (conditional):
  * v_cos < U = 0.20090156350055695880138068245616 (Arb, `ctl-c-v2`);
  * the θ1 table (Arb, `ctl-e-v1`; informational);
  * the optional lower bound v_cos ≥ 0.20090156350055 (Theorem 5.8, `ctl-f-main-v1`).

**What the theorem uses.** It uses only the written lemmas and the EXACT facts above. In particular it uses neither U
nor the optional lower bound (Theorem 5.8).
