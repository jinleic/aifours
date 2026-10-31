# Barycentric simplex covers exclude the last seven cyclic spectra

**WRITTEN + EXACT-CYCLOTOMIC-CERTIFICATE-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 04:16:39 PDT 2026. This closes the seven conditional cyclic spectral classes left by `frontier-20261029-cyclic15-rank1-boxcover-2-no-go-v1.md` SHA-256 `e37ca94bd18d976712df86f7256e2c03da2a4a15462fc7c8acb095ed88076d74`. It is a **cyclic-unitary** exclusion only.

## Result

None of the spectral representatives

`(0,1,2,3,6,8)`, `(0,1,2,3,6,10)`, `(0,1,2,4,6,7)`, `(0,1,2,4,6,10)`, `(0,1,2,4,6,13)`, `(0,1,2,5,7,8)`, `(0,1,2,5,7,11)`

can occur in a 45-distinct-ray C6 lift of `Circ(15;±2,±5,±7)` with a unitary implementing translation. These have U^5 multiplicities `(3,2,1)`. In each case p in the singleton U^5 group equals 1/3. The populations of the 3- and 2-element groups lie in the open product of a 2-simplex and a 1-simplex after writing `p_j=x_j/3`, with x summing to 1 in each group.

## One additional necessary test: kernel/self compatibility

Keep the notation of `frontier-20261029-cyclic15-two-plane-normal-form-v1.md` SHA-256 `b2b0ca5e4d1242c9849bc7d77b4f8183e59a6f3bdef62e8606989b617a8849e7`. Let H be the 2×2 cofactor matrix of the three cross matrices `C_0,C_(-7),C_2`, as in the rank-one packet. Let

`M_x=N_L† diag(lambda^(-2)/p) N_L` and `M_y=N_M† diag(lambda^(-7)/p) N_M`.

At a solution, if H≠0 then `H=kappa*conjugate(z)w^T` with kappa≠0. Every nonzero column of H is proportional to `conjugate(z)`, and every nonzero row is proportional to `w^T`. Therefore the four quantities

`G_x^(b)=H[:,b]^T M_x conjugate(H[:,b])`, `G_y^(a)=conjugate(H[a,:]) M_y H[a,:]^T`

must all vanish: a nonzero column or row gives the paired self-orthogonality `z†M_xz=0` or `w†M_yw=0`, and a zero one gives zero trivially. If H=0 they also vanish. After multiplying by `(product p)^3`, each is a polynomial with coefficients in Q(zeta_15). Strict positivity of `Re(e^(-i theta) conjugate(ref) G)` for a fixed reference coefficient and rational theta proves `G≠0`, excluding every solution at those populations.

## Complete exact cover

For every class, the product of the 2-simplex and 1-simplex is tiled by midpoint-subdivided sub-simplices. On each sub-simplex the certificate substitutes barycentric coordinates and proves one of four obstructions:

1. a signed nonzero cross-plane determinant (`frontier-20261029-cyclic15-crossplane-38-no-go-v1.md` SHA-256 `0a4bd44d9dca934397153be9547e029b6e171677f0690c9862e6262293d06bd8`);
2. a positive-definite v2 or v7 self-plane compression (`frontier-20261029-cyclic15-selfplane-3-no-go-v1.md` SHA-256 `f4f22317a1d497473b7767ef84924da11fcd018e47fad8be084618cb21f37479`);
3. a nonzero rank-one cross-kernel discriminant (`frontier-20261029-cyclic15-rank1-boxcover-2-no-go-v1.md`);
4. a nonzero kernel/self compatibility polynomial G above.

All nonzero expanded coefficients are strictly positive. For every face of each sub-simplex whose relative interior lies in the open population domain, some positive monomial survives, so the inequality is strict there too. There are 151 regions: 54 cross, 58 self-plane, 16 rank-one and 23 G certificates.

## Exact evidence

- Discovery-only plan: `frontier-20261029-cyclic15-simplex-cover-plan-v1.json` SHA-256 `5ebe39d3408cf9cef8b384868e3fe6e3f29d3032336388c73c60c5c93cbe734b`.
- Producer: `frontier-20261029-cyclic15-simplex-cover-proof-v1.py` SHA-256 `0041359241855da2bc8456770f532a90eb29412f7b2144fc198a55c28b5e81cf`, with complete exact certificate `frontier-20261029-cyclic15-simplex-cover-proof-v1.json.gz` SHA-256 `9c7914fb7bbd1e89ff9c423fb4b65e17f1c604a88a4ed38bfb48550580c6b29d`.
- Separate same-owner replay: `frontier-20261029-cyclic15-simplex-cover-replay-v1.py` SHA-256 `db801ebc2dbc4031c975c78c7b1d6c4306fcc5850c988c9cd3af11b6ee0225b3`; result `frontier-20261029-cyclic15-simplex-cover-replay-v1.json` SHA-256 `8b9c44196efeffa61de45c6648ba072941321cc2adca90d4506ac6dac9bb20d3`, **PASS** at 04:16:38 PDT.

The replay rebuilds all four polynomial families in the different exact basis `1,omega,eta,omega eta` over Q(sqrt(5)) and recomputes pivots. It re-expands every sub-simplex and compares every stored coefficient, checking **20367** strict signs with rational trigonometric enclosures. It also checks the face condition and tiling: exact region measures sum to the full product measure, and every pair is separated by an interval endpoint or a triangle edge line.

## Boundary

This is conditional on the cyclic reduction chain summarized in the companion synthesis and still requires independent written and certificate review. It does **not** exclude noncyclic 6D complements, other 4D parity cores, irreducible 10D cores, or 1RQLS10. No formal-kernel verification or novelty clearance is claimed.
