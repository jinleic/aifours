# f183: four-zero branch exclusion — independent same-harness review

**Verdict: supported at the prospectively frozen conditional scope; 0 FATAL / 0 MAJOR / 1 MINOR.** The new support-moment, odd-law, fibre-distribution and block-energy argument is sound as reconstructed below, and independently authored exact code verifies all 32 cases with both specified weight vectors. The minimum selected-certificate margin is **960**, not zero. This is not an unconditional independent re-verification of the imported f131/f152 results. It is not human, independent-model-family, formal/kernel or novelty verification, and does not exclude the remaining ≥6-zero cases or prove a global NL242 theorem.

Reviewer: `ReviewF183NL242FourZero`. Native clock observed immediately before composing this report: **2026-10-29T09:18:20-0700 PDT** (not an asserted file-creation time).

## 1. Frozen scope, integrity, and actual source order

Wave: `f183-nl242-four-zero-branch-empty`. Manifest SHA-256 was checked **before reading its contents** and equals the required `7fc54ffaaf6c90001d5a955ddfab3fb9e7b197a0d76ad7fa612d1c8196303b84` (4,622 bytes). Initial manifest verification clock: `2026-10-29T15:32:16Z`. All five input SHA-256/byte/LF values below matched the manifest; all end in LF and contain no CR. Input-hash verification completed at the observed clock `2026-10-29T15:32:44Z`.

Let `RUN=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h` and `E=/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242`. After the manifest, the following were read **completely and in exactly this order**, before mathematical interpretation or computation:

| Order | Source | Bytes | LF | SHA-256 |
|---|---|---:|---:|---|
| 1 | `RUN/dispositions/info-6-four-zero-rank6-radical-parent-v1.md` | 5831 | 31 | `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3` |
| 2 | `RUN/dispositions/info-6-four-zero-unequal-radical-phases-parent-v1.md` | 6220 | 27 | `a31e8f9c5c913d67ab980367e0347d64b1f6ad5e55c8d7bf0aab9efc85fbc6ec` |
| 3 | `E/frontier-20261029-fourzero-block-energy-exclusion-v1.md` (target) | 9183 | 127 | `9227c8fd98f7679543a4e780fbd8dc827e097c1783ebead73d1565a678400cfb` |
| 4 | `E/frontier-20261029-fourzero-block-energy-check.py` (read only) | 8421 | 177 | `25cc156ae5b4dddb872ed10d0ca32a1a222256cc20c5d3495ed26db41547bd4c` |
| 5 | `E/frontier-20261029-fourzero-block-energy-check-result.json` (data only) | 19220 | 1103 | `52d0ba2accae27e15d71d06daaa33406d93a0064b9a1460eb7c2cdd090e6fe61` |

The final JSON was read as raw LF ranges 1–400, 401–800, 801–1103, then parsed in full by reviewer-authored strict code: duplicate keys, floats and nonfinite constants are rejected; all fields are schema/type checked; canonical sorted reserialization is byte-identical. Complete traversal counted 68 objects, 113 arrays, 640 integers, 68 booleans and 33 strings, with no nulls. Every reported certificate, multiplicity, fibre-type list and no-law flag was compared to my independent computation. The author's Part A count/seed is preserved as an author claim, not represented as a run I reproduced.

No cited-but-unlisted source, sibling review, f161/f162 episode, held payload, public web source or author mathematical program was opened or executed. Only this wave's reviewer artifacts were written. No Git, deletion, publication, external model/API, author contact or infrastructure change occurred.

## 2. Exactly what is imported and conditional

Assume a putative balanced `f:F₂⁹→{0,1}` with `|W_f|≤28` and `|Z|=4`, with `k=W_f/4`. This review **imports, rather than re-reviews the unlisted antecedent proofs of**, the two adopted dispositions:

1. **f152:** `T=⊕supp(f)≠0`, hence `K=T^⊥` is an eight-dimensional linear hyperplane and `H={b:b·T=1}` is its other half. Also `|Z|` is even and at least four; these last two facts are needed only for the final `|Z|≥6` corollary.
2. **f131, in that peak-bounded four-zero case:** `q=(k/2 mod 2)|K` is quadratic, `rank B=6`, and `Z=R=rad B` is a two-plane on which `q=0`. Thus `q` descends to a nondegenerate six-variable `Q₆`, with 28 or 36 zeros, and `z=|{a∈K:q(a)=0}|=112` or `144`.
3. **f152 (E8):** for all `a∈K,r∈R`, `k(a+r)≡k(a)+4λ(r)q(a) (mod 8)`, with `λ∈R*`. The odd quadratic's radical character is `ρ`, and `λ≠ρ`. Input translation adds the same restricted character to both; after a permitted translate one has `ρ=0`, `λ≠0`.
4. **The named mod-4 identification:** on `H`, `k(b)≡(-1)^{Q(b)} (mod 4)`, with **this same odd quadratic `Q` whose radical derivative is `ρ`**. Consequently `ρ=0` means `k mod 4` is constant on every odd `R`-fibre. This precise identification is needed in Lemma 2 to exclude `τ^r=T`, in Lemma 3 to define `ω` and hold `g` fixed along a fibre, and in the odd admissible-value enumeration. Without it, the displayed odd-law proof and its certificate application are not established.

The last elementary fact can also be derived directly: for support bits `b·y`, let `e₂(b)=Σ_{y<y'}(b·y)(b·y')`. Lucas gives `N(b)≡(b·T)+2e₂(b) (mod 4)`. Therefore on `H`, `k≡1+2e₂≡(-1)^{e₂} (mod 4)`; on `K`, `q=e₂|K`. Both have the same polar on `K`-directions. Thus `Q=e₂|H` is the required natural normalization (an additive constant changes the sign convention, not `ρ`). My real-function controls check this fact and sign convention separately. This derivation does not independently re-establish f152's `λ≠ρ` theorem.

For clarity, I denote the **linear map** called `T(s)` in candidate §4 by `L(s)`, keeping `T` for the support XOR. Translation preserves balance, peak, zero positions and `T,K,q,B,R`: `k_t(a)=(-1)^{a·t}k(a)` and the support has even size 256. On the even half, changing signs adds `r·t` to `λ`; on the odd half it adds `r·t` to `ρ`. A functional on the two-plane `R` extends to the ambient space, so normalizing `ρ` to zero while keeping `λ` nonzero is justified by the imported unequal-character result. A basis of `R` can then make `λ̂=1=(1,0)`.

**Dependency chain:** C1 below uses only actual balanced support counting; C2 uses f131's `Z=R,q|R=0`, item 4 and `ρ=0`, and uses E8 to identify `φ_r|K`; C3 uses that common quadratic and its restriction plus rank six; C4 is ordinary restriction/Parseval; C5–C6 use the peak bound, exact-zero geometry and the resulting fibre law/distribution. The corollary adds f152's even lower bound. None of those imported antecedents is being promoted from scope-only support to an independently re-verified theorem by this review.

## 3. Reconstruction of all load-bearing new steps

### C1 — support-moment identity and mod 8: SUPPORTED (0 F/M/m)

For the 256-point support `M`, `k(x)=N(x)-128+128·1_{x=0}`. Flipping `x` to `x+r` flips exactly the support bits indexed by `M^r`. The fully exact formula, including endpoints, is

`k(x+r)-k(x)=|M^r|-2N^r(x)+128(1_{x=r}-1_{x=0})`.

For nonzero `r` this has discrepancy `-128` at `x=0`, `+128` at `x=r`, and no discrepancy elsewhere. For `r=0` both corrections cancel. Hence the author's exact/mod-8 endpoint qualification is correct. The low bit of `N^r(x)` is `x·τ^r`; the second bit is `C(N^r(x),2) mod 2=Q^r(x)`. The pair expansion makes `Q^r` a sum of products of linear functions, so its algebraic degree is at most two, including possible linear terms after Boolean reduction. Thus `-2N^r≡-2(x·τ^r)-4Q^r (mod 8)` on the whole domain. No spectral-array realizability is being inferred from this identity; existence of the actual support is essential.

