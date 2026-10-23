# Unified one-P4 bridge/deletion specification: versioned review-repair overlay r1

Original BR2 and DEL-v1 remain unchanged. This overlay closes the7 bridge and3 deletion-manifest MINORs in parent
`moqls8-k5nf-unified-claude-v1.note.md` (SHA2566200c8d7b72a0335d1bd2bc11b98226ea4439d64ce7ab425fd3d7468477d98f5).
Codex's static disposition is ACCEPT/zero findings (`moqls8-k5nf-unified-codex-v1.note.md`, SHA256
e439c8c0f2c14b5dbf5a3ddc881966495372d7610c784ef54370f8439a47bdb3). These are written-proof/specification reviews,
not solver results, independent replay or a parent theorem disposition. No n8 exclusion is asserted.

Pins: BR2 c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3; DEL-v1
4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6. Earlier generic semantic repairs
`K5_SEMANTIC_REVIEW_REPAIRS.r1.md`41395137…1022 continue to apply; nothing here reopens a fixed finding.

## 1. Property-form T16 (BR2 minor3; no reduced-K5/c112 interface imported)

**T16.** Let Q1,...,Q5 be a genuine pairwise mutually orthogonal set of five QLS(8), all row0-aligned:
Qs(0,c)=|c>. Suppose their(1,0) supports are A={1,2,3},{4},{5},{6},{7} in square order. The Q1 column0 transition
U[k,i]=<Q1(0,k),Q1(i,0)> is unitary and has BOTH row and column degrees at most3: in either row0 or column0 frame,
the five aligned nonempty supports are disjoint by Prop1, and the common collinear frame cell excludes one of eight
positions, leaving seven; 7-4=3 bounds each support.

Then there exists a common column/coordinate permutation in Sym(A)xSym(B), B={4,5,6,7}, a relabelling of squares2–5,
and a common row2–7 permutation, after which the same support normalisation and ascending non-strict ROWLEX hold
and the six Q1 column0 supports in rows2–7 are one of the SIXTEEN lists in
`K5_COLUMN0_TEMPLATE_COVER.r1.md` (SHA2561ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a).

This is a PROPERTY-FORM restatement of its unitary-component/canonicalisation proof. The proof uses only the
hypotheses just given. It does not use reduced-K5 membership, P4 on squares2–5, or non-classicality of those squares.
The old-F reduced-K5 conclusion and the13-case/c112 certification interface (TPL111–113,117–120) are expressly NOT
imported for F_one. All16 unit lists are pinned in the weakened manifest
355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74; every case is required anew.

## 2. Explicit residual moves and ROWLEX (BR2 minors4,7)

For sigma fixing0 and preserving A,B as SETS, define Q'_s(i,sigma(j))=P_sigma Q_s(i,j). Then
Q'_s(0,sigma(j))=|sigma(j)>, and supp Q'_1(1,0)=sigma(A)=A. Q1(1,0) is NOT claimed fixed as a vector under Sym(A).
SB2, Q1's kept ALO and its28 witness implications depend only on that support set, not its coefficients/phases.
Relabel s>=2 to sigma(s+2)-2, a bijection because sigma(B)=B; the set is unordered and pair orthogonality is symmetric,
so relabelling rho is explicitly allowed. Finally IMPOSE ROWLEX by commonly sorting rows2–7, fixing rows0,1.

