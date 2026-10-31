# f888 author candidate v1 — fixed-complement constructive iff and selected-XOR restrictions (independent reconstruction of f848)

**Status: prospective GENERAL AUTHOR candidate (AuthorF888BoolOdd). Parent disposition and independent review are separate.** Native clock observed before composition: 2026-10-31T03:30:35Z (science cutoff 2026-10-31T21:23:27Z). Written proof only; no code prepared or executed.

**Summary of outcome.** Every load-bearing f848 (S1) statement in the assigned scope was rebuilt from definitions on the actual objects: the all-256 coupled integer-k criterion with convolution `64·Ĉ` and inverse `1/128`, the pointwise `v²=1_C` step, Boolean/balance/selected-T reconstruction, original-section and gauge transport, the parity identity, and every overlap/deficiency/derivative-energy/four-fibre constant. **No f848 equation was found false.** Three refinements are new here (Sections 3, 5.4–5.5 and 6.3):

- **R1.** Within the stated even-half scope, `P_C=0` holds **automatically** for every actual u (Proposition B). So the selected-XOR requirement collapses to "the number `N_−` of negative v-signs is odd", equivalently `k(0)` odd. All 256 k then have one common parity, and f848 §4's "computable selected-XOR obstruction" can never fail for an in-scope u. It is a true but vacuous necessary condition, not an obstruction.
- **R2.** The three pair-direction counts `n_i` are all even. The direction attached to each two-entry block type is forced by its slot pair (D3→`h^(1)`, D0→`h^(2)`, Z2→`h^(3)`), giving `(n_1,n_2,n_3)=(18,4,6)` at local `H=0`. f848's "exactly two odd" case and its "24" variant are vacuous. The within-block overlaps are exactly `r=104,76,80`, with disagreement and agreement lower bounds `12,5,6`, total exactly 23.
- **R3.** Integrality of k is automatic from (3.1), and given R1 one odd coefficient suffices. The DC cap pins `N_−=70−k(0)∈{63,65,…,77}`. There is also an exact within-block derivative/four-fibre identity.

None of this constructs or excludes a branch.

## 1. Objects, quantifiers and named conditional imports

Work over F₂. Fix the selected nonzero original `T∈F₂⁹`, a functional `a0` with `a0·T=1`, and `V=a0⊥≅F₂⁸`. Every original point is uniquely `y` or `y+T` with `y∈V`. Let `K=T⊥`. Restriction `ξ↦ξ|_V` is an isomorphism `K→V*`, because `a0∉K` and `V⊥={0,a0}`. Moreover `(a0+ξ)|_V=ξ|_V`. All transforms are unnormalized, `p̂(ξ)=Σ_{y∈V}p(y)(−1)^{ξ·y}`, over all 256 points. For `Y⊆V` write `P_Y=⊕_{y∈Y}y`, and write `Ĉ(λ)=Σ_{y∈C}(−1)^{λ·y}`.

**Fixed actual u (never replaced by a formal spectrum).** `u:V→{−1,0,1}` with `|supp u|=116`, original balance `Σ_y u(y)=0` in ORIGINAL coordinates, and `C=u^{-1}(0)`, `|C|=140`. "In scope" means that u additionally satisfies the named actual even-half requirements. These are imported exactly as displayed in S1–S6 and are never re-proved here:

- **I1.** f263/f244 original-caller scope: `T≠0`, rank-2 quotient, eight W-zeros, fibre pattern `(0,4,8)`, `G3=1` read as 23 `U3` zeros.
- **I2.** Local H per S6: no `U1=0` block has a single `|U0|=4` peak. No identity with any undisplayed historical class table is asserted.
- **I3.** The shared linear decomposition `V=R*⊕P*`, `y=(c,w)`, `c∈F₂⁶`, `w∈F₂²`. Here `U_s(c)=Σ_w u(c,w)(−1)^{s·w}`, `a=U1/3`, `g=U2`. The three nonzero `s∈P≅F₂²` are labelled `s_1,s_2,s_3` with `s_1+s_2=s_3`.
- **I4. Even-half spectra.** Each `û(r,s)=Σ_c U_s(c)(−1)^{r·c}` lies in `{0,±4,±8,±12}`. Specifically: `U0`-spectra are 0 or ±8; `3â=±12` with `â=4σ`, `σ∈{±1}^64`; `|ĝ|∈{4,12}`; `U3`-spectra are ≡4 (mod 8) with magnitude ≤12. In particular `û≡0 (mod 4)` at all 256 frequencies.
- **I5. Local block forms and constants** (S5 §2–3). The 16 `U1=±3` blocks have three nonzero entries and `|U0|=|U2|=|U3|=1`. Every other block has `U1=0` and a transform that is all zero, two entries ±2, or one entry ±4. The energies are `ΣU0²=56`, `ΣU1²=144`, `ΣU2²=136`, `ΣU3²=128`. With `d=H`, the count system is `a=4−2d` (slots 0,2), `b=6−2d` (slots 0,3), `c=18+2d` (slots 2,3), `o=17+d`, plus two `|U2|=4` peaks and one `|U3|=4` peak. At `H=0` this is D0=4, Z2=6, D3=18, Z4=1, Z0=17.
- **I6. Branch geometry.** The two six-span branches `(4;0,4,4,4)` and `(4;2,2,4,4)` (S2–S4). The f244 atom/source/class correspondences and the linked canonical/rank-4/rank-2 five-span no-go bodies stay **named conditional imports**. None was opened.

