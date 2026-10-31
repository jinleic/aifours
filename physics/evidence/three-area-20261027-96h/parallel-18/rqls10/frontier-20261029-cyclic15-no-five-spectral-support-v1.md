# A cyclic 6D lift must have simple spectrum and full v5 support

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:41:59 PDT 2026. The conclusion is field-free and permits arbitrary complex phases, but still assumes the **unitary cyclic action** and the fixed graph incidence; it is not a general 1RQLS10 no-go.

## Statement

For any 45-distinct-ray C6 representation of `G6=Circ(15;±2,±5,±7)` with an ONB at each vertex and a unitary U implementing translation, **U has six distinct eigenvalues and the ray v5 on `(0,5)` has nonzero projection onto every U eigenspace**. Equivalently, v5 is a cyclic vector for U.

The preceding symmetry-free/rank-4 packet `frontier-20261029-cyclic15-rank4-triangle-degeneracy-v1.md` SHA-256 `3ced4cb0b85bfacba7f00e5a160753326877e11c19352617d3c60ba81030b9f9` already gives at least five distinct U eigenvalues in v5's support. The new exact argument excludes **exactly five**. With six dimensions, six distinct supported values then force simple spectrum.

## A linear-algebra reduction independent of graph labels

The exact five-support exclusion has the following standalone form. Let U^15=I on C6, and suppose the six normalized vectors

`v2, U^(-2)v2, v5, U^(-5)v5, v7, U^(-7)v7`

form an ONB. Then v5 cannot have spectral support on exactly five distinct eigenvalues of U.

Assume otherwise. Choose a U eigenbasis adapted to v5: its five occupied eigenvalues each contribute one nonzero coordinate, and the remaining coordinate is zero. After a scalar rephasing of U, the zero row has eigenvalue 1; the occupied eigenvalue exponents form a five-element set S⊂Z15. Orthogonality `v5 ⟂ U^(-5)v5` forces equal v5 population 1/3 in each of the three U^5 classes, so S meets all three residues modulo 3.

In the zero row, both v2 and v7 entries are nonzero. Otherwise row orthogonality forces one of those vectors to be supported only in that one U eigenspace, making it parallel to its shifted partner. At each of the five occupied rows, the v2 and v7 entries are also nonzero: if either vanished, zero-row orthogonality would force both to vanish, and the ONB diagonal would give that single v5 entry population 1/2, exceeding its U^5-class total 1/3.

Put `zeta=exp(2 pi i/15)` and `c_d(a,b)=1+zeta^[d(b-a)]`. These coefficients are never zero because 15 is odd. Zero-row orthogonality gives

`v7_a = -C g_a v2_a`, where `g_a=conjugate(c_2(0,a)/c_7(0,a))`

and C is a nonzero complex constant. Set `t=|C|²` and `z_a=v5_a/v2_a`. Orthogonality of occupied rows a,b then yields

`z_a conjugate(z_b) = H_ab(t) = -[c_2(a,b)+t g_a conjugate(g_b)c_7(a,b)]/c_5(a,b)`.

Each H_ab is affine in t. Consequently every four distinct occupied rows a,b,c,d satisfy the two rank-one minor equations

`H_ab H_cd - H_ad H_cb = 0`,

`H_ac H_bd - H_ad H_bc = 0`.

These are polynomials of degree at most two over Q(zeta_15).

## Complete finite resultant certificate

There are **2250** five-element S meeting all three residues modulo 3. The Galois group `(Z/15Z)^×` partitions them into **299** orbits: 265 of size 8, 31 of size 4 and 3 of size 2. For every orbit representative, two of the ten displayed minor polynomials have a **nonzero resultant**, so they have no common complex root t. Galois conjugation preserves nonvanishing, the formulas, and the orbit coverage. Therefore the five-support assumption is impossible even without using positivity of t.

- Producer `frontier-20261029-cyclic15-support5-resultant-proof-v1.py` SHA-256 `b41ffa7bf51c2526fd6191fa204a37a5349ce13a8819747cbbb303bd87068a1b`.
- Complete certificate `frontier-20261029-cyclic15-support5-resultant-proof-v1.json` SHA-256 `b04b155374c5802a4f910b7531bb050d4af19ec7226aec9244300e0dc1d44e43` records the representative, orbit size, selected two minor indices and exact nonzero resultant in the degree-8 cyclotomic basis.
- Separate exact replay `frontier-20261029-cyclic15-support5-resultant-replay-v1.py` SHA-256 `99dbda5aa892b6f489bcba209eced31c4dd55ffa44bddb9320b5372126543108` regenerates all roots in the different basis `1,omega,eta,omega eta` over Q(sqrt(5)), recomputes every selected minor and resultant, matches its exact value across bases, and checks all 2250 sets are covered. Output `frontier-20261029-cyclic15-support5-resultant-replay-v1.json` SHA-256 `a8eba234b60b485e870dabeeafb77e02687af389301de8cf3d621ee2e59a0acd` is **PASS** at 02:41:59 PDT.

If a putative graph realization had a repeated U eigenvalue, one can choose an eigenbasis within its eigenspace with a zero v5 coordinate; the previous ≥5-distinct-value theorem and the just-proved standalone exclusion leave no possibility. Thus the stated simple-spectrum/full-support conclusion follows.

## Remaining gap

This does not rule out cyclic 6D representations with six distinct eigenvalues and all six v5 coordinates nonzero, nor any symmetry-breaking representation. It does not construct the other 25 QLS cells. The row-to-minor equations, Galois orbit caller, resultant certificate and imported rank-4 theorem require independent mathematical review; no formal-kernel or novelty claim is made.
