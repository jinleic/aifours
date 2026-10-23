# Ball–Simoens Problem 16 at n=8 — frozen ASSEMBLY r2

**Status: CONDITIONAL ASSEMBLY. Not an n=8 theorem, not protocol-complete, no novelty/priority claim.**

Frozen at 2026-10-18T07:50:28.083047-07:00. r2 supersedes `N8_ASSEMBLY.r1.md` (SHA256 `8c9cf1c2cc079e2bfdbab8bd6e0a2c9a79268a534fb4043f9ad1028820fea986`) as the object of any final composition verdict. r1, its registry `2b727fde…6e21798` and the mandatory r1 addendum `N8_ASSEMBLY_QUALIFICATION_CORRECTION.r1.md` (`8bfd2dee…8d4f`) are preserved unchanged; the addendum is incorporated in §8. r2 applies both hostile reviews of r1 — Codex `R/moqls8-assembly-r1-codex-v1.note.md` (`e6687b76…bc37`; 0 FATAL, 0 MAJOR, 1 MINOR) and Claude `R/moqls8-assembly-r1c-claude-v1.note.md` (`5148c21d…5f0d`; 0 FATAL, 0 MAJOR, 11 MINOR) — and adds two parent obligations. Appendix A maps every finding to its repair. No link status is raised beyond its cited authority.

Path prefixes: `L=/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16`; `R=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`; `S=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening`. "LFa–b" cites 1-based LF line numbers of the named SHA-pinned file. Short names: DISP = unified parent disposition; REP = repair overlay; BRIDGE = unified bridge r2; TPL = T16 source; NF2 = normal form r2; NFV = NF parent verdict; PRIM = primary raw text; F10 = first-ten verdict.

Registry `L/review/N8_ASSEMBLY_LINKS.r2.json`, SHA256 `eb7786b92f848ae8e5b74007a555fd2b0257b9665a5ca2dd03be069dfd71e060`. **The registry fingerprints the link documents, manifests and receipts, plus the byte identities it lists explicitly; r2 adds the original CNF, the encoder source and the full name table. Every file entry was rehashed at this freeze. Any other identity is pinned inline here or imported through the cited binding records.** Rehashing is a static read, not a native or proof replay.

## 1. Exact target, terminology and logical shape

**Primary source:** `L/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9` (Ball–Simoens, arXiv:2607.12933v2).
- A QLS(n) is an n×n matrix over Cⁿ whose rows and columns are orthonormal bases (PRIM LF195–196).
- Two QLS are orthogonal if {ψ_ij ⊗ φ_ij} is an orthonormal basis (LF209–215).
- A t-MOQLS(n) is a SET of t pairwise orthogonal QLS (LF215–217).
- Set isotopy allows: (i) entry phases; (ii) common row/column permutations; (iii) a separate unitary on each square (LF217–222).
- A set is classical if, up to isotopy, all entries lie in {|1⟩,…,|n⟩} (LF223–225).
- Problem 16 (LF642): "Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily classical?" At n=8, n−3=5 and n≠4.

**Target (n=8 only):** every set of five MOQLS(8) is classical in the sense of PRIM LF223–225.

*Extraction note (m10c).* PRIM LF209–215 is damaged by extraction. Stray lines contain only "n", and the basis appears as "C ⊗ C". The page-preserving extraction `L/sources/2607.12933v2.layout.txt` (`df1d8b14…4219`, LF104–105) shows the two "n" superscripts displaced onto the line above. The phrase is read as "an orthonormal basis of Cⁿ ⊗ Cⁿ".

*Terminology (m10b).* Here **genuine** means realised by actual vectors in C⁸ that satisfy the QLS and pairwise-orthogonality axioms. A **Boolean model** is any satisfying truth assignment of a CNF and need not be realised. "Genuine" is unrelated to the paper's phrase "not genuinely quantum", which means classical (PRIM LF201, LF223).

*Relabelling (m10a).* U and T16 also relabel the squares of the set (BRIDGE LF59; REP LF37–38). Relabelling is not one of isotopy moves (i)–(iii), but it is harmless:
- A t-MOQLS(n) is a set (LF215–217).
- Move (ii) never changes which vectors occur as entries. Move (i) changes each entry only by a phase. Move (iii) acts on each square separately.
- Hence a set is classical iff each of its squares is classical in the single-square sense of LF201–203 [elementary]. This is invariant under relabelling.
- A8's conclusion "wholly classical" is read exactly as this set-classicality.

**Logical shape.** Write B_C = F_one ∧ (the exact 42 Q1 column-0 units of template C). For the six pairs (C,s) of §6, write S_j = B_C ∧ M_s.
1. **U + T16.** By isotopy moves and square relabelling, every genuine non-classical five-set yields a configuration whose canonical assignment is a model of at least one of the sixteen exact B_C (§§2–3).
2. **D12.** Twelve B_C have parent-accepted exact UNSAT observations. Their protocol qualification is incomplete (§§4, 8.1).
3. **NF, per C.** For each C ∈ {P1-B1, P1-B2, P1-B3, P1-B5}, the accepted NF lemma gives: UNSAT of every S_j with source C implies Boolean UNSAT of B_C (§5). NF by itself refutes nothing.
4. **S6.** All six S_j are bound. None yet has a qualifying UNSAT (§6).
5. **Composition.** A contradiction follows only under ALL antecedents A1–A11 of §7.

