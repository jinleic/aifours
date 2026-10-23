# Hostile review: E1 exact non-MUB flat plane (01 + erratum-1 + parent erratum)

I did this review by hand, working only from the text quoted in your request. I used no tools, files, numerics or float results. Abbreviations: **01** = `…/wh5-flat-plane-classification/01-exact-nonmub-flat-plane-v1.md`, **E** = its `erratum-1.md`, **PE** = `review/rqls10-E1-nonMUB-parent-erratum-v1.md`, **00** = scope freeze, **02** = interface JSON.

## Verdict

**E1 = NO is proved.**
- P = xx† + yy† (01:113–116) is an exact rank-2 orthogonal projector.
- It commutes with U and has all 15 diagonal values equal to 2/5.
- It is not a MUB-pair plane.
- Prop 9(a) is correct as stated.
- Prop 9(b) is correct. It says there are exactly four flat planes of the type (line of E(−ω)) ⊕ (line of E(−ω²)).
- Prop 9(c) is correct once E1 is applied.
- PE is correct and changes no mathematics.

| | FATAL | MAJOR | MINOR |
|---|---|---|---|
| Exact proof (01 + E + PE), still open | 0 | 0 | 5 (wording or completeness; none affects truth) |
| Already closed by the errata (closures verified) | – | – | 3 |
| Metadata | – | – | 2, plus items I could not verify |

**Admissibility against 00:17–18:**
- Closed form: ✓
- Rank 2 and orthogonal projector: ✓ (x and y are orthonormal)
- All 15 diagonal values: ✓ (5 computed explicitly; 10 by exact U-transport, which I also spot-checked directly)
- Not a MUB-pair plane: ✓

## Errata applied

- **PE:5.** Lines 01:14 and 01:48 now read "projective order-3 U". I verified the erratum's claims:
  - U⁶ = I and U³ = −I.
  - U and U² are not I, because −ω is an eigenvalue and (−ω)² = ω² ≠ 1. So the ordinary order is 6.
  - U and U² are not scalar (eigenvalues −1 ≠ −ω; 1 ≠ ω²). So the projective order is 3.
  - (−U)³ = I.
  - 01:179 already speaks of −U and is correct as written.
  - No proof step uses U³ = I.
- **E:6–11.** This extends Lemma 4(b) to all k ∈ Z₅ and to β_Z, and adds the line-permutation property. Verified below.
- **E:13–14.** Completing the square: a(r+h)² = ar² + br + b²(4a)⁻¹ with h = b(2a)⁻¹. Verified.

## Claim-by-claim

| Claim | Proof lines | Verdict |
|---|---|---|
| Notation: ζ = ε⁶, ω = ε¹⁰, ZX = ζXZ, Xf_m = ζ⁻ᵐf_m, g_m = Qf_m, ψ⁰ = f, ψ⁴ = g (12 ≡ 2) | 01:17–24 | ✓ |
| Lemma 1(a)(b): golden-ratio values, G(1) = √5, G(2) = −√5 | 01:26–27, 31–33 | ✓ |
| Lemma 1(c) | 01:27–28, 33; E:13–14 | ✓ |
| Lemma 1(d): ten identities | 01:28–30, 34–40 | ✓ (m5) |
| Cor 2 | 01:41–46 | ✓ |
| Lemma 3: action of U, U³ = −I, cycling Z→T→X→Z | 01:49–55 | ✓ |
| Lemma 4(a) | 01:57–58, 61–65 | ✓ |
| Lemma 4(b) with E1 | 01:59–60, 66–68; E:6–11 | ✓ |
| Lemma 5 | 01:71–77 | ✓ |
| Parity and coordinate formulas for a, b | 01:79–83 | ✓ |
| Lemma 6 | 01:85–100 | ✓ |
| Cor 7 | 01:102–108 | ✓ |
| §4: constants and explicit x, y | 01:111–121 | ✓ |
| Thm 8(i)(ii) | 01:123–124, 126–131 | ✓ |
| Thm 8(iii): transport to X and T | 01:124, 132–134 | ✓ |
| Thm 8(iv) | 01:125, 135, via 9(a) | ✓ |
| Prop 9(a) | 01:140, 144–150 | ✓ |
| Prop 9(b) | 01:140–143, 151–169 | ✓ (m1, m2, m4) |
| Prop 9(c) | 01:143, 170–172; E:6–11 | ✓ with E1 (m3) |
| §6 scope and §7 imports | 01:174–188 | ✓ (01:177–179 is metadata; see M1) |

