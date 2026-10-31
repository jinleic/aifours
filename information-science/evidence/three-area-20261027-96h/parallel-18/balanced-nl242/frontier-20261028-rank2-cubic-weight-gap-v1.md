# info-6 frontier: a cubic weight gap in the rank-at-most-two branch

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T19:54:42-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, not a general four-zero exclusion, witness, novelty or formal-verification claim.

## Statement

For any actual balanced f:F₂⁹→{0,1} with full Walsh peak≤28, let B be the even-half quadratic polar and let `N=#{a:|W_f(a)|∈{4,28}}`. If `rank(B)≤2`, then

    N=256,  or  N=224,  or  N≤208.                                          (1)

In particular N=212 is impossible in this branch. The formal count model `frontier-20261028-four-zero-post212-result.json`, SHA-256 `d94fb7aa244f07aa9dd3ceefe30d79314aaad72aeab76fc0aae3b36151ce6178`, 287 LF, has Z=4, Z+F=192 (which forces rank two), and N=212. Hence no placement of that histogram can satisfy the actual Boolean caller. Other four-zero histograms remain open.

## Cubic support lemma

Every Boolean polynomial p:F₂⁸→F₂ of degree at most three has weight 0, weight 32, or weight at least 48. The minimum-support bound `2^(8−3)=32` for a nonzero degree≤3 polynomial follows by the induction written in `frontier-20261028-even-half-four-zero-obstruction-v1.md`, SHA-256 `7344078fb115eb47f9d5e3c731a63d16567cb09d23af4868810c5d45ef38f8c4`, 59 LF.

Its weight is divisible by four. Indeed express p as an XOR of Boolean monomials and expand that XOR as an integer sum. A single degree≤3 monomial has weight divisible by 32; a product of two such monomials has support size divisible by 4 and coefficient −2; and every term involving three or more monomials has coefficient divisible by 4. Thus a hypothetical nonzero weight strictly between 32 and 48 is 36, 40, or 44.

Let S be the support, w one of those three values, and `R(v)=|S∩(S+v)|`. Every additive derivative `D_v p` has degree≤2 and weight `2(w−R(v))≤2w<96`. The quadratic normal form in eight variables has nonzero weights only in

    {64,96,112,120,128,136,144,160,192,256}.

Therefore each nonzero derivative has weight exactly 64, while a zero derivative means v is a period. The periods form a linear subspace of size 2^s, including zero. Thus `R(v)=w` at its `2^s−1` nonzero members and `R(v)=w−32` at the other `256−2^s` shifts. Double-counting ordered pairs of distinct points of S yields

    w(w−1) = (2^s−1)w + (256−2^s)(w−32),
    w(256−w) = 32(256−2^s).                                                 (2)

For w=36 the left side 7,920 is not divisible by 32. For w=40 or 44 it exceeds 8,192, while the right side is at most 8,192. Thus all three weights are impossible. This proves the cubic support lemma. ∎

The thresholds are sharp for arbitrary cubic functions: `x₀x₁x₂` has weight 32 and `x₀(x₁x₂+x₃x₄)` has weight 48. These are degree-only examples, not actual Walsh peak/unit indicators.

## Application

The quartic coupling `frontier-20261028-quartic-energy-coupling-v1.md`, SHA-256 `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859`, 61 LF, proves that P has degree≤4 with quartic part the Pfaffian 4-form of B. At rank≤2 this 4-form vanishes, so P and h=1+P have degree≤3. Apply the lemma to wt(h)=256−N: wt(h)=0 gives N=256; wt(h)=32 gives N=224; and wt(h)≥48 gives N≤208. This proves (1). ∎

## Finite controls and pins

The finite control checks all 2,560 canonical quadratic-rank/affine-shift representatives in dimension eight against the stated weight set, verifies the explicit weights 32 and 48, and evaluates the period equation for 36, 40, and 44 without applying the strict argument at weight 48. These checks supplement the written proof; disjoint review remains necessary.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-cubic-weight-gap-check.py` | `d37375e715625db92adfaa4bd16b1964363cbb74456d81330345a995d0a64136` | 41 |
| `frontier-20261028-cubic-weight-gap-check-result.json` | `728a7cb4a2cb0ddee7cf36f5a2b01a97bdb90d52171e8cb4ce75001c5c22aec7` | 59 |
| `frontier-20261028-four-zero-post212.py` | `03742468aeba1e2b32f0c6ae0c82c2e1d11e0a1aa4ec612a61d714e72a007a55` | 64 |
| `frontier-20261028-four-zero-post212-result.json` | `d94fb7aa244f07aa9dd3ceefe30d79314aaad72aeab76fc0aae3b36151ce6178` | 287 |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 |

The actual balanced witness-or-unrestricted-exclusion problem remains unresolved by this result. **END.**
