# A 60-support barrier for the entire local GL(6) orbit of the Pandya tensor

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:10:43 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, relying on the explicitly identified exact finite source checks below; independently commissioned scientific review is required before adoption. Not a formal proof, a global AME(4,6) lower bound, or a novelty determination.

## 1. Statement

Let `T` be the specific real 60-term AME(4,6) tensor of [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), in its displayed product basis. For **arbitrary complex invertible** `V_i∈GL(6,C)`, with no factor constrained to preserve any subspace,

`support((V_0⊗V_1⊗V_2⊗V_3)T) ≥ 60`.                                  (1)

The identity has support 60, so the minimum over this tensor's complete local invertible orbit is exactly 60. The LU orbit is a subcase; generic nonunitary output does not preserve AME and is not presented as an AME state.

This is one **specific** orbit. It does not rule out a smaller-support AME state in another orbit, identify the global minimum, prove a lower bound for all AME(4,6) states, or clear novelty. The original global minimum remains unresolved. The argument below uses the unitarity of the source's 2|2 flattenings to analyze arbitrary complex contraction covectors; it does **not** assume the output local maps are unitary.

## 2. Exact source representation and two-uniformity

Suppress the common factor `1/√72`. On each party let `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}`. Relabel each K basis by four colors `0,1,2,3` using

| physical K level | 0 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|
| party 0 | 3 | 2 | 0 | 1 |
| party 1 | 3 | 0 | 2 | 1 |
| party 2 | 3 | 0 | 2 | 1 |
| party 3 | 3 | 2 | 1 | 0 |

The source has exactly:

- `P`: 12 all-K terms, all coefficient `√2`, whose four-color tuples are precisely the 12 even permutations in `A_4`;
- for each pair `i<j`, `E_ij`: eight terms with H on i,j and K on the two spectators. The spectator colors coincide, say `(g,g)`. At each g the H_i-by-H_j coefficient matrix is a signed Pauli; across g=0,1,2,3 these are exactly one each of `I,X,Z,J=ZX`, up to sign;
- no term with one, three, or four H indices.

The Pauli matrices are `I=[[1,0],[0,1]]`, `X=[[0,1],[1,0]]`, `Z=[[1,0],[0,-1]]`, `J=[[0,1],[-1,0]]`. Transposes merely change a sign for J and do not change the set. The even permutations have the key **two-transitivity** property: for any two positions and any two distinct colors, there is exactly one even permutation extending those assignments.

For every 2|2 cut, the unnormalized 36×36 flattening F satisfies `F F†=2 I`. Thus `U=F/√2` is unitary. The normalized state is `T=F/√72=U/6` in every cut. This source isometry and all structural assertions above are independently reproducible finite statements about the pinned table, not assumptions about a general AME tensor.

Source table: `frontier-20261028-pandya-table-v1.txt`, SHA-256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Exact certificate code: `frontier-20261028-four-colour-a4-source-certificate-v1.py`, SHA-256 `66e8402545ed4f99b8a483f9601dfcaf5c38e663fa5ad5bec5b88c5d2d99ba39`; receipt `frontier-20261028-four-colour-a4-source-certificate-v1.json`, SHA-256 `638ab2a6bb1bca1c4ffd535db6e66d293cadebb44a615154fda2250d0628ba6b`. It directly parses the table, checks all 12 even tuples and all six signed-Pauli block families, checks all `3·36²=3888` entries of `F F†=2 I` using integer arithmetic in `Z[√2]`, classifies the 50,625 nonempty four-color support masks used in §5, and rejects a deleted P term. A separate earlier dense witness verifier is `frontier-20261028-independent-dense-verifier-v1.py`, SHA-256 `30ab4c1ab5380e3df864c51a14d9528e595f46f98f1cf1d7e86a966f57309808`; its six-marginal receipt has SHA-256 `923c23cadbf89283eb8124014fd6aeeeff9ff241eb9f39ca60d369a94be25e86`. These are same-harness checks, not independent human verification of the transcription.

## 3. Rank bounds for pure-H and pure-K covectors