**Currently missing:**
- qualifying UNSAT of all six S_j under the full predicate of §6;
- proof-digest provenance for all 18 counted replays (§8.1);
- the independent second (GB) encoding, with proof-certified evidence, for every exhaustive step (§8.2);
- the recommended parent erratum on the amendment's reach (§7, A7);
- a final full-composition parent verdict.

No conclusion of §7 is claimed now.

## 2. Link U — accepted unified reduction, with its exact conditions

**Exact statement.** Take ANY genuine non-classical set of 5 MOQLS(8). Standardise row 0 and apply accepted A8/W8; this produces a weight-3 witness. After square relabelling and common row/column moves, the normal form has:
- Q1(1,0) support {1,2,3} and the other four supports {4},{5},{6},{7};
- non-strict Q1 column-0 ROWLEX;
- canonical Gram/auxiliary values satisfying the exact weak formula F_one.

The other four squares may be classical or non-classical.

**Status.** PARENT CORRECTNESS-ACCEPTED as a CONDITIONAL mathematical reduction and exact formula binding (DISP items 2–3, LF13–14). It is expressly NOT an exclusion by itself. Authority: `R/moqls8-unified-parent-disposition-v1.md`, SHA256 `29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb`. The accepted text is read together:
- BRIDGE `L/review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md` `c391a67a…bbb3`;
- REP `L/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md` `e0f3c860…1704`.

**Load-bearing imports:**
- **W8 (scope corrected, m6).** In row-0 standard form, the five supports at any cell off row 0 are disjoint and avoid the column coordinate. Every such entry therefore has weight ≤ 3 (A8 parent verdict LF13). W8 is ONLY this row-0-frame bound.
  - The bound in an arbitrary line frame is NOT W8. This includes the column-0 frame used for Q1's column-0 transition.
  - That bound is proved inside T16 §1 (TPL LF9–18) and is imported only through T16's admitted range (§3).
- **A8.** Premise: ALL FIVE squares and ALL entries. If every entry of every square has weight ≤ 2 in a row-0 standard form, then all weights are 1 and the set is wholly classical (in the sense of §1).
  - Contraposition gives some weight-3 entry in a non-classical five-set. It is NOT a per-square P4 premise.
  - Authority: `R/moqls8-k1k2-parent-verdict.md` `919daeac…a8f9`. Proofs: `R/moqls8-k1k2-parent-inputs-r2/PROOF_K1_K2.r1.md` `094dab60…3ff3c` and `.r2.md` `d36e646c…2d86`.
  - A8 imports the printed Lemma 10 (PRIM LF342–356). It does NOT import the Egan–Wanless counts or the K1/K2 corollaries.
- **Necessary encoder families and canonical extension, within U's scope:**
  - constants and G2–G5;
  - exact AND/singleton and inclusive-prefix auxiliaries;
  - one true Q1 w3 witness, with all other w3 flags false.

  Source: `L/review/K4K5_ENCODING_SOUNDNESS.r3.md` `a83d3050…8e59`, imported only through U's accepted scope.
- **Original encoder, byte and name binding.** `R/moqls8-encoder-binding-v1/binding-result.v2.json` `dce638a9…6112` ties the following together:
  - encoder `R/moqls8-encoder-binding-v1/code/gram_a.py` `bf1aada1…d05a`, with argv `--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex`;
  - `L/evidence/gram_dev_v1/GA5L_K5_sb2.cnf` `6ecb77a7…469b` (509915 vars, 5740230 clauses, 137664569 B);
  - full name table `R/moqls8-encoder-binding-v1/K5.names.json.gz` `b8423861…2522`;
  - primary map `L/evidence/gram_dev_v1/GA5L_K5_sb2.map.json` `7b4dd597…b197`.

  The first three are now explicit registry entries (Codex M1).
- **Exact weakening.** Delete ONLY the four row-0 P4-ALO clause lines for squares 2–5, at zero-based indices 5735297, 5736866, 5738435 and 5740004.
  - KEEP square 1 (index 5733728).
  - Retain all one-way w3 implications, G families, SB2 and ROWLEX.
  - Add no weight-1, classical-net, L-sort, fixg or other-P4 condition.
  - Recipes: deletions `L/evidence/UNIFIED_ONE_P4_DELETIONS_v1.json` `4509b3e7…e3a6`; weak recipe `L/evidence/n8_one_p4_templates_v1/BASE_RECIPE.json` `264288f8…0c18`.
  - Weak formula `374d6fb4…eeb9` (509915 vars, 5740226 clauses). It is streamed only.
- **Independent weak/base/table/leaf binding.** `R/moqls8-one-p4-parent-binding-v1/RESULT.json` `65311ab0…80b0`.

**Mandatory conditions:**
- genuine QLS/MOQLS axioms;
- the stated row-0/witness normal form;
- the exact weak deletion recipe;
- canonical auxiliary extension.

No reduced-K5, non-classicality or P4 requirement is imposed on squares 2–5. No old-F or c112 proof is imported.

## 3. Link T16 — accepted sixteen-leaf cover (authority and import range, m7)

**Exact statement (property form).** Take five genuine pairwise-orthogonal QLS(8), row-0 aligned, with the specified (1,0) support pattern. The common residual permutations and square relabelling, followed by non-strict ROWLEX, take Q1's column-0 supports to one of the sixteen listed forms. Its canonical assignment models that B_C (DISP LF12; BRIDGE §4, LF78–89).

**Authority.** Item 1 of the unified parent disposition (DISP LF12, "Property-form T16 — ACCEPTED"). r1's "ACCEPTED by U" is withdrawn.

