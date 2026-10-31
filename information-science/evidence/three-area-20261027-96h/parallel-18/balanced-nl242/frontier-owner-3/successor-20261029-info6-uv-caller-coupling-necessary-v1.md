# The two-half caller at the T-split: complete nonzero-shift interface and new XOR couplings for the f244 (G₃,H)=(1,0) residual

**SAME-SLOT CONTEXT-ROTATION WRITTEN MANUSCRIPT (partial, necessary-consequence package + formulation closure).** Native clock observed before writing: **2026-10-29T18:22:41-0700 PDT**. Owner InfoBalancedNL242-3, slot info-6, release `written-releases/info6-owner3-continuation-v1.json` SHA-256 `5f77b9eaaa69d7b342e66b1445c681d32861bbff0c382b5eadb9935184fb6484`. This packet contains fresh all-variable WRITTEN mathematics on the ORIGINAL balanced nine-variable NL≥242 existence-or-global-exclusion question, at the actual Boolean/full-caller interface of the frozen f244 scope: balanced f on F₂⁹, `max|W_f|≤28`, even polar of rank two, exactly eight Walsh zeros, `m=116`, `(e₁,e₂,e₃)=(0,4,8)`, `T≠0`, `q⁻¹(0)=R`, residual `G₃=1` with H the explicit local count of U₁=0 blocks carrying a single |U₀|=4 peak, taken to be 0. **No witness, no exclusion of the residual, the (0,4,8) case, rank two, or the global target is claimed; every result below is a necessary condition on the actual original object or an exact reformulation of it.** No historical H-label equivalence is used or asserted. No code, test, solver, search, model CLI, Git, deletion or publication was performed. The withdrawn P1 roster, f239/CR7, held enumerator extensions, the unreviewed m=114 cross-fibre draft and all unlisted bodies are NONINPUT; standing STOP/HOLD/ZERO/NONINPUT controls remain binding.

## 0. What is new here, stated plainly

1. **The complete caller at the T-split is derived from the Boolean object alone** (Theorem 1): `W_f` on `K=T^⊥` is exactly twice the V-Walsh transform of the even half u, and `W_f` on the whole nonzero-shift coset `K+a₀` is exactly twice the V-Walsh transform of the odd half v — the off-K caller involves **only** v. The frozen packet quoted "odd-half k is odd" from a caller disposition that is not an input body here; this packet derives the full interface, proves global mod-4 divisibility from balance, and reduces the odd-half congruence structure to XOR self-consistency (Theorems 2–3).
2. **Two new necessary conditions on the even half u alone** (Theorem 3): with D the set of 16 blocks where `|U₁|=3` and `z₀(c)` the unique zero of u in block c,
   - **(N1)** `⊕_{c∈D} c = 0` in R*;
   - **(N2)** `⊕_{c∈D} z₀(c) = 0` in P*.
   These are absent from the f244 disposition, the f255 correction and the f263 parent adoption; they are forced by T-self-consistency of the original object together with the adopted caller congruence.
3. **A v-side necessary taxonomy and exact ledgers** (Theorems 3 and 5): the complementary half's block transforms W_s are odd exactly on D; per-fibre congruences `Σ_c W_s(c) ≡ 2 (mod 4)`; the class-forced pair-gap constants δ; per-fibre and global spectrum ledgers.
4. **The interface equivalence** (Theorem 6): the residual question is *exactly* the conjunction of the frozen u-side problem, a bounded sign problem for v on the u-determined complement Ω, and the couplings (N1),(N2), odd positive-count p. This is the requested closure of the *coupling formulation*; the existence sides remain open and are stated as such.

Everything is labeled: PARTIAL. No selected function, spectrum, atom assignment, index tuple or diagnostic appears; all objects below are universally quantified over the frozen scope.

## 1. The T-split interface and the complete caller

Let f: F₂⁹→F₂ be balanced with `max|W_f|≤28`, `s(x)=(−1)^{f(x)}`, and let `T=⊕_{x∈supp f}x`. At the frozen scope `T≠0` is adopted. Fix `a₀` with `a₀·T=1` and let `V=a₀^⊥`, a **linear** hyperplane with `T∉V`, so `F₂⁹=V⊕⟨T⟩` and every x is uniquely `y+εT` with y∈V. Define on V

