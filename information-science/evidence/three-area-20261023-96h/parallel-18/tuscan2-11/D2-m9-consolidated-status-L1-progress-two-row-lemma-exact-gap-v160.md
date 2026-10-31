# Original Tuscan-2(11), entire m = 9 distance-two branch, part 47: consolidated status after v152–v159, a two-row face lemma, and the exact remaining L1 gap

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It consolidates v151 and v152–v159 and adds one small lemma (§2). Every pin below was derived live with `shasum -a 256` at Mon Oct 26 22:46:32 PDT 2026.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. What is closed in the m = 9 branch (all WRITTEN, all unreviewed)

**Earlier cells.**
- **L2 (k = 3)**: every cell is closed. The consolidation and pins of v110–v150 are in v151 (`07df7c7bb200e66541cb4d5ffeaae0a2f206d0a712d1743054c3aa67356313ff`).
- **L4-B**: closed (v113).
- **L1 types 5 and 6**: closed (v118, `5987287dda6ca7a1446058e3c045a25eea00d855953ffbe37b73d28f8594306d`).

**L1 face groups.** The face-group table, anatomy and the counts (K-w) and (K-S) are in v152 (`62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`). The L1 type table is in v117 (`77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`).

**Types 4 and 10 are closed.**
- v153 (`66dcb38b10aad43f86c32f09d2f47f11ba2929163fd208d7cc5bbab29e7902b0`): type 10 with r2 = 3.
- v154 (`31797e84f74a22b11243515d606373b7388bc885280ae9f55b609d1a5896b7fa`): type 4 with r2 = 3.
- v155 (`660996ba8be146a445353c9bbb865b1fc880793ccc94bc94f9c8f2d704a1a72f`): type 10 with r2 = 2, and type 4 with r2 = 2 by the row-reversal mirror.
- r2 = 4 is excluded by (K-S), and r2 = 1 by F0.

**Types 3 and 9 (mirror pair).**
- r2 = 2 is closed by v156 (`68723267d48a313351e1cecdce398fb5a2b1c3e34b41ed30f16eaf1c49747828`).
- r2 = 3 is reduced:
  - v158 (`935a59a9c54429e9a6d2fb5dc827e38d2a010e882038fb605c9fe2556c5eb204`) leaves only λ = 14;
  - v159 (`3bfe0cbb24972d90c9b77d4d69272a1d5ae4aececb00d1c8ab0369d741259d54`) closes λ = 14 with u ≤ 3.

**Type 7 (self-mirror).** r2 = 2 is closed by v157 (`458dce9de731858686a408c773870eb593a854937e2f5b1f46ac08bb40c724f2`).

**Mirror pairs.** Row reversal pairs the types as (1, 11), (2, 12), (3, 9) and (4, 10); types 7 and 8 are self-mirror. The rotation computations are in v155 §5 and v156 §3. For (2, 12):
- the mirror of type 2's rotation (T, Λ+, t1, Λ−, t3, t2) is (T, t2, t3, Λ−, t1, Λ+);
- renaming Λ+ ↔ Λ− and t1 ↔ t2 gives (T, t1, t3, Λ+, t2, Λ−), which is type 12.

## 2. A two-row face lemma (new, WRITTEN)

**Lemma 2R.** Let F be a face with exactly two rows. Every label whose cut lies in F has exactly one passage in F, namely its cut (identity (I) of v114: passages = r_F − 1 = 1).

So an 11-window of F that carries all 11 labels contains both cut positions of F. Since these are 10 apart, the window is a row of F.

**Corollary 2R.** Suppose F2 has two rows, and some F1-row R consists of interior vertices of one G2-thread. Then R is impossible.
- R's vertices pass consecutively in F2, so they form an F2-window carrying all labels.
- By Lemma 2R that window is an F2-row.
- Then the two end vertices of R, which sit on F1-cuts, also sit on F2-cuts. Each of their labels would have two cuts, against (C).

**Application.**
- **Type 12 with r2 = 2:**
  - If ℓ1 ≥ u + 11, then R1 = t1[u..u+10] would be such a row. ℓ1 = u + 10 puts b3 on the cut 20. Hence **ℓ1 ≤ u + 9**.
  - No F1-row lies inside the t3-run.
- **Type 2 with r2 = 2 (mirror):** ℓ2 ≤ u + 9, and no F1-row lies inside the t3-run.

## 3. The exact remaining m = 9 gap

The open cells are all L1, and v152's restrictions apply throughout.

| Types | Open part |
|---|---|
| 3 and 9 | r2 = 3 with λ = 14 and u ≥ 4; r2 = 4 |
| 7 | r2 ∈ {3, 4} |
| 2 and 12 | r2 ∈ {2, 3, 4}; when r2 = 2, also Corollary 2R |
| 1 and 11 | r1 ∈ {3, 4, 5, 6} (K-w) |
| 8 | r1 ∈ {3, 4, 5, 6} (K-w), r1 ≥ 3 |

**Statement scope.** The support-9 statement ("every eligible original T2(11) array with support 9 is impossible") is **not** made. Every m in 10..110 is unresolved, so the original Tuscan-2(11) target is UNMET: no literal table and no all-array contradiction.

## 4. Process notes

- Checkpoints 202 and 203 each had a first unpinned draft that carried an estimated time instead of `/bin/date` output. Both were replaced before any pin, and each file records this in a `clock_note`.
- No other process deviation in this stretch.
- Every pin above is live.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