Theorem A and Lemmas 1–3 need only u, C and the counts `116/140`. Proposition B needs I4, or only its weak form `û(ξ)≡û(0) (mod 4)`. Its coordinate form B′ and R2 need I3 and I5.

A **physical complement** is `v:V→{−1,0,1}` with `v²=1_C` pointwise. Its **reconstruction** is `s_v(y)=u(y)+v(y)`, `s_v(y+T)=u(y)−v(y)`, with `f_v=(1−s_v)/2`. Write `N_−=#{y∈C: v(y)=−1}` and `N_+=140−N_−`.

## 2. Exact constructive iff (Theorem A)

**Lemma 1 (mod-4 parity identity).** Let `Y⊆V` and `ε:Y→{±1}`, and put `F(ξ)=Σ_{y∈Y}ε(y)(−1)^{ξ·y}`. Then for all ξ,
`F(ξ) ≡ |Y| − 2(N_−(ε)+ξ·P_Y) (mod 4)`.
*Proof.* Each term is `1−2J(y)`, where `J(y)=[ε(y)(−1)^{ξ·y}=−1]`, and `J(y)≡[ε(y)=−1]+ξ·y (mod 2)`. So `ΣJ≡N_−+ξ·P_Y (mod 2)`, and `2ΣJ (mod 4)` depends only on `ΣJ (mod 2)`. ∎
For `Y=C` and `ε=v` this is f848 (2.2): `v̂(ξ)≡140−2(N_−+ξ·P_C) (mod 4)`.

**Lemma 2 (reconstruction).** For every physical complement v the following hold.
(i) `s_v` is ±1-valued, since u and v have complementary supports and values ±1 there.
(ii) `#{x:s_v(x)=−1}=2·#{u=−1}+140`. Since `#{u=1}+#{u=−1}=116`, `Σu=0` gives `#{u=−1}=58`. So `f_v` is balanced for EVERY v, and conversely balance of `f_v` forces `Σu=0`.
(iii) `⊕supp f_v = P_C+(N_+ mod 2)T = P_C+(N_− mod 2)T`. Each `u=−1` pair contributes `y+(y+T)=T` (58 of them, even total). A point `y∈C` contributes `y` if `v(y)=−1` and `y+T` if `v(y)=+1`. Also 140 is even.
(iv) Because `V∩⟨T⟩={0}`: `⊕supp f_v=T` ⇔ `P_C=0` and `N_−` odd (f848 (2.1)).
(v) For `ξ∈K`, `W_{f_v}(ξ)=2û(ξ|_V)`, and `W_{f_v}(a0+ξ)=2v̂(ξ|_V)`. Use `ξ·T=0`, `(a0+ξ)·T=1` and `(a0+ξ)|_V=ξ|_V`.
So the 256 odd-half original Walsh values are exactly `2v̂`, and the even half `2û` is fixed by u. ∎

**Lemma 3 (convolution, any real v).** For every real `v` on V and every `λ∈V*`:
`Σ_ξ v̂(ξ)v̂(ξ+λ) = 256·(v²)^(λ)`.
*Proof.* Expand the sum as `Σ_{y,z}v(y)v(z)(−1)^{λ·z}Σ_ξ(−1)^{ξ·(y+z)}`. The inner sum is `256·[y=z]`. ∎

**Theorem A.** Fix u as above (only `|supp u|=116`, `Σu=0` and the fixed C are used). The following are equivalent.

(a) There exists a physical complement v such that `f_v` is balanced, `⊕supp f_v=T` (the selected T), and `|W_{f_v}(a)|≤28` for all 256 `a∈F₂⁹∖K`.

(b) There exists `k:V*→Z` with `k(ξ)∈{±1,±3,±5,±7}` for every ξ, and, for EVERY `λ∈V*` (all 256, including `λ=0`),
`Σ_{ξ∈V*} k(ξ)k(ξ+λ) = 64·Ĉ(λ)`.   (3.1)

Furthermore, `v↦k=v̂/2` and `k↦v=(1/128)Σ_ξ k(ξ)(−1)^{ξ·(·)}` (3.2) are mutually inverse bijections between the sets in (a) and (b). At `λ=0`, (3.1) reads `Σk²=64·140=8960`.

*Proof (a)⇒(b).* Put `k=v̂/2`. By Lemma 2(iv), `P_C=0` and `N_−` is odd. Lemma 1 then gives `v̂(ξ)≡140−2N_−≡2 (mod 4)`, so `k(ξ)` is an odd integer. Lemma 2(v) gives `|4k|=|W|≤28`, hence `|k|≤7`. Lemma 3 with `v²=1_C` gives `4Σk(ξ)k(ξ+λ)=256Ĉ(λ)`, which is (3.1).

