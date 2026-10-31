# Non-Butson odd tensor lifts: all local source orders excluded

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:03:02 PDT 2026**. This strictly extends the fixed-local-order theorem `frontier-20261028-t8b-odd-tensor-no-transversal-v1.md` SHA **980d8cfa9adfd1d9d4969e6c48c4ea5ab95d61cc643012673ed1eb648af501de**. It addresses infinitely many even orders but is NOT an arbitrary-K even-order theorem.

## 1. Claim and one mod-4 invariant

Take the exact non-Butson T8B point K8 from `frontier-20261028-t8b-generic-and-explicit-no-transversal-v1.md` SHA **bb279c42f4e76a77e9cbcbf980501af140969492d14e174fd0a98f2ea9d69ef9**. For EVERY source-row permutation pi of K8 and EVERY odd positive m, the CRT-aligned order `n=8m` Fourier-product QLS based on `K8^pi tensor F_m` has NO orthogonal transversal, including repeated rays. Arbitrary row/column phase gauges and affine global coordinate reindexings are harmless; arbitrary source permutations that MIX the two tensor coordinates are not included.

For a local eight-cell ONB clique Q, write `a_r(Q)` and `b_c(Q)` for its number of cells in local row r and local column c. The exact all-order census proves, for EVERY local K8 source ordering and EVERY local8 ONB clique,

`a_0(Q)+a_1(Q)+2 b_0(Q)+2 = 0 mod4`.                            (1)

If an 8m transversal existed, its cells split into m mutually orthogonal F_m-ray groups, each a local8 ONB clique (as in the predecessor's CRT proof). Since every global row and column occurs once,

`sum_Q a_0 = m`, `sum_Q a_1 = m`, `sum_Q b_0 = m`, `number of groups=m`.

Summing (1) over those m groups gives `6m=0 mod4`, impossible for odd m. This does not require any classification of the local cliques into rows, columns or rectangles.

## 2. Exhaustive exact all-order verification of (1)

A local cyclic coordinate rotation moves source row0 to coordinate0 without changing any ray orthogonality, so the 5040 normalized source orders cover all8! permutations. For each order, the local64-vector graph is computed exactly, and ALL eight-cliques are enumerated; dimension8 prevents larger orthogonal cliques.

`frontier-20261028-t8b-all-row-orders-tensor-parity-v3.cpp` SHA **1fa3ab83af180d4eeef48d49293dfd4b151b3201dbef0aa74afac925ba90594b**, result SHA **e126f743fa0fa9750c9df5f28bd0645bddf06f02ddc57d426dba0a7e5752094b**, uses integer `Q(zeta8) tensor Q(zeta6)` arithmetic and increasing-vertex bitset DFS: **5040 orders, 84096 cliques, maximum24 per order, 0 failures** of (1), 4223616 DFS nodes.

Independently written `frontier-20261028-t8b-all-row-orders-clique-replay-v1.cpp` SHA **1034f8ecd5ebad5569aaad90726788a632005fb2edbe3968762c392b8c7df3d7**, result SHA **20e0faa31fcac2cee418be00817f42f1a256f1ad0175551839a24b4aeae540f0**, uses exact `Q[zeta24]/(x^8-x^4+1)` arithmetic and pivoted Bron–Kerbosch: same5040/84096/0, 1594736 nodes. `frontier-20261028-t8b-all-row-orders-coverage-v1.py` SHA **ad4b4aaf8944858fa63ee1546ccd702757418bdf9aef0a81ce07aecdeea6b3e9**, result SHA **98cf90d10a78c003e064f79962e3cc4162e8603e1a649f3ca7798208c8397ccf**, compares the two ordered per-source-order streams and confirms every clique count and every replay congruence. The initial F2-only incidence screen rejected4464 orders but left576; the stronger directly checked mod4 congruence rejects ALL orders. No conclusion is drawn from the incomplete F2 screen alone.

The factorization `K8 tensor F_m` retains K8's gauge-invariant nonroot cross-ratio, so these examples are outside all finite Butson monomial classes. The programs independently regenerate cliques, but share the source K8 transcription and mathematical caller; they are not a formal or external-model review.

## 3. Boundary

The result concerns the explicit local K8, its local row permutations and odd CRT tensor factors. It does not include arbitrary K8, all Hadamards at dimensions8m, global coordinate mixings, other even orders or unrestricted QLS10. The source-vector algebra, clique enumeration, mod4 implication and CRT caller require independent full review.