`u(y)=[s(y)+s(y+T)]/2 ∈ {−1,0,1}`,  `v(y)=[s(y)−s(y+T)]/2 ∈ {−1,0,1}`.

Then pointwise `u(y)v(y)=0`, `u(y)²+v(y)²=1`, `s|_V=u+v`, `s|_{V+T}=u−v`; `m=|supp u|=116` (adopted) and `|supp v|=256−116=140`. Characters of V are restrictions of characters of F₂⁹, and `a`, `a+a₀` restrict identically; since `K∩⟨a₀⟩=0` and both sides have 256 elements, **restriction identifies K=T^⊥ with the full dual V***.

**Theorem 1 (complete caller split).** With `Û(r)=Σ_{y∈V}u(y)(−1)^{r·y}` and `V̂(r)=Σ_{y∈V}v(y)(−1)^{r·y}` for r∈K≅V*:

`W_f(r)=2Û(r)` for r∈K;  `W_f(r+a₀)=2V̂(r)` for r∈K.

*Proof.* Pair x=y and x=y+T. For r∈K the phases agree: each pair contributes `(−1)^{r·y}[s(y)+s(y+T)]=(−1)^{r·y}·2u(y)`. For a=r+a₀ the phases differ by `(−1)^{a·T}=−1`: each pair contributes `(−1)^{r·y}[s(y)−s(y+T)]=(−1)^{r·y}·2v(y)`. Summing over y∈V gives both identities. ∎

**Corollary 1 (both-half cap decoupling).** `NL(f)≥242 ⟺ max_{r∈K}|Û(r)|≤14 AND max_{r∈K}|V̂(r)|≤14`. The first cap is the entire frozen f244/f263 u-side problem (`Û=2k` with the adopted k-structure); the second cap is a new, independent condition on v alone. Neither half's Walsh values involve the other half at any point: `Σ_r Û(r)V̂(r)=256·Σ_y u(y)v(y)=0` (Fourier-orthogonal halves).

**Lemma 1 (global mod 4).** For balanced f on F₂⁹, `W_f(a)≡0 (mod 4)` for every a. *Proof.* `W_f(a)−W_f(0)=−2·Σ_{a·x=1}(−1)^{f(x)}`, and the inner sum runs over 2⁸=256 signs, hence is even; `W_f(0)=0` by balance. ∎

Consequently `Û` and `V̂` are even everywhere, `k(a)=W_f(a)/4` is integral on all of F₂⁹, on K it is the frozen even k (`k∈{0,±2,±4,±6}` with the eight zeros in the s=0 fibre and `q=k/2 mod 2`), and off K `k=V̂/2`.

**Parseval cross-check (exact).** `Σ_{r∈K}W_f(r)²=4·256·Σu²=1024·116=118784` and `Σ_{r∈K}W_f(r+a₀)²=4·256·Σv²=1024·140=143360`; the total is 262144=2¹⁸ as it must be. On the u-side, `Σ_r k(r)²=7424` splits over fibres as `896+2304+2176+2048` (s=0,1,2,3: 56 values ±4 and 8 zeros; 64 values ±6; 4 values ±2 and 60 values ±6; 8 values ±2 and 56 values ±6), consistent with `4·7424=29696=256·116`. On the v-side `Σ_{(r,s)}V̂(r,s)²=35840`.

## 2. XOR self-consistency of T

T is not free data: it is the XOR of the support of the very f being decomposed.

**Theorem 2 (XOR/balance coupling).** Let `p=#{y∈V: v(y)=+1}` (so `#{v=−1}=140−p` and `Σ_y v(y)=2p−140`). Then necessarily:

(i) **p is odd**; equivalently `Σ_y v(y)≡2 (mod 4)`;
(ii) `⊕_{y∈supp v} y = 0` in V.

Moreover `W_f(a₀)=2(2p−140)`, so `|2p−140|≤14` and `p∈{63,65,67,69,71,73,75,77}`, with `k(a₀)=p−70∈{±1,±3,±5,±7}` odd.