*(b)⇒(a).* Define v by (3.2). It is rational-valued. Orthogonality gives `v̂(ξ)=(1/128)Σ_η k(η)·256·[η=ξ]=2k(ξ)`. Lemma 3 and (3.1) give `(v²)^(λ)=4·64Ĉ(λ)/256=Ĉ(λ)` for all λ. By Fourier inversion, `v²=1_C` **pointwise**. Since v is real, `v=0` off C and `v=±1` on C, so v is a physical complement. Lemma 1 now gives `k(ξ)=v̂(ξ)/2≡70−N_−−ξ·P_C≡N_−+ξ·P_C (mod 2)`. Every `k(ξ)` is odd. At `ξ=0` this forces `N_−` odd, and then every `ξ` gives `ξ·P_C=0`, so `P_C=0`. Lemma 2(iv) yields selected XOR T, Lemma 2(ii) yields balance, and Lemma 2(v) gives odd-half values `4k`, with `|4k|≤28`.

*Bijection.* Fourier inversion `v=(1/256)Σv̂χ=(1/128)Σkχ` gives uniqueness in both directions. ∎

**Scope remarks.** (1) (3.1) is 256 coupled quadratic equations in one 256-vector k. It is not a tally, not 256 independent amplitudes, and not a statement about any C other than the fixed actual one. (2) Even-half caps, ranks, zeros and the named I1–I6 conditions are properties of u. They must already hold, and (3.1) supplies none of them. (3) Solving (3.1) for a fabricated or projected C would not yield a named caller.

**Cross-check with the full-spectrum caller (S5).** Write `κ(a)=W(a)/4` on `F₂⁹`, so `κ(ξ)=û(ξ)/2` and `κ(a0+ξ)=v̂(ξ)/2=k(ξ)` for `ξ∈K`. S5 requires `Σ_a κ(a)κ(a+b)=2^14·1_{b=0}` for all b.

- For `b∈K`, the sum splits into an even part and an odd part. The even part is `Σ_{ξ∈K}κ(ξ)κ(ξ+b)=(1/4)Σûû(·+b)=64(u²)^(b)=64(256δ_b−Ĉ(b))`, using `u²=1−1_C`. The odd part is `Σ_ξ k(ξ)k(ξ+b)`. Since `64·256=2^14`, the S5 equation at `b∈K` is exactly (3.1).
- For `b=a0+b'∉K`, the sum is `2Σ_{ξ∈K}κ(ξ)κ(a0+ξ+b')=(1/2)Σ_ξ û(ξ)v̂(ξ+b')=128(uv)^(b')`. This vanishes because `uv≡0` once `v²=1_C`.

So, given the fixed u, (3.1) is precisely the odd-half residue of the complete Boolean caller.

## 3. Selected XOR for the actual C: P_C=0 is automatic in scope (R1, R2)

**Proposition B.** Let `u:V→{−1,0,1}` satisfy `û(ξ)≡û(0) (mod 4)` for every `ξ∈V*`. In scope this holds by I4, since every `û(ξ)∈4Z`. Then `P_{supp u}=0` and `P_C=0`.
*Proof.* Apply Lemma 1 with `Y=supp u` and `ε=u`. It gives `û(ξ)−û(0)≡−2ξ·P_{supp u} (mod 4)`, hence `ξ·P_{supp u}=0` for all ξ and so `P_{supp u}=0`. For `dim V=8≥2`, every coordinate equals 1 on exactly 128 vectors, so `P_V=0`. Since `C=V∖supp u`, it follows that `P_C=P_V+P_{supp u}=0`. ∎
(Consistency: Lemma 1 at `ξ=0` gives `#{u=−1}≡(116−û(0))/2 (mod 2)`. In original coordinates `û(0)=0`, so this is 58, which is even, as required.)

**Corollary B1.** In scope, for every physical complement v:
- `k(ξ)=v̂(ξ)/2≡N_− (mod 2)` for all 256 ξ, by Lemma 1 with `P_C=0`.
- Hence `⊕supp f_v=T` ⇔ `N_−` odd ⇔ `k(0)` odd ⇔ some `k(ξ)` odd ⇔ all `k(ξ)` odd.
- The first half (`P_C=0`) of f848's two-part condition (2.1) is satisfied automatically. Only the parity bit `N_−` is a genuine condition on v.
- `k(0)=Σv/2=70−N_−`. The single DC cap `|k(0)|≤7` therefore forces `N_−∈{63,65,…,77}` (eight odd values) and `N_+=70+k(0)`.

**Corollary B2 (weaker equivalent hypothesis in Theorem A).** In scope, (b) is equivalent to the following.

(b′) There exists a real `k:V*→R` with `|k(ξ)|≤7` for every ξ, (3.1) for every λ, and `k(0)` an odd integer.