**Admissible text.** Exactly the F3 import range (DISP LF29) of TPL `L/review/K5_COLUMN0_TEMPLATE_COVER.r1.md`, SHA256 `1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a`:
- TPL LF9–19, with the stated support hypothesis replacing LF20's justification;
- TPL LF22–55;
- TPL LF60–64, with the explicit residual moves of REP LF34–38, and WITHOUT the reduced-K5/P4 sentence (TPL LF62–63);
- TPL LF66–109.

**Excluded; not premises.** TPL LF1, LF4–5, LF59 and LF111–131. These lines still assert the old 13-case/c112/reduced-K5 interface (e.g. LF1, LF62–63, LF111–113). The conclusion that every genuine normalised configuration lies in one of SIXTEEN templates comes from DISP LF12 and BRIDGE LF86–89, not from TPL LF111.

**Supporting finite check.** `R/moqls8-unified-delta-v1/RESULT.json` `d3eedf78…ec8b` found 16 orbits among 140 sorted / 43290 labelled necessary patterns. It supports the written component proof; it does not replace it.

**Leaf manifest.** WMAN `L/evidence/n8_one_p4_templates_v1/MANIFEST.json` `355b3380…fc74`. Every B_C has 509915 variables and 5740268 clauses: the weak body plus 42 signed units fixing all coordinate-1..7 bits of Q1 rows 2..7 in column 0.
- ALL 16 enter the cover, including P0-B6, P1-B6 and P2-C4.
- This is a cover of genuine counterexample images. It does NOT assert that every Boolean model of bare F_one lies in one of these 16 masks.

## 4. Link D12 — twelve direct leaves

**Status.** Each exact B_C below is **PARENT-ACCEPTED UNSAT** as a measured-feed native observation:
- first-ten verdict `R/moqls8-fone-first10-parent-verdict-v1.md` `61130625…83e4`;
- direct-12 addendum `R/moqls8-fone-direct12-parent-verdict-v1.md` `515cd9e1…d667`;
- RESULT `f63dbeeb…ee0c` and RESULT-ADDENDUM `a051418a…bab` in `R/moqls8-fone-parent-replay-v1/`.

**Protocol qualification: PROOF_DIGEST_MISSING / QUALIFICATION_INCOMPLETE** (§8.1). This assembly changes neither status.

Receipt directory D=`R/moqls8-fone-parent-replay-v1/receipts/`. Formula SHA is the full DIMACS input hash.

| Leaf | Exact B_C formula SHA256 | Parent receipt file / SHA256 | Status |
|---|---|---|---|
| P0-B1 | `a29d546cad564cd7d20cf1b40dbe18d7baa57b0f25e109fb75e5a8d8042c33c4` | `D/P0-B1.json` / `c818de09c159884a86cf1994453828fc4a111e0c0b449e217efe650f3020e271` | accepted exact UNSAT |
| P0-B2 | `ec6b8507c6cf74fafe0111780672d70ca15ca0825590064899d7f853a45e4dbc` | `D/P0-B2.json` / `969f587dad9d3147dd45d6d37770954c97424743535cde50f75f5c877620d05e` | accepted exact UNSAT |
| P0-B3 | `c42d3520ba7f1e210f09c18d97dbf7988e143d01d06ef932437685ab57a98ba7` | `D/P0-B3.json` / `80e1db9fb550cd1918812e1aa44e979278525e46e2ba6bd0d0f2afa7eb536a3c` | accepted exact UNSAT |
| P0-B4 | `7b4e49c45f7e3678710171d03ae3a01b041640052f7ace3778699bb09bba3b44` | `D/P0-B4.json` / `004bc5fcb36fa2c6f640d5b970b08660a1572c2dccd5dd217bab6fcf03c39deb` | accepted exact UNSAT |
| P0-B5 | `fc52e1092e7818f1ba23498cf85e44f3cbf9f0a2765522ba83b72f32c3bcce0f` | `D/P0-B5.json` / `4c31cdbf5ee2f984d18ca711d6332355404319a440943e220d3e3a375561a0b4` | accepted exact UNSAT |
| P0-B6 | `37afcaae7706407caab277065143a37a4eb09381a8d8f13f309219f7ecba4d08` | `D/P0-B6.json` / `b72a4cb9c183525f37956aaa212b5b744a6b1fd00ef9e2a65c6d154154681d9f` | accepted exact UNSAT |
| P1-B4 | `b1c0200391e35af736e610dcabbb34a4d19c57ffbf13c9a440cd9b70c3d09fb5` | `D/P1-B4.json` / `8c81147135cd114a648c1bc9f0de2b51f243a848a96ca8e230314242ebe0cbcf` | accepted exact UNSAT |
| P1-B6 | `a6b45fd3a62599afedea680392eff1a65a1e44ae524b460e52c07e795a9ac2c3` | `D/P1-B6.json` / `255c1df89a96a9bca3bba573e7ef54ee2c9c8fec733cdef48fee9a8dba3e39d7` | accepted exact UNSAT |
| P2-C1 | `d27129d92833993390847048b0f954b5e7c1b66eb4b386b7822f323f0a57d403` | `D/P2-C1.json` / `1192ea014b4b9e60dc4e059837783a8062db7d1dd2df272f4faaa9c5ba76f2a1` | accepted exact UNSAT |
| P2-C2 | `24f1547251cf6c094852384c4dee42455700b57c09e246735ec0e28328a2e43b` | `D/P2-C2.json` / `03273c7be4a8ade0a4cf00d6001794d76db720ab025b55d3f05ca0d2e8401745` | accepted exact UNSAT |
| P2-C3 | `5fc6827fa9cb2856ae1ad14d1aa319f51305296ede72acb7b188060288ae5597` | `D/P2-C3.json` / `acd0763c44f93eff3c804351ce9c421c3e354559c739988a66d70feff43a961d` | accepted exact UNSAT |
| P2-C4 | `32c4d3db7af5da46151238836dfb14f36e782ca87d139c8ae38211a1ab663b94` | `D/P2-C4.json` / `2bbd69e3f7fafe31e35c4dbf9a8023e159d248f09cc18e0135c105a6edc12070` | accepted exact UNSAT |

