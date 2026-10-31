# f257 declaration-bound streaming checker: implementation and bounded evidence

Observed native clock before this report: **2026-10-29T15:37:17-0700 PDT**.

## Disposition and boundary

`checker-v4.py` is a **successor to f236 v2 and f252 v3, not a newly independent checker**. It preserves the existing identity, applicability, plane-set, color, and streaming archive/category interfaces, and adds the separately pinned R382 diagnostic. It binds the frozen declaration's 22 descriptor families and their declared row formulas, transports, relations, weight rules and applicability guards. Unrecognized descriptors and unsupported scope fields are not inferred by matching vectors. The archive implementation hashes each declared member and compares the actual plane/case/class sets, not just counts. It remains a prospective program: the full real archive was **not** executed and remains **NO GO**.

The top-level theorem/complete-certificate verdict is **UNKNOWN: source-projection equality and actual-law applicability are not proved**. A checked expanded identity or a finite expanded-record coverage comparison is **not** a check that an original source projects to that record. The synthetic archive deliberately demonstrates this boundary: its pinned original-source JSON contains no certificate at all, yet the separate expanded 68-row identity and synthetic one-plane set are conditionally checkable. No theorem, original-source projection, independent model-family review, formal/kernel verification, scientific adoption, or novelty clearance follows. The historic f236 UNKNOWN and all holds remain unchanged. All checks here are same-harness, not an independent reviewer or model family.

## Input verification and actual display coverage

The full manifest was SHA-256 checked **before** reading it: `2db2c57022d0039b323046a855cff91ec84fa99278aded14358e25532329fd93` (10,271 bytes, 150 LF). At observed native clock 2026-10-29T15:29:45-0700 PDT, every declared input below matched its manifest SHA-256, bytes and LF count before any input body was displayed. The final LF was additionally checked later by the executed checker. The whole ZIP also matched 67,393,983 bytes and SHA-256 `3bde5418e776a88b6a8f9c3e7a147a016b2b09272908eac226e1f3b33ced3040`; this is a byte-integrity check, not a scientific archive replay.

All **3,345 declared LF lines** were subsequently displayed in manifest order in raw source windows of at most 15 lines each: all four mandatory errata first, then source entry 05 and sources 06–15, declaration, f236 v2 and f252 v3. The first combined display of sources 09–11 truncated some long displayed lines: after that combined read, the three sources were redisplayed in order from raw windows, with long lines split for display, before any mathematical analysis. Similarly source 08's long final line was redisplayed fully before source 09. Thus the initial display did not strictly finish every visible character of 09 before first displaying 10–11; this is a display-order deviation, not an omitted body, and no analysis was performed before the complete redisplay. The entire manifest itself was displayed in ten raw windows of at most 15 lines.

Full input paths and roles are in the pinned manifest; the following are its corresponding observed whole-file metadata in the same order:

