# A four-party U(2)×U(4) support barrier for the 60-term AME witness

Owner **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:45:08 PDT 2026`**; not exact file-write/completion/runtime. **WRITTEN proof with exact finite support checks, author candidate; not yet independently peer-reviewed, formally verified or novelty-cleared.**

## 1. Statement and exact scope

Let `T` be the SPECIFIC real 60-term AME(4,6) tensor published in [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1). In its displayed product basis set

`H=span{|1>,|2>}`, `K=span{|0>,|3>,|4>,|5>}`.

For each of the FOUR parties take arbitrary complex invertible blocks `A_i∈GL(H)` and `B_i∈GL(K)`, and set `V_i=A_i⊕B_i`. Then

`support((V_1⊗V_2⊗V_3⊗V_4) T) ≥ 60`.                                          (1)

The identity attains60. Thus the exact minimum under this entire block-diagonal subgroup is60. In particular the result applies to all physical unitaries in `(U(2)×U(4))^4`, with arbitrary independent angles, complex phases and mixing inside K. Unlike the preceding special-sector theorem, **the K blocks need NOT be monomial**.

Because arbitrary output coordinate permutations/phases preserve support, (1) also applies to a product unitary for which EACH image `V_i H` is some coordinate 2-plane, even if those output 2-planes differ. Indeed, an output monomial sends each image plane to H, and unitarity sends its orthogonal complement to K. Consequently a hypothetical sub-60 state in THIS tensor's product-unitary orbit must have at least one party whose H image is NOT a coordinate 2-plane. Together with the separately proved three-party result, all four party factors must also be nonmonomial. These are only necessary conditions for an orbit improvement, not a proof that one exists.

No statement about the global minimum over all complex AME(4,6) states, arbitrary U(6)^4, or non-coordinate H/K mixing is implied. The sector's equality classification with MONOMIAL K blocks in the earlier report is not asserted for general U(4) blocks.

## 2. Seven invariant support sectors

The source table splits into disjoint H/K sectors:

- `P∈K⊗K⊗K⊗K`, exactly **12** nonzero coefficients;
- for every unordered pair `{i,j}` of parties, `E_ij` has H indices exactly on i,j and K indices on the complementary k,l, with exactly **8** nonzero coefficients.

There are six E sectors and no source coefficients in sectors with one, three or four H indices. Every product `V_1⊗⋯⊗V_4` preserves each H/K summand separately. Their output supports remain disjoint by sector, even though arbitrary B_i can now mix the K basis levels extensively. Hence total support is the SUM of the seven output-sector supports.

## 3. Exact flattening rank of P

In every 2|2 flattening of P, its twelve nonzero entries occupy twelve DISTINCT rows and twelve DISTINCT columns. Permuting rows and columns therefore gives a 12×12 diagonal matrix of nonzero entries and zeros elsewhere, so

`rank(P_(ij|kl))=12`.

Every local block V_i acts invertibly on K. Thus the flattened output matrix is obtained from this source flattening by invertible left and right Kronecker-product factors and still has rank12. Every matrix has at least rank-many nonzero entries, and flattening preserves the tensor's coefficient count. Therefore the output P sector has support at least12. No support-preserving WLOG or numerical rank threshold is used.

## 4. Exact flattening rank of each E sector

Fix any active pair `{i,j}` and its complementary K parties `{k,l}`. From the source table, its four spectator-coordinate pairs form a matching: all four values of the K basis appear once on the k side and once on the l side. At each such spectator pair, the active H_i×H_j coefficient matrix is an invertible 2×2 block with exactly two nonzero entries (one of the signed I/J/X/Z blocks).

Flatten E_ij across `(H_i⊗K_k) | (H_j⊗K_l)`. Ordering rows and columns by the paired spectator labels makes this 8×8 flattening a direct sum of the four invertible 2×2 blocks. Hence

`rank((E_ij)_(ik|jl))=4·2=8`.

After arbitrary A_i,A_j∈GL2 and B_k,B_l∈GL4, the flattening is multiplied on the left and right by invertible Kronecker-product factors. Its rank remains8, and its output sector has at least8 nonzero coefficients. This applies separately to ALL six active pairs using the SAME four actual local maps.

Summing the seven disjoint sectors gives

`support(output) ≥ 12 + 6·8 = 60`,

and the source T itself attains equality. This proves (1). No assertion is made that each block remains sparse after an arbitrary K mixing; only its invariant bipartition rank is needed.

## 5. Exact source and control checks

The independently transcribed complete source table `frontier-20261028-pandya-table-v1.txt` has SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Two separately implemented in-harness exact Q(sqrt2) routines checked normalization and every entry of all SIX 36×36 two-party marginals for that SAME tensor; they and their targeted controls are pinned in the cited earlier report. This independently reproduces a PUBLISHED witness, not a claimed new construction.

`frontier-20261028-u2u4-sector-flattening-check-v1.py`, SHA256 `2ec8a703efe0800d645808eaf70baed55e63ecc726207b2323eb6502f1574baa`, checks all six P flattenings' row/column uniqueness and every E sector's spectator matching plus invertibility of its four active blocks. Its exact receipt `frontier-20261028-u2u4-sector-flattening-check-v1.json`, SHA256 `6b7d2bfa0e686a2a68aa70787adea4c0ff72e8149c575f9b97dec576154e1383`, reports P rank12 in each flattening and each E sector rank8. Deleting one E coefficient was rejected for the intended “active block not invertible partial permutation” reason.

As a nontrivial physical control, `frontier-20261028-u2u4-mixing-control-v1.py`, SHA256 `d2cfc4d25f17864b1dc9b65f28d983a0a918d0448226eb3080759a2b591ebdb7`, applies the SAME nonmonomial real 45-degree rotation on H AND a normalized 4×4 Walsh matrix on K at ALL four parties. Its exact Q(sqrt2) receipt `frontier-20261028-u2u4-mixing-control-v1.json`, SHA256 `033ec4c02e5adf8ad3c973f87e83a52499b55cc93d0c06b9a8205d9758f8b49a`, reports support256: P sector64 and each of six E sectors32. It independently checks norm numerator/denominator `18432/18432` and every entry of all six marginals equals I/36.

The control is one point, not evidence for the universal quantifier; §§2–4 supply that argument. All checks use exact integer arithmetic, not float tolerances. Same-harness implementations are not an independent scientific review, formal proof or novelty clearance.

## 6. Relation to earlier bounds and remaining frontier

This strictly widens the earlier monomial-K `(U2⊕Mon4)^4` sector theorem to `(U2⊕U4)^4`. The separately certified arbitrary-one-two-level-per-party theorem covers DIFFERENT coordinate pairs with monomial complements and is not subsumed by a fixed H. Neither result controls multiple noncommuting two-level moves per party, arbitrary mixing between H and K, all local U(6)^4, another AME orbit or the global minimum.

The previously reported 60 coefficient state is a public PRIOR construction. Its paper reports a 38–60 support gap, but I have not independently reconstructed the paper's imported classical lower-bound theorem or established a worldwide priority/status result. No sub-60 tensor or strictly improved all-state lower bound is claimed. A disjoint review of the exact table, sector matching and rank proof remains required before adoption.
