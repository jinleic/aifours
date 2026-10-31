# The positive core's 6D complement passes the full elementary squared-overlap relaxation

**WRITTEN + EXACT-RATIONAL-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 01:29:11 PDT 2026. This is a *method barrier and reformulation*, not a construction of 6D rays or a proof that the core lifts.

## Necessary conditions for a genuine complement

Let G be the specific 6-regular, 15-vertex graph G6 from the positive Pauli 4D core in `frontier-20261029-pauli60-positive-tripartite-4d-core-v1.md`, SHA-256 `734e0ff4397534dd8e486f9375984ddb6b3bcbdc51530e57505621726571af96`. A genuine complement has one rank-one projector `P_e` on C6 per edge, with the six edge projectors at each vertex summing to I6. Define its real squared-overlap matrix `X_ef=tr(P_e P_f)=|<v_e,v_f>|²`. Necessarily:

- X is symmetric positive semidefinite, has diagonal 1, entries in [0,1], and real rank at most 36, the dimension of the real vector space of Hermitian 6×6 matrices;
- `X_ef=0` when distinct edges e,f share a vertex, and `X_ef<1` for distinct rays;
- for each edge e and each vertex v, `sum_(f incident to v) X_ef=1`.

Conversely these conditions do **not** state that X factors into 6D rank-one projectors. They are only necessary.

## Exact counterexample to this relaxation as an obstruction

There exists a **rational 45×45 matrix X** satisfying *all* of the above necessary conditions, with **rank exactly 31**. It even has `0<X_ef<1` whenever distinct edges e and f do not share a vertex, so the relaxation exhibits precisely the required adjacency zeros, with no accidental extra zeros. Every row sums to 15/2. Hence PSD, nonnegativity, 36-dimensional Hermitian-space rank, pairwise orthogonality, distinctness inequalities and all 675 context-sum identities cannot, by themselves, exclude a 6D complement for this fixed G.

The witness is `frontier-20261029-g6-overlap-relaxation-witness-v1.json`, SHA-256 `ab38d176f88cfab17307e31ae75b254a7ad3790d9bf097e5afbdb7f79ee64c01`. It records the exact edge order, a common denominator 20000 and all 2025 integer numerators. The exact independent replay `frontier-20261029-g6-overlap-relaxation-replay-v1.py`, SHA-256 `6fa7ec9e487a48a4e1312ec164aae371e800aaba5cd54d5e18106a79b68b8557`, rebuilds G from the original-vector-replayed core `frontier-20261029-pauli60-tripartite-core-independent-v1.json` SHA-256 `ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd`. It checks every entry and context sum, then uses rational symmetric Schur complements to certify 31 strictly positive pivots and 14 zero residual rows. Its result `frontier-20261029-g6-overlap-relaxation-replay-v1.json` has SHA-256 `2d172874b3090bc844378f6ee9fff97ae5d9a46f8ab6be296926d6301da5017f`, **PASS** at 01:29:11 PDT. Floating linear algebra was used only to discover the rational witness; every stated property is checked exactly.

## Lovasz-theta value and quantum-matching context

Let H=L(G) be the line graph on the 45 edges of G, and let B be the 15×45 unsigned vertex-edge incidence matrix. In the standard theta primal, maximize `<J,Y>` over real PSD Y with trace 1 and zeros on H's edges. The witness `Y=X/45` is feasible and has value 15/2.

For the matching upper bound, use `B^T B=2I+A_H` and `B^T 1_15=2 1_45`. Therefore

`Z=(15/4) B^T (I_15 - J_15/15) B = (15/2) I_45 + (15/4) A_H - J_45 >= 0`.

For every feasible Y, `<Z,Y>=15/2-<J,Y> >= 0`. Thus **theta(L(G))=15/2 exactly**. Ordinary line-graph Lovasz theta, even augmented by this witness's entrywise nonnegativity, strict nonedge overlaps and rank-at-most-36 condition, cannot settle the 6D rank-one lift.

More generally the core's edge projectors form a symmetric projector-valued quantum perfect matching. [Cui, Mančinska, Nezhadi and Roberson, Theorem 6.4](https://arxiv.org/html/2502.05136v1#S6.Thmthm4) relates the unrestricted-projector version to a maximum projective packing of the line graph. Our target is narrower: all 45 projectors must be **rank one in one common C6 and represent distinct rays**, followed by compatibility with the other 25 cells. Their theorem does not supply such projectors here. The theta equality and rational X do not even assert an unrestricted projective packing.

## Next mathematical gap

A decisive source-free argument must use constraints not encoded above—for example the existence of a Hermitian rank-one Gram factorization in dimension 6, phases of triple/Bargmann products, or the simultaneous linear dependencies of actual context vectors. Alternatively, an explicit set of 45 actual C6 rays satisfying G's incidence would be a partial lift but still not a complete 1RQLS10. Independent review is required; no novelty claim is made.
