# f67: independent review of the one-restricted-party 60 barrier

**Disposition: NO FINDING at the reconstructed, pinned-table scope. FATAL 0; MAJOR 0; MINOR 0.** This is one same-harness scientific review, not a parent acceptance, independent-model or human review, formal/kernel verification, priority review, or an all-AME/all-four-unrestricted-orbit theorem. Native clock immediately before writing: `2026-10-28T18:09:36-0700 PDT` (not an asserted completion time).

I read the frozen manifest, the complete pinned table and then the complete repaired candidate, in that order. I wrote and executed my own table parser, source-fact enumerator, exact contraction checks and mutations; **no author checker was imported**. The proof below is an independent reconstruction over all complex covectors, not an inference from the finite samples. At this table-relative scope I found no unclosed universal-complex inference gap. The exact table's identification with Pandya's public Table 1 was not independently checked against the paper; the candidate already discloses that its transcription lacks an independent human confirmation. Thus paper attribution is conditional on that byte-level source identification, rather than something this review independently establishes.

## Inputs and evidence bindings

| Item | SHA-256 |
|---|---|
| Frozen `manifest-v1.json` | `5a4c123d4073f47eec13fe8c5388dd8a7cf9d7ce0e0d5c6ccf796ac8672f9737` |
| `frontier-20261028-pandya-table-v1.txt`, 523 bytes, 38 LF | `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` |
| `frontier-20261028-one-restricted-party-60-barrier-v1.md`, 11,896 bytes, 85 LF | `c69c98287440eb9d0e19ff7960044ea8ab3e27e0efc1b8f64dee73e17602b443` |
| `check-independent-v1.py` | `c6a05d080e419002c71344708435288c52b847ec02444dc130c4aa75d0281391` |
| `receipt-independent-v1.json` | `d9f36ea1a9327521e65afad08c03cb883647497f3a98ba4d1a735230fe926051` |

Receipt clock immediately before its exclusive-create write: `2026-10-28T18:08:48-0700 PDT`. The checker reread and rehashed both pinned inputs before the receipt write. The receipt contains **all 12** ordered `(C,B)` orientations, each orientation's six separately rebuilt active-sector views, every spectator pair, the actual signed 2×2 matrix, its Pauli name, all 12 `P` mappings across the cut, and all four structural-zero incidences. All these checks share my own source parser; they are independent of the author's code but not three independent source transcriptions. Author checker/results cited in the candidate were not imported or separately audited.

## Direct source reconstruction

Axes are numbered 0,1,2,3 in table order; `H=(1,2)` and `K=(0,3,4,5)`. Parsing every row yields 60 occupied entries, squared norm 72 before the common normalization, exactly 12 all-K entries of coefficient `sqrt(2)`, exactly eight entries `±1` for each of the six two-H sectors, and no other H/K patterns. For every ordered `(C,B)`, with the remaining axes ordered increasingly as `(A,D)`, all six sectors have exactly four distinct spectator pairs, forming bijections of K. Their four explicitly reconstructed matrices are signed `I,X,Z,J` once each, with all determinants nonzero. For each cut, all 12 all-K entries have distinct projected pairs on **both** sides; the four absent pairs on CB are the `E_AD` spectator matching and those on AD the `E_BC` spectator matching. This is stronger than merely counting twelve entries.

As a checkable illustration, for `(C,B,A,D)=(0,1,2,3)`, the entries below are `spectator-pair: signed Pauli`, in the stated axis orders. `J=[[0,1],[-1,0]]`.

| Active sector; spectator axes | Four reconstructed values |
|---|---|
| AB=(2,1); CD=(0,3) | `00:+X, 33:+J, 45:+I, 54:-Z` |
| AC=(2,0); BD=(1,3) | `00:-Z, 35:-I, 43:-X, 54:+J` |
| AD=(2,3); CB=(0,1) | `00:-J, 34:-Z, 43:+I, 55:+X` |
| BC=(1,0); AD=(2,3) | `00:+I, 35:-J, 43:+X, 54:+Z` |
| BD=(1,3); CA=(0,2) | `00:-X, 34:-Z, 43:-J, 55:+I` |
| CD=(0,3); BA=(1,2) | `00:-Z, 33:-J, 44:+I, 55:+X` |

The full signed matrices/matchings, not merely this example, are in the receipt's `ordered_orientations` array. The following independent inventory displays **all 48** structural incidences. In each row the four triples `(a(c),d(c),pi(c))` are in the fixed `c` order `(0,3,4,5)`; `pi` is the `E_AD` CB matching. Every displayed `(a,d)` lies in the `E_BC` matching and is absent from **every** P entry regardless of C and B, not just absent from the term with that particular `c`.

