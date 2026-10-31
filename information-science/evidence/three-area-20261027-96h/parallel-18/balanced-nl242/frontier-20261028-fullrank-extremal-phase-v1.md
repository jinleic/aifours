# info-6 frontier: extremal full-rank peak/unit phase

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:18:56-0700**. **UNREVIEWED AUTHOR CANDIDATE**. The structural classification below is written mathematics; its small explicit phase table is a same-owner finite computation. Neither is parent-adopted or a disjoint review. No witness, unrestricted exclusion, external novelty, or formal verification is claimed.

## Statement

For any actual balanced f:F₂⁹→F₂ with `T=⊕{x:f(x)=1}≠0` and `max|W_f|≤28`, let K=T⊥ be the even frequency half, B its eight-dimensional even-half polar, Q the odd-half quadratic with the same polar, and `P=1_{|W_f|∈{4,28}}` on the odd half. Suppose `rank(B)=8` and `wt(P)=210`. Put `h=1+P` and `c=wt(hQ)`; in the count convention `A_t=#{a≠0:W_f(a)/4=t}`, this is `c=A₋₅+A₃`. Then

    wt(Q)=136  =>  c∈{10,24,26};
    wt(Q)=120  =>  c∈{20,22,36}.                                  (1)

More precisely, among the 512 quadratic phases Q with this fixed full-rank polar, the respective intersection counts occur 10,120,126 times in the displayed first row, and 126,120,10 times in the second row. In particular the formal ten-zero, rank-eight histogram pinned below has `wt(P)=210`, `wt(Q)=136`, `c=22`, so **that specific histogram cannot be placed as an actual target spectrum**, even though its scalar/dual and even-half mod-8 checks succeed. This does not exclude all ten-zero functions or all rank-eight functions.

The Boolean-to-polynomial identities used here are the unreviewed written-support candidate `frontier-20261028-quartic-energy-coupling-v1.md`: h has degree≤4 and quartic part the Pfaffian four-form of B, and Q has polar B. We prove the following independent polynomial statement: **for any h:F₂⁸→F₂ with that quartic part and wt(h)=46, and any Q with polar B, (1) and the full phase frequencies hold.** Thus the polynomial claim may be reviewed independently of the Boolean caller. The earlier unreviewed rank-six simplex lemma and ten-point flat lemma are pinned below; they are reproduced at the exact scope needed here.

## Slice structure

Choose symplectic coordinates `x∈F₂⁶`, `r∈F₂²`, with

    q₆=x₀x₁+x₂x₃+x₄x₅,
    ω₆=x₀x₁x₂x₃+x₀x₁x₄x₅+x₂x₃x₄x₅,
    h₄=ω₆+r₀r₁q₆.                                                (2)

Each slice `h_r` has quartic part ω₆ and even weight at least 8. Two slices differ by a degree≤2 polynomial; their mixed r-derivative is a quadratic with rank-six polar, hence has weight 28 or 36. A weight-eight slice support S is a symplectic simplex: after translating any support point to 0, the seven other points have zero-diagonal, all-one-off-diagonal Gram matrix, rank six and unique linear relation their sum. Any affine 4-flat contains at most five points of S. Two weight-eight slices are therefore identical, and a weight-eight slice cannot coexist with one of weight 10 or 12: a nonzero quadratic difference of weight at most 18 or 20 must have weight 16 and be an affine 4-flat containing respectively 7 or 6 points of S.

For a weight-ten slice support V, no affine 4-flat contains eight of its points. Indeed V has even cardinality, XOR zero, and full-rank moment matrix `Σ_{v∈V}vvᵀ`: the moment is the symplectic matrix complementary to ω₆. If an affine 4-flat contained at least eight points, translate it to a linear U; zero or one points outside are immediately impossible, and with two outside, their XOR lies in U, so V spans at most five dimensions, contradicting the full moment rank. Consequently two weight-ten slices are identical: otherwise their nonzero quadratic difference has weight 16 and is an affine 4-flat containing eight points of either support.

