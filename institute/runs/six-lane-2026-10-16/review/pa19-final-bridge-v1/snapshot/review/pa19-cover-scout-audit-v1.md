# PA19CoverAudit (read-only scout report, verbatim)

Recorded 2026-10-17 12:38:58 PDT. Static audit; hashes quoted by the scout were worker-recorded, not independently computed. Subsequent worker fixes are not part of this snapshot.

# PA(19,8,6) coverage audit: case split versus generated case lists (read-only)

## Summary
- **No prior parent PA19 audit exists.** A glob and grep of `institute/runs/six-lane-2026-10-16/review/` for pa19, packing and info-1 found nothing, so everything below is new.
- **Mathematical cover: no fatal or major gap found.** The chain runs: valid array → one of 10 column-profile multisets → either one of 486 quad graphs (the balanced multiset ms00) or one of 5,577 skeletons (ms01–ms09) → extra placement splits for the hard cases. Every step is either a condition that any valid array must satisfy, or a symmetry reduction that the code supports.
- **The target is not decided.**
  - M1 is open on 1,073 of 5,577 non-balanced cases.
  - M2 has not run on any of the 5,577.
  - Several links from case list to solved formula are recorded by the worker but never re-derived by the aggregator. The parent must replay them before any acceptance.
- **Limits of this audit.** I ran no scripts and computed no SHA-256 values. Every hash quoted below is worker-recorded. Labels: **[OBS]** = I read the file or a jq result; **[CODE]** = my reasoning from source or by hand; **[CLAIM]** = worker statement I did not verify.

## Architecture (brief)
- `profiles.py` produces the 10 multisets.
- ms00 path: `geng` produces 486 graphs → `cases19q0/` holds M1 (`encode_q0`) and `m2q0b/` holds M2′ (`encode_q0b`).
- ms01–ms09, M1 side: `gen_skel.py` writes `skeletons/` → `gen_skel_cases.py` writes `cases19skel/{index,specs}` → `encode_skel` CNF per case.
  - Easy cases: pass-1 result plus a proof check (`proofcheck/` or `cycle2/proofstream/`).
  - Hard ms06: the same CNF solved directly (`cycle2/hard/`).
  - Hard ms01: full placement split A3 (`cycle2/a3/`).
  - Hard ms09: one-column split A3′ plus batching A3″ (`cycle2/part/`).
- ms01–ms09, M2 side: `gen_skel_b.py` (nauty `genbg`) writes `cycle2/skel-b/`. `compare_skel` maps M1 index to M2 index (`a_to_b`). Then `encode_skel_b` direct for most cases, or `extend_b` + `build_part(batch)` for the split cases.
- `summarize3.py` aggregates per tag into `STATUS3.json`.

## Report

### (1) Cover map