*Proof.* (b)⇒(b′) is immediate. For (b′)⇒(b), define v by (3.2). As in Theorem A, `v²=1_C`, so `v̂(ξ)` is a sum of 140 terms ±1, hence an even integer, and `k=v̂/2∈Z`. Lemma 1 and Proposition B give `k(ξ)≡N_−≡k(0)≡1 (mod 2)`. With `|k|≤7` this is the eight-value set. ∎
Integrality is therefore a consequence of (3.1). The condition `k(0)` odd is not removed. An all-even solution would be a v with `N_−` even and reconstructed support XOR `0≠T`. No claim is made about whether such solutions exist.

**Proposition B′ (coordinate form; reconstruction of f848 §4).** Assume I3 and I5. Put `C_c={w:(c,w)∈C}` and `S={c:|C_c|=1}`. By I5 this is exactly `{c:a(c)≠0}`: a block with transform energy `ΣU_s²=4·#{nonzero entries}` has 3 nonzero entries iff `U1=±3`. Let `γ_c` be the point of `C_c` for `c∈S`, and `δ_c=w+w'` for `C_c={w,w'}`. Full fibres XOR to `0+h+h'+(h+h')=0` and empty fibres to 0. The linear coordinates give f848 (4.1):
`P_C=(⊕_{c∈S}c, ⊕_{c∈S}γ_c+⊕_{|C_c|=2}δ_c)`.
In scope, each of the three terms vanishes separately.

(i) `⊕_{c∈S}c=0`. This is f848's argument, reconstructed. `â(0)−â(r)=2Σ_{c∈S,r·c=1}a(c)`, and `â(0)−â(r)∈{0,±8}` because `|â|=4` (I4). So the sum is ≡0 (mod 4), and since its summands are ±1, their number is even. Hence `r·⊕S=0` for every r.

(ii) `⊕_{c∈S}γ_c=0`. This is new.
- On `c∈S`, three ±1 terms sum to `U1=±3`, so `u(c,w)=a(c)(−1)^{s_1·w}` for `w≠γ_c`. Then `U_s(c)=a(c)[4·[s=s_1]−(−1)^{(s_1+s)·γ_c}]`, so `U0(c)=−a(c)(−1)^{s_1·γ_c}`, `U3(c)=−a(c)(−1)^{s_2·γ_c}` and `U2(c)=−a(c)(−1)^{s_3·γ_c}`.
- `Π_S a=+1`: `Σ_S a=â(0)=±4` gives `#{a=−1}=(16∓4)/2∈{6,10}`.
- `Π_S U0=+1`: `Σ_c U0(c)=û(0)≡0 (mod 4)` (I4; it equals `Σu=0` in original coordinates). Off S, `U0∈{0,±2,±4}` (I5), and the number n of off-S blocks with `|U0|=2` obeys `4n+16n'=56−16=40`, so `n=10−4n'` is even. Hence `Σ_S U0≡0 (mod 4)`. Since `Σ_S U0=16−2#{c∈S:U0(c)=−1}`, that number is even.
- `Π_S U3=+1` by the same argument: `Σ_c U3(c)=û(0,s_3)≡4 (mod 8)`, and `4n+16n'=128−16=112` gives `n=28−4n'`, which is even.
- Hence `(−1)^{s_1·⊕γ}=Π_S(−aU0)=(−1)^{16}·1·1=1`, and likewise `(−1)^{s_2·⊕γ}=Π_S(−aU3)=1`. Since `s_1,s_2` span `P≅(F₂²)*`, `⊕γ=0`.

(iii) `⊕δ_c=0`, and all `n_i` are even. Let `h^(i)` be the nonzero vector of `ker s_i`, and `n_i` the number of pair fibres of direction `h^(i)`. Proposition B with (ii) gives `n_1h^(1)+n_2h^(2)+n_3h^(3)=0`, i.e. `n_1≡n_2≡n_3 (mod 2)`. With `Σn_i=28` (in scope, `H=0`), all three are even. For a general d the pair count is `28−2d`, which is still even, so the conclusion persists.

(iv) Independent count derivation (R2). A `U1=0` block with ±2 entries `α,β` at slots `s,s'` has `u(c,w)=(1/2)(−1)^{s·w}[α+β(−1)^{(s+s')·w}]`. It is nonzero exactly on one coset of `ker(s+s')`, so its C-fibre is the other coset, and its direction is the nonzero vector of `ker(s+s')`. Since `0+s_2=s_2`, `0+s_3=s_3` and `s_2+s_3=s_1`:
- D0 (slots 0,2) has direction `h^(2)`;
- Z2 (slots 0,3) has direction `h^(3)`;
- D3 (slots 2,3) has direction `h^(1)`.
By I5, `(n_1,n_2,n_3)=(18+2d,4−2d,6−2d)`. This is even for every d and equals `(18,4,6)` at local `H=d=0`, agreeing with (iii) by a disjoint route.

