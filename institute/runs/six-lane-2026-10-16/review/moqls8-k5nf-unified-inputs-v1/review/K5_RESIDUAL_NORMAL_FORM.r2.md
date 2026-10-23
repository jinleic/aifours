# K5 residual normal form, r2: three cases by a dimension argument; one already excluded

Model-authored proof candidate, frozen for hostile parent review before use. The r1 note is unchanged. This r2 removes
r1's dependence on all122 accepted root exclusions: a pure-B vector exists by a direct ONB projection argument.
It reduces genuine K5 configurations to c064,c096,c112, of which c112 has an accepted root certificate. No new CNF
UNSAT assertion or case deletion is made. The original full-CNF ledger remains unchanged and incomplete.

## 1. Setting and imported mathematics

Take any genuine reduced-class K5 set of5 MOQLS(8). Apply the accepted standard-form and SB2 moves, putting

    Qs(0,j)=|j> for every s,j;
    supp Q1(1,0)=A={1,2,3};
    supp Qs(1,0)={s+2} for s=2,3,4,5.

Put B={4,5,6,7}. Column0 of Q1 is an ONB of C^8; Q1(0,0)=|0>. Every other column0 vector therefore avoids coordinate0.
By W8 every entry has weight≤3. Let v=Q1(1,0), supported on all three coordinates of A (none zero).
The six remaining vectors w_i=Q1(i,0), i=2,...,7, lie in v⊥ and are pairwise orthogonal. They are normalised.
The source tools are the accepted vector→CNF/SB2 bridge in `K4K5_ENCODING_SOUNDNESS.r3.md` and W8/Lemma2 there;
no F3, K4, catalogue or root proof is needed for sections2–3.

## 2. Projection lemma: a pure-B column0 vector exists

Suppose for contradiction that every w_i meets A. Its overlap with v cannot be exactly one coordinate: that would
make <v,w_i> a single nonzero summand, not zero (Lemma2). Thus every w_i has at least two nonzero A-coordinates.
Since its total weight is at most3, its B-component has at most one nonzero coordinate.

For each b in B, ONB completeness of column0 ensures that some w_i has a nonzero b-component. Indeed v and |0>
have zero b-components, whereas the sum over all column0 vectors of the squared b-component is1. Select such a
vector and call it w_b. Since each w_i has at most one B-coordinate, the four selected vectors w_b are distinct.

Let p_b=P_A w_b be their orthogonal projections onto C^A. Each p_b is nonzero (by the contradiction assumption).
For b≠c the B-components of w_b and w_c are supported on different singleton coordinates and hence are orthogonal.
Their coordinate0 components vanish. Therefore

    <p_b,p_c> = <w_b,w_c> - <P_B w_b,P_B w_c> = 0.

Moreover <v,p_b>=<v,w_b>=0. Thus four nonzero pairwise orthogonal vectors p_b lie in the TWO-dimensional space
C^A ∩ v⊥, a contradiction. This proves that at least one w_i has support contained in B.

## 3. Residual normal form: c064,c096 or c112

Among all pure-B supports of w_i, let T have minimum cardinality k. By section2 and W8, k belongs to{1,2,3}.
Let C_k be the k rightmost coordinates of B:

    C_1={7}, C_2={6,7}, C_3={5,6,7}.

Choose sigma∈Sym(B), fixing0,1,2,3, with sigma(T)=C_k. Apply simultaneously to all squares the common column
permutation j→sigma(j) and P_sigma|j>=|sigma(j)> on the vectors, then relabel squares2,...,5 to restore their
(1,0) singleton supports to{4},{5},{6},{7} in order. Square1 stays fixed.

These moves preserve QLS conditions, mutual orthogonality, row0 standard form and reduced K5. The standard-form
check is explicit: the old row0 entry |j> moves to column sigma(j) as |sigma(j)>. Cell(1,0) stays fixed; Q1's support
A is fixed and the other four supports are merely permuted before square relabelling. Row0-frame support weights
and weight3-containingness of every square are preserved (up to permutations of entries/coordinates).

Finally permute rows2,...,7 commonly to restore the K5 ROWLEX order. The selected vector now has support C_k and
is lexicographically minimal among these six vectors:

- a support meeting A is larger, since it has an earlier1 among positions1,2,3 where C_k has0;
- a pure-B support has cardinality≥k by the choice of k, and the rightmost-k bitvector is the unique lexicographic
  minimum among subsets of B of cardinality≥k (coordinate4 is most significant, then5,6,7).

Consequently the row sort puts a vector with support C_k at(2,0), while fixing rows0,1 and preserving SB2. Ties may
be resolved with the selected vector first. The normalised configuration therefore lies in root c064,c096 or c112
respectively (bit k−1 in the V1 list is coordinate k). ROWLEX is RESTORED after sigma, not assumed invariant under it.
There is no asserted syntactic automorphism of the ROWLEX CNF and no transfer of arbitrary SAT models/DRAT proofs.

## 4. Accepted c112 exclusion and exact remaining obligation

The accepted vector→CNF bridge sends every such normalised K5 configuration into the SAME unconditional base F,
SHA2566ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b.
For c112 the unit list is[-57,-106,-155,-204,253,302,351], leaf CNF SHA256
c95a34c2ed7cd726f5fbfcbbcdb10a125fa8adf4833fef093844b13a565bcd83 (5740237clauses).
Its retained certificate is `evidence/k5_split_v1/all/cube112.drat.zst`, SHA256
b6b1e6d23c5f4a1bbd7630027463d3bc2f398fb245ff6b450a718fd3305d14bd; decompressed proof SHA256
d5fd6fd0fff305ab34a2aed064836d7682ee07ee253b25fa93dc93a525af63c2 (189627541bytes).
It is one of the122 parent-replayed root refutations; provenance is pinned in
`evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.json` (65f6e0dd…3b5e), and the parent replay receipt is
`review/moqls8-k5-root-parent-replay-v1/final-a1/FINAL.json` in the run directory.

Hence complete independently replayed refutations of the c064 and c096 subtrees, together with this normal-form
proof and c112's accepted certificate, would exclude genuine reduced K5. This is NOT yet complete: those two
subtrees remain open. It is not a proof that F is UNSAT from only these three root certificates, because arbitrary
non-realizable support models need not admit the vector projection argument.

The existing 128-root Boolean cover is not rewritten; no skipped root is marked UNSAT. A semantic-coverage receipt
would separately cite this lemma, the accepted necessity bridge, c112's proof and the two complete subtree covers.
No approved schedule changes before explicit parent approval.