| Step | Statement | Count | Evidence |
|---|---|---|---|
| L1 | Pairs agreeing in a column sum to at most C(19,2)=171; each column contributes at least 21; so total excess is at most 3, and exactly L = 3 − excess row pairs agree nowhere | – | README.md:33-36, profiles.py:36 [CODE] |
| L2 | Column profiles: partitions of 19 into ≤6 parts, zeros allowed, at most 24 agreeing pairs | 235 partitions → 6 profiles | profiles.py:13-25,37-38; data/profiles-19-8-6.json:7-8 [OBS]; my hand recount: 235 partitions, 6 profiles [CODE] |
| Multisets | 8 columns with total excess ≤3: ms00–ms09 | 10 | profiles.py:41-43; README.md:42-44 [OBS]; hand recount [CODE] |
| ms00 lemma | t(r) ≤ 2; n₂ = 13 + n₀ and n₀ ≤ 3. Quads form a simple graph with max degree 4 and 13–16 edges | – | README.md:90-97, encode_q0.py:4-12 [CODE: re-derived] |
| ms00 list | `geng -q 8 13:16 -D4` | 486 (309/136/35/6 by edge count) | g6 file; `quadgraphs-independent-check.json` bijection=true [OBS/CLAIM] |
| ms00 binding | `cases19q0/index.json`: 486 unique tags g000–g485; first/last graph6 equals first/last g6 line | 486 | jq [OBS] |
| Skeleton facts | B = N−1−2k = 2; \|T\|+w ≤ 2; per-row miss count is exact and lies in [0, L]; bounds tmax and hmax; exact interval filter when there is one special column | – | gen_skel.py:51,61-63,115; README.md:114-123 [CODE: all are conditions every valid array satisfies] |
| ms01–ms09 lists | `gen_skel` (geng + every linear hyperedge set + iso dedup) | 3215/59/674/39/73/482/482/482/71 = **5,577** | gen_skel.py:67,84,111,132; skeleton file headers [OBS] |
| Independent list | `genbg` with `-Z1 -d2:0 -D{tmax}:4`, h = 0..2c0 | 9/9 bijections | gen_skel_b.py:87-119; compare_skel.py:58; compare-ms0X.json:3-7 [OBS/CLAIM] |
| Index binding | 5,577 entries, unique tags, indices 0..n−1 per multiset, tags well-formed; spec `ms09_s00006` matches `skeletons-ms09[6]` | 5,577 | jq on index.json [OBS]; only one spec spot-checked |
| Per-case symmetry breaking | Value precedence among equal-count labels; row-lex for rows with identical fixed pattern; column-lex for adjacent identical free columns. All are lex-leader for one row-major order, so the orbit minimum satisfies all of them | – | encode_skel.py:45,84-118; encode_q0.py:102-130; encode_partq.py:118-133 [CODE] |
| Hard cases | Pass-1 UNKNOWN | 180 = 31 ms01 + 106 ms06 + 43 ms09 | hard-tags-*.txt; README.md:179 [OBS] |
| ms01 hard | A3: all blocks of the single special column fixed | 31 cases, 17,438 placements. 30 decided; `ms01_s02573` 869/870 (f00012 UNKNOWN, no rerun yet) | a3/*/ext.json headers (all 31 sources match their directory) [OBS] |
| ms09 hard | A3′ one-column split (m=1) + A3″ batches | 31 ext.json, 200,620 placements. 30 decided; s00043 in progress (19,636 placements); 12 not started (s00047, 48, 51, 55–61, 63, 67) | part/*/ext.json, summaries [OBS] |
| ms06 hard | Same CNF solved directly; its SHA must equal pass 1 | 60/106 decided | summarize3.py:78; e.g. ms06_s00028 SHA 5d1e08ae… equal in both records [OBS] |
| M1 total | – | 4,504 decided / **1,073 open** (detail below) | STATUS3.json:14-99 [CLAIM] |
| M2 | Job lists partition all b-indices: 5,397 + 106 + 74 = 5,577. Hard lists equal `a_to_b` of the M1 hard tags, in order | **0 results** | m2-jobs-*.txt vs jq on compare-map [OBS: checked by hand]; no `m2skel_v2/` or `m2part/` directory yet |

The 1,073 open M1 cases:

| Multiset | Open | Breakdown |
|---|---|---|
| ms01 | 1 | `ms01_s02573` |
| ms06 | 276 | 46 hard + 230 awaiting a checked proof |
| ms07 | 273 | awaiting a checked proof |
| ms08 | 482 | awaiting a checked proof |
| ms09 | 41 | 13 hard + 28 awaiting a checked proof |

Split-step soundness [CODE]:
- **Placement enumerators (`extend_p1`/`extend_p1q`, extend_p1q.py:57-124).**
  - Row classes are defined by history (P0 set plus roles so far). Whether a row is available and which rows it agrees with depend only on its class, and rows inside one class either all agree or none do. So always taking the lowest-index rows of each class loses no placement (induction over A, then B, then P).
  - Budget pruning allows each remaining column to move w by at most ±1, which every valid array satisfies.
  - The isomorphism dedup only merges placements related by skeleton automorphisms, the A/B swap, or permuting fixed P1 columns.
  - In the one-column split, any P1 column may be moved to position c0. The remaining P1 columns are only lex-ordered among themselves (encode_partq.py:133, encode_partbatch.py:136).
