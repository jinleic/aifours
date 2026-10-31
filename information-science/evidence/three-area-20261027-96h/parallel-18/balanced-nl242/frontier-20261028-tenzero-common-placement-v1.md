# info-6 frontier: ten-zero common-placement barrier, not a witness

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:23:16-0700**. This is an **explicit formal NON-WITNESS** and an unreviewed same-owner finite check, not an actual Boolean f, a ten-zero no-go, a solver certificate of impossibility, a novelty claim, or a disjoint review.

## Exact object and filters

The pinned placement JSON contains all 512 labelled integers `k(a)` for `a∈F₂⁹`, with `T=256` and `T⊥={0,…,255}`. The 10 zero coordinates are

    {0,64,128,193,194,199,203,223,239,255}.

The same labelled object has `k(0)=0`, `max|k|=7`, `Σk=128`, and `Σk²=16384`. Its even-half function `g(a)=k(a)/2 mod 4` has `g mod 2` a rank-eight quadratic q; the degree≤3 correction to the explicit integer quadratic lift is checked at every one of its 256 positions. On the odd half, `Q=1_{k≡3 mod 4}` is another quadratic with the **same** rank-eight polar. Also `P=1_{|k|∈{1,7}}` has weight 210 and its degree-four part is the Pfaffian four-form of that polar; `wt(Q)=136` and `wt((1+P)Q)=24`. This last pair satisfies the unreviewed extremal phase filter, rather than the excluded earlier scalar vector with intersection 22.

The nonzero-frequency count vector is

| k | −7 | −6 | −5 | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 97 | 60 | 19 | 25 | 0 | 38 | 1 | 9 | 1 | 0 | 5 | 101 | 22 | 22 | 111 |

There are 208 values of magnitude 7. The separately replayed Krawtchouk recurrence checks all 257 corresponding formal dual counts are nonnegative integers. The scalar count solver is used only to produce this SAT count vector; its existence is directly checked and does not certify a binary code or a Boolean function.

The construction is deterministic. Its even residues use the explicit cubic lift and ten-point set in `frontier-20261028-tenzero-mod8-lift-check.py`. On the odd half, the 46-point support of `1+P` is the first explicit representative in the pinned extremal-phase packet; `Q=q₈+x₀+1`. Each residue/phase class is filled in ascending coordinate order according to the table. Thus the even q, even cubic lift, odd Q, odd quartic P, scalar counts and ten zeros coexist **in one labelled spectrum**, not merely in separate count vectors.

## First failing target constraint and cross-check

For a true Walsh spectrum with `W=4k`, the unnormalized inverse character sum of k must be ±128 at every point; equivalently all 511 nonzero-shift autocorrelations `C(s)=Σ_a k(a)k(a+s)` must vanish. This formal spectrum fails both tests:

* `C(1)=−2272`; every one of the 255 nonzero shifts within T⊥ fails, and 247 of 256 shifts in the other coset fail: **502/511** nonzero-shift failures.
* The inverse sum at coordinate 1 is 0, not ±128; **479/512** inverse coordinates fail. The inverse range is [−480,592].
* The two independently implemented paths agree: the constructor computes all 511 correlations and all 512 inverse sums by direct character sums; the separate auditor uses an FWHT and the squared-transform identity for correlations, and independently recomputes the quadratic, cubic and quartic algebraic normal forms.

These failures are properties of this one deterministic placement only. They do **not** rule out a different placement, ten-zero target, or unrestricted target. They locate the next real gap: jointly satisfying the 511 nonzero-shift correlations/equivalently Boolean inverse, with the original rank-eight local and phase constraints. No claim is made that every earlier candidate theorem in the field has been imposed on this placement.

## Pins

| File in this directory | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-tenzero-phase-counts.py` | `a853a64258c18d9cb999188b256f4f5e51e78dd51ecc73cfe2458d9faaffacf6` | 46 |
| `frontier-20261028-tenzero-phase-counts-result.json` | `d56afe8b322880dcd75966a8a003157b6aaa67c3876538091f42e67b94137710` | 288 |
| `frontier-20261028-tenzero-mod8-lift-check.py` | `90f0c82cccc4fd0df5c595b031cdb17a1054b033feb13ba7dc3c5b1b578bd45d` | 56 |
| `frontier-20261028-tenzero-phase-lift-check-result.json` | `1974da6b611c3a5b0691d9948f7f9981f9a447e0752c677cbdfc706869d56eb0` | 36 |
| `frontier-20261028-tenzero-common-placement.py` | `ba9d6fae5b53e9943ce7f8ef6c0e5d04e132ecb84e8d738c6aebeebc6e08c587` | 81 |
| `frontier-20261028-tenzero-common-placement-result.json` | `0bd5313e99e9edf0654292a4a3e8f3b6d80b6457e35beb04791e97b26711015a` | 1570 |
| `frontier-20261028-tenzero-common-audit.py` | `1497b73e33d9218533a706ef2cc4a2de9b596dac6372e2f410a0b47d86b33245` | 65 |
| `frontier-20261028-tenzero-common-audit-result.json` | `3a08410aefb8500c1e09a9a04bb63189f7e4c54a2dec29708d39b770fd3ca309` | 14 |
| `frontier-20261028-fullrank-extremal-phase-v1.md` | `e12b3a32a3f7f19b9dea35615bbf4c8fbd6ba970d1491ca33f3fc8f4bacc6fd4` | 100 |

**END.**
