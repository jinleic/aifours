# P1-B3 simultaneous-pair genuine-GB reduction — CANDIDATE v1

Status: written conditional reduction, not parent-accepted and not a refutation. Frozen at 2026-10-19T11:53:00-0700.

This audits and expands ONLY the B3 part of the existing unreviewed `P1_PAIR_REFINEMENT_OPTION.r1.md` [P]. It does not rediscover its pair table, rely on its orbit-enumeration script, or claim novelty. No CNF, source, binder, numerical probe, solver, checker or CLI review was created or run for this note. The three surviving GB UNKNOWNs and GB15/18 remain unchanged.

## 1. Setting, exact root and claim

Let Q_1,...,Q_5 be genuine, pairwise-orthogonal QLS(8). Assume the accepted U/T16 normal-form hypotheses, specifically:

1. Q_s(0,c) = |c> for every square s and column c.
2. At cell (1,0), Q_1 has support {1,2,3}, while Q_s has singleton support {s+2} for s=2,3,4,5. These are support assertions; an unspecified unit phase on a singleton is harmless.
3. The exact P1-B3 template fixes Q_1 column-0 supports T_i as follows:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| T_i | {1,2,3} | {6,7} | {6,7} | {4,5} | {4,5} | {2,3} | {1,2,3} |

Row 1 comes from SB2; the 42 signed template units fix rows 2 through 7, including all absent coordinates in {1,...,7}.
4. Rows 2 through 7 are in ascending non-strict ROWLEX order by Q_1 column-0 support bits, coordinates 0,...,7, coordinate 0 most significant, False < True, with no secondary key. Rows 0 and 1 are fixed.

For i,c in {1,...,7}, put X_s(i,c)=1 iff <c|Q_s(i,0)> is nonzero. A permutation support means that X_s is a permutation matrix. Write l=s+2 for the label in B={4,5,6,7} belonging to square s>=2.

Let GB_B3 denote the exact GB template formula in [J], entry `P1-B3`: 3,803,745 variables, 17,025,620 clauses, 350,551,015 bytes, SHA256 `f8fd0a51d8ff30069c105b52c20fdc02ad3f22a15a500e95014e5aac4954d487`. Its flags are `--order 8 --quantum 12345 --ngeneric 0 --p4 1 --sb2 --g5`; it has no fixed Gram data, classical data, other-square P4 or ROWLEX. [J] binds its 42 units to the displayed row-2..7 supports. GB_B3 is an input identity, NOT a qualified UNSAT fact.

For s=2,...,5, M_s is the conjunction of the 126 at-most-one clauses

    not g_s((0,c),(i,0)) or not g_s((0,d),(i,0)),
    i=2,...,7 and 1<=c<d<=7.

These use GB's OWN primary names/IDs, namely `1568(s-1)+49c+7i-5` [J,E]; they are not GA's offset-by-one IDs. M_s adds no variables and imposes no whole-square classicality. Only "permutation X_s implies M_s" will be used, not its converse without nonemptiness.

**Candidate claim.** There is a genuine normal-form configuration Q' in the SAME P1-B3 template, obtained by the accepted row/column/unitary moves and square relabelling, whose canonical GB assignment satisfies at least one of the following two conceptual conjunctions:

- H_23 := GB_B3 AND M_2 AND M_3;
- H_24 := GB_B3 AND M_2 AND M_4.

These are mathematical descriptions, not newly generated/bound DIMACS files. Consequently, if BOTH H_23 and H_24 are unsatisfiable, no genuine configuration in the stated P1-B3 normal form exists. No conclusion about arbitrary Boolean models of GB_B3, or Boolean UNSAT of GB_B3 AND M_2, is asserted.

## 2. Two permutation supports: a direct counting proof

The following support facts for genuine configurations are the accepted [G,E] bridge premises; the argument is recalled to make the stronger simultaneous choice explicit.

(A) Every row and column of each X_s is nonempty. Column 0 of Q_s is an orthonormal basis with Q_s(0,0)=|0>; its remaining seven vectors form a basis of the orthogonal complement of |0>.

(B) Two different rows of X_s cannot meet in exactly one coordinate: the corresponding orthogonal vectors would have a one-term nonzero inner product. The analogous assertion for two columns follows from unitarity of the change-of-basis matrix. Only the row assertion is needed for the count below.

(C) The five X_s are entrywise disjoint. For s!=t and distinct cells x=(0,c), y=(i,0), pairwise QLS orthogonality gives

    <Q_s(x),Q_s(y)> <Q_t(x),Q_t(y)> = 0.

