# Rank two, eight zeros: an obstruction to even-half mod-8 periods

**UNREVIEWED AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T14:06:36-0700**. This is one written obstruction in a genuinely remaining rank-two fibre case. It is not a complete rank-two exclusion, an eight-zero exclusion, a witness, a global NL242 theorem, a formal proof, or a novelty claim. No scientific computation, solver, test, model CLI, Git, deletion or publication was performed for this packet.

This successor-round packet is stored in the author's explicitly permitted Oct-23 owner root; that storage does not reopen the closed Oct-23 round. The earlier f166 roster-based completeness claims and all held or withdrawn sources/episodes remain NONINPUT. This proof does **not** use the defective P1 profile list or the claimed rank-two closure.

## 1. The theorem and its external dependency

Let `f:F₂⁹→{0,1}` be balanced with `max|W_f|≤28`, `k=W_f/4`, and exactly eight zeros `Z`. Assume the even-half quadratic polar B has rank two. Put `T=⊕{x:f(x)=1}`, `K=T^⊥`, `q=(k/2 mod 2)|K`, `R=rad B`, `D=n₁+n₃` for odd-half coefficients with `|k|=1` or 3, and m for the agreeing unordered T-pairs.

The accepted caller/f131/f152 inputs and the reductions rederived in §2 give `T≠0`, `q⁻¹(0)=R` with `dim R=6`, and `Z=W`, a linear 3-space contained in R. Translate f once so that the odd-half quadratic phase is invariant along W. This translation preserves T, q, R, Z, m and D. For this normalized representative define the **even mod-8 stabilizer**

`G={r∈W : k(a+r)≡k(a) (mod 8) for every a∈K}`.

**Candidate theorem.** If `G` contains a nonzero r, then `D≥20` and `m≥118`. In particular, if `m≤116`, or if `D≤16`, then `G={0}`. Thus the entire still-open rank-two/eight-zero `m=114` and `m=116` domain has no nonzero even-half mod-8 period after the stated phase normalization. This is a **structural exclusion of a fibre subcase**, not exclusion of those m-values or of rank two.

**External input, explicitly not yet adopted by the parent.** The theorem uses the classical seven-variable first-order Reed–Muller covering-radius bound:

> **(CR7)** For every Boolean sign function `g:F₂⁷→{−1,1}`, `max_ξ |Walsh₇(g)(ξ)|≥16`.

