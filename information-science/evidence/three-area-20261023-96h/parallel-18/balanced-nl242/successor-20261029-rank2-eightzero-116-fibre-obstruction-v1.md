# Rank two, eight zeros, m=116: a new (0,4,8) fibre obstruction

**UNREVIEWED AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T14:25:28-0700**. This packet attacks an actual remaining original-object fibre case; it is not a mod-8-period variant. It gives a written obstruction and an explicit residual, not a full exclusion of m=116, rank two, eight zeros, or the original target. It is not a Boolean witness, formal proof or novelty claim. No scientific computation, solver, test, model CLI, Git, deletion or publication was performed in this continuation.

This successor-round packet is stored in the author's explicitly permitted Oct-23 owner root. That storage does not reopen the closed Oct-23 round. The old P1 low-rank profile roster, all roster-based completeness claims, and held/withdrawn episodes are **NONINPUT**. The separate f239 period packet and its CR7 import are not used here.

## 1. Target, notation and exact claim

Let `f:F₂⁹→F₂` be balanced with `max|W_f|≤28`, put `k=W_f/4`, and assume the even-half polar B has rank two, the Walsh-zero set has size `Z=8`, and m—the number of agreeing unordered T-pairs—is **116**. The adopted caller/f131/f152 reductions, recalled in §2, give `T≠0` and show that the even quadratic q vanishes exactly on the six-dimensional radical R of B. Thus the even frequency space K is `R⊕F₂²`, with the q=0 fibre s=0 and three q=1 fibres `s=1,2,3`.

For each nonzero s let `e_s` count entries `|k|=2` in its 64-point fibre. Exact even energy gives `e₁+e₂+e₃=12`. This packet addresses the still-open fibre pattern

`(e₁,e₂,e₃)=(0,4,8)`                                              (P)

up to permutation of the three nonzero s labels. Put the even inverse u into 64 four-point blocks and use the local class labels defined in §3. Let `g=N(G₃)` and `h=N(H)` be two **global** block counts.

**Candidate obstruction.** Under the target assumptions and (P):

1. `g≠3`.
2. If `g=1`, then `h=0`.

Equivalently, the only pairs `(g,h)` not excluded by this packet are

`(0,0),(0,1),(1,0),(2,0),(2,1),(2,2),(4,0)`.                   (R)

These seven possibilities are a literal **necessary residual**, not claimed realizable. In particular, the packet does not establish that any actual f exists for one of them. The excluded cases are real strict subcases of (P); the full `(0,4,8)` fibre case remains open.

**Dependencies.** The adopted full Walsh caller, the mod-4 quadratic coupling and the general f131 zero/phase context are inputs. The proof rederives the small class table, four-atom and eight-atom sign counts, and the affine-flat intersection statement it uses. It does not invoke f166's incomplete profile split, f207's pending parent disposition, or any solver result. Standard character orthogonality and elementary symplectic/linear algebra are used. All deductions here remain at author-candidate scope pending a separately frozen review.

## 2. Rank-two setup and even energy

Let `T` be the XOR of the 256 points in the support of f, and `K=T^⊥`. The accepted caller gives `T≠0`, k even on K and odd off K, and makes q quadratic on K with polar B.

For completeness, z=64 follows without the withdrawn roster. On the odd coset H choose an affine origin and an identification H≅F₂⁸; all transforms in this paragraph are **eight-dimensional on that coset**. With the odd quadratic sign `g=(-1)^Q`, `D=n₁+n₃`, and the pointwise sign-switch decomposition `k=g(12h'−7)−8δ`, character orthogonality and Parseval give `m=116+D/2+2S`, where S is a signed sum of four values from `{−1,0,1}`. Hence `m≥108+D/2`. A rank-two q has z∈{64,128,192}; for z=128 or 192, the even energy bound `64m≤16(z−8)+36(256−z)` gives `m≤102` or `m≤82`, impossible. For z=64 the radical phase vanishes and the quotient quadratic is anisotropic, so q=0 exactly on R.

On s=0, the 64 even values are 8 zeros and 56 entries ±4. On each s≠0 they are ±2 or ±6. Thus

`64m=16(64−8)+4(e₁+e₂+e₃)+36(192−e₁−e₂−e₃)`.

At m=116 the sum is 12. We assume (P), a specific remaining partition of that sum; no claim is made that it is the only one.

## 3. Four-point blocks and the e₁=0 reduction

Choose coordinates dual to `K=R⊕F₂²`. The agreeing-pair ternary inverse `u:F₂⁸→{−1,0,1}` has `|supp u|=m`; write it as 64 four-entry blocks `u(c,·)` with `c∈F₂⁶`. Define their local Walsh transforms

`U_s(c)=Σ_{z∈F₂²}u(c,z)(−1)^{s·z}`.

The even spectrum is `Walsh₈(u)=2k`; character orthogonality gives

`Σ_c U₀(c)²=64−Z=56`, and `Σ_c U_s(c)²=144−2e_s` for s≠0.    (1)

The following class table is exhaustive: it follows by a four-point Walsh transform of 0,1,2,3,4 nonzero ternary entries. Here j∈{1,2,3} and absolute values are given.

