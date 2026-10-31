# A critical PH7 realization requires an IMBALANCED directed triangle

**NEW ALL-TOPOLOGY WRITTEN CANDIDATE, independently reviewed prerequisites not automatically extended to this application.** MathResearch96h-2. This strictly strengthens `frontier-20261028-ph7-critical-mandatory-triangle-v1.md`, SHA256 `d2437a46148569e7f43c76853331132a3481c20cff06317de57e538c92348612`, using the SAME six-rate exact positivity and nonnegative-boundary certificate. No unrestricted PH7 existence/exclusion is claimed.

## Claim

For an actual PH representation using at most seven states at `z=8/9`, there must exist three distinct states i,j,k for which

    T_ij T_jk T_ki != T_ik T_kj T_ji.              (IMBALANCE)

A missing directed edge has rate0. In particular at least one orientation has positive product, so a directed triangle exists. The graph may otherwise have arbitrary 2-, 3-, 4- and longer cycles, any number of edges, and arbitrary initial/exit support.

The identity/inequality of the two products is invariant under positive diagonal similarity around the cycle and under positive time scaling. Thus it can be stated directly for the actual PH generator T. The SCC/Perron PH reduction and exact zero-boundary Q/H positivity are the explicit dependencies of the mandatory-triangle source, not independently re-proved by an assumed numeric result.

## Proof

Suppose all triples of distinct states have equal forward and reverse triangle products. In the normalized irreducible spectral Metzler matrix G of spectral bound0, form the symmetric geometric-mean matrix

    S_ii=G_ii,        S_ij=sqrt(G_ij G_ji).

The Perron left/right plus Cauchy argument reproduced in the mandatory-triangle source proves `-S` is positive semidefinite. Let its seven real nonnegative eigenvalues be lambda_i.

For each unordered three-vertex set, let A and B be the two oriented triangle products in G. Its two oriented S products sum to `2 sqrt(A B)`. Under the assumed equality A=B, the G and S triangle contributions coincide, including the case A=B=0. Two-cycle products are identical by definition. Thus the actual characteristic coefficients at y6,y5,y4 agree for G and S. This conclusion permits any number of triangles; it does not assume they are absent.

At y3, triangle terms multiply the sum of the four outside diagonal factors. For each given triangle, this outside factor is the same in G and S, and the balanced-triangle contribution still agrees. Disjoint 2+2-cycle products agree. For every unoriented 4-cycle, the two G orientation products sum to at least the two S products by AM–GM, including one-way edges; all such terms have negative determinant sign. Therefore

    [y^j]det(yI-G)=[y^j]det(yI-S) for j=6,5,4,
    [y^3]det(yI-G) <= [y^3]det(yI-S).              (CMP)

No other permutation support can affect these coefficients.

The target characteristic factor and irreducibility give hidden quadratic `Q=y²+p y+q` with `q>0`. By(CMP), the elementary symmetric functions of the nonnegative lambda_i satisfy exactly the system(E4=0,E3>=0) of the mandatory-triangle proof. That proof's exact Qpol/Hpol certificate, including the separately replayed ALL nonnegative-boundary faces, forces E3<0 whenever q>0. Contradiction. Hence at least one triangle has unequal opposite orientation products, proving(IMBALANCE). □

## Review boundaries

The exact certificate and zero-boundary wrapper are pinned in the mandatory-triangle source; no new numerical check or witness is claimed. A reviewer must separately check the extension from absent triangles to equal forward/reverse triangle products at BOTH y4 and y3, the complete 4-cycle comparison and invariant under similarity. It is not enough to cite the already reviewed no-2/no-3 case.

The theorem does NOT rule out imbalanced triangles, multiple triangles, 2-cycles or 4-cycles; in particular it does not decide PH7 at8/9 or establish minimum8. No novelty, formal/Lean/kernel, cross-vendor acceptance, historical hold admission or process repair is claimed.

END — any critical PH7 representation must contain at least one strictly imbalanced directed triangle.