### C2 — `τ^r=0` and one quadratic on both halves: SUPPORTED CONDITIONALLY (0 F/M/m)

For `r∈R`, `q(a+r)=q(a)` since `B(a,r)=q(r)=0`; therefore `k(a+r)≡k(a) (mod 4)` on `K`. Also for nonzero `r∈R`, `|M^r|=N(r)=128` **exactly**, since `k(r)=0`; for `r=0` it is zero. Applying C1 modulo four gives `a·τ^r=0` on `K`, so `τ^r∈K^⊥={0,T}`. Item 4 and `ρ=0` give the same mod-4 invariance on `H`; an odd `b` would have `b·T=1`, ruling out `τ^r=T`. Consequently `τ^r=0`.

C1 now yields `D_r k≡4φ_r (mod 8)` globally, with `φ_r=|M^r|/4+Q^r mod 2`, a **single** quadratic defined on all nine variables. In the actual target case its constant summand is zero mod 2. E8 identifies `φ_r|K=λ(r)q`. This is stronger than choosing unrelated quadratics on the two halves; doing the latter would invalidate C3.

### C3 — odd law, global alternating quadratic, and eight class distributions: SUPPORTED CONDITIONALLY (0 F/M/m)

Since `g=(-1)^Q` is fixed on an odd fibre, `ω=(k-g)/4 mod 2` is well-defined and `D_rω(b)=φ_r(b)`. At `|k|≤7`, its value one is precisely `|k|∈{3,5}`.

Telescoping gives `φ_{r+r'}(x)=φ_{r'}(x+r)+φ_r(x)`. The derivative `D_rφ_{r'}` is affine in `x` and zero on `K`, because `φ_{r'}|K=λ(r')q` and `q` is `R`-invariant. An affine function zero on a linear hyperplane is either zero or its defining linear form; hence its value on `H` is a constant `β(r,r')`, independent of `x`. For each odd `b`, `r↦φ_r(b)` has value zero at zero and polar `β`. On the two-dimensional `R`, every such Boolean function has degree at most two; its polar is bilinear and symmetric, and the cocycle with `r=r'` gives zero diagonal. This fills in the brief bilinearity step in candidate §4 without an extra assumption. Choosing one quadratic `ν` with that polar leaves linear differences `ℓ_b`, so `φ_r(b)=ℓ_b(r)+ν(r)`.

Moreover, `D_{a₁}φ_r` is affine on `K`. Thus at `b_s=a₁+(0,s)`,

`φ_r(b_s)=λ(r)Q₆(s)+L_r(s)+c_r`, with `L_r` linear in `s`.

At `s=0`, `c_r-ν(r)=ℓ_{a₁}(r)` is linear in `r`; subtracting the other linear functionals shows `r↦L_r(s)` is linear for each `s`. Therefore a genuine linear map `L:F₂⁶→R*` and constant `ν̂∈R*` give

`ℓ_{b_s}=Q₆(s)λ̂+L(s)+ν̂`.

There is only one global polar `β`, so after absorbing linear parts the fibre pattern is `const+x·r+h r₁r₂`, with one global `h∈{0,1}`. For `h=1` rebasing a fibre changes its class by `β(r₀,·)`; squared block contributions remain unchanged, and all four class capacities for the selected certificate agree. For `h=0` the class is base-point independent.

Write `P=Q₆+affine` and `A=affine` for the two coordinates of `ℓ`. If `A` is constant, the weight 28/36 of the nondegenerate `P` yields the four extreme vectors. If `A` is nonconstant, its Walsh sum is zero and the Walsh sums of `P` and `P+A` are independently `±8`; the joint counts are

`(16+(S_P+S_{P+A})/4, 16-(S_P+S_{P+A})/4, 16+(S_P-S_{P+A})/4, 16-(S_P-S_{P+A})/4)`.