Fix distinct C,B, let A,D be the other parties, and contract the unnormalized T with nonzero C and B covectors. The result is a 6×6 A-by-D matrix M. Write B's covector as `u=(u_H,u_K)`. The statements in this section hold for **all** nonzero complex covectors, not just basis vectors.

### 3.1 Pure H on C

For `λ∈H_C*\{0}`,

`M_H=[[0, X(λ,u_K)], [Y(λ,u_K), Z(λ,u_H)]]`.

If `u_K≠0`, the matched spectator structure of `E_AC` and `E_DC` gives nonzero X and Y: each nonzero K component selects a distinct column/row and an invertible Pauli image of λ. A 2×2 minor using the zero upper-left block has determinant `−XY≠0`, so rank is at least 2, irrespective of Z.

If `u_K=0`, the nonzero `u_H` produces only Z, on four matched A,D K positions, with entries `u_H^T Q_g λ`. At least two entries are nonzero. Otherwise three of the vectors `Q_g λ` lie in the one-dimensional kernel of `u_H`; after applying the inverse of one Q, λ would be a simultaneous eigenvector of two distinct nonidentity Pauli matrices. These anticommute and are invertible, hence have no common nonzero eigenvector. The distinct matching positions give `rank Z≥2`. Thus a pure-H C covector has **rank at least 2 against every nonzero B covector**.

### 3.2 Pure K on C

Let `t∈K_C*\{0}`. In A,D H/K blocks,

`M_K=[[F(t,u_K), X(t,u_H)], [Y(t,u_H), Z(t,u_K)]]`.          (2)

If `u_H≠0`, choose a color g with `t_g≠0`. The D-K column g of X and the A-K row g of Y are both nonzero, by the matched spectator structure and invertibility of their active Pauli blocks. The entry `Z_{g,g}` is **zero for the whole contraction**, because P uses four distinct colors. Choosing nonzero X and Y entries at that column and row produces a 2×2 minor `[[F_ij,X],[Y,0]]`, of determinant `−XY≠0`; F is allowed to be nonzero. Hence rank is at least 2 even for mixed u_H/u_K.

If `u_H=0`, then `u_K≠0`, X=Y=0, and M is block diagonal. Its 2×2 block is `F=Σ_g t_g u_g Q_g`; the four Q_g are linearly independent, so F=0 implies `t_g u_g=0` for all g. Its 4×4 P block Z has 12 distinct entries, one for each nonmatching pair `(g,h)` of C,B colors, proportional to `t_g u_h`. If Z=0, `supp(t)×supp(u_K)` lies in the four diagonal color pairs, forcing both supports to be the same singleton; then F is a nonzero scalar times an invertible Pauli, so `rank M=2`. Therefore M is never zero. If `rank M=1`, necessarily Z≠0 and F=0. For any fixed g with `t_g≠0`, this forces `u_g=0`; all such rank-one B covectors lie in

`W_t={u : u_H=0 and u_g=0}`, of dimension 3.                      (3)

In a basis of six B covectors at most three lie in W_t, so their six contraction ranks sum to at least `3·1+3·2=9`. These bounds are the elementary content of the earlier one-restricted-party author candidate; here they are restated and used without assuming its review or adoption.

## 4. From a rank-one contraction to product saturation

Suppose a contraction of T with nonzero C,B covectors has rank one. Normalize those covectors. The unitary `U` on the CB|AD cut maps their product to a rank-one A,D tensor of norm 1, hence to a product of two normalized vectors, up to phase. After the appropriate complex conjugations of input vectors, there is a normalized four-party product vector `φ=φ_0⊗φ_1⊗φ_2⊗φ_3` satisfying

`|<φ,T>|=1/6`.                                                       (4)

For **every** 2|2 cut, `T=U/6` with U unitary. Equality in the Cauchy–Schwarz bound `|<φ,T>|≤1/6` means that the normalized U maps the product of the two conjugated input factors to the product of the other two factors, up to a phase. Therefore every two-party contraction of this same φ has rank one. Complex conjugation does not change whether a vector is in H or K or the probabilities introduced next.

