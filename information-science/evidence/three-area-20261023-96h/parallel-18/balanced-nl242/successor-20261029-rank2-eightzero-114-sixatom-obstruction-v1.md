# Rank two, eight zeros, m=114: a six-atom fibre obstruction

**UNREVIEWED AUTHOR CANDIDATE.** Native clock observed before writing: **2026-10-29T14:45:11-0700**. This packet treats a genuinely different remaining original-object case: `m=114` with `(e₁,e₂,e₃)=(0,6,10)`. It is not a variant, erratum, or claimed extension of the frozen m=116 packet f244, and uses no period hypothesis or f239 result. It does not exclude m=114, this entire fibre case, rank two, eight zeros, or the original balanced target. No scientific computation, solver, test, model CLI, Git, deletion or publication was performed in this continuation.

The successor packet is stored in the author's explicitly permitted Oct-23 owner root; this does not reopen that closed round. The incomplete P1 profile roster and all roster-based completeness claims, held episodes and withdrawn sources are NONINPUT.

## 1. Scope and claim

Let `f:F₂⁹→F₂` be balanced, `max|W_f|≤28`, and let `k=W_f/4`. Assume `T=⊕{x:f(x)=1}≠0`, that the even-half quadratic polar has rank two, that the total number of Walsh zeros is `Z=8`, and that the number of agreeing unordered T-pairs is `m=114`.

Assume also the **actual fibre condition** `(e₁,e₂,e₃)=(0,6,10)` up to permutation, where `e_s` counts coefficients with `|k|=2` in the corresponding nonzero q-fibre. The q-fibres, block types and notation are defined below; the q-zero count is not imported from the invalid profile list.

Let `y` count type `G₂` blocks, `g` count type `G₃` blocks, and `h` count type H blocks. The following are **necessary**:

1. `y∈{1,3}`; the values `0,2,4,5,6,7` are impossible.
2. If `y=1`, the six small coefficients in fibre 2 have affine rank 5.
3. If `y=3`, they have affine rank 4, and their unique affine relation has weight 4 and even sign syndrome.
4. The exact remaining class-count parameter triples are the 21 triples listed in §7. They are necessary options, **not** realizations of a Boolean function.

The proof below includes the finite six-atom counts and the only two remaining hard branches, using elementary character sums. It does not use a solver or an unsigned D/m roster. All deductions require disjoint review.

## 2. Even frequency fibres and local ternary blocks

The accepted caller makes k even on `K=T^⊥` and makes `q=(k/2 mod 2)|K` quadratic with polar B. For rank two, q has zero count `z∈{64,128,192}`. At q-zero positions k is 0 or ±4; at q-one positions it is ±2 or ±6. Because there are exactly 8 zeros,

`64m≤16(z−8)+36(256−z)`.

With m=114, z=128 or 192 gives `m≤102` or `m≤82`, a contradiction. Therefore z=64; the radical phase vanishes, the rank-two quotient is anisotropic, and q=0 exactly on the six-dimensional radical R.

Take coordinates `K=R⊕F₂²` with q-zero fibre s=0. Choose the agreeing-pair inverse `u:F₂⁸→{−1,0,1}`; it has `|supp u|=m` and `Walsh₈(u)=2k` on K. View u as 64 four-point blocks `u(c,·)`, c∈F₂⁶, and put

`U_s(c)=Σ_{z∈F₂²}u(c,z)(−1)^{s·z}`.

The q-zero fibre has 8 zeros and 56 entries ±4; the other fibres have e_s entries ±2 and the rest ±6. Parseval gives

`Σ_c U₀²=56`, `Σ_c U_s²=144−2e_s`, and `64m=7808−32Σ_s e_s`.

Thus m=114 requires `Σe_s=16`, consistent with the assumed `(0,6,10)`.

The local Walsh shapes of the four-entry ternary blocks are obtained directly by transforming blocks of weights 0,1,2,3,4:

| class | weight | `|U₀|` | `|U_j|` | other two |
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