| C,B; A,D | `(a,d,pi)` for c=0,3,4,5 |
|---|---|
| 0,1; 2,3 | `(0,0,0) (4,3,4) (3,5,3) (5,4,5)` |
| 0,2; 1,3 | `(0,0,0) (4,3,4) (3,5,3) (5,4,5)` |
| 0,3; 1,2 | `(0,0,0) (4,4,3) (3,3,5) (5,5,4)` |
| 1,0; 2,3 | `(0,0,0) (3,5,4) (4,3,3) (5,4,5)` |
| 1,2; 0,3 | `(0,0,0) (4,5,3) (3,3,4) (5,4,5)` |
| 1,3; 0,2 | `(0,0,0) (4,3,5) (3,4,3) (5,5,4)` |
| 2,0; 1,3 | `(0,0,0) (3,5,4) (4,3,3) (5,4,5)` |
| 2,1; 0,3 | `(0,0,0) (4,5,3) (3,3,4) (5,4,5)` |
| 2,3; 0,1 | `(0,0,0) (4,3,5) (3,4,3) (5,5,4)` |
| 3,0; 1,2 | `(0,0,0) (4,4,3) (5,5,5) (3,3,4)` |
| 3,1; 0,2 | `(0,0,0) (3,4,4) (5,5,5) (4,3,3)` |
| 3,2; 0,1 | `(0,0,0) (3,4,4) (5,5,5) (4,3,3)` |

The source parser also formed each of the three distinct 36×36 flattenings. Direct Gram calculation over `Z[sqrt(2)]` gave `2 I_36` for every one; the transposed cuts give the other three two-body reductions. Thus the **pinned** normalized tensor has all two-body reductions `I_36/36`. This checks its AME property, but does not independently identify the table with the publication.

## Universal-complex proof reconstruction

Treat output rows as complex covectors; contractions here are bilinear, not Hermitian products. Fix C, any other B, and the two remaining parties A,D. The four sector block descriptions follow directly from which axes are in H and K. In every no-cancellation statement below, the matching sends different spectator labels to **different** remaining output columns or rows; nonzero contributions do not need to be added in the same coordinate.

### H covector

For nonzero `lambda` on C-H and nonzero B covector `u=(u_H,u_K)`, the contraction is

`M_H = [[0, X(lambda,u_K)], [Y(lambda,u_K), Z(lambda,u_H)]]`.

If `u_K` is nonzero, choose one nonzero K component. The `E_AC` and `E_DC` spectator bijections put its contributions into a definite column of X and a definite row of Y, respectively. Each is a nonzero vector because the relevant signed Pauli matrix is invertible and `lambda != 0`. They cannot be cancelled by other K components. Select nonzero entries `x,y`; the minor `[[0,x],[y,z]]` has determinant `-xy != 0`, independent of z. Thus the rank is at least 2.

If `u_K=0`, then `u_H != 0` and only the four matching entries of Z remain. Up to nonzero signs and harmless transposes, these are the four values `u_H^T Q lambda`, `Q in {I,X,Z,J}`. If fewer than two were nonzero, three of the vectors `Q lambda` would lie in the one-dimensional kernel of `u_H`. For any one of those three, left-multiply all three images by its inverse: `lambda` would be a common eigenvector of two different members of `{X,Z,J}` up to sign. These two invertible matrices anticommute. Their eigenvalues on a nonzero common eigenvector would both be nonzero, whereas anticommutation forces their product to vanish on it, a contradiction over C. Thus at least two matching entries are nonzero, in different rows and columns, so the rank is at least 2. This argument allows isotropic complex vectors; it does not use positivity or a real-field reduction.

### K covector: mixed case, including nonzero F

For nonzero `t` on C-K,

`M_K = [[F(t,u_K), X(t,u_H)], [Y(t,u_H), Z(t,u_K)]]`,

where F, X, Y, Z are from `E_AD`, `E_AB`, `E_BD`, P, respectively. If `u_H != 0`, fix **any** c with `t_c != 0`. The `E_AB` C-to-D matching picks a column `d(c)` whose X vector is `t_c` times an invertible Pauli image of `u_H`; the `E_BD` C-to-A matching similarly picks a nonzero Y row `a(c)`. Distinctness of matching labels excludes cancellation by other t components. The independently enumerated full P zero gives `Z[a(c),d(c)]=0` for all t and `u_K`, including dense or mixed covectors. Selecting nonzero entries yields

`det [[F[i,j], X[i,d(c)]], [Y[a(c),j], 0]] = -X[i,d(c)] Y[a(c),j] != 0`.

This proves rank at least 2 even when F is nonzero. The zero is essential: `[[1,1],[1,1]]` has both off-diagonal entries nonzero but rank one. An explicit source-derived complex example has `(C,B,A,D)=(0,1,2,3)`, `t_K=(1,i,1+i,-1)` and `u_H=(1,i), u_K=(1,-i,i,1-i)` in the declared H/K orders. Here `F=[[2-i,-2+i],[i,-i]]` is nonzero; for c=0, `a=d=0`, and the indicated minor is `[[2-i,i],[-i,0]]` with determinant `-1`.