| class | block weight | `|U₀|` | `|U_j|` | other two |
|---|---:|---:|---:|---|
| `A_j` | 3 | 1 | 3 | 1,1 |
| B | 3 | 3 | 1 | 1,1 |
| `C_j` | 2 | 2 | 2 | 0,0 |
| `D_j` | 2 | 0 | 0 | 2,2 |
| E | 4 | 2 | 2 | 2,2 |
| F | 1 | 1 | 1 | 1,1 |
| `G_j` | 4 | 0 | 4 | 0,0 |
| H | 4 | 4 | 0 | 0,0 |
| O | 0 | 0 | 0 | 0,0 |

For s≠0 define `v_s(r)=k(r,s)/2∈{±1,±3}`, `σ_s=sign(v_s)`, and `τ_s=σ_s·1_{|v_s|=1}`. Let `t_s=Walsh₆(τ_s)`. Then `τ_s` has exactly e_s signed atoms and

`16U_s=3 Walsh₆(σ_s)−2t_s`, hence `U_s≡t_s (mod 3)`.          (2)

When e₁=0, t₁=0, so U₁ is an integer multiple of 3; its absolute value is at most 4. Equation (1) forces exactly 16 entries of `|U₁|=3`. Therefore there are exactly **16 A₁ blocks**, and the only other possible classes are `C₂,C₃,D₁,G₂,G₃,H,O`.

## 4. Global class counts from the four-atom fibre

Use lowercase `c₂,c₃,d₁,g₂,g,h,o` for the indicated class counts, with `g=g₃`. Let `N₀(U₂)` be the number of zero U₂ entries. The four distinct signed atoms of τ₂ have affine rank 2 or 3. Their Walsh sum has one of these absolute-value histograms `(N₀,N₂,N₄)`:

`(0,64,0)`, `(48,0,16)`, `(24,32,8)`.                          (3)

Indeed, a rank-two support is an affine plane. If the four signs have product −1 the transform has magnitude 2 everywhere; if their product is +1 it is zero at 48 points and magnitude 4 at 16. At rank three, the three character ratios are independent: among their eight patterns, three give 0, four give magnitude 2 and one gives magnitude 4. Equation (2) shows `U₂=0` exactly where `t₂=0`, because U₂ can have only absolute values 0,1,2,4 here and `|t₂|≤4`.

The U₂ energy in (1) is 136. If `x=c₂+d₁` and `y=g₂`, then `x+4y=30`, while `N₀(U₂)=48−x−y`. The first two histograms in (3) are impossible; the third gives

`g₂=2`, `c₂+d₁=22`, `N₀(U₂)=24`.                              (4)

The 24 zero positions have an important geometry: they are `H₂\F₂`, where H₂ is an affine 5-flat and F₂⊂H₂ is an affine 3-flat. To see this, after dividing by one character and translating signs, the four-atom sum is `1+χ₁+χ₂+χ₃`. Its zero patterns have exactly two negative ratios; those and the all-positive pattern form an affine hyperplane H₂, while the all-positive pattern is F₂.

Use (1), `|supp u|=116`, and the total of 64 blocks. Direct substitution gives the complete count parametrization

`c₃=8−2g−2h`, `c₂=2+2g−2h`, `d₁=20−2g+2h`,
`g₂=2`, `o=16+g+h`, with `g,h≥0`, `g+h≤4`, `h≤1+g`.           (5)

Also U₃ has no ±3 entries, so (2) gives

`#{c:U₃(c)=0}=c₂+g₂+h+o=20+3g`
` = #{c:t₃(c)≡0 (mod 3)}`.                                      (6)

## 5. Excluding g=3 by the eight-atom relation

For g=3, (6) requires 29 zero-mod-3 values of the transform of eight distinct signed atoms in F₂⁶. Translate one atom to zero and let r be the affine rank of the eight atoms. The zero-mod-3 predicate depends only on r character ratios, so its number of occurrences is divisible by `2^(6−r)`. An odd count forces r=6.

At affine rank 6 the augmented eight atom columns have exactly one nonzero linear relation. It has even weight `w∈{4,6,8}`: odd weight is forbidden by augmentation and weight 2 by distinctness. The 64 character patterns correspond to the 128 sign patterns satisfying one fixed relation syndrome, modulo simultaneous reversal. A sum of eight signs is divisible by 3 exactly when the number of minus signs is 1, 4 or 7. Elementary binomial counting gives:

| relation weight w | zero count, even relation syndrome | zero count, odd relation syndrome |
|---:|---:|---:|
| 4 | 23 | 20 |
| 6 | 17 | 26 |
| 8 | 35 | 8 |

For example, at w=4 the even-syndrome counts at minus weights 1,4,7 are 4,38,4; divide their sum by two to obtain 23. The other entries follow from `Σ_{j even/odd} binom(w,j)binom(8−w,k−j)` for k=1,4,7. Neither syndrome gives 29, so **g=3 is impossible**. ∎

## 6. If g=1, excluding h≥1

