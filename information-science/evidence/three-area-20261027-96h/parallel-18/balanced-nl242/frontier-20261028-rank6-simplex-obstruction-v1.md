# info-6 frontier: rank-six simplex obstruction at peak/unit weight 224

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T19:00:18-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, with explicit finite incidence controls; no unrestricted exclusion, realization, novelty, human or formal verification is asserted.

## Necessary condition

For an actual balanced f:F₂⁹→{0,1} with `max|W_f|≤28`, use the even-half quadratic q, its polar B, the odd-half quadratic Q, and `P=1_{|W|∈{4,28}}` as in `frontier-20261028-even-odd-quadratic-coupling-v1.md` (SHA-256 `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f`, 63 LF). Suppose

    rank(B)=6,      wt(P)=224,      wt(Q)∈{112,144}.                       (1)

Let A_t count nonzero frequencies with `W/4=t`. Then necessarily

    A₃ + A₋₅ ≡ 4 (mod 8).                                                 (2)

Indeed A₃+A₋₅ counts odd-half positions with P=0 and Q=1. The formal four-zero histogram in `frontier-20261028-four-zero-coupled-rank-result.json` has rank-six-compatible `(z,w)=(144,144)`, wt(P)=224 and `A₃+A₋₅=16`, so it cannot be realized by an actual f. This excludes **every placement with that histogram**, not all four-zero targets.

## Reduction to four six-variable slices

The quartic coupling in `frontier-20261028-quartic-energy-coupling-v1.md` (SHA-256 `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859`, 61 LF) forces the degree-four part of P to be the Pfaffian 4-form of B. Choose symplectic coordinates x∈F₂⁶ on the rank-six part and r=(r₁,r₂)∈F₂² on the radical. Put h=1+P; it has weight 32. Its degree-four terms are exactly

    x₀x₁x₂x₃ + x₀x₁x₄x₅ + x₂x₃x₄x₅.                                      (3)

In particular there are **no** degree-four terms involving a radical coordinate. For each fixed r, h_r(x)=h(x,r) has degree≤4 and the same nonzero quartic part. The quartic coupling also says every affine 4-flat whose direction is nondegenerate for the symplectic form has odd h_r-sum.

The lemma below shows every such h_r has weight at least eight, and its weight-eight support spans the entire six-dimensional affine space. Since the four weights sum to 32, all are exactly eight. Moreover, the absence of radical degree-four terms implies that **any two slices differ by a polynomial of degree≤2**: in `h=h₀+r₁A+r₂B+r₁r₂C`, one has deg A,deg B≤2 and deg C≤1.

If two distinct slices had supports S and S′, their nonzero difference would be a degree≤2 polynomial of weight at least `2^(6−2)=16`, but `|S△S′|≤16`; hence the supports would be disjoint and their union would be a weight-16 quadratic support. By the elementary quadratic normal form, a six-variable quadratic of weight 16 is the indicator of an affine 4-flat. This is impossible because S spans the whole affine six-space. Thus all four slice supports are the **same** eight-point set S.

Q has the same rank-six polar as q. If Q had a nonzero linear term on the two-dimensional radical, its weight would be 128; the hypothesis `wt(Q)∈{112,144}` therefore makes Q independent of r. The lemma shows `Σ_{x∈S}Q(x)` is odd, so

    #{(x,r):h(x,r)=1, Q(x,r)=1} = 4·#{x∈S:Q(x)=1} ≡ 4 (mod 8).

This is exactly A₃+A₋₅, proving (2). ∎

## Lemma: a weight-eight support is a symplectic simplex

Let g:F₂⁶→F₂ have degree≤4, with the nonzero quartic form (3), and suppose every coset of every nondegenerate symplectic 4-subspace has odd g-sum. Then `wt(g)≥8`. If wt(g)=8, every three support points have nondegenerate difference span; the support affinely spans F₂⁶, its XOR is zero, and every quadratic with the same polar has odd sum on the support.

The elementary minimum-support bound gives wt(g)≥4, and wt(g) is even because deg g<6. There are 336 nondegenerate 4-subspaces L of a six-dimensional symplectic space, and each nonzero vector lies in 80 of them: L is in bijection with its nondegenerate 2-dimensional orthogonal complement, whose count is `63·32/6=336`. Transitivity on nonzero vectors follows by extending each vector and a symplectic partner to a basis.

Each L has four cosets and every coset contains an odd number of support points. For weight four the coset pattern is (1,1,1,1), giving no pair of support points with difference in L, impossible because every nonzero difference belongs to 80 such L. For weight six the pattern is (3,1,1,1), giving `3·336=1008` pair incidences, while double counting its 15 pairs gives `15·80=1200`. Thus the minimum is eight.

For weight eight the only patterns are (3,3,1,1), with six pair incidences and two triple incidences, and (5,1,1,1), with ten pair incidences and ten triple incidences. The total pair incidence is `C(8,2)·80=2240`, so exactly 280 subspaces have the first pattern and 56 the second. The triple incidence is consequently `280·2+56·10=1120`.

A triple of distinct points spans a 2-dimensional difference plane. Each nondegenerate difference plane lies in exactly 20 nondegenerate 4-subspaces, and each isotropic difference plane lies in 16. For the count: there are 336 nondegenerate and 315 isotropic 2-planes in dimension six (`63·32/6` and `63·30/6`), while a nondegenerate 4-space contains 20 and 15 respectively; double counting and symplectic transitivity give 20 and 16. Since there are C(8,3)=56 triples and `56·20=1120`, **every** triple must be nondegenerate.

Fix one support point p and let v₁,…,v₇ be the differences to the others. Their alternating Gram matrix has zero diagonal and all off-diagonal entries one; over F₂ it has rank six and kernel spanned by the all-one vector. Hence the differences span the whole six-space, their XOR is zero, and the XOR of all eight support points is zero. If Q is any quadratic with this polar, expansion of `Q(Σ_i v_i)` gives `Σ_i (Q(v_i)+Q(0))=C(7,2)≡1 (mod 2)`; the common translation p and Q's affine part contribute zero over all eight points. Thus Σ_S Q is odd. ∎

## Finite controls and pins

The independent finite checker enumerated all 336 nondegenerate 4-subspaces, confirmed the 80/20/16 incidence constants and the 280/56 pattern split on an explicit eight-point simplex, verified its six-dimensional span and quartic ANF, and checked odd Q-sum for all 128 affine shifts of one rank-six quadratic. These checks supplement the all-variable incidence proof; they are not a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-symplectic-simplex-check.py` | `52713e4b8c49af8fba84b23f1ff947ddb763d82fdce3faae7ce043c10d9b26b5` | 91 |
| `frontier-20261028-symplectic-simplex-check-result.json` | `1584d94a77cdf53bf7bd68dc92cfe5ea1392d1ecfe225fa4185bda06b989015c` | 38 |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 |
| `frontier-20261028-four-zero-coupled-rank-result.json` | `0a4ebd458300628a6962b6038b91172ddf5aa27dbc2c2075a9702b165bc07406` | 285 |

No unrestricted no-go or actual balanced NL242 witness follows. **END.**