- **`extend_b` (M2).**
  - It enumerates exact orbits as per-class (a,b,p) counts, at most one row per block for classes with a nonempty P0 set (extend_b.py:62).
  - It uses the same budget rule (:54-55) and takes the canonical minimum over a brute-force automorphism group times the A/B swap (:111-126).
  - It quotients by the same group as M1, so per-case counts must match. Observed: raw/count equal on two pairs, 10278/815 (ms09_s00001 ↔ b9) and 810/62 (ms01_s01260 ↔ b1554).
- **Batching (A3″).** A selector clause plus guarded placement cells and guarded row-lex; every unguarded constraint is the same for all placements (encode_partbatch.py:46-47,98-101,121-135). So batch UNSAT implies every subcase is UNSAT.
- **M2 v1 symmetry breaking.** It labels Q_d∖Q_c in each P0 column, applies first-occurrence order to special columns, and column-lex to free columns, with no row-lex. Each part relabels different columns, so all can hold at once.

### (2) Gaps

**Fatal: none found.**

**Major (block acceptance; not soundness defects):**
1. **Unfinished cases.** M1 has 1,073 open cases and M2 all 5,577; until they close, the verdict is UNKNOWN.
2. **Unchecked binding.**
   - The aggregator never regenerates the pass-1 CNF from the spec. Only the 60 decided ms06 hard cases show `cnf_matches_pass1_sha`.
   - Split results are tied to ext.json by filename index only. The record `cnf_sha256` is never re-derived. The one incidental match: `batch_04300_04399` and its `_r2` rerun both record 7d9af598….
   - There is no hash manifest for `index.json`, the 5,577 specs, `skel-b/*`, the compare maps, ext.json files or job lists. `SHA256SUMS-cycle1.txt` covers only cycle-1 code and data.
   - `STATUS3` open-tag lists are cut at 500 (summarize3.py:129).
   - The ms00 status block is copied from cycle-1 `STATUS.json` with a hard-coded 486 cases (summarize.py:26-32).

**Minor:**
3. The "independent" skeleton replication shares the same tmax/hmax/filter formulas (gen_skel.py:61-63 vs gen_skel_b.py:86-88), the same nauty package and the same networkx comparison. I re-derived the formulas by hand, so this is acceptable if the dependence is stated.
4. Stale README text:
   - :83 and :137 still say "no independent replication", which cycle 2 superseded.
   - :47-72 describe the abandoned M-class normalization, not the cover actually used.
   - :262 "reproduces exactly" compares two copies of the same code, so it shows consistency, not independence.
5. The M2 batch-range heuristic (summarize3.py:53) depends on writer conventions: M2 stores `[first,last]` plus a `multiset` key, M1 stores explicit lists without it. Consistent today, but fragile.
6. Control coverage:
   - The PA18 control uses an empty skeleton with `base_quad=False` (control18.py:109-110), so it never exercises the cover.
   - `gen_skel_b` is hard-wired to (19,8,6), so it has no small-parameter control.
7. The meaning of the genbg options was taken from nauty documentation. Confirm with `genbg -help`.

**Shortcut for the one open ms01 item [CODE; not a checked result].** `ms01_s02573` f00012 (placement A{9,10,11,12}, B{13,14,15,17}, P{8,16}) leaves only rows 16 and 18 with miss count 2. This matches the recorded vector. A valid array makes the miss count exact, so row 16 must miss two rows that each also miss someone, and only row 18 qualifies. So the subcase has no completion. Under the frozen rules a checked artifact is still needed: either a recorded pre-filter amendment or a longer checked run.

### (3) Files to pin, and a coverage-only replay plan

**Hashes recorded by the worker in `SHA256SUMS-cycle1.txt`** (parent must recompute):

