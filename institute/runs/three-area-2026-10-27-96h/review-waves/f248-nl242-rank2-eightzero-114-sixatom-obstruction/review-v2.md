# f248: independent same-harness review of the six-atom obstruction

Reviewer: **ReviewF248SixAtom**, fresh same-harness task subagent. Native `/bin/date` observed before this write: **2026-10-29T14:55:46-0700 PDT**. This is the reassigned review; the previous `review-v1.md` is a status-only exposure screen and was not modified.

## Disposition and verdicts

**The mathematical claims of the combined body and both mandatory errata are supported at the stated conditional, necessary-obstruction scope.** I find no fatal, major, or minor mathematical finding on those corrected claims. There is **one minor process deviation**, disclosed in §1: the manifest prefix was inspected after, rather than before, the input hashes were also measured in the same `shasum` invocation. No input body was opened before the comparison and measurements. The two superseded sign-multiplicity/dimension statements are false when read alone; the precise additive corrections are indispensable, not optional editorial context.

Verdict notation: **F** = fatal finding, **M** = major finding, **m** = minor finding, and **INCONCLUSIVE** = not established within this review. `0F/0M/0m (supported)` means that the particular corrected, conditional claim is supported, not that any broader claim is accepted.

| Claim | Verdict and reason |
|---|---|
| Derivation of the even-half quadratic, rank-two fibre, bound, and `z=64` (§§2, 3 below) | **0F/0M/0m (supported).** The caller and quadratic needed here can be derived directly from the stated Boolean assumptions; I did so without using the two undeclared linked disposition bodies. The `z=128,192` bounds are 102 and 82, respectively. |
| Ternary four-point block shapes, `A₁=16`, possible classes, square-sum and congruence equations (§4) | **0F/0M/0m (supported).** Direct four-point transform and independent exhaustive control of all 81 ternary blocks; normalization and the `t₂` congruence are reconstructed below. |
| Six-atom affine-rank restrictions and corrected sign-orbit counts (§5) | **0F/0M/0m (supported for the combined packet).** In affine rank four there are four, not five, independent ratios; raw sign patterns need not each occur twice. The two errata jointly repair the original claims. Full parity counts and orbit multiplicities are derived below. |
| `y=7` excluded, hence `y∈{1,3}`, with the asserted rank/syndrome conditions (§6) | **0F/0M/0m (supported).** Both possible ranks at `N=40` contradict the independently derived signed identity `ΣU₂t₂=24`: the respective forced values are 168 and −84. |
| Four count formulas, inequalities, 21 literal triples, and arithmetic example (§7) | **0F/0M/0m (supported at the scalar class-count level only).** The two inequation regions yield precisely 9+12 triples. The example satisfies the displayed sums but is not a spectral or Boolean witness. |
| Withdrawal/noninput boundary | **0F/0M/0m for the derivation presented here.** No step below uses the withdrawn P1 roster, CR7, the `m=116` packet, the period packet, held/f161/f162 payloads, or any linked mathematical body. The body explicitly lists other disposition pins as prerequisites; I did not import them, and I independently derive the only needed caller facts. This audits the displayed logical dependency, not the author's private thought process. |
| Current validity of the two nondeclared prerequisite pins and the author's historical statements about not executing computations, Git, etc. | **INCONCLUSIVE.** Those files and histories were outside the frozen inputs and were not inspected. The body itself says its listed pins were not rehashed in that continuation; I do not promote their metadata or an author PASS line to evidence. |
| Existence/nonexistence of an actual target in any residual triple, full `(0,6,10)` case, `m=114`, rank two, eight zeros, or the balanced target | **INCONCLUSIVE / OPEN.** Neither a witness nor a full exclusion follows. No novelty conclusion. |

In particular, **the `(0,6,10)` case, `m=114`, rank two, and the balanced target remain OPEN** under this review, as do actual placement, compatibility and realizability for every listed scalar triple. This review does not establish a full fibre-case, witness, or global NL242 result.

## 1. Exposure, exact inputs, and actual sequence

The manifest was the **first file opened**. Its measured SHA-256 is `847ce17f45c5153c44f2b26e6f9f03df8f79f1d1d32970c7c662ed9f25649246`, matching assigned prefix `847ce17f45c5`; it measured 4,247 bytes, 46 LF. I then obtained SHA-256 with `shasum -a 256` and bytes/LF with `wc -cl` for the manifest and all four declared inputs before opening any input body. **Sequence deviation, m (process):** manifest and input hashes were obtained in one `shasum` invocation, so the input hashing began before I explicitly inspected the manifest prefix. The resulting prefix was compared and matched before any declared body was opened. All declared source measurements match the manifest. Metadata measurement is not a body read; nonetheless, this was not the prescribed strict compare-then-measure order.

