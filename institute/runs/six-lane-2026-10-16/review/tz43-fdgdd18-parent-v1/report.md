# tz43-fdgdd18 parent verification desk: FDGDD(3,4,5{18}) candidate

Desk `Tz43FdgddParentCheck`, dir `review/tz43-fdgdd18-parent-v1/`. Report written 2026-10-17 22:57:45 PDT (host clock).
Scope: correctness of the finite certificate only. This report gives **no gate, bridge, consequence, novelty or
significance verdict**. Machine-readable record: `result.json`.

## 1. Candidate and pinned inputs

| object | sha256 | bytes | pinned copy |
|---|---|---|---|
| candidate `fdgdd_5_18_inflated_D15.txt` | `3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998` | 700,931 (76,238 LF lines) | `inputs/` |
| `master_H_5_6.json` | `891337721265767e7136aee41a8e0da5f2219decec4216a62e8f6b70ac90db2c` | 25,493 | `inputs/` |
| `local_RDTD_3_4_3.txt` | `fcdb428580365490a83519a30984f275707f60b5a4222732cb0ec0889dad3d58` | 1,270 | `inputs/` |

Each source file hash, the expected hash and the copy hash agree. Copies were made with exclusive create. Read-only
provenance hashes: contract `cfafe572…6a17` (equal to the README record), source text `df52a8f1…4c3c8164`, lane
README `352f9505…0eaf`, construction note `2d91079c…b638`, seed-v1 `92ed1656…129d`, receipt-v1 `83bb6340…a458a6`.

## 2. Definitions implemented (Tan–Zhou arXiv:2503.11934v1, pinned text, LF lines)

* GDD (LF 48–59): "(1) B is a family of subsets of X (called blocks), each having cardinality in K; (2) each block of
  B intersects any given group in at most one point; (3) each t-subset of X from t distinct groups is contained in
  exactly one block."
* PPC/PC (LF 69–70): "A partial parallel class (PPC) of Y is a collection of pairwise disjoint blocks contained in
  Y. A parallel class (PC) of Y is a PPC that partitions Y."
* **Kirkman frame (LF 237–240):** "A Kirkman frame F(2,3,v{m}) (as in [18]), briefly by KF(m^v), is a GDD(2,3,mv)
  of type m^v (X,G,B) such that the block set B can be partitioned into subsets P_r, r ∈ R, each P_r being a PC of
  X \ G for some group G ∈ G. A KF(m^v) exists if and only if m ≡ 0 (mod 2), v ≥ 4 and m(v−1) ≡ 0 (mod 3)."
* Derived design (LF 241–242): "Let (X,G,A) be a GDD(3,4,mv) of type m^v. For any x ∈ X, let A_x = {A\{x} : x ∈ A,
  A ∈ A}. Then the derived design (X\G, G\{G}, A_x) is a GDD(2,3,m(v−1)) of type m^(v−1)."
* FDGDD (LF 246–247): "FDGDD(3,4,v{m}) to denote a GDD(3,4,mv) of type m^v whose derived design at every point is a
  KF(m^(v−1))."

So, for v = 5 and m = 18, the derived design at x lives on the 72 points X∖G_x with the other four groups. Each
class must be a PC of (X∖G_x)∖G_j for some j ≠ group(x), meaning 18 pairwise disjoint triples covering 54 points.
The source states no class counts. Degree counting forces 648 derived triples, 36 classes and 9 classes per missed
group, and these counts are checked only as consistency checks. Format D follows lane README §3 (LF 126–131).

## 3. Checker (own, stdlib only)

`code/check_fdgdd_format_d.py`, sha256 `0312f859e74f3e5aee650a3e41ee92cf2dfa5f674906e65b503ed35b0eaaa9d4`. This desk wrote it from the
definitions above and the README Format D text. No lane checker, producer, seed or mutation code was read, imported
or executed. The checker uses no symmetry and no construction route. Its grammar is strict: ASCII [0-9A-Z space LF]
only, final LF, no blank or comment lines, single spaces, canonical integers, and POINT sections exactly 0..89 in
order. It runs 22 named checks and also enumerates the transverse-triple universe and the per-point cross-pair
universe explicitly, then tests exact equality against them.

## 4. Results on the candidate