| # | Input basename | bytes | LF | SHA-256 |
|---:|---|---:|---:|---|
| 01 | `01-frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` | 2024 | 13 | `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` |
| 02 | `02-frontier-20261028-mixed-plane-symmetry-erratum-v1.md` | 980 | 5 | `cdf6e55ffcfa8163007bf01b173a5a4f1103e6d9b7a70b40c0eacd288bdd2e04` |
| 03 | `03-frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` | 2873 | 9 | `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` |
| 04 | `04-frontier-20261029-primal-checker-subset-coverage-erratum-v1.json` | 1461 | 20 | `7194de8030505ac4ee5c13eccd4f6661988f2be50255d33623a5060ff24a2439` |
| 05 | `05-0005-prospective-review-entry.json` | 8520 | 213 | `c9505f3094131c2be0071b3fee0477f77ce1993c5edfa9af9a62211b8fd4ac2b` |
| 06 | `06-frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` | 4568 | 62 | `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` |
| 07 | `07-frontier-20261028-fourfactor-plane-complete-theorem-v1.md` | 4606 | 28 | `7148eb8fa7ef068743d927454c779290b0f3b4238940c7f4226b50bcb707cde5` |
| 08 | `08-frontier-20261028-fourfactor-plane-color-theorem-v1.md` | 3660 | 25 | `09cb78a5bcd1d811f45d087dad567a49ce4f9f9ca898a0fcde3ef96efa0bb4ca` |
| 09 | `09-frontier-20261028-fourfactor-visibility-family-theorem-v1.md` | 4044 | 20 | `ad7ee5d82f7a2ca20a21bc35f950bf1038fe660258dcbe41619bb67834cc410c` |
| 10 | `10-frontier-20261028-visibility-lattice-theorem-v1.md` | 5047 | 41 | `4180f4e072d3e3e7108c66d90aeadebd169fee6b46dcf64e72b37ab10a357b50` |
| 11 | `11-frontier-20261028-mixed-visibility-theorem-v1.md` | 3470 | 25 | `5c6f885b3c9ca20b6216304fe6449e8011e9c7de27eaf086becd887e3e0bdc74` |
| 12 | `12-frontier-20261029-single-functional-local-decoder-lemma-v1.md` | 3406 | 31 | `77679e92b2927373e288cd5c91c647d43f606136273079bda649a89435984c61` |
| 13 | `13-frontier-20261028-triangle-code-global-obstruction-v1.md` | 3658 | 42 | `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4` |
| 14 | `14-frontier-20261028-syndrome-cover-entropy-gate-v1.md` | 3165 | 25 | `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` |
| 15 | `15-frontier-20261029-all-affine-syndrome-plane-entropy-v1.md` | 13348 | 149 | `9c6b11ca444122cf427a8e46f0a3cef0139f33b0615283322631c9c597c06cbd` |
| 16 | `frontier-20261029-archive-row-semantics-declaration-v1.json` | 27364 | 685 | `c67ecd5bce3ef5cab01a0e9949f56a5f801d80e17209864b7b85ea51b16eea4d` |
| 17 | `reviewer-checker-v2.py` | 60479 | 1138 | `ce407f9780f95559f801940594d2d71e1f969a1e6bceb9c13c41535f9bf0b840` |
| 18 | `checker-v3.py` | 42733 | 814 | `62ee41d7041b7c9630947e650536b32c4cb20a7b862cadbffa821460ff0b8b79` |

No held, withdrawn, f161/f162 or producer code/PASS was used as a premise. Mention of an excluded item in the declared errata/entry is not its use. No external model/API, Git, deletion, publication or infrastructure mutation was used.

## Implementation and pins

* `checker-v4.py` SHA-256 **`43e44f78a012573674d31b0d03696c282f7378f5e192c58c19099451bab86020`**. It hard-binds the f257 manifest, declaration, both predecessors, source bytes/LF, archive, and R382 record. Archive mode checks the packet manifest, every declared member's uncompressed SHA/size, and the actual sets; scientific source projection remains unproved. Time and signal interruption yield UNKNOWN, and output creation is exclusive.
* `reviewer-controls.py` SHA-256 `71211f360fee33615e01445926a56da96a76ce9b7197871e3b38ea3cfcda3cdf`; `reviewer-controls-result.json` SHA-256 `741f1f61de5f31c2098d7ec85611bdca3ffcef002097b0e2dfa8308006757c29`.
* `reviewer-mutations.py` SHA-256 `a45754ffb64222bed8d3dc297c0e136011a6eaae8bc5d7dc4fcb4750ed205eac`; `reviewer-mutations-result.json` SHA-256 `c5786ac685186fbd643c019ddf99b74973998c20b3b33f38b26c0c94a5d3fde8`.
* The real-record receipt `reviewer-r382-result.json` SHA-256 **`5352eeb18ec63fd004e8947d385ca531a38651bce25a593549bd4e70a7aac31b`** identifies the same v4 code and the full source pins. The frozen input files and both predecessors remain unchanged.

## Bounded synthetic and mutation evidence

From this directory, the exact commands were:

```text
/usr/bin/env python3 -B reviewer-controls.py
/usr/bin/env python3 -B reviewer-mutations.py
```