*Consequence.* In f848 §4's dichotomy only the "all even" branch occurs, and there its requirement `⊕γ=0` holds automatically. f848's "computable selected-XOR obstruction" therefore never excludes an in-scope u. It stays a valid necessary condition only for ternary u outside I4/I5. This corrects the emphasis of f848, not any of its equations.

## 4. Original section, gauge transport and parity (exact)

**4.1 Affine gauge.** Take invertible A on V, `b∈V`, `ε,ε'∈{±1}` and `β,β'∈V*`. Let `u_N(z)=ε(−1)^{β·z}u_O(Az+b)` and `v_N(z)=ε'(−1)^{β'·z}v_O(Az+b)`. Write `A^{-*}` for the dual of `A^{-1}`, so that `η·A^{-1}y=(A^{-*}η)·y`. Substituting `y=Az+b` gives:
- `C_N=A^{-1}(C_O+b)` and `P_{C_O}=A·P_{C_N}+140·b=A·P_{C_N}`.
- `û_N(ξ)=ε(−1)^{(ξ+β)·A^{-1}b}û_O(A^{-*}(ξ+β))`. In particular `û_N(β)=ε·û_O(0)=0`. The original balance lands at the **specific** frequency β (for `β=(t,0)`, at `Û0_N(t)=0`), never at a zero chosen afterwards. Residues mod 4 are preserved, so Proposition B holds in every such gauge, consistent with `P_{C_O}=A·P_{C_N}`.
- `v̂_N(ξ)=ε'(−1)^{(ξ+β')·A^{-1}b}v̂_O(A^{-*}(ξ+β'))`. Hence `k_N(ξ)=±k_O(A^{-*}(ξ+β'))`: all 256 magnitudes are permuted, and caps and parities transport.
- `Ĉ_N(λ)=(−1)^{λ·A^{-1}b}Ĉ_O(A^{-*}λ)`. With `η=A^{-*}(ξ+β')`, `Σ_ξk_N(ξ)k_N(ξ+λ)=(−1)^{λ·A^{-1}b}Σ_ηk_O(η)k_O(η+A^{-*}λ)=64Ĉ_N(λ)`, so (3.1) transports exactly.
- `Π_{C_N}v_N=ε'^{140}(−1)^{β'·P_{C_N}}Π_{C_O}v_O`. So `N_−^N≡N_−^O+β'·P_{C_N} (mod 2)`. This is f848's statement, and by Proposition B it is now unconditionally parity-preserving in scope.

These are statements about transported pairs on V. They do not assert that a normalized pair is the even/odd half of an original caller. Original coordinates, T and the transported balance frequency must be carried throughout.

**4.2 Original section change.** Let `a0'=a0+κ` with `κ∈K`, and `V'=a0'⊥`. The map `φ(y)=y+(κ·y)T` is a linear isomorphism `V→V'`: `a0'·φ(y)=κ·y+(κ·y)=0`. Since `{φ(y),φ(y)+T}={y,y+T}`, we get `u'∘φ=u` and `v'∘φ=(−1)^{κ·y}v`. Then:
- `P_{C'}=P_C+(κ·P_C)T` and `N'_−≡N_−+κ·P_C (mod 2)`. Both are invariant when `P_C=0`, which is automatic in scope.
- Index frequencies by K. Then `Ĉ'(λ)=Ĉ(λ)` (because `λ·T=0`), and `k'(λ)=W(a0'+λ)/4=k(λ+κ)` is a translate. (3.1) is translation-invariant in ξ.

So Theorem A, Proposition B and Corollary B1 are independent of the section. This matches the intrinsic meaning: `⊕supp f_v` and the odd-coset Walsh values depend only on f.

## 5. Overlap, deficiency and derivative energy (f848 §5 reconstructed; constants checked)

Throughout, k solves (3.1) with odd entries, `|k|≤7`, and v is its physical complement.

**5.1 Tally.** Let `N2,N6,N10,N14` count `|k|=1,3,5,7`. Then:
- `N2+N6+N10+N14=256` and `N2+9N6+25N10+49N14=8960`.
- Subtracting 25 times the first: `−24N2−16N6+24N14=2560`, i.e. `3(N14−N2)−2N6=320`.
- Reducing mod 3: `N6≡2`.
- `N14=N2+(320+2N6)/3≥108`, with equality iff `(N2,N6)=(0,2)`. Then `N10=146`; check: `18+3650+5292=8960`.
- Always `N6+3N10+6N14=(8960−256)/8=1088`.

**5.2 Overlap and derivative.** Put `r(h)=|C∩(C+h)|` and `D(h)=Σ_y v(y)v(y+h)`. For `h≠0`:
- `y↦y+h` is a fixed-point-free involution of `C∩(C+h)`, so r is even.
- Inclusion–exclusion gives `r≥2·140−256=24`, and trivially `r≤140`.
- The `r/2` unordered pairs each contribute ±2, so `D=r−4m` with `0≤m≤r/2`, where m is the number of pairs with opposite signs.
At `h=0`, `r(0)=D(0)=140`.

