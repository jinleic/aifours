# Order-eight 2×4 Diţă Fourier products have no transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay pin: **Wed Oct 28 22:02:19 PDT 2026**. This closes, subject to full review, the 30720 explicitly open both-free branches in `frontier-20261028-n8-dita-generic-block-frontier-v1.md` SHA **252dd4bb7c44f4394d8f3e592bd1360c977f75b22664fb917a92f836a601998a**. The latter's premature root-caller inference was WITHDRAWN in `frontier-20261028-n8-generic-root-caller-correction-v1.md` SHA **316a4ac8725878236df2e110d5b1feb64576a9649e0e3577bafcc2d6aa866619**; §5 below supplies the missing explicit fixed-root checks. Earlier bytes remain unchanged.

## 1. Claim and exact scope

Let A,B be ANY 4×4 complex Hadamards and delta any four unit phases. Let K be obtained from the block matrix

`[[A, diag(delta) B], [A, -diag(delta) B]]`

by any source-row permutation, row/column unit phases and column permutation. The actual order8 Fourier-product QLS of K has **NO orthogonal transversal**, even when rays repeat. This is a statement over a full continuous two-block Diţă family, with arbitrary complex 4×4 blocks; it is NOT an all-order8 Hadamard theorem, an even-order general no-go, an unrestricted QLS10 result, a novelty claim, or a formal proof.

## 2. Elementary four-dimensional block normal form

Every complex 4×4 Hadamard is monomially equivalent to

`H(z)=[[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]`, `|z|=1`.

For completeness: four unit complex numbers summing to zero form two antipodal pairs. If a pair's sum is zero this is immediate; otherwise the unordered pair is uniquely determined by its sum as the intersection of two unit circles, so the opposite pair has the same endpoints. Dephase the first row and column. Each other row then has the form `[1,-1,z,-z]` after column permutation. If two rows share the same chosen position of −1, orthogonality forces their other phases to be opposite and the fourth row is `[1,1,-1,-1]`, yielding H(z) after row/column permutations. If all three −1 positions are different, take rows `[1,-1,z,-z]` and `[1,w,-1,-w]`; their inner product is `(1-w)(1-conj(z))=0`. Either w=1 or z=1 creates an additional −1 position shared with another row, reducing to the previous case. Thus no outside classification theorem is needed.

The A-normalizing row operation acts on BOTH row halves, and column operations act only on the h=0 block. The transformed B is another Hadamard; its row permutation, row phases and column operations give `diag(delta) P_mu H(beta)`. Source row permutations and column gauges are already allowed. Hence it suffices to consider, for a∈{0,1} and t,b∈{0,1,2,3},

`K_((a,t),(0,b))=H(alpha)_(t,b)`,
`K_((a,t),(1,b))=(-1)^a delta_t H(beta)_(mu(t),b)`.

All alpha,beta,delta_t have unit modulus and mu is an arbitrary permutation.

## 3. Complete normalization and same-group phase classification

A cyclic physical-coordinate shift puts source `(0,0)` at coordinate0; a common shift of the physical row labels puts the transversal cell in h0 column0 at row0. Column gauges make delta_0=1. To arrange mu(0)=0, dephase the B row selected at t=0. If its old row index is s=0,1,2,3, the resulting H block is respectively H(beta), H(beta^(-1)), H(beta), H(beta^(-1)), with row orders `[0,1,2,3]`, `[1,0,3,2]`, `[2,3,0,1]`, `[3,2,1,0]`. Remaining h1 column relabellings are absorbed into its arbitrary transversal assignment. All operations preserve the SAME physical orthogonality constraints.

There are thus 5040 source orderings O with O[0]=0 and 210 assignments R0 of h0 columns with R0[0]=0. Each of their six same-h0 equations is `A+B alpha=0` or `A+B alpha^(-1)=0`, with A,B∈Z[zeta8]. Exact comparison of ratios and squared magnitudes shows each unit alpha is either FREE (all equations identically zero) or an eighth root. Two independently written programs, Python SHA **fb96a9a6b9cbb64b1aa15a58b2fda997766d49f50540b51e18bce6da7137f48d** and C++ SHA **34bef7404003a7d4cd3669a7980e10a81bf6b2fc8aaea5394187229af0da9ded**, produce byte-identical complete 14592-row tables SHA **5abdc4aebf774d3491215ac68dd71ae4d158d9c72ccaabda63cc5905e10a10c5**: 1280 FREE, the other13312 fixed to eighth roots, none to another unit value. Relabelling source t by mu and translating h1 row assignments reduces beta's six equations to the SAME complete table.

Extending through all h1 assignments and all six normalized mu gives 651264 both-group-feasible branches: **421888 fixed/fixed**, **172032 one-free**, **57344 both-free**. Independent `frontier-20261028-n8-dita-generic-full-replay-v1.py` SHA **508d571aac0a0fe0118ddb0ad2f0b868acf1688cd945c5925a247ceb954e84a1**, result SHA **2536a16417ab4859593f59c40f4445201174fe2573c46870abb713c7dc4217aa**, regenerates them from the matched table by an independent h1 caller. Its 40960 one-free residual and57344 both-free branch files are byte-identical to the producer's lists.

