# Ball–Simoens Problem16 at n=8 — frozen ASSEMBLY r1

**Status: CONDITIONAL ASSEMBLY, NOT an n=8 theorem or novelty claim.**

Frozen at 2026-10-18T06:00:41.109079-07:00. This note freezes the link states known at that checkpoint. Later receipts/reviews require a new assembly version, not silent updates.

Path prefixes: `L=/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16`; `R=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`. Every artifact below is fingerprinted in `L/review/N8_ASSEMBLY_LINKS.r1.json`, SHA256 `2b727fde73816970724ff560c8384ed1ce3293caec36c3ce5e5d449686e21798`. Hashing this registry was not a new native/proof replay.

## 1. Exact target and logical shape

The target is **every set of FIVE mutually orthogonal quantum Latin squares of order8 is classical up to the paper’s isotopy**. Each row/column is an ONB; pairwise cellwise tensor products form an ONB. Isotopy allows entry phases, common row/column permutations and separate per-square unitaries. The primary definition is at lines195–225; Problem16 at642 asks whether every(n−3)-MOQLS(n) set,n≠4,is classical. Here ONLY n=8 is in scope.

`L/sources/2607.12933v2.raw.txt` — SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`. **Status: imported primary definitions/question**, not a new theorem.

Write B_C=F_one AND the exact42units of templateC. The assembly is:

1. A hypothetical genuinely non-classical five-set normalises to a model of at least one of sixteen B_C.
2. Twelve B_C are parent-accepted exact UNSAT inputs. Thus only P1-B1/B2/B3/B5 can remain.
3. The new Boolean normal-form proof, IF accepted, maps existence of a model of one of those four to existence of a model of one of six stronger inputs S_j.
4. IF all six exact S_j are independently bound/refuted under the parent certificate predicate, the four B_C close. Combined with(1),(2), no non-classical five-set exists.

**Currently missing:** Claude/parent acceptance of link3, independent parent binding and qualified refutation of all six S_j, and final full-composition disposition. No conclusion in step4 is claimed now.

## 2. Link U — accepted unified reduction, with its exact conditions

**Exact statement:** for ANY genuine non-classical set of5MOQLS(8), standardising row0 and using accepted A8/W8 produces a weight3 witness. After square/common row/column relabelling, its normal form has Q1(1,0) support123, other four supports4/5/6/7, and non-strict Q1 column0 ROWLEX. Canonical Gram/auxiliary values satisfy the exact weak formula F_one. Other four squares may be classical OR non-classical.

**Status: PARENT CORRECTNESS-ACCEPTED as a CONDITIONAL mathematical reduction and exact formula binding**, expressly NOT an exclusion/theorem on its own. Authority: `R/moqls8-unified-parent-disposition-v1.md` — SHA256 `29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb`. Accepted text must be read together: `L/review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md` — SHA256 `c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3`; `L/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md` — SHA256 `e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704`.

Load-bearing background and binding links:

- **W8/A8 ACCEPTED import:** W8 bounds every frame support by3. A8 has the ALL-FIVE/ALL-ENTRIES premise: if every entry of every square has weight≤2 in a row0 standard form, all weights are1 and the set is wholly classical. Contraposition gives some weight3 in a non-classical five-set, NOT a per-individual-square P4 premise. `R/moqls8-k1k2-parent-verdict.md` — SHA256 `919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9`. Its accepted proof sources are `R/moqls8-k1k2-parent-inputs-r2/PROOF_K1_K2.r1.md` — SHA256 `094dab60c7972c956f90c8cf0984c47f79376d0018192457c84adab6e224ff3c` and `R/moqls8-k1k2-parent-inputs-r2/PROOF_K1_K2.r2.md` — SHA256 `d36e646cf0e8faadd5e6131615c6694cbf4187c10abbb6bf54aa17083ab72d86`. A8 imports the primary Lemma10 argument; this assembly does NOT import Egan–Wanless catalogue counts or the later K1/K2 corollaries.
- **Necessary encoder/canonical extension, accepted within U’s scope:** constants/G2–G5, exact AND/singleton and inclusive-prefix auxiliaries, one true Q1 w3 witness and all other w3 flags false. `L/review/K4K5_ENCODING_SOUNDNESS.r3.md` — SHA256 `a83d305013fa920d1ffe361d6d0aeb589f958da477420b2b053a503221858e59` (import only through U’s accepted scope, not a blanket new acceptance of every older K4/K5 assertion).
- **Original encoder/byte/name binding ACCEPTED import:** `R/moqls8-encoder-binding-v1/binding-result.v2.json` — SHA256 `dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112`. It ties encoder `bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a` to original `L/evidence/gram_dev_v1/GA5L_K5_sb2.cnf`, SHA `6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b`,509915vars/5740230clauses. Full-name-table import is `b8423861d03b6e837317c12ef1f2f297301d1bfbbfb7852b93ccec29b85e2522`; the actual primary map used below is `L/evidence/gram_dev_v1/GA5L_K5_sb2.map.json` — SHA256 `7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197`.
- **Exact weakening ACCEPTED binding:** delete ONLY the four row0 P4-ALO clause lines for squares2–5, zero-based indices5735297,5736866,5738435,5740004. KEEP square1 index5733728; retain all one-way w3/G families/SB2/ROWLEX; no weight1/classical-net/L-sort/fixg/other-P4-frame condition is added. Deletion recipe `L/evidence/UNIFIED_ONE_P4_DELETIONS_v1.json` — SHA256 `4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6`; weak recipe `L/evidence/n8_one_p4_templates_v1/BASE_RECIPE.json` — SHA256 `264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18`. Weak formula SHA `374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9`,509915vars/5740226clauses. It is generated/streamed; no nonexistent on-disk weak CNF is asserted.
- **Independent weak/base/table/leaf binding ACCEPTED:** `R/moqls8-one-p4-parent-binding-v1/RESULT.json` — SHA256 `65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0`. Parent traversed all source clauses, four deletions/five ALO domains, mathematical template table,672units/16leaf hashes and16sign-flip binding controls without producer imports. Worker producer code61eda…d400 and inherited worker hash receipts do not substitute for this independent binding.

Conditions are mandatory: genuine QLS/MOQLS axioms, stated row0/witness normal form, exact weak deletion recipe and canonical auxiliary extension. No reduced-K5/non-classicality or P4 requirement is imposed on squares2–5; no old-F/c112 proof is imported.

## 3. Link T16 — accepted sixteen-leaf cover

**Exact statement:** a genuine normalised configuration as in U can be moved, using residual support permutations/square relabelling and common row sorting, to one of16 full Q1-column0 support templates. Its canonical assignment models that B_C. Degree≤3 and the component theorem use the five-square unitary-support hypotheses; they do not assume P4 on the four others.

**Status: property-form T16 ACCEPTED by U**, together with its explicit restricted import/repair scope. Source `L/review/K5_COLUMN0_TEMPLATE_COVER.r1.md` — SHA256 `1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a`; repair `L/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md` — SHA256 `e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704`; supporting independent delta check `R/moqls8-unified-delta-v1/RESULT.json` — SHA256 `d3eedf783e2104c296bc69cb36d7f92c2bd4f4dee38802ff3290b039250cec8b`. The latter reports16orbits from140sorted/43290labelled necessary patterns; it supports, not replaces, the written component proof.

Exact leaf manifest `L/evidence/n8_one_p4_templates_v1/MANIFEST.json` — SHA256 `355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74`. Every B_C has509915vars/5740268clauses: unchanged weak body plus42signed units, all coordinate1..7 bits for Q1 rows2..7 in column0. ALL16 are required, including P0-B6/P1-B6/P2-C4. This is a cover of genuine counterexample images, NOT an assertion that every arbitrary Boolean model of bare F_one lies in one of these16 masks.

## 4. Link D12 — twelve accepted direct leaves

**Exact statement/status:** each of the following exact B_C inputs is **PARENT-ACCEPTED UNSAT**. They are the twelve direct leaves, not the twelve historical unmeasured producer candidates. Aggregate authorities: `R/moqls8-fone-first10-parent-verdict-v1.md` — SHA256 `61130625a144ae8e88e1f3c8cddd22798477808b0673ac5d246d9b8215b983e4` and addendum `R/moqls8-fone-direct12-parent-verdict-v1.md` — SHA256 `515cd9e1908d5f9e7aed262f800e04315ea6145f944ab34cb11d7d98d014d667`. Parent result records: `R/moqls8-fone-parent-replay-v1/RESULT.json` — SHA256 `f63dbeebe2d1728a25520d2af1fa7babab15221e2b01f1e74581b6985979ee0c`; `R/moqls8-fone-parent-replay-v1/RESULT-ADDENDUM-v1.json` — SHA256 `a051418a699fcb6e9070027d26010a4ec018976cf74936083c04d5ee80fe8bab`.

Receipt directory D=`R/moqls8-fone-parent-replay-v1/receipts/`. Formula SHA below is the full DIMACS input hash; each receipt is a separate physical file with the given SHA.

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

Parent receipt audits: `R/moqls8-fone-first10-parent-receipt-audit-v1.json` — SHA256 `43b09c975db7309ef5a5746b658e624d4a8b987a9b3a851c0c1f7469377e9851` and `R/moqls8-fone-direct12-parent-receipt-audit-v1.json` — SHA256 `891e52bdbccc381cfceac47047b963ae1ab48ffc2a4fd6e631b1e6ff959ed262`. The accepted predicate uses ACTUALLY MEASURED complete solver/checker feeds with expected length/hash, solverrc20 and exact `s UNSATISFIABLE`, checkerrc0 and exact `s VERIFIED`, only CR removed, no NOT VERIFIED/TIMEOUT/guard/feed/relay failure. Solver is untrusted; parent drat-trim is `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`. No LRAT-only or proof-free claim is used.

Control scope is not inflated: first-ten verdict records a tiny UNSAT positive and satisfiable checker rejection. Its two first-unit-flip cases were themselves UP-UNSAT and VERIFIED; they count ONLY as measured-input binding controls, not invalid-proof rejection. The last-two audit rehashes its own receipts/logs. This note claims no common mutation suite beyond those saved receipts. Proofs were streamed; acceptance does not imply retained worker proof files.

The four still-open original B_C inputs are:

| Source C | Exact B_C SHA256 | Current mathematical obligation |
|---|---|---|
| P1-B1 | `110ff19e28420494c4f8acbcbec35a29655e30f090fb378ea707f22fe56f6491` | pending closed cover/refutation; proposed link NF below |
| P1-B2 | `13530c0d40a2bdd4abb245789259f7157323d2514c3066daabe7bf363f9f490e` | pending closed cover/refutation; proposed link NF below |
| P1-B3 | `721c6f3bf445ab5523642b1af7ed540271ab0ea23bfd79a2ac8c60f49597130b` | pending closed cover/refutation; proposed link NF below |
| P1-B5 | `92a3d9f659a5c5dc1f3bebbc0a05d5e0cf8818b4c0d307bd6aa9f33a3247ec09` | pending closed cover/refutation; proposed link NF below |

## 5. Link NF — four original Boolean templates to six exact stronger inputs

**Exact statement:** for each fixed source C, `SAT(B_C)` iff at least one named `SAT(B_C AND M_s)` exists, with representatives `{2}` forB1, `{2,4}` forB2, `{2}` forB3, `{2,3}` forB5. This is a Boolean MODEL-EXISTENCE normal form, not a claim each input model already satisfies M_s and not a whole-CNF aux-ID permutation. M_s constrains ONLY column0, not a globally classical square/K4 assumption.

Proof version to accept: `L/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md` — SHA256 `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`. It preserves original `L/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r1.md` — SHA256 `5c748dd8522b0eced47f18e9bebf8129d3923036e4061cae60491d394fa4faa4`; exact minor delta `L/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.diff` — SHA256 `c6b8bfebea8ab669e0869eb542fc2c2330c9cae35570e0333875103b5151e2e5`. Local support proof uses nonempty rows/columns, no singleton overlap and entry-disjointness from G2/G3; distinguished row6/column1 degree≤2 excludes unrestricted fullK33. Residual support stabilizers preserve all42Q1bits/SB2/ROWLEX keys; primary G1–G5 relabel uniformly, with exact AND/u5/w3/inclusive-prefix extension. No phase/unitarity realization is assumed for this Boolean lift.

**Status: PENDING Claude + parent coverage/contract acceptance.** Codex authority `R/moqls8-p1-boolean-normalform-codex-v1.note.md` — SHA256 `030f92a826ab4d85e6d7fd0d9a7e5538986facf897afb6e81f7cb902ad714e30` is ACCEPT-WITH-FIXES ofr1,0FATAL/MAJOR/1MINOR; r2 explicitly lists unrestricted K33 and excludes it by the distinguished-degree bounds. The fact that the repair is written is not represented as a completed Claude/parent acceptance. Parent finite receipt `R/moqls8-p1-normalform-parent-v1/RESULT.json` — SHA256 `e075aff8f56994777bda4d893f07c62f20d0598a56d0cd9a5ab08c440a25cbc2` PASSES all5123×3patterns/classification, actual full42unit ID binding, stabilizer/orbit coverage and126M-clauses/square. It is a finite/format check, NOT full-CNF model verification or a target theorem.

If accepted, NF plus the six exact refutations below closes the four ORIGINAL Boolean B_C obligations; it does not silently change U’s requirement that all16 original leaves close. That proof-composition/coverage acceptance is itself pending.

## 6. Link S6 — six strengthened formula definitions; parent binding/refutations pending

Frozen generator `L/code/generate_p1_monomial_r2.py` — SHA256 `08b67cef53a0851a965be163452842dd7541bb825c5f54817a2f9af7112bc352`; pre-generation freeze `L/review/P1_MONOMIAL_GENERATOR_FREEZE.r2.json` — SHA256 `6234e470b7164587fddb9222cf68d809fc319ecc014961bce7a9d879a66465ae`; generated input-hash manifest `L/evidence/P1_MONOMIAL_FORMULA_HASHES.r2.json` — SHA256 `e04557a4ea83875caa265e9928b488386fe52c2f95306bd6078f7706265eb709`. These are **PLANNED/generated byte identities only**, not solver/checker measured-feed receipts.

Every S_j has509915variables/5740394clauses. Exact stream order: newheader; unchanged F_one body; the original42unit lines; exactly126negative binary clauses fori2..7,1≤c<d≤7, negative literals sorted numerically within each binary. No new variables, H3, rank clauses or whole-square classicality condition. This canonical byte order matches the independent parent M-tail fingerprints; the rejected generatorr1/order mismatch is preserved separately and is not proof evidence. No CNF file or solver run was produced by these generators.

| Formula | Original source C / selected M_s | Exact generated S_j SHA256 | Parent independent input binding | Parent qualified UNSAT |
|---|---|---|---|---|
| P1-B1.M2 | P1-B1 / M2 | `09a117b880a4715e068c33b7601b23b424b70218958675ed68b28f053fd050c0` | pending | pending |
| P1-B2.M2 | P1-B2 / M2 | `3f65ad964ea83c68f78d7a6a90a95820925c70636e610ec0f4e78541531e04b0` | pending | pending |
| P1-B2.M4 | P1-B2 / M4 | `61bddbe074e733a632b10fdac214d4bde1032cda4bdfcf563275d5a5f6fb4af0` | pending | pending |
| P1-B3.M2 | P1-B3 / M2 | `e4b55555bdeb9ba389cec74983576ee66939fe19210bb593d7bdac0ba392428d` | pending | pending |
| P1-B5.M2 | P1-B5 / M2 | `caf1368490f766b1df4be973450fbe8b4dc1867067bfc5a9069f9060528510f4` | pending | pending |
| P1-B5.M3 | P1-B5 / M3 | `36d58ad9c4e5bb0e70e163a50a322079458c9cfd2fee9251dec8d1ec363c8e35` | pending | pending |

A PARENT desk, N8StrengthenedReplay, owns independent regeneration of each six-input byte stream and measured-feed solve/check. This producer lane has no native role on S6. No final parent binding/refutation receipt or disposition was yet supplied at this freeze; consequently no SHA for a nonexistent acceptance record is invented. The manifest above is the exact file/SHA for the PENDING input link. Any SAT/UNKNOWN, unmatched input, incomplete feed, failed control or missing parent acceptance leaves the corresponding obligation OPEN.

## 7. Final implication and precise current conclusion

If U/T16 and their exact byte bindings remain valid, D12 holds, NF receives the remaining independent/parent acceptance, and ALL SIX independently regenerated S_j receive qualified parent measured-feed UNSAT/proof-check receipts, then NF refutes the remaining four B_C. All sixteen possible genuine counterexample images are then refuted. By contradiction, **every set of5MOQLS(8) is classical**, giving an affirmative answer to Ball–Simoens Problem16 ONLY atn=8.

**At this freeze that final implication is NOT yet discharged.** Accepted facts are the conditional unified reduction/cover/binding and twelve exact direct refutations, plus the explicitly scoped background A8/W8. NF has the stated reviews/checks but outstanding acceptance; S6 input binding and native refutations are pending. Thus this is not an unconditional n8 exclusion, not whole-base F_one UNSAT, not a solution for alln, not a K4/K5 claim from old stronger inputs, and not a novelty/priority/publication claim.

No Lean/kernel proof is asserted. The trust boundary remains the imported paper definitions/accepted mathematical arguments, the hash-bound encoder/byte construction and the parent native DRAT checker/certification predicates. Model reviews are not kernel checking or human peer review.

Non-load-bearing runtime facts: the producer signed-cube pilot is stopped/quarantined; UNKNOWN leaves and lifecycle/static/metadata smokes contribute ZERO refutations to this assembly. Producer12counts are never relabelled as parent proofs. No active native process of this lane is planned; oldlease7ff6 is released. No new solve or CNF/ledger amendment is authorised by this note.