**Receipt audits and checker.** Parent receipt audits: first-ten `43b09c97…9851`; direct-12 `891e52bd…d262`. Parent drat-trim `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`. The solver is untrusted.

**Control scope (unchanged, not inflated):**
- a tiny UNSAT positive;
- a satisfiable checker rejection;
- two first-unit-flip controls that remained UP-UNSAT and VERIFIED. These count ONLY as measured-input binding controls (F10 LF23).

No invalid-proof rejection suite on that relay is claimed. Proofs were streamed. No proof digest and no retained proof exist.

**The four original inputs not refuted directly** are discharged only through NF + S6, under the amendment (§§5–7):

| Source C | Exact B_C SHA256 | Current mathematical obligation |
|---|---|---|
| P1-B1 | `110ff19e28420494c4f8acbcbec35a29655e30f090fb378ea707f22fe56f6491` | no direct refutation; NF (§5) + S6 (§6) under amendment A7 |
| P1-B2 | `13530c0d40a2bdd4abb245789259f7157323d2514c3066daabe7bf363f9f490e` | no direct refutation; NF (§5) + S6 (§6) under amendment A7 |
| P1-B3 | `721c6f3bf445ab5523642b1af7ed540271ab0ea23bfd79a2ac8c60f49597130b` | no direct refutation; NF (§5) + S6 (§6) under amendment A7 |
| P1-B5 | `92a3d9f659a5c5dc1f3bebbc0a05d5e0cf8818b4c0d307bd6aa9f33a3247ec09` | no direct refutation; NF (§5) + S6 (§6) under amendment A7 |

## 5. Link NF — per-template Boolean normal form (m1, m4, m8, m11)

**Exact accepted statement** (the operative claim is NFV LF9). Fix C ∈ {P1-B1, P1-B2, P1-B3, P1-B5} and B_C = F_one ∧ C (WMAN). Every Boolean model of B_C yields a Boolean model of B_C ∧ M_s for some s ∈ Rep(C), where:
- Rep(P1-B1) = {2};
- Rep(P1-B2) = {2,4};
- Rep(P1-B3) = {2};
- Rep(P1-B5) = {2,3}.

M_s is the 126 negative binary clauses ¬g_s((0,c),(i,0)) ∨ ¬g_s((0,d),(i,0)), for i=2..7 and 1≤c<d≤7.

**Contrapositive, used in §7: for each such C, UNSAT of every S_j with source C implies Boolean UNSAT of B_C.**

**Reading of the statement:**
- It is one-way, and per C with the same 42 units.
- The per-C form is why BOTH S_j for P1-B2 and BOTH S_j for P1-B5 are required.
- The converse (a model of S_j is a model of B_C) is trivial: S_j's clauses contain B_C's (§6). It carries no load.
- r1's "iff" is withdrawn.
- It is a model transformation: primary relabelling under template stabilizers, recomputation of the forced AND/prefix auxiliaries, and an explicit w3. It is not a CNF automorphism.
- It does not claim that each model already satisfies M_s.
- M_s constrains ONLY column 0.

**Status (m1).** **PARENT CORRECTNESS-ACCEPTED as a conditional Boolean lemma.** Authority: `R/moqls8-p1-normalform-parent-verdict-v1.md`, SHA256 `4748f023a504a263ef99400e83df063ecbfcdebe979b77d24a69ff1f301b7826`, at 06:11:00. This postdates r1's 06:00:41 freeze, so r1's "PENDING Claude + parent" is superseded. Supporting evidence:
- Codex `R/moqls8-p1-boolean-normalform-codex-v1.note.md` `030f92a8…4e30`: ACCEPT-WITH-FIXES, 0/0/1 (fixed in r2).
- Claude `R/moqls8-p1-boolean-normalform-claude-v1.note.md`, SHA256 `a1a8eb7d1ad6223c2d12bc39c0ca8936f511645deb560f1e43bfd3a41a563805`: ACCEPT-WITH-FIXES, 0/0/10.
- Parent finite/format check `e075aff8…cbc2`.
- Parent ID, argv, fingerprint and binding checks (NFV LF21–26).

**Accepted text (m11).** NF2 `L/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md` `8ae0ac01…9e8f`, **read with NFV LF28–32** (the MINOR dispositions). NFV LF9 is the operative claim.
- r1 `5c748dd8…faa4` and diff `c6b8bfeb…e2e5` are preserved.
- Claude MINORs 1, 2, 3, 7 and 8 were dispositioned wording-only and are NOT applied to the NF text.
- MINORs 4, 5, 6 and 9 are discharged by recorded evidence. MINOR 10 is handled by the amendment.
- NF2's own labels "UNREVIEWED" and "PENDING" (NF2 LF1, LF7, LF161) are historical self-descriptions. For status only, the verdict supersedes them; the text is unchanged.