| condition | status |
|---|---|
| candidate_hash_and_pin | **PASS** |
| format_d_strict_parse_and_header | **PASS** |
| 90_points_five_groups_of_18_as_declared | **PASS** |
| every_block_transverse_4_subset | **PASS** |
| transverse_triples_exactly_once_exact_universe_equality | **PASS** |
| 14580_blocks_distinct | **PASS** |
| no_block_inside_a_group_pair_union | **PASS** |
| every_point_derived_design_is_GDD_2_3_72_type_18^4 | **PASS** |
| every_point_classes_partition_derived_into_PCs_of_72_minus_one_group | **PASS** |
| exactly_36_classes_every_point | **PASS** |
| classes_missing_each_group_9_each | **PASS** |
| FDGDD_definition_core | **PASS** |
| positive_under_python3_-B_and_-O_-B | **PASS** |
| controls_rejected_for_intended_reason | **PASS** |
| independent_block_reexpansion_equals_candidate | **PASS** |

The checker's verdict on the candidate is **PASS**: all 22 checks PASS and none are NOT_RUN. Key counts:
* 5 declared groups of 18 partition {0..89}.
* 14,580 block lines, all distinct, all transverse 4-subsets.
* Exact universe equality: the 58,320 transverse triples and the triples of the blocks agree, with 58,320
  incidences, maximum multiplicity 1, 0 uncovered and 0 non-transverse.
* At all 90 points: 648 derived triples cover the 1,944 cross pairs of the other four groups exactly once, giving a
  GDD(2,3,72) of type 18⁴.
* 3,240 classes were checked (36 at every point, 18 triples each). All 3,240 are PCs of (X∖G_x)∖G_j with the
  declared j, and at every point the classes list A_x exactly once.
* Classes missing each other group: **9, 9, 9, 9 at all 90 points**. These actual counts equal the declared label
  counts.

Positive runs (all four reports have identical checks and statistics):

| interpreter and flags | Python | optimize flag | verdict | wall s | max RSS bytes |
|---|---|---|---|---|---|
| `/usr/bin/python3 -B` | 3.9.6 | 0 | PASS | 0.344 | 52477952 |
| `/usr/bin/python3 -O -B` | 3.9.6 | 1 | PASS | 0.341 | 55820288 |
| `/opt/homebrew/bin/python3 -B` | 3.14.3 | 0 | PASS | 0.281 | 65126400 |
| `/opt/homebrew/bin/python3 -O -B` | 3.14.3 | 1 | PASS | 0.280 | 65470464 |

## 5. Controls (fixtures retained in `controls/`, manifest `controls/manifest.json`)

Each fixture is a full copy of the candidate with one defect. The runner is `code/run_matrix.py` and its summary is
`runs/matrix-summary.json`, sha256 `e2a85f942cc71e9febccf44890e9f7c5df6666d0174af6ea14e84bcf1e8d3702`. Every fixture was run 4 times: two
interpreters, each with `-B` and `-O -B`. A run counts as an intended-reason rejection only if all of these hold:
* exit code 1 with verdict FAIL;
* no checker exception;
* every intended check FAILs;
* a recorded F06 example carries the named status, where the manifest names one;
* the fixture hash equals the manifest hash.