By §3.1 no φ_i can be pure H. By §3.2, if any φ_i is pure K then every other φ_j is pure K, since a nonzero H component on j would make their contraction rank at least 2. Consequently a rank-one contraction whose C covector has both H and K components would produce φ with **all four parties mixed**: both its H and K components are nonzero. We now exclude this possibility.

## 5. Four-color probability classification

For this hypothetical all-mixed φ, set

`h_i=||φ_{i,H}||²>0`, `p_i(g)=|φ_{i,K,g}|²≥0`, `h_i+Σ_g p_i(g)=1`.  (5)

Every set `S_i={g:p_i(g)>0}` is nonempty. Let `(g_0,g_1,g_2,g_3)` be an even permutation, and write `x_i=p_i(g_i)`. For each choice of input pair ij and output pair kl, the unitary U has exactly one contribution at the distinct output colors `(g_k,g_l)`: the P coefficient has normalized modulus 1, and no E term can contribute at distinct spectator colors. The pair-to-pair product equality from §4 gives

`x_i x_j = x_k x_l` for every partition `{i,j}|{k,l}`.           (6)

For four nonnegative x_i, the three equalities in (6) imply either all four are positive and equal, or at most one is positive. In particular an even permutation cannot meet exactly two or three of the four S_i.

The resulting nonempty support patterns are exactly:

1. all four S_i are the same singleton;
2. all four are distinct singletons, forming one even permutation;
3. every S_i contains all four colors.

A short written verification: if two parties contain distinct colors, two-transitivity supplies the unique even permutation containing both; the rule forces all four of its colors to occur. Relabel parties and colors simultaneously so this permutation is `(0,1,2,3)`. If any party contains an additional color, a simultaneous relabel lets us assume party 0 also contains 1. Successively applying the rule to even permutations

`(1,3,2,0), (1,2,0,3), (3,2,1,0), (3,1,0,2), (2,3,0,1), (2,0,1,3), (2,1,3,0)`

forces every party to contain every color. If there is no additional color, case 2 holds. If no two parties contain distinct colors, nonemptiness forces case 1. The exact mask certificate in §2 independently enumerates `15^4=50,625` nonempty masks and reports `4+12+1=17` patterns in these three classes; the written argument does not depend on treating that enumeration as formal proof.

A second probability identity follows from the same U. In any cut ij|kl, the HH output on i,j receives only the matched K-input products on k,l. The four signed Pauli matrices are Hilbert–Schmidt orthogonal, with squared norm 2, and their normalized coefficient is `1/√2`. Hence

`h_i h_j = Σ_g p_k(g)p_l(g)` for all distinct i,j,k,l.             (7)

If the four S_i are distinct singletons, the right side of (7) vanishes, contradicting `h_i h_j>0`. If they are the same singleton g, it equals `k_k k_l`, where `k_i=Σ_g p_i(g)>0`. But output at matched K colors `(g,g)` in the reverse cut can only come from the HH-input Pauli block, so Cauchy–Schwarz gives

`k_k k_l = p_k(g)p_l(g) ≤ (1/2) h_i h_j`,

contradicting (7). Thus all four S_i contain all four colors.

In the full-support case, (6) says the selected four probabilities in **every** even permutation are equal. Any two entries `p_i(g),p_j(h)` with distinct parties and colors occur together in such a permutation, and the graph on the 16 party/color entries generated by these co-occurrences is connected. Hence all 16 entries equal a single p>0. Equation (7) gives `h_i h_j=4p²` for every pair; positivity implies all `h_i=2p`. Normalization yields

`p=1/6`, `h_i=1/3`.                                                (8)

## 6. The four-qubit Bloch contradiction

For any input pair i,j and spectator output pair k,l, the matched color output `(g,g)` comes only from the normalized Pauli block `Q_{ij,g}/√2`. The pair-to-pair product equality, together with (8), gives

`p_k(g)p_l(g) = (1/2)|φ_{i,H}^T Q_{ij,g} φ_{j,H}|²`,

where the input H factors may be conjugated; this does not affect their norms. Define each normalized input H spinor `η_i` by dividing that conjugated factor by `√h_i`. With (8), for **every** pair i,j and every g,

