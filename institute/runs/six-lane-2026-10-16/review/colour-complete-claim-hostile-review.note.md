VERDICT: ACCEPT-WITH-FIXES

**Summary.** I re-derived by hand every written inequality on your focus list; the derivations are at the end.
- No critical or high findings. None of the written inequalities is wrong in a way that breaks the chain A → B, C → D, E → G, F.
- Assuming the pinned outputs are as reported, CLAIM.md proves H1.1 exactly as stated: strict inequality, uniqueness, and closed Δ.
- Two medium findings concern the bridge to Theorem 1.1 and its scope. The rest are precision defects, and none of the fixes needs a recomputation.

These items are checked and correct:
- the match to (7.1)–(7.5) on closed Δ;
- the max-entropy parametrisation, the Gibbs/KL identity and the Hessian;
- the Mpoly/Sylvester equivalence and the segment argument (A2);
- the pairing duality, its (3/2) coefficient and all scaling signs;
- the finite-spectrum supergradient bound, the convex vertex bound and the Birkhoff cover;
- the E chain, every Loewner direction, IFT smoothness, the Taylor remainder, strictness, and the value at the centre.

## Findings (severity-ranked)

### MEDIUM

**M1 — The bridge at n\* is overclaimed.**
Locations: §2 › "Other numerical…" › p. 21, Lemma 5.5; §4 › "n-form and m-form".
- The text says "Lemma 5.5 is used only at n\* (Lemma F … gives F(n\*) independently)". Lemma F proves only the *value*.
- The conditional proof also needs the *unique maximiser b*: Lemma 5.6 asserts it, and Lemmas 5.8–5.10 (the Laplace step) use it.
- The paper gets that uniqueness from Lemma 5.5 plus the sentence "unique stationary point of G̃ in the interior of M0(1/9), which must then be a maximum". That step requires excluding maximisers on the boundary of M0(1/9), and nothing quoted does so.
- So the bridge, as written, quietly inherits one analytic step beyond H1.1.

**Fix:** add Lemma F′, which uses only what CLAIM.md already proves.

*Lemma F′.* b is the unique maximiser of f on D.

*Proof.*
1. Take d in the fibre of n\* and y = 0. The proof of Lemma B gives exactly f(d) = Σ_u (1/9)[E(p^u) + ½Σ m̂^u ln m̂^u] − 3 ln 3, where E(p) = Σ p ln(w/p).
2. E(p^u) ≤ H(m̂^u) and ψ(m̂^u) ≤ Ψ\*(0).
3. Equality forces m̂^u = (5/4)1 for every u, by the segment-uniqueness argument of Lemma E step 2 applied at the explicit stationary point μ = 1.
4. Equality also forces p^u = w/900, by the KL equality case.
5. Hence d = b. Off the fibre of n\*, f(d) ≤ ln F(n(d)) < L\*.

This also yields the §4 m-form. After F′, the only paper-side computations needed at b are the Lemma 5.7 rank/parametrisation and H̃, which §2 already reproduces exactly.

**M2 — The scope of the corollary.**
Locations: title; §1 last paragraph; §2 header; §5a › "Version".
- H1.1 is certified for the *preprint's* (7.1)–(7.6). The corollary invokes the *published* Theorem 1.1, and the two versions were never compared.
- The "2009-10-20" date has no recorded provenance and does not appear in §2.
- Normalisation drift would be harmless: factors c^{d} or c^{m/2} only contribute the constants c^{Σd} or c^{5/2} on D.
- Structural drift in (5.1), (5.22)–(5.23) or (7.4)–(7.6) would not be harmless.

**Fix:** diff Hyp 1.1, Thm 1.1, Thm 6.1, (5.1), (5.22)–(5.23) and (7.1)–(7.6) against the version of record. Until that is done, phrase the corollary as "with Theorem 1.1 of the preprint (sha256 5e317a44…)".

### LOW (real gaps, none affecting the chain once fixed)

**L1 — F is never shown to be well defined on ∂Δ.**
Locations: §1 › Fibre / Objective; Lemma B › last sentence.
- On ∂Δ, (7.5) propagates zeros: n^u = 0 forces m^{u+k}_{−k} = 0.
- A class whose two row ports both point to empty classes would admit no spectrum. The theorem quantifies over F on closed Δ, so this must be excluded.

**Fix (proof supplied):**
1. The set of n with a nonempty fibre is a projection of a polyhedron, so it is convex.
2. At a vertex P_σ/3, each occupied class has exactly two live ports. They point to the other two occupied classes, which have distinct rows and distinct columns. So the live ports form the diagonal pair or the antidiagonal pair.
3. Take d^u = (n^u/2)(δ_{(4,0;0,1)} + δ_{(1,0;0,4)}), or the antidiagonal analogue. This gives m = 5/6 on every live port, so (7.5) holds.
4. By convexity every fibre over Δ is nonempty. Fibres are compact and F̂ is continuous (with 0^0 = 1), so the maximum is attained.

