# Parent derivation: sharp PH order for the three-pole family (Commault–Mocanu 2003, Conjecture 1)

Written by the parent on 2026-10-18 around 01:10 PDT, independently of MathPhaseType3's text, which had not been delivered. **This is a parent verification route, not a verdict.** Acceptance still requires the worker's written proof, both CLI-family hostile reviews and the post-result priority check required by the [contract](../screening/math-1-phase-type-complex3-contract.json).

**Source.** The pinned PDF (`screening/phase-type-complex3-intake-v1/commault-mocanu-2003.pdf`, sha `8db1e4aa…0cfb`), read through the parent's text extraction:
- Theorem 6 (Dmitriev–Dynkin; O'Cinneide), printed p.575;
- §2 irreducibility, p.568;
- Proposition 1, Lemma 1 and Theorem 4, pp.570–571;
- Eq. 42, Theorem 14 and Conjecture 1, p.577.

## Statement

Let a>c>0 and b>0, put δ=a−c and β=b/δ, and let

    F(s) = c(a²+b²) / ((s+c)((s+a)²+b²)),
    n* = min{n≥3 : β ≤ cot(π/n)}.

**Claim.** The minimal order of a PH representation of F is n*.

## 1. Lower bound (imported)

1. Take any PH representation (α,T) of order n. Discard every state that does not lie on a path from the initial vertex to the absorbing vertex. This does not change the distribution (CM2003 §2, p.568). The result is an irreducible representation (α′,T′) of order n′≤n.
2. In the realization (T′,α′,−T′1), the poles of F are eigenvalues of T′, in particular −a±ib.
3. Proposition 1 (an irreducible positive realization) makes the eigenvalue of T′ with maximal real part equal to the pole of F with maximal real part, which is −c.
4. Theorem 6 then gives b/(a−c) ≤ cot(π/n′), hence n ≥ n′ ≥ n*.
5. **Review point.** Proposition 1 is proved in CM2003 by reference to Anderson et al. 1996 (discrete time, "the same arguments"). The worker's proof should state this import exactly, or supply the elementary Perron-mode argument: in an irreducible PH representation every state is reached with positive probability and is transient, so the tail of F decays at the slowest communicating class's rate.

## 2. Upper bound, n* = 3

Theorem 14 (Commault–Chemla 1996): order 3 exists iff b ≤ (a−c)/√3. This is imported.

## 3. Upper bound, n = n* ≥ 4 (explicit construction)

Normalize: A=a/δ, C=c/δ=A−1>0, x=s/δ+A, and D(x)=(x−1)(x²+β²). Then F = Kδ³/(δ³D(x)) with K=C(A²+β²), so the target transfer function is K/D(x).

**Angles.**
- Put φ=arctan β and ψ=π−2φ. Since n≥4, φ>π/6.
- The definition of n* is equivalent to 2π/n ≤ ψ < 2π/(n−1).
- Let S=2π−(n−3)ψ. Then 2ψ < S ≤ 3ψ.
- Let G(t)=sin(t+φ)·sin²((S−t)/2+φ) − sin³φ on [0,S/3].
  - **G(0)<0.** We have S/2+φ ∈ (π−φ, 3π/2−2φ], and 3π/2−2φ < π+φ because φ>π/6. So sin²(S/2+φ) < sin²φ.
  - **G(S/3)≥0.** S/3+φ ∈ (φ, π−φ] because 0 < S/3 ≤ ψ. Equality holds iff S=3ψ, i.e. β=cot(π/n).
- The intermediate value theorem gives t* ∈ (0,S/3] with G(t*)=0.
- Set θ₁=t*, θ₂=θ₃=(S−t*)/2 and θ₄=…=θₙ=ψ.
  - Their sum is 2π.
  - Every θᵢ lies in (0, π−φ). This uses ψ<π−φ, and S/2 ≤ π−φ ⇔ ψ ≥ π/(n−2), which follows from ψ ≥ 2π/n with n≥4.
  - ∏ sin(θᵢ+φ) = sin³φ·sin^{n−3}φ = sinⁿφ, because sin(ψ+φ) = sin φ.

**Diagonal and closing weight.**
- Set mᵢ = −β cot θᵢ. Then 1−mᵢ = sin(θᵢ+φ)/(sin θᵢ cos φ) > 0.
- Let W = ∏(1−mᵢ) = βⁿ/∏ sin θᵢ > 0.
- Also iβ−mᵢ = β e^{iθᵢ}/sin θᵢ, so ∏(iβ−mᵢ) = βⁿ e^{2πi}/∏ sin θᵢ = W.
- Hence Q(x)=∏(x−mᵢ) satisfies Q(1) = Q(±iβ) = W.
- Therefore q = Q−W = D·P with P real and monic of degree n−3.

**Cycle matrix.**
- M has diagonal mᵢ, superdiagonal 1 and corner M_{n1}=W.
- Its characteristic polynomial is q. The n-cycle term is sign(σ)·(−1)^{n−1}(−W) = −W.
- u₁=1, u_{i+1}=(1−mᵢ)uᵢ is positive with Mu=u. Since M is irreducible Metzler, its spectral abscissa is 1.
- T₀ = δ(M−AI) is Metzler, irreducible and Hurwitz, with spectral abscissa δ(1−A) = −c.

**Transfer function.**
- From r(xI−M) = e₁ we get rⱼ = ∏_{k>j}(x−m_k)/q(x).
- Take exits t=(0,0,t₃,…,tₙ) and put z=x−m* with m*=(1−β²)/2 = −β cot ψ = m₄=…=mₙ. Then e₁(xI−M)⁻¹t = Σ_{j≥3} tⱼ z^{n−j}/q.
- We need Σ_{j≥3} tⱼ z^{n−j} = K·P.
- P·D = (x−m₁)(x−m₂)(x−m₃)z^{n−3} − W, and D(m*) = −ρ³ ≠ 0 with ρ=(1+β²)/2. So P ≡ W·h (mod z^{n−3}), where h = 1/((1−x)(x²+β²)) expanded at m*.
- Set t₃=K and tⱼ = K·W·h_{n−j} for j≥4, where h_k is the z^k coefficient.

**Positivity.**
- Here m* = −ρ cos ψ and m*²+β² = ρ². So h(m*+z) = ρ⁻³ / ((1−u)(1−2u cos ψ+u²)) with u=z/ρ.
- The Chebyshev partial sums give

      h_k = ρ^{−3−k}·[cos(ψ/2) − cos((k+3/2)ψ)] / (2 sin(ψ/2) sin ψ).

- This is positive for 0≤k≤n−4: we have ψ/2 < (k+3/2)ψ ≤ (n−5/2)ψ < 2π−ψ/2 because (n−2)ψ < 2π, and ψ ∈ (0,2π/3).

**PH normalization.**
- (e₁, T₀, δt) is a positive realization of F. Indeed sI−T₀ = δ(xI−M), and Kδ³/((s+c)((s+a)²+b²)) = F(s).
- It is irreducible: the cycle reaches every state, and state 3 exits since t₃>0.
- CM2003 Theorem 4 / Lemma 1, or directly v = −T₀⁻¹δt > 0, then T = diag(v)⁻¹T₀diag(v), exit = −T1 ≥ 0, α = v₁e₁ = e₁ (since v₁ = F(0) = 1), gives an order-n PH representation.

**Conclusion.** Together with §1 and §2, the minimal order is n* for all a>c>0, b>0. ∎

## Parent finite smoke (aid only, not a premise)

[`phase-type-complex3-parent-smoke-v1/`](phase-type-complex3-parent-smoke-v1/RESULT.v2.json): mpmath at 60 digits, executed in-process from hash-pinned scripts.
- **v1** (`071b6e14…8f1e`, result `da0378af…d670`) passed 133/138 cases. All five failures were exact upper-endpoint cases n=6,9,10,11,12, where G(S/3) evaluated to about −1e−61 because of rounding; the exact value is 0. This was a harness defect, and v1 is retained.
- **v2** (`2dd7bc2a…1c58`, result `cff3a8dc…c575`) passes **138/138**:
  - n*=4..30, with exact upper endpoints and near-lower endpoints for n=4..12 plus 120 seeded random cases;
  - every case has transfer relative error ≤ 7e−60, a Hurwitz dominant eigenvalue equal to −c (checked for n≤22), Metzler off-diagonals, nonnegative exits up to rounding, and α=e₁;
  - all 5 controls pass: the n*−1 construction is not applicable, a perturbed exit breaks the transfer function, a wrong m* breaks it, and the order-3 regime is not used.


## Dated addendum — 2026-10-18T00:56:28-07:00

The opening line's "around 01:10 PDT" was a guessed label. The host clock (file mtime) shows this note was written at **2026-10-18T00:55:05-07:00**; the smoke v2 result was written at 00:52:33. No content changed.

## Dated evidence and citation addendum — 2026-10-18T01:13:39-07:00

- Theorem 6 is on **printed p.574 / PDF10**, not p.575 as the source list above says.
- The exact v2 smoke result SHA is `cff3a8dc8683ceafbd5011da2211513ab96cbedfcd0723aa2afcbf19de575c53`; the earlier suffix `…c575` is a transcription error.
- A separate parent exact-Fraction route now checks rational realizations at a=2, c=1, b²=1/4, 1, 3 (orders 3, 4, 6). Polynomial factorization, exit numerator, positive normalization and twelve exact transfer evaluations pass; three wrong-initial-state controls are rejected. [Receipt](phase-type-complex3-parent-smoke-v1/exact-rational-v1.json), SHA `a005c05c0033b72ffcc37cd61a499f613b644a4633516636c768e9f06eebcdb5`. No worker code was imported.
- The worker's v3 proof extends the IVT construction itself to n=3 by starting at t₀=2φ rather than 0. This was already present as a cross-check in v2; the parent read its derivation and the exact v2→v3 diff. Its validation is part of the ongoing hostile reviews, not supplied by the finite order-3 example.
- A [parent primary-source comparison](phase-type-complex3-priority-parent-spot-v1.json) checks Liu–Yao–Zhang 2025's abstract, Introduction and §2. Their algorithm targets order equal to algebraic degree; it is not an all-n solution of this conjecture in the read scope.