`|η_i^T Q_{ij,g} η_j|² = 1/2`.                                   (9)

For each pair, the four `Q_{ij,g}` are, up to signs and transpose, precisely I,X,Z,J; (9) is therefore true for the same four Pauli operators in the fixed H bases of all parties.

Let `r_i∈R³` be the Bloch vector of the pure spinor η_i, so `||r_i||=1`. Complex conjugation reflects its y component. The Pauli-density-matrix identity says that the four numbers `2|η_i^T Qη_j|²−1`, as Q runs over I,X,Z,J, are the four signed sums of the three products `r_{i,x}r_{j,x}`, `−r_{i,y}r_{j,y}`, `r_{i,z}r_{j,z}`, with sign rows `+++`, `+--`, `--+`, `-+-`. Their 4×3 sign matrix has `H^T H=4 I`. If all four overlaps in (9) equal 1/2, all three coordinate products vanish:

`r_{i,a} r_{j,a}=0` for every distinct i,j and `a∈{x,y,z}`.      (10)

Thus the supports of four nonzero Bloch vectors are pairwise disjoint subsets of a three-element set, impossible. This contradicts the existence of an all-mixed product saturator. Together with §4: **no rank-one contraction of T can have a mixed H/K covector at C**. Pure H was already excluded by §3.1.

## 7. Sum of contraction ranks and conclusion

Apply arbitrary invertible maps to all four parties. Fix C and B and consider their six output coordinate covectors. They form bases of the respective six-dimensional dual spaces. At most four of C's six basis covectors are pure K. For each pure-K C covector, §3.2 gives a sum of at least 9 ranks over B's six outputs. For each other C covector—pure H or mixed—§3.1 and §6 give rank at least 2 against **every** B output, hence a sum of at least 12.

If k≤4 C covectors are pure K, the sum of all 36 contraction ranks is at least

`9k+12(6−k)=72−3k ≥ 60`.                                         (11)

The arbitrary invertible A and D transformations preserve each matrix rank. Each final A,D matrix has at least as many nonzero entries as its rank, and different C,B output slices have disjoint coefficients. Hence (11) is a support lower bound for the fully transformed tensor. The identity attains 60, proving (1), subject to independent review of this written argument and the source reconstruction.

## 8. Diagnostics and scope of checking

A separate exact finite-field diagnostic searched **all 19,200 projective mixed-C covectors and all 19,608 projective B covectors over F_7**, where `3²=2`, for each of the 12 ordered C,B choices: `4,517,683,200` pairs total. No contraction of rank ≤1 appeared. Search source `frontier-20261028-mixed-product-rank-search-v1.cpp`, SHA-256 `49f3e234a41bf5b40e94c0d84ff40fb518a1710e8a656073e9d56252706f26cd`; aggregate of the 12 per-orientation receipts `frontier-20261028-mixed-product-search-aggregate-v1.json`, SHA-256 `1d199aa58fc94094ef2ab2911d4a5ab8454e26a0ee014782943fae86b1edc238`. The aggregate binds hashes observed at aggregation, not a separate execution-time hash attestation. Predicate controls use 10,000 rank-one positives, a zero positive, and 20,000 comparisons with independent modular Gaussian rank: code `frontier-20261028-mixed-rank-search-controls-v1.cpp`, SHA-256 `f883dfc91bd297ae8dc67c1dd03f9a0448491ee789b504fc050affbc9e199308`; receipt SHA-256 `adee780ab29d04c5b4c81d0a099de18023597905f8daf8c906adff40be92ccf1`. This finite-field search is a **diagnostic, not a proof over C**; §§4–7 are the written complex argument.

This candidate strictly strengthens, and if accepted subsumes, the earlier one-restricted-party orbit candidate `frontier-20261028-one-restricted-party-60-barrier-v1.md` SHA-256 `c69c98287440eb9d0e19ff7960044ea8ab3e27e0efc1b8f64dee73e17602b443`. Neither candidate is accepted by merely recording it here. The separate question of whether any other AME(4,6) orbit has a representative with support <60 remains open in this work.
