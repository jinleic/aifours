# A rational-spectral obstruction for the new circulant 6D complement

**WRITTEN + EXACT-INTEGER-SUPPORT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:09:17 PDT 2026. This covers arbitrary complex phases but requires a particular cyclic unitary symmetry and rational spectral populations. It is not an unrestricted 6D, QLS10 or even-order Fourier-product theorem.

## Claim

Let G be `Circ(15; ±2, ±5, ±7)`. Suppose 45 distinct rays in C6 are assigned to its edges, the six incident rays at each vertex form an ONB, and translation `i -> i+1` of G is implemented by a unitary U. For d in `{2,5,7}`, write `v_d` for a normalized ray on edge `(0,d)`. Then **there is no eigenbasis of U in which every coordinate population `|<e_j,v_2>|²` and `|<e_j,v_7>|²` is rational**.

Equivalently, no such cyclic-equivariant realization exists with those two sets of squared spectral amplitudes all rational. In particular a flat-amplitude realization in an eigenbasis of U is impossible. All phase values may otherwise be arbitrary. If a cyclic-equivariant realization exists, every eigenbasis has at least one irrational population among those of v2 and v7.

This applies to the 6D target of the exact 600-cell 4D core `frontier-20261029-600cell-circulant4d-core-v1.md`, SHA-256 `c9370b9c56c57c0ef93ea501cccb0c8fbc34f287e6c418a1a4486bc384498ec1`. It neither requires nor rules out another 4D core.

## 1. Spectral and rational-cyclotomic reduction

The 15 ONB contexts, each ray occurring in two contexts, form an odd parity system. As in `frontier-20261029-g6-dihedral-equivariant-reduction-v1.md`, every commuting projection has even rank and rank 2 is impossible because a ray's orthogonal partner in a 2D sector would have to occur on two distinct edges. Hence the ray projectors are irreducible. U^15 commutes with all of them and is scalar; after rephasing, U^15=I. No smaller positive power can be scalar because translation moves every edge and all 45 rays are distinct. Thus U has projective order 15.

Let `zeta=exp(2 pi i/15)` and take an eigenbasis with U-eigenvalues `zeta^(a_j)`, including multiplicities. At vertex 0 the six ONB rays are

`v_2, U^(-2)v_2, v_5, U^(-5)v_5, v_7, U^(-7)v_7`.

Set `p_dj=|<e_j,v_d>|²`. The diagonal of the ONB identity gives `p_2j+p_5j+p_7j=1/2`. The orthogonality of `v_5` and `U^(-5)v_5` makes the total v5 population in each of the three U^5 eigenspaces exactly 1/3, so every `p_5j<=1/3` and hence `q_j=p_2j+p_7j>=1/6`.

Under the assumed rationality, each p2j and p7j is rational. Since −2 and −7 are units modulo 15, applying a cyclotomic Galois automorphism to their two orthogonality equations gives

`sum_j p_2j zeta^(a_j)=sum_j p_7j zeta^(a_j)=0`, hence `sum_j q_j zeta^(a_j)=0`.

Aggregate q_j by eigenvalue. Every eigenvalue present has a **strictly positive rational** coefficient in this vanishing sum. Write the exponents using CRT as a 3×5 grid, with `omega=zeta^5` and `eta=zeta^3`. The standard degree identity `[Q(omega,eta):Q]=8` implies the grid coefficients satisfy `q_(u,v)=r_u+c_v`: subtract the last row and column to see all 2×2 mixed differences vanish. Because all q are nonnegative, shifting a constant between r and c makes all r,c nonnegative. Therefore the support is a union of complete 3-cycles and 5-cycles of 15th roots.

There are at most six distinct eigenvalues. The three U^5 eigenvalues must all occur. A complete 5-cycle lies in a single U^5 eigenspace, and adding a second covered eigenvalue would require at least two additional distinct points. Thus no 5-cycle is possible. A single 3-cycle would make U^3 scalar, contrary to projective order 15. Consequently the spectrum consists of **exactly two disjoint complete 3-cycles**, six eigenvalues with no multiplicity. The rational coefficient relation also makes the p2 and p7 values constant across each 3-cycle. From the diagonal identity the same holds for p5.

