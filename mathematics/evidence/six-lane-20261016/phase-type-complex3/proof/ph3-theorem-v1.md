# Minimal PH order for one real pole and one complex pair — written all-n proof, version 1

Worker `MathPhaseType3`, lane `mathematics/evidence/six-lane-20261016/phase-type-complex3/`, written
2026-10-18 (PDT). Status: **worker candidate proof, unreviewed.** Scope: Commault–Mocanu (2003) Conjecture 1
(Eq. 42 family) only, not the book's general minimal-representation question. No novelty or priority claim.
Finite computations in `code/`/`runs/` are smoke checks; **no step below depends on a numerical root finder or
table.** The untrusted candidate `review/phase-type-complex3-candidate-v1.md` was re-derived independently; §6
records where this text differs from it.

## 0. Statement

**Definitions.** A real square matrix is *Metzler* if its off-diagonal entries are ≥ 0. For a square matrix X,
s(X) = max Re λ over eigenvalues λ (spectral abscissa). A PH representation of order n of a function F is a pair
(α, T): α ∈ ℝ^{1×n}, α ≥ 0, α𝟙 = 1; T ∈ ℝ^{n×n} Metzler, T𝟙 ≤ 0, T Hurwitz (s(T) < 0); and
F(s) = α(sI − T)⁻¹(−T𝟙). The graph of T has an edge i → j (i ≠ j) iff T_ij > 0.

**Theorem.** Let a > c > 0 and b > 0 be real and
F(s) = c(a² + b²) / [(s + c)((s + a)² + b²)].
Then the minimum order of a PH representation of F equals

n* := min{ n ∈ ℤ, n ≥ 3 : b ≤ (a − c) cot(π/n) }.

Equivalently, with β := b/(a − c), n* = n iff cot(π/(n−1)) < β ≤ cot(π/n) (for n = 3 read the left inequality
as 0 < β). n* is finite because cot(π/n) → ∞.

**Angle form of the bands.** Put φ := arctan β ∈ (0, π/2) and ψ := π − 2φ ∈ (0, π). Since tan is increasing on
(0, π/2) and cot(π/n) = tan(π/2 − π/n): β ≤ cot(π/n) ⇔ φ ≤ π/2 − π/n ⇔ ψ ≥ 2π/n. Hence

  n* = n ≥ 4 ⇔ 2π/n ≤ ψ < 2π/(n−1),  n* = 3 ⇔ 2π/3 ≤ ψ < π.      (0.1)

Part A proves every PH representation has order ≥ n*; Part B constructs one of order exactly n*.

## Part A. Lower bound

Let (α, T) be any PH representation of F, of order n, and t := −T𝟙 ≥ 0.

**A1 (poles are eigenvalues; converse not assumed).** F(s) = α adj(sI − T) t / det(sI − T). In lowest terms F has
numerator c(a² + b²) ≠ 0 and the three distinct simple poles −c, −a + ib, −a − ib; each is therefore a root of
det(sI − T). Nothing is assumed about eigenvalues of T that are not poles of F.

**A2 (trimming unreachable states).** Let R be the set of states reachable from supp(α) (including supp(α)) in
the graph of T, and S its complement. If i ∈ R and T_ij > 0 then j ∈ R, so T_RS = 0. Ordering R first,
T = [[T_RR, 0], [T_SR, T_SS]], so (sI − T)⁻¹ is block lower triangular with (sI − T_RR)⁻¹ in the R-block.
Since α = (α_R, 0) and t_R = −T_RR 𝟙_R (because T_RS = 0),

  F(s) = α_R (sI − T_RR)⁻¹ t_R.

(α_R, T_RR) is a PH representation of order n_R := |R| ≤ n: α_R ≥ 0 with α_R𝟙 = 1; T_RR is Metzler with
T_RR𝟙 = (T𝟙)_R ≤ 0; spec(T_RR) ⊆ spec(T) by block triangularity, so T_RR is Hurwitz. By A1 applied to this
representation, −c and −a ± ib are eigenvalues of T_RR; in particular n_R ≥ 3.

