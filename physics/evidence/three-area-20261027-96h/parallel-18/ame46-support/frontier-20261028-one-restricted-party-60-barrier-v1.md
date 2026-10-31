# One block-preserving and three unrestricted parties: a 60-support barrier for the Pandya tensor

Owner: **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:01:12 PDT 2026`; not a claim about the exact completion time. **WRITTEN author candidate; specific finite source-data facts and bounded controls checked in exact arithmetic below. Independently commissioned scientific review is needed before adoption.** This is not a formal proof, novelty clearance, or a lower bound for all AME(4,6) states.

## 1. Claim and scope

Let `T` be the specific 60-term tensor in [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), with `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}` on each of its four local spaces. Choose any one party `C`; its transform `V_C` is any invertible complex block-diagonal map `GL(H)⊕GL(K)`. The other three parties may each use an **arbitrary** `GL(6,C)` map, with no H/K restriction. Then the number of nonzero output coefficients satisfies

`support((V_0⊗V_1⊗V_2⊗V_3)T) ≥ 60`.                                (1)

The identity attains 60, so 60 is the exact minimum over this restricted invertible orbit. The unitary subcase is physical; generic nonunitary maps do not preserve the AME condition and are not called AME witnesses.

Consequently, a local-unitary transform of this **particular** state with fewer than 60 coefficients would require the image of H to be a non-coordinate 2-plane at **every one** of the four parties. Indeed, if any party maps H to a coordinate 2-plane, unitarity also maps K to its coordinate orthogonal complement; an output permutation, which preserves support, makes that factor H/K block diagonal, and (1) applies. This is only a necessary condition for a sub-60 state in this LU orbit. It is not a statement about arbitrary states, arbitrary orbits, or existence of such a state.

## 2. Finite source facts used

Suppress a common nonzero normalization and write the 60 source coefficients as a sum of seven disjoint sectors: `P`, containing 12 all-K terms of coefficient `√2`, and six `E_ij`, each with exactly parties `i,j` in H and the other two in K, containing eight coefficients `±1`. No other H/K pattern occurs. These are source-table facts, not assumed for general AME tensors.

For every active pair `i,j`:

1. The four K-spectator index pairs of `E_ij` form a perfect matching between the four K levels. Each corresponding 2×2 coefficient matrix on `H_i⊗H_j` is invertible. Up to individual signs and transpose, its four matrices are exactly `I, X, Z, J=ZX`, where

   `I=[[1,0],[0,1]]`, `X=[[0,1],[1,0]]`, `Z=[[1,0],[0,-1]]`, `J=[[0,1],[-1,0]]`.

   These four matrices are linearly independent over C. (The displayed J is `ZX`; sign conventions do not affect any claim below.)
2. For every 2|2 cut, the 12 pairs of K labels appearing on either side in P are pairwise distinct; their four missing label pairs are precisely the spectator matching of the `E` sector active on the other side of that cut.
3. Fix any ordered distinct parties C and B, and call the other parties A,D. For each `c∈K_C`, let `d(c)` be the unique D-K level paired with c in the spectator matching of `E_AB`, and let `a(c)` be the unique A-K level paired with c in the spectator matching of `E_BD`. Then the pair `(a(c),d(c))` is in the A,D spectator matching of `E_BC`; in particular **no P coefficient at all** has this A,D pair, irrespective of its C,B coordinates.

The last sentence is important: it is a full matrix-entry zero, not merely absence of the single P contribution with C level c. It is the structural fact that repairs the mixed-covector cancellation gap in the initial unreviewed proposal.

Source table `frontier-20261028-pandya-table-v1.txt`: SHA-256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Exact source structure code `frontier-20261028-one-restricted-sector-structure-v1.py`, SHA-256 `5a1f5e1ba3ba56b50d21a0c1a6452f41af14ff74204aec7c367d4855084d0a71`; its 3310-line result `frontier-20261028-one-restricted-sector-structure-v1.json`, SHA-256 `6cce096c495b2a4f5040fadeda69267af85f73f8651dc031c0cf401720fb8641`, covers all 12 ordered C,B choices, the P complement matching, all Pauli types, and a deleted-E-coefficient rejection. The independent cross-sector zero checker `frontier-20261028-structural-zero-repair-v1.py`, SHA-256 `68c133ae1c919bc039c7c636e2b8f2810c23aee2bf3a77d697d61d525e39a660`, checks all 48 choices of ordered C,B and c; result `frontier-20261028-structural-zero-repair-v1.json`, SHA-256 `23f2d90c185cc61a020276b17e6e344e4a96518c2969cff7e78566bf46dc0a5a`, also rejects a P coefficient inserted at a claimed zero. These scripts use the same source parser; they are separate structural checks, not independent transcriptions of the paper.

The source table was previously checked by separate exact sparse and dense implementations against all six two-body marginals and normalization. Their source and result identities are recorded in `frontier-20261028-independent-dense-verifier-v1.py` (SHA-256 `30ab4c1ab5380e3df864c51a14d9528e595f46f98f1cf1d7e86a966f57309808`) and its JSON receipt (SHA-256 `923c23cadbf89283eb8124014fd6aeeeff9ff241eb9f39ca60d369a94be25e86`). This is the same-harness check of the displayed witness, not an independent human confirmation of the public transcription.

## 3. Reduction to ranks of 6×6 contraction matrices

Fix C, choose any different B, and let A,D be the other parties. Regard a C-output coordinate as a covector on the C-input and a B-output coordinate as a covector `u=(u_H,u_K)` on the B-input. Since `V_C` preserves H/K, its two H output covectors `λ` are nonzero covectors on H, and its four K output covectors `t` are nonzero covectors on K. Since `V_B` is invertible, its six output covectors form a basis of the 6-dimensional dual space.

For fixed C and B output coordinates, contract T against these covectors. The remaining 36 entries form an A-by-D 6×6 matrix M. Applying the arbitrary invertible A and D maps left- and right-multiplies M by invertible matrices (with the appropriate transpose), so its rank is unchanged. A matrix of rank r has at least r nonzero entries. Therefore the total output support is at least the sum of the ranks of these 12 H-sector and 24 K-sector matrices. No change of variables in the universal argument assumes that V_A or V_D preserves H/K.

## 4. Each H-sector contraction has rank at least 2

Let `λ≠0` be the C-H covector. In the original A and D H/K decompositions,

`M_H(λ,u) = [[0, X(λ,u_K)], [Y(λ,u_K), Z(λ,u_H)]]`.             (2)

The blocks arise respectively from E_AC, E_DC, and E_BC; P does not contribute. If `u_K≠0`, both X and Y are nonzero: for any nonzero component of u_K, the perfect spectator matching selects a distinct output column of X or row of Y, and the corresponding 2×2 active Pauli block sends nonzero λ to a nonzero vector. Thus one can choose nonzero entries `X_{i,d}` and `Y_{a,j}`. Their 2×2 minor uses the zero upper-left block and has determinant `−X_{i,d}Y_{a,j}≠0`, regardless of Z.

If `u_K=0`, then `u_H≠0` and X=Y=0. Z is supported on the four matching A,D pairs and has entries, up to signs and transpose, `u_H^T Q_s λ` for `Q_s∈{I,X,Z,J}`. At least two of these four entries are nonzero. For otherwise three vectors `Q_s λ` would lie in the one-dimensional kernel of the nonzero covector `u_H`. Three distinct Pauli images cannot be collinear: after applying the inverse of one matrix, λ would be a simultaneous eigenvector of two distinct nonidentity Pauli matrices; these two invertible matrices anticommute, so no common nonzero eigenvector exists over C. The matching makes the nonzero Z entries occupy distinct rows and columns, hence `rank Z≥2`.

In either case `rank M_H≥2`. There are two C-H outputs and six B outputs, so their disjoint output coordinates contribute **at least 24** nonzero coefficients.

## 5. Each K-sector slice contributes at least 9

Fix a nonzero C-K covector `t`. Its A,D contraction has the block form

`M_K(t,u) = [[F(t,u_K), X(t,u_H)], [Y(t,u_H), Z(t,u_K)]]`.        (3)

Here F comes from E_AD, X from E_AB, Y from E_BD, and Z from P. Choose any c with `t_c≠0`.

**Mixed or pure H component: `u_H≠0`.** By the E_AB and E_BD spectator matchings and invertibility of their active Pauli blocks, the column `d(c)` of X is nonzero and the row `a(c)` of Y is nonzero. Source fact 3 says `Z_{a(c),d(c)}=0` for the whole matrix, even if `u_K≠0` and t has several nonzero components. Choosing nonzero `X_{i,d(c)}` and `Y_{a(c),j}`, the determinant of rows `i,a(c)` and columns `j,d(c)` is

`det [[F_ij, X_{i,d(c)}], [Y_{a(c),j}, 0]] = −X_{i,d(c)}Y_{a(c),j} ≠ 0`.

Thus `rank M_K≥2`. This argument explicitly allows F to be nonzero; nonzero X and Y alone would not suffice.

**Pure K component: `u_H=0`.** Since the B covector is nonzero, `u_K≠0`, and (3) becomes `diag(F,Z)`. The four matched C,B products `t_c u_{π(c)}` are the coefficients of the four signed Pauli matrices in F, so linear independence implies

`F=0  ⇒  t_c u_{π(c)}=0  for each c∈K`.                          (4)

The 12 remaining, nonmatched C,B products are precisely the 12 entries of Z, each at a different A,D pair and multiplied by `√2`; hence no cancellation between products occurs. If `Z=0`, the support rectangle `supp(t)×supp(u_K)` is contained in the four-edge matching. As both vectors are nonzero, each support must be a singleton and the two singleton levels must be matched. Then F is a nonzero scalar times one Pauli matrix, so `rank F=2`. In particular M_K is never the zero matrix.

If instead `rank M_K=1`, Z cannot be zero by the previous paragraph. Block diagonality then forces `F=0`; (4), together with our fixed `t_c≠0`, implies `u_{π(c)}=0`. Therefore for this fixed t every rank-one B covector lies in the linear subspace

`W_t = { u : u_H=0 and u_{π(c)}=0 }`,

which has complex dimension 3. (This is a containment, not a claim that every vector in W_t gives rank one.) The six B output covectors form a basis, so at most three of them can lie in W_t. Every contraction has rank at least 1 and every other contraction has rank at least 2. Their rank sum is therefore at least `3·1+3·2=9`. The four C-K outputs give **at least 36** nonzero coefficients.

Combining the H and K sectors gives `24+36=60`, proving (1) conditional only on the exact source facts in §2.

## 6. Explicit finite controls and limitations

A distinct direct-contraction script constructs the full 6×6 matrices from the table and computes Gaussian-elimination rank over `F_17`, with `6²=2`; it uses all 12 ordered choices of C,B and nonzero 0/1 covectors. It checks 2,268 H contractions and 11,340 K contractions, including mixed u_H/u_K vectors. It finds 144 K rank-one examples and verifies that each lies in the specified dimension-3 containment; all 2,268 H ranks are at least 2 and no K contraction is zero. Code `frontier-20261028-mixed-contraction-controls-v1.py`, SHA-256 `a5b4d3a38a776b2f84aafd943bebedc43e6e303650788054291c57c7860a5729`; result `frontier-20261028-mixed-contraction-controls-v1.json`, SHA-256 `28ad81a0ea7a672e9fe56dd1a58c51bbd2df060a4d072cffc23fa613bcdb9ef4`. These are bounded exact controls, **not** a proof over C; the universal proof is the written rank and Pauli argument above.

The earlier standalone two-unrestricted-party ≥56 written candidate `frontier-20261028-two-unrestricted-parties-56-barrier-v1.md`, SHA-256 `7ff771b9a5266e039fba16bfcaeec26d4dc7f843fd19173bc7b369b1ee26e254`, is a separate weaker result; this candidate would subsume it if independently accepted. No claim is made that an arbitrary four-party LU or an arbitrary AME tensor has support at least 60. A rigorous all-orbit/all-state lower bound or an explicit sub-60 AME witness remains the original open deliverable.
