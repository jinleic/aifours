# Ball–Simoens Problem 16 at n=8 — ASSEMBLY r4 (UNFROZEN DRAFT 1)

**Status: CONDITIONAL ASSEMBLY.** This is not an n=8 theorem, it is not protocol-complete, and it makes no novelty or priority claim.

**UNFROZEN DRAFT.** Prepared at 2026-10-18T10:17:46.249007-07:00 under parent instruction (static only). It is NOT frozen and is not the object of any verdict. The frozen assembly of record remains r3 (`L/review/N8_ASSEMBLY.r3.md`, SHA256 `64d5d06b77f611c00ede71a8826102734e3d09a39e3028b761c24edbb8710345`).

Link statuses below are the status as of 2026-10-18T10:17:46 PDT. The parent will say when to freeze, after the GA/GB replay statuses settle. Statuses are refreshed at that point, and the frozen r4 is written as a new file with its own exact r3→r4 diff. Later receipts and reviews require a new assembly version, not silent updates.

Once frozen, r4 will supersede r3 as the object of any final composition verdict. The following are preserved unchanged:
- r1 (`8c9cf1c2cc079e2bfdbab8bd6e0a2c9a79268a534fb4043f9ad1028820fea986`), r2 (`ba97fce38ff3f97a72f374f8ab084775a47cc6def7223e5f6177c52fced0a41c`) and r3 (`64d5d06b77f611c00ede71a8826102734e3d09a39e3028b761c24edbb8710345`);
- registry r1 (`2b727fde73816970724ff560c8384ed1ce3293caec36c3ce5e5d449686e21798`), registry r2 (`eb7786b92f848ae8e5b74007a555fd2b0257b9665a5ca2dd03be069dfd71e060`) and registry r3 (`83eed6642c4edd76d8de8780aafbcd7a50b74c72ed1706bc2ea61c5b324e64ac`);
- the mandatory r1 addendum `L/review/N8_ASSEMBLY_QUALIFICATION_CORRECTION.r1.md` (`8bfd2dee4b7471d5187732d318c4c392467512fc42b2e24f085c7261baf28d4f`).

The exact r2→r3 unified diff is `L/review/N8_ASSEMBLY.r2-to-r3.diff` (SHA256 `28497a38cc09722a518cffee506c6e2ab8472b90c75e26f846911faba7915f50`, 82446 B). The working r3→r4 diff for this draft is `L/review/drafts/N8_ASSEMBLY.r3-to-r4.draft1.diff`. It is cited by path only, because its hash depends on this text.

**Reviews applied:**
- r3 delta, Codex (`R/moqls8-assembly-r3-delta-codex-v1.note.md`, SHA256 `6c0011a806f05a4716318ac72c3d24c0f73c65c8088977b7fd9bb95bf9e59c62`): ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 2 MINOR. It accepts r3 as the conditional skeleton and confirms all five r3 parent decisions and Claude r2-delta MINORs 2–10. Both MINORs are applied in this draft (Appendix D), together with its instruction to update the GB statuses.
- r2 delta, Claude (`R/moqls8-assembly-r2-delta-c-claude-v1.note.md`, SHA256 `4ae89ea9a967f44ed5000e12c451c40069c8d2bc1fec5fbc595c6b57a97af4c9`): ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 10 MINOR. All ten are applied (Appendix B).
- r2 delta, Codex (`R/moqls8-assembly-r2-delta-codex-v1.note.md`, SHA256 `4259b60fc35feb0aeeebc25a577a072f5a23cebf8747699689f4005061a96418`): ACCEPT, 0/0/0, no repair requested.
- The r1 reviews stay applied as in r2 (Appendix A): Codex `e6687b76d8a065187eeafd2835d0fecfbc889dcf34d761ddd5ee28bc173abc37` and Claude `5148c21d7dffc9e5f32f30be330e98d5bbf3035532c52ebbf5b1dfe291e95f0d`.