Because the four even slice weights add to 46, these exclusions and the rank-six mixed derivative leave exactly the possible sorted patterns

    (8,8,8,22),  (8,8,14,16),  (10,12,12,12).                   (3)

For example, in `(10,10,10,16)` and `(10,10,12,14)`, the two or three weight-ten slices coincide, making the mixed derivative the difference of two slices whose total weights are at most 26, contrary to its minimum 28. All patterns containing an 8 together with 10 or 12 are already impossible.

## Reduction of the three patterns to explicit representatives

Affine symplectic transformations of x preserve (2), and affine transformations of the two r-coordinates preserve its quartic part. They act by bijection on the Q phases. Thus it suffices to classify slice supports up to those transformations.

For a simplex S, every permutation of its eight points extends to an affine symplectic transformation: relative to any chosen base point, the seven difference vectors have the same Gram matrix and the same unique relation. In particular all such simplexes are equivalent, and their stabilizer is transitive on subsets of any fixed size. A quadratic with prescribed polar is uniquely determined by its values on S, because S affinely spans F₂⁶.

* In `(8,8,8,22)`, the three simplex slices are S. The mixed derivative is `D=S△U`, a rank-six quadratic of weight at most 30 and hence 28. It has `|D∩S|=7`. The simplex stabilizer and uniqueness of D reduce this to one representative.
* In `(8,8,14,16)`, the two simplex slices are S. Let H=S△T for the 14-slice T; H is an affine 4-flat containing five points of S. Let H′=S△U for the 16-slice U. Its weight is 16 or 24. If it were 16, H′ would also be an affine 4-flat; their symmetric difference would be the rank-six mixed derivative of weight 28, forcing `|H∩H′|=2`. Two affine 4-flats in F₂⁶ are either disjoint or meet in at least four points, a contradiction. Hence `wt(H′)=24` and `S⊂H′`. The mixed derivative `D=H△H′` is the unique quadratic with the fixed polar that equals 1 on `S\H` and 0 on `S∩H`. Every H is the affine span of its five simplex points, so this is one orbit.
* In `(10,12,12,12)`, each difference between the weight-ten support V and a weight-12 support is a weight-16 quadratic, hence an affine 4-flat containing seven points of V. These three flats must be distinct: if two were equal, their XOR with the third would be a rank-two indicator, not the rank-six mixed derivative. The next lemma gives a single orbit for V and exactly three such flats, so this case too has one representative; an r-coordinate affine map permutes the three non-V slices.

**Ten-point orbit lemma.** Let V have the moments above and an affine 4-flat meeting V in seven points. Then V is affine-symplectically equivalent to

    V₀={0,3,7,11,12,13,14,16,32,48}.                               (4)

Moreover V₀ has exactly three affine 4-flats meeting it in seven points.

Proof. Translate the 7-point flat to a linear U. The three nonzero quotient classes of the outside points are distinct: their sum is zero because ⊕V=0. Their projected second moment is nondegenerate on the two-dimensional quotient. Hence U and its symplectic complement R are both nondegenerate. In the decomposition U⊕R, vanishing of the cross block of `Σ vvᵀ` forces the three outside points to have a common U-coordinate; translating by it makes them exactly `R\{0}`. Translation preserves the moment because |V| is even and ⊕V=0.

The seven inside points have XOR zero and moment the nondegenerate symplectic matrix on U. Toggle the point 0 in their indicator. The resulting four-variable polynomial has degree≤2: its weight and first moments are even, so its degree-four and degree-three coefficients vanish. Its polar is the complementary-moment matrix and is nondegenerate. A rank-four quadratic on F₂⁴ has weight 6 or 10; the toggled indicator has weight 6 if 0 was inside and 8 otherwise. Thus 0 is inside and the other six inside points form the support M of a rank-four weight-6 quadratic with M excluding 0. All such quadratics with fixed symplectic polar are linearly symplectically equivalent by the standard hyperbolic symplectic-basis construction. Taking `R={0,16,32,48}` and `M={3,7,11,12,13,14}` gives (4).