After measurement, I read the parent reassignment and the earlier status-only screen, as well as general memory/review-protocol guidance. I wrote the pre-body attestation `reviewer-exposure-screen-v2.txt`: as a fresh reviewer I had not seen any serialized held/withdrawn/ZERO info-6 body, formula, guide, or consumer, including the P1 roster, or f161/f162 payload. The manifest and previous reviewer screen exposed names and status-only metadata, not those payloads. I had not done candidate mathematics at that point. The parent reassignment explicitly replaces the manifest's original reviewer/output with this fresh reviewer and `review-v2.md`.

The following measurements are from the single pre-body measurement, not copied as unverified source assertions. Paths under `E` mean `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/`; `P` means `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Order | Input | SHA-256 | bytes | LF | Actual complete raw windows |
|---:|---|---|---:|---:|---|
| 1 | `P/info-6-six-walsh-zeros-excluded-conditional-parent-v1.md` | `c1a85da652e8308e20c9129ebf1d031b1d97e343edfdb6f9620d38e18525a03e` | 4566 | 21 | 1–15, 16–21 |
| 2 | `E/successor-20261029-rank2-eightzero-114-sixatom-sign-orbit-erratum-v1.md` | `d172e122f2809524607025f33545c70740fd5625a4e3e61259a187280b1cc828` | 1216 | 9 | 1–9 |
| 3 | `E/successor-20261029-rank2-eightzero-114-sign-orbit-erratum-addendum-v1.json` | `7cf87cef7e39abecd65507cc15b2a8f9b25c727d52b3e3a23bd1d01a944a8ee3` | 1104 | 16 | 1–15, 16 |
| 4 | `E/successor-20261029-rank2-eightzero-114-sixatom-obstruction-v1.md` | `14449ed6655541634f648dc06edfd8612442ebce5af0428c46c342f2b99a784d` | 11356 | 156 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–120, 121–135, 136–150, 151–156 |

Every listed window was raw and at most 15 lines, including each last line; both errata were read before the target, and all four bodies were displayed before mathematical reasoning. One attempted target `16–30` read initially used a mistyped directory and returned `Path not found`; no bytes were displayed by that failed attempt. I corrected the path and resumed at 16–30 in the order shown. This is the only failed source-read attempt. No linked disposition, held/withdrawn source, sibling scientific review, author code, external search/model/API, or author contact was used. The previous review-v1 was read only as the expressly required status/reassignment screen.

## 2. Imports and independent caller reconstruction

The adopted six-zero disposition is a **scope-only premise**, not a license to import its links or an eight-zero conclusion. Its express adopted statements include `T≠0`, `Z⊂K=T⊥` with `0∈Z`, even `|Z|`, the rank/zero bound, the degree statement and the five-space parity statement; they are not used to silently import the two linked caller dispositions. The present theorem assumes balanced `f`, peak `|W_f|≤28`, `T≠0`, rank two, eight zeros, `m=114`, and the actual fibre tuple `(0,6,10)` up to permutation. Standard finite-field, Walsh/Parseval and elementary integer facts are used. In fact the caller properties necessary below follow directly, as follows.

Put `S={x:f(x)=1}`. Balancedness gives `|S|=256` and `T=⊕_{x∈S}x`. For `a∈K=T⊥`, let `n(a)=#{x∈S:a·x=1}`; it is even. For `a≠0`, `W_f(a)=−512+4n(a)`, so `k(a)=n(a)−128`; at `a=0`, balancedness gives `k(0)=0`. Thus `k` is even on `K` and `q(a)=k(a)/2 mod 2` is `n(a)/2 mod 2`. Since `n(a)` is even, this equals `binom(n(a),2) mod 2 = Σ_{x<y in S}(a·x)(a·y)`. It is therefore a well-defined quadratic function on the eight-dimensional `K`; its polar is alternating. The assumed rank is two. This is a derivation, not a hidden import of the caller/mod-4 source or of a roster.

Choose an 8-dimensional complement to `⟨T⟩` in the original space, and define `u(x)=( (−1)^{f(x)}+(−1)^{f(x+T)} )/2` on representatives. It is ternary and has support exactly the `m` agreeing unordered `T`-pairs. Identifying its dual with `K`, `Walsh₈(u)=W_f/2=2k`, hence `64m=Σ_{a∈K}k(a)^2`. Write `Z` for the number of Walsh-zero frequencies, not the adopted disposition's set symbol.

