# ROOT-COVER-HOLDS

**The frozen v003 ledger is an exhaustive, disjoint 128-root partition with a consistent declared provenance mapping. It is not a K5 exclusion certificate.**

**Coverage/provenance defects found:** FATAL: none; MAJOR: none; MINOR: none. Outstanding exclusion obligations and audit limits are listed below.

All lane-relative references below use:

`L = /Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/`

## 1. Root coverage

I inspected all 128 records in each of `LEDGER.v001.json`, `LEDGER.v002.json`, and `LEDGER.v003.json`, not merely the worker validator’s result.

In all three versions:

- IDs are exactly `c000` through `c127`, each occurring once.
- Indices are exactly `0..127`, and each ID matches its index.
- Every record has `depth = 1`, `ancestor = null`, and seven literals.
- For  
  `V1 = [57,106,155,204,253,302,351]`,  
  literal position `k`, counting from zero, is positive precisely when bit `k` of the root index is one.
- Consequently, the literal vectors enumerate every sign assignment of these seven distinct variables exactly once. No reversed-orientation qualification is needed.
- There are no `REFINED` records, depth-two records, non-null ancestors, or child IDs in these three ledgers. All 128 roots remain terminal.

Thus the disjunction of the 128 root cubes is a tautology, and distinct roots are mutually inconsistent. Fixed variables or root-level UNSAT results do not change that combinatorial coverage.

The declared chain agrees across the three ledgers, `code/k5_cover.py:30–39`, and `README.md:204–215`:

| List | Variables |
|---|---|
| V1 | 57, 106, 155, 204, 253, 302, 351 |
| V2 | 64, 113, 162, 211, 260, 309, 358 |
| V3 | 71, 120, 169, 218, 267, 316, 365 |
| V4 | 78, 127, 176, 225, 274, 323, 372 |
| V5 | 85, 134, 183, 232, 281, 330, 379 |
| V6 | 92, 141, 190, 239, 288, 337, 386 |
| V7 | 1625, 1674, 1723, 1772, 1821, 1870, 1919 |
| V8 | 1632, 1681, 1730, 1779, 1828, 1877, 1926 |

V2–V8 are declarations for possible refinements; **no such refinement is present in v003**.

**Source references:** `L/review/K4K5_ENCODING_SOUNDNESS.r3.md:9–14,43–46,125–130`; `L/README.md:179–215`; each ledger’s header/chain at lines `1–81`.

The source, ledger headers, manifest, and all strict receipts agree on base SHA-256:

`6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b`

They declare `509915` variables and `5740230` base clauses. Every strict root receipt declares `5740237` clauses, consistent with adding seven units.

## 2. Historical chain and exact categories

| Version | UNSTARTED | Worker-strict CERTIFIED | UNKNOWN | REFINED |
|---|---:|---:|---:|---:|
| v001 | 128 | 0 | 0 | 0 |
| v002 | 122 | 0 | 6 | 0 |
| v003 | 0 | 122 | 6 | 0 |

The only v001→v002 record changes are the six original non-UNSAT roots becoming `UNKNOWN`, with `worker-root` evidence. The other 122 roots remain `UNSTARTED`; old positive records were **not** promoted to certification.

The only v002→v003 record changes are those 122 `UNSTARTED` roots becoming `CERTIFIED`, each referencing `strict_L1/RESULTS.jsonl`. The six UNKNOWN records, their literals, and their evidence references remain unchanged.

Declared predecessor links are:

- v001: `prev_sha256 = null`.
- v002: `prev_sha256 = 5a38223b0058786db809dd0c114db3f74d19ab0792b4364f06265e221844378b`.
- v003: `prev_sha256 = 1421933455c998031c4df3834920a07f834252933c530f18d1eb333d01829371`.

All three declare writer SHA-256:

`9326589645ce7d871b4b1595d3c465577d1aee9f27143d43a2b8000c14d022c7`

**References:**  
`L/evidence/k5_split_v1/ledger/LEDGER.v001.json:2259–2267`;  
`…/LEDGER.v002.json:2283–2297`;  
`…/LEDGER.v003.json:2771–2785`;  
`L/README.md:233–257`; `L/code/k5_cover.py:241–297`.

The parent encoder-binding receipt independently declares the same v002 hash. The supplied v003 pin and the retained manifest’s `ledger_sha256` agree on:

`b9b3fc67fe5abdf6be197b7cb642226bc1c5f344348edb068b6388c02bc8b14b`

These are **declared/pinned hash comparisons, not fresh digest computations by this audit**.

## 3. Strict receipts and retained-proof provenance

I inspected all **122 strict receipts** and all **122 retained-manifest rows**.

For every resolved root:

- Receipt ID, index, depth, ancestor, and complete literals match its ledger root.
- The receipt binds the expected base and v002 input ledger.
- The leaf-CNF SHA, proof-stream SHA, retained compressed-proof SHA/path, and byte counts agree between the strict receipt, retained manifest, and original worker receipt where applicable.
- The manifest’s strict-receipt file and declared line hash match the v003 evidence reference.
- The manifest’s original worker-receipt file and declared line hash match `ROOT_RECLASSIFY_v1.json`.
- Declared decompressed proof SHA/bytes equal declared strict-stream SHA/bytes.
- The companion `.sha256` list agrees with the manifest’s compressed-proof paths and digests.

The retained mapping is exactly:

- `pilot/cubeNNN.drat.zst` for **c001, c003, c008, c009, c014, c024**;
- `all/cubeNNN.drat.zst` for the remaining **116 resolved roots**.

There is **no missing, stale, duplicated, or mismatched declared mapping** among these 122 roots. The six unresolved roots are deliberately absent from this resolved-proof manifest.

**References:**  
`L/evidence/k5_split_v1/strict_L1/RESULTS.jsonl`, records 1–122;  
`L/evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.json`, header and all `rows`;  
`L/evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.sha256`;  
`L/evidence/k5_split_v1/pilot/RESULTS.jsonl:1–6`;  
`L/evidence/k5_split_v1/all/RESULTS.jsonl`;  
`L/evidence/k5_split_v1/ROOT_RECLASSIFY_v1.json`.

The manifest pin supplied by the parent is:

`65f6e0dd47c582b108906aa808e3d2453ec45ac3b8bbfa19c01e586e989c3b5e`

## 4. Explicit unresolved frontier

Every row below is still **UNKNOWN, worker-root evidence only**, with no strict receipt or refinement in v003.

| Root | Complete literal vector | v003 record starts | Original receipt |
|---|---|---:|---|
| c016 | −57, −106, −155, −204, +253, −302, −351 | line 419 | `all/RESULTS.jsonl:12` |
| c032 | −57, −106, −155, −204, −253, +302, −351 | line 755 | `all/RESULTS.jsonl:27` |
| c048 | −57, −106, −155, −204, +253, +302, −351 | line 1091 | `all/RESULTS.jsonl:43` |
| c064 | −57, −106, −155, −204, −253, −302, +351 | line 1427 | `all/RESULTS.jsonl:59` |
| c080 | −57, −106, −155, −204, +253, −302, +351 | line 1763 | `all/RESULTS.jsonl:75` |
| c096 | −57, −106, −155, −204, −253, +302, +351 | line 2099 | `all/RESULTS.jsonl:91` |

Their original receipts explicitly say `solver_status = "UNKNOWN"` and `verified = false`, after approximately 900 seconds. Their partial proof-file hashes are **not UNSAT certificates**.

## 5. Certification predicate and consuming-side handling

The current predicate is not merely the receipt’s `verified` or `strict_ok` boolean:

- `k5_cover.strict_ok`, lines `58–64`, requires all designated fields, self-exit, no RSS guard trip, solver return code 20 with `s UNSATISFIABLE`, checker return code 0 with exact `s VERIFIED`, absence of `s NOT VERIFIED`, and empty feed/relay errors.
- `k5_resplit.py:141–145` strips carriage returns/whitespace from checker status lines before applying that conjunction.
- `k5_leafrun.py:155–166` builds the identity-bound receipt and derives its `strict_ok`.
- The **consumer**, `k5_cover.py:267–297`, explicitly dispatches `worker-root` versus `strict`: old UNSAT records are ignored for certification; strict records become CERTIFIED only through `strict_ok`, otherwise UNKNOWN.
- `k5_cover.py:119–128,174–197` checks receipt identity and disallows worker-root certification.
- `complete` requires every terminal leaf to be CERTIFIED (`k5_cover.py:198–205`).

All 122 inspected strict receipts contain the required passing field values. With six UNKNOWN terminal roots, the declared completion predicate is nevertheless **false**.

The old records independently lack the recorded solver/compression/decompression/feed fields required by their reclassification predicate; treating them as worker-only evidence is justified, not just a validator assertion.

## Outstanding obligations and limits

- **MAJOR for any whole-K5 exclusion claim:** the six UNKNOWN roots remain unresolved.
- **MAJOR for parent proof acceptance:** none of the 122 worker-strict certificates is promoted to parent acceptance by this report. Independent hash-bound DRAT replay remains a separate obligation.
- **Cryptographic audit limit:** I compared declared hashes and mappings but did not recompute file/receipt-line hashes, regenerate CNFs, read/decompress proof payloads, or execute a checker. In particular, the v001 digest is observed as v002’s predecessor declaration, not freshly established here.
- This conclusion concerns **v001–v003 only**, not any later refinement ledger.
- The README’s dated addendum permits new depth-two/K4 proofs to be non-retained; that is not a missing-retention defect in this root audit (`README.md:284–289`).

**Overall correctness:** correct for the frozen root partition and declared provenance consistency. **Confidence:** 0.98.

**No K4 or K5 exclusion is established. No leaf-proof replay was performed by this audit.**
