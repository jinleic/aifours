# Genuine-level normal form for the four P1 templates — r1 (UNREVIEWED written argument)

Status: written lemma only. It has had no review, no new computation and no solver run. It does not claim an n=8 theorem or novelty.

Purpose: supply the bridge named as [unreviewed] in `N8_ASSEMBLY.r2.md` §8.2. GB strengthened counterparts GB(B_C ∧ M_s) can only discharge template C if every GENUINE configuration in template C can be moved to one that also satisfies M_s. The accepted NF lemma is about Boolean models of GA's B_C, so it does not apply directly to GB. The same statement at the genuine level also gives an alternative to the Boolean model transformation for GA's S_j (Remark 3).

Primary text: `sources/2607.12933v2.raw.txt`, SHA265851e4…8df9. Lines LF195–225 give the definitions and set isotopy. NF text: `review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md`, SHA8ae0ac01…9e8f; this note reuses its §1 combinatorics and §4 generator list. The residual moves are those of REP `N8_UNIFIED_REVIEW_REPAIRS.r1.md` LF34–38.

## Setting

A **normalised genuine configuration** is five genuine pairwise-orthogonal QLS(8), Q_1..Q_5, with the following properties.
- **Row-0 standard form:** Q_s(0,c) = |c⟩ for every s and c.
- **SB2 pattern at (1,0):** supp Q_1(1,0) = {1,2,3}, and supp Q_s(1,0) = {s+2} for s = 2..5.
- **Template:** Q_1's column-0 supports in rows 2..7 equal template C. Here C ∈ {P1-B1, P1-B2, P1-B3, P1-B5} (TPL §4, the 42 bits).
- **ROWLEX:** the rows are sorted ascending non-strictly by Q_1's column-0 support key.

By U and T16 (accepted, `N8_ASSEMBLY.r2.md` §§2–3), every genuine non-classical five-set reaches such a configuration for one of the sixteen templates.

For each s, define the 7×7 support matrix X_s(i,c) = [⟨c|Q_s(i,0)⟩ ≠ 0], with i, c = 1..7.

## Lemma 1 (support axioms hold for genuine configurations)

The matrices X_1..X_5 satisfy (A), (B) and (C) of NF §1.

**(A) Rows and columns are nonempty.**
- Rows: Q_s(i,0), i ≥ 1, is a unit vector orthogonal to Q_s(0,0) = |0⟩, because column 0 is an orthonormal basis. Its support is therefore a nonempty subset of {1..7}.
- Columns: for c ≥ 1, |c⟩ ⊥ |0⟩ = Q_s(0,0). So |c⟩ lies in the span of {Q_s(i,0) : i ≥ 1}, and some ⟨c|Q_s(i,0)⟩ ≠ 0.

**(B) No two rows, and no two columns, of one X_s meet in exactly one position.**
- Rows: for i ≠ i', Q_s(i,0) ⊥ Q_s(i',0). The inner product is a sum over the common support. With exactly one common coordinate it would be a single nonzero term, which is impossible.
- Columns: U_s[c,i] = ⟨c|Q_s(i,0)⟩ for c, i = 0..7 is unitary, since it changes between two orthonormal bases. So rows c ≠ c' of U_s are orthogonal, and the same one-term argument applies to the column supports of X_s.

**(C) The five X_s are entrywise disjoint.** Take squares s ≠ t, a cell x = (0,c) and a cell y = (i,0), with i, c ≥ 1 so that x ≠ y. Pairwise orthogonality (LF209–215) makes {Q_s(z) ⊗ Q_t(z)} an orthonormal basis. Hence ⟨Q_s(x),Q_s(y)⟩⟨Q_t(x),Q_t(y)⟩ = 0, i.e. ⟨c|Q_s(i,0)⟩⟨c|Q_t(i,0)⟩ = 0. ∎

**Consequence.** X_1 is the P1 template matrix. Rows 1 and 7 are {1,2,3}, row 6 is {2,3}, and rows 2..5 are the B-type list. NF §1 is a purely combinatorial argument from (A), (B), (C) and these X_1 rows, so it applies verbatim. At least the stated number of X_2..X_5 are permutation matrices: ≥1 for B1, B2 and B3, and ≥2 for B5.

## Lemma 2 (the stabilizer moves are genuine moves)

Take a generator pair (σ, ρ) from NF §4:
- σ permutes B = {4,5,6,7} and fixes 0, 1, 2, 3;
- ρ permutes rows 2..5 and fixes 0, 1, 6, 7;
- τ(1) = 1 and τ(s) = σ(s+2) − 2.