### K covector: pure K, zero case and the fixed subspace

If `u_H=0`, nonzero u is purely K and the matrix is `diag(F,Z)`. Let `pi` be the CB matching for `E_AD`. Because the four signed Pauli matrices form a basis of the complex 2×2 matrix space,

`F=0` if and only if `t_c u_{pi(c)}=0` for all four c.

Every one of the other 12 CB pairs produces a separate AD entry of Z, multiplied by the same nonzero `sqrt(2)`. The CB and AD projections of P are both injective, so this is genuinely one product per entry: Z cannot hide cancellation between distinct products. If `Z=0`, the nonempty support rectangle of t and u lies wholly within a bijective four-edge matching. Both supports must therefore be singletons at matched endpoints. F is then a nonzero scalar times an invertible Pauli, hence rank 2; in particular **no** nonzero u gives a zero contraction.

Now fix t once and for all and choose any fixed `c0` with `t[c0] != 0`. If the contraction has rank one, it cannot have `u_H != 0` by the mixed minor, and cannot have `Z=0` by the previous paragraph. The rank-one block diagonal matrix then has `F=0`, which implies `u[pi(c0)]=0`. Therefore **every** rank-one u is contained in the same subspace `W_t={u_H=0, u[pi(c0)]=0}` of dimension 3. This is containment only, not equality. For any six linearly independent B output rows, at most three lie in W_t; all six have rank at least 1 and those outside W_t have rank at least 2. The six-rank sum is at least `3*1+3*2=9`, for every B basis and every nonzero t.

### Support and physical caller

The C block-preserving invertible map supplies two nonzero H covectors and four nonzero K covectors; the B invertible map supplies six independent output covectors. For each fixed C and B output coordinate, unrestricted invertible A and D operations send the remaining matrix M to `V_A M V_D^T`, so its rank is invariant. Every rank-r matrix has at least r nonzero entries: if it had fewer, the number of occupied rows, and hence its rank, would be at most that number. The fixed C,B slices are disjoint coefficient sets, so summing their lower bounds is valid. Consequently the H rows contribute at least `2*6*2=24`, the K rows at least `4*9=36`, giving support at least 60. The source has exactly 60 entries, so the identity attains the restricted-orbit minimum. No H/K restriction on A, B, or D was inserted in this argument.

If an individual local **unitary** U maps H onto a coordinate 2-plane, U maps the orthogonal K onto that plane's coordinate orthogonal complement. An output-coordinate permutation makes `PU` block diagonal for the original H/K partition without changing coefficient support. Thus any sub-60 local-unitary image of this particular pinned tensor must send H to a non-coordinate 2-plane at **every** party. This is only a necessary condition; no unrestricted four-party minimum, existence of a sub-60 image, or result for arbitrary AME states follows. The orthogonal-complement step is specific to the unitary caller and is not asserted for arbitrary invertible maps.

## Exercised controls and limits

- Over `F_17`, with `6^2=2`, all 12 orientations and nonzero 0/1 inputs gave 2,268 H contractions of rank at least 2 and 11,340 K contractions of rank at least 1. All 144 K rank-one examples obeyed the appropriate fixed-subspace containment. Across mixed cases, 18,432 chosen structural-zero minors were nonzero; in 7,872 the selected top-left F entry was itself nonzero. A concrete entry has `F=X=Y=1`, Z entry zero and determinant `16` in `F_17`.
- Over exact `Q(i,sqrt(2))`, not floating point, all 12 orientations passed a genuinely isotropic `(1,i)` pure-H rank-two case and a dense mixed case with nonzero F; all 48 corresponding mixed structural minors were nonzero. For single-support pure-K covectors there were 48 matched cases of rank 2 and 144 nonmatched cases of rank 1.
- Thirteen deterministically generated invertible B bases, including the identity, were checked in each orientation. Across 780 selected K-covector/basis cases the minimum six-rank sum was 9 and at most three rows were rank one; the selected H cases had minimum sum 12. These are additional controls, not the proof for arbitrary bases.
- Each of the 48 claimed P zeroes was separately mutated by inserting an all-K `sqrt(2)` coefficient at that AD pair; the exact structural-zero predicate rejected it for the intended reason, and an explicit mixed contraction changed the previously zero entry from 0 to 6 in `F_17`. Deleting one E coefficient was rejected for the sector's missing eighth entry; flipping its sign was rejected for a duplicated/missing Pauli type. The 2×2 counterexample above exercises the invalid shortcut that ignores the P zero.

The field samples, selected exact-complex cases, and mutation tests do not themselves prove anything universally over C. The universal-complex conclusion rests on the written Pauli, matching, determinant, linear-independence, support-rectangle and dimension arguments above. Public-table transcription, priority/novelty and any all-AME or all-four-unrestricted-orbit statement remain outside this review.
