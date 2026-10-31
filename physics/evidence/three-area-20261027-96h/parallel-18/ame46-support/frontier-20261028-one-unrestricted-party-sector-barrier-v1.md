# One unrestricted local GL(6) plus three GL(2)⊕GL(4) factors: exact 60 support floor

Owner **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:46:39 PDT 2026`**, not an exact file-write/completion/runtime clock. **WRITTEN author candidate, exact source-sector checks cited below; unreviewed, not a global AME theorem or novelty certification.**

## 1. Result

Let T be the specific published real 60-term AME(4,6) tensor in [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), in the verified reference product basis. Put `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}` at each party.

Choose ANY one party a. Let its local transformation be an arbitrary `V_a∈GL(6,C)`, with NO requirement to preserve H or K. At each of the other three parties r, take arbitrary `V_r=A_r⊕B_r`, with `A_r∈GL(2,C)` on H and `B_r∈GL(4,C)` on K. Then

`support((V_1⊗V_2⊗V_3⊗V_4)T) ≥ 60`.                                          (1)

Identity attains60. Thus this restricted orbit's exact support minimum is60. The statement is valid for arbitrary complex invertibles; the physical case is one arbitrary U(6) and three arbitrary U(2)⊕U(4) unitaries. Nonunitary maps do NOT in general preserve AME, so no nonunitary output is called an AME witness.

**Necessary condition for a sub-60 LU in this ONE orbit:** for at least TWO parties, the image of H under the local unitary is not a coordinate 2-plane in the output basis. If at least THREE parties mapped H to coordinate 2-planes, output monomial permutations would carry those planes back to H, preserving support; unitarity then makes those three factors block diagonal, so (1) applies to the remaining unrestricted party. This is a stronger necessary condition than the previous all-block-diagonal theorem. It does not say two such non-coordinate images suffice.

## 2. Exact source decomposition

The source support contains:

- one `P` sector with zero H indices and twelve terms;
- six `E_ij` sectors with H indices exactly in the pair i,j, eight terms each;
- no terms with one, three or four H indices.

For P, ANY 2|2 flattening has rank12: the12 source terms occupy distinct flattened rows AND distinct columns, with nonzero coefficients. For every E_ij, choose the cross flattening `(H_i,K_k)|(H_j,K_l)`, where k,l are the other two parties. The four source spectator K-index pairs form a matching and each corresponding H_i×H_j matrix is invertible2×2; the cross flattening is thus a direct sum of four such blocks and has rank8.

These are exact source facts, not assumed from the AME equations alone. The finite source certificate is `frontier-20261028-u2u4-sector-flattening-check-v1.json`, SHA256 `6b7d2bfa0e686a2a68aa70787adea4c0ff72e8149c575f9b97dec576154e1383`; it checks all six P flattened-row/column matchings and every E spectator matching/active block. Code SHA256 `2ec8a703efe0800d645808eaf70baed55e63ecc726207b2323eb6502f1574baa`. The complete transcribed tensor is `frontier-20261028-pandya-table-v1.txt`, SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`, whose normalization/all six marginals were checked separately as recorded in `frontier-20261028-two-party-orbit-obstruction-v1.md` SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`.

## 3. Seven sectors remain distinguishable without restricting party a

Partition ONLY the OTHER THREE parties into H/K coordinate subspaces. Their eight possible H/K patterns are mutually disjoint in the final product basis. The source tensor occupies exactly seven:

- a pattern with **zero H indices** among those three contains P and no E sector;
- each of the three patterns with **one H index** among those three contains exactly the E sector whose active pair consists of that H party and a;
- each of the three patterns with **two H indices** among those three contains exactly the E sector whose active pair is those two H parties;
- the all-three-H pattern is empty.

This is a one-to-one classification of the SAME seven source tensors. The unrestricted V_a may mix H and K on party a, but it cannot mix patterns of the OTHER three parties. Their block-diagonal transformations preserve those patterns. Therefore the seven output supports remain pairwise disjoint even when V_a does not preserve H/K.

## 4. Each output sector retains its source flattening rank

Take any of the seven source sectors and its 2|2 cut from §2. Apply the SAME four local transformations to it. In that flattening, the output matrix is the source matrix multiplied on each side by the appropriate Kronecker product of the two local maps on that side (with transpose on the right). Every factor is invertible on the relevant input/output spaces. In particular, V_a acts on a full 6-dimensional factor, so allowing it to mix H with K **does not** alter the rank argument.

For P the output-sector flattening rank is still12. For each E_ij it is still8. A matrix of rank r has at least r nonzero entries, and flattening merely reindexes a sector's coefficients. Thus the seven output supports, which are disjoint by §3, total at least

`12 + 6·8 = 60`.

The source identity transformation gives60, proving the exact restricted-orbit minimum. This reasoning covers **every** choice of unrestricted party and **all** complex invertible matrices; no chosen local basis or sampled-angle argument is used.

## 5. Boundaries and check levels

The proof strictly extends the earlier all-four-block-diagonal result `frontier-20261028-u2u4-sector-orbit-barrier-v1.md` SHA256 `8bf0f06dea859552924fa3be3340f70966d6b56b4c162335193bc7cf168b44f0`: the fourth party may now be a completely unrestricted GL(6) map. It does not cover two or more unrestricted parties; grouping by only two preserved H/K factors merges several source sectors and the present rank sum does not automatically survive. It does not cover another AME orbit or establish global support60.

The sector-rank checks and source-state six-marginal verifications are exact same-harness computations with separately structured witness checkers; the new arbitrary-map statement is written linear algebra on those checked source facts. No independently commissioned review, formal/kernel proof, novelty/priority clearance or strictly improved all-state lower bound is claimed. No scientific outcome is inferred from earlier quarantined records. The unrestricted original AME(4,6) minimum and actual sub-60 witness remain unresolved.