## 2. All six basis rays become flat

Write the two spectral cosets as eigenvalues `alpha omega^k` and `beta omega^k`, k=0,1,2, with `omega=exp(2 pi i/3)` and `rho=beta/alpha`, a 15th root of unity. In either coset, let `x_(k,d)` be the k-th coordinate of v_d and define a 3×3 matrix Y by

`Y_(k,2)=x_(k,2)`, `Y_(k,5)=x_(k,5)`, `Y_(k,7)=omega^(-k) x_(k,7)`.

For `k != l`, row orthogonality of the six-column basis above gives

`sum_d x_(k,d) conjugate(x_(l,d)) [1+omega^(-d(k-l))]=0`.

Using `d=2,5 ≡2 (mod 3)` and `d=7 ≡1 (mod 3)`, this is exactly orthogonality of rows k,l of Y. The ONB diagonal equation gives every row squared norm 1/2, so `sqrt(2)Y` is unitary. Since each column's squared entries are constant in k, its column norm forces every such entry to have squared magnitude 1/6. Thus **all six basis rays are flat** in the U eigenbasis.

A 3×3 complex Hadamard matrix is, after row and column phases, the Fourier matrix or its conjugate: this follows directly because three unit phases summing to zero are a rotated `{1,omega,omega²}`. Accordingly in coset h=A,B write

`Y^h_(k,d)=r^h_k c^h_d omega^(sigma_h k ell_d)/sqrt(6)`,

where all r,c have modulus 1, `sigma_h` is +1 or −1, and `(ell_2,ell_5,ell_7)=(0,1,2)`.

## 3. Cross-coset row orthogonality is impossible

Set `h_d=c^A_d conjugate(c^B_d)`, so h2,h5,h7 are nonzero, and `e^h_d=sigma_h ell_d + 1_(d=7) (mod 3)`. For rows k in coset A and l in coset B, putting `delta=k-l`, orthogonality gives, after harmless nonzero row phases,

`sum_d h_d omega^[k(e^A_d-e^B_d)+delta e^B_d] (1+rho^d omega^(-d delta))=0`.

If `sigma_A != sigma_B`, the three differences `e^A_d-e^B_d` are distinct modulo 3. Taking the 3-point Fourier transform in k with delta=0 forces `h_d(1+rho^d)=0` for every d. This is impossible because rho has odd order dividing 15.

If `sigma_A=sigma_B=sigma`, Fourier transformation in delta gives one equation per residue. For sigma=+1 they are

`h2+h7=0`, `h5+h2 rho²=0`, `h5 rho⁵+h7 rho⁷=0`.

The first two make the third `-2 h2 rho⁷=0`, impossible. For sigma=−1 the equations are

`h2+h5 rho⁵=0`, `h2 rho²+h7 rho⁷=0`, `h5+h7=0`.

The first and third make the second `2 h2 rho²=0`, again impossible. This completes the stated conditional no-go.

## Exact checks and limitations

The purely integer support and exponent-table replay `frontier-20261029-cyclic15-rational-support-replay-v1.py` SHA-256 `d1121d7770d9b3d1fe2c0bad5362dbe7c101eb3745ce4eae32934e57e29c06ec` verifies all support-cover cases with at most six eigenvalues: exactly 10 satisfy three U^5 phases and projective order 15, all unions of two 3-cycles. It also verifies both residue tables used above. Result `frontier-20261029-cyclic15-rational-support-replay-v1.json` SHA-256 `118c2397ed864200213ea766c8a685b687b0babb657b84276c8b934f7588f234` records **PASS** at 02:09:17 PDT. The cyclotomic degree identity and elementary 3×3 Hadamard classification are named mathematical imports; the support and cross-row deductions are written here.

The proof does **not** handle irrational spectral populations, broken cyclic symmetry, general 6D complements or general 1RQLS10. The reduction, coordinate phases, and line-graph-to-QLS caller require independent mathematical review; no formal-kernel proof, external review or novelty claim is asserted.
