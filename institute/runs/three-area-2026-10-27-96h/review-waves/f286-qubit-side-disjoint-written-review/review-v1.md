# f286 disjoint written review (review-v1) — Reviewer ReviewF286Qubit

## 0. Review envelope

- Packet: `literal-packet-v1.md`, SHA-256 `f092268ab534ad84bb8267037352f5a54a89b3b7b292c36583f419c83f4bdca9`, 9165 bytes, 121 LF (verified against freeze-receipt-v1 at clock 2026-10-30T03:36:04-0700 PDT, together with manifest SHA `c6da3726a6794b22767fe1e6dba5113f9c90461670277aa61087883953c588f9`).
- Read completeness: entire packet read raw in windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–121 (contiguous; covers packet lines 1–121 = source S1 lines 1–119 plus the two packet header/footer lines). No elision found. Line citations below are packet `S1|L|` lines.
- Status-only controls (manifest list) read for status only; no excluded links followed. The f284 review body/outcomes and, per the 2026-10-30 status notice received mid-review, all f285 review/disposition/outcome material were NOT accessed and are NONINPUT to this review.
- Mode: WRITTEN_ONLY. No scientific code, CAS, interpreter, solver, enumeration or replay was run; no selected concrete/numerical instance was constructed privately or publicly. Every argument below is general symbolic algebra over free complex parameters. The only parametric families appearing are (a) verification of the packet's own line-41 essentiality claim and (b) a refutation of the literal unrestricted-trace reading of line 45 — both symbolic in free parameters with no numerical values chosen.
- Pre-body administrative ACK sent to Main before any packet read (clock 2026-10-30T03:36:04-0700 PDT).

## 1. Imports (exact scope, all standard finite-dimensional complex linear algebra)

1. Schur unitary triangularization of a complex 2×2 matrix (packet L21).
2. Singular value decomposition; `|Tr Z| ≤ ||Z||₁ ≤ √(rank Z)·||Z||_F` with its equality characterization (L37, L103).
3. Ky Fan maximum principle / von Neumann trace duality in the two forms used (L51, L71): `√S₂(Y) = max_{rank R≤2, ||R||_F=1} |Tr(R†Y)|` with `S₂(Y) := s₁(Y)²+s₂(Y)²`, and `Tr(PM) ≤ Σ_{i≤rank P} λᵢ(M)` for `M ⪰ 0`, `P` a projection.
4. Frobenius inner product `⟨X,Z⟩ = Tr(X†Z)` (conjugate-linear in the first argument, linear in the second — the convention used throughout this review and consistent with the packet); unitary invariance; `||A⊗B||_F² = ||A||_F²||B||_F²`; partial-trace conventions and identities `Tr_n(A⊗B) = Tr(B)A`, `Tr(R†(C⊗I_n)) = Tr(C·Tr_n R†)`, `Tr(R†(I₂⊗D)) = Tr((Tr_2 R)†D)`, `Tr(P(M⊗I_B)) = Tr(ρ_A M)`.
5. Cauchy–Schwarz (ℂⁿ, Frobenius, and ℓ₂ on ℝ³) and AM–GM / nonnegativity of `ux²+vy²−2√(uv)xy` for `u,v>0` (L87).
6. Support lemma for `P ⪰ 0`: `ker(Tr_B P) ⊗ Cⁿ ⊆ ker P` (both sides), hence `P = (Π⊗I)P(Π⊗I)` for any projection `Π ⊇ ran Tr_B P` (implicit at L61).
7. Rank algebra: rank of a block/compression ≤ rank of the matrix; rank invariance under invertible column/row swaps; `rank [[X,Y],[Z,W]] = rank X` ⟹ ∃B,C with `Y = XB`, `Z = CX`, `W = CXB` (L107–109).
8. Nilpotent ⟹ traceless; a matrix annihilated by a polynomial with distinct roots is diagonalizable on that support (L113).

No other mathematics is used; nothing outside the packet and this import list enters the verdicts.

## 2. Written reconstruction

### 2.1 Qubit hollowing lemma (L21)

Let `M ∈ M₂(C)`, `Tr M = 0`. Schur gives `Ũ M Ũ† = [[λ,z],[0,−λ]] =: M̃` for some unitary `Ũ`, since the traceless diagonal must be `{λ,−λ}` (any `λ ∈ C`). For a unit vector `x = e^{iψ}(cosθ, e^{iφ}sinθ)`, `θ∈[0,π/2]`, the expectation is phase-invariant and computes to `⟨x|M̃|x⟩ = λcos(2θ) + (z e^{iφ}/2)sin(2θ)` — verified by direct multiplication (`M̃x = (λcosθ + ze^{iφ}sinθ, −λe^{iφ}sinθ)`, then `cosθ(λcosθ+ze^{iφ}sinθ) + e^{−iφ}sinθ(−λe^{iφ}sinθ)`). Writing `λ = |λ|e^{iβ}`, `z = |z|e^{iγ}`, choose `φ := β+π−γ` so that `ze^{iφ}` has phase opposite to `λ`; then the expectation is `e^{iβ}(|λ|cos2θ − (|z|/2)sin2θ)`, which vanishes for `2θ = arctan(2|λ|/|z|) ∈ [0,π/2)`, i.e. `θ ∈ [0,π/4)`. If `λ = 0` take `θ = 0` (any `φ`); if `z = 0` take `θ = π/4`. The orthogonal complement `x⊥` then satisfies `⟨x⊥|M̃|x⊥⟩ = Tr M̃ − ⟨x|M̃|x⟩ = 0`. So `M` is unitarily similar to a zero-diagonal matrix. **Correct** (the phrase at L21 "Choose φ opposite the phase of λ" is to be read as "choose φ so that the phase of `ze^{iφ}` is opposite to that of `λ`"; with that reading — the only one that makes the magnitudes cancellable — the lemma stands).