**L2 — A false identity under §3's own notation.**
Location: Lemma E › (Q) › Mean-value form.
- "H(m̂) = H(m)·Σm/5" is false for the entropy H defined in §3. The correct scaling is H(cm̂) = cH(m̂) − c ln c.
- The identity is true for 𝓗(μ) := ½diag(m)⁻¹ − S2⁻¹ = Hess ψ, because Hess ψ(cm) = c⁻¹ Hess ψ(m). That scaling law also justifies X0 = −(1/9)B3ᵀHess ψ(5/36·1)B3.

**Fix:**
- Rename the Hessian and state the scaling law once.
- De-collide the other overloaded symbols:
  - P: the projection I − J/4 and the congruence matrix;
  - G: the Gram matrix and the stationarity map;
  - K: the cone, the Krawczyk operator and K_u;
  - X: three different objects;
  - D: diag(m), 'D' leaves and D_c.

**L3 — A statement contradicted by the next sentence.**
Location: Lemma E › (Q) › "Dependence on c".
- "Ψ\* … depend[s] on z only through c" is false, since Ψ\*(z+t1) = Ψ\*(z) + 5t.
- Only m̂, X and R depend on c alone, and that is all the proof uses.

**Fix:** reword the sentence accordingly.

**L4 — Uniqueness is attributed to the wrong lemma.**
Locations: Lemma F ("unique by strict concavity"); §4 ("Lemma A (A1)").
- (A1) gives strict concavity only on the *open* slice, so it cannot exclude a co-maximiser on the boundary.

**Fix:** promote the Lemma E step 2 argument to a new item (A3): "ψ + ⟨z,·⟩ has at most one maximiser on conv(S); any interior stationary point is it." Then cite (A3) in both places.

**L5 — Ψ\* is written as a max, but attainment is never proved.**
Locations: §3 Notation ("Ψ\* := max"); end of the (A2) proof ("Berge … no longer needed").
- Attainment for arbitrary z needs H to be upper semicontinuous, which is Berge's theorem.
- Only Lemma E needs attainment, and there Krawczyk plus (A2) supply it.

**Fix:** define Ψ\* as a sup. Lemmas B, C and D then hold verbatim.

**L6 — A load-bearing surjectivity is unproved.**
Location: Lemma A › Bijection.
- (A1) needs m(·) to map onto int K, so that the Hessian formula holds at every point of each slice.

**Fix:** cite Brown (1986), Thm 3.6, or add this argument.
- Write m = Σλ_s s with all λ_s > 0. The map θ ↦ ⟨θ,m⟩ − Φ(e^θ) is strictly concave.
- It is also coercive: in any direction v, if some ⟨v,s⟩ > 0 the exponential term dominates; otherwise ⟨v,m⟩ < 0, because S spans ℝ⁴.
- So it has a unique critical point, and there m(θ) = m.

**L7 — The edge set is never defined.**
Locations: §3 Notation; Lemma B › Pairing.

**Fix:** define the edges as {{(u,k), (u+k, −k)}}.
- This is a fixed-point-free involution on the 36 ports, and its quotient is the tensor product K3×K3.
- With this definition, Σ_u⟨z^u, m^u⟩ = 0 is literally (7.5).

**L8 — Side conditions are unstated.**
Location: Lemma E › (Q) › Mean-value form / Loewner bound.
- The centre μ_c must lie in the Krawczyk box. Otherwise ∂_jX must be enclosed on the hull of the box and μ_c.
- The ratio bound needs ε_L < 1.

**Fix:** state both conditions and confirm them in the code.

**L9 — Precision and documentation.**
- **(a) Term counts.** Lemma A's term counts depend on the dropped index: P2 has 943 terms when index 0 is dropped (antidiagonal pair versus same-row pair). Tabulate the counts per index.
- **(b) "Supremum … exactly 2".** This is an unproved checker observation. Label it as such or drop it.
- **(c) §6 versus checker B's (C) step.** §6 says "λ_max(Hess Ū) at 16 vertices, λ_max convex". B's docstring instead certifies the affine majorant Tm built from nlo_u.
  - Both arguments are valid. Hess Ū equals an affine part plus Σ_u (3/2)/n^u(η)·A_uA_uᵀ. Each scalar coefficient is convex and each matrix is PSD, so λ_max is convex.
  - Still, §6 should describe what was actually run.
- **(d) Checker B's D4 input.** D4 imports "ψ concave on conv(S)", which is stronger than (A1)+(A2). Either restate it as (A2)+(A3), or prove it: Berge gives usc, Gale–Klee–Rockafellar gives lsc, so H is continuous.
- **(e) Stale status.** §6 says checker C "is being run". Record its result and hashes.

## Answers to your three questions

**Can the certificate settle exactly H1.1 and then invoke Theorem 1.1 for all even n?** Yes, subject to M1 and M2.
- The theorem in §1 is H1.1 verbatim.
- Every use listed in §2 is qualitative:
  - Uniqueness locates the maximisers of f in the fibre of n\*.
  - Lemma 5.10's α follows from uniqueness plus continuity of f on the compact set D.
  - (6.3) and Theorem 6.1 use the same f, so n ≡ 2, 4 (mod 6) needs nothing further.

