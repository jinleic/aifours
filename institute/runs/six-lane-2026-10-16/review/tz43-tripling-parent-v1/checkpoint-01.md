# Tz43TriplingAudit checkpoint 01 — 2026-10-18T00:45:54-07:00 (host clock)

This is auxiliary verification for the already-closed §4(3) FDGDD(3,4,5{18}). It is not a new problem slot.

## Done

**Desk created.** `review/tz43-tripling-parent-v1/` was created at 00:34 PT with `mkdir`, without `-p`.

**Master pinned.** `inputs/master_H_5_6.json` has SHA-256 `891337721265767e7136aee41a8e0da5f2219decec4216a62e8f6b70ac90db2c`. It is an exclusive copy, and the SHA was checked before the copy.

**Disk gate.**

| Time (PT) | Free bytes | Gate (12.2e9 + growth) | Action |
|---|---|---|---|
| 00:38 | 12,060,577,792 | Failed | Reported once to Main; no launch |
| 00:43 | 17,730,867,200 | Passed | Resumed |
| 00:43 | 17,699,848,192 | Passed | Matrix |

**Lemma note.** `lemma-v1.md`, SHA-256 `ff2569b3…337d`, contains Lemma 1 (zero-sum tripling), Lemma 2 (degree g/2) and Theorem 3 (any H(5,6,4,3) gives an FDGDD(3,4,5{18})). The only import is Hall's theorem.

**Generator.** `code/build_tripled_fdgdd.py`, SHA-256 `6c0db393…2d02`, is stdlib-only.
- A dry run in hashes-only mode and the write run produced identical SHAs.
- Positive certificate `fdgdd_5_18_konig_tripled.txt`: SHA-256 `5442b8c71612f9e021bdb990ea8931cf0919514bf4685f70d59dd80ce804ff12`, 700,931 bytes, 76,238 LF.
- Its first 14,588 lines (header, GROUPS and BLOCKS) are byte-identical to the original `3e22f502…a998`; both prefixes have SHA-256 `1887ddc9…c34b`. The files first differ at line 14591, inside the POINT 0 frames.
- Four mutation fixtures are in `fixtures/`. `build-manifest.json` has SHA-256 `0bab3d48…0cc4`.

**Checker matrix.** `code/run_checker_matrix.py`, SHA-256 `08c9ba07…4084`, produced `checker-matrix-v1.json`, SHA-256 `9ec69c1a…cd48`.
- 52 of 52 executions came out as expected: 8 positive and 44 rejections, each for its intended category.
- Every fixture's hash was checked before and after its runs, and all stderr was empty.
- The parent checker `0312f859…` and the Claude checker `2b2a7f19…` are unchanged.

**Reviews launched.** `tz43-tripling-codex-v1` and `tz43-tripling-claude-v1` were launched async from cwd `review/` after a fresh gate check.
- Codex prompt SHA-256 `168835b2…533e`, 10,713 bytes.
- Claude prompt SHA-256 `4dee3198…94d7`, 78,544 bytes.

## Not done or not claimed

- No SAT was rerun.
- The original certificate was not modified.
- No novelty claim is made, and no other new family claim is assumed.
- Acceptance waits for both reviews.