Both exited **0**. Native control start/end were `2026-10-29T15:35:29-0700 PDT` / `2026-10-29T15:35:29-0700 PDT`; mutation start/end were `2026-10-29T15:36:53-0700 PDT` / `2026-10-29T15:36:53-0700 PDT`. Each script has a 115 s cooperative/signal limit; both finished within the displayed seconds. The receipts contain exact subprocess argv, output hashes, source/input hashes, exit codes, and per-control expected reasons.

The controls compared **22/22** declared row-family formulas to synthetic independently specified expected vectors, and checked a synthetic 68-row, 511-coordinate proper-subgraph identity with a genuinely constructed 3-color decomposition. Positive CLI checks exited 0 for `identity`, `applicability`, `planes` and `color`; all receipts preserve the UNKNOWN theorem boundary. An in-process synthetic streaming archive check verified one noncover category, one certificate and one actual direction plane; its ZIP SHA-256 is `af9696ce8509c8421dd5ba4d5d094eb578bc510ae3aefab5fd50f54850d73d67`. This does not exercise the real archive or the other four real categories.

The **33** input/negative controls record their intended reasons, including changed declaration/hash, unknown/alias descriptor, arity, CMI/pair order, gate selector, singleton/local/visibility and selected-factor guards, duplicate or floating JSON, noncanonical rational, missing file, row/archive cap, interrupt, mismatched relation/sign/inner weight/image/target/action, missing/member hash, and same-count wrong plane set. **15/15** one-site in-memory code mutants were detected with recorded baseline and mutant outcomes. In particular, the sign-guard mutant was detected by its changed reason but still rejected later at `COEFFICIENT_IDENTITY_MISMATCH`; it is not represented as an unsafe acceptance. This is targeted evidence, not an exhaustive mutation or robustness proof.

## One authorized real-record diagnostic

Exact command (the surrounding shell recorded the actual native clocks and exit):

```text
/usr/bin/env python3 -B checker-v4.py r382 --time-limit-ms 110000 --max-rows 5000 --output reviewer-r382-result.json
```

Observed native start `2026-10-29T15:35:36-0700 PDT`, end `2026-10-29T15:35:36-0700 PDT`, process exit **0**, internal elapsed **84 ms**. The archive hash was checked before and after this diagnostic; the selected JSONL member was `coefficients/residual-recovered3.jsonl`, zero-based record index 1, R382 SHA-256 `48118dc6a138998cb509675f7ffd497aa131d5c00b106950427f164c45f50d29`, 137,939 bytes. The declaration-bound expanded record passed the conditional identity check for 1,104 rows, one action, 5,119 possible coordinates, including the pinned `[gate,1]` locator. The receipt says `R382_IDENTITY_CONDITIONAL` and the theorem verdict remains UNKNOWN.

Access disclosure: sequential ZIP/JSONL decoding to index 1 read and discarded the preceding framed record line; it was not parsed, displayed, retained, or used as a premise. The program checked the preceding line ends in LF and is at most **8 MiB**; it did not persist that line's exact byte count, so that count is **unrecorded** rather than estimated. The only interpreted real member record was the pinned R382 line. The member was not read to its end and its separate uncompressed member hash was not asserted in this diagnostic; whole-archive SHA and exact record SHA were checked. No bulk archive replay or other real-record interpretation occurred.

Separately, Main reported parent-kernel metadata from an earlier bounded gate-schema inspection of the same member: the retained preceding line was **43,967 bytes**, SHA-256 `f929220c9f9e43d4c7a4fcb78b82b5b69762e0e5572fc66157df54dc75a32437`, observed at 14:35:31. This is parent-observed framing metadata, not a count captured by this checker run; it was not used as a scientific premise, and no member reread was performed to recover it.

## Remaining limits

This is not a full scientific replay, source-projection proof, full-category test, verification of all 748 records, proof of written entropy/transport premises for actual laws, or an unrestricted guessing-number result. Input and implementation mutation tests do not prove coverage for unexecuted modes or future inputs. The archive interface may encounter unreviewed real-data schema or caps and must then fail closed; it has not been authorized or exercised on the real packet. The exact skipped-line byte count was not recorded. Real full archive execution remains **NO GO**.