**Dependencies (m8, qualified).**
- r1's "primary G1–G5" is corrected to **constants and G2–G5**; no G1 family exists.
- NFV LF9's "uses only G2/G3 support facts" means that no unitary, phase or rank realization is used.
- As a statement about CNF families, that phrase holds only for the local permutation-count lemma (NF2 §1, LF33–78). That lemma uses the G2/G3 consequences (A)–(C) alone.
- The model transformation (NF2 §§2–4, LF80–147) additionally needs invariance under the primary relabelling, or explicit re-extension, of:
  - the constants, G4 and G5;
  - SB2;
  - the kept Q1 P4-ALO with its one-way w3 implications;
  - ROWLEX with inclusive-prefix lexeq;
  - the AND/b3/c4/u5 definitions.
- It also needs the frozen instance to contain no classical-L variables or constraints and no fixg (NF2 LF98–100; argv check NFV LF25).

## 6. Link S6 — six strengthened inputs: BOUND; qualified UNSAT PENDING (m1, m3, m9)

**Generation (unchanged from r1).**
- Generator `L/code/generate_p1_monomial_r2.py` `08b67cef…c352`.
- Freeze `L/review/P1_MONOMIAL_GENERATOR_FREEZE.r2.json` `6234e470…65ae`.
- Planned-hash manifest `L/evidence/P1_MONOMIAL_FORMULA_HASHES.r2.json` `e04557a4…b709`.

These are planned byte identities only, not receipts.

**Composition** (BINDING.json `composition_rule`):
- The header `p cnf 509915 5740268` becomes `p cnf 509915 5740394`.
- The weak body and the 42 unit lines stay unchanged and in place.
- The 126-clause M_s tail is appended after the last unit line. Negative literals are sorted numerically within each binary.
- No new variables, H3, rank clause or whole-square classicality condition is added.

Clause arithmetic: 5740230 − 4 = 5740226; +42 = 5740268; +126 = 5740394, with 126 = 6 rows × C(7,2).

**Binding = BOUND (m1).** Parent `R/moqls8-strengthened-parent-replay-v1/BINDING.json`, SHA256 `5e1116e8311bfe4b2e06554edd0c77fc564574b06c1320334373648171f5f98c` (script `bind_v1.py` `b010baa4…786c`; status MATCH; mismatches []). Each parent-composed input equals the worker r2 hash. Bound hashes in full:

| S_j | Source C | s | Bound S_j SHA256 (parent-composed = worker r2) | Bytes | Source B_C | Binding | Qualified UNSAT | Observed at this freeze (NOT qualifying) |
|---|---|---|---|---|---|---|---|---|
| P1-B1.M2 | P1-B1 | 2 | `09a117b880a4715e068c33b7601b23b424b70218958675ed68b28f053fd050c0` | 137665036 | `110ff19e…6491` | BOUND | PENDING | native verification observed; PROOF_DIGEST_MISSING; not qualifying |
| P1-B2.M2 | P1-B2 | 2 | `3f65ad964ea83c68f78d7a6a90a95820925c70636e610ec0f4e78541531e04b0` | 137665034 | `13530c0d…490e` | BOUND | PENDING | not attempted |
| P1-B2.M4 | P1-B2 | 4 | `61bddbe074e733a632b10fdac214d4bde1032cda4bdfcf563275d5a5f6fb4af0` | 137665034 | `13530c0d…490e` | BOUND | PENDING | not attempted |
| P1-B3.M2 | P1-B3 | 2 | `e4b55555bdeb9ba389cec74983576ee66939fe19210bb593d7bdac0ba392428d` | 137665032 | `721c6f3b…130b` | BOUND | PENDING | UNKNOWN: in-flight disk-floor stop 07:04:14; no refutation |
| P1-B5.M2 | P1-B5 | 2 | `caf1368490f766b1df4be973450fbe8b4dc1867067bfc5a9069f9060528510f4` | 137665031 | `92a3d9f6…ec09` | BOUND | PENDING | not attempted |
| P1-B5.M3 | P1-B5 | 3 | `36d58ad9c4e5bb0e70e163a50a322079458c9cfd2fee9251dec8d1ec363c8e35` | 137665031 | `92a3d9f6…ec09` | BOUND | PENDING | not attempted |

The composition verdict is PENDING (§7).

**Observed native state** comes from the desk RESULT `R/moqls8-strengthened-parent-replay-v1/RESULT.json` (SHA `74e64f07…b7a9`, assembled 07:19:19):
- P1-B1.M2: receipt `ada3f86e…03d2`.
- P1-B3.M2: receipt `c71b0e7d…894f`.

The desk file may later be superseded. This paragraph records only that snapshot, and none of it is a qualifying refutation.

**Tail binding (m9).** The tail literals name the intended primary bits through the same primary map as the WMAN units:
- On map `7b4dd597…b197`, every g_s((0,c),(i,0)) with s=1..5 and c,i=1..7 has ID 1568(s−1)+49c+7i−6 (NFV LF22).
- Claude's SB2 cross-check (Q2 row 1, coordinate 4) decodes to 1765 (NFV LF23).
- The canonical tails rebuilt from the map reproduce the parent fingerprints for s=2..5 (NFV LF24).