## 3. The rank-two fibre and square sums

The radical `R` of the rank-two polar has dimension six, and `q|R` is linear. If it is nonzero then exactly half of the 256 points are zeros of `q`. If it vanishes, `q` descends to a nondegenerate two-dimensional quadratic form, with either one or three zero quotient points. Accordingly the possible `q`-zero counts are `z=64,128,192`. On `q=0`, the peak bound and evenness give `k∈{0,±4}`; on `q=1`, `k∈{±2,±6}`. The eight spectral zeros all lie in `q=0`, so

`64m ≤ 16(z−8)+36(256−z)`.

For `z=128` the right side is 6528 (`m≤102`), and for `z=192` it is 5248 (`m≤82`), both incompatible with `m=114`. Thus `z=64`, `q|R=0`, and the quotient is the anisotropic two-dimensional form: its zero fibre is exactly `R`, with three nonzero fibres of 64 coefficients each.

Choose dual block coordinates so that `K=R⊕F₂²`, and define `U_s(c)=Σ_{z∈F₂²}u(c,z)(−1)^{s·z}` for `c∈F₂⁶`. Since `Walsh₆(U_s)(r)=2k(r,s)`, Parseval gives `Σ_c U_s(c)^2=(1/16)Σ_r k(r,s)^2`. In the zero fibre this is `56`; in a nonzero fibre having `e_s` small `|k|=2` entries it is `144−2e_s`. Also

`64m = 56·16 + Σ_{s=1}^3[4e_s+36(64−e_s)] = 7808−32Σ_s e_s`,

so `m=114` entails `Σe_s=16`, exactly consistent with the explicitly assumed `(e₁,e₂,e₃)=(0,6,10)`. This does not classify any other fibre pattern.

## 4. Four-point blocks and the six-atom congruence

Direct four-point Walsh transforms of the 81 ternary blocks give exactly the shapes in the body: weight 0 gives O; weight 1 gives F; weight 2 gives C or D; weight 3 gives A or B; weight 4 gives E, G or H. Their complete multiplicities in the independent control are recorded in §8. Since `e₁=0`, all `v₁=k/2` signs have absolute value 3. Inverting the six-dimensional Walsh transform makes `U₁` divisible by 3; its absolute value is at most 4. The square sum 144 therefore forces precisely sixteen `|U₁|=3` blocks, all A₁. All other possible classes have `U₁=0`, namely C₂, C₃, D₁, G₂, G₃, H, O. In that order their unsigned `(U₀,U₁,U₂,U₃)` shapes are

`(2,0,2,0), (2,0,0,2), (0,0,2,2), (0,0,4,0), (0,0,0,4), (4,0,0,0), (0,0,0,0)`;

A₁ has `(1,3,1,1)`. These are absolute-value shapes, not prescribed signs.

For nonzero fibre `s`, let `v_s=k(r,s)/2∈{±1,±3}`, `σ_s=sign(v_s)` and `τ_s=σ_s·1_{|v_s|=1}`. Thus `v_s=3σ_s−2τ_s`; `τ_s` has `e_s` distinct signed atoms. With `t_s=Walsh₆(τ_s)`, inversion gives

`16U_s=3Walsh₆(σ_s)−2t_s`, hence `U_s≡t_s (mod 3)`.

Let `y=N(G₂)`, `g=N(G₃)`, `h=N(H)` and use the other lower-case counts for C₂, C₃, D₁, O. For `e₂=6`, `ΣU₂²=132=16+4(c₂+d₁)+16y`, so

`c₂+d₁+4y=29`, `N:=#{c:U₂(c)=0}=48−c₂−d₁−y=19+3y`.

The allowed `U₂` values are `0,±1,±2,±4`; no nonzero one is divisible by 3. Thus `N=#{c:t₂(c)≡0 mod 3}`. Six distinct atoms have affine rank `d∈{3,4,5}`: an affine space of rank at most two has only four points, and six points have rank at most five. Their sign ratios depend on `d` independent linear characters, making the zero-mod-3 predicate constant on cosets of a dimension `6−d` subspace; consequently `N` is even. Nonnegativity in `c₂+d₁+4y=29` gives `0≤y≤7`, so the only preliminary values are `y=1,3,5,7`, with `N=22,28,34,40` respectively.

## 5. Corrected sign orbits and exact counts

