# Independent finite checks: gcDCQS(18^4:2) and mcDSQS(74)

Recorded: 2026-10-17T19:21:38.740409-07:00. This report checks explicit finite designs, not §4(3), its gate, a consequence bridge, or novelty.

## 1. gcDCQS(18^4:2): PASS

The exclusively pinned 715,330-byte input matches SHA-256
`1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e`. The new standard-library checker is definition-first, imports/executes no claimant checker, and assumes no symmetry.
Both `python3 -B` and `python3 -O -B` pass. All noncomment records are consumed by the strict Format S grammar.

| Condition | Result | Exact observations |
|---|---|---|
| (a) Points, groups, stem, blocks | PASS | X=0..73; stem {72,73}; four disjoint 18-point groups partition X\S; 15,066 distinct 4-subsets. |
| (b) CQS coverage | PASS | Exact set equality with all 60,264 allowed triples; multiplicity one; zero missing, forbidden or multiply covered triples. No block contains a forbidden triple (stronger than only excluding a whole block inside S∪G). |
| (c) Derived incomplete STS | PASS, all 72 group points | STS(73,19), with the declared hole; 819 triples; exact allowed-pair universe of 2,457 pairs, each once; 513 hole-meeting and 306 hole-avoiding triples. |
| (c) Good colouring | PASS, all 72 group points | Exactly 37 nonempty PPCs; triples pairwise disjoint inside each class; exact partition of derived triples; exactly 10 classes avoid the hole. |
| (d) Stem derived GDD | PASS, both stem points | 648 transverse triples at each point; exact universe of 1,944 cross-group pairs, each once; type 18^4. |
| (d) Kirkman frame | PASS, both stem points | 36 classes, each 18 disjoint triples covering exactly X\(S∪G_k); 9 classes omit each group; exact partition of the derived triples. |
| (e) Worker consistency data | MATCH | At every group point: `24^24 23^3 18^5 17^4 16^1`, 37 classes and 819 triples; both stem frames have 36 classes. The profile is reported, not used as a symmetry assumption. |

The frame group count follows directly from the definition: 648/18=36 classes, each point has degree 27, so 36−27=9 classes omit its group. Source: LF 237–240, 281–288.

### Retained gcDCQS controls

Each of the following **13 distinct fixtures** is rejected for the exact intended category under **both** interpreter modes (26 mutant executions). A wrong-expected-SHA argument is also rejected in both modes.

| Fixture | Intended category | `-B` / `-O -B` |
|---|---|---|
| swap-block-points | `b.coverage` | Rejected / rejected |
| delete-block | `b.coverage` | Rejected / rejected |
| duplicate-block | `format.duplicate_block` | Rejected / rejected |
| colour-class-collision | `c.partial_parallel` | Rejected / rejected |
| holefree-class-now-meets-hole | `c.holefree_count` | Rejected / rejected |
| break-stem-frame-class | `d.frame_parallel` | Rejected / rejected |
| corrupt-group-declaration | `a.group_partition` | Rejected / rejected |
| out-of-range-label | `range.point` | Rejected / rejected |
| unknown-line | `format.unknown_line` | Rejected / rejected |
| malformed-block-record | `format.record` | Rejected / rejected |
| duplicate-point-section | `format.duplicate_section` | Rejected / rejected |
| repeated-point-in-block | `format.distinct_points` | Rejected / rejected |
| out-of-order-class | `format.class_order` | Rejected / rejected |

The hole-count control is isolated: move derived triple {9,63,72} at x=0 from class 10 to class 0. All 37 classes remain nonempty PPCs and still partition all 819 triples; the number avoiding the hole becomes **9**, producing `c.holefree_count` rather than a collision rejection. The stem-frame control preserves the total triple partition but leaves its first class with 17 triples and uncovered points {9,18,27}.

## 2. mcDSQS(74): original format FAIL; mathematical record projection PASS

The exclusively pinned **original** matches SHA-256
`eaff77fc63cc408756f72b6f6213eb7449a13e1efc5ba0c40401fc51d4f216c3` (767,743 bytes). The requested existing checker, unchanged at SHA-256
`ca74181eb7524c23aad002b0d913c74a03284ae96e97684aad5487ac83d78630`, rejects it in both modes as **`CertificateError: non-ASCII certificate`**. Its second full-line `#` comment contains U+222A (`∪`, byte offsets 303–305, zero-based). The checker decodes the entire file as ASCII before removing comments. No mathematical check is reached in those original-input executions.