| File | Manifest line | SHA-256 |
|---|---|---|
| src/encode_e1.py | :2 | 2a76e8bdc813e92e60de4267bc0538eef0e0849effb692671fb044c14b16b830 |
| src/encode_q0.py | :3 | 8d2840f4cc5116f8acbd96d5a9a9d1e432b660887a082cc969a94ee306419299 |
| src/encode_q0b.py | :4 | 3c431849be93bb198adf484e5dac144bd0ab56d86f541913bd9b17435586e24d |
| src/encode_skel.py | :5 | 0783c3ea42a9e023657756de5ff0b4482a18d2c654e4be3a2955bda5bad1dc3a |
| src/gen_skel.py | :7 | 7042249df25c51f5deb3da7d560b8935b468d46798464e54cc5e0862bd74fafd |
| src/gen_skel_cases.py | :8 | 5c77c1177ba9167d1e754fa01f5227048a1c1d1b933190932dc5982334a8e5ce |
| src/graphs_check.py | :9 | 27e798ed8a7645967f38e14f8f64c8b417c940418a5d284f5ab82f24f45834c0 |
| src/profiles.py | :12 | a45c95175b9c7f0c28e9b4cc076a6e88ead4df777242483ebdb6496243ec02ef |
| src/run_cases.py | :13 | c32de7089b2bddb4c841286bf12552f50d1ccc66d98d82a9f1dbda3001d02007 |
| src/run_proofpass.py | :15 | f2f291677261437e56335ea0fd3e6d8e67a4aa30b633daa04fd408f55f6f78ec |
| data/quadgraphs-8v-13to16e-D4.g6 | :23 | 687602738d82cf0ff3d66f4307c90633503c32edba957e7a5cca349a7ea56d8c |
| data/profiles-19-8-6.json | :24 | aaf73eda8237173e2c30fea9a8af77b120dd172585627f9e34c451da7efd6902 |
| data/quadgraphs-independent-check.json | :25 | 3ea92ac3400a69258bc3183cef21237b3fcebbc46cfb0506dd5189dd02ff1a7b |
| skeletons/skeletons-ms01.json | :27 | 00707e5b089bfb7ab885dda760791b42f6673622c3c6918c8a651366e22d0710 |
| skeletons/skeletons-ms02.json | :28 | da0447d20088a8caeca8164db9af9b4dbb8106e172084a84247cbfc38488465d |
| skeletons/skeletons-ms03.json | :29 | e50d96b0352fdb6da0eb873fe86abb56f775aa4e00d745fb834479418cdbed16 |
| skeletons/skeletons-ms04.json | :30 | ca4f41c89fc95fa99cb3bcffa61bbf0a6d028402f245828a08a0fb1f56a0629c |
| skeletons/skeletons-ms05.json | :31 | 973be16c7f10c0cb19cba7abebb234a1081d1efc5205e763566c06eb610541cb |
| skeletons/skeletons-ms06.json | :32 | 1c1253abf572a36507a10e3d4d435f967cbe12bbd1af4af1110f744dad699504 |
| skeletons/skeletons-ms07.json | :33 | db30f54bcadc2806e8398ff4cf13225252e42a1d15698660e94246341f2f0a14 |
| skeletons/skeletons-ms08.json | :34 | 7fd197b7ba7b3564f105a666cfcc0ddd11765661776d7d211f4474810d00569d |
| skeletons/skeletons-ms09.json | :35 | 34a031067c86fb06a2facc4e336645878b902b110855ec327476a458ec482e68 |

**No recorded hash; the parent must compute now and again at closeout:**
- The contract and the current README.md.
- `cases19skel/index.json` and the 5,577 `cases19skel/specs/*.json`.
- `cases19q0/index.json`.
- Sources: `src/{gen_skel_b, compare_skel, extend_p1, extend_p1q, extend_b, encode_full, encode_partq, encode_partbatch, encode_skel_b, stream_check4, summarize3, run_hard4–7, rerun_unknown, run_m2skel5, run_m2part, run_m2partbatch}.py`.
- `cycle2/skel-b/*` (lists, `compare-ms0X`, `compare-map-ms0X`).
- `cycle2/a3/*/ext.json` (31), `cycle2/part/*/ext.json` (43 at completion), and later `cycle2/m2part/*/ext.json` (74).
- `cycle2/m2-jobs-*.txt`, `cycle2/hard-tags-*.txt`, and `STATUS3.json` (snapshot).

**Replay rules.** No solver runs. Use `python -B` (or `PYTHONDONTWRITEBYTECODE=1`) so imports don't write `__pycache__` into the lane. Write outputs only to a parent review directory. Run one process at a time under `nice`, with no `subprocess.run(timeout=…)` (it sends SIGKILL). Read only small JSON files and rebuild CNFs in memory; never copy proofs or CNFs. Cost estimates for R3, R5, R6 and R8 are guesses.

