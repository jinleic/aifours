# Exact qubit–qutrit source cannot complement the positive Pauli 4D core

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 01:19:55 PDT 2026. This excludes a specific finite 6D source for one fixed 4D parity core; it is not a no-go for unrestricted 1RQLS10.

## Statement and explicit 6D source

Use the 30-ray, 15-basis 4D Pauli core of `frontier-20261029-pauli60-positive-tripartite-4d-core-v1.md` (SHA-256 `734e0ff4397534dd8e486f9375984ddb6b3bcbdc51530e57505621726571af96`). Let its 15 contexts be in the certified three families of five and let **G6** be the complement of its degree-4 context-intersection graph inside K5,5,5. Thus G6 has 15 vertices and is 6-regular. The only balanced tripartition of this 4D graph is unique up to relabeling the families, as documented in `frontier-20261029-pauli-core-fullcubic6-complement-no-go-v1.md`.

Let `omega = exp(2 pi i/3)` and `zeta = exp(2 pi i/12)`. In C2 take the three ordered pairs `(e0,e1)`, `((1,1),(1,-1))`, and `((1,i),(1,-i))`. In C3 take the standard basis and the three ordered bases whose b-th vector is `(omega^(a t^2 + b t))_{t=0,1,2}`, with a,b in `{0,1,2}`. The vectors within each displayed basis have equal norms. Define the finite projective source S to contain:

1. all product rays `q tensor v`, with q from one of the three C2 bases and v from one of the four C3 bases; and
2. all rays `q0 tensor v + zeta^k q1 tensor w`, where `(q0,q1)` is one of the ordered C2 bases, v and w are distinct members of the same C3 basis in either order, and `0 <= k < 12`.

S has exactly **936** distinct rays (72 of them product rays), and exactly **16560** orthonormal six-ray bases. The remaining 864 rays in this source have Schmidt rank 2 with equal nonzero Schmidt coefficients.

**Claim.** There is no assignment of 45 distinct rays from S to the edges of G6 such that the six rays incident to each vertex form an orthonormal basis. The claim also holds for any single unitary image of S. Consequently this particular positive Pauli 4D core cannot be completed to a 4+6 balanced-quotient 75-ray parity core using this 6D source.

## Certificate and exact replay

The source orthogonality graph and its six-cliques were enumerated exactly over the cyclotomic field. Local qubit and qutrit Clifford actions and global complex conjugation generate 30 source-basis orbits; the checked generators permute S and preserve orthogonality. Every possible image of a fixed target vertex is represented by the checked viable orbit roots. The finite search then assigns distinct source bases to target vertices: target neighbors must share exactly one source ray, non-neighbors none, and a ray cannot occur at a third context.

The search additionally uses the following **necessary** Hall condition. At any assigned vertex, its six basis rays must be matched bijectively to its six target neighbors. Already assigned neighbors determine some ray matches. For every subset of the remaining rays, the union of still-unassigned neighboring vertices whose current source-basis domains contain that ray must have at least the subset's size. These domains are over-approximations, so a recorded Hall deficiency really excludes every completion. Other leaves have an empty source-basis domain. Every branch lists all allowed next-basis choices; no satisfactory complete assignment occurred.

- Producer: `frontier-20261029-qubit-qutrit-6d-complement-proof-v1.py`, SHA-256 `ab1deb4583dff8a25643b0ce43f2f9be06b8aea08400db1b4cb845845141d6d9`.
- Full literal proof forest: `frontier-20261029-qubit-qutrit-6d-complement-proof-v1.json.gz`, SHA-256 `3e50b31d20466bea87e6e2f981f0a5964d36699706132a198e420c519505efe8`. The summary `frontier-20261029-qubit-qutrit-6d-complement-proof-v1.json` has SHA-256 `8ac7422b5ff3aa6054458eb537b02b286dc5082655d908853764a2c1181d40fc`.
- Independent replay: `frontier-20261029-qubit-qutrit-6d-proof-replay-v1.py`, SHA-256 `6604ff3dcc16c72e0f7a5b63939bd82cdaba7c893c45ec1057bb2a27f007c44d`; output `frontier-20261029-qubit-qutrit-6d-proof-replay-v1.json`, SHA-256 `5867dde7bba861612184cb9d9321767aa5d94f2d7ac77da92c299944b3e73be3`, **PASS** at 01:19:48 PDT.

The replay independently generates the declared source, converts producer coordinates to the different exact basis `1,omega,i,i omega` of Q(i,omega), recomputes all original vector inner products, finds all bases by pivoted Bron–Kerbosch, reconstructs the actual source symmetry permutations, and rebuilds G6 from `frontier-20261029-pauli60-tripartite-core-independent-v1.json` SHA-256 `ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd`. It checks every one of the **298702** literal proof nodes: **25186** exhaustive branches, **231240** independently verified Hall-deficiency leaves, and **42276** empty-domain leaves, including all root-orbit coverage. This is an exact computer-assisted finite certificate, not a formal kernel proof or external review.

## Limits and next issue

This source includes entangled as well as product 6D rays, so the obstruction is not a product-basis-only observation. It does not exclude other 6D phases or amplitudes, a different 4D parity core, an irreducible 10D core, or general 1RQLS10. The explicit completeness and Hall replay need independent human review; no novelty claim is made.