Let the six distinct atom positions be `r_i` and their fixed signs `σ_i`. At a block-space point `c`, their six evaluated signs are `σ_i(−1)^{r_i·c}`. Dividing by the first sign leaves five ratios, whose **linear span has dimension `d`**, not necessarily five. Global reversal changes the sum's sign but not divisibility by three. Hence there are `2^d` attainable reversal orbits, each attained by `2^(6−d)` block-space points.

* If `d=5`, all 32 reversal orbits occur, each twice. A six-sign sum is divisible by three exactly at minus weights 0, 3, 6: there are `1+20+1=22` raw patterns, or 11 reversal pairs, hence `N=11·2=22`. This conclusion does not assume equal multiplicity of the two raw orientations.
* If `d=4`, the unique nonzero affine relation among the six augmented atom columns has even weight; distinctness rules out weight two, so it has weight four or six. Let its sign syndrome be the product of the fixed atom signs on that relation, equivalently even/odd minus parity on the relation. There are 32 formally admissible raw patterns (16 reversal pairs), but **four** independent ratios, with each pair attained at four points. For raw minus weight 0, 3, 6 the counts are:

  | relation weight | even syndrome | odd syndrome |
  |---:|---:|---:|
  | 4 | `1+12+1=14` | `0+8+0=8` |
  | 6 | `1+0+1=2` | `0+20+0=20` |

  Thus `N=2·(raw count)` is respectively `28,16,4,40`. In detail, if the base atom character lies in the span of the four ratio characters, each orbit has one realized raw orientation occurring four times; if it does not, the two orientations each occur twice. Both possibilities are realized by the reviewer control. The base sentence that each raw pattern occurs twice is false in general. The first erratum fixes the orbit argument but incorrectly says **five** independent ratios; the mandatory addendum correctly changes that to **four**. Only the combined corrected reading supports the four numerical counts.
* If `d=3`, the predicate repeats eightfold, hence `N` is a multiple of eight. The reviewer independently enumerated all six-subsets and signs in a three-space as a stronger finite control (§8), but the divisibility alone suffices here.

Now `N=34` cannot occur at any rank, so `y=5` is impossible. `N=22` forces rank five, proving the `y=1` condition. `N=28` forces rank four with a weight-four relation and even syndrome, proving the `y=3` condition. For `N=40`, rank five is impossible, leaving precisely the two branches below.

## 6. Excluding `y=7` without an author solver

When `y=7`, the class equation gives `c₂+d₁=1`: there are exactly sixteen `|U₂|=1`, one `|U₂|=2`, seven `|U₂|=4`, and forty zeros. Since `τ₂` agrees in sign with `σ₂` on six points, six-dimensional Parseval and §4 give

`ΣU₂t₂ = (3·64·6−2·64·6)/16 = 24`.  
This is a signed identity, not an absolute-value bound.

**Rank four.** `N=40` forces a weight-six relation with odd syndrome. Every admissible six-sign pattern has odd minus parity; weights 1 and 5 give `t₂=±4`, while weight 3 gives zero. There are 24 nonzero block points. The congruence `U₂≡t₂ (mod 3)` forces `U₂t₂=4,−8,16` at magnitudes `|U₂|=1,2,4`, respectively. Thus the signed sum is `16·4−8+7·16=168`, not 24: contradiction.

**Rank three.** Factor out the common base character and identify the six signed atoms with a ternary sign function on an affine three-space. Its eight Walsh values are even, bounded by 6 in magnitude, and have squared sum `8·6=48`. `N=40` says exactly five of the eight are divisible by three. The remaining three have magnitudes 2 or 4. At most one of the five can have magnitude 6.

If none has magnitude 6, all three remaining magnitudes must be 4. Inverting those three coefficients at any point produces an odd sum of three `±4` terms divided by 8, a half-integer, impossible for the original ternary function. Otherwise exactly one coefficient has magnitude 6; the three remaining magnitudes must all be 2, and the other four are zero. In the six-dimensional block space this means 32 zero-transform points, 8 points of magnitude 6, and 24 points of magnitude 2. Congruence makes precisely those 24 points the nonzero `U₂` positions. The respective products for `|U₂|=1,2,4` are `−2,4,−8`, forcing `16·(−2)+4+7·(−8)=−84`, not 24: contradiction.

Both possibilities for `y=7` are excluded. Consequently `y∈{1,3}` with exactly the corresponding necessary atom conditions stated above. No assertion of sufficiency follows.

## 7. Complete scalar class-count residual

The four independent displayed scalar equations used to parametrize the remaining classes are

`c₂+c₃+4h=10`,  
`c₂+d₁+4y=29`,  
`c₂+c₃+d₁+2(y+g+h)=33`,  
`c₂+c₃+d₁+y+g+h+o=48`.

