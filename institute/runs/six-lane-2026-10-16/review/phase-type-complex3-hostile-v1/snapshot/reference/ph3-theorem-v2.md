# Minimal PH order for one real pole and one complex pair — written all-n proof, version 2

Worker `MathPhaseType3`, lane `mathematics/evidence/six-lane-20261016/phase-type-complex3/`, 2026-10-18 PDT.
Status: **worker candidate proof, unreviewed.** Claim wording is about correctness only: no novelty, priority or
"first" claim. Scope: Commault–Mocanu (2003) Conjecture 1 for the Eq. (42) family only, not the book's general
minimal-representation question (book p.544). Finite computations in `code/`, `runs/` are smoke checks; **no step
below depends on a numerical root finder or a table.**

Version 2 replaces v1 (`proof/ph3-theorem-v1.md`, kept unchanged) after parent instructions of 00:58 PDT:
(i) Part A now quotes Proposition 1 of the paper exactly and spells out the reduction of an arbitrary PH
representation — states unreachable from α, states that never reach absorption, reducible classes — before
applying Theorem 6 to the dominant eigenvalue −c; (ii) the n* = 3 case is stated as a separate import of Theorem 14,
with the construction's n = 3 coverage demoted to an independent cross-check. Part B is unchanged in substance.

## 0. Statement