Let P_σ be the coordinate permutation unitary. Define

    Q'_{τ(s)}(ρ(i), σ(j)) = P_σ Q_s(i,j).

This new set has the following properties.
- **Isotopic to the old set, up to square relabelling.** It is a common row permutation ρ and a common column permutation σ, which is isotopy (ii). It also applies the same unitary P_σ to each square, which is isotopy (iii). Square relabelling by τ is allowed because a t-MOQLS is a set (`N8_ASSEMBLY.r2.md` §1). The new squares are therefore genuine, pairwise orthogonal, and classical exactly when the old ones are.
- **Row-0 standard form is kept:** Q'(0, σ(j)) = P_σ|j⟩ = |σ(j)⟩. Column 0 stays column 0, because σ fixes 0.
- **SB2 is kept:** row 1 is fixed by ρ, and σ fixes {1,2,3} pointwise. Square s with singleton {s+2} becomes square τ(s), whose singleton is {σ(s+2)} = {τ(s)+2}.
- **The template and ROWLEX are kept.** NF §4 checks that each displayed pair preserves every Q_1 column-0 support mask in its FINAL row. So the 42 template bits hold for Q'_1, and the ROWLEX keys are row-wise identical.
- **The w3 witness is kept:** supp Q'_1(1,0) = σ{1,2,3} = {1,2,3}.
- **Permutation status moves with the label:** X'_{τ(s)} is obtained from X_s by permuting rows with ρ and columns with σ. So X'_{τ(s)} is a permutation matrix iff X_s is.

This is the support-set version of the residual move already accepted in REP LF34–38. It needs no auxiliary-variable extension, because it acts on vectors. ∎

## Proposition (genuine normal form)

Let C ∈ {P1-B1, P1-B2, P1-B3, P1-B5}. Every normalised genuine configuration in template C can be moved, by isotopy and square relabelling, to a normalised genuine configuration in the SAME template C. In the new configuration, X_s is a permutation matrix for some s ∈ Rep(C), where Rep(P1-B1) = {2}, Rep(P1-B2) = {2,4}, Rep(P1-B3) = {2} and Rep(P1-B5) = {2,3}.

A permutation X_s means every Q_s(i,0), i = 2..7, has singleton support in {1..7}. That is exactly the property encoded by the 126 binaries M_s.

**Proof.** By Lemma 1, some X_s (s ≥ 2) is a permutation matrix, and for B5 at least two are. Its label s+2 lies in B. Choose the Lemma 2 moves exactly as NF §4 does:
- **B1 and B3:** the generated action on B is transitive, so the label can be sent to 4, which gives M_2.
- **B2:** the orbits are {4,5} and {6,7}. Send the label to 4 (giving M_2) or to 6 (giving M_4).
- **B5:** the orbits are {4}, {5,6} and {7}. There are two permutation squares with distinct labels, and at most one of them has label 7. A label of 4 gives M_2. A label of 5, or a label of 6 after applying (5 6), gives M_3.

Composites of generator moves are again moves of the Lemma 2 type. ∎

## Remarks and scope

1. **GB.** Suppose the GB necessity note is accepted, i.e. the canonical GB assignment of a normalised genuine configuration in template C satisfies GB(B_C). By the Proposition, the moved configuration also satisfies the M_s binaries. So GB(B_C ∧ M_s) UNSAT for every s ∈ Rep(C) excludes every genuine configuration in template C. This bridge needs GB's necessity, not NF's Boolean model transformation. GB has no ROWLEX, so omitting it only weakens the GB formula.
2. **Input identity.** The six GB strengthened counterparts are exactly these (C,s) pairs; ALL22 GB input identities MATCH (`evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json`).
3. **GA alternative (not a replacement unless accepted).** The canonical GA assignment of the moved configuration satisfies F_one and the 42 units (U's accepted necessity and canonical extension). Because X_s is a permutation, it also satisfies the 126 M_s clauses. So GA S_j UNSAT for all s ∈ Rep(C) would also exclude genuine configurations in template C without NF's Boolean auxiliary re-extension. That would remove the m8 dependency list from the trust base of the four P1 leaves, at the cost of excluding only genuine images rather than proving Boolean UNSAT of B_C. The assembly only needs genuine images (`N8_ASSEMBLY.r2.md` §3). Whether to adopt this alternative is a parent decision; until then, NF remains the accepted route.
4. **What this note does not cover.** It does not certify any formula, and it does not change the D12/S6 status, the proof-digest provenance obligation or the GB proof-certification requirement. It makes no claim about arbitrary Boolean models of B_C.