**A3 (the dominant eigenvalue of the trimmed generator is −c).** Let μ := s(T_RR) < 0. Since T_RR + κI ≥ 0 for
κ ≥ max_i |(T_RR)_ii|, Perron–Frobenius gives that μ is a real eigenvalue of T_RR with a left eigenvector u ≥ 0,
u ≠ 0, uT_RR = μu.

* For τ > 0, e^{T_RR τ} = e^{−κτ} Σ_k τ^k (T_RR + κI)^k / k! with κ > max|(T_RR)_ii|, so (e^{T_RR τ})_{ij} > 0
  whenever j = i or j is reachable from i. Every j ∈ R is reachable from some i with α_i > 0 (the path stays in R),
  hence p := α_R e^{T_RR τ} is entrywise positive. Put ε := min_j p_j / max_j u_j > 0; then p − εu ≥ 0.
* u·t_R = −u T_RR 𝟙 = −μ (u·𝟙) > 0.
* f(r) := α_R e^{T_RR r} t_R ≥ 0 for r ≥ 0 (all factors nonnegative). For r ≥ τ, since e^{T_RR (r−τ)} t_R ≥ 0,
  f(r) = p e^{T_RR (r−τ)} t_R ≥ ε u e^{T_RR (r−τ)} t_R = ε e^{μ(r−τ)} (u·t_R).
* For real s > μ, (sI − T_RR)⁻¹ = ∫₀^∞ e^{−sr} e^{T_RR r} dr, so F(s) = ∫₀^∞ e^{−sr} f(r) dr and
  F(s) ≥ ε (u·t_R) ∫_τ^∞ e^{−sr} e^{μ(r−τ)} dr = ε (u·t_R) e^{−sτ}/(s − μ) → +∞ as s ↓ μ.

A rational function unbounded as s ↓ μ has a pole at μ. The only real pole of F is −c, so s(T_RR) = −c.

