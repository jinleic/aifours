# Exact source-independent q3 square on 2×2×2 output support

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable proof; UNREVIEWED.** This is a source-independent original-q3 theorem for a substantial structured subclass, including arbitrary complex rank≤2 operators whose range has local support dimension≤2 at every site. It also applies to higher-rank matrices with the same output support. It is not the original full rank≤2 theorem: a general rank2 range need not have these local support bounds. No source/certificate, global equality, novelty, parent/f62/f153, human/family/formal/Lean or physical-operational acceptance is claimed.

## 1. Statement and exact equality set on the supported class

Let `H=(C⁴)^tensor3`. For each site choose an arbitrary two-dimensional subspace `E_i⊂C⁴`, and let P_i be its orthogonal projection. Denote by `L_E` the vector space of all complex operators C on H satisfying

`(P_1⊗P_2⊗P_3) C = C`.                                            (1)

No assumption of Hermiticity, positivity, product form or operator rank is made. For X∈L_E let

`D_i^E(X) = P_i ⊗ Tr_i X`, `R_i=Id−D_i^E/2`,                          (2)

where P_i is inserted in its original physical site and the traces are unnormalized. The other output sites of `Tr_i X` retain their prescribed E_j support. Then

`q3(C) = || R_1 R_2 R_3 C ||HS² >= 0`                                 (3)

for **every** C∈L_E. Moreover the complete equality condition on L_E is

`q3(C)=0  iff  R_1 R_2 R_3 C=0`
`iff C∈ker R_1 + ker R_2 + ker R_3`,                                  (4)

with `ker R_i = { P_i⊗X_i : X_i has output support E_j at both remaining sites }`. The three summands need not have a unique decomposition. Intersecting this exactly described linear equality space with rank≤2 gives the equality set within the supported original-rank domain; no parameterization of all its rank≤2 members, or of the global equality set, is asserted.

If actual local output support has dimension0,1 or2, choose a two-dimensional extension E_i and (3)–(4) still apply. q3(C)=q3(C†), so the same conclusion holds when the local **input** support (equivalently, output support of C†) has dimension≤2 at every site. Because (1) has an eight-dimensional output space, its operators have rank at most8, but no rank≤2 hypothesis enters the proof.

This class includes every `C=|u><x|+|v><y|` with u and v arbitrary product vectors and x,y **arbitrary, possibly entangled**, by taking `E_i=span{u_i,v_i}` and extending to dimension2 as needed. It also includes the entire two-product-rank-one class and the explicit nonproduct equality families in `frontier-20261028-d4-two-product-rank1-operators-v1.md`, SHA256 `73dcfa39a5a1e2f52794cae41985d4c7cae294f37d186d28903b7647b7f16f46`. These inclusions do not imply that every rank2 C has the support property.

The square is valid only under the explicit support constraint (1), with fixed support-dependent P_i. It is not an unrestricted polynomial-SOS representation on arbitrary rank-two factors and does not contradict the parent-adopted unrestricted-factor polynomial-SOS obstruction.

## 2. Written proof of the exact square

Use the Hilbert–Schmidt inner product. Each `D_i^E` maps L_E to itself. For X,Y∈L_E,

`<X,D_i^E Y>HS = <Tr_i X,Tr_i Y>HS = <D_i^E X,Y>HS`.               (5)

The first equality uses `P_i X=X` at site i; the equality holds even though the input legs of X,Y are unrestricted. Thus D_i^E is self-adjoint. Also, because `Tr P_i=2`,

`(D_i^E)² = 2 D_i^E`.                                                 (6)

For different sites, `D_i^E` and `D_j^E` commute: their insertions and partial traces act on distinct tensor factors. Hence every `R_i=Id−D_i^E/2` is a self-adjoint orthogonal projection, and their product R is also a self-adjoint orthogonal projection.

For every subset S of the three sites, factor insertion and the support condition (1) give

`<C, (Π_(i∈S) D_i^E) C>HS = ||Tr_S C||HS²`.                         (7)

Expand the product R with coefficients `(−1/2)^|S|` and use (7):

`<C,R C>HS = ||C||HS²−(1/2)Σ_i||Tr_i C||HS²`
`             +(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|² = q3(C)`.

Because R is an orthogonal projection, `<C,R C>=||R C||HS²`, proving (3).

For commuting orthogonal projections, the simultaneous spectral decomposition gives `ker(R_1R_2R_3)=ker R_1+ker R_2+ker R_3`. Finally `ker R_i=range D_i^E`: one direction follows from (6), and conversely R_iX=0 implies `X=D_i^E X/2`. The range consists exactly of `P_i⊗X_i` with the other output support constraints, since `D_i^E[(P_i/2)⊗X_i]=P_i⊗X_i`. This proves (4).

## 3. Scope and provenance

The proof is purely the original trace algebra on a precisely defined output-support subspace; it does not invoke the public-source identity, corrected multipliers, a numerical q3 state, or an executable checker. It does not use or reconstruct the elected HELD/ZERO/NONINPUT episode or its guidance. The prior public full-target Werner claim retires new-discovery status; no novelty or literature-exhaustiveness claim is made. Previous process/held findings and frozen f153/f62 review scopes remain unchanged. Most importantly, (3) is not asserted for rank2 C whose output or input is not contained in a 2×2×2 product subspace.
