# info-6 frontier: sextic zero-indicator structure at eight points

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T22:08:03-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. It is independent of the pending four-zero kernel-pair exclusion and does not assert that any zero configuration is realizable by a Boolean target.

## Statement

For any balanced f:F₂⁹→{0,1} with nonzero one-support XOR T, write k=W_f/4, K=T^⊥, q=k/2 mod2 on K, B its polar, `Z₈={a∈K:k(a)≡0 mod8}`, and R=rad(B). Then:

- If rank(B)=8, **|Z₈|≥10**.
- If rank(B)=6, |Z₈|=6 is impossible. If |Z₈|=8, its indicator has a **nonzero period in R**.
- If rank(B)≤4 and |Z₈|=8, Z₈ is a linear 3-plane.

For a balanced peak≤28 target, T≠0 and Z₈ is its Walsh-zero set. Hence an eight-Walsh-zero target cannot have rank eight; at rank six its zero set must have a nonzero radical period; at rank≤4 it must be a linear 3-plane. These are necessary conditions, not a construction or an exclusion of all eight-zero targets.

## Sixth derivatives from the energy caller

The f131 mixed-energy identity, also reconstructed in `frontier-20261028-four-zero-radical-reduction-v1.md` (SHA-256 `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229`, 63 LF), says that on the cosets of every five-dimensional L≤K,

    |(a+L)∩Z₈| + wt(q|_{a+L})/4   is constant modulo 2.                    (1)

If rank(B|L)≤2, the quadratic weight quotient is even. If it has rank four and radical generator r, the quotient is `1+q(r)+B(a,r)`. Let M be any six-dimensional subspace of K and L a hyperplane of M. Differentiating (1) once in a direction m∈M\L yields

    D_M 1_{Z₈} = [rank(B|L)=4]·B(m,r).                                     (2)

The right side is 1 exactly when rank(B|M)=6. Indeed, if B|M is nondegenerate, every hyperplane has rank four and its radical r pairs nontrivially with m. Conversely, if rank(B|M)≤4, a rank-four L with B(m,r)=1 would add a further hyperbolic pair and make rank(B|M)=6. Thus every sixth derivative is the nondegeneracy indicator of the restricted polar.

The predecessor proves `deg 1_{Z₈}≤6`. In symplectic coordinates, (2) fixes its complete sextic ANF part to the Pfaffian 6-form: the sum of the products of any three symplectic coordinate pairs. For rank eight, splitting coordinates into x∈F₂⁶ and r=(r₁,r₂)∈F₂², this is

    x₀x₁x₂x₃x₄x₅ + r₁r₂ ω₄(x),
    ω₄=x₀x₁x₂x₃+x₀x₁x₄x₅+x₂x₃x₄x₅.                                         (3)

For rank six the same first monomial is the entire sextic part and r are radical coordinates. Each fixed-r six-variable slice therefore has odd weight, because its full six-variable ANF coefficient is one. Any two slices differ by degree at most four, since no sextic term contains exactly one r coordinate.

## Rank-eight exclusion at weights four, six and eight

The difference of two distinct singleton slices would have weight two, below the minimum weight `2^(6−4)=4` for a nonzero degree≤4 function; hence all singleton slices are identical. For rank eight, the mixed r-coordinate derivative has degree≤4 and quartic part ω₄. The rank-six symplectic lemma in `frontier-20261028-rank6-simplex-obstruction-v1.md`, SHA-256 `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b`, 60 LF, makes its weight at least eight. For completeness, its elementary incidence proof uses 336 nondegenerate 4-subspaces of a six-dimensional symplectic space, 80 through each nonzero vector: a weight-four support would give zero pair incidences per four cosets, and weight six would give 1,008 instead of the required 1,200.

Since all four slice weights are odd, total weight four gives (1,1,1,1), and total six gives (1,1,1,3). In either case the mixed derivative is zero or has weight at most four, impossible. Total eight has sorted slice weights either (1,1,1,5) or (1,1,3,3). The first has three identical singleton slices, leaving a mixed derivative of weight at most six; in the second the two singleton slices coincide, leaving the difference of the two weight-three slices, also of weight at most six. Both contradict the lower bound eight. The zero indicator has degree≤6<8, so its weight is even; it is nonempty because 0∈Z₈. Therefore rank eight forces |Z₈|≥10.

## Rank-six equality shape

For rank six the mixed radical derivative has degree≤3, since the sextic part has **no** radical coordinate; its nonzero weight is at least `2^(6−3)=8`. The same odd-slice argument excludes total weight six. At total weight eight, pattern (1,1,1,5) is impossible. For pattern (1,1,3,3), the singleton slices coincide and the two weight-three slices must also coincide, otherwise their mixed derivative would have weight at most six.

Let S be the singleton and T the common three-point support. Their difference is a nonzero degree≤4 six-variable polynomial of weight at most four, hence exactly four: S and T are disjoint. Its four-point support is an affine 2-plane by the usual minimum-support equality argument: any difference of two support points produces a derivative of degree≤3 and overlapping support of weight less than eight, hence a zero derivative. The two singleton radical labels differ by one nonzero r∈R, and the other two labels differ by that same r, so Z₈ is r-periodic. This proves the rank-six eight-point assertion.

At rank≤4, f131 gives deg `1_{Z₈}≤5`; if its weight is eight, the same equality/period argument makes its support an affine 3-plane, linear because it contains zero. ∎

## Limits and finite controls

A formal rank-six q/Z parity model with eight points, a nonzero radical period and a **nonplanar** zero set satisfies all 43,180 affine-six-flat H2 checks; it is **not** an actual Boolean function or Walsh witness. The separate checker also exhausts all 10,795 six-spaces and 43,180 affine six-flats for canonical rank-six and rank-eight sextic Pfaffian controls and rejects a sextic mutation. These controls do not replace the written all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-eightzero-sextic-check.py` | `b3b7002566026408dfea095ac5e78c2fd63ccbd2605c8b9e22ace0ec4547638c` | 67 |
| `frontier-20261028-eightzero-sextic-check-result.json` | `261e9f533387da9a7b6591bd4300412627120a4499c8732f2269b9e995107d76` | 21 |
| `frontier-20261028-eightzero-shape-check.py` | `35df5313bdc784602d9b69fee94743c5df484d4b3a9efd59e5de2c0ac7096976` | 40 |
| `frontier-20261028-eightzero-shape-check-result.json` | `8797bede1a81a55a2306edc405a8b8339c9325e74be7c31fafa8b96736eb0231` | 23 |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 |
| `frontier-20261028-four-zero-radical-reduction-v1.md` | `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229` | 63 |

No original-target witness or unrestricted contradiction follows. **END.**
