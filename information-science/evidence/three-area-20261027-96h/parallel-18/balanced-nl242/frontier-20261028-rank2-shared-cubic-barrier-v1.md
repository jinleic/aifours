# info-6 frontier: a shared-cubic rank-two barrier and Q-weight correction

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T02:58:09-0700**. The 512-integer object below is a formal **NON-WITNESS**, not an actual Boolean function, code, unrestricted exclusion or novelty claim. Its finite checks are same-owner, not disjoint review. The correction is additive; all pinned earlier files remain unchanged.

## Mandatory correction: odd quadratic weights

The unreviewed D28 profile packet `frontier-20261028-rank2-D28-profile-v1.md` SHA256 `c0a9de1ca74f7ecd8ced70d5cb45115563e1f6cca20efc07c7c77364595d48bc`, 35 LF, incorrectly says the odd rank-two Q has weight only 64 or 128. With fixed rank-two polar its correct possible weights are **64, 128 or 192**: a nonzero radical linear term gives 128; a zero radical term gives either 64 or 192 according to the quotient quadratic and constant. The unreviewed packet's Q-weight enumeration and its `frontier-20261028-rank2-D28-profile-check.py` and result are **INCOMPLETE/NONINPUT**. They must not be used to exclude or cover the omitted weight-192 case. Its algebraic D28 endpoint formula in the separate D28 placement packet does not depend on this list. This correction does not adopt that endpoint or any other theorem.

The earlier cubic weight-divisibility withdrawal `frontier-20261028-cubic-divisibility-withdrawal-v1.md` remains mandatory; its three withdrawn candidates stay noninput. The corrected lowrank profile, corrected parity and common-cubic candidates remain author-only.

## One labelled D12 shared-cubic object

The pinned receipt gives all 512 integers `k(a)` with frequency coordinates split into an even and odd half. The object simultaneously satisfies the following **listed filters**:

* `k(0)=0`, `max|k|=7`, `Σk=128`, `Σk²=16384`; even and odd first sums are 0 and 128.
* Its even q has rank-two polar and exactly 64 zeros; exactly eight actual k zeros form a 3-plane. Its even mod8 correction is cubic. The odd Q has the **same** rank-two polar and weight **192**; its indicator `h=1_{|k|∈{3,5}}` is a single global cubic.
* The odd absolute counts are `(n₁,n₃,n₅,n₇)=(2,10,134,110)`, so D=12 and even energy is `64·118`. Even `E₂=8`, and the parent-adopted congruence `E₂+2n₃≡0 mod4` holds.
* All four odd inverse coefficients on the Q Walsh-support plane are exactly +128. All 257 formal Krawtchouk dual counts are nonnegative integers. These conditions are **not** a code-realization or Boolean-caller proof.

For reproducibility, the constructor uses the three even-cubic affine masks `(28,62,52)` and four odd-cubic 64-bit slice masks recorded in its receipt; all choices are deterministic. The separate dual checker uses the three-term integer Krawtchouk recurrence, and the independent placement audit computes a direct 512×512 inverse, cross-checks all shifts via the squared-FWHT identity, and verifies every q/Q second derivative and both cubic ANFs.

The exact failure is decisive for this one placement: **483/512** full inverse entries are not ±128, and **506/511** nonzero-shift autocorrelations are nonzero, with maximum absolute correlation 5760. The first audit draft contained an FWHT assignment typo and failed against the direct transform; it was corrected before the pinned successful run, with no output receipt produced by the failed run. No false result was accepted.

Thus common even and odd cubic structure, same polar, scalar/dual feasibility and the four quadratic-support inverses can coexist in a labelled spectrum while the full original caller fails. The object does **not** exclude any other placement with the same counts, prove rank-two existence, or settle the original target. Every rank remains open at its exact parent-adopted/author-only boundary.

## Pins

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-shared-cubic-placement.py` | `177478be8838c25a82208916575bdee35b935fd97edf84c8fe72459c6d2d59fb` | 73 | deterministic formal placement |
| `frontier-20261028-rank2-shared-cubic-placement-result.json` | `7581458a93462f424a4c6f77f468c1b43c84fedce63399790be0df474692400f` | 562 | full labelled NON-WITNESS |
| `frontier-20261028-rank2-shared-cubic-audit.py` | `795abda3f6943588a55e5c8bde558918556beba167a99114d36b639c5e22814b` | 59 | independent transform/polar audit |
| `frontier-20261028-rank2-shared-cubic-audit-result.json` | `d92fec51e10142482122e4eb093d294943a199a9081e6323aabfccf04a02bf86` | 12 | independent receipt |
| `frontier-20261028-rank2-shared-cubic-dual-audit.py` | `1ab247fdfacfbc912180d372159a14458e621a34e473c34d73d7160e808065b0` | 34 | dual recurrence checker |
| `frontier-20261028-rank2-shared-cubic-dual-audit-result.json` | `c28d58ed9c3e636a02ec3745193e9e624651712b266e5d67307408101e5edf9b` | 278 | 257 dual counts |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | unreviewed profile predecessor |
| `frontier-20261028-cubic-common-top-v1.md` | `fdb93f48b8c788b719e6d753a682c567f1c76430c879b95f7cfb2edef8e1005e` | 47 | unreviewed corrected cubic predecessor |

**END.**
