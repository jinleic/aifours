# A written heavy-core obstruction for the remaining support-47 residual

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Thu Oct 29 10:05:50 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. Its proof is elementary complex unitarity and finite combinatorics. No SAT, LRAT, no-Hamming-one, no-OLS(6), phase solver, external classical theorem, or held material is a premise.

## 1. Exact statement and global boundary

Let ψ be a normalized complex AME(4,6) state in any product basis, with support `N=47`. Assume exactly `t=27` coefficients have modulus1/6. Then this state does not exist.

The separate, unreviewed reduction `frontier-20261029-n47-residual-reduction-v1.md`, SHA-256 `9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`, claims that any N=47 state must have t=27, using the recorded f113 t≤29 input and a new seven-row excess-four lemma. That reduction and its no-OLS(6)/prior-t≤30 boundary are **not adopted here**. If it is independently accepted, this packet would then exclude N=47. A global lower bound48 additionally needs the separate N=45 and N=46 compositions; no such global conclusion is claimed or adopted here.

The direct proof below also explains why the two larger exact-CNF certificate searches found no supports. Their69 certificates are corroboration only and are not used in the written argument.

## 2. Residual structure from all six marginals

For every 2|2 cut, `U=6ψ` is a36×36 unitary. A modulus1/6 coefficient exhausts its row and column norms and is the only nonzero there in every cut. Let P be the27 such positions and E the other20. Removing P gives a9×9 unitary V in each cut with every row and column degree at least2. A singleton would itself be maximal.

A unitary of support `2n+2` and no singleton line is, up to row/column permutations, one3×3 block with8 nonzeros plus2×2 blocks. Here is the elementary argument. Support components are square. Two unitary rows cannot share exactly one nonzero column. A zero-excess component is a full2×2 block. Excess1 is impossible: the unique degree3 row needs degree2 neighbours supported on one common pair of its three columns, leaving the third column degree1. Thus total excess2 occurs in one positive-excess component. In a connected component of size≥3, degree2 rows have disjoint column pairs; equal pairs span C² and split off a2×2 block. If there are s degree2 and b higher rows, `s≤b≤2`, so component size≤4. Size4 would have two degree3 rows covering two disjoint pairs in even numbers, impossible. The component is3×3 with8 entries; all others are2×2.

Thus every pair system of E has nine values: exactly two **heavy** values with3 extensions, and seven **ordinary** values with2. In each cut, the two heavy rows are the two full rows of the unique3×3 block, and the two heavy columns are its two full columns. Their2×2 heavy-row/heavy-column rectangle is therefore entirely nonzero. **All four words in that rectangle are forced E positions.** This fact is used across the three cuts of this same tensor.

## 3. Local degree identities and existence of low-heavy symbols

For any local E symbol a at party i, let m_i(a) count P words using a. The P/E row partition gives, for every j≠i,

`d_i(a):=|π_j(E_a)|=6−m_i(a)`.

So d_i(a) is j-independent, is at least2 (d=1 would make E_a a singleton), and sums to9 over the residual alphabet. Hence each local alphabet has size at most4. Each pair projection has9 values, so every alphabet has size at least3.

Let h_ij(a) count the heavy (i,j) values using a. Counting E_a gives `|E_a|=2d_i(a)+h_ij(a)`, so h_ij(a) is also j-independent. Denote it by h_i(a); it is nonnegative and sums to2. A party is:

- **split** if two distinct symbols have h_i=1;
- **merged** if one symbol has h_i=2.

At most one party is merged: two merged parties would make their two distinct heavy pair values equal the same pair of distinguished symbols.

We need at least two parties having a heavy symbol of degree d=2. In fact there are at least three. Let r_i be the residual alphabet sizes. Calling a P coordinate active when its value belongs to that residual alphabet, the P/E partition gives `6r_i−9` P words active at i and `r_i r_j−9` active at both i,j. Since `k−C(k,2)≤1` for an active count k∈{0,…,4},

`6Σ_i r_i−Σ_{i<j}r_i r_j≤9`.

For r_i∈{3,4}, this excludes `(3,3,3,3)` (left18), `(3,3,3,4)` (15), and `(3,3,4,4)` (11). Thus at least three parties have r_i=4. Their degree multiset is `(2,2,2,3)`. Once merged parties are excluded in §4, each is split and at least one of its two heavy symbols has degree2. Call such a symbol **low-heavy**. A low-heavy symbol a has a five-word E fiber, because `|E_a|=2·2+1=5`.

## 4. A merged party is impossible

Suppose A is merged, with distinguished symbol a. B,C,D are split; label each one's two heavy symbols by0,1. Their heavy pair relations are binary matchings. Swap labels at C,D so that BC and BD are equality matchings; the CD matching is then either equality or inequality.

The forced heavy rectangles of §2 show that E contains `(a,b,c,d)` whenever **at least one** of BC, BD, CD is a heavy pair: in the cut with that opposite pair, the A-containing pair is automatically heavy for either bit of its split partner.

- If CD is equality, every binary triple b,c,d has two equal bits. All eight cube triples are forced. Fixing, for example, b=0 then gives four extensions of the heavy pair (a,0), exceeding3. Contradiction.
- If CD is inequality, the six forced triples have these CD row supports:

  `b=0 : {00,01,10}`,
  `b=1 : {11,01,10}`.

  Each of the two heavy AB rows already has its full allowed3 extensions; the supports cannot be enlarged. But the two heavy rows of one eight-entry3×3 unitary block must both occupy **the same three columns**, whereas these two forced supports differ. Contradiction.

