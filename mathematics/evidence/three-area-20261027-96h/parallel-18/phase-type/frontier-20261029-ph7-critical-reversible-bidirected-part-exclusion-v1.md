# A critical PH7 realization needs a NON-REVERSIBLE bidirected cycle

**NEW ALL-TOPOLOGY CRITICAL-RATIO THEOREM CANDIDATE; written extension of the pinned no-two-cycle theorem plus an exact rational regression check of the cover identity.** Not independently reviewed; parent adoption, formal proof and novelty clearance are pending. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 04:46:25 PDT 2026**. Not an 8/9 existence/exclusion verdict and not a minimum-order claim.

## 1. Theorem

Let G be any critical realization: an irreducible seven-by-seven Metzler matrix of spectral bound0 whose characteristic polynomial contains `D(y)=y[(y+1)^2+8/9]^2` (the PH caller is the same separately supported irreducibility theorem, SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`, as in the girth-four and no-two-cycle candidates). Let F be the undirected graph on the seven states whose edges are the **bidirected pairs** `{i,j}` with `G_ij G_ji>0`.

Then F contains a cycle `i_1,i_2,...,i_k,i_1` (k>=3) that is **not reversible**:

    G_{i1 i2} G_{i2 i3} ... G_{ik i1}  !=  G_{i2 i1} G_{i3 i2} ... G_{i1 ik}.

In particular F is not a forest. This strictly extends `frontier-20261029-ph7-critical-no-two-cycle-exclusion-v1.md` (SHA256 `46659f60be21537f02d6ea76ceac3be2b89a7a55c3d2b1e8f249c7c315383745`), which is the special case of an empty F.

**Corollary (edge count).** A critical realization has at least **11** positive off-diagonal transitions. A non-reversible F-cycle of length k contributes 2k directed edges on k states; adding the remaining 7-k states to a strongly connected digraph requires at least (7-k)+1 further arcs (every ear of an ear decomposition with r new internal states has r+1 arcs). Hence at least k+8>=11 arcs.

## 2. Proof

**Reversible part.** Let `G2` keep the diagonal of G and exactly the off-diagonal entries `G_ij` with `G_ij G_ji>0`. Suppose, for contradiction, that every cycle of F is reversible. Choosing positive scalings along a spanning forest of F and using Kolmogorov's cycle criterion (path independence of the products of ratios `G_ji/G_ij`), there is a positive diagonal Dg with `S=Dg G2 Dg^{-1}` symmetric, off-diagonal entries `sqrt(G_ij G_ji)`.

`G2 != G`: otherwise G would be similar to a symmetric matrix and have real spectrum, while `-1+-i sqrt(8/9)` are eigenvalues. Since G is irreducible and `G2<=G` off the diagonal with equal diagonal, strict Perron-Frobenius monotonicity (applied to `G+cI>=0`) gives spectral bound `s(G2)<s(G)=0`. Thus `A:=-S` is real symmetric with eigenvalues `0<ut_1<=...<=ut_7`.

**Cover identity.** Call a directed cycle of G *one-way* if it uses at least one edge outside G2; every one-way cycle has length >=3 because both edges of a 2-cycle lie in G2. Splitting the cycles of each permutation into G2-cycles and one-way cycles gives

    det(yI-G) = sum_L prod_{C in L}(-w_C) * det((yI-G2)_{V\cup L}),

over sets L of pairwise vertex-disjoint one-way cycles, `w_C` the product of the entries of G around C. For every state set U, `det((yI-G2)_U)=det(yI+A_U)` because principal submatrices inherit the diagonal similarity. Collecting degrees >=3 (two disjoint one-way cycles cover at least six states):

    [y^6]=e1(ut),  [y^5]=e2(ut),  [y^4]=e3(ut)-W1,
    [y^3]=e4(ut) - sum_t w_t tr(A_{V\t}) - C4one,

where `W1>=0` and `C4one>=0` are the total weights of the one-way 3- and 4-cycles and `tr(A_{V\t})=sum_{i not in t} u_i`. The separately written script below verifies these identities EXACTLY on seeded rational examples, including a reversible bidirected triangle.

**Ky Fan.** For the real symmetric A, the sum of any four diagonal entries is at least the sum of its four smallest eigenvalues: `tr(A_{V\t}) >= ut_1+ut_2+ut_3+ut_4 =: S4(ut)`.

**Reduction.** Matching with `D(y)(y^2+py+q)` and the Perron facts p>0, q>0 for G give exactly the system of the no-two-cycle theorem with the rates replaced by `ut`:

    p=e1(ut)-4>0,  q=e2(ut)-4e1(ut)+74/9>0,
    E4(ut)=W1>=0,  E3(ut)-E4(ut)*S4(ut) = C4one + sum_t w_t[tr(A_{V\t})-S4(ut)] >= 0.

Sections 3-4 of the no-two-cycle theorem derive a contradiction from precisely these facts about seven positive real numbers (elimination of the largest, the imported girth-four `Qpol>0, Hpol>0`, the elementary f1<4 case, and the exact 1653-leaf residual cover). Nothing there uses that the numbers are diagonal entries. Contradiction. □

## 3. Actual check

`frontier-20261029-ph7-reversible-part-identity-check.py`, **75LF/3443B**, SHA256 `8b9366db18fbc14e509b0cca78fb4bc4887a3f6f9650b82792e44d4cc7102ebf`, builds seeded random rational 7x7 Metzler matrices (four with a bidirected forest, two with a Kolmogorov-balanced bidirected triangle plus a pendant pair), computes both characteristic polynomials exactly and enumerates one-way 3- and 4-cycles; it actually printed

    PASS: exact reversible-part cover identities on all seeded trials

It is a regression check of the written identity, not its proof. The algebraic core is the pinned no-two-cycle chain: checker SHA256 `6c88f6707f9af73b77de262b8704dabe1fafcf968ebe1a705234aee72960c93c`, residual certificate SHA256 `45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be`, stdlib replay SHA256 `abaa152c15444dbe7333465f65fc873533399366bfb9ad870f77281ec10a80a3`, and the imported girth-four certificate SHA256 `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8`.

## 4. Review targets and remaining gap

Review should check Kolmogorov symmetrization on cyclic F, the strict spectral-bound inequality, the one-way cycle cover identity and its coefficient extraction, Ky Fan for four diagonal entries, and that the no-two-cycle algebra uses only positivity of the seven numbers.

Open: graphs whose bidirected graph contains a non-reversible cycle (for example a fully bidirected triangle whose two directed 3-cycle weights differ). No witness, no 8/9 decision, no minimum-order statement. Historical holds and process findings are unchanged and are not premises.

END - a critical seven-state realization needs a non-reversible cycle of bidirected pairs, hence at least eleven transitions.
