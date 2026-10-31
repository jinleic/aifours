# Mixed real-sign and cubic-phase 6D rays cannot complement the positive Pauli 4D core

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 01:21:26 PDT 2026. This is a finite-source, fixed-core obstruction, not a general 1RQLS10 no-go.

## Exact claim

Let `omega=exp(2 pi i/3)` and let S be the union of projective rays represented by nonzero vectors in **either** `{0,1,omega,omega²}^6` or `{0,1,-1}^6`. Every source ray must lie in one of those two alphabets after its own projective rescaling; different rays may choose different alphabets. A single common unitary change of coordinates is also allowed.

For the positive 4D Pauli parity core in `frontier-20261029-pauli60-positive-tripartite-4d-core-v1.md` SHA-256 `734e0ff4397534dd8e486f9375984ddb6b3bcbdc51530e57505621726571af96`, take its 15 contexts in the certified 5+5+5 families. Let G6 be the degree-6 complement of its 4D context-intersection graph in K5,5,5. **There is no assignment of 45 distinct S rays to the edges of G6 such that each vertex's six incident rays form an orthonormal basis.** Thus that 4D core has no 4+6 balanced-quotient parity-core completion from this mixed source.

This is stronger than testing the real-sign and cubic sources separately: any particular basis or entire putative completion could mix rays from both subalphabets. It is stronger than the prior unverified bounded union search, which timed out and established no no-go. The balanced family partition is unique up to relabeling, by the two coloring checks cited in `frontier-20261029-pauli-core-fullcubic6-complement-no-go-v1.md`.

## Exact finite proof

Projective normalization yields **1666** rays and the exact orthogonality graph has **3386** six-ray bases. Coordinate permutations and complex conjugation generate 45 source-basis orbits; 43 orbit representatives can have at least six distinct single-ray-intersection partners, as every target context requires. The search fixes one target vertex at each viable representative and assigns source bases to the other vertices, requiring single-ray intersections exactly on target edges, no intersection otherwise, and no source ray in three contexts.

At each assigned target vertex its six rays must match its six neighbors bijectively. For a subset of unmatched rays, the union of unassigned neighboring vertices whose current candidate domains contain them must have size at least the subset's size. The domains deliberately over-approximate possible completions. A literal Hall-deficient subset therefore certifies rejection; other rejection leaves have an empty domain. Branches enumerate **every** allowed next basis, and all viable root representatives are covered.

- Producer `frontier-20261029-mixed-union6-complement-proof-v1.py` SHA-256 `a4f419001d26969deb4357b992b8ff04785a250cdfa7113df85a10d1083dfb25`; summary `frontier-20261029-mixed-union6-complement-proof-v1.json` SHA-256 `5e733cabdb79e2ec9048cf4455616aa34f94e5e939b3c6771c8585a4e9f71df8`.
- Complete literal forest `frontier-20261029-mixed-union6-complement-proof-v1.json.gz` SHA-256 `0128ff598bdc0cba1323fad9508f8c5be9e40eaaf1820afe8f611abc7a33eeaa`: **1025837** nodes.
- Independent replay `frontier-20261029-mixed-union6-proof-replay-v1.py` SHA-256 `6945255dac9e1f93307f5d7e0cc2be1ebcc87de8f7b29896c1b8a28b568f4861`; result `frontier-20261029-mixed-union6-proof-replay-v1.json` SHA-256 `1198148a68bc96a2441aea338dd6bcfdcb16bb0256a47f6de50287c69f1869c5`, **PASS** at 01:21:18 PDT.

The replay regenerates the two ray families by support and relative phase, checks original inner products in the different exact Z[omega] basis, enumerates all six-cliques using pivoted Bron–Kerbosch, rebuilds all source-basis orbits with a different generating set for coordinate permutations, reconstructs G6 from `frontier-20261029-pauli60-tripartite-core-independent-v1.json` SHA-256 `ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd`, and checks every proof-tree child and every Hall subset. The forest comprises **76468** branches, **806298** Hall-deficient leaves and **143071** empty-domain leaves. This is an exact computer-assisted certificate; it is not formal-kernel verification or external review.

## Limits

This excludes only the stated source, up to one common unitary, paired with this particular positive Pauli 4D core. General 6D complex vectors, other 4D cores, irreducible 10D cores and unrestricted 1RQLS10 remain open. In particular, no incompatibility between arbitrary real and cubic source rays is asserted beyond this fixed incidence. Full independent mathematical review of the finite certificate and its interpretation remains required; no novelty claim is made.
