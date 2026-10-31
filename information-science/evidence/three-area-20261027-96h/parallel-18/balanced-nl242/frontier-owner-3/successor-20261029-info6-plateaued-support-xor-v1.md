# The support XOR of plateaued Walsh spectra vanishes: (N1) is vacuous in-class

**SAME-SLOT WRITTEN MANUSCRIPT (the declared (U)-side step; partial package, one self-contained theorem and its consequences).** Native clock observed before writing: **2026-10-29T20:06:38-0700 PDT**. Owner InfoBalancedNL242-3, slot info-6. This packet resolves, in the vacuous direction, the open item left by the f270 review and repeated in the f270 erratum: *whether some plateaued 16-support has nonzero XOR*. The answer is no. Consequences at the frozen f244 residual `(G₃,H)=(1,0)`: **(N1) is automatically satisfied by every admissible u — it is redundant relative to the adopted block structure — and (N2) remains the only genuinely new u-side condition.** No witness, no exclusion, no change to the residual's open status is claimed. All-variable written mathematics only; no code, solver, search, selected function, spectrum, atom assignment or diagnostic; the f272 composite (base `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a65b443cdc156a` + erratum `a3826398f2c2d02d94e07f7da85a3cabf7301d966d5b19972887f2bd0281ac9c`) is untouched; standing NONINPUT controls remain binding.

## 1. Setting

Let `σ: F₂⁶ → {±1}` be **plateaued with amplitude 16**, i.e. `Walsh(σ)(r) ∈ {0, ±16}` for all r; write `D = supp Walsh(σ)` (`|D| = 16` by Parseval: `Σ_r Walsh(σ)(r)² = 64·64 = 4096 = 16·256`), `ε_r = sign Walsh(σ)(r)`, and `μ := Walsh(σ)/16 ∈ {0,±1}^{F₂⁶}`, so `supp μ = D` and `μ(r) = ε_r` on D. Inverting, `σ(x) = (1/64)Σ_r Walsh(σ)(r)(−1)^{r·x} = (1/4)Σ_{r∈D}ε_r(−1)^{r·x}`, so equivalently `|Σ_{r∈D}ε_r(−1)^{r·x}| = 4` for all x — the dual signed form used in the base manuscript's §5.

**Proposition 0 (perfectness).** `μ∗μ = 16·δ₀`, where `(μ∗μ)(c) = Σ_b μ(b)μ(b+c)`.

*Proof.* The Fourier transform of `μ∗μ` on the group `F₂⁶` is `μ̂²` (characters are real, `μ̃ = μ`). Now `μ̂(r) = (1/1)·` — directly: `μ̂(r) = Σ_c μ(c)(−1)^{r·c} = 4σ(r)` by the inversion identity above — so `μ̂(r)² = 16σ(r)² = 16` for every r, a constant; hence `μ∗μ` is the inverse transform of the constant 16, which is `16·δ₀`. In coefficients: `(μ∗μ)(0) = Σ_b μ(b)² = 16` and `(μ∗μ)(c) = 0` for `c ≠ 0`. ∎

This is the standard "plateaued ⟺ dual is a perfect signed array" fact, restated for the record; the base manuscript's Theorem 4/§5 already used `|Σ_{r∈D}ε_rχ_r| = 4`.

## 2. The theorem

**Theorem (support XOR vanishes).** Let `μ: F₂⁶ → {0,±1}` be perfect with weight 16 (`μ∗μ = 16δ₀`). Then

`⊕_{c∈supp μ} c = 0` in F₂⁶.

Consequently every plateaued-16 `σ` on `F₂⁶` has `⊕D = 0`: **(N1) holds automatically in-class.**

*Proof.* Work in the integral group ring `Z[G]`, `G = F₂⁶` (additive), with basis `{g^c}` and product `g^b·g^{b'} = g^{b+b'}`. Let

`x := Σ_c μ(c) g^c ∈ Z[G]`.

By Proposition 0, `x·x = 16·g^0`. Introduce the u-basis: `g_i ↦ 1 + u_i` for the six standard generators, giving the ring isomorphism

`Z[G] ≅ Z[u₁,…,u₆]/(u_i² + 2u_i)`   (from `g_i² = 1`),