Since row 0 is standard, this says X_s(i,c) and X_t(i,c) cannot both be one.

A non-permutation 7-by-7 support obeying (A),(B) has at least nine ones. With at most seven ones it is a permutation by (A). With eight, exactly one row would have degree two and six would be singleton rows. Their singleton columns are distinct, because equal singleton columns give a row-intersection of size one. No other row may meet any of those six columns, again by (B). The supposed degree-two row has only one column left, a contradiction.

The displayed X_1 has 16 ones. If three of X_2,...,X_5 were non-permutation, their total with X_1 would be at least

    16 + 3*9 + 7 = 50,

whereas (C) permits at most 7*7=49 ones in total. Therefore at least TWO of X_2,...,X_5 are permutation matrices. This is the B3 instance of the accepted NF section-1 bound [N], and of correction N2 in [E], not a new finite search. If more than two are permutations, select any two.

## 3. Three genuine generator moves and exact preservation

All cycles below act on named indices and fix every index not displayed. The accepted B3 generator pairs [N,G,E] are

| name | coordinate/column sigma | row rho | square tau on {2,3,4,5} |
|---|---|---|---|
| a | (4 5) | identity | (2 3) |
| b | (6 7) | identity | (4 5) |
| c | (4 6)(5 7) | (2 4)(3 5) | (2 4)(3 5) |

In every row, tau(1)=1 and tau(s)=sigma(s+2)-2 for s>=2. With P_sigma the coordinate-permutation unitary, define

    Q'_{tau(s)}(rho(i),sigma(j)) = P_sigma Q_s(i,j).

The following checks apply simultaneously to all squares, not just to one selected square.

**Genuineness and allowed moves.** A common row permutation and a common column permutation preserve every row/column ONB and the tensor-product ONBs. Applying P_sigma to each square preserves them by unitarity (each pair uses P_sigma tensor P_sigma). These are the accepted isotopy moves, followed by harmless relabelling of the set of squares.

**Row 0 and column 0.** Each rho fixes 0. Thus Q'_{tau(s)}(0,sigma(j))=P_sigma|j>=|sigma(j)>. Each sigma fixes 0, so column 0 stays column 0.

**SB2 and the Q1 witness.** Each rho fixes row 1; each sigma fixes 1,2,3 pointwise. Q'_1(1,0) therefore retains the same three-coordinate witness. For s>=2, support {s+2} becomes {sigma(s+2)}={tau(s)+2}, precisely the singleton demanded by the NEW square label. No phase or extra P4 condition is introduced.

**All 42 template bits and ROWLEX.** It is enough to check sigma(T_i)=T_{rho(i)}. For a and b, both sets {4,5} and {6,7} are fixed as sets, and rho is the identity. For c, sigma interchanges {4,5} with {6,7}, while rho sends rows 2,3 to 4,5 and rows 4,5 to 2,3, respectively. Rows 6 and 7 have T_6={2,3} and T_7={1,2,3}, fixed pointwise by sigma and at fixed row indices. Thus the support at each FINAL row is exactly its original T_i, including zeros. Coordinate 0 remains absent in rows i>=1 by column orthogonality to |0>. Every full eight-bit ROWLEX key is consequently identical at its final row; rows 2..7 remain sorted with no appeal to arbitrary-CNF automorphism.

**Both permutation supports move together.** Directly from the genuine move,

    X'_{tau(s)}(rho(i),sigma(c)) = X_s(i,c).

So every selected permutation matrix remains a permutation matrix, with its label l=s+2 sent to sigma(l). This is simultaneous: choosing a move to handle the pair does not destroy the first selected permutation.

The product ab has sigma=(4 5)(6 7), rho=identity and tau=(2 3)(4 5); a and b commute. Preservation for it also follows from the generator checks, or directly from the same setwise support check.

## 4. All six unordered pairs: explicit maps, no group enumeration

Pick two distinct permutation-square labels. This is one of the six unordered pairs below. The displayed action sends it to {4,5} or {4,6}:

| selected labels | move | image of the two labels (in displayed order) | representative | rho | tau |
|---|---|---|---|---|---|
| {4,5} | identity | 4->4, 5->5 | {4,5} | identity | identity |
| {6,7} | c | 6->4, 7->5 | {4,5} | (2 4)(3 5) | (2 4)(3 5) |
| {4,6} | identity | 4->4, 6->6 | {4,6} | identity | identity |
| {4,7} | b | 4->4, 7->6 | {4,6} | identity | (4 5) |
| {5,6} | a | 5->4, 6->6 | {4,6} | identity | (2 3) |
| {5,7} | ab | 5->4, 7->6 | {4,6} | identity | (2 3)(4 5) |