The key is exactly(g_1((0,c),(i,0))) for c=0,...,7, coordinate0 most significant, False<True, ascending NON-STRICT,
no secondary key; bit0 is identicallyFalse. This comes from gram_a.py248–270, not C9. Source encoder SHA256
bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a. Impose/establish, not an assumption of prior sort.
The initial witness avoids its old column j specifically by column-j orthogonality to(0,j)=|j> (source rule#2).

## 3. Fully explicit canonical auxiliary values (BR2 minor1,7)

Take actual Gram support values and exact self/line constants. Set b3/c4 to the AND of their two defining operands,
u5 to its exact singleton-frame-support condition, and lexeq to prefix equality of the sorted Q1 keys. G2 holds
for every orthogonal pair; G3–G5 and constants hold for every QLS. Include all AND/u5/lexeq definition clauses in
the family list (they are retained byte-for-byte, not removed by this weakening).

Set w3_1(frame0,cell(1,0))=TRUE. Its support is{1,2,3}; every6-subset K of{0,...,7} meets that support, since the
complement of K has only2elements. Hence each of the28 implications is satisfied, and the kept Q1 ALO is satisfied.
Set EVERY OTHER w3 flag FALSE, including all other Q1 flags and every flag of squares2–5. Their one-way clauses
then hold. The only positive occurrences of each square's flags were its ALO (gram_a.py242–247); only the four
squares2–5 ALOs are removed. Thus every retained clause has a canonical satisfying extension whenever the vectors
satisfy the hypotheses. "Defining values" is not used for the one-way w3 flags.

## 4. Specification/freeze versus observed generation (BR2 minor2; DEL minors1–3)

BR2 and DEL-v1 were frozen at23:34, before weakened bytes were generated. Their wording about reading, identifying
and retaining bytes is to be interpreted as REPORTED MANUAL INSPECTION plus GENERATOR OBLIGATIONS, not an assertion
that a new CNF existed at the earlier freeze or that an independent pinned checker had already run then. DEL's
"other_clauses" field means the obligation to retain every other clause byte/order, including AND/u5/lexeq definitions.
Its historical "generated_weakened_CNF=false" is a freeze-time status, not a later-generation receipt.

The method is a BYTE FILTER of the pinned oldF, NOT a fresh encoder invocation with `--p4 1`, which would remove
other variables/clauses and renumber lexeq. Preserve509915variables and all old numbering. Exact output header bytes
are `p cnf 509915 5740226\n` (ASCII LF). The source header is line1 with no comment/blank lines; hence zero-based
clause index i corresponds to one-based clause i+1 and source-file line i+2. Each16-case header is
`p cnf 509915 5740268\n`, followed by the weakened body and exactly42units in row i=2,...,7,coordinate c=1,...,7 order.
Canonical lane-relative paths are used for formula/recipe data; absolute parent paths in DEL are references to the
already-pinned input artifacts, not alternate output locations.

Observed preparation AFTER the freeze:
- producer `n8_one_p4_formula.py` SHA25661eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400;
- `BASE_RECIPE.json` SHA256264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18;
- observed weak base SHA256374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9;
-16-case manifest355b3380…fc74 above, pinning every42unit list, count5740268 and leaf-CNF SHA.

A NEW second-path traversal check actually ran at2026-10-18 00:04:37PDT, not at the freeze:
`verify_one_p4_deletion.py` SHA256825c3cd7fabfd2efe25ff9e21f1044bed09c32a58e6be92aa63a3961e2893016,
receipt `BYTE_FILTER_VERIFICATION_v1.json` SHA25665aafe0ad577645036c6cc15e4f4705f0bb19a4f5e8eed2867954da8d761cc88.
It checked source SHA6ecb77a7…469b, exact source header, all5740230 LF-only/no-comment clause lines, all4deleted
hashes and Q1keep, and compared EVERY5740226retained source clause byte-for-byte IN ORDER against the next output
clause. It verified all five56-flag name-table domains and bound all16 exact42unit cases/header/SHAs; all_pass=true.
No CNF file was stored. This is generation evidence, not a refutation or parent replay. Future solver/checker streams
must match those pinned case hashes, and parent regeneration/negative controls remain obligations.

## 5. Correct import status and complete conditional conclusion (BR2 minors5–7)

The parent A8 authority is a **correctness-accepted partial result; no novelty claim**: parent verdict
`moqls8-k1k2-parent-verdict.md` SHA919daeac…a8f9, Proofoutline1/line13, read-and-bound lineage/line9, disposition/line36.
A8 has exactly the five-square/all-entries/all-squares weight<=2 premise stated there. Its printed Lemma10 dependency
is included in the import. The primary definitions/isotopies and rules#2/#3 are Ball–Simoens2607.12933v2:
`sources/2607.12933v2.raw.txt` SHA256265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9,
lines195–225,287–302; printed Lemma10 lines342–356; Problem16 line642 (n-3=5 at n8).

Other pinned mathematical interfaces: `K4K5_ENCODING_SOUNDNESS.r3.md` SHA256
a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59 and
`K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md` SHA25634e11e52c28a798eb378c397097dbccaa753aca74d54e8ccbf6465b2088177d4,
read with the earlier generic repair note41395137…1022. They supply the ALL-QLS necessary families/auxiliary
extensions and ROWLEX source meaning, not an assertion that the old reduced-K5 conclusion applies to F_one.

The ONLY permitted final implication is conditional on ALL of:
1. accepted primary definitions/rules, Lemma10-inside-A8, A8/W8 and the all-QLS necessity/normalisation bridge;
2. parent acceptance of property-form T16 (not merely model-reviewed/reduced-K5 coverage);
3. exact byte-filter receipts and16 complete pinned CNF/unit identities, including the3c112 cases anew;
4.16/16 strict refutations with complete self-exit/feed/proof-stream/hash/guard predicates (no proof-free/SAT-model claim);
5. independent parent regeneration and proof replay with fail-closed controls; and
6. parent disposition of the repaired bridge, T16 and case evidence.

If these gates hold, every hypothetical non-classical five-set maps to a satisfying assignment of a refuted weakened
template, a contradiction; this WOULD answer Problem16's n=8 case affirmatively. Gates/certificates are still open.
No full-base Boolean UNSAT statement, old-to-weakened certificate transfer, novelty claim or current n8 theorem is made.
