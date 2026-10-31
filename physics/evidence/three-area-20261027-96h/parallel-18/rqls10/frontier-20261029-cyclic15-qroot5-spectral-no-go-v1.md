# The cyclic-15 complement also excludes Q(sqrt(5)) spectral populations

**WRITTEN + EXACT-FINITE-ALGEBRA-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:21:13 PDT 2026. This closes the real-quadratic-field gap left by `frontier-20261029-cyclic15-disjoint-field-no-go-v1.md`, SHA-256 `9f0821c445993766a5401ffcba9d14ce717b9d60942264e493de3450fcc9c057`. It remains conditional on the named cyclic unitary symmetry, not a general G6 or 1RQLS10 no-go.

## Statement

Under the hypotheses of `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md` SHA-256 `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada`—45 distinct C6 edge rays on `G6=Circ(15; ±2,±5,±7)`, an ONB at every vertex, and a unitary U implementing translation—there is no U eigenbasis in which the squared coordinates of both representative rays v2 and v7 all lie in **Q(sqrt(5))**.

More generally, the same proof applies to any real field F containing sqrt(5) for which `[F(zeta_15):F]=4`. Combined with the preceding disjoint-field result, no real quadratic field can contain all of those populations. Irrational populations outside the stated field cases, broken cyclic symmetry, arbitrary G6 complements and unrestricted 1RQLS10 remain open.

## Exact spectral census

As in the preceding proof, rephase U so U^15=I, and write its six eigenvalue exponents modulo 15. Since U has projective order 15 and all three U^5 eigenspaces occur, after a common eigenphase shift we need only examine multisets `(0,a1,...,a5)` containing all three residues mod 3 with `gcd(15,a1,...,a5)=1`.

For each distinct eigenvalue exponent a of multiplicity m, set `q_a` to the sum over that eigenspace of `p2_j+p7_j`. Orthogonality and the diagonal ONB equations imply

`sum_a q_a zeta_15^(-2a)=0`,

`sum_(a=r mod 3) q_a = n_r/2 - 1/3`, for r=0,1,2,

`m/6 <= q_a <= m/2`,

where n_r is the total multiplicity in residue class r. The first identity uses the d=2 moment directly and the d=7 moment after the automorphism `zeta_15 -> zeta_15^11`, which fixes Q(sqrt(5)) and sends −7 to −2. The bounds use `0<=p5_j<=1/3`.

`frontier-20261029-cyclic15-qroot5-spectrum-census-v1.py` SHA-256 `6baa6c56d623c24526965e6702fc2fc8f4ea392de6fdc2fcddf48108a795c4b0` solves those exact equations and inequalities for **all 7740** normalized multisets over Q(sqrt(5)). It uses the basis `1,omega,eta,omega eta` over Q(sqrt(5)), exact pair arithmetic, exact signs and one-variable interval bounds. There are 7316 inconsistent systems, 390 consistent systems with no free parameter and 34 with one; just **21** meet the necessary bounds. Up to common eigenphase and graph multipliers `1,4,11,14`, they fall into four classes:

| Representative spectrum | Number among the 21 |
|---|---:|
| `(0,0,3,5,10,12)` | 5 |
| `(0,1,2,4,5,12)` | 12 |
| `(0,1,5,6,10,11)` | 2 |
| `(0,2,5,7,10,12)` | 2 |

The multipliers preserve `{±2,±5,±7}`; 4 and 11 exchange the d=2 and d=7 seed orbits up to translation, while 1 and 14 preserve them. Thus the field hypothesis and population constraints survive this reduction. The last two classes are the two disjoint 3-cycle spectra. The census result `frontier-20261029-cyclic15-qroot5-spectrum-census-v1.json` SHA-256 `fa4f2fcfa29b8ed7f4daf875eb8d3df5601321cf357977d3120d8ed702451a3f` records **PASS** at 02:21:13 PDT.

## Excluding the four classes

**Two 3-cycle classes.** The exact moment kernels checked by the census make p2 and p7 constant across each 3-cycle even over Q(sqrt(5)); the diagonal identity then does the same for p5. The three-row unitary argument and final complex-Hadamard cross-row contradiction in the rational-spectral packet apply verbatim. Thus neither class is possible.

**Repeated-eigenvalue class `(0,0,3,5,10,12)`.** Exact elimination fixes `q_5=q_10=1/6` and forces `p2_5=p2_10` and `p7_5=p7_10`. Hence `p5_5=p5_10=1/3`. Consider the two rows of the six-column ONB corresponding to eigenvalues `zeta^5` and `zeta^10`. For each d=2,5,7 the magnitude of the paired-column coefficient `1+zeta^(5d)` is 1. The v5 term in their row inner product has magnitude 1/3, while the other two terms have total magnitude `p2_5+p7_5=q_5=1/6`. They cannot cancel.

**Simple-eigenvalue class `(0,1,2,4,5,12)`.** Exact elimination fixes `q=(X,X,Y,Y,X,Y)` in this order, where `X=(sqrt(5)-1)/3` and `Y=1-sqrt(5)/3`. The moment-only control `frontier-20261029-cyclic15-qroot5-population-control-v1.md` SHA-256 `035ce7d91b78c6d653c5e69d5d5a5022a5b423c1795ae2a71882135daf975d11` shows why positivity alone cannot reject this case. But rows 0 and 12 of the ONB must be orthogonal. Their d=5 coefficient has magnitude 2, while their d=2 and d=7 coefficients have common magnitude `c=(sqrt(5)-1)/2`. Cauchy–Schwarz would therefore require

`2 sqrt((1/2-X)(1/2-Y)) <= c sqrt(XY)`.

This fails exactly, since the difference of the squared sides is `(6 sqrt(5)-13)/9>0`. Thus this last class is impossible too.

## Why the general field extension holds

If F contains sqrt(5) and `[F(zeta_15):F]=4`, the same four field-basis elements used in the census remain linearly independent over F, and the automorphism zeta -> zeta^11 extends while fixing F. All row reductions have coefficients in Q(sqrt(5)); their ranks, inconsistency statements, unique q values and moment-kernel equalities remain valid over F. Every one-parameter feasibility interval has endpoints in Q(sqrt(5)), so the exact real bound test also remains necessary over F. The four class exclusions then use only real nonnegativity, Cauchy–Schwarz and the prior complex-Hadamard contradiction.

In particular F may be Q(sqrt(5)), or a real extension linearly disjoint from the cyclotomic field over Q(sqrt(5)). Together with the earlier degree-8 theorem, this excludes populations all contained in any one real quadratic number field.

## Review boundary

The finite census is an exact author calculation, not an independent mathematical or formal-kernel review. The spectrum normalization and graph-multiplier caller, field-extension claim, previous Hadamard contradiction and both row inequalities require independent verification. No conclusion is made for arbitrary algebraic populations, arbitrary cyclic realizations, symmetry-breaking complements, or unrestricted 1RQLS10; no novelty claim is asserted.