**Definitions.** A real square matrix is *Metzler* if its off-diagonal entries are ≥ 0; s(X) is the spectral
abscissa (max real part of an eigenvalue). A PH representation of order n of F is (α, T) with α ∈ ℝ^{1×n},
α ≥ 0, α𝟙 = 1; T ∈ ℝ^{n×n} Metzler, T𝟙 ≤ 0, T Hurwitz; and F(s) = α(sI − T)⁻¹(−T𝟙). (For Metzler T with
T𝟙 ≤ 0, Hurwitz ⇔ nonsingular, so this agrees with the paper's "non-singular PH generator".) The graph of T has
an edge i → j (i ≠ j) iff T_ij > 0; the input vertex points to every i with α_i > 0, and i points to the
absorbing vertex iff (−T𝟙)_i > 0.

**Theorem.** Let a > c > 0 and b > 0 be real and F(s) = c(a² + b²) / [(s + c)((s + a)² + b²)]. The minimum order
of a PH representation of F equals n* := min{ n ∈ ℤ, n ≥ 3 : b ≤ (a − c) cot(π/n) }.

With β := b/(a − c): n* = n iff cot(π/(n−1)) < β ≤ cot(π/n) (for n = 3 read 0 < β). Put φ := arctan β ∈ (0, π/2)
and ψ := π − 2φ ∈ (0, π). As tan is increasing on (0, π/2) and cot(π/n) = tan(π/2 − π/n), β ≤ cot(π/n) ⇔ ψ ≥ 2π/n;
hence

  n* = n ≥ 4 ⇔ 2π/n ≤ ψ < 2π/(n−1),  n* = 3 ⇔ 2π/3 ≤ ψ < π.      (0.1)

## Part A. Lower bound: every PH representation of F has order ≥ n*

Let (α, T) be a PH representation of F of order n and t := −T𝟙 ≥ 0.

**A1 (poles are eigenvalues; the converse is not assumed).** F(s) = α adj(sI − T) t / det(sI − T). In lowest
terms F has the constant numerator c(a² + b²) ≠ 0 and the three distinct simple poles −c, −a ± ib. Each pole is a
root of det(sI − T). Nothing is assumed about eigenvalues of T that are not poles of F.

**A2 (reduction 1: states unreachable from α).** Let R be the set of states reachable from supp(α) in the graph
of T (supp(α) ⊆ R) and S its complement. If i ∈ R and T_ij > 0 then j ∈ R, so T_RS = 0. Ordering R first,
T = [[T_RR, 0], [T_SR, T_SS]], (sI − T)⁻¹ is block lower triangular with (sI − T_RR)⁻¹ in the R-block, α = (α_R, 0)
and t_R = −T_RR𝟙_R. Hence F(s) = α_R(sI − T_RR)⁻¹t_R. (α_R, T_RR) is a PH representation of order n_R := |R| ≤ n:
α_R ≥ 0, α_R𝟙 = 1, T_RR is Metzler, T_RR𝟙 = (T𝟙)_R ≤ 0, and spec(T_RR) ⊆ spec(T) (block triangularity), so T_RR
is Hurwitz. By A1 for this representation, −c and −a ± ib are eigenvalues of T_RR; in particular n_R ≥ 3.

**A3 (reduction 2: there are no states that never reach absorption).** Let X be any PH generator (Metzler,
X𝟙 ≤ 0, Hurwitz) with exit vector x := −X𝟙, and let U be the set of states from which no state j with x_j > 0 is
reachable (a state reaches itself). If i ∈ U then x_i = 0, and X_ij > 0 implies j ∈ U. Hence X_{U,U^c} = 0 and, for
i ∈ U, Σ_{j∈U} X_ij = Σ_j X_ij = −x_i = 0, i.e. X_UU𝟙 = 0. So 0 ∈ spec(X_UU) ⊆ spec(X) if U ≠ ∅ (block
triangularity), contradicting Hurwitz. Thus U = ∅: from every state some exit is reachable. Applied to X = T_RR
(paths from R stay in R), every state of R lies on a path from the input vertex to the absorbing vertex, i.e. the
trimmed representation is *irreducible* in the sense of the paper (p.570, PDF6: "We say that the representation
is irreducible if any state vertex belongs to an input–output path in the associated graph."). Reduction 2 removes
nothing; it only certifies irreducibility.

**A4 (reducible classes allowed; the dominant eigenvalue of T_RR is −c).** T_RR need not be an irreducible
matrix (it may have several strongly connected classes); the following argument does not use irreducibility of
T_RR. Let μ := s(T_RR) < 0. For κ > max_i |(T_RR)_ii|, T_RR + κI ≥ 0, and Perron–Frobenius for nonnegative
(possibly reducible) matrices gives that ρ(T_RR + κI) = μ + κ is an eigenvalue with a left eigenvector u ≥ 0,
u ≠ 0; so uT_RR = μu.
* For τ > 0, e^{T_RR τ} = e^{−κτ} Σ_k τ^k (T_RR + κI)^k / k!, so (e^{T_RR τ})_{ij} > 0 whenever j = i or j is
  reachable from i. Every j ∈ R is reachable from some i with α_i > 0 (A2), hence p := α_R e^{T_RR τ} > 0
  entrywise. With ε := min_j p_j / max_j u_j > 0, p − εu ≥ 0.
* u·t_R = −u T_RR 𝟙 = −μ (u·𝟙) > 0.
* f(r) := α_R e^{T_RR r} t_R ≥ 0, and for r ≥ τ, since e^{T_RR(r−τ)} t_R ≥ 0,
  f(r) = p e^{T_RR(r−τ)} t_R ≥ ε u e^{T_RR(r−τ)} t_R = ε e^{μ(r−τ)} (u·t_R).
* For real s > μ, F(s) = ∫₀^∞ e^{−sr} f(r) dr ≥ ε (u·t_R) e^{−sτ}/(s − μ) → +∞ as s ↓ μ.
A rational function unbounded as s ↓ μ has a pole at μ; the only real pole of F is −c. Hence s(T_RR) = −c, and
−c is the eigenvalue of T_RR of maximal real part.

*Relation to Proposition 1 of the paper.* Commault–Mocanu p.570 (PDF6), verbatim: "**Proposition 1:** Consider a
linear system with transfer function g̃(s) which admits a positive realization. For any irreducible positive
realization (A, B, C) the eigenvalue of A with maximal real part is the pole of maximal real part of g̃(s)." Its
printed proof is a pointer: "The result is proved in Anderson et al. (1996) for discrete-time systems but the same
arguments can be used for continuous-time systems. Also the notion of irreducibility is not explicit in the
formulation of Anderson et al. (1996)", followed by "The same result was proved for PH-representations in Neuts
(1984)." Under the paper's dictionary (ẋ = Ax + Bu, y = Cx, g̃ = C(sI − A)⁻¹B, edge x_i → x_j iff a_ji > 0) the
trimmed representation is the irreducible positive realization (A, B, C) = (T_RRᵀ, α_Rᵀ, t_Rᵀ) (A3), and the pole
of maximal real part of F is −c (as a + ib, a − ib have real part −a < −c). So A4 is exactly the instance of
Proposition 1 needed here; A4 proves it directly and Part A does not rely on the cited proof.

**A5 (sector bound at the dominant eigenvalue −c).** Theorem 6 of the paper (p.574, PDF10; Dmitriev–Dynkin 1945,
O'Cinneide 1991): "Let T be a phase-type generator of order n. Let −λ₁, λ₁ > 0, be its eigenvalue with maximal real
part and −λ₂ ± iθ, λ₂ > 0 and θ > 0, be any pair of its complex eigenvalues. The following relation is satisfied
θ/(λ₂ − λ₁) ≤ cot(π/n)." Apply it to the PH generator T_RR of order n_R with −λ₁ = −c (A4), −λ₂ ± iθ = −a ± ib
(A2): b/(a − c) ≤ cot(π/n_R). Appendix A gives an independent proof of this inequality for every Metzler matrix,
reducible or not.

*Why the reductions matter.* Applied to an untrimmed T, Theorem 6 only gives b/(a − λ₁) ≤ cot(π/n) with
−λ₁ = s(T) ≥ −c; an unreachable state with eigenvalue in (−c, 0) makes this strictly weaker. A2 removes such
states; A4 shows no reachable state (in any class, observable or not) carries an eigenvalue of real part > −c.

**A6 (conclusion).** n_R ≥ 3 and β ≤ cot(π/n_R), so n_R ∈ {m ≥ 3 : β ≤ cot(π/m)} and n ≥ n_R ≥ n*. ∎(A)

## Part B. Construction of order n for every n ≥ 4 with n* = n (also valid for n = 3, used only as a cross-check)

Throughout, n := n* and β, φ, ψ are as in §0, so (0.1) holds. The steps are written for every n ≥ 3; the theorem
uses Part B for n* ≥ 4 and imports the n* = 3 case (Part C).

**B0 (time normalization).** δ := a − c > 0, A := a/δ > 1, C := c/δ = A − 1 > 0, β = b/δ, and
Φ(σ) := F(δσ) = C(A² + β²)/[(σ + C)((σ + A)² + β²)]. If (α, T′) is an order-n PH representation of Φ, then (α, δT′)
is one of F: δT′ is Metzler, δT′𝟙 ≤ 0, Hurwitz, and α(sI − δT′)⁻¹(−δT′𝟙) = α(s/δ·I − T′)⁻¹(−T′𝟙) = Φ(s/δ) = F(s).
With x := σ + A: Φ = K/D(x), K := C(A² + β²) > 0, D(x) := (x − 1)(x² + β²).

**B1 (three angles by one intermediate-value argument).** S := 2π − (n − 3)ψ and s(θ) := sin(θ + φ). Then

  2ψ < S ≤ 3ψ.  (B1.1)

For n ≥ 4: S > 2ψ ⇔ (n − 1)ψ < 2π and S ≤ 3ψ ⇔ nψ ≥ 2π, both by (0.1). For n = 3: S = 2π and 2π/3 ≤ ψ < π. On
[0, π − φ]: s ≥ 0 with s = 0 only at π − φ; s(θ) ≥ sin φ iff θ ∈ [0, ψ]; 0 ≤ s(θ) < sin φ on (ψ, π − φ].

*Lemma B1.* There are θ₁, θ₂, θ₃ ∈ (0, π − φ) with θ₁ + θ₂ + θ₃ = S and s(θ₁)s(θ₂)s(θ₃) = sin³φ.

*Proof.* t₀ := max(0, S − 2(π − φ)); S ≤ 3ψ < 3(π − φ) gives t₀ < S/3. For t ∈ [t₀, S/3]: t ∈ [0, ψ] and
(S − t)/2 ∈ [S/3, (S − t₀)/2] ⊆ [0, π − φ]. Let G(t) := s(t)·s((S − t)/2)² − sin³φ (continuous).
G(S/3) = s(S/3)³ − sin³φ ≥ 0 since S/3 ≤ ψ. If t₀ > 0, then (S − t₀)/2 = π − φ and G(t₀) = −sin³φ < 0; if t₀ = 0,
then S/2 ∈ (ψ, π − φ] by (B1.1) and S ≤ 2(π − φ), so 0 ≤ s(S/2) < sin φ and G(0) < 0. By the intermediate value
theorem some t* ∈ (t₀, S/3] has G(t*) = 0. Put θ₁ := t*, θ₂ := θ₃ := (S − t*)/2: then 0 ≤ t₀ < θ₁ ≤ S/3 ≤ ψ < π − φ
and S/3 ≤ θ₂ < (S − t₀)/2 ≤ π − φ. ∎

Any root may be used. At the upper band endpoint (nψ = 2π, S = 3ψ) one may take t* = S/3: all θ = ψ = 2π/n. Since
t* > t₀ ≥ 0 strictly, θ₁ > 0 and all diagonal entries below are finite for every β in the band; the lower endpoint
β = cot(π/(n−1)) belongs to the band of n − 1 (at it, G(t₀) = 0 and the n-state bracket degenerates, which is why
the band rule uses n − 1 there). For n ≥ 4, t₀ = 0 (S ≤ 2(π − φ) ⇔ (n − 2)ψ ≥ π, implied by ψ ≥ 2π/n, n ≥ 4); for
n = 3, t₀ = 2φ > 0.

**B2 (the cycle matrix).** θ₄ = … = θ_n := ψ; all θ_i ∈ (0, π − φ) ⊂ (0, π) and Σθ_i = S + (n − 3)ψ = 2π.
m_i := −β cot θ_i. For θ ∈ (0, π), with β = sin φ/cos φ:

  1 − m(θ) = sin(θ + φ)/(cos φ sin θ),  (I1)    iβ − m(θ) = β(cot θ + i) = β e^{iθ}/sin θ.  (I2)

So 1 − m_i > 0, and m_i = m_* := −β cot ψ = tan φ cot 2φ = (1 − β²)/2 for i ≥ 4. W := Π_{i=1}^n (1 − m_i) > 0.
M: M_ii = m_i, M_{i,i+1} = 1 (1 ≤ i ≤ n − 1), M_{n,1} = W, all other entries 0. M is Metzler; its graph is the
directed n-cycle 1 → 2 → … → n → 1.

**B3 (characteristic polynomial, divisibility).** In the Leibniz expansion of det(xI − M) only the identity and the
n-cycle i ↦ i + 1 (mod n) are supported; the cycle has sign (−1)^{n−1} and entry product (−1)^{n−1}(−W). Hence
q(x) := det(xI − M) = Π_{i}(x − m_i) − W. q(1) = 0 by the definition of W. By (I1), (I2),

  q(iβ) = [sin^n φ · e^{iΣθ_i} − Π_i sin(θ_i + φ)] / (cos^n φ Π_i sin θ_i),

and e^{iΣθ_i} = e^{2πi} = 1, Π_i sin(θ_i + φ) = s(θ₁)s(θ₂)s(θ₃)·sin(ψ + φ)^{n−3} = sin³φ·sin^{n−3}φ (as
sin(ψ + φ) = sin(π − φ)) = sin^n φ. So q(±iβ) = 0 (real coefficients), D | q, and P := q/D is monic of degree n − 3.

**B4 (Perron root of M is 1).** u₁ := 1, u_{i+1} := (1 − m_i)u_i (i < n); u > 0. (Mu)_i = m_iu_i + u_{i+1} = u_i for
i < n, and (Mu)_n = m_nu_n + W = m_nu_n + (1 − m_n)u_n = u_n. M + κI (κ > max|m_i|) is nonnegative, irreducible with
positive diagonal, hence primitive; by Perron–Frobenius its only eigenvalue with a positive eigenvector is its
spectral radius, so ρ(M + κI) = 1 + κ and every other eigenvalue λ of M has |λ + κ| < 1 + κ, so Re λ < 1. s(M) = 1.

**B5 (resolvent row; orientation).** For x ∉ spec(M), y_j := Π_{k=j+1}^n (x − m_k)/q(x) satisfies y(xI − M) = e₁:
column 1 gives [Π_{k=1}^n(x − m_k) − W]/q = 1, column j ≥ 2 gives [−Π_{k=j}^n(x − m_k) + (x − m_j)Π_{k=j+1}^n(x − m_k)]/q = 0.
So e₁(xI − M)⁻¹t = N_t(x)/q(x) with N_t(x) := Σ_{j=1}^n t_j Π_{k=j+1}^n (x − m_k).

**B6 (exit vector; cancelling numerator).** ρ := (1 + β²)/2; 1 − m_* = ρ, m_*² + β² = ρ², D(m_*) = −ρ³ ≠ 0;
h(x) := −1/D(x) = 1/[(1 − x)(x² + β²)], analytic at m_*; h_k := h^{(k)}(m_*)/k!; z := x − m_*. Define

  t₁ = t₂ := 0,  t₃ := K,  t_j := K·W·h_{n−j}  (4 ≤ j ≤ n).

For j ≥ 3, Π_{k=j+1}^n (x − m_k) = z^{n−j}, so N_t = K[z^{n−3} + W Σ_{k=0}^{n−4} h_k z^k]. With R₃ := Π_{i≤3}(x − m_i),
P·D = q = R₃z^{n−3} − W; in ℝ[[z]], D(m_* + z) is a unit, so P(m_* + z) = W h(m_* + z) + z^{n−3}R₃/D: the
coefficients of z^k, k ≤ n − 4, are W h_k, and P is monic of degree n − 3. Hence N_t = K·P and
e₁(xI − M)⁻¹t = KP/(DP) = K/D(x). (n = 3: P = 1, N_t = t₃ = K.)

**B7 (every exit positive, every n).** With u := z/ρ: 1 − (m_* + z) = ρ(1 − u), (m_* + z)² + β² = ρ²(1 − 2cos ψ·u + u²)
(as m_*/ρ = cos 2φ = −cos ψ), so h(m_* + z) = ρ^{−3}/[(1 − u)(1 − 2cos ψ·u + u²)]. Since
1/[(1 − e^{iψ}u)(1 − e^{−iψ}u)] = Σ_k u^k sin((k+1)ψ)/sin ψ, multiplying by Σu^k and telescoping
2 sin(ψ/2) sin(jψ) = cos((j − ½)ψ) − cos((j + ½)ψ):

  h_k = ρ^{−3−k} c_k,  c_k = [cos(ψ/2) − cos((k + 3/2)ψ)] / [2 sin(ψ/2) sin ψ].

For 0 ≤ k ≤ n − 4: ψ/2 < (k + 3/2)ψ ≤ (n − 5/2)ψ < 2π − ψ/2, the last because (n − 2)ψ < 2π (ψ < 2π/(n − 1)); on
(ψ/2, 2π − ψ/2), cos < cos(ψ/2). So c_k > 0, h_k > 0, t₃, …, t_n > 0.

**B8 (Hurwitz; diagonal PH normalization).** T₀ := M − A·I: Metzler, irreducible, s(T₀) = 1 − A = −C < 0. For τ > 0,
e^{T₀τ} > 0 entrywise, so (−T₀)⁻¹ = ∫₀^∞ e^{T₀τ}dτ > 0 entrywise and v := (−T₀)⁻¹t > 0. D_v := diag(v),
T′ := D_v⁻¹T₀D_v, α′ := e₁D_v = v₁e₁. T′ is Metzler, T′𝟙 = −D_v⁻¹t ≤ 0, T′ is Hurwitz (similar to T₀), and
α′(σI − T′)⁻¹(−T′𝟙) = e₁((σ + A)I − M)⁻¹t = K/D(σ + A) = Φ(σ). v₁ = e₁(−T₀)⁻¹t = Φ(0) = 1, so α′ = e₁. By B0,
(e₁, δT′) is an order-n PH representation of F; in original units T = D_v⁻¹(δM − aI)D_v, exits −T𝟙 = δD_v⁻¹t,
α = e₁. (Any positive multiple of t gives the same T′; v₁ = 1 fixes the multiple for which α′ = e₁.) ∎(B)

## Part C. Conclusion

* **n* = 3 (imported, separately).** Theorem 14 of the paper (p.577, PDF13; Commault and Chemla 1996), printed:
  "Consider a PH-distribution with Laplace transform f̃(s) = 1/q(s), q(s) = (1 + s/c)(1 + s/(a + ib))(1 + s/(a − ib))
  (42) where a, b, c ≥ 0. This distribution has an order 3 representation if and only if b ≤ (a − c)/√3 (43)."
  Our domain a > c > 0, b > 0 lies inside the printed hypothesis a, b, c ≥ 0, and 1/q(s) = F(s). So n* = 3 ⇒ an
  order-3 representation exists (import); order ≥ 3 holds by A1 (three distinct poles). Independent cross-check, not
  needed by the theorem: Part B with n = 3 (t₀ = 2φ > 0) also produces an order-3 representation; it is checked
  exactly at β = 1/√3 (run e01-exact, item E10) and in ball arithmetic at six interior β (runs b01, b02).
* **n* ≥ 4.** Part B gives an order-n* representation for every a > c > 0, b > 0 with n* ≥ 4.
* **Lower bound.** Part A gives order ≥ n* for every PH representation (all topologies; unreachable states,
  cancellations, unobservable or reducible classes allowed).

Hence the minimum PH order of F is exactly n*, i.e. Commault–Mocanu Conjecture 1 holds for the Eq. (42) family,
conditional only on the imported Theorem 14 for n* = 3 (and, if Appendix A is not used, on the imported Theorem 6).

## Appendix A. Independent proof of the sector inequality (A5)

**Lemma A.** Let X be an m×m Metzler matrix (m ≥ 2) and λ a non-real eigenvalue. Then
|Im λ| ≤ (s(X) − Re λ) cot(π/m).

*Irreducible case.* μ := s(X); Perron–Frobenius gives r > 0 with Xr = μr, and Re λ < μ for every eigenvalue λ ≠ μ
(primitivity of X + κI). Q := diag(r)⁻¹(X − μI)diag(r) is Metzler with Q𝟙 = 0; z := λ − μ is an eigenvalue of Q
with eigenvector w ∈ ℂ^m; after conjugating if necessary z = −x + iy, x > 0, y > 0; z = |z|e^{i(π−φ)} with
φ := arctan(y/x) ∈ (0, π/2). For r ≥ 0, e^{Qr} is stochastic and e^{Qr}w = e^{zr}w, so with
K := conv{w₁, …, w_m} ⊂ ℂ ≅ ℝ² (multiplication by e^{zr} is ℝ-linear) e^{zr}K ⊆ K.
1. 0 ∈ K (closed; e^{zr}w_i → 0). K is not in a line L: else 0 ∈ L and for w_i ≠ 0 the arguments arg w_i + yr of
   e^{zr}w_i ∈ L would stay in {ϑ, ϑ + π} mod 2π.
2. 0 ∈ int K: else a unit ν has Re(ν̄w) ≥ 0 on K; a vertex v ≠ 0 exists, and for r with arg(e^{zr}v) = arg(−ν),
   Re(ν̄e^{zr}v) < 0.
3. K is a convex polygon with vertices v₁, …, v_p (counter-clockwise, 3 ≤ p ≤ m, v_k ≠ 0); ω_k ∈ (0, π) is the
   angle at 0 of Δ_k = (0, v_k, v_{k+1}) (indices mod p), Σω_k = 2π; ε_k is its angle at v_k, so its angle at v_{k+1}
   is π − ω_k − ε_k.
4. K ⊆ v_k + C_k, C_k := cone(v_{k+1} − v_k, v_{k−1} − v_k) (closed, angular width < π, containing −v_k in its
   interior). e^{zr}v_k ∈ K gives zv_k ∈ C_k. Rotating so that v_k > 0: −v_k has direction π, v_{k+1} − v_k has
   direction π − ε_k (upper half plane, since arg(v_{k+1}/v_k) = ω_k ∈ (0, π)), v_{k−1} − v_k points into the lower
   half plane, and zv_k has direction π − φ. Hence φ ≤ ε_k for all k.
5. Law of sines in Δ_k: |v_{k+1}|/|v_k| = sin ε_k / sin(ω_k + ε_k) =: g_k(ε_k); the product over k is 1.
   (log g_k)′ = cot ε − cot(ω_k + ε) > 0 on (0, π − ω_k), and φ ≤ ε_k < π − ω_k, so 1 ≥ Π_k g_k(φ):
   sin^pφ ≤ Π_k sin(ω_k + φ), all ω_k + φ ∈ (0, π).
6. log sin is concave on (0, π): sin φ ≤ sin(φ + 2π/p) with φ + 2π/p ∈ (0, π). For 0 < u < v < π, sin u ≤ sin v
   ⇔ u + v ≤ π; so 2φ + 2π/p ≤ π, i.e. y/x = tan φ ≤ cot(π/p) ≤ cot(π/m).

*General case.* In Frobenius normal form X is block triangular with irreducible diagonal blocks; λ is an eigenvalue
of a block B (size m_B, Perron root μ_B ≤ s(X)). 1×1 blocks have real eigenvalues and irreducible 2×2 Metzler
blocks have discriminant (B₁₁ − B₂₂)² + 4B₁₂B₂₁ ≥ 0, so m_B ≥ 3 and
|Im λ| ≤ (μ_B − Re λ)cot(π/m_B) ≤ (s(X) − Re λ)cot(π/m). ∎

Applied with X = T_RR, m = n_R, λ = −a + ib, s(X) = −c (A4): b ≤ (a − c)cot(π/n_R). This is the classical
Dmitriev–Dynkin/O'Cinneide statement, re-derived; no new result is claimed for it.

## Appendix B. Formula summary and remarks

* Normalized time: m_i = −β cot θ_i, m_* = (1 − β²)/2, ρ = (1 + β²)/2, W = β^n/Π_i sin θ_i,
  t = K·(0, 0, 1, W h_{n−4}, …, W h₀), h_k = ρ^{−3−k}c_k.
* At β = cot(π/n) the uniform cycle (all θ_i = 2π/n) attains equality in Theorem 6 (the polygon of Appendix A is
  the regular n-gon).
* Finite smoke (hash-bound receipts in `receipts/`): exact sympy identities (run e01-exact; its single FAIL, item
  E4, is a simplifier miss resolved by run e02-exact-e4 with three independent symbolic methods); 320/640-bit ball
  arithmetic instances n = 3..12, 16, 20, 24, 32, 48, 64 including upper endpoints and f = 10⁻¹² from the lower
  endpoint (runs b01, b02); designed mutations (run m01). None of these is part of the proof.

## Differences from the untrusted candidate (`review/phase-type-complex3-candidate-v1.md`)

* The candidate's IVT starts at t = 0 for n ≥ 4 (at n = 3, G(0) = 0); Lemma B1 uses t₀ = max(0, S − 2(π − φ)).
* Angle choice ψ = π − 2φ, m_* = (1 − β²)/2, divisibility, the exit formula t_j = K W h^{(n−j)}(m_*)/(n−j)!, the
  generating function, the sign test cos(ψ/2) − cos((k + 3/2)ψ), v₁ = 1 and α = e₁ were re-derived and agree.
* The candidate gave no lower-bound applicability argument; A2–A4 supply it.