To count the seven-point flats of V₀, any five points of M affinely span the four-dimensional U. A flat meeting R in fewer than three points and containing seven points of V₀ must therefore be U itself. A flat meeting R in three points contains all of R and has form `R⊕L` for a two-dimensional linear L⊂U; it contains seven of V₀ exactly when all three nonzero points of L lie in M. The only such triples are `{3,13,14}` and `{7,11,12}`. Thus there are exactly three flats. ∎

## Exact finite phase table

Write integers as binary coordinate masks. Let `S={0,1,2,7,11,31,47,63}`, `H={0,…,15}`, `D₇={x:q₆(x)+<12,x>+1=1}`, and `D₃={x:q₆(x)+<60,x>=1}`, where `<a,x>` is parity of `a & x`. Let V₀ be (4), and its three seven-point flats be

    H₀={0,…,15},
    H₁={0,3,13,14,16,19,29,30,32,35,45,46,48,51,61,62},
    H₂={0,7,11,12,16,23,27,28,32,39,43,44,48,55,59,60}.

The representatives, in r order 00,01,10,11, are

    (S,S,S,S△D₇),
    (S,S,S△H,S△(H△D₃)),
    (V₀,V₀△H₀,V₀△H₁,V₀△H₂).                                    (5)

Each has weight 46 and exactly the quartic part in (2). The following complete table is obtained by direct enumeration of the 512 phases `Q=q₆+x₆x₇+<a,x>+b`, `a∈F₂⁸`, `b∈F₂`; all three representatives have the same table:

| wt(Q) | wt(hQ) | number of phases |
|---:|---:|---:|
| 136 | 10 | 10 |
| 136 | 24 | 120 |
| 136 | 26 | 126 |
| 120 | 20 | 126 |
| 120 | 22 | 120 |
| 120 | 36 | 10 |

The 97-LF checker below constructs the three literal representatives, independently computes their ANFs and all 512 intersections each, and checks the canonical 7-flat count. It exhausts only this explicit finite table; the all-variable reduction is the written orbit argument above. This proves the stated polynomial criterion conditional on that finite computation and the cited support lemma; it does not use a solver's UNSAT verdict. ∎

## Formal ten-zero model and remaining gap

The pinned formal rank-eight model has Z₈ size 10 and a separately checked degree≤3 lift of its even-half mod-8 data; all 257 scalar dual coefficients are integral and nonnegative. Its `wt(Q)=136`, `wt(P)=210`, `A₋₅+A₃=22` fail (1). The count vector, its mod-8 lift and its checks are **not** a labelled Boolean spectrum or a target witness; excluding this vector is not a ten-zero no-go. Other scalar counts, quotient placement, common q/Q, all 511 nonzero-shift correlations, Boolean inverse and the original witness-or-unrestricted-exclusion gap remain. The original book/modern status and novelty are not resolved by this packet.

## Pins

| File in this directory | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-extremal-fullrank-phase-check.py` | `b6e528cb026aa44810ad5124fdb4f6240a181297fb1c1cc0e5e24036f114a849` | 97 |
| `frontier-20261028-extremal-fullrank-phase-check-result.json` | `fe4067857a8c91f6ab9c9bbc90a3cdd62f5fde1ebf5155ecda824cda32072ae2` | 149 |
| `frontier-20261028-tenzero-rank8-counts-result.json` | `d037ca8df3a0b472e2e3943481fb54b591968067ba3439d6679a69f1ebea002e` | 287 |
| `frontier-20261028-tenzero-mod8-lift-check.py` | `90f0c82cccc4fd0df5c595b031cdb17a1054b033feb13ba7dc3c5b1b578bd45d` | 56 |
| `frontier-20261028-tenzero-mod8-lift-check-result.json` | `4728b0e038b43e3194533de81fc354ff368315ee7b3f6b6144838254662f22cf` | 36 |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 |
| `frontier-20261028-rank-bound-sharpening-v1.md` | `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab` | 60 |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 |

**END.**