Equivalently `ρ(RM(1,7))=56`. The introduction of Wang–Lou–Wang, [*The Covering Radius of RM(1,9) is 242*, arXiv:2610.17871v1](https://arxiv.org/html/2610.17871v1), explicitly attributes the `RM(1,7)` value 56 to J. Mykkeltveit, “The Covering Radius of the (128,8) Reed–Muller Code is 56,” *IEEE Transactions on Information Theory* **26** (1980), 359–362, and cites X. Hou, “Covering Radius of the Reed–Muller Code R(1,7) — A Simpler Proof,” *Journal of Combinatorial Theory A* **74** (1996), 337–341. The cited arXiv paper's statement and bibliography were read; the 1980 and 1996 proofs were **not** opened or independently checked. The candidate theorem is conditional on (CR7), and its use needs a parent-approved frozen import/review. No claim that the 2026 RM(1,9) theorem itself has been adopted is made.

Without (CR7), the proof still establishes the weaker **written obstruction**: if `G` has a nonzero element, then `D≥16`, the odd-half phase in §4 is identically 1, and the counts in §5 hold. The step upgrading 16 to 20 is exactly where (CR7) is used.

## 2. Independent setup and bounds

The f131 degree reduction gives `1_Z∈RM(5,8)` at polar rank two. A minimum-weight word of RM(5,8) has support an affine 3-flat; since `0∈Z`, Z is a linear 3-space. We recall the z=64 reduction without using a profile list.

Identify the odd coset with K by an affine origin and use the **eight-dimensional** Walsh transform there. Let `g=(-1)^Q`, where Q is the odd-half quadratic and has polar B; put `h=1_{|k|∈{3,5}}`. The pointwise decomposition

`k=g(12h−7)−8δ`, with `wt(δ)=D` and `Σδg=n₃−n₁`,

together with odd-half Parseval gives

`m=116+D/2+2S`, where `S=Σ_{y∈Y}σ(y)v(y)`, `|Y|=4`, `|S|≤4`, and `v=Walsh₈(k|H)/128∈{−1,0,1}`.

Here Y is the complete Walsh support of g. In particular `m≥108+D/2`; balance makes m even, so `D≡0 (mod 4)`. This explicitly fixes the transform-domain ambiguity noted in f207's MINOR m1. It introduces no relation `m≡1−D`.

The even energy is at most `16(z−8)+36(256−z)`. At polar rank two, `z∈{64,128,192}`; for the latter two this gives `m≤102` or `m≤82`, contrary to `m≥108`. Hence z=64, q is anisotropic on K/R, and `q⁻¹(0)=R`. Thus W=Z⊂R. With `E=#{a∈K:|k(a)|=2}`, exact even Parseval gives

`64m=16(64−8)+4E+36(192−E)=7808−32E`,

so `E=244−2m` and

`E+D≤28`.                                                        (1)

These are whole-half identities and bounds, not a finite unsigned-profile census.

For r∈W, the odd quadratic changes by a constant `ρ(r)` because r is in R. The map `ρ:W→F₂` is linear. An input translate t with `r·t=ρ(r)` for every r∈W makes ρ vanish on W. If two translates achieve that normalization, their difference is orthogonal to W; therefore they induce the same stabilizer G, although their individual signed coefficients may differ.

## 3. One direction and an exact pair-count identity

Assume, for contradiction or reduction, that a nonzero `r∈G` exists. In the normalized representative:

- On K, `k(a+r)≡k(a) (mod 8)` by definition of G.
- On H, the phase normalization gives `k(b+r)≡k(b) (mod 4)`.
- On K the mod-8 relation also implies mod-4 equality. Thus **every** r-pair in the full 512-frequency domain has a difference divisible by 4.

Because `|k|≤7`, its absolute difference is in `{0,4,8,12}`. Let `N_j` be the number of the 256 unordered r-pairs with absolute difference j. Booleanity of f gives the exact nonzero-shift correlation `Σ_a k(a)k(a+r)=0` and `Σ_a k(a)²=2¹⁴`. Therefore

`16N₄+64N₈+144N₁₂=16384`, `N₀+N₄+N₈+N₁₂=256`,

hence

`5N₁₂=4N₀+3N₄`.                                                (2)

This explicitly uses the full caller's r-correlation, not merely a scalar magnitude histogram.

Among the 128 even pairs, 32 lie in R. Four of those are the zero pairs in W; the other 28 consist of ±4 values. Their differences are 0 or 8. The other 96 even pairs lie at q=1. A difference 8 there pairs an entry of magnitude 2 with one of magnitude 6, so there are at most E such pairs. Since every even pair is congruent modulo 8,

`N₀(K)≥128−28−E=100−E`; in particular `N₄(K)=N₁₂(K)=0`.       (3)

## 4. The odd mod-8 phase must be constant 1

Let M be the 256-point support of the normalized f, `M^r={x∈M:r·x=1}`, `N^r(a)=#{x∈M^r:a·x=1}`, and `τ^r=⊕M^r`. Because r∈Z and r≠0, `|M^r|=128`. Counting the flip of `[a·x]` over M^r gives, modulo 8 even at the zero-frequency exceptional points,

`k(a+r)−k(a) ≡ |M^r|−2(a·τ^r)−4 binom(N^r(a),2)`.

The binomial term is a Boolean polynomial of degree at most two in a. Mod-4 equality for **every** a forces `a·τ^r=0` for every a, hence `τ^r=0`. Thus

`k(a+r)−k(a) ≡4φ_r(a) (mod 8)`,

for a quadratic Boolean φ_r, and φ_r vanishes on K because r∈G. Restricting a quadratic that vanishes on K to the complementary affine hyperplane H gives an affine function there. Also `φ_r(a+r)=φ_r(a)`, since the two differences are negatives and `4φ_r` is unchanged by sign modulo 8. Consequently the number t of odd unordered r-pairs with φ_r=1 is exactly 0, 64, or 128.

When φ_r=0 on an odd pair, the entries have the same residue modulo 8. If neither has magnitude 1 or 3, then their magnitudes are 5 or 7; same mod 4 and mod 8 forces them to be equal. At most D odd pairs can touch one of the D low-magnitude coefficients. Therefore

`N₀(H)≥128−t−D`.                                                (4)

Every difference-12 pair is odd and has φ_r=1, so `N₁₂≤t`.

- If `t=0`, then `N₁₂=0`, contradicting (2) and `N₀(K)≥100−E≥72`.
- If `t=64`, then by (1), (3), and (4), `N₀≥(100−E)+(64−D)≥136`. Equation (2) gives `5N₁₂≥4·136=544`, but `5N₁₂≤320`. Contradiction.

Therefore **t=128**: every odd r-pair differs by 4 modulo 8. The only possible absolute differences there are 4 and 12; every even pair differs by 0 or 8.

## 5. Defect count and the CR7 step

Write `b=N₄(H)`. Since t=128, `N₁₂=128−b` and `N₀=N₀(K)`. Equation (2) becomes

`N₀(K)+2b=160`.                                                  (5)

There are only 128 even pairs, so `b≥16`. An odd difference-4 pair must touch at least one of the D coefficients of magnitude 1 or 3: two high-magnitude entries in the same mod-4 class are either equal or differ by 12. Distinct r-pairs are disjoint, hence `b≤D`. This proves `D≥16` and `m≥116` **without (CR7)**.

Suppose now `D=16`. Then b=16 and (5) forces `N₀(K)=128`. Thus the even k is not merely congruent: it is **exactly invariant**, `k(a+r)=k(a)` for all a∈K.

Choose `a₀∈H`, set `L={x:a₀·x=0}`, and write every point uniquely as `y` or `y+T` with `y∈L`. For `s(x)=(-1)^{f(x)}` define ternary functions

`u(y)=(s(y)+s(y+T))/2`, `v(y)=(s(y)−s(y+T))/2`.

Then `u(y)²+v(y)²=1`, `Walsh₈(u)(a)=2k(a)` for a∈K, and `Walsh₈(v)(a)=2k(a₀+a)`. Exact invariance under r gives `u(y)=0` on the affine 7-flat `A={y∈L:r·y=1}`; hence `v|A` is a Boolean sign function. For a∈K its seven-variable Walsh coefficient, up to the harmless sign caused by the choice of affine origin of A, is

`B_a = Σ_{y∈A}v(y)(−1)^{a·y} = k(a₀+a)−k(a₀+a+r)`.

As a ranges over K/⟨r⟩, this lists all 128 Walsh coefficients of `v|A`. The constant odd mod-8 phase gives `|B_a|∈{4,12}` for all a. This contradicts (CR7), which requires a coefficient of magnitude at least 16.

Thus `D≠16`. Since D is a multiple of 4 and `D≥16`, we get `D≥20` and hence `m≥108+D/2≥118`. Therefore m≤116 forces `G={0}`. ∎

## 6. Non-vacuous arithmetic control and residual

The (CR7) step cannot be replaced by the pair counts alone. The following **formal pair multiset**, with no frequency placement or claimed function, meets the magnitude, energy and single-r-correlation arithmetic:

- Even half: four `(0,0)` pairs; 28 `(4,4)` pairs; 96 `(6,6)` pairs. Then `E=0`, `m=122`, and the even squared energy is `7808`.
- Odd half: 8 `(-3,1)` pairs, 8 `(1,5)` pairs, and 112 `(-7,5)` pairs. Then `(n₁,n₃,n₅,n₇)=(16,8,120,112)`, `D=24`, and the odd squared energy is `8576`.
- The sum of the products over the even pairs is `3904`; the sum over the odd pairs is `−3904`. Hence the one selected r-correlation is zero, while (5) has `N₀(K)=128`, `b=16`.

This control checks only explicit integer arithmetic. It is **not** a labelled common spectrum, a Boolean function, a verification of the other 510 correlations, or a target witness. If it came from an actual f with the assumed exact even period and odd mod-8 phase, §5 and (CR7) would rule it out.

The first unproved residual is whether a rank-two/eight-zero target can have a **trivial** G. In particular, neither `m=114` nor `m=116` has been excluded. Cases with nonzero G and `D≥20`, and all other ranks/zero counts, also remain open here. A future attempt must use further common-frequency geometry or actual Booleanity; the former defective low-rank profile list does not cover this residual.

## 7. Exact pins, review status and boundaries

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`; `F=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f207-nl242-eight-zero-all-ranks-parity/`.

| Source | SHA-256 | LF | Role |
|---|---|---:|---|
| `P/info-6-four-zero-rank6-radical-parent-v1.md` | `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3` | 31 | f131 degree / rank≤4 input |
| `P/info-6-four-zero-unequal-radical-phases-parent-v1.md` | `a31e8f9c5c913d67ab980367e0347d64b1f6ad5e55c8d7bf0aab9efc85fbc6ec` | 27 | f152 common phase context, not its four-zero-only conclusion |
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | full caller / mod-4 |
| `successor-20261029-eightzero-all-ranks-parity-v1.md` | `5ddc94327a59f8bc4511267fedd08576d8f98fbb21fb94206e541c24b60774cc` | 206 | author context; its rank-two facts are rederived above |
| `F/review-v1.md` | `0d998c348e0e0031b764cf9476e321f8887a42bcfe9042423784ddeff1aa0a2b` | 156 | f207 reports 0F/0M/1m, pending parent disposition; m1 respected in §2 |

The external (CR7) theorem is a **separate explicit mathematical input**, not an f131/f152 adoption. The new argument, count control and restrictions have not been disjointly reviewed, formally checked or novelty-audited. All historical STOP/HOLD/ZERO/NONINPUT controls continue unchanged.
