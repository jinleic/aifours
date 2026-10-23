# K5 normal form r3 — explicit imports and clarifications to r2

This r3 package is the unchanged mathematical proof in `K5_RESIDUAL_NORMAL_FORM.r2.md` (SHA256
1a3a47cf939e55fc125b4b70e1e171af6ca28f895a6cdfe4e61b47e8ebb8ca7f) together with this addendum. It addresses the
prompt-only Claude advisory `K5_NORMAL_FORM_CLAUDE_v1.stdout.json` (ACCEPT-WITH-FIXES: two import-documentation
MAJORs, no mathematical counterexample). Parent disposition is still required before any schedule cutover.
No proof of K5 emptiness or full-base CNF UNSAT is asserted.

## 1. Exact bridge hypotheses and reduced class (M2)

For the purpose of the normal-form argument, reduced K5 means a genuine set of five MOQLS(8), in row0 standard
form, in which EACH square has at least one weight3 entry in that frame. This is the m=5 branch of the accepted
Lemma10 reduction: no square was changed to a classical output. A weight3 entry implies non-classicality by the
accepted ray-count argument. There is no order on squares2–5, columns or coordinates in this class definition.

The accepted vector-to-CNF bridge, invoked in r2§4, has EXACTLY the following normalisation hypotheses:

1. row0 standard form;
2. K5 SB2 at(1,0), with supports {1,2,3},{4},{5},{6},{7} in square order;
3. non-strict ascending ROWLEX on Q1's column0 entries in rows2–7, defined in section2 below.

There are no further symmetry-breaking predicates in the pinned K5 formula. The full active families are the
Gram constants, G2,G3,G4,G5, P4 on squares1–5 in frame row0 ONLY, the K5 SB2 units, and this ROWLEX. No fixg,
weight1, generic classical-square variables, other frame-P4, column sort or square order is active.

These imports are explicit in the accepted `K4K5_ENCODING_SOUNDNESS.r3.md`§§2–3.1,5–6, with encoder
`code/gram_a.py` SHA256 bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a and exact flags

    --order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex

The exact argv, including output paths, is in `evidence/gram_dev_v1/GA5L_K5_sb2.map.json` metadata and the
accepted soundness note. The pinned base SHA256 is6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b.
The parent's `review/moqls8-encoder-binding-v1/binding-result.v2.json` binds actual emitted families and counts.

The definition of reduced K5 is invariant under the moves used in r2: common row permutations fixing row0,
common column permutations accompanied by the corresponding computational-basis permutation P_sigma, and square
permutations. These moves preserve the multiset of row0-frame weights in each square, up to square/entry/coordinate
relabelling. Therefore each square still has a weight3 entry after the residual move and the row re-sort.

## 2. ROWLEX and V1, with bit orientation (M1, m1, m2)

`gram_a.py`248–270 implements EXACTLY

    v_i <=_lex v_(i+1), for i=2,...,6,
    v_i=(g_1((0,c),(i,0)))_(c=0,...,7), with False<True,

where coordinate0 is most significant, then1,...,7. The coordinate0 bit is identically False (common column0),
so the effective order is coordinates1,...,7 with coordinate1 most significant. No ordered KEY has column0 row
index0 or1; of course each key still uses row0 as its reference basis. There is no secondary sort key. The order is
non-strict: equal support vectors are allowed. Every row attaining the minimal key in r2§3 has support C_k, so
tie-breaking is immaterial; there is no need to identify a particular vector among ties.

The V1 list is, in this exact coordinate order,

    [g_1((0,c),(2,0)) : c=1,...,7] = [57,106,155,204,253,302,351].

Its root label is the integer sum_{c in support}2^(c-1), NOT a ROWLEX rank. Thus C_1={7}, C_2={6,7},
C_3={5,6,7} have labels64,96,112. The label bit weights run oppositely to the lexicographic significance.
These meanings are independently checked in the parent's encoder-binding receipt and root-cover audit.

## 3. Explicit residual action and precise conclusion (m3–m5)

Write the step1 action as

    Q'_s(i,sigma(j)) = P_sigma Q_s(i,j).

Column0 is fixed, and Q1(1,0)=v is fixed as a vector because v is supported on A and sigma is the identity there.
For s>=2 the singleton support at(1,0) becomes {sigma(s+2)}. Relabel the square s to label sigma(s+2)-2; this is a
permutation of labels2,...,5 and restores all four singleton SB2 supports. The common row sort on indices2,...,7
then restores the exact non-strict ROWLEX import above, without altering rows0,1 or SB2.

The final bridge statement is: the canonical assignment of every such normalised genuine configuration satisfies
F AND the seven units of c064,c096 orc112, respectively. The c112 refutation is an IMPORTED, parent-accepted
certificate, not rechecked in the prompt-only mathematical audit. The two remaining genuine-vector cases are open.
No transfer of arbitrary satisfying assignments or DRAT proofs is used.
