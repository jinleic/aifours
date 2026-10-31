# info-6 frontier: a labeled quotient relaxation and its next failures

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T21:41:57-0700 PDT**. This is a **formal labeled spectrum**, not an actual Boolean function or target witness. It is additive to, and does not amend, `frontier-20261028-fourzero-phase-consolidated-v1.md`, SHA-256 `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a`, 154 LF. No unrestricted conclusion or novelty is claimed.

## What is actually placed

Starting from the previously checked normalized formal fiber multiset `frontier-20261028-four-zero-directed-10.json`, this construction assigns every tuple to an actual frequency in one common F₂⁷ quotient and R=span(64,128). It uses the nondegenerate minus-Arf quadratic

    q(x)=x₀x₁+x₂x₃+x₄x₅+x₀+x₁,          x∈F₂⁶,

on the even quotient, the same q as the odd quadratic Q, `λ(r)=r₁`, and `ρ=0`. The four formal zero frequencies are exactly R. The construction also solves the complete even-half cubic mod-8 equation `k/2≡g₀+2h (mod4)` and aligns each nonzero-q fiber with one common degree≤3 h; this is more than the earlier **unlabeled** tuple multiset.

The labeled k has the original formal histogram, k(0)=0, |k|≤7, `Σk=128`, `Σk²=16,384`, and `C(r)=0` for all three nonzero r∈R. The separately pinned earlier dual checker confirms the histogram's 257 nonnegative integral dual coefficients. These facts do not imply that the array is a Walsh transform.

## Exact next failures

The independent direct checker finds that this particular assignment **fails** stronger required conditions:

- The odd peak/unit indicator P has algebraic degree **7**, whereas the written quartic-coupling candidate requires degree≤4 with a prescribed quartic part. No claim is made that every rearrangement of the same tuples fails this condition.
- Of the **508** nonzero shifts outside R, its full direct autocorrelation fails at **506**. The other two happen to vanish; satisfying three radical directions alone is not enough.
- Its direct 512×512 inverse has **481** entries of magnitude different from 128. It therefore cannot be a Boolean sign table and is not a target witness.

The independent checker reconstructs the full histogram, common q and Q, the even-half h by Möbius inversion, the λ/ρ relations and all 512 autocorrelations; it also rejects a deliberately changed Q value. The scalar model remains a relaxation, and no actual frequency-labeling satisfying the missing conditions is claimed.

## Pinned evidence

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-fourzero-quotient-placement.py` | `7770a243f8986d94ae4463d948e3ed7df2475d8499c0347edf521c7071561f41` | 106 |
| `frontier-20261028-fourzero-quotient-placement-result.json` | `102a6b2e6b97a21e6619f1b0075b8eda943499edd236530f1d3c518c471fe3f5` | 545 |
| `frontier-20261028-fourzero-quotient-check.py` | `6814bf075780cfc3cd0eac66103eb0f4e4a34f4259e2e0bc2e492b4de2f9ef74` | 60 |
| `frontier-20261028-fourzero-quotient-check-result.json` | `b68a7d3a4fe357f8b91d4b769640135685db5e44033675a0d45b3e9e2d02f210` | 22 |
| `frontier-20261028-four-zero-directed-10.json` | `0557b2b6fc27994c3169b5387f9243c29e54b420e9c9c7dc3eab15a56bb9338c` | 516 |
| `frontier-20261028-four-zero-directed-10-dual.json` | `2008329bb49d6d6c1da7bae9ab6b8394f24337ba9a1ad96363033c98f556f2ad` | 19 |

All controls are same-owner computations, not disjoint review. The four-zero and unrestricted target questions remain open in this work. **END.**