Fingerprint artifact: `R/moqls8-p1-normalform-parent-v1/RESULT.json`, SHA256 `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2`. Field `mononomial_clause_checks.<s>.ordered_bytes_sha256` (key spelled as in the file), produced by `check_local_boolean_v1.py` `abfa623a…2531`:

| s | Fingerprint | Used |
|---|---|---|
| 2 | `6fe525a9e6df69193b918d3f0ec29c841d0a66845ee58b3ca0690b9fe2988708` | yes |
| 3 | `e9f44b5f4c9ca4a4de152bcc47385283da7b66d074b10956a0fcdc7440b5ca7c` | yes |
| 4 | `900a6bc37239e6835f4190ccf42dfc4088dfd4a43dcc4aec522d9297da8e4dea` | yes |
| 5 | `233636b1002e5b9f877999d9cce0ab822b44c585edee70a9248f601652554cce` | no |

The 42 units (s=1) and the three tails used (s=2,3,4) therefore decode against the same map as the WMAN units (DISP LF28; §2). Each tail expresses exactly M_s (NF2 LF153–159):
- G3 gives nonemptiness;
- SB2 makes row 1 a singleton;
- the constants handle coordinate 0.

**Full certification predicate for each S_j (m3).** The amendment (NFV LF36–40) retains "the unchanged F4 strict predicate". Its bullet list there is a summary:

- measured complete solver and checker feeds whose hash equals the bound strengthened hash;
- solver rc20 with exact `s UNSATISFIABLE`;
- parent drat-trim rc0 with exact `s VERIFIED` after CR removal only;
- no NOT VERIFIED or TIMEOUT.

The full predicate is DISP LF40. Quoted verbatim:

> For EACH counted worker refutation: solver and checker self-exit, no guard/relay/feed error, solverrc20 with `s UNSATISFIABLE`, checkerrc0 with a raw log line equal to `s VERIFIED` after CR removal only and no `s NOT VERIFIED`/`s TIMEOUT`; both input-feed hashes equal that WMAN case hash; proof-stream SHA and byte count recorded. The inherited status parser also strips whitespace, so the parent must inspect/hash-bind raw logs rather than take its normalized status alone as evidence of exact-line conformance. LRAT-only or proof-free outcomes do not count.

DISP LF41 (controls and final-verdict clause), verbatim:

> After16/16 qualifying refutations, independent parent regeneration and proof replay with intended negative controls and a final full-composition verdict remain mandatory. If any case is SAT/UNKNOWN/unstarted, the full exclusion remains open. No duplicate proof/CNF retention, floor reduction, cap increase or unreviewed H3 transfer is authorized.

**For S_j, these words bind as follows:**
- "both input-feed hashes equal that WMAN case hash" means equality with the bound S_j hash printed above, with each feed length equal to the bound byte count.
- "Solver and checker self-exit, no guard/relay/feed error" and "raw log line … after CR removal only" apply unchanged. Raw logs must be hash-bound and inspected; the normalized parser status is not enough.
- Proof-stream SHA256 and byte count must be recorded from the actually delivered proof stream at run time. A later hash of a different or regenerated stream does not qualify (§8.1).
- LRAT-only and proof-free outcomes do not count.
- Any SAT, UNKNOWN, timeout, guard stop or binding mismatch leaves that S_j, and hence its source template, OPEN.

**Controls for the six replays: OWN controls, not inherited.** They must run on the same frozen relay/checker build that produces the qualifying S6 evidence. The F10 LF23 self-tests are not inherited, for two reasons:
- the S6 desk is a separately versioned pipeline;
- the hashing/counting relay required by §8.1 is new (correction `a4b51119…7b70`).

Minimum classes, as previously exercised by parent desks:
- a tiny known-UNSAT positive passes;
- a satisfiable checker input is rejected (`s NOT VERIFIED`);
- invalid proofs (truncated, empty, wrong-CNF) are rejected, as in the K2 parent replay v2 (A8 parent verdict, verification table);
- a feed-hash mismatch is rejected by the measured-feed comparison;
- the recorded proof SHA256 and byte count agree with an independent hash of a retained small control proof.

Unit-flip inputs that remain UNSAT by unit propagation alone count only as binding controls (r1 LF71; F10 LF23). The exact suite and its adequacy are parent determinations.

## 7. Final implication, antecedents and trust boundary (m2, m4, m5)

**Antecedents.** The conclusion below holds only if ALL of the following hold.
- **A1.** The primary definitions (§1, PRIM LF195–225) and rules #1–#3 (LF287–302), with Lemma 10 (LF342–356) inside A8. A8/W8 as accepted (§2).
- **A2.** U: DISP items 2–3, with their exact conditions and byte bindings (§2).
- **A3.** T16: DISP item 1, within the F3 import range (§3).
- **A4.** D12: each of the twelve direct B_C is exactly refuted under the ORIGINAL contract, including conforming proof-digest evidence (§8.1). DISP LF37–41 continue to govern these twelve.
- **A5.** NF: the accepted per-C lemma (§5).
- **A6.** S6 binding: all six S_j are bound. DONE: BINDING.json `5e1116e8…f98c`.
- **A7.** The contract amendment (NFV LF36–42), as an explicit antecedent.
  - **Scope:** the four templates P1-B1/B2/B3/B5 ONLY.
  - **Superseded wording:** for those four, it supersedes the 16/16 wording of the accepted U text, insofar as that wording demands direct refutation of those four original inputs:
    - DISP LF37 ("All16 cases required");
    - DISP LF41 ("After16/16 qualifying refutations …");
    - REP LF108–110 (items 3–5 of the only permitted final implication);
    - BRIDGE LF93 ("verified UNSAT of ALL16").
  - **Substitution:** A5 plus A8 replace that requirement for those four templates.
  - **Twelve direct leaves:** they stay under the original contract.
  - **Recommended erratum:** read literally, the superseded lines would leave the final step unlicensed. A one-line parent erratum to NFV stating this reach is recommended; it is not performed here.
