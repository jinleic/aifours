# info-6 frontier: the two radical phases cannot both vanish

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T21:19:01-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. The proof below is written, with finite inequality controls; it is not a formal/kernel or disjoint-review acceptance and does not exclude all four-zero targets.

## Statement

For any actual balanced f:F₂⁹→{0,1} with Walsh peak≤28 and exactly four Walsh zeros, the preceding all-variable reduction makes the zero plane R the rank-six even-half polar radical. Let λ:R→F₂ be the mod-8 radical functional from `frontier-20261028-radical-fiber-autocorrelation-v1.md`, SHA-256 `7fef5e3cec28f32fe824f742ccdf1124b6b2019527e671e14ba9f4eee15a3260`, 56 LF, and let ρ:R→F₂ be the radical linear part of the odd-half quadratic Q. Then

> **λ and ρ cannot both be zero.**

Equivalently, if Q is nonbalanced (weight 112 or 144), its radical part ρ is zero and λ must be nonzero. Hence, writing `z=#{q=0}` and `m=A₋₂+A₆`, one has `m=72` when z=112 and `m=56` when z=144. Conversely, a noncentral m forces Q to be balanced of weight 128. This is a proper four-zero necessary condition, not an exclusion of all four-zero targets.

## Three pointwise four-entry inequalities

Partition K and the odd half into the 128 cosets F of the zero plane R; each F contains four scaled Walsh coefficients. Define

    E_F = Σ_{a∈F} k(a)²,       S_F = Σ_{a∈F} k(a).

Suppose λ=ρ=0. On an even q-zero nonradical fiber every k is ±4, and `E_F=64`; hence `S_F²≥10E_F−640`. On an even q-one fiber k mod8 is constant by λ=0, so its four values are either all in `{−6,2}` or all in `{−2,6}`. If n of the first type equal −6, then `E_F=16+32n`, `S_F²=(8−8n)²`, and

    S_F²−10E_F+864 = 64(n−3)(n−4) ≥ 0.                                      (2)

The sign-reversed class has the same squares and satisfies the same inequality.

On an odd fiber Q is constant because ρ=0. Its four k values are either in `{−7,−3,1,5}` or in the negative set `{−5,−1,3,7}`. In both cases

    S_F² ≥ 10E_F−1464.                                                       (3)

For a short proof, maximize `10Σx_i²−(Σx_i)²` over the cube [−7,5]⁴. It is convex in each coordinate, so a maximum occurs at a vertex. If n coordinates are −7 and 4−n are 5, the value is `600+720n−144n²`, whose maximum for n=0,…,4 is 1,464. Negating all entries leaves E_F and S_F² unchanged.

## Summing to a contradiction

The radical fiber itself has k=0. Put `z=#{q=0}` on K. Rank six and q|R=0 give z∈{112,144}; there are `(z−4)/4` nonradical q-zero fibers, `(256−z)/4` q-one fibers and 64 odd fibers. Parseval gives `Σ_F E_F=2¹⁴=16,384`. Summing (2)–(3) and the q-zero inequality gives

    Σ_F S_F² ≥ 10·16,384 − 640(z−4)/4 − 864(256−z)/4 − 1464·64
              = 16,384 + 56(z−16).                                          (4)

However, the exact Boolean autocorrelation caller gives `R(0)=16,384` and R(r)=0 for every nonzero r∈R, while

    Σ_F S_F² = Σ_{r∈R} R(r) = 16,384.

Equation (4) is larger by 5,376 for z=112 and by 7,168 for z=144. This contradiction proves that λ and ρ cannot both vanish. The phase/count consequence follows from the earlier λ-fiber theorem and the rank-six quadratic normal form. ∎

This proof does **not** rely on the exploratory integer solver's UNSAT result or on the computer-assisted residue-count census. The three pointwise inequalities and the sum-of-squares identity are sufficient.

## Finite controls and pins

A separate script checks every unordered four-entry multiset in the three classes, confirms the optimal constants, and verifies that reducing any constant by one fails an equality example. It also checks both exact aggregate gaps. These finite checks do not replace the written proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-fiber-energy-inequality-check.py` | `8e8fd623a43d4c14917fbe696f0133530701defb175393545eb279d63602f96f` | 40 |
| `frontier-20261028-fiber-energy-inequality-check-result.json` | `225e29fcdc194403097bbd5b7bcfefe487dc58575dfdcfed0fff9e8d7233a82a` | 91 |
| `frontier-20261028-radical-fiber-autocorrelation-v1.md` | `7fef5e3cec28f32fe824f742ccdf1124b6b2019527e671e14ba9f4eee15a3260` | 56 |
| `frontier-20261028-four-zero-rank6-only-v1.md` | `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37` | 43 |

The rank-six four-zero branch and original unrestricted witness-or-exclusion problem remain open in this work. **END.**