## Independent re-derivations

Items marked "(new)" are my own checks by a route not used in the file.

### Radicals, Gauss sums, trig (Lemma 1, Cor 2)

- **Golden-ratio values.** Let s = ζ+ζ⁴ and s′ = ζ²+ζ³.
  - s + s′ = −1 and ss′ = ζ³+ζ⁴+ζ⁶+ζ⁷ = −1.
  - s = 2cos(2π/5) > 0 selects s = (√5−1)/2 = 1/φ, with √5 > 0. Then s′ = −φ.
- **Gauss sums.** t² takes the values 0,1,4,4,1 and 2t² takes 0,2,3,3,2.
  - G(1) = 1 + 2s = √5 and G(2) = 1 + 2s′ = −√5.
  - For a = 2: (4a)⁻¹ = 8⁻¹ = 3⁻¹ = 2, and −2 ≡ 3. ✓
- **Cosine values used implicitly** (see m5):
  - 2cos(π/5) = −(ζ²+ζ³) = φ
  - 2cos(3π/5) = −1/φ
  - 2cos(6π/5) = −φ
- **Lemma 1(d), all ten identities:**
  - α+β = 4cos(π/3)cos(π/5) = φ
  - γ+δ = −1/φ
  - αβ = −1 + 1/φ
  - γδ = −φ − 1 = −φ²
  - αγ = 1/φ + α
  - βδ = 2cos(22π/15) + 1/φ = β + 1/φ
  - γ² = 2 + β
  - δ² = 2 + 2cos(28π/15) = 2 + α
  - (α−β)² = φ² − 4αβ = (φ+1) − 4(φ−2) = 9 − 3φ
- **Cor 2.**
  - u + v = φ + 1/φ = √5.
  - uv = −1 − φ − 1/φ − φ² = −1 − 3φ.
  - AB = 5 + 5 − 1 − 3φ = 9 − 3φ.
  - A + B = 3√5.
- **(new) Closed forms for A and B.**
  - φαB = φ(√5α + αβ − αγ) = φ((√5−1)α − 1) = 2α − φ = α − β.
  - φα(α−β) = 3φ − 1 + φγ, with φγ = 2cos(7π/15) + 2cos(π/15) = −β − δ. Hence φα(α−β) = √5 + α − δ = A.
  - So B = (α−β)/(φα) and A = φα(α−β).
  - Their product reproduces AB = (α−β)², and α > 0 gives a second proof that A, B > 0.

### U = QF†

- **Action on the bases.**
  - F†e_s = f_{−s}, so Ue_s = g_{−s}.
  - Uf_s = ζ^{2s²}e_s.
  - (F†g_m)_t = (G(2)/5)ζ^{3(m−t)²}. After multiplying by ζ^{2t²}, the exponent is 3m² − 6mt + 5t² ≡ 3m² − mt.
  - So Ug_m = −ζ^{3m²}f_{−m}. The only source of the sign is G(2) = −√5.
- **U³ = −I.** U³e_s = −ζ^{5s²}e_s = −e_s.
- **(new) Spectrum cross-check.**
  - tr U = G(1)/√5 = 1.
  - tr U² = −G(4)/√5 = −1.
  - With multiplicities (1,2,2) for (−1, −ω, −ω²), the traces are −1 + 2 = 1 and 1 + 2(ω+ω²) = −1. ✓
- **Clifford action (Lemma 4(a)).**
  - F†XF = Z⁻¹ and F†ZF = X.
  - QXQ†e_t = ζ^{4t+2}e_{t+1} = ζ²XZ⁻¹e_t.
  - M(a,c) = (c, −a−c) has determinant 1 and M³ = I.
  - M(1,k) ∈ L_k exactly when k² + k + 1 ≡ 0. For k = 0,…,4 the values are 1,3,2,3,1, so no line L_k is fixed.
  - L₁ → L₃ → L₂ → L₁, and L_Z → L₄ → L₀ → L_Z, which matches Z → T → X.