*Proof.* Split `T=⊕_{x∈supp f}x` over the 256 pairs {y,y+T}, y∈V. Each pair contributes `f(y)·y ⊕ f(y+T)·(y+T) = [f(y)⊕f(y+T)]·y ⊕ f(y+T)·T`, an identity valid in all four cases (both 1: `0·y⊕T`; both 0: `0`; f(y)=1 only: `y`; f(y+T)=1 only: `y⊕T`). Summing over pairs,

`T = (⊕_{y: f(y)≠f(y+T)} y) ⊕ p·T`,   p := #{y∈V: f(y+T)=1}.

Here `f(y)≠f(y+T)` exactly on `supp v` (that is what `v≠0` means), and `p=#{v=+1}`, since `v(y)=+1` means `s(y)=+1, s(y+T)=−1`, i.e. `f(y)=0, f(y+T)=1`, while `v(y)=−1` gives `f(y+T)=0`. Hence `⊕_{y∈supp v} y = T⊕pT = (1+p)T`. The left side lies in the linear space V while `T∉V`; if p were even the right side would be `T∉V`, impossible. So p is odd, and then `(1+p)T=0`, giving (ii). Finally `W_f(a₀)=2V̂(0)=2Σ_y v(y)=2(2p−140)` by Theorem 1; Lemma 1 forces this ≡0 (mod 4), confirming `Σv≡2 (mod 4)`, i.e. (i) ⟺ p odd; the cap gives `|2p−140|≤14`. ∎

**Reconstruction direction (exact converse structure).** Conversely, let any pair u,v on V with values in {−1,0,1}, `uv=0` pointwise, `Σ_y u(y)=0`, p odd and `⊕_{supp v}y=0` be given, and define s on V by `u+v` and on V+T by `u−v`, `f=(1−s)/2`. Then f is balanced (`Σ_{F₂⁹}s=2Σu=0`), `W_f` is given by Theorem 1, and the XOR of supp f equals `(⊕_{supp v}y)⊕pT=T`, i.e. the construction is self-consistent. **So the couplings in this section are exactly equivalent to T-self-consistency — nothing more and nothing less.**

## 3. Block taxonomy of the complementary half

Use the shared coordinates of the adopted correction: `K=R⊕P` with `dim R=6`, P≅F₂² labelled 0,1,2,3 (q vanishes only at s=0), `V≅R*⊕P*`, block transforms `U_s(c)=Σ_z u(c,z)χ_s(z)` and, newly, `W_s(c)=Σ_z v(c,z)χ_s(z)` with `χ_s(z)=(−1)^{s·z}`; `Û(r,s)=Σ_c U_s(c)(−1)^{r·c}`, `V̂(r,s)=Σ_c W_s(c)(−1)^{r·c}`.

**Adopted u-side facts used verbatim** (f244 disposition + f255 correction + f263 parent, at (G₃,H)=(1,0)): counts `A₁=16, C₂=4, C₃=6, D₁=18, G₂=2, G₃=1, H=0, O=17` summing to 64; `U₁∈{0,±3}` with exactly 16 nonzero blocks; `t₁=0` (e₁=0) so `U₁=3·Walsh_R(σ₁)/16`; energies `ΣU₀²=56`, `ΣU_s²=144−2e_s` (144,136,128); in the 48 blocks with `U₁=0` the values `U₀,U₂,U₃` are even and each block is all-zero (O), a ±2-pair at one of `(U₀,U₂),(U₀,U₃),(U₂,U₃)` (C₂,C₃,D₁), or a single ±4 peak among `U₀,U₂,U₃` (H=0, G₂, G₃); `{U₂=0}=H₂∖F₂`, `H₂=H_*`, `|F₂∩B₃|=2`, and the f263 cross-fibre conditions (XOR/sign equality, all-t overlap bound (C), sign condition (S)).

**Theorem 4 (per-block complementary structure, forced).** Complementarity `uv=0`, `u²+v²=1` forces, per block:

- **A₁ blocks** (c∈D, `|U₁(c)|=3`, sixteen): the u-block is `u(c,z)=ε_c χ₁(z)` on the three z≠z₀(c) and 0 at `z₀(c)` (alignment with ±χ₁ is forced by `|U₁|=3`); hence v is supported on the single point `(c,z₀(c))` with value `δ_c=±1`, and `W_s(c)=δ_c χ_s(z₀(c))`: **odd**, of magnitude 1, for all four s.
- **C₂/C₃/D₁ blocks** (28): u occupies a 2-set `{z₁,z₂}`, v the complementary 2-set `{z₃,z₄}`; writing `δ_c=z₁+z₂=z₃+z₄≠0`, the class forces δ_c: for C₂, `s·δ_c=0 ⟺ s∈{0,2}`; for C₃, `⟺ s∈{0,3}`; for D₁, `⟺ s∈{0,1}` — i.e. **δ_c is the same vector for every block of a given class**. The v-block transform is `W_s(c)=η₃χ_s(z₃)+η₄χ_s(z₄)∈{0,±2}`, with `|W_s|=2` exactly on `{s: χ_s(δ_c)=η₃η₄}`: the same fibre-pair as u if `η₃η₄=+1`, the complementary pair if `−1`. (For C₂ the options are {0,2} or {1,3}; C₃: {0,3} or {1,2}; D₁: {0,1} or {2,3}.)
- **G₂/G₃ blocks** (3): u has four ±1 entries aligned to the peaking character, so **v≡0 on the block** and `W_s(c)=0` for all s.
- **O blocks** (17): `u≡0`, so v is an arbitrary ±1 4-vector; `W_s(c)=Σ_z η_zχ_s(z)∈{0,±2,±4}` with `Σ_s W_s(c)²=16`, forcing exactly one of two patterns: a **spike** (`η=±χ_{s₀}` up to sign: one fibre gets ±4, the others 0) or a **quartet** (all four fibres get ±2).

Ledger check: `|supp v|=16·1+28·2+3·0+17·4=140` and u-entries `16·3+28·2+3·4+17·0=116=m`. ∎

The v-support `Ω:={y:u(y)=0}` is thus **determined blockwise by u's classes alone**; the only freedom v carries is the signs `δ_c, η, η_z` and, on the u-side, the still-open choices inside u (notably the gap positions `z₀(c)`).

## 4. Congruence theorem and the new XOR conditions

**Theorem 3 (off-coset congruence structure).** Under the frozen scope (balance, T-self-consistency, Lemma 1, and the adopted fact that all Walsh values off K have `k=W_f/4` odd — equivalently `V̂≠0` mod 4 anywhere):

(i) For every s, `{c∈R*: W_s(c) is odd} = D`, and `V̂(r,s) ≡ Σ_c W_s(c) − 2·(r·D̂)` (mod 4) where `D̂=⊕_{c∈D}c` — using `(−1)^{r·c}=1−2(r·c)` exactly and `Σ_c W_s(c)(r·c) ≡ r·D̂ (mod 2)` since only D-blocks contribute odd terms.
(ii) Flatness `V̂(r,s)≡2 (mod 4)` for all (r,s) holds **iff** `(N1) D̂=0` and `(VB) Σ_c W_s(c)≡2 (mod 4)` for each s∈{0,1,2,3}. At s=0, r=0 this is `Σ_y v(y)≡2 (mod 4)`, i.e. exactly p odd (Theorem 2). Hence, given p odd:
**the adopted odd-half caller congruence is equivalent to (N1) together with the three mixed congruences `Σ_{y∈Ω} v(y)χ_s(z(y)) ≡ 2 (mod 4)`, s=1,2,3.**
(iii) **(N1) and (N2) hold for u**: `⊕_{c∈D}c=0` in R*, and `⊕_{y∈Ω} z(y)=0` in P*, which by Theorem 4 reduces (O-blocks contribute the XOR of all four z, which is 0; G-blocks nothing; and the 28 pair-gaps δ_c cancel pairwise because C₂,C₃,D₁ have even counts 4,6,18 with class-constant δ) to

  **(N2) `⊕_{c∈D} z₀(c) = 0` in P*.**

