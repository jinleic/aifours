# info-6 frontier: consolidated rank-eight extremal necessary conditions

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T22:45:58-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This consolidates and strengthens the immutable author-only phase/sign fragments; it does not amend any frozen review. The Boolean-to-polynomial caller and six-dimensional support lemma are explicitly pinned author-written inputs, not parent-adopted results. The written orbit and Fourier arguments, and all finite phase tables, require a disjoint full-scope review. No witness, unrestricted exclusion, book-source equivalence, novelty, or formal verification is claimed.

## Theorem and exact scope

Let f:F₂⁹→F₂ be balanced, have nonzero `T=⊕{x:f(x)=1}`, and satisfy `max|W_f|≤28`. Let B be the even-half polar on K=T⊥ and suppose `rank(B)=8`. On the other frequency half put

    k=W_f/4,   P=1_{|k|∈{1,7}},   n_j=#{|k|=j}, j=1,3,5,7.

Assume the **extremal branch** `wt(P)=210`. Then there is a phase-dependent bit `j∈{0,1}` defined in §5 for which

    3n₁+n₃ ≥ 195+16j,       n₁−n₃ ≥ 45+4j,                     (1)
    n₁ ≥ 60+5j,             n₇ ≤ 150−5j.                         (2)

Let m be the number of the 256 unordered T-pairs on which f agrees. Then

    m≥126+4j,   wt(D_T f)=2(256−m)≤260−8j.                      (3)

In particular this branch has at most 150 peak-28 coefficients. For m=126, necessarily j=0 and `(n₁,n₃)` is one of `(60,15),(61,12),(62,9),(63,6),(64,3),(65,0)`; `n₅=46−n₃` and `n₇=210−n₁`. No claim is made that any listed case is realizable. The single formal ten-zero histogram in the pinned placement packet has `n₁=2,n₃=5`, so this candidate would exclude every placement of **that histogram**, not all ten-zero functions.

The hypotheses `rank(B)=8` and `wt(P)=210` are essential scope. Other P weights and ranks, actual construction, the unrestricted witness-or-exclusion problem, and external mathematical status remain open. The earlier parent-adopted four-zero rank/radical result is separate and not used as an accepted premise here.

## Boolean caller and six-dimensional lemmas

The pinned `quartic-energy-coupling` author candidate supplies the following exact caller for an actual f: `Q=1_{k≡3 mod 4}` is a quadratic on the odd half with polar B, while `h=1−P` has degree≤4 and quartic part the Pfaffian 4-form of B. Here wt(h)=46. This caller is unreviewed; the following polynomial theorem can be checked independently: **for every degree≤4 h of weight 46 with this full-rank quartic form, and every Q with the same polar, the finite identities in §4 hold.**

Take symplectic coordinates `x∈F₂⁶`, `r∈F₂²` so the quartic part is

    ω₆(x)+r₀r₁q₆(x),
    ω₆=x₀x₁x₂x₃+x₀x₁x₄x₅+x₂x₃x₄x₅,
    q₆=x₀x₁+x₂x₃+x₄x₅.                                         (4)

Every six-variable slice has quartic part ω₆ and even weight at least 8. Any two slices differ by a degree≤2 polynomial; their mixed r-derivative has nondegenerate rank-six quadratic part and therefore weight 28 or 36.

The pinned rank-six lemma proves every weight-8 slice support is a symplectic simplex S. Briefly: all four cosets of every nondegenerate 4-subspace have odd support. There are 336 such subspaces and every nonzero difference lies in 80. Weight 4 is impossible; weight 6 gives 1,008 pair incidences versus 1,200 by double counting. At weight 8, the possible 4-coset patterns have counts 280 and 56, giving 1,120 triple incidences. Each nondegenerate difference plane lies in 20 such subspaces, each isotropic one in 16; since 56·20=1,120, every triple is nondegenerate. Relative to any point of S, the other seven differences have all-one-off-diagonal Gram matrix of rank six and sole relation their sum. Thus S spans F₂⁶ and every affine 4-flat contains at most five of its points.

Two weight-8 slices are identical: otherwise their difference has weight 16 and is an affine 4-flat containing an entire simplex. A weight-8 slice cannot coexist with a weight-10 or 12 slice, since their quadratic difference would be a 16-point affine 4-flat containing 7 or 6 simplex points.

For a weight-10 slice support V, the XOR is zero and the moment matrix `Σ_{v∈V}vvᵀ` is the full-rank symplectic matrix: each entry is the complementary quartic coefficient. An affine 4-flat cannot contain eight points of V. After translation to U, zero or one points outside is impossible, while two outside have XOR in U and put V in a space of dimension at most five, contradicting the full-rank moment. Hence distinct weight-10 slices cannot coexist: their difference would be an affine 4-flat containing eight points of V.

Since four even slice weights sum to 46, the only patterns remaining are

    (8,8,8,22),  (8,8,14,16),  (10,12,12,12).                 (5)

Patterns containing both 8 and 10/12 are already impossible. With three identical weight-10 slices, or two such slices and weights 12/14, the mixed derivative would have weight at most 26, contradicting rank six.