For s≠0 define `v_s(r)=k(r,s)/2∈{±1,±3}`, `σ_s=sign(v_s)`, `τ_s=σ_s·1_{|v_s|=1}`, and `t_s=Walsh₆(τ_s)`. The support of τ_s consists of e_s **distinct signed atoms**. Inverse Walsh gives

`16U_s=3Walsh₆(σ_s)−2t_s`, so `U_s≡t_s (mod 3)`.             (1)

With e₁=0, U₁ is an integer multiple of 3 of magnitude at most 4. Its square sum is 144, so exactly 16 blocks are A₁. The only other possible classes are `C₂,C₃,D₁,G₂,G₃,H,O`.

## 3. The class-count equations

Use lower-case counts `c₂,c₃,d₁,y,g,h,o` for those seven classes. In the second fibre, e₂=6, so `ΣU₂²=132`. Its nonzero entries occur at the 16 A₁ blocks, at `c₂+d₁` blocks with magnitude 2, and at y blocks with magnitude 4. Therefore

`c₂+d₁+4y=29`, `N:=#{U₂=0}=48−c₂−d₁−y=19+3y`.             (2)

In these allowed classes `U₂∈{0,±1,±2,±4}`. Equation (1) therefore says

`N= #{c:t₂(c)≡0 (mod 3)}`.                                    (3)

There are six distinct atoms. Their affine rank is 3, 4, or 5. The zero predicate for t₂ modulo three factors through the affine-rank character ratios, so its number of points is divisible by `2^(6−rank)`. In particular N is even. Since (2) also gives `0≤y≤7`, y must lie in `{1,3,5,7}`.

## 4. Six signed atoms: exact zero counts

The following table gives all zero-mod-3 counts needed for (3). It follows from a binomial count, not a numerical solver or a frozen m=116 packet.

| affine rank of six atoms | relation / syndrome | possible N |
|---:|---|---:|
| 5 | no affine relation | 22 |
| 4 | unique relation, weight 4; even or odd syndrome | 28 or 16 |
| 4 | unique relation, weight 6; even or odd syndrome | 4 or 40 |
| 3 | support lies in an affine 3-space | a multiple of 8 |

For rank 5, the six character signs are independent up to global reversal. A sum of six ±1 signs is divisible by 3 exactly at minus weights 0,3,6; this occurs `1+20+1=22` times among 64 sign patterns, giving N=22.

At rank 4, the augmented six atom columns have one nonzero relation. Its weight is even and cannot be 2, so it is 4 or 6. For a fixed sign syndrome the relation requires even or odd minus parity on its w positions. At minus weights 0,3,6, the admissible sign-pattern counts are:

| w | even syndrome | odd syndrome |
|---:|---:|---:|
| 4 | `1+12+1=14` | `0+8+0=8` |
| 6 | `1+0+1=2` | `0+20+0=20` |

Each occurs twice on F₂⁶, giving N=28/16 and 4/40. At rank 3, the predicate is constant on cosets of a 3-space and N is a multiple of 8.

Thus `y=5`, which would give N=34, is impossible. `y=1` gives N=22 and necessarily affine rank 5. `y=3` gives N=28 and necessarily affine rank 4, relation weight 4 and even syndrome. It remains to rule out y=7.

## 5. Excluding y=7 using the signed inner product

If y=7, (2) yields `c₂+d₁=1` and N=40. We use the exact identity

`Σ_c U₂(c)t₂(c)=4e₂=24`.                                      (4)

It follows from (1), `ΣWalsh(σ₂)t₂=64Σσ₂τ₂=64e₂`, and `Σt₂²=64e₂`.

For N=40 the affine rank is 4 or 3. Rank 5 gives N=22. At rank 4, the preceding table forces the **weight-6 relation and odd sign syndrome**. All six signs then have odd minus parity, so their Walsh sum has only values 0 or ±4: minus weight 3 gives 0, while weights 1 and 5 give ±4. There are exactly 24 nonzero positions.

The class counts at y=7 give 16 entries `|U₂|=1`, one `|U₂|=2`, and seven `|U₂|=4`. Since `t₂≡U₂ (mod 3)`, their respective products U₂t₂ are 4, −8, and 16. Hence

`ΣU₂t₂=16·4−8+7·16=168`,

contradicting (4).