**Parent decisions incorporated** (parent instructions for r3 and for this r4 draft):
1. A10 counts exactly 18 GB inputs: 12 direct + 6 strengthened.
2. All 22 generated GB hashes are input identities, not 22 mandatory refutations.
3. The single certification predicate of §7 binds EVERY counted GA and GB replay.
4. A worker-only PASS never substitutes for a parent replay.
5. The reach of A7 is confirmed by parent erratum `R/moqls8-p1-normalform-parent-verdict-v1-erratum-1.md` (SHA256 `da050a74916b691a0af3a3257e286ce3725247628a80dc0ae4a341fb133887c2`).
6. **GB written lemmas.** The GB necessity note r2 and the genuine NF bridge r1, read with GB review erratum r2, are CORRECTNESS-ACCEPTED at the conditional written-lemma and input-identity scopes ONLY. Authority: parent verdict `R/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md` (SHA256 `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, 5094 B, 2026-10-18T09:57:24-07:00). It accepts no GB refutation, no n=8 theorem and no full gate. The optional genuine-only alternative for GA is NOT adopted.
7. **Replay statuses reported by the parent** (status as of 2026-10-18T10:17:46 PDT):
   - GA P0-B4 and P0-B5 are PARENT-QUALIFIED PASS under v5d (audit `2e7a12e3196d540511389b9d5690f69e325ff5988dfe226084ee5f4c54d67adb`).
   - GA P1-B2.M2 v5d attempt 1 is UNKNOWN, after an external SIGTERM at 09:25:51. Attempt 2 is frozen under v5e and has not run.
   - The other GA formulas run sequentially in the parent batch.
   - GB parent replay is not yet authorized.

**Path prefixes.**
- `L=/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16`
- `R=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`
- `S=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening`

"LFa–b" cites 1-based LF line numbers of the named SHA-pinned file.

**Short names.** DISP = unified parent disposition; REP = repair overlay; BRIDGE = unified bridge r2; TPL = T16 source; NF2 = normal form r2; NFV = NF parent verdict; PRIM = primary raw text; F10 = first-ten verdict.

**Identity pins (m5, m6).** Every SHA256 in this note is printed in full.
- **Registry.** `L/review/N8_ASSEMBLY_LINKS.r3.json` (SHA256 `83eed6642c4edd76d8de8780aafbcd7a50b74c72ed1706bc2ea61c5b324e64ac`) stays the registry. This draft creates no new registry.
  - Registry r3 fingerprints exactly the 80 FILES in its `files` map (path, SHA256, bytes), each rehashed at the r3 freeze.
  - It also lists non-file identities (formula, proof, fingerprint and tail hashes) with the records that carry them.
- **Narrowed coverage claim (Codex r3-delta MINOR 2).** Registry r3 does NOT fingerprint every cited file. Cited in r3 but not registered as file entries:
  - the twelve historical direct-leaf receipt files. Their SHA256 values survive in registry r3 `identities.direct_leaves`; §4 now prints their paths and byte counts.
  - the r2→r3 diff, pinned in this header;
  - registry r3 itself, pinned by full SHA256 above;
  - the lane's worker GB run directories, which are not evidence.
- **New citations.** Every artifact first cited in r4 is pinned inline with full SHA256 and byte count (Appendix E). It is not registered.
- **Registry comparison (narrowed).**
  - For all 30 file entries of registry r1, path, SHA256 and byte count are unchanged in registries r2 and r3.
  - For the 12 r1 direct-leaf records, the identity fields `formula_sha256` and `receipt_sha256` are unchanged in r2 and r3.
  - Those records are NOT identical. r2 kept `receipt_file` and added `protocol_qualification` with a recoded `status`. r3 dropped `receipt_file`, recoded `status` and added `qualified`.
  - r3's statement that these records were "identical, same path and same SHA256" in r1, r2 and r3 is withdrawn.
- The two pins that r2 abbreviated wrongly were wrong only in r2's prose, never in any record: `094dab60c7972c956f90c8cf0984c47f79376d0018192457c84adab6e224ff3c` and `65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0`.

Rehashing is a static read, not a native or proof replay.

## 1. Exact target, terminology and logical shape

**Primary source.** `L/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9` (Ball–Simoens, arXiv:2607.12933v2):
- A QLS(n) is an n×n matrix over Cⁿ whose rows and columns are orthonormal bases (PRIM LF195–196).
- Two QLS are orthogonal if {ψ_ij ⊗ φ_ij} is an orthonormal basis (LF209–215).
- A t-MOQLS(n) is a SET of t pairwise orthogonal QLS (LF215–217).
- Set isotopy allows (i) entry phases, (ii) common row/column permutations, and (iii) a separate unitary on each square (LF217–222).
- A set is classical if, up to isotopy, all entries lie in {|1⟩,…,|n⟩} (LF223–225).
- Problem 16 (LF642): "Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?" At n=8, n−3=5 and n≠4.

**Target (n=8 only).** Every set of five MOQLS(8) is classical in the sense of PRIM LF223–225.

*Extraction note.* Text extraction damages PRIM LF209–215: some stray lines contain only "n", and the basis appears as "C ⊗ C". In the page-preserving extraction `L/sources/2607.12933v2.layout.txt` (SHA256 `df1d8b1467166d2e615461669401dfada86bb9033ffd4a7e0acb34b8e8584219`, LF104–105), the two "n" superscripts sit on the line above. So the phrase reads "an orthonormal basis of Cⁿ ⊗ Cⁿ". The typeset edition is `L/sources/quantum-latin-2607.12933v2.pdf`, SHA256 `2d60d45fbc3e3d1d5f5d6cfec0f7040b6f362ba3d7c7b3e358d3fb02a6e21afe`. Its page identification is in `L/review/N8_ASSEMBLY_PARENT_CHECKS_AND_PRIMARY.r1.md`, SHA256 `e8e296a897c81f325031dbe05eaf355b71baad0e805b233448873c224f480c4f`.

*Terminology.* **Genuine** means realised by actual vectors in C⁸ that satisfy the QLS and pairwise-orthogonality axioms. A **Boolean model** is any satisfying truth assignment of a CNF and need not be realised. "Genuine" is unrelated to the paper's phrase "not genuinely quantum", which means classical (PRIM LF201, LF223).

*Relabelling.* U and T16 also relabel the squares of the set (BRIDGE LF59; REP LF37–38). Relabelling is not one of the isotopy moves (i)–(iii), but it is harmless:
- A t-MOQLS(n) is a set.
- Move (ii) never changes which vectors occur as entries, move (i) changes each entry only by a phase, and move (iii) acts on each square separately. So a set is classical if and only if each of its squares is classical in the single-square sense of LF201–203 [elementary].
- Single-square classicality does not depend on labels, so set-classicality is invariant under relabelling.
- A8's "wholly classical" is read exactly as this set-classicality.

**Logical shape.** Write B_C = F_one ∧ (the exact 42 Q1 column-0 units of template C), and S_j = B_C ∧ M_s for the six pairs (C,s) of §6.
1. **U + T16.** By isotopy moves and square relabelling, every genuine non-classical five-set yields a configuration whose canonical assignment is a model of at least one of the sixteen exact B_C (§§2–3).
2. **D12.** Twelve B_C have parent-accepted native UNSAT observations, each PROOF_DIGEST_MISSING. Of the fresh qualified parent replays, P0-B4 and P0-B5 are PARENT-QUALIFIED PASS (v5d); the other ten are PENDING (§4).
3. **NF, per C.** For each C ∈ {P1-B1, P1-B2, P1-B3, P1-B5}, the accepted NF lemma gives: UNSAT of every S_j with source C implies Boolean UNSAT of B_C (§5). NF itself refutes nothing.
4. **S6.** All six S_j are BOUND (identity). None has a qualifying UNSAT (§6).
5. **Composition.** The n=8 conclusion may be asserted only if A1–A11 all hold (§8).

**Currently missing.**
- Fresh, digested, qualified parent replays of the ten direct B_C not yet qualified (A4). P0-B4 and P0-B5 are PARENT-QUALIFIED PASS (§4).
- Qualified parent replays of all six S_j (A8). None is qualified yet; P1-B2.M2 attempt 1 is UNKNOWN (§6).
- Proof-digest provenance for every counted replay, GA and GB (A9). Contemporaneous digests exist so far only for GA P0-B4 and P0-B5.
- The remaining GB obligation of A10: 18 qualified parent GB replays (A10(iii)), not yet authorized. A10(i) and A10(ii) are accepted at conditional written-lemma scope only (§8, §9.2).
- The final full-composition parent verdict (A11).

No conclusion of §8 is claimed now.

## 2. Link U — accepted unified reduction, with its exact conditions

**Exact statement.** Take ANY genuine non-classical set of 5 MOQLS(8). Standardise row 0 and apply accepted A8/W8; this produces a weight-3 witness. After square relabelling and common row/column moves, the normal form has:
- Q1(1,0) support {1,2,3};
- the other four supports {4}, {5}, {6}, {7};
- non-strict Q1 column-0 ROWLEX;
- canonical Gram/auxiliary values that satisfy the exact weak formula F_one.

The other four squares may be classical or non-classical.

**Status.** PARENT CORRECTNESS-ACCEPTED as a CONDITIONAL mathematical reduction and exact formula binding (DISP items 2–3, LF13–14). It is expressly NOT an exclusion on its own.
- Authority: `R/moqls8-unified-parent-disposition-v1.md`, SHA256 `29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb`.
- Accepted text, read together: BRIDGE `L/review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md` `c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3` and REP `L/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md` `e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704`.

**Load-bearing imports.**
- **W8.** In row-0 standard form, the five supports at any cell off row 0 are disjoint and avoid the column coordinate, so every such entry has weight ≤ 3 (A8 parent verdict LF13). W8 is ONLY this row-0-frame bound. The bound in any other line frame is proved inside T16 §1 (TPL LF9–18) and imported only through T16's admitted range (§3).
- **A8.** The premise covers ALL FIVE squares and ALL entries: if every entry of every square has weight ≤ 2 in a row-0 standard form, then all weights are 1 and the set is wholly classical.
  - Contraposition gives some weight-3 entry in a non-classical five-set. It is NOT a per-square P4 premise.
  - Authority: `R/moqls8-k1k2-parent-verdict.md` `919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9`.
  - Proofs: `R/moqls8-k1k2-parent-inputs-r2/PROOF_K1_K2.r1.md` `094dab60c7972c956f90c8cf0984c47f79376d0018192457c84adab6e224ff3c` and `.r2.md` `d36e646cf0e8faadd5e6131615c6694cbf4187c10abbb6bf54aa17083ab72d86`.
  - A8 imports the printed Lemma 10 (PRIM LF342–356). It does NOT import the Egan–Wanless counts or the K1/K2 corollaries.
- **Necessary encoder families and canonical extension** (within U's scope): constants and G2–G5; exact AND/singleton and inclusive-prefix auxiliaries; one true Q1 w3 witness, with all other w3 flags false. Source `L/review/K4K5_ENCODING_SOUNDNESS.r3.md` `a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59`.
- **Original encoder, byte and name binding.** `R/moqls8-encoder-binding-v1/binding-result.v2.json` `dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112` ties together:
  - encoder `R/moqls8-encoder-binding-v1/code/gram_a.py` `bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a`, argv `--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex`;
  - `L/evidence/gram_dev_v1/GA5L_K5_sb2.cnf` `6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b` (509915 vars, 5740230 clauses, 137664569 B);
  - full name table `R/moqls8-encoder-binding-v1/K5.names.json.gz` `b8423861d03b6e837317c12ef1f2f297301d1bfbbfb7852b93ccec29b85e2522`;
  - primary map `L/evidence/gram_dev_v1/GA5L_K5_sb2.map.json` `7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197`.
- **Exact weakening.** Delete ONLY the four row-0 P4-ALO clause lines for squares 2–5, at zero-based indices 5735297, 5736866, 5738435 and 5740004. KEEP square 1 (index 5733728).
  - Keep all one-way w3 implications, G families, SB2 and ROWLEX.
  - Add no weight-1, classical-net, L-sort, fixg or other-P4 condition.
  - Recipes: `L/evidence/UNIFIED_ONE_P4_DELETIONS_v1.json` `4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6` and `L/evidence/n8_one_p4_templates_v1/BASE_RECIPE.json` `264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18`.
  - Weak formula identity: `374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9` (509915 vars, 5740226 clauses). It is streamed only; no on-disk weak CNF is asserted.
- **Independent weak/base/table/leaf binding.** `R/moqls8-one-p4-parent-binding-v1/RESULT.json` `65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0`.
  - The parent traversed all source clauses, the four deletions and five ALO domains, the mathematical template table, 672 units and 16 leaf hashes, and 16 sign-flip binding controls, without producer imports.
  - The worker producer code `L/code/n8_one_p4_formula.py` (`61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400`) and inherited worker hash receipts do not substitute for this independent binding.

**Mandatory conditions:**
- genuine QLS/MOQLS axioms;
- the stated row-0/witness normal form;
- the exact weak deletion recipe;
- canonical auxiliary extension.

No reduced-K5, non-classicality or P4 requirement is imposed on squares 2–5. No old-F or c112 proof is imported.

## 3. Link T16 — accepted sixteen-leaf cover

**Exact statement (property form).** Take five genuine pairwise-orthogonal QLS(8), row-0 aligned, with the specified (1,0) support pattern. The common residual permutations and square relabelling, followed by non-strict ROWLEX, take Q1's column-0 supports to one of the sixteen listed forms. Its canonical assignment models that B_C (DISP LF12; BRIDGE §4, LF78–89).

Degree ≤ 3 and the component theorem use the five-square unitary-support hypotheses. They do not assume P4 on the four other squares.

**Authority.** Item 1 of the unified parent disposition (DISP LF12, "Property-form T16 — ACCEPTED").

**Admissible text.** Exactly the F3 import range (DISP LF29) of TPL `L/review/K5_COLUMN0_TEMPLATE_COVER.r1.md` (`1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a`):
- LF9–19, with the stated support hypothesis replacing LF20's justification;
- LF22–55;
- LF60–64, with the residual moves of REP LF34–38 and WITHOUT the reduced-K5/P4 sentence (LF62–63);
- LF66–109.

**Excluded (not premises).** TPL LF1, LF4–5, LF59 and LF111–131. These still assert the old 13-case/c112/reduced-K5 interface. The sixteen-template conclusion is taken from DISP LF12 and BRIDGE LF86–89.

**Supporting only.** The parent delta check `R/moqls8-unified-delta-v1/RESULT.json` `d3eedf783e2104c296bc69cb36d7f92c2bd4f4dee38802ff3290b039250cec8b` (16 orbits from 140 sorted / 43290 labelled necessary patterns) does not replace the written component proof.

**Leaf manifest.** WMAN `L/evidence/n8_one_p4_templates_v1/MANIFEST.json` `355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74`.
- Every B_C has 509915 variables and 5740268 clauses.
- ALL 16 enter the cover, including P0-B6, P1-B6 and P2-C4.
- This is a cover of genuine counterexample images. It is NOT a Boolean cover of bare F_one.

## 4. Link D12 — twelve direct leaves

These are the twelve direct leaves, not the twelve historical unmeasured producer candidates.

**Status.** Each historical row is a **parent-accepted native UNSAT observation** with **PROOF_DIGEST_MISSING**; it is unchanged and immutable. Fresh, digested, qualified parent replays under §7 (status as of 2026-10-18T10:17:46 PDT): **P0-B4** and **P0-B5** are **PARENT-QUALIFIED PASS** under v5d (§4.1). The other ten are **PENDING**.

Authorities:
- first-ten verdict `R/moqls8-fone-first10-parent-verdict-v1.md` `61130625a144ae8e88e1f3c8cddd22798477808b0673ac5d246d9b8215b983e4`;
- direct-12 addendum `R/moqls8-fone-direct12-parent-verdict-v1.md` `515cd9e1908d5f9e7aed262f800e04315ea6145f944ab34cb11d7d98d014d667`;
- `R/moqls8-fone-parent-replay-v1/RESULT.json` `f63dbeebe2d1728a25520d2af1fa7babab15221e2b01f1e74581b6985979ee0c`;
- `R/moqls8-fone-parent-replay-v1/RESULT-ADDENDUM-v1.json` `a051418a699fcb6e9070027d26010a4ec018976cf74936083c04d5ee80fe8bab`;
- provenance correction `R/moqls8-parent-replay-provenance-correction-v2.md` `a4b511195f64e0f8cfe2f8d0fe7ccc0bac278bec0859a9d3897c8de612b47b70`.

| Leaf | Exact B_C formula SHA256 | Historical parent receipt file / SHA256 / bytes | Status | Qualified (fresh, digested) |
|---|---|---|---|---|
| P0-B1 | `a29d546cad564cd7d20cf1b40dbe18d7baa57b0f25e109fb75e5a8d8042c33c4` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B1.json` / `c818de09c159884a86cf1994453828fc4a111e0c0b449e217efe650f3020e271` / 10077 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P0-B2 | `ec6b8507c6cf74fafe0111780672d70ca15ca0825590064899d7f853a45e4dbc` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B2.json` / `969f587dad9d3147dd45d6d37770954c97424743535cde50f75f5c877620d05e` / 10088 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P0-B3 | `c42d3520ba7f1e210f09c18d97dbf7988e143d01d06ef932437685ab57a98ba7` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B3.json` / `80e1db9fb550cd1918812e1aa44e979278525e46e2ba6bd0d0f2afa7eb536a3c` / 10110 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P0-B4 | `7b4e49c45f7e3678710171d03ae3a01b041640052f7ace3778699bb09bba3b44` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B4.json` / `004bc5fcb36fa2c6f640d5b970b08660a1572c2dccd5dd217bab6fcf03c39deb` / 11868 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PARENT-QUALIFIED PASS (v5d; §4.1) |
| P0-B5 | `fc52e1092e7818f1ba23498cf85e44f3cbf9f0a2765522ba83b72f32c3bcce0f` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B5.json` / `4c31cdbf5ee2f984d18ca711d6332355404319a440943e220d3e3a375561a0b4` / 12318 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PARENT-QUALIFIED PASS (v5d; §4.1) |
| P0-B6 | `37afcaae7706407caab277065143a37a4eb09381a8d8f13f309219f7ecba4d08` | `R/moqls8-fone-parent-replay-v1/receipts/P0-B6.json` / `b72a4cb9c183525f37956aaa212b5b744a6b1fd00ef9e2a65c6d154154681d9f` / 12142 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P1-B4 | `b1c0200391e35af736e610dcabbb34a4d19c57ffbf13c9a440cd9b70c3d09fb5` | `R/moqls8-fone-parent-replay-v1/receipts/P1-B4.json` / `8c81147135cd114a648c1bc9f0de2b51f243a848a96ca8e230314242ebe0cbcf` / 10088 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P1-B6 | `a6b45fd3a62599afedea680392eff1a65a1e44ae524b460e52c07e795a9ac2c3` | `R/moqls8-fone-parent-replay-v1/receipts/P1-B6.json` / `255c1df89a96a9bca3bba573e7ef54ee2c9c8fec733cdef48fee9a8dba3e39d7` / 10121 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P2-C1 | `d27129d92833993390847048b0f954b5e7c1b66eb4b386b7822f323f0a57d403` | `R/moqls8-fone-parent-replay-v1/receipts/P2-C1.json` / `1192ea014b4b9e60dc4e059837783a8062db7d1dd2df272f4faaa9c5ba76f2a1` / 10102 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P2-C2 | `24f1547251cf6c094852384c4dee42455700b57c09e246735ec0e28328a2e43b` | `R/moqls8-fone-parent-replay-v1/receipts/P2-C2.json` / `03273c7be4a8ade0a4cf00d6001794d76db720ab025b55d3f05ca0d2e8401745` / 10614 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P2-C3 | `5fc6827fa9cb2856ae1ad14d1aa319f51305296ede72acb7b188060288ae5597` | `R/moqls8-fone-parent-replay-v1/receipts/P2-C3.json` / `acd0763c44f93eff3c804351ce9c421c3e354559c739988a66d70feff43a961d` / 10123 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |
| P2-C4 | `32c4d3db7af5da46151238836dfb14f36e782ca87d139c8ae38211a1ab663b94` | `R/moqls8-fone-parent-replay-v1/receipts/P2-C4.json` / `2bbd69e3f7fafe31e35c4dbf9a8023e159d248f09cc18e0135c105a6edc12070` / 10127 B | parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING | PENDING |

**Receipt audits:** `R/moqls8-fone-first10-parent-receipt-audit-v1.json` `43b09c975db7309ef5a5746b658e624d4a8b987a9b3a851c0c1f7469377e9851` and `R/moqls8-fone-direct12-parent-receipt-audit-v1.json` `891e52bdbccc381cfceac47047b963ae1ab48ffc2a4fd6e631b1e6ff959ed262`.

**Checker:** parent drat-trim `R/moqls7-parent-proofcheck-v1/drat-trim` `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`. The solver is untrusted.

**Historical control scope (not inflated):**
- one tiny UNSAT positive;
- one satisfiable-checker rejection;
- two first-unit-flip inputs that remained UP-UNSAT and VERIFIED. These count only as measured-input binding controls (F10 LF23).

For these historical receipts, proofs were streamed. No proof digest and no retained proof exist.

### 4.1 Fresh qualified GA direct replays (status as of 2026-10-18T10:17:46 PDT)
**Authority.** Parent audit `R/n8-ga-leaves-P0-B4-B5-parent-audit-v1.json` (SHA256 `2e7a12e3196d540511389b9d5690f69e325ff5988dfe226084ee5f4c54d67adb`, 3599 B, at 2026-10-18T10:12:54-07:00): status PARENT_QUALIFIED_PASS. It re-checked the full v5d certification predicate from raw receipts:
- script and PRE-EXEC binding, and post-gate identity;
- measured complete solver and checker feeds equal to the bound leaf formula SHA256 and bytes;
- solver rc20 with the single status line `s UNSATISFIABLE`; checker rc0 with the single status line `s VERIFIED`;
- raw logs re-hashed;
- relay read == delivered == checker-consumed N, with equal SHA256;
- FIFO EOF and relay/feed settlement;
- no stop latch, events, survivors, unfinished threads or scanner failures;
- pinned binaries re-hashed.

The audit cites:
- PRE-EXEC `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5d-two-short-leaves-parent-a1.json` (`44739921890eeab80493214e5fd65fc18b16e7160b9ab5fdcce12a60380492e0`, 41979 B);
- run summary `R/moqls8-strengthened-parent-replay-v1/runs/run-20261018T100330.json` (`ef15f7c5e8d6700fedf28a313595f24d46777f4e87cd6e6648d03cc51abd8232`, 12902 B);
- parallel GO `R/n8-two-short-leaves-parallel-parent-go-v1.json` (`92ace11da7125559fcab817e13cc8fb3457a800f1df978428bab196da8c8d9a5`, 1376 B);
- the v5d native-control parent audit `R/n8-v5d-native-control-parent-audit-v1.json` (`c3191c6d890abc48b6c51025f396fad35e6ff5ee41ed6accfe321e843f3b81e4`, 2833 B), status ALL_FIVE_NATIVE_CONTROLS_VERIFIED. The five controls are unsat, sat-checker, truncate, early-close and suffix.

| Leaf | Formula SHA256 / bytes | v5d receipt / SHA256 / bytes | Proof-stream SHA256 | Proof bytes read = delivered = checker N | Status lines | Solver / checker log SHA256 |
|---|---|---|---|---|---|---|
| P0-B4 | `7b4e49c45f7e3678710171d03ae3a01b041640052f7ace3778699bb09bba3b44` / 137663265 B | `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P0-B4.json` / `457dfe551344a8340e22116d9862263168a1467e5dcf91c653f107e9afad0366` / 24042 B | `7f0a1d6bf66594b9172a6e727c700b6773169726442374349f10231e23696101` | 11590623 = 11590623 = 11590623 | rc20 s UNSATISFIABLE; rc0 s VERIFIED | `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162` / `71d788dc34d50a4c5686aeadb9ae5c78a25bda95a6ab87ade59dd7d79c3e6463` |
| P0-B5 | `fc52e1092e7818f1ba23498cf85e44f3cbf9f0a2765522ba83b72f32c3bcce0f` / 137663266 B | `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P0-B5.json` / `e3187cd898c28c66260f5142aae7c68cf7dff5122d9b9d737749c8cc48c4250b` / 24041 B | `e694bfccdf03e0b4cf168bce5043704493fb9b20f4c14a80c9d589097f16b26a` | 11587677 = 11587677 = 11587677 | rc20 s UNSATISFIABLE; rc0 s VERIFIED | `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162` / `051fa8a5807d4b127c37e753d147a6bff58a986498cfc970b77c2282c855e635` |

Both solver logs are the 16-byte quiet output `s UNSATISFIABLE`, so their hashes coincide. These two leaves satisfy A4 and A9 for their own inputs only. The ten other direct leaves remain PENDING.

**The four original inputs not refuted directly** are discharged only through NF + S6 under A7 (§§5–8):

| Source C | Exact B_C SHA256 |
|---|---|
| P1-B1 | `110ff19e28420494c4f8acbcbec35a29655e30f090fb378ea707f22fe56f6491` |
| P1-B2 | `13530c0d40a2bdd4abb245789259f7157323d2514c3066daabe7bf363f9f490e` |
| P1-B3 | `721c6f3bf445ab5523642b1af7ed540271ab0ea23bfd79a2ac8c60f49597130b` |
| P1-B5 | `92a3d9f659a5c5dc1f3bebbc0a05d5e0cf8818b4c0d307bd6aa9f33a3247ec09` |

## 5. Link NF — per-template Boolean normal form

**Accepted statement** (operative: NFV LF9). Fix C ∈ {P1-B1, P1-B2, P1-B3, P1-B5} and B_C = F_one ∧ C (WMAN). Every Boolean model of B_C yields a Boolean model of B_C ∧ M_s for some s ∈ Rep(C), where Rep(P1-B1) = {2}, Rep(P1-B2) = {2,4}, Rep(P1-B3) = {2} and Rep(P1-B5) = {2,3}. M_s is the 126 negative binaries ¬g_s((0,c),(i,0)) ∨ ¬g_s((0,d),(i,0)) for i=2..7 and 1≤c<d≤7.

**Contrapositive, used in §8:** for each such C, UNSAT of every S_j with source C implies Boolean UNSAT of B_C.

**How the lemma is read.**
- It is one-way and per C, with the same 42 units. That is why BOTH S_j of P1-B2 and BOTH of P1-B5 are required.
- The converse is trivial and carries no load.
- It is a model transformation, not a CNF automorphism.
- M_s constrains ONLY column 0.

**Status.** PARENT CORRECTNESS-ACCEPTED as a conditional Boolean lemma: `R/moqls8-p1-normalform-parent-verdict-v1.md`, SHA256 `4748f023a504a263ef99400e83df063ecbfcdebe979b77d24a69ff1f301b7826`.
- Codex `R/moqls8-p1-boolean-normalform-codex-v1.note.md` `030f92a826ab4d85e6d7fd0d9a7e5538986facf897afb6e81f7cb902ad714e30`: ACCEPT-WITH-FIXES 0/0/1, fixed in NF r2.
- Claude `R/moqls8-p1-boolean-normalform-claude-v1.note.md` `a1a8eb7d1ad6223c2d12bc39c0ca8936f511645deb560f1e43bfd3a41a563805`: ACCEPT-WITH-FIXES 0/0/10.
- Parent ID/argv/fingerprint/binding checks: NFV LF21–26.
- The parent finite/format check `R/moqls8-p1-normalform-parent-v1/RESULT.json` `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2` is **supporting only**.

**Accepted text.** NF2 `L/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md` `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`, read with NFV LF28–32; NFV LF9 is the operative claim.
- r1 `5c748dd8522b0eced47f18e9bebf8129d3923036e4061cae60491d394fa4faa4` and diff `c6b8bfebea8ab669e0869eb542fc2c2330c9cae35570e0333875103b5151e2e5` are preserved.
- Claude MINORs 1, 2, 3, 7 and 8 are wording-only and not applied to the NF text. MINORs 4, 5, 6 and 9 are discharged by evidence; MINOR 10 by the amendment (A7).
- NF2's self-labels "UNREVIEWED"/"PENDING" (LF1, LF7, LF161) are historical and superseded for status only.

**Dependencies.**
- The families are "constants and G2–G5"; no G1 family is defined in the cited sources.
- NFV LF9's "uses only G2/G3 support facts" means it needs no unitary, phase or rank realization.
- As a statement about CNF families, that phrase holds only for the local permutation-count lemma (NF2 §1, LF33–78).
- The model transformation (NF2 §§2–4, LF80–147) also needs invariance or re-extension of: the constants, G4, G5, SB2, the kept Q1 P4-ALO with its one-way w3 implications, ROWLEX with inclusive-prefix lexeq, and the AND/b3/c4/u5 definitions.
- It also needs the absence of classical-L variables and of fixg (NF2 LF98–100; NFV LF25).

## 6. Link S6 — six strengthened inputs: BOUND (identity); qualified UNSAT PENDING

**Generation.**
- Generator `L/code/generate_p1_monomial_r2.py` `08b67cef53a0851a965be163452842dd7541bb825c5f54817a2f9af7112bc352`.
- Freeze `L/review/P1_MONOMIAL_GENERATOR_FREEZE.r2.json` `6234e470b7164587fddb9222cf68d809fc319ecc014961bce7a9d879a66465ae`.
- Planned-hash manifest `L/evidence/P1_MONOMIAL_FORMULA_HASHES.r2.json` `e04557a4ea83875caa265e9928b488386fe52c2f95306bd6078f7706265eb709`.

These are planned byte identities only, not receipts. The rejected generator r1 and its order mismatch are preserved separately; they are not proof evidence. No CNF file or solver run was produced by these generators.

**Composition.**
- The header `p cnf 509915 5740268` becomes `p cnf 509915 5740394`.
- The weak body and the 42 unit lines are unchanged and stay in place.
- The 126-clause M_s tail is appended, with negative literals sorted within each binary.
- No new variables, H3 or rank clause, or whole-square classicality is added.
- Clause count: 5740230 − 4 = 5740226; +42 = 5740268; +126 = 5740394.

**Binding = BOUND (identity only).** Parent `R/moqls8-strengthened-parent-replay-v1/BINDING.json`, SHA256 `5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c` (script `bind_v1.py` `b010baa4dd5c7620f7c6215beeb052af80846bfd6c3ee0a80e8d8a235144786c`; status MATCH).

| S_j | Source C | s | Bound S_j SHA256 | Bytes | Source B_C SHA256 | Binding | Qualified UNSAT |
|---|---|---|---|---|---|---|---|
| P1-B1.M2 | P1-B1 | 2 | `09a117b880a4715e068c33b7601b23b424b70218958675ed68b28f053fd050c0` | 137665036 | `110ff19e28420494c4f8acbcbec35a29655e30f090fb378ea707f22fe56f6491` | BOUND (identity) | PENDING |
| P1-B2.M2 | P1-B2 | 2 | `3f65ad964ea83c68f78d7a6a90a95820925c70636e610ec0f4e78541531e04b0` | 137665034 | `13530c0d40a2bdd4abb245789259f7157323d2514c3066daabe7bf363f9f490e` | BOUND (identity) | PENDING |
| P1-B2.M4 | P1-B2 | 4 | `61bddbe074e733a632b10fdac214d4bde1032cda4bdfcf563275d5a5f6fb4af0` | 137665034 | `13530c0d40a2bdd4abb245789259f7157323d2514c3066daabe7bf363f9f490e` | BOUND (identity) | PENDING |
| P1-B3.M2 | P1-B3 | 2 | `e4b55555bdeb9ba389cec74983576ee66939fe19210bb593d7bdac0ba392428d` | 137665032 | `721c6f3bf445ab5523642b1af7ed540271ab0ea23bfd79a2ac8c60f49597130b` | BOUND (identity) | PENDING |
| P1-B5.M2 | P1-B5 | 2 | `caf1368490f766b1df4be973450fbe8b4dc1867067bfc5a9069f9060528510f4` | 137665031 | `92a3d9f659a5c5dc1f3bebbc0a05d5e0cf8818b4c0d307bd6aa9f33a3247ec09` | BOUND (identity) | PENDING |
| P1-B5.M3 | P1-B5 | 3 | `36d58ad9c4e5bb0e70e163a50a322079458c9cfd2fee9251dec8d1ec363c8e35` | 137665031 | `92a3d9f659a5c5dc1f3bebbc0a05d5e0cf8818b4c0d307bd6aa9f33a3247ec09` | BOUND (identity) | PENDING |

**Producer role.** Parent desks own the independent regeneration and the measured-feed solve/check of each S_j. This producer lane has no counted native role on S6, for either GA or GB.

**Historical observation, carried from r2 and NOT qualifying.** It comes from the desk RESULT snapshot `R/moqls8-strengthened-parent-replay-v1/RESULT.json` `74e64f070a31f53cc6e66814dd4bd4293ce5725f557153b0f749eb1f0490b7a9` (assembled 07:19:19):
- P1-B1.M2: native verification observed, PROOF_DIGEST_MISSING (receipt `ada3f86eefb0b1c71099f981c3be9e8febe0874af8a67739b3279c795c7103d2`).
- P1-B3.M2: UNKNOWN, disk-floor stop (receipt `c71b0e7dd19cce098da0add53ece7e0b388293f289641f3af41af76e2594894f`).
- The others: not attempted.

**Parent status after r3** (status as of 2026-10-18T10:17:46 PDT). None of these runs is qualifying.
- **P1-B2.M2, v5d attempt 1: UNKNOWN.**
  - The driver received an external SIGTERM at 09:25:51; source not established by the parent. The solver was terminated, and the receipt records the safety stop.
  - Receipt `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P1-B2.M2.json` (SHA256 `62a388cb165895dece12fe5e3d5209c14e7f061977ca502ed7b59d16fe11c777`, 24278 B, run tag 20261018T091549).
  - PRE-EXEC `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5d-formulas-parent-a1.json` (`f20a6f8ec15404848be73ca45849992f32fdfb7219f883b039387ef2a3fb889f`, 53350 B).
  - This UNKNOWN is immutable.
- **P1-B2.M2, attempt 2: frozen under v5e, not yet run.** It has a separately named PRE-EXEC: `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5e-B2-M2-parent-attempt2.json` (`83ce9d8d2716f003288a2cd6db6c056097b8d788e11d5a8dd20f9ec447662ab6`, 37060 B). Its bound feed is `3f65ad964ea83c68f78d7a6a90a95820925c70636e610ec0f4e78541531e04b0`, 137665034 B, equal to the BINDING row above.
  - Parent audit of the v5e native controls: `R/n8-v5e-native-control-parent-audit-v1.json` (`65ab801c9070701dcc4235855a7161c881eead0dd97b19a5aa2e7d652bc3c5d9`, 2230 B), status ALL_FIVE_NATIVE_CONTROLS_VERIFIED.
- **The other five S_j:** they run sequentially in the parent batch. No qualifying result has been reported.

Any interrupted or stopped run is UNKNOWN (§7).

**Tail binding.**
- On map `7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197`, every g_s((0,c),(i,0)) has ID 1568(s−1)+49c+7i−6 (NFV LF22).
- The SB2 cross-check (Q2 row 1, coordinate 4) gives 1765 (LF23).
- The canonical tails for s=2..5 reproduce the parent fingerprints (LF24).

Fingerprints: `R/moqls8-p1-normalform-parent-v1/RESULT.json` `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2`, field `mononomial_clause_checks.<s>.ordered_bytes_sha256`, produced by `check_local_boolean_v1.py` `abfa623afdd89def969ef48abc2c4a508a84e1f1488651243d023e7dd7762531`:

| s | Fingerprint | Used |
|---|---|---|
| 2 | `6fe525a9e6df69193b918d3f0ec29c841d0a66845ee58b3ca0690b9fe2988708` | yes |
| 3 | `e9f44b5f4c9ca4a4de152bcc47385283da7b66d074b10956a0fcdc7440b5ca7c` | yes |
| 4 | `900a6bc37239e6835f4190ccf42dfc4088dfd4a43dcc4aec522d9297da8e4dea` | yes |
| 5 | `233636b1002e5b9f877999d9cce0ab822b44c585edee70a9248f601652554cce` | no |

The 42 units (s=1) and the tails used (s=2,3,4) decode against the same map as the WMAN units.

## 7. Certification predicate for EVERY counted replay (GA and GB)

This section applies to all 36 counted replays:
- GA: the 12 direct B_C and the 6 S_j;
- GB: the 12 direct GB_C and the 6 GB_{C,s} (§9.2).

The amendment retains "the unchanged F4 strict predicate" (NFV LF36–40). Its summary bullets are not exhaustive:

- measured complete solver and checker feeds whose hash equals the bound strengthened hash;
- solver rc20 with exact `s UNSATISFIABLE`;
- parent drat-trim rc0 with exact `s VERIFIED` after CR removal only;
- no NOT VERIFIED or TIMEOUT.

**DISP LF40, verbatim:**
> For EACH counted worker refutation: solver and checker self-exit, no guard/relay/feed error, solverrc20 with `s UNSATISFIABLE`, checkerrc0 with a raw log line equal to `s VERIFIED` after CR removal only and no `s NOT VERIFIED`/`s TIMEOUT`; both input-feed hashes equal that WMAN case hash; proof-stream SHA and byte count recorded. The inherited status parser also strips whitespace, so the parent must inspect/hash-bind raw logs rather than take its normalized status alone as evidence of exact-line conformance. LRAT-only or proof-free outcomes do not count.

**DISP LF41, verbatim:**
> After16/16 qualifying refutations, independent parent regeneration and proof replay with intended negative controls and a final full-composition verdict remain mandatory. If any case is SAT/UNKNOWN/unstarted, the full exclusion remains open. No duplicate proof/CNF retention, floor reduction, cap increase or unreviewed H3 transfer is authorized.

**How the words bind for each counted replay.**
- **Feeds.** "Both input-feed hashes equal that WMAN case hash" means equality with the bound identity of that input: the WMAN leaf hash for a GA direct leaf, the BINDING hash for a GA S_j, the GBBINDING hash for a GB input (§9.2). Each feed must also have the bound byte count, and be measured complete as written to the solver and to the checker.
- **Proof digest.** The proof-stream SHA256 and byte count are recorded from the actually delivered stream at run time. Bytes read must equal bytes relayed and the checker-consumed count N reported by the checker, as in the parent predicates (GA audit `2e7a12e3196d540511389b9d5690f69e325ff5988dfe226084ee5f4c54d67adb`; GB verdict `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c` LF20).
- **Logs.** Raw solver and checker logs are hash-bound. Status lines are checked exactly, with CR removed only.
- **Exit.** Solver and checker must self-exit cleanly, with no guard, relay or feed error.
- **Checker.** Fixed parent drat-trim `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`, or a separately reviewed, pinned successor.
- **Excluded outcomes.** LRAT-only or proof-free outcomes do not count.
- **Worker runs.** A worker-only PASS never substitutes for the parent replay.

**Fail-closed list.** Any of the following leaves that input, and hence its template, OPEN:
- SAT, UNKNOWN, timeout, or a run unstarted;
- an incomplete or mismatched feed;
- a failed or missing control;
- checker rejection (`s NOT VERIFIED`, `s TIMEOUT` or a non-zero rc);
- a missing or mismatched proof digest or byte count;
- a binding mismatch;
- a guard, relay or feed error, or a non-self-exit;
- any interruption or signal (an interrupted checker is UNKNOWN even after solver rc20);
- missing parent acceptance.

**Provenance bars** (correction `a4b511195f64e0f8cfe2f8d0fe7ccc0bac278bec0859a9d3897c8de612b47b70`), binding for every counted run: no weaker formula, no weaker checker, no skipped cases, no lost guard handling, no relaxed disk or memory limit.

**Own controls** are required for every relay version that produces counted evidence, GA and GB alike. They are not inherited. Classes:
- a tiny known-UNSAT positive passes;
- a satisfiable checker input is rejected (`s NOT VERIFIED`);
- invalid proofs (truncated, empty, wrong-CNF) are rejected, as in the K2 parent replay v2 (A8 parent verdict, verification table);
- a feed-hash mismatch is rejected;
- **NEW, never previously exercised by parent desks:** the recorded proof SHA256 and byte count agree with an independent hash of a retained small control proof.

Unit-flip inputs that remain UNSAT by unit propagation count only as binding controls (r1 LF71; F10 LF23). The exact suite and its adequacy are parent determinations.

## 8. Final implication, antecedents and trust boundary

**The n=8 conclusion may be asserted only if A1–A11 all hold.** No n=8 statement may be made until A1–A11 all hold (NFV LF42). This includes forms qualified "modulo provenance" or "pending GB".

**Antecedents.**
- **A1. Primary.** Primary definitions (PRIM LF195–225) and rules #1–#3 (LF287–302), with Lemma 10 (LF342–356) inside A8; A8/W8 (§2).
- **A2. U.** DISP items 2–3 with their exact conditions and byte bindings (§2).
- **A3. T16.** DISP item 1 within the F3 import range (§3).
- **A4. D12.** Each of the twelve direct B_C has a qualifying, fresh parent replay under §7. The existing observations are PROOF_DIGEST_MISSING and do not satisfy A4. The only alternative is a separately explicit, authorised protocol exception, and none is granted. *Status (status as of 2026-10-18T10:17:46 PDT): satisfied for P0-B4 and P0-B5 (§4.1); PENDING for the other ten.*
- **A5. NF.** The accepted per-C lemma (§5).
- **A6. S6 binding.** All six S_j BOUND. DONE: `5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c`.
- **A7. Amendment reach.** CONFIRMED by parent erratum-1 `da050a74916b691a0af3a3257e286ce3725247628a80dc0ae4a341fb133887c2`.
  - The amendment replaces the direct-refutation requirement for P1-B1, P1-B2, P1-B3 and P1-B5 ONLY, wherever the 16/16 wording expresses it: DISP LF37 and LF41, REP LF108–110, and BRIDGE LF93.
  - Only the direct-16/16 quantifier changes.
  - The regeneration, negative-control, fail-closed, retention and floor/cap clauses all bind the six S_j and are never relaxed.
  - The twelve direct leaves keep the original contract.
- **A8. S_j refutations.** A qualifying parent replay under §7 of ALL SIX S_j (GA), including both of P1-B2 and both of P1-B5. *Status (status as of 2026-10-18T10:17:46 PDT): none satisfied. P1-B2.M2 attempt 1 is UNKNOWN; attempt 2 is frozen under v5e and not run (§6).*
- **A9. Digests.** Runtime proof-digest provenance for every counted replay, GA and GB: 18 + 18. No backfill (§9.1). *Status (status as of 2026-10-18T10:17:46 PDT): recorded for GA P0-B4 and P0-B5 only.*
- **A10. GB.** All three parts must hold (§9.2):
  - (i) parent acceptance of the GB necessity/differences note, including GB-name semantics and GB's independence from GA at CNF construction;
  - (ii) parent acceptance of the genuine-level GB normal-form bridge for the four P1 templates, with the genuine-move obligations of §9.2.1;
  - (iii) a qualifying parent replay under §7 for each of exactly 18 counted GB inputs.

  *Status (status as of 2026-10-18T10:17:46 PDT):*
  - **(i) and (ii) are ACCEPTED ONLY at conditional written-lemma scope**, by parent verdict `R/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md` (SHA256 `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`). That verdict accepts exactly two things:
    - for genuine configurations already in U/T16 normal form, the canonical assignment satisfies GB_C;
    - for genuine configurations in a P1 template, the genuine moves of §9.2.1 reach a representative M_s.
  - It accepts no GB refutation and no transformation of arbitrary Boolean GB models. It makes no equivalence claim with the GA formulas and does not import GA's auxiliary extension. The optional genuine-only GA alternative is NOT adopted.
  - (i) and (ii) remain written lemmas, conditional on A1–A3 and on the shared imports listed in the trust boundary below.
  - **(iii) is PENDING.** Parent GB replay is not yet authorized.
- **A11. Final verdict.** A final full-composition parent verdict with hostile assembly reviews (NFV LF42; DISP LF41) that reconciles A1–A10.

The mathematical derivation uses A1–A8. A9–A11 are protocol gates; A9 is also embedded in A4 and A8 through DISP LF40.

**Implication.** Assume A1–A11, and suppose a genuine non-classical set of five MOQLS(8) existed.
1. By A1–A3 it yields a model of B_C for one of the sixteen templates C.
2. If C is one of the twelve direct templates, A4 contradicts this.
3. Otherwise C ∈ {P1-B1, P1-B2, P1-B3, P1-B5}. For that C, by A5, UNSAT of every S_j with source C (A8, with A6 identifying the refuted bytes) implies Boolean UNSAT of B_C, a contradiction. A7 licenses this substitution.

Every set of five MOQLS(8) would then be classical, which answers Problem 16 affirmatively ONLY at n=8. NF refutes nothing by itself.

**Trust boundary.**
- **Primary layer:**
  - the imported primary definitions and rules #1–#3 (PRIM LF287–302);
  - the printed Lemma 10.
- **Accepted written proofs:**
  - A8/W8, U and T16, as accepted by the parent;
  - the encoder necessity and canonical extension, within U's scope.
- **Byte layer:** the hash-bound GA encoder, byte and name construction.
- **Certification predicates and trusted tooling:**
  - parent drat-trim `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`;
  - the feed-hashing / proof-digest relay of each counting desk, each version source-reviewed with its own controls;
  - the raw-log status parser, with raw logs hash-bound;
  - the S6 binder `bind_v1.py` `b010baa4dd5c7620f7c6215beeb052af80846bfd6c3ee0a80e8d8a235144786c`;
  - the NF finite checker `check_local_boolean_v1.py` `abfa623afdd89def969ef48abc2c4a508a84e1f1488651243d023e7dd7762531`;
  - the GB binder `R/moqls8-gb-parent-binding-v1/scripts/bind_gb_v2.py` `188c88de64fa994ca7e212f8d1618da9a0eb3433e2e162a835139bbfa4985f51`.

  The solvers are untrusted.
- **Leaf split:**
  - the twelve direct leaves rest on DRAT certificates of the exact B_C bytes;
  - the four P1 leaves rest on the written NF lemma (two model families plus parent finite checks; not compiled into DRAT, Lean or an independently checked clause audit, NF2 LF161) together with DRAT certificates of DIFFERENT formulas, the six S_j.
- **GB layer (for A10):**
  - the independently written GB encoder `L/code/gram_b_r2.py` `4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0`;
  - the GB necessity note and the genuine-level bridge (§9.2), accepted by the parent only at conditional written-lemma scope (`f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`). They are reviewed by two model families with parent finite/decode checks; they are not DRAT-, Lean- or kernel-checked;
  - the GA and GB P1 routes share the NF §1 combinatorics, the NF §4 stabilizer choice and its finite check, the WMAN template table, and U/T16. GB independence therefore holds at CNF construction only.

No Lean or kernel proof is asserted. Model reviews are not kernel checking or human peer review.

## 9. Additional parent obligations

### 9.1 Proof-digest provenance for every counted replay (A9)
Parent correction `a4b511195f64e0f8cfe2f8d0fe7ccc0bac278bec0859a9d3897c8de612b47b70` withdraws the interpretation recorded in `R/moqls8-parent-replay-predicate-addendum-v1.md` (`38451b0a0143b9b493df7a4ce79d8922e6b50ae94b50fb61bc21d22d18282d37`, preserved): that omitting the proof SHA was a mere clarification. F4 requires the proof SHA256 and byte count (DISP LF40).

**Scope:** every counted replay, GA (12 + 6) and GB (12 + 6).

**Existing observations** (the twelve direct GA receipts and the P1-B1.M2 GA verification):
- Their streams were discarded without digests. No digest can be recovered or backfilled.
- They stay PROOF_DIGEST_MISSING / QUALIFICATION_INCOMPLETE.
- They are not SAT results, counterexamples or failed refutations.
- Historical receipts and verdicts remain immutable.

**Closure** needs fresh conforming evidence under §7, or a separately explicit authorised protocol exception. None is granted. The §7 provenance bars apply to every counted run.

**Fresh conforming evidence so far** (status as of 2026-10-18T10:17:46 PDT): GA P0-B4 and P0-B5 under v5d. For each, the proof-stream SHA256 and byte counts at relay read, delivery and checker count are recorded and equal (§4.1). Every other counted replay, 34 of 36, lacks it.

### 9.2 Independent second encoding — GB (A10)
**Requirement.** Lane contract `S/phys-1-moqls8-problem16-contract.json`, SHA256 `25a018b0412f4a343f448b581762b6bb22fa604e371e02489f2e7405fbf72acf`, acceptance.positive_answer (LF29), requires "two independently written encodings for every exhaustive step". GA (`bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a`) alone cannot close this.

**Parent determination:** the counted GB exhaustive steps are exactly 18. They are the twelve direct GB_C and the six GB_{C,s}, where:
- GB_C = GB base + the 42 GB-own-name template units of C;
- GB_{C,s} = GB_C + the 126 GB-own-name M_s binaries.

All 22 generated GB hashes are input identities. The four GB P1 template formulas are identities only and are not counted refutations: P1-B1 `48c1688eaec843cab5d2cf375e0c1a2623fc37cebc6341fcb705e8c44b14a72f`, P1-B2 `0e62eed6f38e3556a409e9ee3798fff6d87984a7ecdc97d93e0de19eae95c192`, P1-B3 `f8fd0a51d8ff30069c105b52c20fdc02ad3f22a15a500e95014e5aac4954d487`, P1-B5 `87ec8493d2ec5807a6c7b4b065193fcb703e09d1d105cea62f4cac0f52bc9422`.

**Source.**
- Package `L/review/GB_ONE_P4_SOURCE_PACKAGE.r2.json` `b90b42cc6517af4d0d14aab6c19dc32a1ed67bbe56e90a7aca615d68df25bdf7`.
- Generator `5ca7c0da82c5ddd308acbbc2424da1ac6b4a0db08d0571f656eda5e841ffe262` and untouched encoder `4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0`.
- Necessity note r2 `L/review/GB_ONE_P4_NECESSITY.r2.md` `b9b4a595ca50b1334419d8584edc128e852dd4f206cd21fc5a07a793a2e72365`.
- Conventions `50a5bf4a8fbd9d6d45566428a10073db9148e0589592c7d8666c607c4eb67b37` and freeze `3a2a521b7f1d4ff2c153005d92f17a3abb96e0ee12d040c4bb6ddab81ad12d67`.

That GB carries the same semantic 42 units and M_s tails is a claim of the GB note: "implied by the same genuine leaf", not the same Boolean formula. The reviews below assessed it, and the parent accepted it at conditional written-lemma scope (below).

#### 9.2.1 Genuine-move obligations behind A10(ii) (Claude r2-delta MINOR-1(d); Codex r3-delta MINOR 1)
The obligations are stated explicitly here.

**Setting.** Fix C ∈ {P1-B1, P1-B2, P1-B3, P1-B5} and a genuine configuration already in the U/T16 normal form with template C. Use:
- the genuine move Q'_{τ(s)}(ρ(i),σ(j)) = P_σ Q_s(i,j);
- (σ, ρ) from the NF §4 generators, with σ permuting B = {4,5,6,7} and fixing 0, 1, 2, 3, and ρ permuting rows 2..5 and fixing 0, 1, 6, 7;
- τ(1) = 1 and τ(s) = σ(s+2) − 2.

The bridge must establish:
1. **U's row-0 standard form is preserved.** Q'_t(0,c) = |c⟩ for every square t and coordinate c, because ρ fixes row 0 and P_σ|j⟩ = |σ(j)⟩.
2. **The (1,0) pattern (SB2) is preserved.** supp Q'_1(1,0) = σ({1,2,3}) = {1,2,3} and supp Q'_{τ(s)}(1,0) = {σ(s+2)} = {τ(s)+2} for s = 2..5, because ρ fixes row 1.
3. **The Q1 weight-3 witness is preserved.** It is Q'_1(1,0), with support {1,2,3} in the row-0 frame.
4. **All 42 template bits are preserved.** σ(T_i) = T_{ρ(i)} for i = 2..7, where T_i is the template support of Q_1(i,0). So every Q1 column-0 mask is unchanged in its final row, and the ROWLEX keys are row-wise identical. This condition is imported from NF §4 (NF2 LF137–139) and the parent finite stabilizer check `R/moqls8-p1-normalform-parent-v1/RESULT.json` `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2` (`template_checks`), as stated in erratum r2 N3.
5. **A representative permutation square.** After the move, X_s is a permutation matrix for some s ∈ Rep(C): {2}, {2,4}, {2}, {2,3} respectively. This follows from bridge Lemma 1 plus NF §1 counting (erratum r2 N2 and N5).
6. **The exact 126 own-GB-name tail binaries hold.** A permutation X_s implies, for i = 2..7 and 1 ≤ c < d ≤ 7, the clause ¬g_s((0,c),(i,0)) ∨ ¬g_s((0,d),(i,0)).
   - The literals are GB's OWN identifiers id(g_s((0,c),(i,0))) = 1568(s−1) + 49c + 7i − 5, with TRUE = 1.
   - Each clause is serialized as a sorted negative pair, in (i, c<d) order.
   - The parent binder decoded every appended literal of all six GB strengthened inputs through GB's own table: GBBINDING `R/moqls8-gb-parent-binding-v1/GBBINDING.json` `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`, `controls.c_decode_inverse_name_table`. Each has 126 tail lines, no decode errors, and decodes to the intended (s, i, c<d) in order with negative ascending literals.
   - The GB tail byte identities (GBBINDING `tails`; equal to the lane manifest's `GB_M_binary_tail_sha256` for the same inputs):

| s | GB M_s tail SHA256 | Bytes | First line | Used by |
|---|---|---|---|---|
| 2 | `140a33f7d6b763ed5f988168280bcbe8bc77716bdb460607b9401f891ec589ab` | 1764 | `-1675 -1626 0` | P1-B1.M2, P1-B2.M2, P1-B3.M2, P1-B5.M2 |
| 3 | `03444c39e52e39fccc589c9bab01da77c77cc9ebc44c3afe405d281e6a33d2ff` | 1764 | `-3243 -3194 0` | P1-B5.M3 |
| 4 | `9b79f60ed496d678142effdf926d592ec90e5d6a6d0e692d36ebb3e964353a40` | 1764 | `-4811 -4762 0` | P1-B2.M4 |

7. **Nonemptiness is separate from at-most-one.** The 126 binaries say only that each Q_s(i,0), i = 2..7, has AT MOST one support coordinate in {1..7}. Nonemptiness of each support comes from the genuine ONB facts (bridge Lemma 1 (A)) and, inside GB, from G3. It does not come from the M_s tail. Only "X_s is a permutation ⇒ the 126 binaries hold" is used (erratum r2 N4).

**Status.** Items 1–7 are ACCEPTED at conditional written-lemma scope by the GB parent verdict (`f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, LF8 and LF15). The shared mathematical inputs remain imports at their accepted scopes. GB does not independently replace them: U/T16, the WMAN template table, NF §1 combinatorics, and the NF §4 stabilizers and representatives.

**Input identity: BOUND (identity only).**
- Parent `R/moqls8-gb-parent-binding-v1/GBBINDING.json` `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673` (PASS) decodes every appended literal through GB's own table.
- The lane adapter's manifest `L/evidence/GB_ONE_P4_MANIFEST.r2.json` `4daf8fcf9cbc5645fa74eeafc498484dd4a1aa2397b24f428b081d31050b680d` and its own-hash receipt `L/evidence/GB_ONE_P4_OWN_HASHES.r2.json` `9781c877728b6a6f53511ecdd618eb4fc4ed3e87369398e82892cb4da0d9943f` were x-created before the parent file was read.
- They agree on all 22 (SHA256, bytes, headers): comparison `L/evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json` `df3fb6e6661f46b5cb9673bfc8750482c69978cf0b64d7ea7224f4a434f0b651`.
- Base body identity: `f5da05206f44ff72e5aeade076820e2de52c9d2352f58b048ded1df76bdbf1b9` (350550717 B, 17025578 clauses).

| Counted GB input | Kind | GB SHA256 | Bytes | Header | Identity | Qualified parent replay |
|---|---|---|---|---|---|---|
| P0-B1 | direct GB_C | `b364c1e6e21af72f59692e9ee3777e955b59b9eac3727f323eb85a91d71cc9fa` | 350551018 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P0-B2 | direct GB_C | `259bc80bbadb36791edfdc2d3f07b57ff225782b55b4690cadcf7ec94c849b9d` | 350551016 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P0-B3 | direct GB_C | `ca58afda03a78d1cc945eeea9e53e7851aa76fa44063d75d460230ca7a1bdc63` | 350551014 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P0-B4 | direct GB_C | `77df8b038dc995dce79737e7956958a2d0ec3e99bfc3abc1cf3c65f95b7a9a9a` | 350551012 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P0-B5 | direct GB_C | `dad7a44837d72d4b1f20007eea9e3c344edc00b493e4dc965afd6684a2e89d10` | 350551013 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P0-B6 | direct GB_C | `76f4b6634f0d5c0ff4b9398c1016c955cebc6fbee835ea4ab0983a7f84414abf` | 350551010 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P1-B4 | direct GB_C | `03271e5afc5b161debaa58ccf00dd56df97f196baa12da4685bb6e97b3d2408b` | 350551013 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P1-B6 | direct GB_C | `10d40a85c310fba22b9ce3083923765e1fb1ef07274bb76fa1898c7c8d999cb2` | 350551011 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P2-C1 | direct GB_C | `2311bd829bcfd8c0e1b7531ddffa26a39f255ca1e26d87d793b2451d0c053135` | 350551016 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P2-C2 | direct GB_C | `9ecc9df4873811ec1307fdd6bc25e5451cd6dc7f43a6496686306fd5284e7326` | 350551014 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P2-C3 | direct GB_C | `24d93eb50a0fe7a352d718859aa62769a9d458b444e94f62cdabce8a52422f78` | 350551011 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P2-C4 | direct GB_C | `88fa1587fcd1269774ce4cef8d26564eea9e576ab0ae1b09b822015e8c1ef977` | 350551010 | `p cnf 3803745 17025620` | BOUND (identity only) | PENDING |
| P1-B1.M2 | strengthened GB_{C,s} | `1873f550493e6f74c65fa6b185b0f499551dece56822258dbfbaac3338813687` | 350552783 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |
| P1-B2.M2 | strengthened GB_{C,s} | `1aa38ae7c04cd5d8b5f8bd224aa825cee149313d25a3886bb2e76eadf078a3f8` | 350552781 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |
| P1-B2.M4 | strengthened GB_{C,s} | `2544240d14e105b1ec7ff25f9d7366ed9aad6faa2db8b36d4c3af42001698293` | 350552781 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |
| P1-B3.M2 | strengthened GB_{C,s} | `47e099afcf7b3fbae36a90ae23f03e4e6b2e13a97a0a88c05c1b9602b1268871` | 350552779 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |
| P1-B5.M2 | strengthened GB_{C,s} | `6a423719e4f00aa27a2e14acba89c09a02c4b368d7d012adc0224e93830d7065` | 350552778 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |
| P1-B5.M3 | strengthened GB_{C,s} | `0ae019350469470e5a232e8b70a263dedbc2598ff628fc06ecd2c26c17ef7c51` | 350552778 | `p cnf 3803745 17025746` | BOUND (identity only) | PENDING |

**Parent status.** Parent verdict `R/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md` (SHA256 `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, 5094 B, 2026-10-18T09:57:24-07:00): CORRECTNESS-ACCEPTED at the conditional written-lemma and input-identity scopes ONLY.
- It accepts no GB refutation, no n=8 theorem and no full gate.
- The optional genuine-only GA alternative is NOT adopted.
- GA and GB are independent only at CNF construction (verdict LF18).

**Reviews behind that verdict:**
- GB necessity:
  - Codex `R/n8-gb-necessity-bridge-codex-v1.note.md` `ad9e5f04e9eedcf0f5daaf612010b3bd0fa6e86f786dbcbb3412fe8fe44113fc`: ACCEPT.
  - Claude `R/n8-gb-math-bridge-claude-v1.note.md` `4aeed1e22213477a220681ec9eff004f73ec6b1caa5f623455d990b4c03d15e9`: ACCEPT-WITH-FIXES, 0/0/6.
- Genuine bridge `L/review/GB_NF_GENUINE_BRIDGE.r1.md` `1a352d364a2e2c68a344735537db7e6f10861e01d520cf75dcbef7a61fbf504b`:
  - Codex: ACCEPT-WITH-FIXES, 0/0/2.
  - Claude: ACCEPT-WITH-FIXES, 0/0/6.
- Errata, x-created; originals unchanged:
  - `L/review/GB_REVIEW_ERRATUM.r1.md` `7b51788c6881efd339a2a9b10732f1292684e7775773021d33f4482ac77d1c4e`;
  - `L/review/GB_REVIEW_ERRATUM.r2.md` `a2d3b9b3cd7bfe1cb4ffe20bbfbaf80856051ab6a4e743ffa86591513fbe407d`, which incorporates r1.

**GB replay status** (status as of 2026-10-18T10:17:46 PDT): parent GB replay is not yet authorized. All 18 counted GB inputs are PENDING.

**Worker runs.** The lane's worker GB runs (`L/evidence/gb_direct_v3` to `v6`) are worker evidence only. They are neither counted nor cited as evidence here, and they are stood down. Two lane records relate to them; neither is evidence:
- their spent-FIFO deletion deviation, `L/review/GB_WORKER_FIFO_UNLINK_DEVIATION.r1.md` (SHA256 `9357eb48a6ff83138386e69a27ff5c3d2fd0a8dcfd62e82d52c5dcfdd0271704`, 11040 B);
- a static handoff for a parent-owned replay, `L/review/GB_R6_PARENT_HANDOFF.r1.md` (SHA256 `0870f26c2a3713a0e520b7e92721888de9ff8d7edc5dfdaeb684c58d4d63dc1b`, 12862 B).

## 10. Precise current conclusion

As of this draft (status as of 2026-10-18T10:17:46 PDT) the final implication is NOT discharged.

**Accepted:**
- U and T16 with their byte bindings;
- the scoped A8/W8;
- NF as a conditional per-C Boolean lemma;
- the reach of A7 (erratum-1);
- the GB necessity note and the genuine NF bridge, at conditional written-lemma scope only (`f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`; A10(i)–(ii)).

**Parent-qualified counted replays:** GA direct P0-B4 and P0-B5 (v5d; `2e7a12e3196d540511389b9d5690f69e325ff5988dfe226084ee5f4c54d67adb`). 2 of 36.

**BOUND (identity only):**
- the six S_j;
- the 22 GB inputs.

**Observations, not qualifying:**
- the twelve historical direct GA native UNSAT observations (PROOF_DIGEST_MISSING);
- the historical P1-B1.M2 verification (PROOF_DIGEST_MISSING);
- UNKNOWN: P1-B2.M2 v5d attempt 1 (external SIGTERM 09:25:51) and the historical P1-B3.M2 (disk-floor stop).

**Pending:**
- A4: fresh replays of the ten direct leaves not yet qualified;
- A8: all six S_j replays (P1-B2.M2 attempt 2 frozen under v5e, not run);
- A9: digests for the 34 counted replays not yet qualified;
- A10(iii): 18 parent GB replays (not yet authorized). A10(i)–(ii) are accepted at conditional written-lemma scope only;
- A11: the final verdict.

**This is not:**
- an unconditional n=8 exclusion;
- whole-base F_one UNSAT;
- a result for all n;
- a K4/K5 claim from old inputs;
- a novelty, priority or publication claim.

**Non-load-bearing runtime facts:**
- The producer signed-cube pilot is stopped and quarantined.
- UNKNOWN leaves and lifecycle/static/metadata smokes contribute ZERO refutations.
- Producer12 counts are never relabelled as parent proofs.
- The old lease 7ff6 has ended.

This note authorises no solve, CNF or ledger amendment.

## Appendix A — r1 findings (applied in r2, retained)

All r1 findings stay applied as in r2's Appendix A:
- Claude m1–m11;
- Codex M1;
- the two parent obligations.

r3 moves the certification predicate into §7, renumbers the obligations to §9 and the conclusion to §10, and prints every pin in full.

## Appendix B — r2-delta findings (Claude `4ae89ea9a967f44ed5000e12c451c40069c8d2bc1fec5fbc595c6b57a97af4c9`) → r3

| Finding | Repair in r3 |
|---|---|
| MINOR-1 GB under-specified | A10 (i)–(iii); §9.2: exactly 18 counted GB inputs (parent determination); 22 hashes are identity only; GB note claims marked as such; independence at CNF construction only; T16 and NF finite checks marked supporting only (§§3, 5); A9 and §9.1 cover GA and GB |
| MINOR-2 D12 label | §4 table: "parent-accepted native UNSAT observation; PROOF_DIGEST_MISSING" plus a "Qualified (fresh, digested)" column = PENDING |
| MINOR-3 fail-closed list | §7: full refusal list; provenance bars for every counted run; own controls for every relay version (GA and GB); checker pinned to a46c0c71 or a reviewed successor |
| MINOR-4 A7 | §8 A7: confirmed by erratum-1 `da050a74916b691a0af3a3257e286ce3725247628a80dc0ae4a341fb133887c2`; only the direct-16/16 quantifier changes; control, regeneration, fail-closed, retention and floor/cap clauses bind the six S_j |
| MINOR-5 wrong abbreviations | All pins printed in full; registry r1/r2/r3 comparison recorded in the header. The comparison wording ("identical") is NARROWED in r4 to unchanged identity fields (Appendix D) |
| MINOR-6 inline pins | Full SHA256 for every identity; audit file paths restored (§4). The claim "registry r3 lists every cited file and identity" is NARROWED in r4 to its 80 registered files plus listed identities; the twelve historical receipt paths and byte counts are printed in §4 (Appendix D) |
| MINOR-7 labels | §10 "BOUND (identity only)" for GB; "no G1 family is defined in the cited sources" (§5); digest-agreement control marked NEW (§7) |
| MINOR-8 trust boundary | §8: PRIM rules #1–#3; certification predicates and trusted tooling; GB layer and shared trust base |
| MINOR-9 deleted r1 guards | Restored (Appendix C) |
| MINOR-10 gate wording | §8: "may be asserted only if A1–A11"; the 'modulo provenance' / 'pending GB' prohibition (NFV LF42) |

## Appendix C — restored r1 guard texts
1. Later receipts/reviews require a new assembly version (header).
2. The independent binding's scope; worker producer code `L/code/n8_one_p4_formula.py` (`61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400`) and its receipts do not substitute (§2).
3. T16 assumes no P4 on the four other squares (§3).
4. The twelve direct leaves are not the historical producer candidates (§4).
5. The rejected generator r1 is not evidence; no CNF or solve came from the generators (§6).
6. The producer lane has no counted native role on S6, now for GA and GB (§6).
7. Producer12 counts are never relabelled as parent proofs (§10).

## Appendix D — r3-delta findings (Codex `6c0011a806f05a4716318ac72c3d24c0f73c65c8088977b7fd9bb95bf9e59c62`) → r4 draft

| Finding | Repair in r4 (draft) |
|---|---|
| MINOR 1 — Claude r2-delta MINOR-1(d) implicit (r3 LF348, LF407–418) | New §9.2.1 makes items 1–7 explicit: row-0 form, (1,0) SB2 pattern, Q1 witness, all 42 template bits via σ(T_i)=T_ρ(i) with ROWLEX keys, the representative permutation square, the exact 126 own-GB-name tail binaries (ID formula, ordering, parent decode, tail SHA256s), and nonemptiness kept separate from at-most-one. A10(ii) points to §9.2.1 |
| MINOR 2 — registry claims overreach (r3 LF36–38, LF516; registry r3 LF18, LF447–520) | Header narrowed to the 80 registered files plus listed identities, with the cited-but-unregistered files named; comparison narrowed to unchanged identity fields, recoded records stated, r3 wording withdrawn; §4 restores the twelve historical receipt paths and byte counts; Appendix B rows MINOR-5/6 annotated; no new registry, new citations pinned inline (Appendix E) |
| GB acceptance statements (Codex note LF10; r3 LF76, LF347–348, LF383, LF447, LF480) | §1 missing-list, §8 A10 (i)/(ii) annotated "ACCEPTED ONLY at conditional written-lemma scope" pinning `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c`, §8 trust boundary, §9.2 parent status, §10 accepted/pending lists; GA alternative not adopted; input identities stay BOUND; replay qualifications and final composition stay PENDING |

**Parent status updates** (status as of 2026-10-18T10:17:46 PDT):
- A4: P0-B4 and P0-B5 PARENT-QUALIFIED PASS (§4.1).
- §6: P1-B2.M2 attempt 1 UNKNOWN; attempt 2 frozen under v5e, not run.
- A9 counts updated.
- §7 proof-digest bullet aligned with the parent predicates: read = delivered = checker-consumed N.

No mathematical claim, scope or predicate is weakened.

## Appendix E — artifacts first cited in r4 (pinned inline; not in registry r3)

| Artifact | SHA256 | Bytes |
|---|---|---|
| `R/moqls8-assembly-r3-delta-codex-v1.note.md` | `6c0011a806f05a4716318ac72c3d24c0f73c65c8088977b7fd9bb95bf9e59c62` | 2158 |
| `R/moqls8-gb-necessity-genuine-nf-parent-verdict-v1.md` | `f529224e82ce6126d1a1fbc5776330d4b9ac6970faadb681acb3a8b56358ce0c` | 5094 |
| `R/n8-ga-leaves-P0-B4-B5-parent-audit-v1.json` | `2e7a12e3196d540511389b9d5690f69e325ff5988dfe226084ee5f4c54d67adb` | 3599 |
| `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P0-B4.json` | `457dfe551344a8340e22116d9862263168a1467e5dcf91c653f107e9afad0366` | 24042 |
| `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P0-B5.json` | `e3187cd898c28c66260f5142aae7c68cf7dff5122d9b9d737749c8cc48c4250b` | 24041 |
| `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5d-two-short-leaves-parent-a1.json` | `44739921890eeab80493214e5fd65fc18b16e7160b9ab5fdcce12a60380492e0` | 41979 |
| `R/moqls8-strengthened-parent-replay-v1/runs/run-20261018T100330.json` | `ef15f7c5e8d6700fedf28a313595f24d46777f4e87cd6e6648d03cc51abd8232` | 12902 |
| `R/n8-two-short-leaves-parallel-parent-go-v1.json` | `92ace11da7125559fcab817e13cc8fb3457a800f1df978428bab196da8c8d9a5` | 1376 |
| `R/n8-v5d-native-control-parent-audit-v1.json` | `c3191c6d890abc48b6c51025f396fad35e6ff5ee41ed6accfe321e843f3b81e4` | 2833 |
| `R/moqls8-strengthened-parent-replay-v1/receipts/v5d-P1-B2.M2.json` | `62a388cb165895dece12fe5e3d5209c14e7f061977ca502ed7b59d16fe11c777` | 24278 |
| `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5d-formulas-parent-a1.json` | `f20a6f8ec15404848be73ca45849992f32fdfb7219f883b039387ef2a3fb889f` | 53350 |
| `R/moqls8-strengthened-parent-replay-v1/PRE-EXEC-v5e-B2-M2-parent-attempt2.json` | `83ce9d8d2716f003288a2cd6db6c056097b8d788e11d5a8dd20f9ec447662ab6` | 37060 |
| `R/n8-v5e-native-control-parent-audit-v1.json` | `65ab801c9070701dcc4235855a7161c881eead0dd97b19a5aa2e7d652bc3c5d9` | 2230 |
| `L/review/N8_ASSEMBLY.r2-to-r3.diff` | `28497a38cc09722a518cffee506c6e2ab8472b90c75e26f846911faba7915f50` | 82446 |
| `L/review/GB_WORKER_FIFO_UNLINK_DEVIATION.r1.md` | `9357eb48a6ff83138386e69a27ff5c3d2fd0a8dcfd62e82d52c5dcfdd0271704` | 11040 |
| `L/review/GB_R6_PARENT_HANDOFF.r1.md` | `0870f26c2a3713a0e520b7e92721888de9ff8d7edc5dfdaeb684c58d4d63dc1b` | 12862 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B1.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `c818de09c159884a86cf1994453828fc4a111e0c0b449e217efe650f3020e271` | 10077 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B2.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `969f587dad9d3147dd45d6d37770954c97424743535cde50f75f5c877620d05e` | 10088 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B3.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `80e1db9fb550cd1918812e1aa44e979278525e46e2ba6bd0d0f2afa7eb536a3c` | 10110 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B4.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `004bc5fcb36fa2c6f640d5b970b08660a1572c2dccd5dd217bab6fcf03c39deb` | 11868 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B5.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `4c31cdbf5ee2f984d18ca711d6332355404319a440943e220d3e3a375561a0b4` | 12318 |
| `R/moqls8-fone-parent-replay-v1/receipts/P0-B6.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `b72a4cb9c183525f37956aaa212b5b744a6b1fd00ef9e2a65c6d154154681d9f` | 12142 |
| `R/moqls8-fone-parent-replay-v1/receipts/P1-B4.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `8c81147135cd114a648c1bc9f0de2b51f243a848a96ca8e230314242ebe0cbcf` | 10088 |
| `R/moqls8-fone-parent-replay-v1/receipts/P1-B6.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `255c1df89a96a9bca3bba573e7ef54ee2c9c8fec733cdef48fee9a8dba3e39d7` | 10121 |
| `R/moqls8-fone-parent-replay-v1/receipts/P2-C1.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `1192ea014b4b9e60dc4e059837783a8062db7d1dd2df272f4faaa9c5ba76f2a1` | 10102 |
| `R/moqls8-fone-parent-replay-v1/receipts/P2-C2.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `03273c7be4a8ade0a4cf00d6001794d76db720ab025b55d3f05ca0d2e8401745` | 10614 |
| `R/moqls8-fone-parent-replay-v1/receipts/P2-C3.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `acd0763c44f93eff3c804351ce9c421c3e354559c739988a66d70feff43a961d` | 10123 |
| `R/moqls8-fone-parent-replay-v1/receipts/P2-C4.json` (historical receipt; SHA256 already in registry r3 `identities`, path and bytes restored) | `2bbd69e3f7fafe31e35c4dbf9a8023e159d248f09cc18e0135c105a6edc12070` | 10127 |
