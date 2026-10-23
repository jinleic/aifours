# ADDENDUM-v1: parent-desk fixes for the hostile review of C5 (m1–m7)

Desk `review/olson-p5o4-parent-replay-v1/`. Written after host clock 10:22:10 PDT 2026-10-18. This addendum answers the
parent-desk MINORs of `review/olson-p5o4-complete-claim-claude-v1.note.md` (7816550f…6a5f).

It consists of new files only. RESULT-v1/NOTE-v1 and RESULT-primary-v1/NOTE-primary-v1 are unchanged, and all four still
hash to their published SHAs. Re-hashing gives 144/144 RESULT-v1 pins and 122/122 RESULT-primary-v1 pins.

Machine-readable files:
- `ADDENDUM-v1.json`, which pins this note;
- evidence `out/addendum-v1/evidence/evidence.json` (67337f7b…2d32), written by `src/addendum_evidence_v1.py`.

**Verdict and scope unchanged: CONFIRMED for C5′ on D, conditional on this code; no code changed.**

**m2.** This desk establishes only C5′. C5 = PLAN-v1 §2 (R1, R2) + PM* + this C5′. This desk did not audit the
reduction; the hostile review's §A1 re-derived PM* in the PLAN-v1 L20 form.

## m6: provenance

**Toolchain.**
- `clang++` on PATH is `/usr/bin/clang++` (xcrun shim). It resolves to
  `/Library/Developer/CommandLineTools/usr/bin/clang++`.
- Apple clang 17.0.0 (clang-1700.3.19.1), target arm64-apple-darwin27.0.0, SDK 26.0, ld-1221.4, macOS 27.0.1 (26A434).
  Python is 3.14.3.

**Builds.** Both ran with cwd = desk and TMPDIR = desk/tmp. Both printed no compiler output, and each printed the hashes
immediately afterwards (session transcript):

| time | command | source → binary |
|---|---|---|
| 08:40:29 | `clang++ -O2 -std=c++17 -Wall -Wextra -o bin/replay_v1 src/olson_p5o4_replay_v1.cpp` | d0f7860b…6521 → b219bcda…91fc |
| 08:43:02 | `clang++ -O2 -std=c++17 -Wall -Wextra -o bin/replay_v2 src/olson_p5o4_replay_v2.cpp` | 89abe678…6b68 → **4bb26b02…1cf8** |

**Reproducible rebuild (10:16).** The same two commands were run into `out/addendum-v1/rebuild/` with the same
basenames. Both binaries came out **bit-identical** to `bin/`: same SHA-256, LC_UUID and ad-hoc CDHash. "bin/replay_v2
was built from 89abe678…" therefore no longer has to be imported: anyone with this toolchain can check it.

**The v2 build comment.** `src/olson_p5o4_replay_v2.cpp` was created at 08:42 by `cp -n` from v1 and then edited in
exactly three hunks:
- the brute usage comment (L13–14);
- `run_brute` with its two section-header comment lines (L464–560);
- the brute dispatcher line (L837).

Line 9 (`// Build: … -o bin/replay_v1 src/olson_p5o4_replay_v1.cpp`) was inherited unchanged. It is a stale comment, not
the command that was used. An automated check finds 0 changed lines outside comments, `run_brute` and the dispatcher.
So enum, controls, check, the DP, the group table and filter (d) are textually identical in v1 and v2.

Its filesystem birth time, 08:39:19, equals v1's [INFERENCE: carried over by `cp`]. Its last write was 08:42:58.
`bin/replay_v2` was created at 08:43:04 and never modified. Both times precede the first v2 run at 08:43:12.

**Which binary produced which run** (taken from the commands logged in each `out/<run>.log`):

| run | command | start–end PDT | exit |
|---|---|---|---|
| controls-v2 | `./bin/replay_v2 controls` | 08:43:12–08:43:13 | 0 |
| **enum-clean-v2** | `./bin/replay_v2 enum … none` | 08:43:13–08:43:39 | 0 |
| enum-bug-{untwisted,target8,parity}-v2 | `./bin/replay_v2 enum … <bug>` | 08:43:39–08:44:47 | 0 |
| check-all-avoiders-v2 | `./bin/replay_v2 check …` | 08:47:13–08:47:16 | 0 |
| indep-check-v1 | `python3.14 -B src/indep_check_v1.py …` | 08:47:16–08:47:21 | 0 |
| compare-primary-v1 (aggregation only) | `python3.14 -B src/compare_primary_v1.py …` | 09:48:59 | 0 |

`controls-v1` and `enum-clean-v1` were produced by `bin/replay_v1`. Their logs lack a cmd line; the command comes from
the session transcript. They serve only as the v1/v2 byte-identity cross-check.

**Timing relative to the external SIGTERM at 09:25:51.**
- Every native route-1 run ended by 08:47:21, which is **2,310 s (38.5 min) before** the SIGTERM.
- Every route-1 output file was created and last written inside the window of its producing run. Code files were last
  written before their first use.
