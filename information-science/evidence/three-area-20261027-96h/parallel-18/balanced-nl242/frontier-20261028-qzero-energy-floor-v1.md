# info-6 frontier: q-zero-dependent peak floors

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:00:59-0700**. **UNREVIEWED AUTHOR CANDIDATE**. The energy bounds apply to the original Boolean object and use the parent-adopted Walsh caller/mod-4 coupling at its exact written-support scope; they are not themselves adopted, independently reviewed, novelty-checked, or formally verified. The final constant-quadratic exclusion additionally uses the unreviewed quartic caller identified below. No unrestricted resolution or witness is claimed.

## General inequality

Let f:F₂⁹→F₂ be balanced with nonzero support XOR T and `max|W_f|≤28`. Write `k=W_f/4`, let q be `k/2 mod 2` on T⊥, let z be the number of q-zeros, let Z be the number of Walsh zeros (all in T⊥), let m count agreeing unordered T-pairs, and let n₇ be the total number of magnitude-28 Walsh coefficients. Then

    M(z,Z) = 2 floor((9216−20z−16Z)/128),
    m≤M(z,Z),
    n₇ ≥ max(0, ceil((64(256−M(z,Z))−6400)/24)).              (1)

In particular Z≥1, since W_f(0)=0. The following unconditional-in-Z table uses only Z≥1:

| q-zero count z | m upper bound | n₇ lower bound |
|---:|---:|---:|
| 64 | 122 | 91 |
| 96 | 112 | 118 |
| 112 | 108 | 128 |
| 120 | 106 | 134 |
| 128 | 102 | 144 |
| 136 | 100 | 150 |
| 144 | 98 | 155 |
| 160 | 92 | 171 |
| 192 | 82 | 198 |
| 256 | 62 | 251 |

The previously parent-adopted ≥92 bound is stronger than the z=64 row. For rank eight, z is 120 or 136, hence the new floor is respectively **134 or 150**. A separate, unreviewed proof has at least ten zeros in the rank-eight branch; if one assumes Z≥10, (1) sharpens the two floors to **139 or 155**, respectively. The displayed rank-eight floors with Z≥1 do not depend on that unreviewed zero result.

## Proof

Use T as the last coordinate. The even-half k values are even, so peak≤28 gives `k∈{0,±2,±4,±6}` there. On q=0, the only nonzero values are ±4; on q=1, the values are ±2 or ±6. Thus

    Σ_{a∈T⊥}k(a)² ≤16(z−Z)+36(256−z).                            (2)

For `u(y)=((−1)^{f(y,0)}+(−1)^{f(y,1)})/2`, the even-half k is half the eight-variable Walsh transform of u; consequently the left side of (2) is 64m. Balance gives Σu=0, so m is even. This gives the first two assertions in (1).

On the other half all k are odd and have magnitude at most 7. There are 256 of them and exactly n₇ have magnitude 7; all the rest have magnitude at most 5. Their squared energy is exactly `64(256−m)`, so

    64(256−m) ≤ 49n₇+25(256−n₇).                                (3)

Combine (3) with m≤M(z,Z), solve for integer n₇, and clamp below at 0. This proves (1). The checker independently enumerates possible even m and integer peak counts in the displayed rows. ∎

## Additional constant-q obstruction, conditional on the quartic caller

If the even quadratic q is the constant zero function, then z=256. The table gives n₇≥251, so at most five odd-half positions are not peak-28. The unreviewed `quartic-energy-coupling` paper proves `h=1−P`, with `P=1_{|k|∈{1,7}}`, has degree≤4 and the odd-half Q has the same polar as q. Hence `wt(h)≤5` forces h=0 by the elementary Boolean degree-four minimum-support bound 16, and Q is affine.

In this case all odd-half k are ±1 or ±7 and at most five are ±1. The baseline `k₀=−7(−1)^Q` has an inverse coefficient of magnitude `7·256=1792`. Changing each unit position from its baseline alters that coefficient by at most 8, so the actual inverse coefficient is at least `1792−8·5=1752` in magnitude. A Boolean caller requires every odd-half inverse coefficient to be 0 or ±128. Contradiction. Thus **q cannot be identically zero**, conditional on that unreviewed quartic caller. This does not rule out a nonconstant affine q or all rank-zero polar cases. ∎

## Controls and status

A separately pinned labelled ten-zero **formal NON-WITNESS** has z=136, Z=10, even-energy m=80 and n₇=208, so it satisfies the arithmetic bounds `m≤98,n₇≥155`; it fails 502 nonzero-shift correlations and 479 inverse coordinates. It is not a Boolean counterexample and does not demonstrate feasibility of the target. The exact table checker also recomputes each bound by integer enumeration, not by solving an UNSAT model.

The 23-LF parent disposition below adopts the Walsh caller and mod-4 coupling only at same-harness written-support level; this new energy corollary and the rank-specific numbers have no adoption or disjoint review. The explicit constant-q part additionally depends on the unreviewed quartic paper.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-qzero-energy-floor-check.py` | `6d0d2e451e848e487e0b0cc1035e3638cd39624786dd49b79eccad327d6127d1` | 43 | finite integer control |
| `frontier-20261028-qzero-energy-floor-check-result.json` | `43f7d3c99a2b225453bbe3b094576c58e0e59068973abc5c60cc393da67beab7` | 74 | finite integer receipt |
| `frontier-20261028-tenzero-common-placement-result.json` | `0bd5313e99e9edf0654292a4a3e8f3b6d80b6457e35beb04791e97b26711015a` | 1570 | formal non-witness |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 | unreviewed quartic caller |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written support |

**END.**