### 2.2 The exact all-n block identity (2.2) (L25–33)

Let `R ∈ M(C²⊗Cⁿ)` have qubit blocks `P,Q,T,S ∈ M_n(C)`. Then, for every `n ≥ 1` and arbitrary complex blocks (no rank or trace assumption needed for the identity itself):

- `Tr_n R = [[TrP, TrQ],[TrT, TrS]]`, so `||Tr_n R||_F² = |TrP|²+|TrQ|²+|TrT|²+|TrS|²`;
- `Tr_2 R = P+S`, so `||Tr_2 R||_F² = ||P||²+||S||²+2Re Tr(P S†)`;
- `|Tr R|²/2 = |TrP+TrS|²/2`.

Hence
`2||R||² − LHS(1.1) = ||P−S||² + 2||Q||²+2||T||² − |TrQ|²−|TrT|² − |TrP|²−|TrS|² + |TrP+TrS|²/2`,
and since `−|a|²−|b|²+|a+b|²/2 = −|a−b|²/2` for `a,b ∈ C` (expand both sides: each equals `−(|a|²+|b|²)/2 + Re(āb)`), this is exactly
`||P−S||² − |Tr(P−S)|²/2 + 2||Q||² − |TrQ|² + 2||T||² − |TrT|²`, i.e. (2.2). **Exact identity, verified algebraically.** (Independently re-verified symbolically at `n=1`, where blocks are scalars `p,q,t,s ∈ C`: LHS `= |p|²+|q|²+|t|²+|s|²−|p+s|²/2`, RHS `= |p−s|²/2+|q|²+|t|²`, and `|p|²+|s|²−|p+s|²/2 = |p−s|²/2` for all complex `p,s`.)

### 2.3 Proof of (1.1) (L23, L35–39) and essentiality of the rank bound (L41)

Conjugating `R` by a qubit unitary `U⊗I_n` preserves `rank R`, `||R||_F`, `Tr R`, `||Tr_2 R||_F`, and `||Tr_n R||_F` (it conjugates `Tr_n R` and fixes `Tr_2 R`), and (1.1) is invariant under this. Choose `U` hollowing the traceless part of `Tr_n R` (§2.1); in that basis `Tr(P−S) = 0` (this is (2.1); indeed `Tr_n R = (TrR/2)I₂ + hollow`). The first bracket of (2.2) is then `||P−S||² ≥ 0`. The blocks `Q = (⟨e₁|⊗I)R(|e₂⟩⊗I)` and `T = (⟨e₂|⊗I)R(|e₁⟩⊗I)` are compressions, so `rank Q, rank T ≤ rank R ≤ 2`; for any matrix `Z`, `|Tr Z| ≤ Σᵢsᵢ(Z) = ||Z||₁` (from `Z = Σ sᵢuᵢvᵢ†`, `Tr Z = Σ sᵢ⟨vᵢ,uᵢ⟩`) and `||Z||₁² ≤ rank(Z)||Z||_F²` (Cauchy–Schwarz on singular values), so `|Tr Z|² ≤ 2||Z||_F²` for `rank Z ≤ 2`. Hence the remaining two brackets of (2.2) are nonnegative and `LHS(1.1) ≤ 2||R||_F²`. **(1.1) holds for every `n ≥ 1` and every complex `R` of rank ≤ 2** (rank 0 and 1 included; `n=1` included, where it reduces to `|TrR|² ≤ 2||R||²`). Boundaries check out.

Essentiality (L41): for nonzero traceless `C ∈ M₂`, `R = C⊗I₃ ∈ M(C²⊗C₃)` has `rank R = 3·rank C ≥ 3`, `Tr_3 R = 3C`, `Tr_2 R = Tr(C)⊗I₃ = 0`, `Tr R = 0`, `||R||² = 3||C||²`; so LHS(1.1) `= 9||C||²` against RHS `6||C||²` for every `C ≠ 0` in the family — the rank hypothesis cannot simply be dropped. **Correct symbolic observation.**

### 2.4 Channel decomposition, weights, and the equivalence (1.1) ⟺ (3.1) (L45–59)

