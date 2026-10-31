# info-6 frontier: phase divisibility at the rank-two cubic boundary

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T19:58:11-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**; no frozen review is changed, and no unrestricted exclusion or witness is claimed.

## Statement

For an actual balanced f:F₂⁹→{0,1} with full Walsh peak≤28, use the even-half polar B, odd quadratic Q, peak/unit indicator P, and signed counts A_t of the preceding papers. If

    rank(B)≤2     and     wt(P)=224,

then

    A₃+A₋₅ = #{P=0,Q=1} ∈ {0,8,16,24,32}.                                (1)

If rank(B)=0, the smaller set `{0,16,32}` applies. The condition is necessary only; no row is asserted realizable. Together with `frontier-20261028-rank2-cubic-weight-gap-v1.md`, SHA-256 `0efc3ea97c00048a698c221ef494e8e6e26e3e67ebd3dad132c9ebc7fb530121`, 48 LF, the rank≤2 branch has N=256, N=224 with (1), or N≤208.

## Proof

The quartic coupling makes P a polynomial of degree≤3 when rank(B)≤2. Let h=1+P; then h also has degree≤3 and weight 32. For any shift v its derivative D_vh has degree≤2 and weight at most 64. A nonzero Boolean quadratic on eight variables has weight at least 64, so either D_vh=0 or it has weight exactly 64. In the latter case the support S of h and its translate S+v are disjoint, because `wt(D_vh)=2(32−|S∩(S+v)|)`.

The periods of h form a linear subspace R. Choose x₀∈S. Every v=x+x₀ with x∈S has `S∩(S+v)≠∅` and therefore is a period; conversely x₀+v∈S for every v∈R. Hence `S=x₀+R`, an affine five-flat of 32 points.

The odd-half Q has the same polar as q, so its restriction to the direction of S has alternating rank at most two. A quadratic on five variables with rank zero or two has weights among `{0,8,16,24,32}` by elementary quadratic normal form. Since `A₃+A₋₅=|S∩{Q=1}|`, (1) follows. At rank zero, the restriction is affine and its weight is 0,16, or 32. ∎

## Finite controls and pins

A separate control directly checked all 256 translations of an explicit affine five-flat, obtaining 32 periods and derivative weights 0 or 64, and checked all 128 affine shifts of representative rank-zero/rank-two quadratics on five variables. These checks do not replace the all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-rank2-boundary-check.py` | `a3a361c1f2cc8d92de9e7ebd985ccae14be40ffc55bfdacd9444bac9e05bc2aa` | 37 |
| `frontier-20261028-rank2-boundary-check-result.json` | `7ce041f479a3ab2d40fbda847beb812d5182319ea2c44713c9a9c655e64f5890` | 43 |
| `frontier-20261028-rank2-cubic-weight-gap-v1.md` | `0efc3ea97c00048a698c221ef494e8e6e26e3e67ebd3dad132c9ebc7fb530121` | 48 |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 |

The actual balanced witness-or-unrestricted-exclusion gap remains. **END.**