## 4. Cross-phase algebra and branch exhaustion

For each branch, the 16 cross-group Gram equations form `C(alpha,beta) delta=0`. Every coefficient is an explicit sum of two zeta8 powers multiplied by a monomial in alpha^(-1),beta. All delta_t must be nonzero and have equal magnitude1.

The EXACT branch tree is:

1. Fixed/fixed: 397312 cross matrices have rank4 modulo65521; 24576 have rank3 but their signed-minor kernel vector has unequal squared magnitudes modulo65521. Both cases exclude unit delta.
2. One-free: phase-independent cross rows reject131072 by rank4. The remaining40960 give 32768 incompatible linear free-phase systems and8192 exact minor polynomials forcing the free phase into eighth roots. **All 16384 actual fixed-root specializations** have unequal kernel norms, independently replayed below; this is the explicit caller missing from the withdrawn inference.
3. Both-free: parity-block phase scalings give 22528 rank4 rejections and4096 phase-invariant cofactor contradictions. The remaining30720 have 28672 exact SEPARABLE bivariate minor gates and2048 exact BINOMIAL gates. Among separable gates,12288 are nonzero monomials on the unit torus; the other16384 force25600 one-root specializations. Of those, rank/norm/linear gates reject18432; 7168 exact univariate gates force14336 fully fixed root cases, all with unequal kernel norms. Each of the2048 binomial gates forces `x=k*y^(+1)` or `x=k*y^(-1)` with x=alpha^(-1), y=beta and every allowed k an eighth root; a three-row cofactor then has one coordinate identically zero and another a nonzero monomial, forcing some delta_t=0. All branches are therefore rejected within this finite proof.

For rank/norm tests, integer-isqrt prime checker SHA **11533f22400d08f18c3d130875cef54aa548526dc803b0aefd4f2cafce751d19** verifies p=65521 prime, root `w=57852` and conjugate root `w^(-1)=8031`. A nonzero modular minor proves nonzero exact rank. If modular rank3 and an actual unit delta existed, exact rank would be3; the signed 3×3 cofactor vector would span its kernel and its four squared magnitudes would agree. Evaluating each cofactor at w and w^(-1) makes any unequal norm residues an exact contradiction. Rank4 over C is already impossible for nonzero delta. No inference from a modular equality alone is made.

## 5. Independent replay and actual error boundary

- **Same-group / full coverage:** independently coded Python+C++ h0 tables match byte-for-byte as above. Full branch replay result **2536a16417ab4859593f59c40f4445201174fe2573c46870abb713c7dc4217aa** reproduces all651264 cases, rank/norm counts and exact residual streams.
- **Both-free invariant caller:** independent `frontier-20261028-n8-dita-freefree-replay-v1.py` SHA **39b8e99a308d64320ff83bd5e89e94659ec85462b6cdb0bd3dc481b24f1e482e**, result **1f0c9e6590586da2b073b6a19c84a221488d8a4ee048cb8e34e379b9f52a8533**, regenerates57344 cases and the identical 30720 residual stream.
- **Linear/specialization callers:** `frontier-20261028-n8-dita-linear-gate-replay-v1.py` SHA **bb6c178a1f17d62a10089e0dde0ef13a681a204c073060c7a7ae5fc7d4a743e2**, result **7e8a6c4ddde0d2c28017d9c892e8ae6d04dbcca8caf70fff8f5047c2e1efaf3e**, reproduces the 40960 one-free branch gates,25600 both-free root specializations and their bit-identical residuals.
- **Bivariate terminal certificates:** `frontier-20261028-n8-dita-bivariate-cert-replay-v1.py` SHA **e71e59569cb4fe8b4809a24d12d7cddf13c4a25e01124e622eaab8cb9f256bfb**, result **490437c022939c600764d976f47219af608df9577f9400e06f8f1afdc67d2d24**, independently reconstructs every selected determinant via a 3×3 exact interpolation grid, verifies all28672 separable and2048 binomial certificates, and checks each claimed cofactor polynomial by ten exact evaluation points against degree<=9.
- **Univariate terminal certificates and corrected fixed-root calls:** `frontier-20261028-n8-dita-univariate-cert-replay-v1.py` SHA **df552972a9d3f9015a53d9d951c1f9d4865eac3323fb3889b18c2b1b71440aab**, result **530661def0cdc172d62936712f3c12da211ef9fe2636c96e2be751c624a9c944**, independently interpolates all8192+7168 minor polynomials and rejects all16384+14336 explicit fixed-root cases by unequal cofactor norms modulo the DIFFERENT prime97, without fallback. This repairs the explicitly withdrawn root-caller inference prospectively, not by editing its old packet.

The replay desks use shared mathematical reductions and, except the terminal fixed roots, the same prime. They are not a Lean/kernel proof, external configured-family review or novelty clearance. Complete mathematical and code review is still required.

## 6. Exact open boundary

There are complex 8×8 Hadamards outside the stated 2×4 Diţă block family. This packet does not prove or disprove whether ANY of those yield an even-order Fourier-product transversal, nor does it establish a general even-order theorem. It does not solve the original order10 100-ray 1-RQLS problem. The unrestricted even/Fourier question remains open in this work.