| fixture | category | intended | failed checks (identical in all 4 runs) | rejected for intended reason |
|---|---|---|---|---|
| `c01_point_swap_between_blocks` | point swap between blocks | `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE` | `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D02_DERIVED_IS_GDD_2_3`, `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `c02_deleted_block` | deleted block | `C09_BLOCK_COUNT`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE` | `C09_BLOCK_COUNT`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D01_DERIVED_COUNT`, `D02_DERIVED_IS_GDD_2_3`, `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `c03_duplicated_block` | duplicated block | `C08_BLOCKS_DISTINCT`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE` | `C08_BLOCKS_DISTINCT`, `C09_BLOCK_COUNT`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D01_DERIVED_COUNT`, `D02_DERIVED_IS_GDD_2_3`, `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `c04_block_inside_two_groups` | a block inside two groups (non-transverse) | `C06_BLOCK_TRANSVERSE`, `C07_BLOCK_NOT_IN_GROUP_PAIR_UNION` | `C06_BLOCK_TRANSVERSE`, `C07_BLOCK_NOT_IN_GROUP_PAIR_UNION`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D01_DERIVED_COUNT`, `D02_DERIVED_IS_GDD_2_3`, `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `c05_frame_class_two_triples_share_point` | a frame class with two triples sharing a point | `F05_CLASS_PAIRWISE_DISJOINT` (F06 status `OVERLAP`) | `F05_CLASS_PAIRWISE_DISJOINT`, `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP` | 4/4 |
| `c06_frame_class_not_full_parallel_class` | a frame class that is not a full parallel class of its 72-18 points | `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP` (F06 status `NOT_FULL`) | `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP`, `F08_CLASS_COUNT`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |
| `c07_frame_class_spans_two_missing_groups` | a frame class spanning two missing groups | `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP` (F06 status `SPANS_TWO_OR_MORE_MISSING_GROUPS`) | `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP` | 4/4 |
| `c08_out_of_range_point_label` | out-of-range label (point label 90 in a block) | `C03_POINT_LABEL_RANGE` | `C03_POINT_LABEL_RANGE`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D01_DERIVED_COUNT`, `D02_DERIVED_IS_GDD_2_3`, `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `c08b_out_of_range_frame_label` | out-of-range label (FRAME label 5) | `F02_FRAME_LABEL_VALID` | `F02_FRAME_LABEL_VALID`, `F07_FRAME_LABEL_MATCHES_MISSED_GROUP`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |
| `c09_group_declaration_duplicate_label` | corrupted group declaration (label declared twice, one missing) | `C04_GROUPS_PARTITION` | `C04_GROUPS_PARTITION` | 4/4 |
| `c09b_group_declaration_swapped_labels` | corrupted group declaration (two labels swapped between groups) | `C06_BLOCK_TRANSVERSE` | `C06_BLOCK_TRANSVERSE`, `C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE`, `D02_DERIVED_IS_GDD_2_3`, `F02_FRAME_LABEL_VALID`, `F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP`, `F07_FRAME_LABEL_MATCHES_MISSED_GROUP`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |
| `x10_frame_label_mismatch` | extra: declared FRAME label differs from the missed group | `F07_FRAME_LABEL_MATCHES_MISSED_GROUP` | `F07_FRAME_LABEL_MATCHES_MISSED_GROUP`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |
| `x11_missing_point_section` | extra: POINT 89 section removed | `F01_POINT_SECTIONS` | `F01_POINT_SECTIONS`, `F04_CLASSES_PARTITION_DERIVED`, `F08_CLASS_COUNT`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |
| `x12_non_derived_triples_in_intact_class` | extra: class still a PC but two triples are not derived | `F04_CLASSES_PARTITION_DERIVED` | `F04_CLASSES_PARTITION_DERIVED` | 4/4 |
| `x13_frame_label_own_group` | extra: FRAME label equal to the group of x | `F02_FRAME_LABEL_VALID` | `F02_FRAME_LABEL_VALID`, `F07_FRAME_LABEL_MATCHES_MISSED_GROUP`, `F09_DECLARED_MISSED_GROUP_COUNTS` | 4/4 |

Totals: **60 of 60 control runs** were rejected for the intended reason, and **4 of 4 positive runs** passed.
Notes on specific fixtures:
* c05 swaps two triples between two label-1 classes at x = 0, so the union of the classes is still A_x.
* c06 moves one triple of a class at x = 45 into a new one-triple class, so all classes stay disjoint.
* c07 is a Kempe-type exchange of one 8-triple component between the label-1 and label-2 classes at x = 0. Both
  classes keep 18 disjoint triples on 54 points, but each now misses 10 + 8 points from two groups, and only F06
  fails.
* x10–x13 are extras beyond the requested list.

## 6. Independent block re-expansion (step 4)

`code/reexpand_blocks.py`, sha256 `8ed1989c425a89cb29bb0acdbdd5dd58cf9c2bbd72983563b51f0dac65df355a`, uses only the pinned master and the
RDTD's GROUPS and BLOCKS. For each master block p0<p1<p2<p3 and each RDTD block, the RDTD point at position b of
group i maps to 3·p_i + b.

* **Result: EQUAL.** The 14,580 inflated blocks and the 14,580 candidate blocks are equal as multisets, with
  0 missing and 0 extra.
* The candidate's line order equals the sorted inflation.
* The inflated groups equal the declared groups.
* Sorted-block sha256 is `09c0cc09ba8a48965edc83cfdbba11a43fe00fc4233d5316878a280dbdbcb9e7` on both sides.
* Runs: `/usr/bin/python3 -B` and `/opt/homebrew/bin/python3 -O -B`.
* **Frames are not reproduced this way, and no attempt was made to.** The frames were found after inflation
  (construction note §3) and are not determined by the master or the RDTD. They are verified directly in §4.
* Comparison controls show that the comparison detects differences. With the c01 fixture it reports 2 missing and
  2 extra blocks: `[0,18,36,60]` and `[1,18,36,62]` are missing, `[0,18,36,62]` and `[1,18,36,60]` are extra. With
  c02 it reports 1 missing (`[11,24,36,67]`), and with c03 1 extra (`[4,33,39,71]`).
* Informational ingredient checks, which are not acceptance conditions:
  * the master is a GDD(3,4,30) of type 6⁵: 540 distinct transverse blocks, with all 2,160 transverse triples covered exactly once;
  * the RDTD file's blocks form a TD(3,4,3) and equal the 27 zero-sum vectors, so the point assignment order does not matter (checked: the reversed assignment gives the same multiset);
  * the 30 master permutations are block- and group-preserving bijections. They are closed under composition and act regularly. Their element orders are 1¹ 2¹⁵ 3² 5⁴ 15⁸ and they are non-abelian, which matches D15.

## 7. Resources

* At most 2 busy processes at any time; all runs were sequential.
* Checker: 0.28–0.34 s wall per positive run, 52–65 MB max RSS. Controls: 0.08–0.40 s.
* The full 64-run matrix took 23.2 s.
* Re-expansion: 0.05–0.06 s, at most 35.5 MB RSS.
* The desk holds about 12.9 MB, almost all of it fixtures. Free disk at the last check was 13,941,448,704 bytes, above
  the 12,000,000,000-byte floor.

## 8. Deviations (all retained, nothing renamed or deleted)

1. A shell-variable slip (`$c__sys39__B` was read as one empty variable) caused two problems:
   * The first comparison-control run wrote `runs/reexpand-control-.json`. Its content is the c01 comparison, input
     sha256 `c8c48b40…2451`.
   * The c02 and c03 runs in the same command refused to overwrite that file (exclusive create) and exited with
     FileExistsError.

   All three were rerun under correct names. The misnamed file is retained.
2. The code was drafted and dry-run in the eval kernel (in-process Python 3.14, no child processes) before being
   written once to `code/` with exclusive create. The dry run left `tmp/reexpand-dryrun-1.json`, a retained scratch
   file.
3. `python3` was exercised as both `/usr/bin/python3` 3.9.6 and the PATH `python3`, which is
   `/opt/homebrew/bin/python3` 3.14.3.
4. The grammar is stricter than the README wording; the candidate conforms. F09 counts declared FRAME labels. The
   actual missed-group counts are recorded separately and agree with them.
5. No reviewer CLI was run; this assignment did not ask for one.

Not assessed:
* the worker's SAT re-solves and replay scripts;
* the "master is not frame-derived" diagnostic;
* automorphism transport of frames (not needed, since every point's frame was checked directly);
* gate, bridge, novelty and significance.

**UNKNOWNs: none.** No run timed out or was interrupted.

## 9. Files (sha256)

* `code/check_fdgdd_format_d.py` `0312f859e74f3e5aee650a3e41ee92cf2dfa5f674906e65b503ed35b0eaaa9d4`
* `code/make_controls.py` `0e30a510aab55aa8ec70efeef458667b0f036079f38b853f6a280b4b07bdeb67`
* `code/reexpand_blocks.py` `8ed1989c425a89cb29bb0acdbdd5dd58cf9c2bbd72983563b51f0dac65df355a`
* `code/run_matrix.py` `673a82c29f8f6884965c5858fedb63587bed856ab71fec3258c416d1a7400be2`
* `controls/manifest.json` `e05cb4f607f6ee694ccdfa63fde85cd1ef4a5b63678982a941862c40803493aa` (15 fixture hashes inside)
* `runs/matrix-summary.json` `e2a85f942cc71e9febccf44890e9f7c5df6666d0174af6ea14e84bcf1e8d3702` (64 per-run reports in `runs/`)
* `runs/reexpand-candidate__sys39__B.json` `db2fc6a04a9fce2a3e7267d7cab0bcd8f58defe4a2de5f2e5713cdc4f767bcce`
* `runs/reexpand-candidate__brew__OB.json` `64ecc36a4946d93ce2f6a8ca784b288fb560820d829110db8a20f6c09b9c2c03`
* `result.json` `3197db9c6907fa191effc9f5df27bb75c006686e1e08af52e3c07f96f80f243f`
* `checkpoint-01.md` `e195d0f9d696096082ae31fa39d0a3e9bc4968ad4a07e6d0caa7e5cd3afe65e5`