*Proof.* (i) is the displayed computation; oddness lives only on D by Theorem 4. (ii): if `D̂≠0` pick r with `r·D̂=1` and the residue flips by 2, contradicting flatness; then flatness at r=0 is (VB). (iii): by Theorem 2(ii), `⊕_{y∈Ω}y=0`; its R*-component counts each block with odd v-support parity, which by Theorem 4 is exactly D, giving (N1); its P*-component is the z-XOR over Ω, which by the block reduction above is `⊕_{c∈D}z₀(c) ⊕ 4·δ(C₂-const) ⊕ 6·δ(C₃-const) ⊕ 18·δ(D₁-const) = ⊕_{c∈D}z₀(c)`, since 4,6,18 are even. ∎

**Remarks.**
(a) (N1) and (N2) are conditions on the **even half u alone** (D and the gap positions z₀ are u-data). They are not implied by any adopted f244/f255/f263 statement, which involve only class counts, the s=2,3 atom geometry and U-level identities; a generic 16-set D fails (N1) with probability 63/64, so this is a genuine restriction, not a vacuity.
(b) The cap side adds `|V̂(r,s)|≤14` with `V̂(r,s)∈2+4Z`, i.e. `V̂∈{±2,±6,±10,±14}` exactly; in particular **V̂ never vanishes**, so the eight Walsh zeros of f all lie on K, re-deriving the adopted zero placement from the interface rather than from the unread caller body.
(c) `Σ_{(r,s)}V̂=256·v(0)∈{0,±256}`, consistent with 256 residues of 2 mod 4.

## 5. The plateaued shape of D

Since `t₁=0`, `16U₁=3·Walsh_R(σ₁)` with `σ₁=sign k(·,1):R→{±1}` (well-defined: `|k(r,1)|=6` everywhere as `e₁=0`). As `U₁∈{0,±3}`, `Walsh_R(σ₁)∈{0,±16}`, and Parseval `Σ_cWalsh_R(σ₁)²=64·64=4096=256·|D|` re-pegs `|D|=16`. So **σ₁ is a three-valued (16-support, amplitude-16) sign field on F₂⁶**, and D is its Walsh support. Fourier inversion gives the dual form: `(D,ε)` with `ε_c=sign U₁(c)` satisfies `|Σ_{c∈D}ε_cχ_r(c)|=4` for **all** r∈R, and conversely; D is simultaneously the two-level Walsh support of a dual sign field θ with `Walsh(θ)∈{0,±16}` supported on D. (N1) is thus a statement about such plateaued pairs.

*Compatibility illustration (not a placement).* `σ₁=(−1)^{x₁x₂+x₃x₄}` (independent of x₅,x₆) has `Walsh_R(σ₁)(c)=±16` exactly on the 4-dimensional subspace `D={c:c₅=c₆=0}` and 0 elsewhere; this D satisfies `⊕D=0` (XOR over a subgroup). So (N1) is satisfiable in isolation — it restricts without excluding. No claim is made that this σ₁ extends to a u or an f; it is a written check that the new condition is not self-contradictory.

## 6. Exact ledgers (necessary integer identities)

**Per-fibre energies.** `E_s:=Σ_c W_s(c)²` satisfies `Σ_s E_s=4·140=560` (four-point Parseval summed over blocks) and `64·E_s=Σ_{r∈R}V̂(r,s)²`. By Theorem 4, `E_s=16+P_s+O_s` where the 16 A₁-blocks contribute 1 to every fibre, `P_s` collects the 28 pair-contributions 4+4 into two fibres (class-forced candidate pairs, free sign choice per block), and `O_s` collects 17 contributions each of spike-type 16 or quartet-type 4-per-fibre, with `Σ_sP_s=224`, `Σ_sO_s=272`.

**Spectrum ledger.** Since `V̂∈{±2,±6,±10,±14}` on all 256 points with `ΣV̂²=35840`: writing `n_j` for the count of `|k|=j` values off K (`k=V̂/2∈{±1,±3,±5,±7}`),

`n₁+n₃+n₅+n₇=256`,  `n₁+9n₃+25n₅+49n₇=8960`,  equivalently `n₃+3n₅+6n₇=1088`;

per fibre, `n₆(s)+3n₁₀(s)+6n₁₄(s)=2E_s−8` in the |V̂|-counting. These are necessary integer conditions on any solution's v-spectrum; the ledger's integer relaxation is nonempty (e.g. `n₇=168,n₅=20,n₃=20,n₁=48`), which only shows non-vacuity — **it is not a spectrum, placement, or witness**, and no sufficiency direction is claimed anywhere in this section.

