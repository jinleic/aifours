# K5: residual S4 normalisation reduces the six unresolved vector cases to two

Model-authored proof candidate, 2026-10-17. This does NOT declare any new CNF leaf UNSAT, change the frozen full
128-root ledger, or solve K5. It is a proposed additional mathematical bridge, pending parent hostile review and
explicit approval before it is used to reduce the remaining computation.

## 1. Setting and exact imported machine fact

Let Q1,...,Q5 be a genuine reduced-class K5 set of 5 MOQLS(8), in row-0 standard form, with the accepted SB2 and
ROWLEX normalisations of `K4K5_ENCODING_SOUNDNESS.r3.md`:

- Qs(0,j)=|j> for all s,j;
- at (1,0), supports are A={1,2,3}, {4}, {5}, {6}, {7}, in square order;
- the overlap-support vectors v_i of Q1(i,0), i=2,...,7, are nondecreasing in the bit order 0,1,...,7, where bit0
  is most significant (and identically0 here).

Put B={4,5,6,7}. Every column-0 support avoids coordinate0. Each square has a weight-3 entry in the row-0 frame
by the definition of reduced K5. W8 bounds every entry's weight by3.

Imported machine fact: the 122 parent-replayed root refutations of the unconditional K5 CNF
`6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b` exclude every assignment of
V1=[57,106,155,204,253,302,351] except indices

    16, 32, 48, 64, 80, 96

whose Q1(2,0) supports are respectively {5}, {6}, {5,6}, {7}, {5,7}, {6,7}.

Machine imports: parent `review/moqls8-k5-root-parent-replay-v1/final-a1/FINAL.json` (122/122 replay PASS, as
reported by the parent); independent partition/provenance audit `review/moqls8-k5-root-cover-audit-v1.md`;
lane `evidence/k5_split_v1/ledger/LEDGER.v003.json`, SHA b9b3fc67fe5abdf6be197b7cb642226bc1c5f344348edb068b6388c02bc8b14b;
retained-proof manifest `evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.json`, SHA
65f6e0dd47c582b108906aa808e3d2453ec45ac3b8bbfa19c01e586e989c3b5e.

In particular every such genuine normalised K5 configuration has a pure-B column-0 entry in some row2,...,7
(its current row2), of weight1 or2.

## 2. Residual move and proof of the new normal form

Choose, among the pure-B supports of Q1(i,0), i=2,...,7, one T with minimum cardinality k. The preceding machine
fact implies that this set of supports is nonempty and k is1 or2.

Let C_k be the k rightmost coordinates: C_1={7}, C_2={6,7}. Choose sigma in Sym(B), extended by the identity on
{0,1,2,3}, with sigma(T)=C_k. Apply to ALL squares the following vector-level moves:

1. Move column j to column sigma(j), and apply P_sigma|j>=|sigma(j)> to every entry of every square.
2. Relabel squares2,...,5 so their supports at (1,0) are again {4},{5},{6},{7} in this order; square1 stays fixed.
3. Permute rows2,...,7 commonly so that Q1's column-0 support vectors are again lexicographically nondecreasing.
   Resolve ties by putting the chosen entry first among entries with its support.

These moves preserve the QLS conditions and mutual orthogonality. Step1 keeps row-0 standard form because the
entry moved into column sigma(j) is |sigma(j)>. Since sigma fixes0 and A, it fixes cell(1,0), keeps Q1's support A
there, and only permutes the other four singleton supports; step2 restores SB2. Each square's row-0-frame weights
are preserved, up to reindexing of entries/coordinates, so every square is still an untouched weight-3-containing
square: the set is still in reduced K5. Step3 fixes rows0,1, and so keeps SB2 and row-0 standard form.

We now prove that step3 places a support C_k at row2. All column-0 supports avoid0. Any support meeting A has a1
at a position1,2 or3 at which the C_k vector has0; hence it is lexicographically larger than C_k. Every other
support is a nonempty subset of B, and its cardinality is at least k, by the definition of k (sigma preserves
cardinality and the property of being pure-B).

Elementary bit-order lemma: among the subsets of B of cardinality at least k, the vector of C_k is the unique
lexicographic minimum. For k=1 it is0001; for k=2 it is0011, in coordinate order4,5,6,7. More generally, if another
subset has a1 earlier than the first1 of C_k it is larger; otherwise it has to contain all k rightmost positions
to have cardinality at least k, so it equals C_k.

The chosen entry has support C_k after step1. Thus it can be placed first by step3. The resulting genuine K5
configuration satisfies the SAME K5 SB2 and ROWLEX normalisations and belongs to root c064 (if k=1) or c096 (if k=2).
This proves the new normal form.

Crucial distinction: ROWLEX is NOT claimed invariant under step1. It is re-established by the still-available common
permutation of rows2,...,7, AFTER the coordinate permutation. There is no proposed syntactic automorphism of the
ROWLEX CNF and no transfer of arbitrary SAT-model assignments or DRAT proofs between these six roots.

## 3. Consequence, and what remains unproved

If the genuine classes admitted by roots c064 and c096 are excluded (e.g. by strict, independently replayed
refutations of their CNF subtrees), then K5 is empty: any K5 set first reaches an accepted SB2/ROWLEX form; the122
root exclusions force a pure-B entry of weight at most2; the new normal form puts it in c064 or c096, contradiction.

This implication depends on the122 accepted root refutations AND the accepted vector-to-CNF necessity bridge.
It does not depend on K4 or F3. It does not imply that the full base CNF is UNSAT from only these two root subtrees:
non-realizable support models outside the newly normalised vector image have not been addressed. Therefore:

- the original full-CNF ledger remains unchanged and incomplete;
- c016,c032,c048,c080 are NOT silently marked certified/UNSAT;
- a new semantic-coverage receipt would explicitly cite this normal-form lemma, the122 root proof pins, and the
  complete c064/c096 subtree receipts, rather than claim a tautological Boolean cover;
- no reduction of the approved compute schedule takes effect before parent approval.

## 4. Independent audit obligations

Check the residual moves (including square relabelling), the row0/P4/SB2 invariants, the bit-order orientation, the
minimum-cardinality argument, and the original target quantifiers. A small exhaustive bit-pattern control may check
the bit-order lemma and restoration of the rightmost-k minimum, but does not replace this vector-level proof.
