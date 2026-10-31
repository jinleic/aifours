# info-6 frontier: rank-sensitive peak/unit bounds from symplectic slices

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T19:18:45-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. All conclusions are necessary conditions on one actual balanced Boolean function, not a witness, global exclusion, novelty or formal-verification claim.

## Statement

For any balanced f:F₂⁹→{0,1} with `max|W_f|≤28`, let q be the even-half quadratic on the eight-dimensional K, B its alternating polar, and

    N = #{a:|W_f(a)|∈{4,28}}.

The preceding quartic and simplex results imply:

1. If `rank(B)≥6`, then `32≤N≤224`.
2. If `rank(B)=8`, then in fact **N≤214**. Equivalently, if `Z+F∈{120,136}`, where Z counts Walsh zeros and F counts magnitude-16 coefficients, then N≤214 and in particular the number of magnitude-28 coefficients is ≤214.

The second bound strengthens the immediate rank-eight consequences `N≤222` and `N≡2 (mod 4)`. It does not exclude the four-zero case or the original target.

## Six-dimensional slice facts

By `frontier-20261028-quartic-energy-coupling-v1.md` (SHA-256 `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859`, 61 LF), the quartic part of `P=1_{|W|∈{4,28}}` is the Pfaffian 4-form of B. On any affine six-space whose direction is symplectic of rank six, both P and 1+P restrict to degree≤4 polynomials with the nonzero rank-six quartic form. The lemma proved in `frontier-20261028-rank6-simplex-obstruction-v1.md` (SHA-256 `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b`, 60 LF) says each such restriction has even weight at least eight. If its weight is eight, its support is a symplectic simplex.

A simplex has eight points, affine span six, and a unique affine dependence involving all eight: after translating one point to zero, its other seven difference vectors have the all-one-off-diagonal Gram matrix of rank six and their only linear dependence is their sum. Consequently **no affine 4-flat contains six of its points**.

When rank(B)≥6, choose a nondegenerate six-dimensional direction. Its four affine cosets partition K, so each of P and 1+P has at least `4·8=32` points. This proves `32≤N≤224`.

## The full-rank improvement

Suppose rank(B)=8 and write K=F₂⁶_x⊕F₂²_r in symplectic coordinates. For h=1+P, the forced degree-four part is

    ω₆(x) + r₁r₂ q₆(x),
    ω₆=x₀x₁x₂x₃+x₀x₁x₄x₅+x₂x₃x₄x₅,
    q₆=x₀x₁+x₂x₃+x₄x₅.                                                     (3)

Thus, absorbing all lower-degree terms,

    h(x,r)=H(x)+r₁A(x)+r₂B(x)+r₁r₂(q₆(x)+C(x)),
    deg A,deg B≤2,  deg C≤1.                                                 (4)

The four six-variable slices h_r each have the rank-six quartic ω₆, have even weight, and have weight at least eight. Any two slices differ by a quadratic of degree≤2.

Two weight-eight slices must be identical. Otherwise their nonzero difference has weight at least 16 by the elementary quadratic minimum-support bound and at most 16 by the two support sizes. Equality makes their supports disjoint and their union the support of a weight-16 quadratic, hence an affine 4-flat. That cannot contain either simplex, which spans six dimensions.

Similarly, a weight-eight slice S cannot coexist with a weight-10 or weight-12 slice S′. Their quadratic difference would have weight at most 18 or 20; the six-variable quadratic normal form forces it to have weight 16 and support an affine 4-flat. Its intersection with S would have size `(8+16−|S′|)/2`, namely seven or six, contradicting the simplex fact above.

The count congruence in the quartic-coupling paper gives `wt(h)=256−N≡2 (mod 4)`. Since each slice weighs at least eight, the only possible weights below 42 are 34 and 38. For 34 the slice weights are (8,8,8,10), already impossible. For 38 the possible sorted patterns are (8,8,8,14), (8,8,10,12), and (8,10,10,10); the latter two are impossible. In the remaining pattern the three weight-eight slices are the same S. The mixed radical derivative is then the quadratic difference between S and the weight-14 slice, whose weight is at most 22. But (4) makes this derivative a **rank-six quadratic** on F₂⁶, whose weight is 28 or 36. Contradiction. Therefore `wt(h)≥42`, and N≤214. ∎

The weight-16 quadratic classification used here is elementary: a nonzero six-variable quadratic has possible weights 16,24,28,32,36,40,48,64. Weight 16 arises only from rank two and is, after an affine change of coordinates, the indicator of a codimension-two affine subspace.

## Honest remaining gap and finite controls

A formal four-zero histogram still satisfies the currently listed count constraints: `Z=4`, `Z+F=112` (rank six), `wt(Q)=112`, `N=212`, and 209 peaks. Its 257 dual coefficients are nonnegative integers and were independently checked forward and backward; it is **not** a code, a placed spectrum, or a Boolean witness. Its existence as a count vector does not establish that the stronger spatial conditions are jointly realizable. The original four-zero and unrestricted problems remain unresolved by this result.

The finite support checker exhausted all 4,194,304 six-variable quadratic polynomials, verified that all 2,604 weight-16 ones are affine 4-flat indicators, and independently checked that the explicit symplectic simplex meets every affine 4-flat in at most five points. It also records a rank-six-quartic slice of weight ten, showing the proof does **not** assume weight ten is impossible in isolation.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-full-rank-support-check.py` | `dca4c0f5cd90bbc6be751a3cc3aa70dd48176141b3db183d79fece526ee1ba15` | 66 |
| `frontier-20261028-full-rank-support-check-result.json` | `fdd3f47fba59ff07501ce658eabf2be8166e6d31bf8a4e5407fadae879589280` | 40 |
| `frontier-20261028-four-zero-post-simplex.py` | `d6b44b9264a1e0714dd26c3c17f7fbfe2cc6e5cffac250a0d5b05073a63d9145` | 54 |
| `frontier-20261028-four-zero-post-simplex-result.json` | `4a3b0d9c0f4bbc8e48d030ea9936a24e202bcfd3a3f7244dab9d39d01d9c95ae` | 287 |
| `frontier-20261028-four-zero-post-simplex-check.json` | `a07c594bb72da67fcee7ef74b58e793052d5a561907107236c0dd9e640efce1c` | 19 |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 |

The finite controls are same-owner checks, not a disjoint review. **END.**
