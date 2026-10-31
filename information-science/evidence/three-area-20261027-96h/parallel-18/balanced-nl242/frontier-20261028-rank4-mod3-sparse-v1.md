# info-6 frontier: rank-four modulo-three sparse obstruction

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:35:00-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This is additive to the immutable collective-polar packet and gives a shorter independent route for its rank-four z=128 subcase. It depends on that unreviewed collective identity and on the parent-adopted caller, not on the unreviewed quartic/orbit candidates. No unrestricted no-go, target witness, novelty, disjoint review, or formal verification is claimed.

## Statement

Let f:F₂⁹→F₂ be balanced with nonzero support XOR T and `max|W_f|≤28`. Suppose its even-half polar B has rank four. Write z for the even quadratic's zero count, Z for the number of Walsh zeros, m for agreeing unordered T-pairs, n_j for odd-half `|W_f/4|=j`, and `D=n₁+n₃`. Then

    z=96,    D∈{8,10,12,14,16,18,20,22,24},
    104≤m≤112,    Z≤40,    n₇≤197.                                (1)

The collective predecessor proves rank-four z=160 impossible, z=96 gives m≤112 and D≤24, and for every rank-four case D is even with

    m=116+S+D/2,    S=Σ_{y∈Y}σ(y)v(y),   |Y|=16.                 (2)

Here Y is the affine Walsh support of the odd quadratic's sign g, `Walsh(g)=64σ` on Y, and the actual ternary `v=Walsh(k)/128`. The new argument shows that **D=0,2,4,6 are impossible for any rank-four case**; then z=128 is excluded immediately by its even-energy upper bound m≤102 versus `m≥100+D/2≥104`. No claim is made about existence or nonexistence in the remaining z=96 branch.

## A universal modulo-three count identity

Use the predecessor's sign-switch decomposition `k=g(12h−7)−8δ`, with δ∈{−1,0,1} and wt(δ)=D. Modulo 3,

    Walsh(δ)(y)+v(y)≡Walsh(g)(y).                                 (3)

Let `M=#{y:Walsh(δ)(y)≠0 mod 3}` and let `a=#{y∈Y:Walsh(δ)(y)≡0 mod 3}`. Because `64≡1 mod 3`, write `d_y=σ(y)Walsh(δ)(y) mod3` and `u_y=σ(y)v(y)∈{−1,0,1}` on Y. Equation (3) gives `d_y+u_y≡1`. Thus: d=0 gives u=+1 and adds an inverse-support point compared with M; d=1 gives u=0 and removes one; d=2 gives u=−1 and keeps one. Outside Y, v is nonzero exactly where Walsh(δ) is nonzero modulo 3.

If the numbers of Y indices in d classes 0,1,2 are a,b,c, then a+b+c=16, `wt(v)=M+a−b`, and `S=a−c`. Since `wt(v)=256−m`,

    m−S=272−M−3a.                                                 (4)

Combining (4) with (2) yields the exact integer identity

    M+3a = 156−D/2,     0≤a≤16.                                  (5)

This uses all 16 quadratic-support indices and all 256 inverse positions; it is not a selected-frequency test.

## Excluding D=0,2,4

For D=0, `M=0,a=16`, contradicting (5). For D=2, Walsh(δ) is 0 on exactly half of F₂⁸ and ±2 on the other half, so M=128. Equation (5) requires a=9, but on the affine 4-space Y the zero set of a two-character sum is either empty, all of Y, or an affine hyperplane of size 8. Thus a∈{0,8,16}, contradiction.

For D=4, the four distinct signed support points have affine rank 2 or 3. Rank 3 gives M=160. Rank 2 is an affine plane; according to the product of its four signs, M is 64 or 256. Equation (5) requires `M+3a=154`: M=64 would give a=30, while 160 and 256 exceed 154. Therefore D=4 is impossible. ∎

## Excluding D=6

Six distinct atoms have affine rank r∈{3,4,5}. Equation (5) requires `M+3a=153`, so `105≤M≤153` and M is divisible by 3.

* r=5: the six character signs are independent up to global sign. Among 64 sign patterns, the sums divisible by 3 are −6,0,6, occurring `1+20+1=22` times. Hence `M=4·42=168`, too large.
* r=4: there is one nonzero affine relation among the six atoms. It has even weight 4 or 6, since the atoms are distinct. The two sign syndromes give M values `{144,192}` for relation weight 4 and `{96,240}` for relation weight 6; the finite checker verifies these four elementary binomial counts. Only M=144 lies in the required range, forcing a=3.
* r=3: each character pattern is repeated 32 times in F₂⁸, so M is a multiple of 32. The only multiple in [105,153] is 128, not divisible by 3.

For the r=4 survivor, translating one atom to 0 shows that the zero-modulo-three predicate for Walsh(δ) is constant on cosets of a four-dimensional subspace H (a possible overall sign changes neither zero nor nonzero). M=144 means 112 zero positions, namely 7 zero patterns in the 16-element quotient F₂⁸/H. Restrict this predicate to the affine 4-space Y. If `dim(dir(Y)∩H)=d`, its number a of zero positions is divisible by `2^d`. Since a=3 is odd, d=0 and the restriction map is bijective onto the entire quotient; it must then contain all 7 zero patterns, not 3. Contradiction. Thus D=6 is impossible. ∎

With D≥8 even and the collective bound, rank-four z=96 has m≥104 and D≤24. In that branch even energy gives `Z+2D≤56`, so Z≤40. Finally `256+48n₇≤64(256−m)` implies n₇≤197. These complete (1).

## Intended-reason control and limits

The checker verifies the six-atom sign-pattern table and gives an explicit **D=8 coarse near miss**: a rank-four quadratic sign with |Y|=16, a signed eight-atom δ with M=152 and a=0, and a ternary v determined by (3). It has m=110, S=−10, n₁=3, n₃=5 and satisfies (2) and (5). It is not a target witness: its reconstructed odd-half Walsh transform reaches magnitude 50 rather than at most 14, fails that bound at 43 positions, and its odd modulo-4 quadratic mismatches all 256 positions. No even half or Boolean realization is claimed. This shows the sparse-count proof is not rejecting every D=8 modulo-three model.

All new conclusions, the finite sign counts, and the collective predecessor require disjoint review. This does not exclude rank-four z=96, any rank-six/eight branch, or the original target.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank4-mod3-code-check.py` | `89e682cba2cb813fd89f60c90553ec3b977bdfb0feed2160b59e93b8550aab93` | 57 | finite and coarse-positive controls |
| `frontier-20261028-rank4-mod3-code-check-result.json` | `2184d3ac6360e9947b01095e7eb50ea66d4f8a833e4b356f144209ebff0321a7` | 48 | finite receipt |
| `frontier-20261028-collective-polar-exclusion-v1.md` | `e562e6074dec7beb4a713eed24c3044d6115965de0c60b5c9faf7827da86426d` | 108 | unreviewed collective predecessor |

**END.**