This gives exactly the four mixed vectors. Independently enumerating all `128²=16384` ordered pairs of affine coordinates for **each** Arf type confirms the full list:

`(0,0,28,36), (0,0,36,28), (12,20,16,16), (16,16,12,20), (16,16,20,12), (20,12,16,16), (28,36,0,0), (36,28,0,0)`.

The four extreme vectors each have multiplicity 64 and the four mixed ones each 4032, summing to 16384. Two seeded invertible changes of six-variable basis reproduce the same multiplicities. This enumeration is safely a superset: any additional restrictions from actual support realizability could only reduce capacities, not invalidate the contradiction.

### C4 — four block-energy equations and their equivalence: SUPPORTED (0 F/M/m)

For input flat `A_c={x:x·ρ_i=c_i}`, character expansion gives `1_{A_c}(x)=¼Σ_{r∈R}χ_r(c)(-1)^{r·x}`. Hence its restricted Walsh value is `S_F(c)=Σ_rχ_r(c)k(a+r)` for one frequency representative per `R`-coset, up to the harmless sign from changing that representative. There are 128 such frequency characters. Parseval on the 128-point flat yields `E_c:=Σ_F S_F(c)²=16384`, or `Σ_F u_F(c)=4096` for `u_F=S_F²/4`.

Expanding the squares gives **exactly** `E_c=Σ_{r∈R}χ_r(c)C(r)`, with `C(r)=Σ_a k(a)k(a+r)`. Inversion gives `Σ_cχ_r(c)E_c=4C(r)`. Therefore the four equations are equivalent to `C(0)=16384` (Parseval) and the three equations `C(r)=0` for nonzero `r∈R`. No other shift-correlation equation is used in this new capacity step.

### C5 — admissible fibre sets: SUPPORTED CONDITIONALLY (0 F/M/m)

There are 64 even and 64 odd fibres. On the even side: one zero fibre `R`; `(z/4)-1=27` or `35` nonzero `q=0` fibres with all entries in `{±4}`; and `64-z/4=36` or `28` `q=1` fibres with entries in `{±2,±6}` and E8. The exclusion of zero in the nonzero `q=0` fibres uses **exactly `Z=R`**, not just a histogram. E8 at every base point is equivalent to `(k_r/2)(-1)^{λ(r)}` constant mod four. All 32 such ordered `q=1` vectors were independently enumerated. Their seven distinct contribution vectors, split by the number `e` of magnitude-two entries, are:

| e | Distinct contribution vectors, block order 0, λ̂=1, 2, 3 |
|---:|---|
| 0 | `(0,144,0,0)` |
| 1 | `(16,64,16,16)` |
| 2 | `(64,16,0,0)`, `(0,16,64,0)`, `(0,16,0,64)` |
| 3 | `(16,0,16,16)` |
| 4 | `(0,16,0,0)` |

The `q=0` vectors give 64 at any one block or 16 at all four. The odd set consists of 512 ordered vectors with entries `{±1,±3,±5,±7}` and common residue mod four. Their patterns partition into exactly 64 vectors in each `(h,x)` class. The rebase law was checked at all four possible representatives. Thus all actual fibres are included in the enumerated sets; no unjustified restriction or extra realizability claim is introduced.

## 4. C6 — exact capacity certificate and all 32 inequalities

**SUPPORTED CONDITIONALLY (0 F/M/m).** For every actual fibre, `w·u_F` is bounded by the maximum over its admissible set, for any weights. C4 therefore implies `4096Σw≤Σ_F cap_F(w)`. A strict upper bound smaller than the left side is contradictory. This is a direct finite dual bound, not an inference from a numerical solver status. I neither ran nor relied on the author's Z3 work.

Let `W1=(2,3,6,6)` with required total **69632**, and `W2=(12,5,12,9)` with required total **155648**. Independent maxima are:

| Weight | even q=0 / q=1 | odd h=0, class order 0,1,2,3 | odd h=1 |
|---|---|---|---|
| W1 | 384 / 432 | 456,456,872,872 | 668,668,668,668 |
| W2 | 768 / 848 | 2352,1280,1776,1344 | 1832,1832,1832,1832 |

Here are **both capacities for every case**. An asterisk marks the certificate selected by the written case rule, not a claim that every other weight also certifies. E/H mean elliptic/hyperbolic.

| h | N | E: W1 | E: W2 | H: W1 | H: W2 |
|---:|---|---:|---:|---:|---:|
| 0 | (0,0,28,36) | 81728 | **149376*** | 81344 | **148736*** |
| 0 | (0,0,36,28) | 81728 | **152832*** | 81344 | **152192*** |
| 0 | (12,20,16,16) | **68416*** | 155008 | **68032*** | 154368 |
| 0 | (16,16,12,20) | **68416*** | 157568 | **68032*** | 156928 |
| 0 | (16,16,20,12) | **68416*** | 161024 | **68032*** | 160384 |
| 0 | (20,12,16,16) | **68416*** | 163584 | **68032*** | 162944 |
| 0 | (28,36,0,0) | **55104*** | 163200 | **54720*** | 162560 |
| 0 | (36,28,0,0) | **55104*** | 171776 | **54720*** | 171136 |
| 1 | (0,0,28,36) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (0,0,36,28) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (12,20,16,16) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (16,16,12,20) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (16,16,20,12) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (20,12,16,16) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (28,36,0,0) | **68672*** | 168512 | **68288*** | 167872 |
| 1 | (36,28,0,0) | **68672*** | 168512 | **68288*** | 167872 |

For example, `384·27+432·36+668·64=68672<69632`, margin 960. At `h=0`, W1 gives `55104+416(N₂+N₃)` or `54720+416(N₂+N₃)`; at 32 the margins are 1216/1600. For the two extreme distributions with `N₂+N₃=64`, W2's worst margins are 2816/3456. These exhaust the 32 combinations. **The conclusion `|Z|≠4` follows at items 1–4's adopted scope; the corollary `|Z|≥6` additionally uses f152's even lower bound.**

### M1 — MINOR wording error (candidate line 93)

“Three weight vectors” should say **two distinct weight vectors used in three case groups**. Groups (i) and (ii) use the same W1. The displayed values, checker and manifest agree on the actual two vectors, and the contradiction is unaffected. No FATAL or MAJOR mathematical defect was found.

## 5. Actual independent bounded controls and intended-reason negatives

