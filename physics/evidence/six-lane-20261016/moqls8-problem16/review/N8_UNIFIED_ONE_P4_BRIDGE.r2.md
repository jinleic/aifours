# Unified n8 bridge, r2: any counterexample yields one of16 weakened-F template assignments

Frozen BEFORE generating any weakened-F CNF. Supersedes the less-specific r1 note, which is unchanged. Preparation
and the later16 strict runs were approved by the parent; order remains current c064 root,13 old-F templates,16
weakened-F templates. No target exclusion is claimed before the independent reviews and parent certificate replay.

## 1. Exact formula and deletion pins

F is the unconditional generic-five-Gram base `evidence/gram_dev_v1/GA5L_K5_sb2.cnf`, SHA256
6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b,509915vars,5740230clauses. Define F_one by
removing ONLY the four P4 at-least-one-flag clauses for squares2–5 in frame row0. Retain Q1's P4-ALO, all one-way
w3 clauses, G2–G5, Gram constants, K5-form SB2 and Q1 ROWLEX. There is no weight1 condition, L-sort, classical net,
fixg, or P4 frame other than row0. The accepted active-family/ROWLEX specification is made explicit in
`K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md` and the accepted `K4K5_ENCODING_SOUNDNESS.r3.md`.

Indices below are ZERO-based clause indices excluding the DIMACS header. Hashes are SHA256 of the exact ASCII
clause bytes INCLUDING the terminating newline. One-based clause number=index+1; text-file line=index+2.

| square | operation | index | exact clause-line SHA256 |
|---|---|---:|---|
|1|KEEP|5733728|373d8b86cfb58475c193634b334c33126b14e952aa5dd96e2d38216be5137281|
|2|DELETE|5735297|80fffa942be4520652ee48dc1fbfb7d4906e4f7f3264b1dbd6cf5bbe5c3f85ba|
|3|DELETE|5736866|f5563e41d95ff0c6a2da0a5847ec55dc00d44c000b4ec7d12d704cbfe2ee4506|
|4|DELETE|5738435|bf50e1c047931470b66afb57a73e446358290e003c22634539deb6ccc1c6c691|
|5|DELETE|5740004|d73bdfbcb8b411d5e5cf8dbd4339a78276b11042d82173edf70ea8ff97e4d1d7|

The source was read/hash-bound once. Each of these five56-literal positive clauses was independently identified
through every literal in the full K5 name table as precisely the56 w3 flags of that square, frame row0, with one
flag for every off-row0 cell. Name-table SHA256 b8423861d03b6e837317c12ef1f2f297301d1bfbbfb7852b93ccec29b85e2522.
`evidence/UNIFIED_ONE_P4_DELETIONS_v1.json` records all index conventions and pins. All other clause bytes/order
remain identical. The new header will be509915vars,5740226clauses; no weakened formula has been generated yet.

Labels2–5 are arbitrary QLS here, classical or non-classical. Their retained w3 implications admit the all-false
flag assignment. No other family requires them to have a weight3 entry.

## 2. Exact A8 import and acceptance

Imported theorem A8: for a genuine set of FIVE MOQLS(8) in any row0 standard form, if every entry of every square
has weight at most2 in that frame, the set is wholly classical (indeed all weights are1 in that form).

Parent authority (run-relative): `review/moqls8-k1k2-parent-verdict.md`, SHA256
919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9:

- line13, Proof outline item1, explicitly states W8 and TheoremA8, including all-weights<=2 implies all-weights1;
- line9 states that the parent read all of the revised proof, bound every review fix, and that r2 imports the
  unchanged A8 proof from r1;
- line36 gives the parent CORRECTNESS-ACCEPTED disposition for that package (partial original result, not n8 solved).

The accepted proof package there is r1 SHA094dab60c7972c956f90c8cf0984c47f79376d0018192457c84adab6e224ff3c plus
r2 SHAd36e646cf0e8faadd5e6131615c6694cbf4187c10abbb6bf54aa17083ab72d86. A8 is not re-proved or newly certified
by the current bridge. This use of A8 does not import the Egan–Wanless counts needed for later K1/K2 corollaries.