- **Lemma 4(b) for every k.**
  - (XZ^kψ^k_m)(t) = ζ^{−5kt+2k−m}ψ^k_m(t), so the eigenvalue is ζ^{2k−m}.
  - D_u·XZ^k = ζ^{c−ka}·XZ^k·D_u.
  - Hence D_uψ^k_m ∈ ℂ·ψ^k_{m+c−ka} for all k ∈ Z₅, and D_{(a,c)}e_t = ζ^{ct}e_{t+a}.
  - Nothing in the argument uses k ∉ {0,4}, exactly as E1 claims.

### Eigenspaces and coordinates (Lemma 5, Lemma 6, Cor 7)

- **(new) Second route to Lemma 5.**
  - v_{μ,s} = (I − μ²U + μU²)e_s.
  - (U+μ)(I − μ²U + μU²) = U + μ + μU³ − μ³U = 0.
  - So v_{μ,s} is 3 times the E(−μ)-projection of e_s.
- **Parity and basis.**
  - Πv_{μ,s} = v_{μ,−s}, so a is even, b is odd, and ⟨a,b⟩ = 0.
  - a₀ ≠ 0 and b₂ ≠ 0 (since α ≠ β), so {a, b} is an orthogonal basis of the 2-dimensional E(−ω). The same holds for a′, b′.
- **Coordinate formula 01:81–82 re-derived** (using g_{−1} − g_{−4} = g₄ − g₁ and ζ⁴⁸ = ζ³).
- **All eight ε-products in 01:92–99 re-derived:**
  - ε² + ε¹⁰ = γζ
  - ε⁸ + ε¹⁰ = −δε⁹ = δζ⁴ (using ε⁹ = −ζ⁴)
  - (ε⁶−ε²⁴)(ε²−ε²⁸) = β − γ
  - ε¹⁸(ε¹²−ε¹⁸)(ε²⁰−ε¹⁰) = (α−β)ζ³
  - ε²² + ε²⁰ = −δε²¹ = δζ (using ε²¹ = −ζ)
  - ε²⁸ + ε²⁰ = γζ⁴
  - (ε⁶−ε²⁴)(ε²²−ε⁸) = α − δ
  - the sign flip coming from ω − ω²
  - The ± conventions at 01:91 agree with the parity.
- **(new) Direct eigen-equation checks on the final coordinates.**
  - (Ua)₀: use γζ + δζ⁴ = 2ω − φω², which follows from ε² + ε⁸ = φε⁵ and ε⁵ = −ω². Then (Ua)₀ = (1/5)(2φ − 4ω + 2φω²) = −ω(5+√5)/5 = −ωa₀. ✓
  - (Ub)₁ = (1/5)[(ζ−ζ³)B + (ζ³−ζ²)(α−β)]. After dividing by ω:
    - the real part is B(γ−β−A)/2 = −√5B;
    - the imaginary part is sin(π/5)·(α − β − φαB), which is 0 by the closed form above.
    - So (Ub)₁ = −ωb₁. ✓
  - (Ub′)₁ = −ω²b′₁ checks the same way, using A = φα(α−β).
- **Cor 7.**
  - ‖√5a‖² = (1+√5)² + 2γ² + 2δ² = 15 + 3√5 = N.
  - ‖√5b‖² = 2B² + 2AB = 6√5B > 0, so B > 0. The same argument gives A > 0.
  - ζ·conj(a_t)b_t is real at t = 1, 2, and parity covers the rest.

### Witness (§4, Thm 8)

- **Constants.**
  - p = 3(5−√5)/20 lies in (0, 3/4).
  - p/N = (3−√5)/40 = c².
  - (1−p)/(6√5) = (3+√5)/120 = s².
  - Every radicand is positive and every root is taken positive.
- **Coordinates.**
  - x_t = c·√5a_t + iζs·√5b_t/√B.
  - The step (α−β)/√B = √A needs α > β and A, B > 0; both are proved.
  - All ten entries at 01:115–116 match, including the sign swaps (y₂ carries −is√B because √5b′₂ = −(α−β)ζ³).
  - x₀ = c(1+√5) = 1/√5, since c²(6+2√5) = 1/5.