## Three orbit reduction

Every permutation of a simplex extends to an affine symplectic transformation: the seven differences relative to a basepoint have identical Gram matrix and sole relation. Thus simplexes form one orbit; the stabilizer is transitive on their subsets. A quadratic with prescribed polar is uniquely determined by its values on a simplex because it affinely spans F₂⁶.

* Pattern `(8,8,8,22)`: the three weight-8 slices are S. The mixed derivative D between S and the 22-slice is a rank-six quadratic with weight 28 and `|D∩S|=7`; this is a single orbit.
* Pattern `(8,8,14,16)`: write H=S△T for the 14-slice. H is a 16-point affine 4-flat containing five points of S. For the 16-slice U, H′=S△U has weight 16 or 24. If 16, H and H′ are affine 4-flats whose difference has weight 28, so their intersection would have size 2; two such flats in six dimensions are disjoint or meet in at least four points. Hence H′ has weight 24 and contains all of S. The mixed derivative D=H△H′ is the unique quadratic with prescribed polar equal to 1 on `S\H` and 0 on `S∩H`. This is a single orbit.
* Pattern `(10,12,12,12)`: the difference between the weight-10 support V and each other support is an affine 4-flat containing seven of its points. The three flats are distinct, else their XOR would have rank two rather than the required rank six. The lemma below gives one orbit for V and exactly three such flats; an affine change in r permutes the remaining slices.

**Seven-flat lemma.** Every such V with an affine 4-flat meeting it in seven points is affine-symplectically equivalent to

    V₀={0,3,7,11,12,13,14,16,32,48},                             (6)

and V₀ has exactly three seven-point affine 4-flats.

Proof. Translate the seven-point flat to U. The three outside quotient vectors are the three distinct nonzero vectors of a two-dimensional space, since their XOR is zero. Their projected moment is nondegenerate, hence U and its symplectic complement R are nondegenerate. In U⊕R, the zero cross-moment forces all three outside points to have the same U-component. Translate it away, making them `R\{0}`; even cardinality and XOR zero preserve the moment. The seven inside points have XOR zero and nondegenerate U-moment. Toggle 0 in their indicator: the resulting four-variable polynomial has degree≤2, nondegenerate polar, and weight 6 if 0 was inside or 8 if not. Rank-four quadratics have weight 6 or 10, so 0 was inside and the other six points form a rank-four weight-6 quadratic support M excluding 0. Such quadratics with fixed polar and weight 6 are symplectically equivalent by a hyperbolic symplectic-basis construction. This yields `R={0,16,32,48}` and `M={3,7,11,12,13,14}`.

Any five points of M affinely span U. A seven-point flat meeting R in fewer than three points must therefore be U. A flat meeting R in three points contains all R and is `R⊕L` for a two-dimensional linear L⊂U; it contains seven of V₀ exactly when all three nonzero points of L lie in M. The only such triples are `{3,13,14}` and `{7,11,12}`. Hence exactly three flats. ∎

For the finite tables below, the representatives use binary masks:

    S={0,1,2,7,11,31,47,63};  H₀={0,…,15};
    D₇={x:q₆(x)+<12,x>+1=1}; D₃={x:q₆(x)+<60,x>=1};
    H₁={0,3,13,14,16,19,29,30,32,35,45,46,48,51,61,62};
    H₂={0,7,11,12,16,23,27,28,32,39,43,44,48,55,59,60};
    (S,S,S,S△D₇), (S,S,S△H₀,S△(H₀△D₃)),
    (V₀,V₀△H₀,V₀△H₁,V₀△H₂).                                 (7)

Each Q phase is `q₆+x₆x₇+<a,x>+b`, a∈F₂⁸ and b∈F₂. Thus there are 512 phases per representative.

## Complete finite syndrome and ten-character tables

For every phase let `r=(1+6Q+4h) mod 8`, `b₀=1_{r∈{1,3}}`, and `k₀=r−8b₀`. Let K₀ be its unnormalized 256-point Walsh transform. The pinned exact checker verifies, for every phase and y,

    K₀(y)/8 ≡ A(−1)^{<p,y>} (mod 16),   A∈{−5,+5},            (8)

with the following representative-dependent p. For every representative, 256 phases have A=+5 and r(p)=3, and 256 have A=−5 and r(p)=5. In particular h(p)=1.

| slice pattern | p | phases | inverse indices per phase |
|---|---:|---:|---:|
| (8,8,8,22) | 255 | 512 | 256 |
| (8,8,14,16) | 143 | 512 | 256 |
| (10,12,12,12) | 0 | 512 | 256 |

Put `α=sign(A)` and let δ₀(x)=`1_{h(x)=1,x≠p}(-1)^{Q(x)}`. The new incidence checker verifies for every phase that there are exactly 10 characters y with

    α(−1)^{<p,y>} Walsh(δ₀)(y)=27.                              (9)