## 3. Every genuine non-classical five-set normalises into F_one

Let S be ANY genuine set of5 MOQLS(8) that is not wholly classical. Standardise row0 of each square by its own
unitary; mutual orthogonality, classicality and per-square ray counts are preserved. A8 implies that some entry
has weight at least3. W8 bounds every entry's weight by3, so the chosen weight is exactly3.

Relabel its square Q1. The entry occurs at(i,j), i!=0, since all row0 entries have weight1. Commonly permute rows1–7
to put its row at1; commonly send column j to0 by sigma and apply P_sigma to every square's vectors. This keeps row0
standard form: the old |k> moves to column sigma(k) as |sigma(k)>. The selected support avoids its own column
coordinate by row/column orthogonality, hence avoids0 after this move.

At the aligned cell(1,0), the five supports are pairwise disjoint (Prop1 with each row0 basis cell), nonempty, and
avoid0. Since Q1's support has size3, the other four must be singletons and these five supports partition the seven
available coordinates. A further common coordinate/column permutation fixing0 maps them, in square order, to
{1,2,3},{4},{5},{6},{7}. Thus the exact original SB2 predicates hold, regardless of which other squares are classical.
Finally sort rows2–7 commonly by Q1's column0 support key, restoring the exact ascending non-strict ROWLEX without
moving row0 or the weight3 witness at(1,0). No L-sort is imposed or used.

Read off the canonical Gram/auxiliary assignment as in the accepted encoder bridge. G2–G5 and constants are
necessary for ALL QLS, not only non-classical ones. Q1's P4-ALO is satisfied: its flag at(1,0) may be true, and its
three overlaps satisfy every6-of8 clause. For squares2–5 set every w3 flag false; their one-way implications all
hold and their ALO clauses are precisely the four clauses removed. All other auxiliaries take their defining values.
The resulting assignment satisfies F_one. No Lemma10 reduction, fixed non-classical count, all-frame P4 or
classical catalogue is used in this normalisation.

## 4. Why the same component theorem and ALL16 templates apply

`K5_COLUMN0_TEMPLATE_COVER.r1.md`§1 proves both row and column degrees at most3 for Q1's column0 transition using
only: five aligned QLS, G2 support disjointness, nonempty overlaps in each row/column ONB and seven available frame
positions. This is valid for classical and non-classical members alike. Its§2 component theorem uses only unitary
support orthogonality, the degree bounds and component rank balance. Its§§3–4 use only Q1's fixed weight3 support
and the residual Sym(A)xSym(B) column/coordinate action, square2–5 relabelling and common row2–7 sort.

Every one of those hypotheses is present for the normalised S in§3. P4 on squares2–5 and reduced-K5 membership
are not used. The residual moves preserve F_one's NECESSITY hypotheses: Q1 still has its weight3 witness, whereas
other-square classicality is unrestricted. Thus the genuine configuration normalises into one of the16 complete
Q1-column0 support templates. Its canonical assignment satisfies F_one plus that template's42units.

## 5. Exact consequence and remaining gates

Independent verified UNSAT of ALL16 such formulas, together with this bridge, the accepted A8/original necessity
imports and the reviewed template theorem, would prove every set of5 MOQLS(8) is classical: a counterexample would
yield a satisfying assignment of one refuted formula. This is the FULL n8 instance of Problem16, not a reduced class.

The three c112 templates must be run afresh: c112's old certificate refutes the stronger all-five-P4 formula, so
it cannot be imported for F_one. The13 old-F template certificates remain separate restricted results. F_one+42units
has5740268clauses for every one of the16 cases. No arbitrary SAT model is asserted to yield genuine vectors, and no
claim of whole-base CNF UNSAT is needed. No target theorem is asserted before both reviews, complete per-case
receipts and the parent independent replay/disposition.