**5.3 Deficiency.** Put `d=(49−k²)/8`, which is `6,5,3,0` for `|k|=1,3,5,7`. Then `Σd=(49·256−8960)/8=448`. The same computation as Lemma 3 gives `Σ_ξ v̂(ξ)²(−1)^{ξ·h}=256D(h)`, i.e. `Σ_ξ k²(−1)^{ξ·h}=64D(h)`. For `h≠0`:
- `Σ(49−8d)(−1)^{ξ·h}=−8Σd(−1)^{ξ·h}`, so `D(h)=−(1/8)Σ_ξ d(ξ)(−1)^{ξ·h}=M(h)/4−56`, where `M(h)=Σ_{ξ·h=1}d`.
- Hence `M=4D+224=4r−16m+224≡4r (mod 16)`, since `224=14·16`.
- From `D∈[−r,r]` and `0≤M≤448`: `max(0,224−4r)≤M≤min(448,224+4r)`, and `|D|≤min(r,56)`.
- If `r≡2 (mod 4)`, then `D≡2 (mod 4)`, so `D≠±56` and `|D|≤54`. This matters only when `r≥56`.
All of these hold simultaneously for the one placement `ξ↦d(ξ)` and the one actual function r.

**5.4 Derivative energy.** D has transform `v̂²`, so Parseval gives `Σ_hD²=(1/256)Σv̂⁴=(1/16)Σk⁴`. For `x=k²∈{1,9,25,49}`, `x²=74x−1225+(x−25)(x−49)`, and the last factor equals `1152,640,0,0`. Hence:
- `Σk⁴=74·8960−1225·256+1152N2+640N6=349440+1152N2+640N6`;
- `Σ_{h≠0}D(h)²=21840+72N2+40N6−140²=2240+72N2+40N6≥2320`.
Equality holds iff `(N2,N6)=(0,2)`, i.e. exactly the formal tally `(0,2,146,108)`; recall `N6≥2` from `N6≡2 (mod 3)`.

Additional exact identities (new, R3):
- `D̂(ξ)=v̂(ξ)²=4k(ξ)²∈{4,36,100,196}` at all 256 ξ.
- `Σ_{h≠0}D(h)=4k(0)²−140` and `Σ_{h≠0}r(h)=140²−140=19460`.
- Each opposite-sign unordered pair `{y,z}⊆C` is counted once, at `h=y+z`. So `Σ_{h≠0}m(h)=N_+N_−=4900−k(0)²`, consistent with `Σ(r−D)=4Σm`. This is odd in scope.

**5.5 Within-block shifts (f848 (5.6), sharpened by R2).** For `h=(0,h^(i))`, a full fibre contributes 4 to r, a pair fibre of direction `h^(i)` contributes 2, and every other fibre contributes 0. So `r(0,h^(i))=68+2n_i`. In scope `(n_1,n_2,n_3)=(18,4,6)`, which gives `r=104,76,80`. All three are ≡0 (mod 4), so only `|D|≤56` applies. The number of disagreeing pairs `m=(r−D)/4` and of agreeing pairs `r/2−m=(r+D)/4` are each at least `(r−56)/4=12,5,6`. f848's `3+⌈n_i/2⌉` is confirmed, and the total over the three directions is exactly 23. f848's "24 when two are odd" case cannot occur in scope.

## 6. Four-fibre saturation congruences (f848 §6 reconstructed; new per-direction identity)

**6.1** Put `V_s(c)=Σ_w v(c,w)(−1)^{s·w}`. Then `v̂(r,s)=Σ_cV_s(c)(−1)^{r·c}`, and six-dimensional Parseval gives `Σ_rk(r,s)²=(1/4)·64·Σ_cV_s²=16E_s`, where `E_s=Σ_cV_s(c)²`. By fibre type:
- a singleton gives `V_s=±1`;
- a pair `{w,w+δ}` gives `V_s=(−1)^{s·w}[v_1+v_2(−1)^{s·δ}]∈{0,±2}`;
- a full fibre gives `V_s∈{0,±2,±4}`;
- an empty fibre gives 0.

So `E_s=16+4b_s+16p_s`. With `A_s+B_s+C_s+D_s=64`:
- `A_s+9B_s+25C_s+49D_s=256+64b_s+256p_s`;
- `B_s+3C_s+6D_s=24+8b_s+32p_s≡0 (mod 8)` for each of the four s. These are (6.1)–(6.2).
- Summing over s gives 1088 for every o, matching 5.1.

**6.2** On a full fibre, `Π_w v(c,w)(−1)^{s·w}=Π_w v(c,w)` because `Σ_{w∈F₂²}w=0`.
- With an odd number of negatives, every `V_s` is a sum of four ±1 with odd −1 count, so `|V_s|=2` for all four s.
- With an even number, `V_s∈{0,±4}` and `ΣV_s²=16`, so there is exactly one `|V_s|=4`.
- A pair fibre has exactly two s with `|V_s|=2`.
Hence `Σ_sb_s=56+4o`, `Σ_sp_s=17−o` and `0≤o≤17`; this is (6.3). Also `Σ_sE_s=4·140=560`.