To finish the reachable mathematical checks without modifying the input or checker, a **separate** comment-free projection was retained:
`mcdsqs74/input/mcdsqs74_c21.comment-free.txt`, SHA-256
`f5808eee152d5e6e02fb0a6efc94573b6716de403a44edfb49a0d9e31fa37a6f` (767,434 bytes).
`mcdsqs74/comment-projection-binding.json` records the exact byte transformation and equality of every noncomment record. This is **not** a byte-exact original-input PASS.

The same unchanged parent checker passes the projection under both modes:

- **SQS(74): PASS** — 16,206 distinct 4-subsets; exact equality with all 64,824 triples, every one covered once.
- **Derived STS(73): PASS at all 74 points** — 876 triples at every point (the STS pair property follows from the checked SQS triple property).
- **Minimum colouring: PASS at all 74 points** — exactly 37 nonempty PPCs, disjoint inside classes and exactly partitioning each derived triple set. Class-size profiles: `24^29 23^5 22^2 21^1` at 72 points, `24^29 23^4 22^4` at 2 points.

The exact definition is at **source LF 127–130**, not LF 205–292:

> An SQS(v) with minimum colorable derived designs, abbreviated to mcDSQS(v), refers to an SQS(v) whose derived design at every point is minimum colorable.

LF 110–125 gives χ′(73)=(73+1)/2=37. Independently, the counting lower bound used by the unchanged checker is `ceil(876/24)=37`; the degree bound 36 alone is insufficient, since `36×24=864<876`.

### Retained mcDSQS controls

These **8 distinct fixtures** are based on the explicitly bound comment-free records, not on the raw file that already fails encoding. Both interpreter modes reject every fixture for its listed exact reason (16 mutant executions). Wrong expected SHA and wrong expected order are also rejected in both modes.

| Fixture | Intended category | Exact rejection reason, both modes |
|---|---|---|
| swap-block-points | `sqs.triple_universe` | `some 3-subset is uncovered` |
| delete-block | `blocks.length_boundary` | `invalid block syntax` |
| duplicate-block | `blocks.distinct` | `duplicate block` |
| colour-class-collision | `colour.disjoint` | `colour class is not a partial parallel class` |
| colour-beyond-37 | `colour.index_order` | `missing or out-of-order CLASS 36 at point 0` |
| colours-header-38 | `colours.r_equals_lower_bound` | `COLOURS is not the counting lower bound ceil(D/M)` |
| out-of-range-label | `range.point` | `block point outside range` |
| repeated-point-in-block | `format.distinct_points` | `repeated point in block` |

**Deletion limitation:** the unchanged checker's fixed-length block parser encounters `POINT 0` in its final expected block slot after a block is deleted. Thus that fixture tests the structural block-list boundary (`invalid block syntax`), not a separately reached uncovered-triple check. The block-swap fixture does reach and reject the triple-universe condition.

### Bridge inputs: hashes only, builder NOT executed

- `code/build_mcdsqs74.py`: `56ac950070a117f4a73acbe1bd9752125871e73a72afc342bb05f83e132d3217`.
- `sources/sxk/sxk_prop3_transcription.json`: `3610b32c75738348751c4f58dd9243358e66c2b72d2a15d80bf91e0f49a0d057`.

## 3. Resources, receipts, and limits

- **54 sequential checker executions:** 30 gcDCQS, 2 rejected original mcDSQS, and 22 mcDSQS projection/control executions. No timeout, signal, or builder execution occurred.
- Checker-suite wall time including per-run resource sampling: **34.551 s** (gcDCQS 21.544 s; mcDSQS 13.008 s). Slowest individual child: 0.657 s.
- Peak child RSS: **74,743,808 bytes (71.28 MiB)**. Largest sampled external math-1 RSS: 1,460,699,136 bytes. Lane sampling found at most 3 external busy processes before a launch; one owned checker at a time keeps the sampled busy total ≤4. The lane owner reserved one checker slot.
- `result.json` contains separate candidate results, exact counts, every outcome, input/checker/fixture hashes, timing/RSS, and deviations. Full pointwise counts and stdout/time/resource samples remain in `runs/` and `mcdsqs74/*-runs/`; fixture manifests identify every retained mutant.
- Primary source SHA-256: `df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`. LF numbering uses `split('\n')`; excerpts, frozen contract entry, original paths, and observed bridge hashes are in `provenance.json`.
- Deviations are limited to the original mcDSQS encoding failure, its explicitly bound comment-only projection, the fixed-length parser's block-deletion rejection boundary, and correction of the mcDSQS definition's source line range. **No mathematical deviation in the gcDCQS check.**
- No seed replay, symmetry audit, construction-bridge proof, gate decision, §4(3) conclusion, or priority/novelty determination is claimed here. All newly written files are inside this exclusive review directory; source/lane artifacts remain untouched.