They are respectively the `U₀²` sum, the `U₂²` sum, total weight 114, and total number 64 after removing 16 A₁ blocks. Solving them gives

`c₃=4+2y−2g−2h`, `c₂=6−2y+2g−2h`,  
`d₁=23−2y−2g+2h`, `o=15+y+g+h`.

They also give `c₃+d₁+4g=27`, equivalent to the required `U₃²=124`, so this sum has not been dropped. For `y=1`, nonnegativity is exactly `g,h≥0`, `g+h≤3`, `h≤g+2`; for `y=3`, it is exactly `g,h≥0`, `g+h≤5`, `h≤g`. The other nonnegativity constraints are automatic in these regions. Enumerating them yields the literal residual:

- `y=1`: `(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,0,1), (1,1,1), (1,2,1), (1,0,2), (1,1,2)`.
- `y=3`: `(3,0,0), (3,1,0), (3,1,1), (3,2,0), (3,2,1), (3,2,2), (3,3,0), (3,3,1), (3,3,2), (3,4,0), (3,4,1), (3,5,0)`.

The two lists contain 9 and 12 distinct triples. Conversely each satisfies all the displayed **scalar count equations** with nonnegative integer class counts; neither the converse nor the example establishes common sign/atom placement or Boolean realizability. For `(1,0,0)`, the formula gives `(A₁,C₂,C₃,D₁,G₂,G₃,H,O)=(16,4,6,21,1,0,0,16)`, which totals 64, has weight `48+2(4+6+21)+4=114`, and has squared sums `(56,144,132,124)`.

The exact remaining gap is to place both nonzero fibres' atoms and signs compatibly, satisfy all remaining nonzero-shift/common-spectrum correlations and Boolean inversion, or construct a target. None of those is certified by the 21-class list or by this review.

## 8. Reviewer-owned exact control and intended-reason negatives

I wrote and ran only the standard-library reviewer control `reviewer-exact-control-v1.py` in this wave. It does **not** import, execute, or compile author code. Script SHA-256 before execution: `4047c54972c8a00d892c068ae953e3a4b4c58d85f9b9914bcbae78040907bc93`; 7,406 bytes, 181 LF. Python reported `3.14.3`. The script's initially written undefined helper was replaced by standard-library `math.prod` **before hashing and the first execution**; no earlier execution took place.

One bounded run, tool deadline 120 s: native `/bin/date` immediately before the process was `2026-10-29T14:54:46-0700 PDT`; native `/bin/date` immediately after was `2026-10-29T14:54:47-0700 PDT`; process exit status **0**. A timeout or cap would have meant UNKNOWN, not exclusion. The run gave:

- all 81 ternary block shapes: `O=1`, `F=8`, `B=8`, `E=8`, `H=2`, and for each `j=1,2,3`, `A_j=8`, `C_j=4`, `D_j=4`, `G_j=2`;
- rank-five representative configurations: 128 sign/translation instances, all `N=22`; rank-four weight-four/even, weight-four/odd, weight-six/even, weight-six/odd: 64 instances each, respectively `N=28,16,4,40`; the two affine translations exhibit the two orientation multiplicity regimes;
- all `binom(8,6)·2^6=1,792` signed six-subsets of an affine three-space: `N=16` in 1,344 and `N=40` in 448. Every `N=40` case had absolute transform multiset `{0×4, 2×3, 6×1}`. The independent inverse-parity control checked all `binom(8,3)·2^3·8=3,584` three-`±4` coefficient/point combinations and found nonintegral inversion in each;
- direct enumeration from the scalar count equations independently returned exactly the 21 triples above and checked their parametrized counts; the two `y=7` signed products were 168 and −84 versus the required identity 24.

The script's seven intended-reason negatives all rejected the deliberately false propositions: five independent rank-four ratios (16 assignments observed, not 32); raw patterns always twice (a fixed-base pattern occurs four times); possible `N=34`; either `y=7` product equalling 24; inclusion of `(3,0,1)` despite negative `C₂`; and deletion of `(1,0,0)` while claiming the full list. These controls corroborate finite arithmetic; the written derivation above, not an author PASS or solver status, supplies the conditional argument.

## 9. Assurance boundary

This is a **same-harness** review, not human review, independent-model-family review, formal/kernel verification, or novelty verification. No author execution result, linked review, solver failure, withdrawn roster, m=116 packet, period packet, or CR7 premise is used. The stated mathematical support is limited to the frozen assumptions and the corrected necessary obstruction; the `(0,6,10)` case, `m=114`, rank two and the balanced target remain **OPEN**.