- **Norms and Z-diagonal.** Let S := c²(γ²+δ²) + s²(A+B) = (11−3√5)/40 + (5+3√5)/40 = 2/5.
  - Each of |x₁|²+|x₂|², |y₁|²+|y₂|², |x₁|²+|y₁|² and |x₂|²+|y₂|² equals S.
  - Hence ‖x‖² = ‖y‖² = 1/5 + 2S = 1, and the Z-diagonal of P is 2/5 at every t.
- **Orthogonality.**
  - The imaginary parts cancel within the pairs t = 1,4 and t = 2,3.
  - This leaves ⟨x,y⟩ = 1/5 + 4c²γδ = 1/5 − 4c²φ² = 1/5 − (3−√5)(3+√5)/20 = 0.
  - This is also forced by x and y having distinct U-eigenvalues.
- **Transport to X and T.**
  - Ue_s = g_{−s}, U²e_s = −ζ^{3s²}f_s, and U†PU = P. ✓
- **(new) Direct check, independent of transport.**
  - f₀†x = −ω/√5, f₀†y = −ω²/√5, and g₀†x = −ω²/√5.
  - Each has modulus squared 1/5.
  - These are exactly the phases predicted by U†x = −ω²x and U†y = −ωy, with f₀ = −U²e₀ and g₀ = Ue₀.

### Non-MUB-pair (Prop 9(a))

- **The file's Parseval argument.**
  - Σ_{n=0}^{4}|tr PWⁿ|² = 5·Σ_m P_mm² = 10. The n = 0 term is 4, so tr PWⁿ ≠ 0 for some n ∈ {1,…,4}.
  - Wⁿ ∝ D_{n(1,k)}, and |tr PD_{Mu}| = |tr PD_u| ≠ 0.
  - Mu = n(k, −1−k) lies in L_k only if n(k²+k+1) ≡ 0, which is impossible.
  - So Lemma 4(b), already in its original scope k ∈ {1,2,3}, gives tr PD_{Mu} = 0. Contradiction. ✓
- **(new) A second route.**
  - U(XZ^k)U† ∝ (XZ^{k′})^k, with k′ = −(1+k)k⁻¹ = 3, 1, 2 for k = 1, 2, 3.
  - This operator has simple spectrum on ψ^{k′}, so U sends ψ^k-lines onto ψ^{k′}-lines.
  - A U-invariant ψ^k-pair plane would therefore also be a ψ^{k′}-pair plane.
  - But computing in the ψ^k form, ψ^{k′}_j†Pψ^{k′}_j = 2·|G(3(k−k′))|²/25 = 2/5, not 1. Same conclusion.

## Separate audit: Prop 9(b) "exactly four" and Prop 9(c) WH transport

### 9(b), restricted to the type (line of E(−ω)) ⊕ (line of E(−ω²))

1. **The normal form is complete.**
   - Any unit x in E(−ω) is, up to phase, √p·â + τ√(1−p)·b̂.
   - P meets E(−ω) exactly in ℂx and E(−ω²) exactly in ℂy, so P corresponds bijectively to the pair (ℂx, ℂy).
2. **Reduction to Z.** P commutes with U, so Z-flatness is equivalent to full flatness.
3. **Even/odd split.**
   - Z-flatness is equivalent to (E0), (E2), and the two odd equations together.
   - The even equation at t = ±1 follows from tr P = 2.
4. **The even system is as written.**
   - The entries are |â₂|² = (2+α)/N, |â′₂|² = (2+β)/N, |b̂₂|² = A/(6√5), |b̂′₂|² = B/(6√5), and (A+B)/(6√5) = 1/2.
   - Its determinant is positive:
     - A − B = (α−β) + (γ−δ) > 0;
     - (A−B)² = 9 + 12φ > 9 − 3φ = (α−β)²;
     - 6√5 < N.
   - The pair (p₀, p₀) solves the system. These are exactly the τ-independent sums of Thm 8(ii).
   - So p = q = p₀ ∈ (0,1).
5. **The odd system is as written.**
   - r₁, r₂, r′₁, r′₂ are as stated.
   - r₁r′₂ − r₂r′₁ = −(α−β)(γ²B + δ²A)/(KK′) < 0, using γ = 2cos(4π/15) > 0.
   - So τ and τ′ lie in {±iζ}.