- **A8.** Qualifying, parent-replayed UNSAT of ALL SIX S_j under the full predicate and own controls of §6. This includes both S_j for P1-B2 and both for P1-B5.
- **A9.** Proof-digest provenance for all 18 counted replays (§8.1).
- **A10.** An independent second encoding with proof-certified evidence for every exhaustive step (§8.2).
- **A11.** A final full-composition parent verdict with hostile assembly reviews (NFV LF42; DISP LF41) that reconciles A1–A10.

**Implication (m4).** Assume A1–A11, and suppose a genuine non-classical set of five MOQLS(8) existed.
1. By A1–A3, it yields a model of B_C for one of the sixteen templates C.
2. If C is one of the twelve direct templates, A4 contradicts this.
3. Otherwise C ∈ {P1-B1, P1-B2, P1-B3, P1-B5}. For that C, the accepted NF lemma (A5) gives: UNSAT of every S_j with source C (A8, with A6 identifying the refuted bytes) implies Boolean UNSAT of B_C. That is a contradiction. A7 licenses this substitution for the original 16/16 requirement.

Hence **every set of five MOQLS(8) would be classical**: an affirmative answer to Problem 16 ONLY at n=8. NF refutes nothing by itself. NF plus the six certificates imply Boolean UNSAT of the four B_C.

**Trust boundary (m5).** The common base is:
- the imported primary definitions and printed Lemma 10;
- the written A8/W8, U and T16 proofs, as accepted by the parent;
- the encoder necessity and canonical-extension arguments, within U's scope;
- the hash-bound encoder/byte/name construction;
- the parent drat-trim `a46c0c71…8e37`. The solver is untrusted.

The leaves then split:
- **Twelve direct leaves:** DRAT certificates of the exact B_C bytes themselves, checked by parent drat-trim (subject to A9).
- **Four P1 leaves:** these rest on two different things:
  - the written NF lemma, reviewed by two model families (Codex and Claude) with parent finite/format and ID checks. It is NOT compiled into DRAT, Lean or an independently checked clause audit (NF2 LF161);
  - DRAT certificates of DIFFERENT formulas — the six S_j (B_C plus 126 clauses) — not of B_C itself.

No Lean or kernel proof is asserted. Model reviews are neither kernel checking nor human peer review.

## 8. Two additional parent obligations (incorporating addendum 8bfd2dee…8d4f)

### 8.1 Proof-digest provenance for all 18 replays
Parent correction `R/moqls8-parent-replay-provenance-correction-v2.md`, SHA256 `a4b511195f64e0f8cfe2f8d0fe7ccc0bac278bec0859a9d3897c8de612b47b70` (06:31:58), withdraws an earlier interpretation: that omitting the proof-stream SHA256 was a mere clarification. That interpretation is in `R/moqls8-parent-replay-predicate-addendum-v1.md` `38451b0a…2d37`, which is preserved. F4 requires the proof SHA256 and byte count (DISP LF40).

**Scope:** all 18 replays counted in §7 — the twelve direct (A4) and the six S_j (A8).

**Existing observations** (the twelve direct receipts and the P1-B1.M2 verification):
- The proof streams went directly to drat-trim and were discarded without a recorded digest. No digest can be recovered or backfilled.
- Status: **PROOF_DIGEST_MISSING / QUALIFICATION_INCOMPLETE**.
- They remain observations of native verification against measured, bound CNFs. They are not SAT results, counterexamples or failed refutations.
- The historical receipts and verdicts stay immutable.

**Closure requires, for each of the 18,** fresh conforming evidence that records the proof-stream SHA256 and byte count of the actually delivered stream. The relay that does this must be separately source-reviewed and controlled. The only alternative is a separately explicit, authorised protocol exception; none is granted here. A later relay cannot supply digests for older, discarded streams. The five S_j not yet verified need the digest at their first qualifying run.

### 8.2 Independent second encoding (GB)
The lane contract `S/phys-1-moqls8-problem16-contract.json`, SHA256 `25a018b0412f4a343f448b581762b6bb22fa604e371e02489f2e7405fbf72acf`, acceptance.positive_answer (LF29), requires: "Computer assistance only with exact or proof-certified computation (DRAT/LRAT checked by an external checker), a written proof that the finite reduction is exhaustive (support rules, lossless symmetry breaking), and two independently written encodings for every exhaustive step."

GA (`gram_a.py` `bf1aada1…d05a`) is one encoding and cannot close this alone. The exhaustive steps here are the twelve direct B_C and the six S_j, which together with NF replace the four P1 B_C.

**Source.** Package `L/review/GB_ONE_P4_SOURCE_PACKAGE.r2.json` `b90b42cc…bdf7`:
- generator `5ca7c0da…e262`;
- untouched GB encoder `L/code/gram_b_r2.py` `4b593e55…eae0`;
- necessity/differences note r2 `b9b4a595…2365`, still UNREVIEWED;
- conventions `50a5bf4a…7b37`;
- freeze `3a2a521b…2d67`.