**Do any definitions, domains or hypotheses fail at the boundary?** No.
- **Lemma B.** n^u = 0 makes both T_u and the bound term zero.
- **Lemma C.** Only m0 needs to be interior.
- **Lemma D.** t ↦ ta + (3/2)t ln t is convex on [0,∞).
- **Lemma E.** It is entirely interior.
- **Remaining items.** The only omission is L1, which holds.
- **Code check.** Confirm that the D-vertex code special-cases exact n^u = 0. A naive 0·log 0 in ball arithmetic is not finite, so the PASS suggests it does.

**Are any claims stronger than the evidence?** Yes: M1, the phrasing in M2, L3, L4 and L9(b).

## Independent derivations (all agree with CLAIM.md)

1. **Counts and moments.**
   - |S| = 56 − 24 + 4 = 36.
   - Φ = (a+b+c+d)⁵ − (a+b)⁵ − (c+d)⁵ − (a+c)⁵ − (b+d)⁵ + a⁵ + b⁵ + c⁵ + d⁵, so Σw = 900.
   - Σw s_k = 1125, so m(b) = 5/36.
2. **Lemma F value.** ln 8100 + (5/2)ln(5/36) = (5/2)ln(5/4) + ln 900 − 3 ln 3 = (9/2)ln 5 − 3 ln 2 − ln 3 = L\*.
3. **Lemma B coefficient.** The entropy contributes −n ln n and the ½Σ m ln m term contributes +(5/2)n ln n, giving (3/2)n ln n.
4. **Lemma A algebra.**
   - S2·1 = 5m, so ∇H = −θ − ⅕1 and ∇²H = −S2⁻¹.
   - Mpoly·1 = 0, and uᵀMpoly u = 5Φ(2u′ᵀDu′ − u′ᵀS2u′).
   - Sanity check at μ = 1: Mpoly = 10125000I − 4050000V0 − 2531250J, with eigenvalues 6412500 (twice) and 4972500 on 1⊥.
5. **R(0) via the Hadamard basis.**
   - V0 has eigenvalues 11/12, 11/12 and 229/180 on 1⊥, so Hess ψ there has −38/55, −38/55 and −442/1145.
   - Hence R(0) = (55/38)(P_r + P_t) + (1145/442)P_rt.
   - Its first row is (46065/33592, −1145/1768, −1145/1768, −2555/33592), an exact match.
   - The claim's formula equals (V0⁺ − (2/5)P)⁻¹ on 1⊥.
6. **G is nonsingular.**
   - Gy = 0 forces c_u = −c_v on every edge.
   - The triangle (0,0),(1,1),(2,2) then forces y = 0.
   - Y is the exact minimiser of the ε = 0 quadratic part; the factor 45/4 = 9·5/4 checks.
   - Σ_u C_uᵀ1 = 0, so Σℓ_u = 0 for any Y; also Σ A_u = 0.
7. **The c-box.** γ = (6c\*, 3c\*, 6c\*)·r0 exactly, with c\* = 75582/17915.
8. **Loewner directions.**
   - −ε/(1+ε)·S2c⁻¹ ⪯ ΔS2⁻¹ ⪯ ε/(1−ε)·S2c⁻¹ gives the entrywise bound via the spectral norm, which is at most the Frobenius norm.
   - X ⪰ Xmin ≻ 0 gives R ⪯ R̄, which is the direction the upper bound needs.
   - For checker B: N ⪯ Nhi and m̂ ≥ mlo give X ⪰ Xlb.
9. **Segment uniqueness.** φ(t) ≥ (1−t/s)φ(0) + (t/s)φ(s); letting s↑1 shows φ is constant. This is valid.
10. **Lemma G.** Each cell is avoided by 4 of the 6 permutations, the facets are tetrahedra, and radial projection gives the cover.

## Trust limits

- **Unverified by me.** I had no tools, so I did not verify SHA 8c1081f8…, the code, the JSON or the PDF. Lemma A's positivity and Lemmas D and E (Q, C) rest on the reported outputs.
- **Checker independence.** Checkers A, B and C implement one shared written scheme, so a common-mode error in the scheme would pass all three. The derivations above address that risk.
- **Rigour.** The rigour rests on arb. mpmath.iv's elementary-function enclosures are not documented to arb's standard, so B is corroboration. All margins (1.73e-11, 0.0292, 1.165) are far above working precision.
- **Unseen definitions.** (7.6) and (5.1) were not in the excerpts. I matched them only through F(b) = 5^{5/2}·25/24, which agrees with M = 25/24 and with (25/24)^n.
- **Imported from the paper (accurately disclosed in §5a).** These are the overlapping-cycle small-subgraph-conditioning moments, Lemmas 5.1/5.9/5.10, and the sketched Section 6.
  - Confirm that the anchors check the condition-(iv) identity E(Y²)/(EY)² → exp(Σλ_iδ_i²) itself, not just the two sides separately.
  - The colouring corollary is only as reliable as these imports.