6. **Converse.** Every sign choice satisfies all four equations, so all four planes are flat. The file does not state this (m2).
7. **Distinctness.** This uses 0 < p₀ < 1. ✓

So "exactly four" is proved for this type. The file correctly does not claim the remaining U-invariant types: a whole 2-dimensional eigenspace, or the (−1)-line plus a line. Nor does it claim anything about non-invariant planes (01:180–182, 02:47).

### 9(c) with E1

- By E1 as re-derived above, every D_w permutes the lines of all six bases: β_Z, ψ⁰ = β_X, ψ¹, ψ², ψ³, ψ⁴ = β_T.
- D_w† ∝ D_{−w} does the same.
- So D_wPD_w† is a flat rank-2 projector, and it is a MUB-pair plane exactly when P is. This holds for every flat non-MUB-pair P.
- Before the erratum, 01:59–60 gave only k ∈ {1,2,3} and only "zero diagonal". But 01:170–171 needs k = 0, 4, β_Z, and the permutation property. E1 closes this gap.
- The file correctly does not claim the number of translates.

## Open findings and minimal repairs (all MINOR)

- **m1, 01:160.** "Hence p = q is the unique solution" does not follow from a nonzero determinant alone.
  - Repair: "Hence (E0), (E2) have at most one solution. Since (p₀, p₀) solves them (the t = 0, ±2 sums of Thm 8(ii) do not involve τ), p = q = p₀."
- **m2, 01:140–143 against 151–169.** Only necessity is proved. Thm 8 covers only σ = σ′ = +1.
  - Repair: add "Conversely, p = q = p₀ with τ, τ′ ∈ {±iζ} satisfies (E0), (E2) and both odd equations, which together are equivalent to Z-flatness."
- **m3, 01:143.** In 9(c), P is unquantified.
  - Repair: "for every flat non-MUB-pair plane P, in particular each of the four in (b)".
- **m4, 01:165–166.** The symbol X is reused for Re(τζ⁻¹), clashing with the shift operator X.
  - Repair: rename to ξ, η.
- **m5, 01:34–35 and 01:167.** Two elementary facts are left unstated:
  - the values 2cos(π/5) = φ, 2cos(3π/5) = −1/φ, 2cos(6π/5) = −φ (immediate from 1(a) and cos(π−x) = −cos x);
  - γ²B + δ²A > 0 (needs A, B > 0 and γ > 0).
  - Repair: one clause each.

**Already closed and verified:** Lemma 4(b) scope (E1); Lemma 1(c) wording (E2); "order-3" at 01:14 and 01:48 (PE).

## Metadata (not verified, not load-bearing)

- **Not checked, per your no-tools instruction:**
  - all SHA-256 values and byte counts (02:14–15);
  - the 0444 file modes and package size;
  - the `/bin/date` timestamps;
  - the authority and transition references;
  - "frozen_before_derivation";
  - the "no computation / CLI" attestations (00:38–41, 02:49).
  - My verdict is about the quoted text. Whether that text matches those hashes is unverified.
- **Decimals at 01:23 and 01:111.** Not checked, and never used. The proof uses only α > β, γ > δ and positivity facts it proves itself.
- **M1, 01:177–179.** The remark calls Prop 9(b) "the exact version of '4 per conjugate'". But the float operator at 00:25 is a different formula: QXQF with Q = diag(ζ^{t²}), which also clashes with 01's Q, and F_{j,t} = ζ^{−jt}/√5. Nothing proves it is projectively a WH-conjugate of U^{±1}.
  - Repair: label the remark as heuristic, conditional on that unverified identification.
- **M2, 02:32–33.** The dependency lists are incomplete.
  - Thm8 also uses Lem1(d), Cor2 and Lem6.
  - Prop9 also uses Lem1(d), Cor2, Lem3, Lem6 and Thm8(ii).
- **Exposure items, 00:22–35.** These include 130 = 30 + 100, four orbits of 25, and "float U order 3". They are context only and enter no proof step.

## What does not follow

- No full classification of Z/X/T-flat planes.
- No count of distinct WH translates. The figure 100 is float exposure only.
- No claim that every exotic plane is U_w-invariant.
- Nothing on the W8 ansatz or E2/E3. Maximal 1-RQLS(10) remains OPEN / UNKNOWN.
- No novelty assessment.