- **R0 (≈1 min).** Pin the files above.
  - Run `shasum -c SHA256SUMS-cycle1.txt`. Code and data lines must pass; README, checkpoints and STATUS lines are expected to fail because those files were edited later.
  - Record the nauty and networkx versions, and confirm the `-Z`, `-d`, `-D` options with `genbg -help`.
- **R1 (seconds).** A stdlib script recounts the profiles: expect 235 partitions, 6 profiles, 10 multisets in the same order as `profiles-19-8-6.json`.
- **R2 (≈5 min).**
  - Regenerate the 486 graphs with `geng -q 8 13:16 -D4` and hash the output against the g6 file. Rerun `graphs_check.py`.
  - For each tag g000–g485: the index graph6 must equal the g6 line; the M1 and M2′ result files must show UNSAT, the same graph6, and matching CNF SHA; the `.check.json` must have `ok`; the M2′ file must have `lrat_verified`.
- **R3 (≈5–30 min).**
  - Rerun `gen_skel`, `gen_skel_b` and `compare_skel` for ms01–ms09 into the parent directory. Byte-compare with the lane files and the `a_to_b` maps; expect 3215/59/674/39/73/482/482/482/71.
  - Using the networkx atlas, count graphs on 5, 6 and 7 vertices with maximum degree 4; the generator headers say 34, 122 and 510. This checks the geng input without nauty.
- **R4 (≈1 min).** For each of the 5,577 index entries, the spec's skeleton, c0, special profiles and L must equal the matching entry of `skeletons-msXX.json`.
- **R5 (≈30–90 min).** Rebuild each CNF in memory with `encode_skel.build` and `stream_check4.cnf_bytes_of`, and compare its SHA-256 with `results/<tag>.json` and the proof-check record. Do all 5,577, or at least the 180 hard cases plus 1,000 random ones.
- **R6 (≈30–90 min).**
  - Regenerate `extend_p1` for the 31 ms01 hard cases, `extend_p1q` with m=1 for the 43 ms09 hard cases, and `extend_b` for the 74 matching b-indices.
  - Each output must equal the stored ext.json. For each M1/M2 pair, the placement count and the raw count must be equal.
- **R7 (≈5 min).** Run the parent's own strict aggregator, not `summarize3`.
  - Every record's tag must match its directory.
  - Each f-file's name index must equal the index field inside it.
  - Each batch's indices must lie within range and match its filename.
  - Each counted result must be UNSAT, checked, and not interrupted.
  - Include the `_r2` reruns, write the full open lists (no 500 cut), require both M1 and M2 per case, and stop on any SAT.
- **R8 (≈20–60 min).** Re-derive the CNF SHA for every `_r2` record and a seeded sample of at least 200 f/batch records from (spec, ext.json placement).

### (4) What remains imported or worker-only
- **Imported:**
  - How nauty `geng`/`genbg` behave and that they are complete.
  - networkx: the graph atlas covers every graph up to 7 vertices, and `is_isomorphic` and the WL hash work as documented.
  - kissat, CaDiCaL, drat-trim and lrat-check are correct.
  - The CPro1 PA18 array and the literature open status.
- **Worker-only:**
  - Every UNSAT status, `checked` flag and `cnf_sha256`, and every SHA256SUMS entry.
  - The bijection and `graphs_check` outputs, and the (13,5,4) and PA18 control results.
  - That ext.json files and pass-1 CNFs are deterministic and match the current specs.
  - That the clause encodings implement the stated constraints. This was out of scope; I read only their symmetry-breaking parts.

**Controls that are no-ops or circular:**
- The `extend_p1q` vs `extend_p1` check compares two copies of the same code.
- The PA18 control bypasses the skeleton entirely.
- The M1/M2 placement-count agreement is real but covers only 2 production cases plus 16 cases at (13,5,4); R6 extends it to all 74 at low cost.

ms00 results are restricted to all-balanced columns. Nothing here claims the PA(19,8,6) question is decided.