so that `u_i² = −2u_i` — **not** `0`; this integral relation, invisible modulo 2, is the whole engine. The monomials `u_S = ∏_{i∈S}u_i` form a Z-basis, `x = Σ_S a_S u_S` with integer `a_S`, and for any two subsets S, T:

`u_S·u_T = (−2)^{|S∩T|} u_{S∪T}`

(each `i ∈ S∩T` contributes `u_i² = −2u_i`; the remaining variables multiply monomially). Now compare the coefficient of the degree-one monomial `u_{{i}}` on both sides of `x·x = 16`:

- Right side: the element `16` is the constant `16·u_∅`; its `u_{{i}}`-coefficient is **0**.
- Left side: `x·x = Σ_{S,T} a_S a_T u_S u_T`; the pairs with `S∪T = {i}` are exactly `(∅,{i}), ({i},∅), ({i},{i})`, with intersection sizes `0,0,1`, contributing `a_∅a_i + a_ia_∅ − 2a_i²`. Hence

`2a_i(a_∅ − a_i) = 0` for every i, i.e. `a_i ∈ {0, a_∅}`.

The constant coefficient is `a_∅ = Σ_c μ(c) = μ̂(0) = 4σ(0) = ±4` (flatness, Proposition 0's proof). Therefore `a_i ∈ {0, ±4}` is **even** for every i. Finally, unwinding the basis change — the coefficient of `u_i` in `g^c = ∏_j(1+u_j)^{c_j}` is `c_i` — gives

`a_i = Σ_{c∈D} μ(c)·c_i ≡ #{c ∈ D : c_i = 1} (mod 2)`,

because `μ(c) ≡ 1 (mod 2)` on the support. Every coordinate of `⊕D = #{c∈D: c_i=1}ᵢ` is even. ∎

**Remark (why parity needs the integral lift).** Reducing `x² = 16` modulo 2 gives `x̄² = 0` in `F₂[u]/(u_i²)`, which for ANY even-cardinality support collapses to the vacuous statement `0 = 0`; the XOR content survives only through the relation `u_i² = −2u_i` over Z. In particular no mod-2 argument can prove the theorem, and none was needed.

**Remark (sharpness).** The evenness of the flat amplitude is essential. For weight `w = 1`: `μ = ±δ_a` is perfect with `μ̂ ≡ ±(−1)^{a·r}` flat of amplitude 1, and `⊕supp = a ≠ 0` is possible — e.g. a linear function `σ = (−1)^{ℓ}` on any `F₂ⁿ` is plateaued with singleton Walsh support `{ℓ}`. The theorem's parity step needs `a_∅ = ±√w` even, i.e. `w ≡ 0 (mod 4)`; weight 4 and weight 16 both qualify.

**Worked check (hand-verified, not a computation).** Weight-4 prototype on `F₂²`: `D = {0, e₁, e₂, e₁+e₂}` with `ε = (+,+,+,−)` is perfect (each nonzero difference `e₁, e₂, e₁+e₂` is realized by exactly two pairs with opposite sign products). In the u-basis, `x = 1 + g₁ + g₂ − g₁g₂ = 2 − u₁u₂`: `a_∅ = 2 = √4`, `a₁ = a₂ = 0`, and `x² = (2−u₁u₂)² = 4 − 4u₁u₂ + u₁²u₂² = 4 − 4u₁u₂ + 4u₁u₂ = 4` — the identity `x² = w` holds visibly, the degree-one coefficients `2a_i(a_∅−a_i)` vanish as claimed, and `⊕D = 0`.

## 3. Consequences at the frozen residual

**(C1) (N1) is vacuous in-class.** The f270 review's open item — "whether some plateaued 16-support has ⊕D ≠ 0" — resolves in the negative: none does. Every `σ₁ = sign k(·,1)` satisfying the **named plateaued-structure import** (Import I, §4) is plateaued-16 on `R ≅ F₂⁶`: the imported statements supply `16U₁ = 3·Walsh_R(σ₁)` with `t₁ = 0`, `U₁ ∈ {0,±3}` and exactly 16 nonzero blocks, and the passage to `Walsh_R(σ₁) ∈ {0,±16}` is division by 3 and 16 applied to the import — arithmetic on the imported statement, not a restatement of its proof. The Theorem then yields `(N1) ⊕_{c∈D}c = 0` automatically.

**(C2) Redundancy of (N1).** At the frozen scope, (N1) is *implied* by the adopted plateaued structure via the Theorem. The corrected u-side clause of the interface (base Theorem 6 as amended by the f270 erratum) may therefore drop "(N1)" from its list of genuinely additional conditions: **the only new u-side condition is (N2)** `⊕_{c∈D} z₀(c) = 0` in P*, which the Theorem does not touch (it constrains the c-XOR of D, not the z₀-gap placement inside blocks). (U) is thus: frozen f244/f255/f263 system (including the plateaued `σ₁` structure) **plus (N2)**.

**(C3) Corrigendum to the base's Remark (a).** The base manuscript's Remark (a) stated that (N1),(N2) "are not implied by any adopted f244/f255/f263 statement". That sentence **survives for (N2)** but **fails for (N1)**: (N1) is a consequence of the adopted statements via the present Theorem. This is an additive correction to be folded by the parent into the next freeze; the frozen bytes of the base and erratum are untouched here.

**(C4) General form.** The same proof runs on `F₂ⁿ` verbatim: any perfect `{0,±1}` array `μ` (equivalently, the normalized dual `Ŵσ/2^{(n+t)/2}` of any plateaued Boolean function σ with Walsh support size `2^{n−t} ≡ 0 (mod 4)`) satisfies `⊕ supp μ = 0`. For `2^{n−t} ≡ 2 (mod 4)` or singleton supports the amplitude `2^{(n+t)/2}` is odd and the conclusion can fail (Remark on sharpness); bent functions (`supp = everything`, XOR of the whole group) are consistent with the theorem.

**(C5) Interface status unchanged.** (V) is untouched; the residual `(G₃,H)=(1,0)`, the (0,4,8) case, the other six class-count pairs, m=114, other fibre patterns, rank two and the global balanced NL242 target all remain OPEN. No witness, no exclusion.

## 4. Provenance and boundaries

**Named imports (cited, not restated).** The application §3(C1)–(C2) rests on the following adopted statements, imported by name and SHA; their proofs are not reproduced here. The Theorem and Proposition 0 (§§1–2) are self-contained all-variable mathematics and use no import.

| Import | SHA-256 | Imported statement used |
|---|---|---|
| I. f255 correction `successor-20261029-f255-boolean-local-normalization-correction-v1.md` | `e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4` (12388 B, 151 LF) | `16U_s = 3·Walsh_R(σ_s) − 2t_s` with `t₁ = 0`; `U₁ ∈ {0,±3}` with exactly 16 nonzero blocks |
| II. f244 obstruction parent `info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` (4246 B, 24 LF) | adopted m=116, (0,4,8), rank-two/eight-zero scope; A₁ = 16 class count |
| III. f263 residual parent `info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md` | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` (8344 B, 31 LF) | parent adoption of the corrected composite at (G₃,H)=(1,0) with H the explicit local U₀-peak count |

The f270 review and erratum (pinned below) supplied the open item and the corrected interface wording. The Theorem, Proposition 0's packaging, the u-basis engine, the sharpness remark and the worked check are new written mathematics of this packet. Native clocks: declaration to Main before composition; this file at 2026-10-29T20:06:38-0700 PDT. No frozen body, review, or the f272 composite was modified; no selected finite object was constructed or consulted (the weight-4 prototype is a hand-verified illustration of the ring identity, not a search product); no external source or model. Same-harness; not human, independent-model-family, formal/kernel or novelty verification.

| Pinned object | SHA-256 | bytes | LF |
|---|---|---|---:|
| Base manuscript (unchanged) | `a1b7036f4b37738e3a5bb58527b46129eeaf3d5c733872a278a65b443cdc156a` | 19712 | 135 |
| f270 erratum (unchanged) | `a3826398f2c2d02d94e07f7da85a3cabf7301d966d5b19972887f2bd0281ac9c` | 11328 | 60 |
| f270 review (context, unchanged) | `7d1f153a76283764ac8c178d4594843dbdd78bbad15a98ae3672bf8890065207` | 23878 | 132 |