Thus no party is merged. All four are split.

## 5. The three classes of heavy matchings

Label the two heavy symbols at each party by0,1. For each party pair ij, its two heavy values form a matching `x_i xor x_j=e_ij`, where e_ij∈{0,1}. Swapping the bit labels at a party switches its incident edge signs. This is a relabeling only: it need not preserve a preassigned degree label; the actual low-heavy symbol is tracked after relabeling.

There are exactly three switching/permutation classes:

1. **balanced:** all six heavy relations are equalities;
2. **antibalanced:** all six are inequalities;
3. **mixed:** one inequality and five equalities.

To verify completeness, switch so the three edges from party0 are equalities. The remaining triangle has0,1,2 or3 inequalities. Zero is balanced; three is antibalanced after switching party0. One is already a single negative edge. Two share a triangle vertex; switching that vertex removes those two negatives and leaves only its star edge to party0 negative. Party permutations identify the single-negative-edge placements.

For each class let F be the union of the three forced heavy rectangles from §2, viewed as words on the four binary heavy alphabets. Every word of F is an actual E word, not an independently chosen replacement support.

## 6. The mixed class overloads a heavy value immediately

Take the unique inequality at BC, all other relations equality. Fix the heavy BC value `(b,c)=(0,1)`.

- The heavy BC×AD rectangle forces the two words with `(a,d)=(0,0),(1,1)`.
- The AB×CD rectangle forces `(a,d)=(0,1)`.
- The AC×BD rectangle forces `(a,d)=(1,0)`.

Thus this one heavy pair has four distinct E extensions, whereas its multiplicity is3. The mixed class is impossible.

## 7. The balanced class cannot have one low-heavy symbol

In the balanced class, F is exactly the eight even-weight binary four-words (weights0,2,4). Fix a low-heavy symbol at party i with bit a∈{0,1}. Its fiber already contains four F words; the three other bit coordinates each occur twice at0 and twice at1. Both heavy symbols of every other party occur, so its degree2 forces the entire fiber's projection at each other party to be exactly those two heavy symbols.

The fifth word in the fiber must bring the heavy-neighbour bit a from count2 to its required count3, at **each** other party. It would therefore have all four bits a. But that word is already in F. A support cannot duplicate a word, so this is impossible.

At least one low-heavy party exists by §3, so the balanced class is excluded.

## 8. Two low-heavy parties exclude the antibalanced class

In the antibalanced class, F consists exactly of the six binary four-words of weight2.

Fix a low-heavy symbol at party i, first with bit0. Its fiber contains the three F words whose other three bits have weight2. At each other party, the heavy-neighbour bit1 occurs twice and bit0 once. The five-word fiber must use exactly the two heavy symbols in each coordinate, and the two additional words must each add one0 and one1 in every other coordinate. Thus their other-bit triples must be complementary. A weight1 triple cannot be used, since its complement has weight2 and is already in F; the only possible pair is `000,111`.

Therefore this fiber forces both the uniform word `0000` and the **star** W_i,0 with bit0 at i and bit1 at every other party. By complementing bits, a low-heavy symbol1 forces `1111` and the star W_i,1 with bit1 at i and0 elsewhere.

Take low-heavy symbols at two distinct parties i,j, with bits a,b.

- **a≠b.** The pair value `(a,b)` at ij is heavy. F supplies two extensions, and both distinct stars W_i,a and W_j,b have this same pair value and lie outside F. Four E extensions exceed the heavy multiplicity3.
- **a=b.** Let k,l be the other two parties and fix their pair value to `(1−a,1−a)`, which is **ordinary**, not heavy. F supplies one extension. Both distinct stars W_i,a and W_j,a have that value at k,l and lie outside F. Three E extensions exceed the ordinary multiplicity2.

Thus two low-heavy parties are impossible in the antibalanced class. Section3 supplies at least three such parties. This excludes the last class.

## 9. Conclusion and exact boundaries

Merged parties are impossible; each all-split heavy-matching class is impossible. Therefore the assumed N=47,t=27 AME state cannot exist. Every load-bearing word, degree and marginal in the proof belongs to the **same original tensor** throughout.

This conclusion is a WRITTEN candidate until independent review. Combining it with the separately unreviewed N=47→t=27 reduction would exclude N=47; that reduction inherits f113's no-OLS(6)/prior-t≤30 boundary. The present branch proof itself uses no classical import. No global support≥48 disposition, exact minimum, smaller-support witness, formal proof or priority claim is made.

## 10. Tiny exact controls, not premises

`frontier-20261029-heavy-core-controls-v1.py`, SHA-256 `bd23f161a1cdf9cc2e09aafba711f236e9e9761f6de3bca58d48e1e1525db74b`, imports no solver or previous research program. Receipt `frontier-20261029-heavy-core-controls-v1.json`, SHA-256 `cae2ff361400ad3aefe086613fd6cc0e87b57a720549dca910ecbe5246598288`, checks all64 signed K4 patterns:8 balanced,8 antibalanced,48 mixed. It checks64 balanced low-heavy fibers have no five-point completion,64 antibalanced five-point fibers have a unique completion,192 pairs of such fibers overload a pair value, and all8 merged triangle cases have the stated obstruction. Antibalanced and balanced forced cores by themselves obey the pair caps, a nonvacuity check: the low-heavy fiber step is essential.

The69 larger exact-CNF LRAT proofs and Z3 diagnostics are not inputs to §§2–9. They remain frozen corroborating artifacts at their separate encoder/checker trust boundaries; this written proof requires no certificate checker to be accepted as a premise.