**6.3 New per-direction identity.** For a pair fibre of direction `h^(i)`, `s·h^(i)=0` iff `s∈{0,s_i}`. Let `q_i` be the number of its disagreeing pair fibres. Then:
- `b_0=28−Σq+o` and `b_{s_i}=(n_i−q_i)+Σ_{j≠i}q_j+o`. These sum to `56+4o`.
- The four-point autocorrelation gives `Σ_wv(c,w)v(c,w+h)=(1/4)Σ_sV_s(c)²(−1)^{s·h}`. Hence
`D(0,h^(i))=(1/2)(E_0+E_{s_i})−140=2(b_0+b_{s_i})+8(p_0+p_{s_i})−124`.
- Combined with `|D|≤56`, this gives `34≤b_0+b_{s_i}+4(p_0+p_{s_i})≤90` for each i, with `b_0+b_{s_i}=28+n_i−2q_i+2o` even. These are new necessary four-fibre inequalities.

Written check of the constant: take the formal all-plus sign choice on the actual C. It is not a capped complement (`N_−=0`, `k(0)=70`). It gives `q=0`, `o=0`, `p_0=17`, `b_0=28` and `b_{s_i}=n_i`, so `D=68+2n_i=r`, as it must when every pair agrees. This is a constant check only, not evidence about any v.

**6.4 Boundary.** If `N14=108`, then `N2=0`, so every `A_s=0`. Substituting `D_s=64−B_s−C_s` gives `384−5B_s−3C_s≡0`, i.e. `5B_s+3C_s≡0`, and multiplying by 5 gives `B_s≡C_s (mod 8)` for each s; this is (6.4). Further, `ΣB_s=N6=2` and `ΣC_s=146≡2 (mod 8)`. This is consistent, and still a necessary description, not a witness.

## 7. Boundary cases (all handled)

- **λ=0 and h=0.** (3.1) includes `λ=0`, i.e. `Σk²=8960`. Sections 5.2–5.5 are for `h≠0`. The `h=0` terms (`r=D=140`, `M` not used) enter only in 5.4 and in the identities of 5.4/6.2.
- **Parity of v.** Every v with `N_−` even is excluded (Corollary B1). An example is the all-plus formal choice of 6.3. The DC cap alone pins `N_−∈{63,…,77}` odd.
- **`P_C≠0`.** This never occurs for an in-scope actual C (Proposition B). f848's "complement with `P_C≠0`" exclusion is vacuous there.
- **Tally boundary.** `N14=108` ⇔ `(0,2,146,108)` ⇔ `Σ_{h≠0}D²=2320`. At that boundary (6.4) applies with `ΣB_s=2`.
- **o extremes.** Both `o=0` and `o=17` are compatible with (6.3), and `Σ_s(B+3C+6D)=1088` for every o.
- **`r≡2 (mod 4)` sharpening.** It applies only to shifts with `r≡2`. All three within-block shifts have `r≡0 (mod 4)`.
- **d ≠ 0.** Outside local `H=0`, the n's are `(18+2d,4−2d,6−2d)`. They are still even, but the exact r-values of 5.5 are specific to `d=0`.
- **Affine gauge with b≠0.** `P_{C_O}=A·P_{C_N}` uses `|C|` even, and balance sits at `β`, not at a reselected zero.
- **Section change.** It translates k by κ, while `Ĉ` and the parities are unchanged.
- **Branches.** Both six-span branches, together `(4;0,4,4,4)` and split `(4;2,2,4,4)`, are covered verbatim. No statement here depends on, constructs or excludes either one.

## 8. Result limits

- No actual u in either branch, and no 256-entry k solving (3.1), is exhibited or ruled out. Theorem A is a constructive decision criterion **in principle**; no search was run.
- A formal tally, an independently placed spectrum, or a solution of (3.1) for a projected C is not a physical v. Only the fixed actual u and its C are quantified.
- I1–I6 remain named conditional imports exactly as listed. These include the f244 atom/source/class correspondences, the explicit local-H definition, the even-half spectra and block forms, and the linked five-span no-go bodies, none of which were opened. Proposition B needs only the residue part of I4. B′(ii)–(iv) need I3/I5 as well.
- No witness, no global NL242 statement, no exclusion of any branch, no source/historical-class identity, no novelty or publication priority, and no human/independent-family/formal/kernel acceptance is claimed.

## 9. Ledger of f848 (S1) claims in the assigned scope