GB uses its own variable names, P4 only for Q1, SB2/G5 and NO ROWLEX. It carries the same semantic 42 units and 126-clause M_s tails, mapped through GB names.

**Input identity — DONE (identity only).** The parent binding `R/moqls8-gb-parent-binding-v1/GBBINDING.json` (`d917203d…c673`, PASS) and the lane adapter agree on all 22 GB counterparts: SHA256, bytes and headers.
- Lane adapter: frozen code run unchanged at 07:46. Manifest `L/evidence/GB_ONE_P4_MANIFEST.r2.json` `4daf8fcf…680d`.
- Own-hash receipt `9781c877…943f`, x-created before the parent file was read.
- Comparison `L/evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json` `df3fb6e6661f46b5cb9673bfc8750482c69978cf0b64d7ea7224f4a434f0b651`: ALL_22_MATCH.
- Template headers are `p cnf 3803745 17025620`; strengthened headers are `p cnf 3803745 17025746`.
- Base body `f5da0520…f1b9` (350550717 B, 17025578 clauses).

GB counterpart hashes: P0-B1 `b364c1e6…c9fa`; P0-B2 `259bc80b…9b9d`; P0-B3 `ca58afda…dc63`; P0-B4 `77df8b03…9a9a`; P0-B5 `dad7a448…9d10`; P0-B6 `76f4b663…4abf`; P1-B1 `48c1688e…a72f`; P1-B2 `0e62eed6…c192`; P1-B3 `f8fd0a51…d487`; P1-B4 `03271e5a…408b`; P1-B5 `87ec8493…9422`; P1-B6 `10d40a85…9cb2`; P2-C1 `2311bd82…3135`; P2-C2 `9ecc9df4…7326`; P2-C3 `24d93eb5…2f78`; P2-C4 `88fa1587…f977`; P1-B1.M2 `1873f550…3687`; P1-B2.M2 `1aa38ae7…a3f8`; P1-B2.M4 `2544240d…8293`; P1-B3.M2 `47e099af…8871`; P1-B5.M2 `6a423719…7065`; P1-B5.M3 `0ae01935…7c51`;

**Still required for A10:**
- review/acceptance of the GB necessity/differences note;
- proof-certified evidence (DRAT checked by the parent checker) for every GB counterpart under the parent's final interpretation. No GB solve has qualified; a worker timing probe is separate and not qualifying.
- for the six GB strengthened counterparts, a bridge that NF does not supply directly. NF is a lemma about GA's Boolean models. The GB bridge must use a genuine-level reading of NF:
  - the support lemma (A)–(C) holds for genuine configurations;
  - NF's §4 moves are realisable by common row/column permutations with P_σ and by square relabelling (REP LF34–38).

  That reading is [unreviewed] and must be reviewed together with the GB note.

## 9. Precise current conclusion
At this freeze, the final implication is NOT discharged.

**Accepted:**
- U and T16 with their byte bindings;
- the scoped background A8/W8;
- NF as a conditional per-C Boolean lemma;
- S6 input binding;
- GB input identity (identity only);
- the twelve direct native UNSAT observations. These are parent-accepted, but their protocol qualification is incomplete.

**Pending:**
- qualifying refutations of the six S_j;
- proof-digest provenance for all 18 replays;
- GB necessity review, the genuine-level NF reading for GB, and proof-certified GB evidence;
- the recommended amendment erratum;
- the final verdict.

**This is not:**
- an unconditional n=8 exclusion;
- whole-base F_one UNSAT;
- a result for all n;
- a K4/K5 claim from old inputs;
- a novelty, priority or publication claim.

**Non-load-bearing runtime facts:**
- The producer signed-cube pilot is stopped and quarantined.
- UNKNOWN leaves and lifecycle/static/metadata smokes contribute ZERO refutations.
- The old lease 7ff6 has ended.

This note authorises no solve, CNF or ledger amendment.

## Appendix A — findings disposition

| Finding | Repair in r2 |
|---|---|
| Claude m1 (superseded link states) | §5 status, with pins of NFV `4748f023…7826`, Claude NF `a1a8eb7d…3805` and BINDING `5e1116e8…f98c`; §6 table prints the six bound hashes; binding = BOUND, UNSAT = PENDING, composition verdict = PENDING |
| m2 (amendment reach) | §7 A7 (explicit antecedent; superseded lines listed; P1-B1/B2/B3/B5 only; erratum recommended) |
| m3 (incomplete S6 predicate) | §6 (DISP LF40 and LF41 quoted verbatim; feeds bound to BINDING hashes; own controls; UP-unit-flip scope) |
| m4 (implication wording) | §1 step 3; §5 per-C one-way statement, "iff" withdrawn; §7 implication; A7 and A11 added |
| m5 (trust-boundary split) | §7 trust boundary |
| m6 (W8 scope) | §2 W8 bullet |
| m7 (T16 authority and range) | §3 |
| m8 (G1, dependency) | §5 dependencies; "constants and G2–G5" |
| m9 (M-tail fingerprints) | §6 tail binding (artifact, field, four fingerprints, ID formula, 1765) |
| m10 (relabelling, genuine, extraction) | §1 notes |
| m11 (NF text status) | §5 accepted text |
| Codex M1 (registry coverage) | Header sentence; registry r2 adds explicit CNF, encoder and name-table entries |
| Parent: proof-digest provenance | §8.1; A9 |
| Parent: GB second encoding | §8.2; A10 |