With g=1, (6) gives 23 zero-mod-3 positions. They are odd in number, so the previous argument forces affine rank 6 and, by the table, a weight-4 relation with even syndrome. The four atoms in that relation form an affine 2-plane, with sign product +1; the other four character ratios are independent over that plane.

By an affine change of coordinates on the block space, sign translations and an irrelevant overall character, the eight-atom Walsh sum has the same zero-mod-3 set as

`t₃(u,v)=4·1_{u=0}+Σ_{j=1}⁴(-1)^{v_j}`, with `u∈F₂²`, `v∈F₂⁴`.

Its zero-mod-3 set is exactly

`B₀ = {(u,v):u≠0, |v|=2} ∪ {(0,v):|v|=1 or 4}`.             (7)

There are 18+5=23 points. By (4), `U₂=0` on `H₂\F₂`, and by the class table the intersection of the U₂- and U₃-zero sets consists exactly of the H and O blocks. From (5),

`|B₀∩(H₂\F₂)|=h+o=17+2h`.                                      (8)

### 6.1 Every hyperplane contains at most 19 points of B₀

For a character indexed by `(α,β)∈F₂²×F₂⁴` put `w=|β|`. Directly summing (7),

`Walsh(1_{B₀})(α,β) = (3 if α=0 else −1) K₂(w) + K₁(w)+K₄(w)`,

where `K₂(w)=(6,0,−2,0,6)` and `K₁(w)+K₄(w)=(5,1,1,−3,−3)` for w=0,…,4. For every nonzero character the absolute value is at most 15. Equality occurs only for `α=0`, `β=1111`, with coefficient +15. Consequently any affine hyperplane contains at most `(23+15)/2=19` points of B₀; the only one containing 19 is

`H_*={v:|v| is even}`.                                          (9)

Equation (8) therefore excludes h≥2. If h=1, the intersection in (8) is 19, so H₂=H_* and F₂ is an affine 3-flat in H_* **disjoint from B₀**.

### 6.2 No affine 3-flat in H_* is disjoint from B₀

Write `V_even={v:|v| even}` (dimension 3) and `L={0,1111}`. Equation (7) becomes

`B₀∩H_* = ((F₂²\{0})×(V_even\L)) ∪ {(0,1111)}`.               (10)

Let F⊂F₂²×V_even be an affine 3-flat. Consider the dimension of its projection onto the u-coordinates.

- Dimension 0: if u=0, F contains `(0,1111)`; otherwise its V_even fibre contains a point outside L.
- Dimension 1: one projected u is nonzero, and its four-point fibre cannot fit in the two-point L.
- Dimension 2: each fibre is a two-point line, and all four lines are parallel. Avoiding (10) forces all three nonzero-u fibres to equal L. The affine map of their offsets in `V_even/L` is then zero at the three nonzero u values, hence also at u=0. That fibre is L and contains `(0,1111)`.

Thus no such F exists, contradicting h=1. Together with h≥2 already excluded, **g=1 implies h=0**. ∎

## 7. Exact residual and arithmetic control

Nonnegativity in (5) gives g∈{0,1,2,3,4}, `g+h≤4` and `h≤1+g`. Removing g=3 and removing h>0 at g=1 gives exactly the seven pairs (R) in §1.

A non-vacuous **class-count relaxation** at the surviving pair `(g,h)=(1,0)` is

`A₁=16, C₂=4, C₃=6, D₁=18, G₂=2, G₃=1, H=0, O=17`.

The counts total 64, their block weights total 116, and their U₀,U₁,U₂,U₃ square sums are respectively 56,144,136,128. This is only an integer class-count control: it does not exhibit compatible atom placements/signs, the common Walsh spectrum, or a Boolean f. It shows why this packet does not claim the whole (P) case is impossible.

The first unproved step is to enforce the actual common signs/frequency geometry and the remaining nonzero-shift caller equations for the seven residual pairs, or produce an actual target. The other m=116 e-patterns, m=114, all other rank-two cases, ranks 4/6/8 and the original balanced witness-or-exclusion question remain open at their respective scopes.

## 8. Source pins and status

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Adopted prerequisite | SHA-256 | LF | Scope used |
|---|---|---:|---|
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | full caller, parity and common quadratic coupling |
| `P/info-6-four-zero-rank6-radical-parent-v1.md` | `12efd10b4a9de2ac70cd49541e36e6a0c5df6bd4deecbb74e085c2eb48795dc3` | 31 | general quadratic/zero context; no four-zero branch conclusion |
| `P/info-6-four-zero-unequal-radical-phases-parent-v1.md` | `a31e8f9c5c913d67ab980367e0347d64b1f6ad5e55c8d7bf0aab9efc85fbc6ec` | 27 | T≠0 and common odd/even polar; no four-zero phase exclusion |

All three are imported only at their same-harness written-support scope. The block argument, exact relation-code table, hyperplane calculation, flat lemma and class-count control in this file need a fresh disjoint full-scope review. No independent-model-family, human, formal/kernel, computational replay or novelty verification was performed for this packet. All standing STOP/HOLD/ZERO/NONINPUT controls remain binding.