| f848 claim | Status here |
|---|---|
| §1 fibre counts 16/28/3/17, `#C=140`, `S=supp a`; 28 = D0 4 + D3 18 + Z2 6 | Reconstructed from I5 (import). |
| §2 ±1 reconstruction; balance ⇔ `Σu=0`; 58 negative u-pairs; XOR formula; (2.1) | Reconstructed (Lemma 2). |
| (2.2) and "all 256 `v̂/2` odd ⇔ (2.1)" | Reconstructed (Lemma 1). Refined: in scope equivalent to `k(0)` odd (B1). |
| Gauge: `û_N(β)=εû_O(0)`, `P_{C_O}=AP_{C_N}`, parity change `(−1)^{β·P_{C_N}}`; section change | Reconstructed with exact formulas (4.1–4.2). Parity invariance is unconditional in scope (Proposition B). |
| Theorem (3.1)/(3.2): eight-value integer k, `64Ĉ`, `1/128`, pointwise `v²=1_C`, selected T, caps, bijection, `Σk²=8960` | Reconstructed (Theorem A, both directions). Refined (B2): integrality automatic, one odd coefficient suffices. Cross-checked as the exact odd-half residue of the S5 full caller. |
| Branch-wise conditional frontier | Consistent, conditional on I1–I6. |
| (4.1); first coordinate `⊕S=0` | Reconstructed. |
| §4 parity dichotomy and "obstruction" | Equations correct, but **vacuous in scope**: `⊕γ=⊕δ=0` and all `n_i` are even (Proposition B′, two disjoint routes). It can never exclude an in-scope u. Emphasis correction only. |
| (5.1) constants, unique tally `(0,2,146,108)` | Reconstructed. |
| (5.2)–(5.4): r even, `24≤r≤140`, `D=r−4m`, `d∈{0,3,5,6}`, `Σd=448`, `D=M/4−56`, `M≡4r (16)`, bounds, `abs(D)≤min(r,56)`, 54-sharpening | Reconstructed. |
| (5.5) `2240+40N6+72N2≥2320`, equality iff tally | Reconstructed (interpolation identity). |
| (5.6) `68+2n_i`, `3+⌈n_i/2⌉`, `23+#odd/2` | Reconstructed. Refined: `r=104,76,80`, bounds `12,5,6`, total exactly 23; the "24" case is vacuous. |
| (6.1)–(6.3) `256+64b+256p`, `24+8b+32p`, mod 8, `56+4o`, `17−o` | Reconstructed. New per-direction identity and inequalities (6.3). |
| (6.4) `C_s≡B_s (mod 8)` at `N14=108` | Reconstructed. |
| §7 remaining gap and non-claims | Agreed. |

No f848 equation or constant in scope was found false. The one substantive correction is that §4 is a necessary condition that holds automatically, not an obstruction.

## 10. Read and process declaration

- **Administrative reads.** Before any body access I read completely the manifest (`eb1e0e2f…`), freeze receipt (`7d6744fb…`), final binding (`b5dd021e…`), live metadata (`2a16051d…`) and actual dispatch receipt (live `2657800c…`). I also read all 22 manifest-listed status-only controls. Every live sha256 matched its pin (computed with `shasum -a 256`). Controls were used for status and permissions only, never as mathematical input.
- **Prebody ACK.** I wrote `prebody-ack-v1.md` (3776 B) exclusively and delivered the ACK directly to Main ("Delivered to Main") before any body read.
- **Packet read.** I then read the sole part `literal-packet-part-01-v1.md` (sha `6eddba41…`, 457 LF, 67617 B) completely and in order, as 23 raw windows: LF 1–20, 21–40, …, 421–440, 441–457. These include every source ending: S1 LF 1–146, S2 1–46, S3 1–27, S4 1–37, S5 1–162, S6 1–13, and terminal blank LF 457. Each window had ≤20 LF. Its byte size was precomputed by a line-length count of at most 5838 B (all <30000 B). No raw display was clipped and no recovery was needed.
- **One extra display.** After the complete read, one non-raw numbered display of LF 438–448 (tool header context 275–276) confirmed the S5/S6 boundary and the terminal LF. That display truncated LF 446 at 768 characters, but LF 446 had already been read whole in the raw window 441–457.
- **Sources.** S1–S6 were read only through the packet. No link target, unlisted file, held episode, held consumer, sibling output or old code was opened.
- **No execution.** There was no network, external model, scientific execution, test, compilation, solver, child subprocess, Git, deletion or cleanup. The only shell commands were `date -u`, `ls`, `shasum -a 256` and the window byte count, all administrative. No code was prepared: **no prepared code hash**.
- **Fresh instance.** The one written instance is the formal all-plus sign check in 6.3, disclosed there. No private selected instance was used.
- **Composition.** This file was composed by an initial write, one correction of the (b)⇒(a) parity sentence and the S5 cross-check wording, three appends, one cosmetic table-cell fix (pipes inside code replaced by `#C`/`abs`), one d-caveat in 3(iii), and this declaration update, all before return. One mis-anchored caveat edit briefly overwrote the last bullet of 3(ii). The next edit restored that bullet verbatim from my own preceding raw display. No frozen or previously returned file was edited.
- **Discarded attempt.** One earlier response, made after the complete packet read and before this file existed, was discarded by the harness at an output-token limit. None of its planned tool calls ran, and no file or message came from it.
- **Other deviations.** No other process deviation is known.

Clock observed before writing these final sections: 2026-10-31T03:34:56Z.
