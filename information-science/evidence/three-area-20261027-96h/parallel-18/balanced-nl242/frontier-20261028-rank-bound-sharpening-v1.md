# info-6 frontier: a sharper full-rank bound and rank-six boundary

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T19:26:58-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, additive to immutable `frontier-20261028-full-rank-peakunit-bound-v1.md` (SHA-256 `3c7473f24a24efdbe0cbf9bfed074b4ee026e611e35f5df6dcc14e0412fce35d`, 64 LF). No frozen review is amended and no unrestricted no-go or witness is claimed.

## Necessary conditions

For any actual balanced f:F₂⁹→{0,1} with full Walsh peak≤28, use the preceding even-half polar B, odd-half quadratic Q, `P=1_{|W|∈{4,28}}`, and `N=wt(P)`. Then:

1. If `rank(B)=8`, **N≤210**. Thus for `Z+F∈{120,136}` the number of |W|=28 coefficients is also at most 210.
2. If `rank(B)=6`, then N≤224 as before, but **N≠220**. At N=216, writing A_t for nonzero-frequency `W/4=t`, one additionally has `A₃+A₋₅≡4 (mod 8)` when `wt(Q)∈{112,144}`, and `A₃+A₋₅=20` when `wt(Q)=128`.

These are branch-conditional necessary filters. The formal four-zero count model with rank six and N=212 from the predecessor remains outside both boundary cases and is not resolved here.

## A ten-point slice lemma

On a six-dimensional symplectic space, consider a Boolean polynomial g of degree≤4 whose quartic part is the rank-six Pfaffian form `ω₆=x₀x₁x₂x₃+x₀x₁x₄x₅+x₂x₃x₄x₅`. If wt(g)=10, **no affine 4-flat contains eight points of its support**. Also, every quadratic Q with the same polar has odd sum on that support.

To prove this, let S be the support. Since deg g≤4<6, both `|S|` and the XOR of S are zero modulo two. For distinct i,j, the parity `Σ_{x∈S}x_i x_j` is the coefficient of the complementary four-variable monomial of g: summing a Boolean polynomial over F₂⁶ retains only its full-degree coefficient. Consequently the symmetric matrix `M=Σ_{x∈S}xxᵀ` is the standard nondegenerate rank-six symplectic matrix (its diagonal is zero). Because |S| is even and ⊕S=0, M is unchanged by translating S.

Suppose an affine 4-flat contains at least eight points of S, and translate it to a linear 4-space U. If no point lies outside U, the support spans at most four dimensions. One outside point is impossible because the support XOR is zero. With exactly two outside points a,b, their XOR belongs to U, so all ten points lie in the at-most-five-dimensional span of U and a. In every case rank M≤5, a contradiction.

For the last assertion, `Σ_S Q = Σ_x g(x)Q(x) (mod 2)` is the full-degree coefficient of gQ. Only the quartic terms of g and the quadratic terms of Q can cover all six variables. Their three complementary symplectic pairings contribute `1+1+1=1` modulo two; lower terms and Q's affine part cannot contribute. ∎

## Rank-six boundary

The rank-six simplex proof in `frontier-20261028-rank6-simplex-obstruction-v1.md` (SHA-256 `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b`, 60 LF) partitions h=1+P into four six-variable slices along the two-dimensional radical. Each slice has the quartic form ω₆, even weight at least eight, and any two slice differences have degree≤2. Weight-eight supports are symplectic simplexes; two such slices must be identical, and a weight-eight slice cannot coexist with one of weight 10 or 12, by the quadratic-weight/affine-flat argument in the pinned full-rank predecessor.

The count congruence gives `wt(h)≡0 (mod 4)`. If wt(h)=36, its only sorted slice patterns are (8,8,8,12) and (8,8,10,10), both impossible. Hence N=220 is impossible.

If wt(h)=40, the sorted patterns are (8,8,8,16), (8,8,10,14), (8,8,12,12), (8,10,10,12), and (10,10,10,10). The middle three are impossible. In the first, the three weight-eight slices coincide and the fourth differs from them by the mixed radical derivative, an affine polynomial. Its support would have size at most 24, but a nonzero affine polynomial on six variables has weight 32 or 64, so it must vanish, contradiction.

In the last pattern, any two distinct weight-ten slices differ by a nonzero quadratic of weight at most 20, hence by a weight-16 quadratic supported on an affine 4-flat. That flat would contain `(10+16−10)/2=8` points of the first support, contradicting the lemma. Thus all four slices are the same S of weight ten.

If Q is nonbalanced, its polar has rank six and it is independent of the radical, so the lemma gives `#{P=0,Q=1}=4·odd≡4 (mod 8)`. If Q is balanced, its radical linear term is nonzero and exactly two of the four radical points above each of the ten x belong to Q, giving 20. These counts equal A₃+A₋₅. ∎

## Sharpening the rank-eight case

In the full-rank proof of the pinned predecessor, the four six-variable slice weights of h=1+P are even and at least eight; any two slices differ by a quadratic, while their mixed radical derivative is a **rank-six quadratic**, of weight 28 or 36. Weight-eight slices are identical to one another and cannot coexist with weight 10 or 12. In addition, by the lemma just proved, any two weight-ten slices must be identical: a distinct pair would differ by a weight-16 affine-4-flat indicator containing eight support points.

The predecessor already excludes wt(h)=34 and 38. At wt(h)=42 the sorted possibilities are

    (8,8,8,18), (8,8,10,16), (8,8,12,14),
    (8,10,10,14), (8,10,12,12), (10,10,10,12).

All middle cases contain an incompatible 8/10 or 8/12 pair. In the first, the three weight-eight slices are identical, so the mixed derivative is their difference from the weight-18 slice and has weight at most 26, less than 28. In the last, the three weight-ten slices are identical, so the mixed derivative has weight at most 22. Both contradict rank six. Since `wt(h)≡2 (mod 4)` and the predecessor gives wt(h)≥42, now `wt(h)≥46` and N≤210. ∎

The bound N=210 is attained by an explicit degree-four P with the forced full-rank quartic part: take a six-variable symplectic simplex S, a rank-six quadratic Q₆ of weight 28 with seven ones on S, and let the four slices of h be S,S,S,S△Q₆. Their weights are 8,8,8,22. This shows sharpness **only for the isolated quartic-coupling filter**, not for the full Walsh problem or for a Boolean f.

## Finite controls and pins

The separate control enumerates all 2,604 affine 4-flats in F₂⁶, checks the explicit simplex has maximum intersection five and an explicit weight-ten rank-six slice has maximum intersection seven, checks the odd Q-sum for all 128 affine shifts, and constructs the stated N=210 quartic-only example. The all-4,194,304 quadratic weight check is pinned in the predecessor. These controls do not replace this written proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-rank-bounds-sharpness-check.py` | `b88377492218dd6eb3f03111f07358899ba476beea2202a72c0a20ef278fdbc0` | 70 |
| `frontier-20261028-rank-bounds-sharpness-check-result.json` | `84a96cd321cbfee193d2ebd81eb375b9336025a7c1cd811b028a5d675b20594d` | 18 |
| `frontier-20261028-full-rank-peakunit-bound-v1.md` | `3c7473f24a24efdbe0cbf9bfed074b4ee026e611e35f5df6dcc14e0412fce35d` | 64 |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 |

The actual balanced witness-or-unrestricted-exclusion gap remains. **END.**