The standalone reviewer program imports/executes **no author code**. Its only transcribed author data are the eight-entry candidate-weight list (for matching the JSON's first-certifying-weight/no-law flags) and the explicit relaxed point, both recomputed rather than trusted. Distribution enumeration is organized as all pairs of affine coordinates; E8 membership is checked at every pair of base points, independently of the author's shortcut. Python integers are unbounded; numpy `int64` operations use only small bounded exact integers (counts ≤256, Walsh sums ≤512, matrix/correlation accumulations safely below 2³¹), with no floating arithmetic in the mathematics.

**Final one-shot receipt:** `reviewer-f183-controls-v1-execution.json` records native clocks **09:16:58–09:17:01 PDT**, 120-second hard subprocess cap, stdin `DEVNULL`, exit **0**, no cap, elapsed **3.396007 s**. Internal mathematical run time was 3.286 s. **54/54 positive checks, 17/17 intended-reason negative checks; no UNKNOWN in the final run.** These are grouped check predicates, not a tally of independent theorems.

Exercised positive coverage includes:

- 12 independently seeded balanced real Boolean functions (`SHA256('reviewer-f183-boolean-i')` determines each seed), **all 511 nonzero r**: **3,127,320** exact off-endpoint identities, **3,139,584** global mod-8 identities, **6,132** quadratic-degree checks and 768 direct-count spot checks. Walsh coefficients are computed independently by the integer character matrix, not assumed from the support-count formula.
- On those functions: the standard odd mod-4 fact and its even counterpart; degree ≤2 of the global second support bit; the polarization formula; linearity of `r↦τ^r`; all spectral correlations; **96** seeded two-planes with direct restricted Walsh formulas, block Parseval, and the exact character-inversion equivalence.
- Four additional real balanced functions constructed with `τ^r=0` on a chosen two-plane and `|M^r|≡0 mod4`: the global `D_rk=4φ_r mod8` law, cocycle, quadraticity, affine derivatives, and odd fibre law. These are deliberately out-of-target controls, not witnesses for the four-zero hypotheses.
- All fibre sets, all 16384 class maps per form, two independent GL₆ basis changes, all **64** evaluations (32 cases × two specified weight vectors), every numerical §7 inequality and every author-JSON certificate field/multiplicity.

Important intended-reason negatives:

1. **Drop the odd mod-8 law:** all 32 cases fail to certify for every one of the eight author-candidate weights. Without the law W1's odd capacity becomes 872 in every class and W2's becomes 2352. In addition, I constructed independent exact type-count points for **both forms** with all four block energies 4096 and odd affine-class count `(20,0,20,24)`. These points are geometrically unrealizable, but are valid in the no-law relaxation regardless of the prescribed class counts; by weak duality no choice of weights can separate that relaxation. Their complete type lists are in the result JSON, not Boolean witnesses.
2. **Requested unrealizable point `(16,0,16,32)`:** all author-supplied even/odd types were checked admissible; counts are 27/36/64; all block energies are exactly 4096; every odd pattern is affine. The count vector is absent from both enumerated realizable sets (already its first-coordinate weight is 32 rather than 28/36). With this N, W1/W2 capacities are 75072/160320, so neither certifies. This establishes that three radical correlations plus the local affine pattern rule do not suffice without common class-map geometry.
3. W1 alone fails at `h=0,N₂+N₃=64` (81728 or 81344 versus 69632); W2 is genuinely needed for these cases.
4. The exact C1 identity fails at the endpoints by exactly ∓128; dropping `-4Q^r` fails exactly where `Q^r=1`; flipping the sign of `2x·τ^r` fails exactly where `x·τ^r=1`; using the third instead of second support-count bit exceeds degree two in all 6132 tested nonzero directions.
5. Reversing the standard odd mod-4 sign fails at every odd point. Permuting nonzero spectral entries preserves Parseval but violates a block equation in all 96 sampled planes; the algebraic equivalence remains correct and the violations match nonzero radical-shift correlations.
6. In constructed out-of-target functions, omitting the constant `|M^r|/4` from `φ_r` when that quotient is odd breaks its law at every x. Dropping the target input that `φ_r|K` is R-invariant gives **24** pairs with a nonconstant derivative on H; hence the global-β argument is not automatic from quadraticity alone.

A separate sensitivity computation (not a new theorem) removes E8 only on even `q=1` fibres: the written selected weights certify just 2/32 cases. This documents the load-bearing status of the f152 even law; it does not prove no different weights could compensate.

## 6. What is, and is not, beyond the three radical equations

The last capacity step uses only **Parseval plus the three nonzero R-shift correlations**, but the proof is emphatically **not** a consequence of those scalar equations alone. It also needs all the explicitly declared structure: actual Boolean support and support-moment identities, peak and balance, exact `Z=R`, rank-six quadratic geometry, E8, the translation with unequal characters, the named mod-4 identification, one global `φ_r` on both halves, one global alternating quadratic part, and the joint class map `Q₆λ̂+L+ν̂` across all 64 odd fibres. None of these can be replaced by independent per-fibre choices or a scalar histogram. The requested relaxed point demonstrates the distinction concretely. I found **no additional undeclared mathematical assumption** needed beyond these declared inputs and finite character orthogonality/Parseval, Lucas' second-bit identity and elementary quadratic-form linear algebra. The imported dispositions may themselves depend on further Booleanity/correlation arguments; their antecedents were not re-opened and are not claimed independently verified here.

## 7. Per-claim dispositions and process qualifications

| Claim | Disposition | Exact dependency / limit |
|---|---|---|
| Adopted f131/f152 antecedent theorems | **Scope-only import; independent antecedent verification INCONCLUSIVE/not attempted** | Only the two adopted dispositions were allowed; no claim that their unlisted sources were reviewed. |
| C1 support identity/mod-8/degree | **SUPPORTED — 0 F/M/m** | Actual balanced support of size 256; endpoint qualification mandatory. |
| C2 τ=0 and common quadratic | **SUPPORTED CONDITIONALLY — 0 F/M/m** | f131 zero/radical structure, standard mod-4 fact with f152 ρ=0, and E8 for restriction. |
| C3 odd law/global ν/eight distributions | **SUPPORTED CONDITIONALLY — 0 F/M/m** | C2 including its common restriction, rank six, nonzero λ; no independent-fibre replacement. |
| C4 four block equations/equivalence | **SUPPORTED — 0 F/M/m** | Actual Boolean restrictions and character orthogonality/Parseval; only three nonzero R correlations in the equivalent form. |
| C5 finite fibre enumeration | **SUPPORTED CONDITIONALLY — 0 F/M/m** | Peak, exact Z=R, E8 and the standard odd mod-4/fibre law. |
| C6 all capacities / four-zero exclusion / ≥6 corollary | **SUPPORTED CONDITIONALLY — 0 F/M/m** | All above; ≥6 also imports the f152 even lower bound. No global NL242 statement. |
| M1 “three weight vectors” | **MINOR** | Candidate line 93; two distinct vectors, three case groups. |
| Author result's listed certificate/relaxed-point claims | **SUPPORTED by independent recomputation — 0 F/M/m** | Author identity-trial count/seed remains reported data, not a replay of author code. |

Process/nonacceptance history and deviations are not concealed:

- One earlier stdout-only development run at observed native clocks **09:00:14–09:00:42 PDT** took 28.265 s and reported 54/54 positive and 15/15 negative predicates, plus **two UNKNOWN bounded stochastic searches** for optional no-law points. Those search failures were never treated as evidence of infeasibility or acceptance. They were replaced by the explicit exact constructions above; the final script/receipt, with no remaining UNKNOWN, is the delivered evidence. No final artifact was overwritten.
- An environment probe for SciPy failed with `ModuleNotFoundError`; no installation, solver execution or inference from that failure occurred. The delivered controls need only the already available Python/numpy (versions 3.14.3/2.4.3).
- Initial administrative shell commands used shell directory listing/working-directory changes and a one-byte end-of-file probe rather than the preferred specialized-tool conventions. This is a **tool-convention deviation**, not an input-order or mathematical-scope expansion; no unlisted mathematical content was read. All subsequent review/receipt outputs stay in the owned wave directory.
- No execution hit a 120-second cap. No author program was run/imported. No held source was consulted. All theorem-level scope limits above remain binding despite passing controls.

## 8. Delivered evidence and hashes

| Artifact | SHA-256 |
|---|---|
| `reviewer-f183-controls-v1.py` (840 LF; final independently authored source) | `c6ae50b854626d5daeda8b13523aab0b9355fd6bc36d02a0e6ec9b81cc99900f` |
| `reviewer-f183-controls-v1-result.json` (38289 bytes / 2720 LF) | `6625dffda63da43335fd5cc5f073891b2a2a2639fb6ea228964094e5a69f40c7` |
| `reviewer-f183-controls-v1-execution.json` (clock/exit/cap/script/result/stdout/stderr binding) | `810a3d1e6b000f76282eeb4b765e3d4411ae4be866f09ccba74ab38dfd1bd796` |

The SHA-256 of this completed `review-v1.md` is delivered in the final reply rather than inserted self-referentially. Files created: this report and the three reviewer-prefixed artifacts listed above. The original manifest and all author inputs were left unchanged.