**A4 (sector bound).** Theorem 6 of Commault–Mocanu (Dmitriev–Dynkin 1945, O'Cinneide 1991; paper p.574) states:
for a PH generator of order m with eigenvalue −λ₁ (λ₁ > 0) of maximal real part and any complex pair −λ₂ ± iθ
(λ₂ > 0, θ > 0), θ/(λ₂ − λ₁) ≤ cot(π/m). Apply it to T_RR (m = n_R) with λ₁ = c (A3), λ₂ = a, θ = b (A2):
b/(a − c) ≤ cot(π/n_R). An independent proof of exactly the needed inequality is Appendix A.

Hence n_R ≥ 3 lies in {m ≥ 3 : b ≤ (a − c)cot(π/m)}, so n ≥ n_R ≥ n*. ∎(A)

*Why A2–A3 are needed.* Applied to an untrimmed T, Theorem 6 only gives b/(a − λ₁) ≤ cot(π/n) with
−λ₁ = s(T) ≥ −c; if an unreachable state has eigenvalue in (−c, 0) this is strictly weaker. A3 shows that no
reachable state (observable or not) can carry an eigenvalue with real part > −c, so trimming unobservable states is
unnecessary.

## Part B. Construction of order n*

Throughout, n := n* ≥ 3 and β, φ, ψ are as in §0, so (0.1) holds.

**B0 (time normalization).** δ := a − c > 0, A := a/δ > 1, C := c/δ = A − 1 > 0, β = b/δ, and
Φ(σ) := F(δσ) = C(A² + β²) / [(σ + C)((σ + A)² + β²)]. If (α, T′) is an order-n PH representation of Φ then
(α, δT′) is one of F: δT′ is Metzler, δT′𝟙 ≤ 0, Hurwitz, and
α(sI − δT′)⁻¹(−δT′𝟙) = α(s/δ·I − T′)⁻¹(−T′𝟙) = Φ(s/δ) = F(s).
With x := σ + A: σ + C = x − 1 and Φ = K/D(x), where

  K := C(A² + β²) > 0,  D(x) := (x − 1)(x² + β²).

**B1 (three angles; one intermediate-value argument for every n ≥ 3).** Put S := 2π − (n − 3)ψ and
s(θ) := sin(θ + φ). Then

  2ψ < S ≤ 3ψ.  (B1.1)

For n ≥ 4: S > 2ψ ⇔ (n − 1)ψ < 2π and S ≤ 3ψ ⇔ nψ ≥ 2π, both by (0.1). For n = 3: S = 2π, and 2π/3 ≤ ψ < π
gives (B1.1). On [0, π − φ], θ + φ ∈ [φ, π], so s(θ) ≥ 0 with s(θ) = 0 only at θ = π − φ; s(θ) ≥ sin φ iff
θ ∈ [0, ψ]; and 0 ≤ s(θ) < sin φ for θ ∈ (ψ, π − φ].

*Lemma B1.* There are θ₁, θ₂, θ₃ ∈ (0, π − φ) with θ₁ + θ₂ + θ₃ = S and s(θ₁)s(θ₂)s(θ₃) = sin³φ.

*Proof.* Let t₀ := max(0, S − 2(π − φ)). From S ≤ 3ψ = 3π − 6φ < 3(π − φ) we get t₀ < S/3. For
t ∈ [t₀, S/3]: t ∈ [0, ψ] (as S/3 ≤ ψ), and (S − t)/2 ∈ [S/3, (S − t₀)/2] ⊆ [0, π − φ]. Define the continuous
function G(t) := s(t)·s((S − t)/2)² − sin³φ on [t₀, S/3].
* G(S/3) = s(S/3)³ − sin³φ ≥ 0 because S/3 ≤ ψ.
* If t₀ > 0 then (S − t₀)/2 = π − φ and G(t₀) = −sin³φ < 0. If t₀ = 0 then S/2 ∈ (ψ, π − φ] by (B1.1) and
  S ≤ 2(π − φ), so 0 ≤ s(S/2) < sin φ and G(0) = sin φ·s(S/2)² − sin³φ < 0.
By the intermediate value theorem there is t* ∈ (t₀, S/3] with G(t*) = 0. Set θ₁ := t* and θ₂ := θ₃ := (S − t*)/2.
Then 0 ≤ t₀ < θ₁ ≤ S/3 ≤ ψ < π − φ and S/3 ≤ θ₂ < (S − t₀)/2 ≤ π − φ. ∎

Any root t* may be used; uniqueness is not needed. At the upper band endpoint (nψ = 2π, S = 3ψ) one may take
t* = S/3, giving θ₁ = θ₂ = θ₃ = ψ = 2π/n. Because t* > t₀ ≥ 0 strictly, θ₁ > 0 for every β in the band, so no
infinite diagonal entry occurs; at the lower endpoint β = cot(π/(n−1)) the band rule assigns n − 1, not n.
(For n ≥ 4 in fact t₀ = 0, since S ≤ 2(π − φ) ⇔ (n − 3)ψ ≥ 2φ, which follows from (0.1); this is not needed.)

**B2 (the cycle matrix).** Put θ₄ = … = θ_n := ψ (none if n = 3). Then θ_i ∈ (0, π − φ) ⊂ (0, π) for all i,
Σ_i θ_i = S + (n − 3)ψ = 2π. Define m_i := −β cot θ_i. For θ ∈ (0, π), using β = sin φ / cos φ:

  1 − m(θ) = sin(θ + φ) / (cos φ sin θ),  (I1)
  iβ − m(θ) = β (cot θ + i) = β e^{iθ} / sin θ.  (I2)

By (I1) and θ_i < π − φ, 1 − m_i > 0. For i ≥ 4, m_i = m_* := −β cot ψ = tan φ cot 2φ = (1 − β²)/2.
Let W := Π_{i=1}^n (1 − m_i) > 0 and let M be the n×n matrix with M_ii = m_i, M_{i,i+1} = 1 (1 ≤ i ≤ n − 1),
M_{n,1} = W, all other entries 0. M is Metzler and its graph is the directed n-cycle 1 → 2 → … → n → 1.

**B3 (characteristic polynomial and divisibility).** In the Leibniz expansion of det(xI − M) the only permutations
supported on nonzero entries are the identity and the n-cycle i ↦ i + 1 (mod n), of sign (−1)^{n−1}, whose entry
product is (−1)^{n−1}·(−W). Hence

  q(x) := det(xI − M) = Π_{i=1}^n (x − m_i) − W.

q(1) = Π(1 − m_i) − W = 0. By (I1), W = Π_i sin(θ_i + φ) / (cos^n φ Π_i sin θ_i); by (I2),
Π_i (iβ − m_i) = β^n e^{iΣθ_i} / Π_i sin θ_i. Hence

  q(iβ) = [sin^n φ · e^{iΣθ_i} − Π_i sin(θ_i + φ)] / (cos^n φ Π_i sin θ_i).

Here e^{iΣθ_i} = e^{2πi} = 1 and, since sin(ψ + φ) = sin(π − φ) = sin φ,
Π_{i=1}^n sin(θ_i + φ) = s(θ₁)s(θ₂)s(θ₃)·sin^{n−3}φ = sin^n φ by Lemma B1. So q(iβ) = 0, and q(−iβ) = 0 because q
has real coefficients. As 1, iβ, −iβ are distinct, D | q; P := q/D is a monic real polynomial of degree n − 3.

**B4 (Perron root of M is 1).** Let u₁ := 1 and u_{i+1} := (1 − m_i)u_i (1 ≤ i ≤ n − 1); u > 0. For i < n,
(Mu)_i = m_i u_i + u_{i+1} = u_i; and (Mu)_n = m_n u_n + W = m_n u_n + (1 − m_n)u_n = u_n because
W = (1 − m_n)·Π_{i<n}(1 − m_i) = (1 − m_n)u_n. So Mu = u. For κ > max_i |m_i|, M + κI is nonnegative,
irreducible (graph = n-cycle) with positive diagonal, hence primitive; by Perron–Frobenius the only eigenvalue with
a positive eigenvector is its spectral radius, so ρ(M + κI) = 1 + κ and every other eigenvalue λ of M satisfies
|λ + κ| < 1 + κ, hence Re λ < 1. Thus s(M) = 1. (Spectrum of M = roots of q = {1, ±iβ} ∪ roots of P.)

**B5 (resolvent row, orientation fixed).** For x not an eigenvalue of M, the row vector y with
y_j := Π_{k=j+1}^n (x − m_k) / q(x) satisfies y(xI − M) = e₁: column 1 gives
y₁(x − m₁) − W y_n = [Π_{k=1}^n (x − m_k) − W]/q(x) = 1, and column j ≥ 2 gives
−y_{j−1} + (x − m_j)y_j = [−Π_{k=j}^n (x − m_k) + (x − m_j)Π_{k=j+1}^n (x − m_k)]/q(x) = 0. Hence for t ∈ ℝ^n

  e₁(xI − M)⁻¹ t = N_t(x)/q(x),  N_t(x) := Σ_{j=1}^n t_j Π_{k=j+1}^n (x − m_k).

(Only the unit forward weights M_{j,j+1} = 1 enter; the closing weight W enters only q.)

**B6 (the exit vector and the cancelling numerator).** Let ρ := (1 + β²)/2. Then 1 − m_* = ρ and
m_*² + β² = ρ², so D(m_*) = −ρ³ ≠ 0 and h(x) := −1/D(x) = 1/[(1 − x)(x² + β²)] is analytic at m_*. Write
h_k := h^{(k)}(m_*)/k! and z := x − m_*. Define

  t₁ = t₂ := 0,  t₃ := K,  t_j := K·W·h_{n−j}  (4 ≤ j ≤ n).

*Claim:* N_t = K·P. For j ≥ 3, Π_{k=j+1}^n (x − m_k) = z^{n−j} (all those k are ≥ 4), so
N_t = K·[z^{n−3} + W Σ_{k=0}^{n−4} h_k z^k]. Write P(m_* + z) = Σ_{k=0}^{n−3} p_k z^k with p_{n−3} = 1. With
R₃(x) := Π_{i=1}^3 (x − m_i), P·D = q = R₃(x) z^{n−3} − W. In the formal power series ring ℝ[[z]],
D(m_* + z) is a unit (constant term −ρ³), so P(m_* + z) = W·h(m_* + z) + z^{n−3}R₃/D, i.e. p_k = W h_k for
0 ≤ k ≤ n − 4 (the Taylor series of the analytic h is its formal expansion). Thus P = z^{n−3} + W Σ_{k≤n−4} h_k z^k
and N_t = K P. (For n = 3: P = 1 and N_t = t₃ = K.) Consequently, as rational functions,

  e₁(xI − M)⁻¹ t = K P(x) / (D(x) P(x)) = K / D(x).

**B7 (every exit is positive, for every n).** With u := z/ρ: 1 − (m_* + z) = ρ(1 − u) and
(m_* + z)² + β² = ρ² + 2m_* z + z² = ρ²(1 − 2cos ψ·u + u²), because m_*/ρ = (1 − β²)/(1 + β²) = cos 2φ = −cos ψ. So

  h(m_* + z) = ρ^{−3} / [(1 − u)(1 − 2cos ψ·u + u²)].

Since 1 − 2cos ψ·u + u² = (1 − e^{iψ}u)(1 − e^{−iψ}u), its reciprocal is Σ_k U_k u^k with
U_k = Σ_{j=0}^k e^{i(2j−k)ψ} = sin((k + 1)ψ)/sin ψ (ψ ∈ (0, π)). Multiplying by 1/(1 − u) = Σ u^k and telescoping
2 sin(ψ/2) sin(jψ) = cos((j − ½)ψ) − cos((j + ½)ψ):

  h_k = ρ^{−3−k} c_k,  c_k := Σ_{j=0}^k sin((j+1)ψ)/sin ψ = [cos(ψ/2) − cos((k + 3/2)ψ)] / [2 sin(ψ/2) sin ψ].

The denominator is positive. For 0 ≤ k ≤ n − 4 (only needed when n ≥ 4): ψ/2 < (k + 3/2)ψ ≤ (n − 5/2)ψ, and
(n − 5/2)ψ < 2π − ψ/2 ⇔ (n − 2)ψ < 2π, which holds as ψ < 2π/(n − 1) by (0.1). On (ψ/2, 2π − ψ/2),
cos < cos(ψ/2). So c_k > 0, h_k > 0, and t₃, …, t_n > 0, t ≥ 0, t ≠ 0. (Slack: (n − 1)ψ < 2π even gives c_{n−3} > 0.)

**B8 (Hurwitz, diagonal PH normalization).** T₀ := M − A·I is Metzler with s(T₀) = 1 − A = −C < 0 (B4), and
irreducible. For τ > 0, e^{T₀τ} is entrywise positive (irreducibility, as in A3), so
(−T₀)⁻¹ = ∫₀^∞ e^{T₀τ} dτ is entrywise positive and v := (−T₀)⁻¹ t > 0. With D_v := diag(v),

  T′ := D_v⁻¹ T₀ D_v,  α′ := e₁ D_v = v₁ e₁.

T′ is Metzler (off-diagonal (T₀)_ij v_j / v_i ≥ 0); T′𝟙 = D_v⁻¹ T₀ v = −D_v⁻¹ t ≤ 0; T′ is similar to T₀, hence
Hurwitz. For σ with σ + A ∉ spec(M):
α′(σI − T′)⁻¹(−T′𝟙) = e₁ D_v D_v⁻¹(σI − T₀)⁻¹ D_v D_v⁻¹ t = e₁((σ + A)I − M)⁻¹ t = K/D(σ + A) = Φ(σ).
Finally v₁ = e₁(0·I − T₀)⁻¹ t = Φ(0) = K/(C(A² + β²)) = 1, so α′ = e₁ is a probability vector. (e₁, T′) is an
order-n PH representation of Φ and, by B0, (e₁, δT′) is one of F. In original units:

  T = D_v⁻¹(δM − aI)D_v,  exit −T𝟙 = δ D_v⁻¹ t,  α = e₁,  with spec(δM − aI) ∋ δ − a = −c, −a ± ib. ∎(B)

## Part C. Conclusion

Part A gives order ≥ n* for every PH representation (all topologies, with unreachable/unobservable states and
cancellations allowed); Part B gives an order-n* representation for every a > c > 0, b > 0. Hence the minimum PH
order of F is exactly n*, which is Commault–Mocanu Conjecture 1 for the Eq. (42) family. For n* = 3, Part B
re-derives the sufficiency half of their Theorem 14 (b ≤ (a − c)/√3) by the same construction.

## Appendix A. Independent proof of the sector inequality used in A4

**Lemma A.** Let X be an m×m Metzler matrix (m ≥ 2) and λ a non-real eigenvalue. Then
|Im λ| ≤ (s(X) − Re λ) cot(π/m).

*Irreducible case.* Let μ := s(X); Perron–Frobenius gives r > 0 with Xr = μr, and (as in B4) Re λ < μ for every
eigenvalue λ ≠ μ. Q := diag(r)⁻¹(X − μI)diag(r) is Metzler with Q𝟙 = 0; z := λ − μ is an eigenvalue of Q with
eigenvector w ∈ ℂ^m; replacing (λ, w) by the conjugates if necessary, z = −x + iy with x > 0, y > 0. Write
z = |z|e^{i(π − φ)} with φ := arctan(y/x) ∈ (0, π/2). For r ≥ 0, P(r) := e^{Qr} is stochastic and
P(r)w = e^{zr}w, so each e^{zr}w_i is a convex combination of w₁, …, w_m. With K := conv{w₁, …, w_m} ⊂ ℂ ≅ ℝ² and
multiplication by e^{zr} being ℝ-linear, e^{zr}K ⊆ K for all r ≥ 0.
1. 0 ∈ K (K is closed and e^{zr}w_i → 0). K is not contained in a line L: else 0 ∈ L, and for w_i ≠ 0 the points
   e^{zr}w_i ∈ L have arguments arg w_i + yr, which do not stay in a set {ϑ, ϑ + π} mod 2π.
2. 0 ∈ int K: otherwise a supporting line through 0 gives a unit ν with Re(ν̄w) ≥ 0 on K; a vertex v ≠ 0 exists,
   and for r with arg(e^{zr}v) = arg(−ν) we get Re(ν̄ e^{zr}v) < 0, a contradiction.
3. So K is a convex polygon with vertices v₁, …, v_p (counter-clockwise, 3 ≤ p ≤ m, all v_k ≠ 0). Let ω_k ∈ (0, π)
   be the angle at 0 of the triangle Δ_k = (0, v_k, v_{k+1}) (indices mod p); Σ_k ω_k = 2π. Let ε_k be its angle
   at v_k; its angle at v_{k+1} is π − ω_k − ε_k.
4. K ⊆ v_k + C_k, C_k := cone(v_{k+1} − v_k, v_{k−1} − v_k), closed. From e^{zr}v_k ∈ K: z v_k ∈ C_k. Rotating so
   that v_k > 0: −v_k has direction π, v_{k+1} − v_k has direction π − ε_k (upper half plane, since
   arg(v_{k+1}/v_k) = ω_k ∈ (0, π)), v_{k−1} − v_k has direction π + (its angle) in the lower half plane, and z v_k
   has direction π − φ. Hence z v_k ∈ C_k forces φ ≤ ε_k for every k.
5. Law of sines in Δ_k: |v_{k+1}|/|v_k| = sin ε_k / sin(π − ω_k − ε_k) = g_k(ε_k), g_k(ε) := sin ε / sin(ω_k + ε)
   on (0, π − ω_k). The product of the ratios around the polygon is 1. (log g_k)′ = cot ε − cot(ω_k + ε) > 0, so g_k
   is increasing, and φ ≤ ε_k < π − ω_k gives 1 = Π g_k(ε_k) ≥ Π g_k(φ), i.e.
   sin^p φ ≤ Π_k sin(ω_k + φ), with every ω_k + φ ∈ (0, π).
6. log sin is concave on (0, π); Jensen with mean (1/p)Σ(ω_k + φ) = φ + 2π/p ∈ (0, π) gives sin φ ≤ sin(φ + 2π/p).
   For 0 < u < v < π, sin u ≤ sin v ⇔ u + v ≤ π (sin v − sin u = 2cos((u+v)/2) sin((v−u)/2)). Hence
   2φ + 2π/p ≤ π, i.e. y/x = tan φ ≤ cot(π/p) ≤ cot(π/m).

*General case.* In Frobenius normal form (simultaneous permutation of rows and columns) X is block triangular
with irreducible diagonal blocks; λ is an eigenvalue of a block B of size m_B with Perron root
μ_B ≤ s(X). A 1×1 block has a real eigenvalue, and an irreducible 2×2 Metzler block has discriminant
(B₁₁ − B₂₂)² + 4B₁₂B₂₁ ≥ 0, so m_B ≥ 3. The irreducible case gives
|Im λ| ≤ (μ_B − Re λ)cot(π/m_B) ≤ (s(X) − Re λ)cot(π/m). ∎

In A4 apply Lemma A to X = T_RR, m = n_R, λ = −a + ib, s(X) = −c: b ≤ (a − c)cot(π/n_R). Lemma A is the classical
Dmitriev–Dynkin/O'Cinneide sector statement; this appendix is an independent re-derivation, not a new result.

## Appendix B. Remarks

* Formula summary (normalized time): m_i = −β cot θ_i, m_* = (1 − β²)/2, ρ = (1 + β²)/2,
  W = β^n / Π_i sin θ_i, exits t = K·(0, 0, 1, W h_{n−4}, …, W h₀), h_k = ρ^{−3−k} c_k.
* Extremal case: at β = cot(π/n) the uniform cycle (all θ_i = 2π/n, all m_i = m_*) has
  b/(a − c) = cot(π/n), equality in Theorem 6; the polygon of Appendix A is then the regular n-gon.

## 6. Differences from the untrusted candidate

* The candidate's IVT starts at t = 0 and is stated for n ≥ 4; at n = 3, G(0) = 0. Lemma B1 uses
  t₀ = max(0, S − 2(π − φ)) and covers all n ≥ 3 uniformly (for n = 3, t₀ = 2φ > 0).
* Everything else in the candidate (angle choice ψ = π − 2φ, m_* = (1 − β²)/2, divisibility, exit formula
  t_j = K W h^{(n−j)}(m_*)/(n−j)!, the generating function, the sign test cos(ψ/2) − cos((k + 3/2)ψ), v₁ = 1 and
  α = e₁) was re-derived and agrees. The candidate gave no lower-bound applicability argument; A2–A3 supply it.