- The only route-1 files written after 09:25:51 are the compare-primary-v1 outputs and log, and the two aggregation
  scripts.
- All 48 route-1 files (outputs, logs, sources, binaries, and the v1 twin) match **both** RESULT pins.

## (3) Fresh route-1 rerun

The rerun ran at 10:16:41–10:17:08 as `./bin/replay_v2 enum out/enum-clean-v2-rerun-a1 none`:
- under `ulimit -t 600`, exit 0, 26.59 s wall, 3,014,656 B RSS;
- the binary hashed 4bb26b02… both before and after the run;
- the output directory and files were created exclusively.

Results:
- `avoider_classes.txt`, `mixed_classes.txt`, `nonrigid_avoider_classes.txt` and `survivor_multisets.txt` are
  **byte-identical** to enum-clean-v2, and to the v1 twin.
- `summary.json` is byte-identical except for the single timing field `elapsed_s` (26.294 → 26.584). `maxrss_bytes` is
  identical.

## m5: pins (enum-clean-v2, the run the verdict uses; the rerun has identical list hashes)

| file | SHA-256 | bytes |
|---|---|---|
| nonrigid_avoider_classes.txt | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty) | 0 |
| mixed_classes.txt | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty) | 0 |
| avoider_classes.txt | fae66ba680ddbd007ffa9a42650797a0d3555cd270f0db313d8cb8c3a086eb59 | 27,520 |
| summary.json | 6c17552bc625b805e7f663dc80c513292062571f98ad661f7ead0c3333a80c15 | 8,074 |
| survivor_multisets.txt | 3f5e874cd54cea35213ec5d841d0bf217c7a7cdee63f24dab2f4da2b8b311c4d | 1,232 |

**Fail-closed external check.** This check runs outside the frozen code. It requires:
- both files to be empty;
- per-H mixed = 0 and non-rigid = 0;
- exact strata 0..7, `all_checks_ok`, bug = none, and 640 avoider lines.

It passes for enum-clean-v2, the rerun and the v1 twin. C5′ is now enforced by this check rather than read off the
summary.

**The `fv != 0` remark.** Acknowledged and not changed, because the code is frozen. −1 is unreachable: the table is
filled for every multiset of size R (C(R+4,4) of them, asserted), and every leaf multiset has size R by construction.

## m1, m7, m3, m4: wording

**m1.** **Route 2 supports nothing in the verdict.** The verdict rests on route 1 alone: (a)–(d) are proved, and the
DP decides every (d)-survivor. Route 2 is the same binary, DP and group table without the filter. It only re-confirms
the proved fact (d).
- NOTE-primary-v1 §6 should read: "A partial, optional no-filter check (H = 0, 1, 4–7 complete; H = 2, 3 UNKNOWN) is in
  §7. It is not a premise; (d) is proved in §2."
- NOTE-v1's "Two routes give this result" is superseded by the same rule. The H = 2, 3 rerun finished at 10:00:51 and
  is not cited.

**m7.** Read "independent implementation; plan-time counts seen". This is an unblinded, independent implementation
of the same method as the worker's Stage D (the P1′/(d) filter plus an ordered DP). It is not an independent method.
PLAN-v1, including its plan-time counts, was displayed in full before the code was written. The phrase "both of my
independent routes" in my final message (10:02) is withdrawn: routes 1 and 2 share one implementation.

**m3.** These avoiders are not maximal o_F = 4 words:
- PC-k2 has **maximal o_F = 2**. It lies in D only through 6 non-maximal splittings of s0⁷.
- A2 also has maximal o_F = 2, since S₄, S₁ and S₂ merge.

The maximal o_F = 4 witnesses are A1 (H=1, runs 4/4/4/1⁹, y=0000) and A3 (H=4, runs 4/4/4/444, y=0243). All runs of
both are non-empty.

**Classification of the 640 avoider classes by maximal o_F.** The value was computed from the literal cyclic words of
every l-tuple, agrees with the block-structure formula, and is constant over the l-tuples. Per-class list:
`out/addendum-v1/evidence/avoider_classes_oF.txt`.

| maximal o_F | classes | by H | representations | runs |
|---|---|---|---|---|
| 4 | 160 | 80 at H = 1, 80 at H = 4 | 3,120 | exactly the classes with all runs non-empty |
| 2 | 480 | 160 at H = 2, 320 at H = 3 | 8,000 | all have an empty run |
| 0 | **none** | | | |

**m4.** In `summary.json`, every `words_*` field, `avoider_words`, `nonrigid_avoider_words` and `literal_words` count
**labelled representations**, not raw words. `literal_words` counts sequence-run representations, which still repeat
literal words.

For one stratum H, the sequence-run 4-tuples number C(R+3,3)·5^R. That is per H, **before** multiplying by
C(H+3,3)·625. The verdict quotes only representation counts. The full field legend is in `ADDENDUM-v1.json`.