Fix `n`, traceless `C ∈ M₂(C)`, traceless `D ∈ M_n(C)` (see Finding M1 on the unstated `Tr D = 0`), `t ∈ C`, and `Y = tI_{2n} + C⊗I_n + I₂⊗D`. Block expansion gives, for every `R`,
`Tr(R†Y) = t·conj(Tr R) + ⟨(Tr_n R)_0, C⟩ + ⟨(Tr_2 R)_0, D⟩`,
where `(·)_0` is the traceless part; the two trace-channel terms drop out precisely because `Tr C = Tr D = 0` (for the `t`-channel, `t Tr R† = t·conj(Tr R)` — the conjugation convention). Formalize in the orthogonal direct sum `ℂ ⊕ M₂⁰ ⊕ M_n⁰` (Frobenius): with
`U' := (Tr R/√(2n), (Tr_n R)_0/√2, (Tr_2 R)_0/√2)`, `W' := (√(2n)·t, √2·C, √2·D)`,
one has `⟨U',W'⟩ = Tr(R†Y)`, `||W'||² = 2n|t|²+2||C||²+2||D||²` (the "weighted source"), and
`||U'||² = |Tr R|²/(2n) + ||(Tr_n R)_0||²/2 + ||(Tr_2 R)_0||²/2` (the packet's L55 expression).
Cauchy–Schwarz gives `|Tr(R†Y)|² ≤ (2n|t|²+2||C||²+2||D||²)·||U'||²` for every `R` — this is the correct content of the compressed L51–55 sentence. Moreover `||U'||²` is **exactly half of LHS(1.1)** for every `R` (no rank assumption): using `||Tr_n R||² = |TrR|²/2 + ||(Tr_n R)_0||²` and `||Tr_2 R||² = |TrR|²/n + ||(Tr_2 R)_0||²`, LHS(1.1) `= ||(Tr_n R)_0||² + ||(Tr_2 R)_0||² + |TrR|²/n = 2||U'||²`. This verifies L57's "expands to one half of the left side of (1.1)" as an exact identity.

Equivalence, both directions, within the class `Tr C = Tr D = 0`:
(⟹) For `||R||_F = 1`, `rank R ≤ 2`: `|Tr(R†Y)|² ≤ (source)·(LHS(1.1)/2) ≤ source` by (1.1); maximizing over the sphere and using the Ky Fan duality `√S₂(Y) = max |Tr(R†Y)|` (L51, Import 3 — attained by the top-two singular pair, phases aligned) yields (3.1).
(⟸) Given `R` with `rank R ≤ 2`, `||R|| = 1`, set for any `σ ∈ C\{0}`: `t = σTr R/(2n)`, `C = σ(Tr_n R)_0/2`, `D = σ(Tr_2 R)_0/2` (both traceless). Then `Tr(R†Y) = σ||U'||²` and `source = |σ|²||U'||²`, so `S₂(Y) ≥ |Tr(R†Y)|² = |σ|²||U'||⁴` while (3.1) gives `≤ |σ|²||U'||²`; hence `||U'||² ≤ 1 = ||R||²`, i.e. (1.1) for `R`, and rescaling gives general `R`. So (1.1) and (3.1) are **exactly equivalent** as "all-variable" statements over traceless `C,D` and arbitrary complex `t`, for each `n`. L57's claim is correct in this class; the literal hypothesis line (L45, "traceless `C∈M2(C)`, `D∈Mn(C)`") leaves `Tr D = 0` unstated, and without it (3.1) is false in general (Finding M1, with a parametric family).

### 2.5 The lift: support, leakage identity, and the exact gap decomposition (3.2) (L61–79)

Let `P` be a rank-two projector on `C⁴⊗C⁴` with `ρ_A := Tr_B P` of rank ≤ 2 (no assumption on the other marginal, separability, or PPT). Pick a rank-2 projection `Π` on the A factor with `ran ρ_A ⊆ ran Π` (possible; if `rank ρ_A = 1` the choice is non-unique and any choice works). By the support lemma (Import 6) — for `w ⊥ ran ρ_A`, `⟨w⊗eᵢ|P|w⊗eᵢ⟩ = ⟨w|ρ_A|w⟩ = 0` forces `√P|w⊗eᵢ⟩ = 0`, hence `P(w⊗ψ) = 0` and by self-adjointness also the adjoint — `P = (Π⊗I₄)P(Π⊗I₄)`. Fix an A-basis with `ran Π = span(e₁,e₂)` (a unitary change of basis on the A side preserves `Tr(PX†X)`, `L`, tracelessness, and normality of `A²`, `B²`). Write
`A = [[αI₂+C, A₁₂],[A₂₁, A₂₂]]`, `Tr C = 0` (any 2×2 block decomposes so, with `α = Tr(block₁₁)/2`), `B` arbitrary traceless 4×4, `X = A⊗I₄+I₄⊗B`, `Y := αI₈ + C⊗I₄ + I₂⊗B = A₁₁⊗I₄ + I₂⊗B` on `ranΠ⊗C⁴ ≅ C²⊗C⁴`.

Compression identity: since `P = (Π⊗I)P(Π⊗I)`, `Tr(PX†X) = Tr(P·(Π⊗I)X†X(Π⊗I))`. Expanding `X†X = (A†A)⊗I + I⊗B†B + A†⊗B + A⊗B†`, the compressions are `(ΠA†AΠ)⊗I₄` (whose (1,1) block is `A₁₁†A₁₁ + A₂₁†A₂₁`), `I₂⊗B†B`, `A₁₁†⊗B`, `A₁₁⊗B†`; the three `B`-terms together with the `A₁₁†A₁₁`-term are exactly `Y†Y`. Hence
`Tr(PX†X) = Tr(PY†Y) + Tr(ρ A₂₁†A₂₁)`, with `ρ := ρ_A|_{ranΠ} ⪰ 0`, `Tr ρ = 2`. (L69.) **Exact; verified.** This is L67's "inside output and `A₂₁` leakage output occupy orthogonal local A subspaces": in `X†X` the leakage enters the seen block only through `A₂₁†A₂₁⊗I₄`, with no cross terms (cross terms of `A₁₂`/`A₂₁` live in blocks `P` does not see).

Bounds: `Tr(PY†Y) = ||YP||_F² = ⟨P, Y†Y⟩ ≤ S₂(Y)` (Ky Fan max principle, `rank P = 2`; Import 3), and (3.1) at `n = 4`, `t = α`, `D = B` (both traceless ✓) gives `S₂(Y) ≤ 8|α|²+2||C||²+2||B||²` (L71). Trace zero: `0 = Tr A = 2α + 0 + Tr A₂₂` gives `Tr A₂₂ = −2α`, hence `4|α|² = |Tr A₂₂|² ≤ 2||A₂₂||²`, i.e. `||A₂₂||² ≥ 2|α|²`; and `ρ ⪯ 2I₂` (2×2 psd of trace 2 has eigenvalues in [0,2]).

Exact decomposition (3.2): using `||A||² = 2|α|²+||C||²+||A₁₂||²+||A₂₁||²+||A₂₂||²` (the cross term `⟨αI₂,C⟩ = ā Tr C = 0`) and `2||A₂₁||² − Tr(ρA₂₁†A₂₁) = Tr((2I₂−ρ)A₂₁†A₂₁)`:
`2L − Tr(PX†X) = 2||A₁₂||² + Tr[(2I₂−ρ)A₂₁†A₂₁] + 2(||A₂₂||²−2|α|²) + [8|α|²+2||C||²+2||B||²−Tr(PY†Y)]`. **Exact identity; term-by-term accounting verified.** All four brackets are ≥ 0 (`2I₂−ρ ⪰ 0` and `Tr(HZ†Z) = ||ZH^{1/2}||² ≥ 0`; the last bracket `≥ S₂(Y) − Tr(PY†Y) ≥ 0`). Hence `Tr(PX†X) ≤ 2L`: **(1.2) holds whenever the A-local marginal rank is ≤ 2, for arbitrary complex traceless `A,B`, with no hypothesis on the other marginal, separability or PPT.**

Factor exchange (L79): the swap unitary `S` on `C⁴⊗C⁴` maps `(P, A, B)` to `(SPS, B, A)` with `X ↦ SXS†`, `L` symmetric, `Tr(PX†X)` invariant, and "A-marginal rank ≤ 2" ↔ "B-marginal rank ≤ 2"; normality of `A²`/`B²` is preserved. So the B-local case follows identically. **(1.2) fully SUPPORTED.**

### 2.6 Equality analysis: a normal local square is forced (L83–115)

**(i) Rank-one marginal (L83–87).** If `Tr_B P` has rank 1, then `ρ_A = 2|v⟩⟨v|` (trace 2) and the support lemma gives `P = |v⟩⟨v|⊗M`, `M ⪰ 0`; `P² = P` gives `M² = M` and `Tr M = Tr P = 2`, so `M = Q`, a rank-2 projection ("rank Q = 2" ✓); the B-marginal-rank-one case is the swap. For the first orientation put `a = ⟨v,Av⟩`, `b = Tr(QB)`. Expanding `Tr(PX†X) = 2||Av||² + ||BQ||² + 2Re(āb)` (via `Tr(P(A†⊗B)) = āb`, `Tr(P(A⊗B†)) = a·b̄`, `Tr(P(I⊗B†B)) = Tr(QB†B) = ||BQ||²`, `Tr(P(A†A⊗I)) = 2⟨v|A†A|v⟩`):
- `Tr A = 0 = a + Σ_{i≤3}⟨eᵢ,Aeᵢ⟩` over an ONB of `v⊥` ⟹ `|a|² ≤ 3Σ_{i≤3}|⟨eᵢ,Aeᵢ⟩|² ≤ 3Σ_{i≤3}||Aeᵢ||² = 3(||A||²−||Av||²)`, i.e. `||A||²−||Av||² ≥ |a|²/3` (L85, ✓ "elementary Cauchy", dim `v⊥ = 3`).
- `b = Tr(QB)`, `Tr((I−Q)B) = −b`, both `Q` and `I−Q` rank 2 ⟹ `||BQ||² = Σ_{i≤2}||Beᵢ||² ≥ (|b|²)/2` and `||B(I−Q)||² ≥ |b|²/2` (L85, ✓).
Then, with `2||B||² − ||BQ||² = ||BQ||² + 2||B(I−Q)||²` and `−2Re(āb) ≥ −2|a||b|`:
`2L − Tr(PX†X) ≥ (2/3)|a|² + (3/2)|b|² − 2|a||b| ≥ 0`, the last by AM–GM since `√((2/3)(3/2)) = 1` (L87 ✓). The gap is a sum of three nonnegative brackets `[2(||A||²−||Av||²) − (2/3)|a|²]`, `[||BQ||²−|b|²/2] + [2||B(I−Q)||² − |b|²]`, `[(2/3)|a|²+(3/2)|b|²−2|a||b|]`; gap `= 0` forces equality in both B trace inequalities, which forces (equality in both Cauchy–Schwarz steps: diagonal entries equal and phases aligned; `|⟨eᵢ,Beᵢ⟩| = ||Beᵢ||` forcing `Beᵢ ∥ eᵢ`) `B = (b/2)Q ⊕ (−b/2)(I−Q) = (b/2)(2Q−I₄)` — normal (scalar × Hermitian), so `B²` is normal (L87 ✓; the edge `b = 0` gives `B = 0`). **SUPPORTED.**

**(ii) Rank-exactly-two A marginal: saturation and source recovery (L89–97).** `ρ` 2×2 psd of trace 2 and rank 2 has both eigenvalues in `(0,2)`, so `2I₂−ρ ≻ 0` (L89 ✓ — if an eigenvalue were 2 the other would be 0). If the total gap (3.2) vanishes, each bracket vanishes: `A₁₂ = 0`; `Tr((2I₂−ρ)A₂₁†A₂₁) = 0` with `2I₂−ρ ≻ 0` forces `A₂₁ = 0` (write `Tr(HZ†Z) = ||ZH^{1/2}||²`, `H^{1/2}` invertible); `||A₂₂||² = 2|α|² = |Tr A₂₂|²/2` is equality in the rank-2 trace bound for the 2×2 matrix `A₂₂`, forcing `A₂₂ = (Tr A₂₂/2)I₂ = −αI₂` (L91 ✓, by the equality case of Import 2 as at L103); and `Tr(PY†Y) = 8|α|²+2||C||²+2||B||²`, so both Ky Fan inequalities are equalities (L93 "saturated" ✓).

Put `R := YP` (an operator on `C²⊗C₄`, `rank R ≤ rank P = 2`). Then `Tr(R†Y) = Tr(PY†Y) = ||YP||² = ||R||² =: m`. The chain of §2.4 gives `m² = |Tr(R†Y)|² ≤ (source)·||U'(R)||²` with `source = 8|α|²+2||C||²+2||B||² = m`, while (1.1) applied to `R` gives `||U'(R)||² ≤ ||R||² = m`. Hence `||U'(R)||² = m`: **equality in (1.1) for this `R`**; and equality in the Cauchy–Schwarz pairing forces `W' = e^{iθ}U'` with `θ` pinned to 0 because `⟨U',W'⟩ = m > 0` real (L97's "proportionality constant is exactly one" ✓). Componentwise: `√8·t = Tr R/√8`, `√2·C = (Tr₄R)_0/√2`, `√2·D = (Tr₂R)_0/√2`, i.e. `t = TrR/8`, and **(4.1)** `C = (Tr₄R)_0/2`, `B = (Tr₂R)_0/2` (L95 ✓, conjugation conventions consistent: the `t`-channel pairs `t` with `conj(Tr R)`; `C` and `B` carry no conjugation). Zero source: if `R = 0` then `m = 0` and the saturated bracket forces `α = C = B = 0`, and then `A = A₁₁⊕A₂₂ = 0⊕0 = 0`, so `A = B = 0` and both squares are (zero, hence) normal — L97 "trivial" ✓. Note `R = 0` iff `YP = 0` iff `Tr(PY†Y) = 0`, so the nonzero case is exactly `m > 0`. **SUPPORTED.**

**(iii) Hollowed block structure and the nuclear-norm equality case (L99–103).** Conjugating the whole equality configuration by a qubit unitary `U⊗I₄` on the A-support factor preserves everything load-bearing: `Tr(PX†X)` (A-side unitary covariance), `L`, `rank R`, and — decisive for (4.1) — `Tr₂((U⊗I)R(U†⊗I)) = Tr₂ R`, so the recovered `B` is unchanged, while `Tr₄R` conjugates and `C` conjugates with it; normality statements about `A²`, `B²` are unitary-similarity invariant. Hence WLOG the traceless part of `Tr₄R` is hollow (§2.1). Equality in (2.2) for `R` (from (ii)) forces each bracket to vanish: `||P−S||² = 0`, i.e. the two diagonal blocks coincide (`=: G`), and `2||Q||² = |TrQ|²`, `2||T||² = |TrT|²` (L101: `R = [[G,Q],[T,G]]` ✓ — note `Q`,`T` here are 4×4 blocks, an overload of the letter `Q` used for the B-side projection at L83; context separates them).

Nuclear equality (L103): for `Z` with `rank Z ≤ 2`, `|Tr Z| ≤ ||Z||₁ ≤ √2||Z||_F`; equality `|TrZ|² = 2||Z||²` with `Z ≠ 0` forces (α) `(s₁+s₂)² = 2(s₁²+s₂²)`, i.e. `s₁ = s₂ > 0` (a rank-1 `Z` would give `s₁² < 2s₁²`), so `rank Z = 2`; and (β) `|Σ sᵢ⟨vᵢ,uᵢ⟩| = Σ sᵢ` with `|⟨vᵢ,uᵢ⟩| ≤ 1`, forcing `vᵢ = e^{iβᵢ}uᵢ` with all phases aligned. Hence `Z = λ(u₁u₁†+u₂u₂†) = λΠ`, `λ ∈ C\{0}`, `Π` a rank-2 orthogonal projection (or `Z = 0`). **L103 verified** ("its two singular values equal and its left and right singular directions equal up to a common phase" ✓). So each of `Q, T` is `0` or `λΠ`.

**(iv) The rank-two pivot (L105–111).** If `Q = T = 0`: `Tr₄R = (TrG)I₂`, so `(Tr₄R)_0 = 0` and (4.1) gives `C = 0`; then `A = αI₂ ⊕ (−αI₂)`, which is normal (indeed `A² = α²I₄`) — L105 ✓.

Otherwise say `Q = λΠ ≠ 0` (`T ≠ 0, Q = 0` symmetric by the row-swap). Swapping the two block columns is right-multiplication by an invertible permutation, so `M' := [[λΠ, G],[G, T]]` still has `rank M' ≤ 2`; its top-left block has rank 2, so `rank M' = 2 = rank(λΠ)`. The pivot lemma (Import 7): `rank [[X,Y],[Z,W]] = rank X` implies `Y = XB`, `Z = CX`, `W = CXB` (from `rank[X Y] = rank X` and `rank[[X],[Z]] = rank X`, then `W − CXB = 0` since the reconstructed product `[[I],[C]]X[I,B]` already attains rank 2). Applied: `G = λΠB` (so `ΠG = G`), `G = CλΠ` (so `GPi = G`), `T = CG`. Then `G = ΠGΠ` and, using `CΠ = ΠB` (from `λCΠ = λΠB = G`),
`G² = (λCΠ)(λΠB) = λ²CΠB = λ·CG = λT`, i.e. **`T = λ⁻¹G²`** — (4.2) verified. If `T = 0` then `G² = 0`. If `T = μΠ′ ≠ 0`, then `T = λ⁻¹G² = λ⁻¹ΠG²Π` (using `G = ΠGΠ`) has `ran T ⊆ ran Π`; but `ran Π′ = ran T`, and `Π′, Π` are both rank-2 projections, so `Π′ = Π` and `G² = λμΠ` — L111 ✓. (Internal consistency check, symbolic: for `G = gΠ` one gets `R = [[g,λ],[λ⁻¹g²,g]]⊗Π` with `det[[g,λ],[λ⁻¹g²,g]] = g² − g² = 0`, so `rank R = 2` — the derived structure is non-vacuous.)

**(v) `B²` normal in every nonzero-`Q/T` equality case (L113).** From the block form, `Tr₂R = 2G`, so `(Tr₂R)_0 = 2G − (TrG/2)I₄` and (4.1) gives `B = G − (TrG/4)I₄` (L113 ✓; note this uses the hollowed basis, legitimate because `Tr₂R` is invariant under qubit conjugation, per (iii)).
- If `G² = 0`: `G` is nilpotent, `Tr G = 0`, `B = G`, `B² = 0` — normal ✓.
- If `G² = κΠ`, `κ ≠ 0`: on `ran Π`, `G² = κI₂` and `G` is zero off `ran Π` (`G = ΠGΠ`); `z² − κ` has the two distinct roots `±√κ`, so `G|_{ranΠ}` is diagonalizable with eigenvalues in `{√κ, −√κ}`. If they are opposite, `Tr G = 0` and `B = G`, `B² = G² = κΠ`, and `κΠ` is normal (`ΠΠ† = Π`). If they coincide, `G|_{ranΠ} = ±√κ·I₂`, i.e. `G = ±√κΠ`, `Tr G = ±2√κ`, and `B = ±√κ(Π − I₄/2)` — a scalar times a Hermitian matrix, hence normal (indeed `(Π−I/2)² = I₄/4`). **In every subcase `B²` is normal** (L113 ✓). Note the first subcase does not claim `B` normal — only `B²`, which is all the theorem needs.

**(vi) Conclusion (L115).** Across all cases — rank-one marginal (⟹ `B` or, by swap, `A` normal), rank-exactly-two marginal (⟹ `A = B = 0`, or `A` normal via `Q = T = 0`, or `B²` normal), and the factor-exchanged mirrors — **equality in (1.2) forces `A²` or `B²` normal.** The contrapositive gives strictness of `Tr(PX†X) < 2L` whenever both `A²` and `B²` are nonnormal, under the same marginal hypothesis. Nothing in the argument presumes block-diagonality of `A` before equality forces it (L115 ✓ — `A₁₂, A₂₁ = 0` were derived, not assumed). **Strictness claim SUPPORTED.**

### 2.7 The "consequently" sentence and scope statements (L15, L17, L119)

L15's consequence: if the pair `(A,B)` admits a maximizing rank-two projector `P*` for `Tr(P X†X)` (equivalently, `P*` spans the top-two right singular space of `X` — `max_{rank-2 proj} Tr(PX†X) = S₂(X)` by the Ky Fan max principle) whose either local marginal has rank ≤ 2, then `S₂(X) = Tr(P*X†X) ≤ 2L` by (1.2), strictly when both squares are nonnormal. The inference is valid in-packet given the standard Ky Fan identity; the identification of `S₂(A⊗I₄+I₄⊗B) ≤ 2L` with the external name "T2" is an import from outside the packet (T2 is not defined in-packet; the packet itself defers "unrestricted T2" at L17/L119). **SUPPORTED as a conditional with that import boundary (Finding M5).** The remaining scope sentences (L17: unhandled domain = both local marginal ranks ≥ 3, matching exactly the proof's coverage; no counterexample asserted there; no η, T3/Z2/q3, physical/η counterexample, source-correctness, independent-family/human/formal or novelty claims; L119 repeats this) are **consistent with the reconstruction and honestly stated. SUPPORTED.**

## 3. Per-claim verdicts

| # | Claim (packet lines) | Verdict |
|---|---|---|
| V1 | Rank-two partial-trace inequality (1.1), all `n≥1`, all complex `R`, `rank R ≤ 2` (L7–9) | **SUPPORTED** (§2.1–2.3; quantifiers, complex phases, rank-0/1, `n=1` boundaries all check) |
| V2 | Hollowing lemma (L21) | **SUPPORTED** (§2.1; wording note M3) |
| V3 | Exact block identity (2.2) (L27–33) | **SUPPORTED** — exact for all `n`, all complex blocks, independent of rank/trace hypotheses (§2.2) |
| V4 | Trace bound `|TrZ|² ≤ rank·||Z||²`, block ranks ≤ 2, conclusion (L35–39) | **SUPPORTED** (§2.3) |
| V5 | Essentiality of rank restriction, symbolic family `C⊗I₃` (L41) | **SUPPORTED** (`9||C||²` vs `6||C||²`, rank ≥ 3 — verified symbolically) |
| V6 | Ky Fan/Frobenius duality `√S₂(Y) = max…` (L49–51) | **SUPPORTED** (standard import; statement consistent) |
| V7 | Channel weights; "expands to one half of LHS(1.1)" (L53–57) | **SUPPORTED** in content — the L55 expression is exactly `½·LHS(1.1)` for every `R`, and the pairing bound is the Cauchy–Schwarz of §2.4; wording garbled (M2), `Tr D = 0` implicit (M1) |
| V8 | Weighted Ky Fan bound (3.1) and equivalence with (1.1) (L57–59) | **SUPPORTED** within the class `Tr C = Tr D = 0`, `t ∈ C` arbitrary, per `n` (both directions reconstructed, §2.4); literal unrestricted-`D` reading of L45 is false (M1) |
| V9 | Support choice, block form of `A`, `Y` (L61–65) | **SUPPORTED** (support lemma + A-basis change; legitimate) |
| V10 | Orthogonal-subspace statement and exact leakage identity (L67–69) | **SUPPORTED** — `Tr(PX†X) = Tr(PY†Y) + Tr(ρA₂₁†A₂₁)` exact (§2.5) |
| V11 | `Tr(PY†Y) ≤ S₂(Y) ≤ 8|α|²+2||C||²+2||B||²`; `Tr A₂₂ = −2α`, `||A₂₂||² ≥ 2|α|²`, `ρ ≤ 2I₂` (L71) | **SUPPORTED** (all four verified) |
| V12 | Exact gap decomposition (3.2), all brackets ≥ 0 (L73–77) | **SUPPORTED** — exact identity, term-by-term (§2.5) |
| V13 | Original-pair consequence (1.2), either marginal ≤ 2, arbitrary complex traceless `A,B` (L11–13, L79) | **SUPPORTED** (A-side + factor exchange; no assumption on other marginal/PPT ✓) |
| V14 | Rank-one marginal structure `|v⟩⟨v|⊗Q`, `rank Q = 2` (L83) | **SUPPORTED** |
| V15 | Cauchy bounds `|a|²/3`, `|b|²/2`, gap `≥ (2/3)|a|²+(3/2)|b|²−2|ab| ≥ 0`; equality ⟹ `B = (b/2)(2Q−I₄)` normal (L85–87) | **SUPPORTED** (including `b = 0` edge) |
| V16 | Rank-exactly-two: `2I₂−ρ ≻ 0`; equality ⟹ `A₁₂=A₂₁=0`, `A₂₂=−αI₂`, saturation (L89–93) | **SUPPORTED** |
| V17 | Source recovery (4.1) with proportionality constant exactly 1; zero-source trivial (L93–97) | **SUPPORTED** (chain and phase-pinning reconstructed; zero source ⟹ `A=B=0`) |
| V18 | Hollowed `R = [[G,Q],[T,G]]`; `Q,T ∈ {0} ∪ {λΠ}` via nuclear-norm equality (L99–103) | **SUPPORTED** (equality case fully characterized; notation overload note) |
| V19 | `Q=T=0` ⟹ `C=0`, `A` normal (L105) | **SUPPORTED** (`A = αI₂⊕(−αI₂)`) |
| V20 | Rank-two pivot (4.2) `G=ΠGΠ`, `T=λ⁻¹G²`; `T=0` ⟹ `G²=0`; `T=μΠ′≠0` ⟹ `Π′=Π`, `G²=λμΠ` (L107–111) | **SUPPORTED** (pivot lemma + `CΠ=ΠB` computation; symmetric case covered) |
| V21 | `B = G−(TrG/4)I₄`; `G²=0` or `G²=κΠ` ⟹ `B²` normal in every case (L113) | **SUPPORTED** (distinct-roots analysis incl. coincident-eigenvalue subcase) |
| V22 | Equality ⟹ `A²` or `B²` normal; contrapositive strictness for both squares nonnormal (L115, L15 sentence 2) | **SUPPORTED** (case union complete; contrapositive valid) |
| V23 | "Consequently … satisfies T2, strictly on the both-squares-nonnormal complement" (L15 sentence 3) | **SUPPORTED as conditional** — in-packet derivation via Ky Fan max identity; "T2" is an external import (M5) |
| V24 | Scope boundaries (L17, L119) | **SUPPORTED** (match proof coverage; no η/global-T2/novelty assertions) |
| V25 | Methodology self-description (L3) | Consistent with the reconstructed proof; a process statement, not graded mathematically |

## 4. Findings

No FATAL and no MAJOR mathematical findings. The reconstruction is complete and every load-bearing step closes.

- **M1 (MINOR; L45 / (3.1)).** The hypothesis line reads "For traceless `C∈M2(C)`, `D∈Mn(C)` and `t∈C`" — the proof of (3.1) and of the channel split requires `Tr D = 0` (the `t`-channel cross term `⟨tI, I⊗D⟩ = 2t̄TrD` and the `R`-trace channel `⟨(TrR/n)I_n, D⟩` otherwise do not vanish). Under the literal unrestricted-`D` reading, (3.1) is false in general: parametrically, at `n = 1`, `C = 0`, `D = t ≠ 0`, one gets `Y = 2tI₂` with `S₂(Y) = 8|t|²` against the claimed bound `2|t|²+2|t|² = 4|t|²`. Harmless to the theorems: every use (L63–71, `D = B` traceless) and the equivalence direction (which constructs traceless `C,D`) lies in the traceless class. Fix: state `Tr D = 0` explicitly at L45.
- **M2 (MINOR; L53–55).** "The squared dual norm of the weighted source `2n|t|²+2||C||²+2||D||²` **is** `|Tr R|²/(2n)+…`" is garbled: a source-side constant cannot equal an `R`-dependent functional. The correct, verified content: with `U'`, `W'` as in §2.4, `Tr(R†Y) = ⟨U',W'⟩`, `||W'||² =` the source weight, `||U'||² =` the L55 expression `≡ ½·LHS(1.1)` exactly, and Cauchy–Schwarz gives the pairing bound. The subsequent derivation (L57–59) is correct under this reading.
- **M3 (MINOR, wording; L21).** "Choose `φ` opposite the phase of `λ`" must be read as choosing `φ` so that `ze^{iφ}` has phase opposite to `λ` (`φ = argλ − argz + π`); then `tan2θ = 2|λ|/|z|` pins `θ ∈ [0,π/4]`, with `λ = 0` / `z = 0` immediate as stated. Under this reading the lemma is fully correct.
- **M4 (MINOR, compression; L99).** Hollowing after (4.1) is legitimate because the whole equality configuration is covariant under qubit unitaries on the chosen A-support (`Tr(PX†X)`, `L`, normality of `A²`,`B²` invariant; `Tr₂R` invariant so the recovered `B` is unchanged, `Tr₄R` and `C` conjugate together). The packet compresses this to "as in Section 2". Correct but understated; also the A-basis choice at L61 ("write `A=[[…]]`") is an implicit unitary change with the same covariance justification.
- **M5 (NOTE / import boundary; L15).** "satisfies T2" uses the external target's name; within the standard reading (`S₂(A⊗I₄+I₄⊗B) ≤ 2L`) the consequence is a valid in-packet derivation (`max_{rank-2 proj P'} Tr(P'X†X) = S₂(X)` by Ky Fan, then (1.2) with the maximizing `P'`). This review endorses only that conditional; it makes and endorses no `η`, unrestricted/global T2, T3/Z2/q3, counterexample, or novelty claim.

Minor notational note (no separate severity): the letter `Q` denotes the B-side rank-2 projection at L83 and an off-diagonal block of `R` at L101; context disambiguates. "Either" in L11/L15/L119 is used inclusively (at least one), consistently with the proof.

## 5. Overall assessment and boundaries

The packet's three mathematical theorems — the all-`n` rank-two partial-trace inequality (1.1), the original-pair bound (1.2) for rank-two projectors with either local marginal of rank ≤ 2 (arbitrary complex traceless `A,B`), and strictness when both `A²`,`B²` are nonnormal — are **fully reconstructed and correct as written**, with quantifiers, complex trace/conjugation conventions, and rank-one/zero/degenerate boundaries all verified. The weighted Ky Fan equivalence (3.1) is correct in the (intended) traceless class and mis-stated only by leaving `Tr D = 0` implicit (M1, MINOR). Findings M1–M4 are MINOR precision/wording items that do not affect any theorem statement or proof step as used.

Boundaries of this review: same-harness written reconstruction only; not an independent-family, human, formal/kernel, or novelty verification; no stance on f274 `η`, unrestricted T2/T3/Z2/q3, physical or `η` counterexamples, or the broader correctness of the owner source beyond this frozen body; no selected-instance or computational evidence used or produced.
