# Three-syndrome direction planes: exact noncover census

**Status: WRITTEN with exact kernel enumeration, conditional on the pinned proper-subgraph inequality; independent scientific review pending.** Every three-state q=8 syndrome support has one of 174,251 two-dimensional direction planes after syndrome translation, as shown in `frontier-20261028-three-syndrome-affine-normalization-v1.md` SHA-256 `70c51a7d3dab9f2ac03e75a0aa6e6c99784557bf1c1178f6326b12d43c16c3fc`. Exactly **20,993** of those planes have nonconstant factor indices whose triangles fail to cover all ten vertices; the general syndrome-cover gate `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` therefore gives `Delta<=0` for any actual graph-FD law on any of these planes, including arbitrary probabilities and every affine translate.

| Number of varying factors | Noncover: `Delta<=0` | Cover: unresolved by this test |
|---:|---:|---:|
| 2 | 45 | 0 |
| 3 | 480 | 0 |
| 4 | 2,483 | 247 |
| 5 | 6,480 | 3,600 |
| 6 | 7,865 | 17,545 |
| 7 | 3,640 | 40,040 |
| 8 | 0 | 49,185 |
| 9 | 0 | 32,800 |
| 10 | 0 | 9,841 |
| **Total** | **20,993** | **153,258** |

The covering count is unresolved **by the noncover test**, not globally: seven explicitly certified equivariant-bicover planes also have no-gap candidate proofs, several conditional on the repaired two-syndrome theorem. The 20,993 count is separate and does not import that theorem; it does import the previously pinned nine-active-vertex proper-subgraph entropy certificate and conditional tensorization.

`frontier-20261028-three-syndrome-cover-census.py` SHA-256 `4172221aef0376414ae4c57d41940d469088738c68290e27693d0de2a096e5f8`, receipt SHA-256 `62a9b65a63d7cc72a966754f7c358c3a1a5018fd55da1a416a04df922c579303`, enumerates each plane exactly once via ordered nonzero masks `a<b<a xor b`, reconstructs its varying-factor union and triangle vertex coverage, and compares to the independent Gaussian-binomial plane count. A formal proof, independent scientific review and novelty clearance are not claimed; the unrestricted guessing-number problem remains open.