**Fibre sums.** `Σ_{r∈R}k(r,s)=32·U_s(0)` (character inversion at c=0); for s=1 this reads `6Σσ₁=32U₁(0)`, i.e. `Σσ₁=Walsh_R(σ₁)(0)∈{0,±16}`, consistent with §5.

## 7. Interface equivalence and the exact remaining gap

**Theorem 6 (formulation closure).** Within the frozen f244 scope at `(G₃,H)=(1,0)`, the residual admits a balanced f with `max|W_f|≤28` **if and only if** there exist u and v on V such that:

(U) u realizes the entire adopted u-side system — the block identities and counts of f244/f255, the f263 cross-fibre conditions, the eight in-fibre zeros — **together with the new (N1), (N2)**;
(V) v signs the u-determined complement Ω with `|V̂(r,s)|≤14` and `V̂∈2+4Z` on all 256 characters, `p∈{63,…,77}` odd, and the three mixed congruences `Σ_{y∈Ω}v(y)χ_s(z(y))≡2 (mod 4)`, s=1,2,3;
and then f is reconstructed by `s|_V=u+v`, `s|_{V+T}=u−v`, is balanced iff `Σu=0`, meets the cap iff both caps hold, and is T-self-consistent iff (N1),(N2),p-odd hold (Theorem 2's converse).

*Proof.* Theorems 1–5 and the reconstruction paragraph of §2. ∎

**Exact remaining gap (honest, partial).** Both sides of the conjunction are open: (U) is the frozen f263 open problem — the seven class-count pairs and, within (1,0), atom placements satisfying (C),(S) are unproven to be realizable by an actual u (and the f263 §8 formal control fails block compatibility at c=0, so no placement is known); (V) is a new bounded sign-assignment problem — 256 capped, congruent linear forms over the fixed Ω — whose solvability is neither established nor refuted here. **This packet therefore yields no witness and no exclusion; it closes the coupling formulation and adds necessary conditions (N1), (N2), the mixed congruences, the p-range, and the ledgers.** No statement is made about the other six class-count pairs, m=114, other fibre patterns, other ranks, or the global target.

## 8. Boundary compliance and provenance

WRITTEN mathematics only, from the five frozen inputs and elementary Boolean/Fourier analysis; universal coordinate arguments only; no selected finite object was computed, inspected or used for planning; no program, solver, test, search, external model, Git operation, deletion, source edit or publication. H is used solely as the explicit local U₀-peak count (value 0 here); no historical class-label equivalence is asserted. All prior STOP/HOLD/ZERO/NONINPUT controls remain binding; this context rotation lifts none.

| Input (frozen order) | SHA-256 | LF |
|---|---|---:|
| `successor-20261029-info6-status-only-handoff-v1.md` | `790221d103c71d62ff6186f502daf0feab3b9eebe9c63bfcd58a12bd320f6c3f` | 29 |
| `dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-obstruction-parent-v1.md` | `18403a17269311682255e3bb9823a89a0a69cd7344a66ad02bdd841bcc52f912` | 24 |
| `successor-20261029-f255-boolean-local-normalization-correction-v1.md` | `e0c3f4807732d6cd70d47485f1692366c0f77abfd1c5169e7a5782114bfddcf4` | 151 |
| `successor-20261029-f244-residual-cross-fibre-placement-v1.md` | `686dd9177d6ff8788b6463d8d4e444e8bda4231ce7060a76ad0cfdea5f39144c` | 183 |
| `dispositions/info-6-nl242-rank2-eightzero-116-fibre-048-residual-10-cross-fibre-parent-v1.md` | `e09be9069bf8027bdb53e60a73c804f525b1c5c1953d517e417b5749b555ba09` | 31 |

All five were SHA/byte/LF-verified before display and displayed completely in raw ≤15-LF windows before this composition; `startup-ack-v1.json` precedes this file. Native clocks: ACK 2026-10-29T18:17:36-0700; this manuscript 2026-10-29T18:22:41-0700. Same-harness author work; not human, independent-model-family, formal/kernel or novelty verification.