At rank 3, the zero predicate repeats eightfold, so N=40 corresponds to five of the eight values of a 3-dimensional Walsh transform being divisible by 3. This transform is that of a ternary six-point sign function and has squared sum `8·6=48`; its values are even and bounded by 6. The other three coefficients have magnitude 2 or 4.

- If none of the five divisible-by-3 coefficients has magnitude 6, the other three must all have magnitude 4. Inverting three coefficients ±4 would give only half-integers `(±4±4±4)/8`, impossible for a ternary function.
- Otherwise exactly one has magnitude 6, and the other three nonzero coefficients must all have magnitude 2. On F₂⁶ this repeats to four-zero-coefficient orbits (32 points), three magnitude-2 orbits (24 points), and one magnitude-6 orbit (8 points). Hence at every nonzero U₂ entry, `|t₂|=2`. The congruence in (1) forces products −2, 4, −8 at `|U₂|=1,2,4`, respectively. Thus

`ΣU₂t₂=16·(−2)+1·4+7·(−8)=−84`,

again contradicting (4). Therefore **y=7 is impossible**. This proves items 1–3 in §1. ∎

## 6. Complete class-count parametrization

Write `g=N(G₃)` and `h=N(H)`. The U₀ square sum, the total block weight 114, the total of 64 blocks, and (2) give

`c₃=4+2y−2g−2h`, `c₂=6−2y+2g−2h`,
`d₁=23−2y−2g+2h`, `o=15+y+g+h`.                              (5)

All counts are nonnegative integers. For y=1, (5) is equivalent to `g+h≤3` and `h≤g+2`. For y=3 it is equivalent to `g+h≤5` and `h≤g`. Conversely, each triple satisfying these inequalities gives nonnegative **class counts** obeying the displayed scalar sums; this converse is only at the class-count level.

## 7. Literal residual and non-vacuous control

The 21 remaining `(y,g,h)` triples are

- y=1: `(1,0,0),(1,1,0),(1,2,0),(1,3,0),(1,0,1),(1,1,1),(1,2,1),(1,0,2),(1,1,2)`;
- y=3: `(3,0,0),(3,1,0),(3,1,1),(3,2,0),(3,2,1),(3,2,2),(3,3,0),(3,3,1),(3,3,2),(3,4,0),(3,4,1),(3,5,0)`.

All other class counts are determined by (5) and `A₁=16`. The affine-rank/syndrome conditions of §1 remain mandatory. This list does not claim that its entries have actual atom placements, compatible signs, common spectra or Boolean realizations.

A formal class-count control at `(y,g,h)=(1,0,0)` is

`A₁=16, C₂=4, C₃=6, D₁=21, G₂=1, G₃=0, H=0, O=16`.

These total 64 blocks, have total block weight 114, and have square sums `(U₀,U₁,U₂,U₃)=(56,144,132,124)`. This is an arithmetic control only, not a target witness or a proof that the six-atom constraints can be placed with the rest of the spectrum.

The first unproved step is to impose a common placement and signs across both nonzero fibres, the remaining nonzero-shift correlations, and Boolean inversion on all 21 triples, or construct an actual target. Other m=114 fibre patterns, m=116, other ranks and the original witness-or-unrestricted-exclusion problem remain open. No conclusion about f244 is drawn here.

## 8. Inputs and verification boundary

`P=/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/`.

| Prerequisite | SHA-256 | LF | Scope |
|---|---|---:|---|
| `P/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | full caller and common mod-4 quadratic coupling |
| `P/info-6-four-zero-unequal-radical-phases-parent-v1.md` | `a31e8f9c5c913d67ab980367e0347d64b1f6ad5e55c8d7bf0aab9efc85fbc6ec` | 27 | general T≠0 and common phase; not the four-zero conclusion |

The source pins are the metadata values observed before the immediately preceding owner packet; the inputs have not been rehashed during this continuation. All cited results remain at same-harness written-support scope. The rank-two local block argument and six-atom table in this file need fresh disjoint review. No independent-model-family, human, formal/kernel, computational replay, or novelty verification was performed. No source listed above is a withheld or incomplete P1 profile roster.