This table is verified by the displayed literal images; it does not rely on a computed group order. The three generators preserve the block partition {{4,5},{6,7}}, so within-block pairs cannot mix with cross-block pairs. The table nevertheless supplies a map for every pair, which is all the coverage argument needs. Labels {4,5} mean squares {2,3}; labels {4,6} mean squares {2,4}. By section 3 both final squares are permutation supports. Therefore M_2 and M_3 hold together in the first representative, and M_2 and M_4 hold together in the second.

## 5. Fresh canonical GB auxiliaries; no Boolean-model transfer

Use the accepted GB necessity theorem [G], read with [D,E], on the transformed GENUINE configuration Q'. Its row-0 form, SB2, Q1 weight-three witness and SAME template have all just been checked. GB has no ROWLEX, but the stronger normal-form condition was preserved anyway.

Set each GB primary to the actual zero/nonzero Gram relation of Q'. Set the TRUE constant to true; assign each conjunction its exact Boolean AND, each counter/threshold variable its semantic prefix predicate, and each singleton auxiliary its semantic singleton predicate, as in [D] section 2. The accepted necessity theorem states that these canonical values satisfy the complete GB base: the genuine tensor-orthogonality, ONB, Parseval and same-ray facts give G2 through G5, and the Q1 witness gives its only P4 condition. The SAME 42 template units then give GB_B3. No old auxiliary values or GA IDs are transported, and no encoder is executed.

For each selected final square s, permutation support implies at most one true primary among each row's seven bits. Hence every binary in M_s is true in this same canonical assignment. Adding the two M_s tails introduces no new auxiliaries and cannot create a conflict between two different auxiliary extensions: there is just the one canonical assignment already satisfying GB_B3. Section 4 supplies either H_23 or H_24, proving the candidate claim.

## 6. Conditional exclusion and exact limits

Assume, as mathematical hypotheses, UNSAT(H_23) and UNSAT(H_24). A genuine P1-B3 normal-form configuration would yield one canonical assignment satisfying one of them by sections 2 through 5, a contradiction. This proves ONLY the stated conditional genuine-level reduction.

Neither UNSAT hypothesis is established here. No pair DIMACS is generated, no new byte/hash binding or proof certification exists, no accepted six-input contract is amended, and the old single-input B3.M2 UNKNOWN remains UNKNOWN. Adoption would require a separate parent decision/amendment and the full exact-input certification obligations; this note alone changes no count or A10/A11 status.

In particular:
- there is no transformation of an arbitrary Boolean GB model and no proof that GB_B3 or GB_B3 AND M_2 is Boolean-UNSAT;
- this does not substitute already-qualified GA certificates for independent GB evidence;
- B2 is untouched: its support count guarantees only one permutation square, so this two-square argument does not close either B2 representative;
- the shared U/T16, WMAN and NF combinatorial/stabilizer imports are not independently checked merely because GB has independent CNF construction;
- no unconditional n=8 theorem, counterexample or novelty/priority conclusion follows.

## 7. Source and authority pins

[G] is the sole parent authority for accepted GB necessity/genuine normal-form implications, at its stated conditional scope. [N] supplies the shared combinatorics and generators, read as imported in [G,E], not a GB Boolean-discharge rule. [P] is the old UNREVIEWED pair proposal being audited. The current parent authorization permits written derivation/review-packet preparation only.

- [P] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/P1_PAIR_REFINEMENT_OPTION.r1.md`, SHA256 `cf4ad886d418701d198c16036a14d9e98b8cfe9fa1c058175206d2a5f724ec3d`.
- [G] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md`, SHA256 `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`.
- [N] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md`, SHA256 `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`.
- [BR] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/GB_NF_GENUINE_BRIDGE.r1.md`, SHA256 `1a352d364a2e2c68a344735537db7e6f10861e01d520cf75dcbef7a61fbf504b`.
- [D] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/GB_ONE_P4_NECESSITY.r2.md`, SHA256 `b9b4a595ca50b1334419d8584edc128e852dd4f206cd21fc5a07a793a2e72365`.
- [E] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/GB_REVIEW_ERRATUM.r2.md`, SHA256 `a2d3b9b3cd7bfe1cb4ffe20bbfbaf80856051ab6a4e743ffa86591513fbe407d`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [SCOPE] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-pair-written-route-parent-decision-v1.json`, SHA256 `2be99c4f1b499114cf0fa003c428be0f707d3108ab986f9bc03fc0c671becde8`.