Call this set Y. For each of the 45 positions x∈h\{p}, the modification `−(-1)^Q(x)` contributes +1 to exactly **2** characters in Y and −1 to 8. For each of the 210 positions x∉h it contributes +1 to exactly **6** and −1 to 4. A center switch contributes −1 to every character in Y. These are 1,536×255 exact incidence checks, not randomized samples.

## Sign switches and the inequalities

For any allowed odd-half k, write `k=r−8b` with b a bit and set δ=b−b₀. Its nonzero positions are exactly those with |k|=1 or 3, so `D=Σδ²=n₁+n₃`. The center table shows `δ(p)∈{0,−α}`; let `j=−αδ(p)∈{0,1}`. The number of δ switches in h is n₃, and in P it is n₁. Comparing δ with δ₀, there are `45−n₃+j` removed h switches, n₁ added P switches, and j center switches. Using the incidence table gives the exact identity

    Σ_{y∈Y} t_y = 270−6(45−n₃+j)+2n₁−10j
                 = 6n₃+2n₁−16j,                                 (10)
    t_y:=α(−1)^{<p,y>}Walsh(δ)(y).

An actual f has `Walsh(k)(y)=128v(y)` for ternary v, so (8) implies `t_y≡5 (mod 16)` for every y. Fourier inversion and Parseval give

    Σ_y t_y=−256j,       Σ_y t_y²=256D,
    Σ_y (t_y−5)(t_y+11)=256(D−55−6j).                         (11)

For every integer t≡5 mod16, each of `(t−5)(t+11)`, `(t−5)(t−21)`, and `(t−21)(t−37)` is nonnegative. Thus, using the nonnegative terms outside Y,

    (t−5)(t+11) ≥ 32(t−5),
    (t−5)(t+11) ≥ 64(t−13)                                    (12)

on Y. Substitute (10) into (11) and (12): the first inequality yields `3n₁+n₃≥195+16j`, the second yields `n₁−n₃≥45+4j`. Adding them proves (1)–(2).

For the support conclusion, balance makes m even. Odd-half Walsh Parseval gives `Σ k²=64(256−m)`; the deficit from 256·7² is

    8(m−60)=6n₁+5n₃+3n₅=138+2(3n₁+n₃),                       (13)

because `n₃+n₅=wt(h)=46`. This and (1) imply m≥126+4j and the derivative bound. If m=126, j=0 and `3n₁+n₃=195`; the two inequalities give exactly the six listed integer pairs. ∎

## Controls and review boundaries

The sign-syndrome checker also applies a deliberately illegal center change `δ=A·1_p`; all inverse sums become divisible by 128 but one coefficient acquires magnitude at least 33, violating |k|≤7. Changing the wrong center fails divisibility. This is a positive near miss for the modular identity, not a Boolean spectrum. The incidence checker additionally constructs a deterministic legal bit pattern per phase and directly checks (10), but does not claim those patterns have a Boolean inverse. All calculations are same-owner checks; the cited orbit theorem and caller remain unreviewed. No solver UNSAT output is used as proof.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-extremal-ten-character-check.py` | `a2a10c767b35f58ebf5de2baaa3041f543086ad004e2730f0db14590dbda65b9` | 61 | finite control |
| `frontier-20261028-extremal-ten-character-check-result.json` | `ced3278b6b284abd1cfc552aa32904a315c0304d64c57f6beb3a081ef0e0ba92` | 78 | finite control |
| `frontier-20261028-extremal-center-sign-check.py` | `c08efb40e3081da1f35c8d2fc6f1cfca23c0bb8a200d773341837d31ad438c12` | 51 | finite control |
| `frontier-20261028-extremal-center-sign-check-result.json` | `d6b190754a8c995fc36016e4bf4976fb7e6509986245f97bbab77b9963ec9f8b` | 29 | finite control |
| `frontier-20261028-extremal-sign-syndrome-check.py` | `aacaf9e79c9d01325fb0c6f7310c96e5085a70040f91c1a620cc84d502db7f2f` | 63 | finite control |
| `frontier-20261028-extremal-sign-syndrome-check-result.json` | `8d80d4f6b53ec7e2ffd39d8357602944e80f67c2f8a1445b568648f8180cd287` | 60 | finite control |
| `frontier-20261028-quartic-energy-coupling-v1.md` | `ceeaa06d3b2ae95b5ff779307a1246153ed4a465538de5bcfa94eb8e16c8e859` | 61 | unreviewed caller |
| `frontier-20261028-rank6-simplex-obstruction-v1.md` | `121f8ade103f4d5ae2dad76ae9367f2cda6cd1665ac612b0860e44d05489e12b` | 60 | unreviewed support lemma |
| `frontier-20261028-rank-bound-sharpening-v1.md` | `f741e11a0cc0a73e8c094f6c2c74a09f3f902db58100e3dc9e76bf059c109aab` | 60 | unreviewed supporting proof |
| `frontier-20261028-fullrank-extremal-phase-v1.md` | `e12b3a32a3f7f19b9dea35615bbf4c8fbd6ba970d1491ca33f3fc8f4bacc6fd4` | 100 | unreviewed orbit precursor |

**END.**
