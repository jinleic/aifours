# sun-coset7 lane summary v1 (math-1, transition 44: Sun 2006 Conjecture 1.2 at k = 7). PARTIAL

**Snapshot.** State at the freeze recorded in `evidence/lane-summary-v1.sha256`. Any later event (a smoke run, a Stage C run, a review outcome) goes into a new version.

**Bottom line.** All six residual classes are **OPEN**. This lane does not establish a k = 7 result. Correctness, novelty and significance are kept separate. Nothing here is claimed novel, and a search miss is not treated as novelty.

## 1. Claims, with exact scope

### Written claims (reviewed in part)

**Theorem R1(7)** — `README.md` 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1.

Setting: an arbitrary group, with 7 finite-index subgroups (they may coincide) whose left cosets are pairwise disjoint and whose pairwise index gcds are all ≤ 6. Any such counterexample falls into one of six classes:

| class | description |
|---|---|
| K7 | all 21 gcds equal 6 |
| K6.2\* | at most one index divisible by 5; six vertices in C = A_2 ∩ A_3; the remaining vertex d has 2 ∣ n_d and 3 ∤ n_d; the case where all six gcd(n_d, n_i) equal 2 is removed by D2 |
| K6.3 | as K6.2\*, except that d has 3 ∣ n_d and 2 ∤ n_d |
| K5.2\* | five vertices in C; the other two have e ≥ 2 and 3 ∤ n; the case C ∩ E = ∅ is removed by D2′ |
| K5.3 | five vertices in C; the other two have 3 ∣ n and 2 ∤ n |
| KII | exactly two indices divisible by 5: x ∈ A_2∖A_3 and y ∈ A_3∖A_2, with C = V∖{x, y} |

Imports:
- Zhu's Sun(3) and Sun(4);
- the accepted Sun(5), verdict 2cf02436…5301;
- the accepted Sun(6), verdict efe1d849…1e29;
- sun-coset5 Prop 4.5, used only as stated at proof-v4 line 67 with proof at lines 69–101, per the parent ruling.

Lemmas D2 and D2′ are in `rules-k7-v1.md` §3. M-S Lemma 4.6 and Menon's results are not used.

**Rules for computed removals:**

| file | sha256 | contents |
|---|---|---|
| `rules-k7-v1.md` | 77b9afec… | T, K, P, VFC, CAP |
| `rules-k7-addendum-v1.md` | fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066 | Lemma RPLP-k7, the CAP extension, per-universe CAP hypotheses, FH UNUSED, errata |
| `rules-k7-erratum-v1.md` | 75a61776871748a53191d4d3b6fe3d4435c6b8216929a9c60067b9f28d705560 | W1: L5 requires 2 ≤ \|T\|. W2: Farkas applies to the closed relaxation without TOT. |

**Review status:**
- Codex written review (`review/sun-coset7-written-v1-codex-v1.note.md`, 6c9872c4…08ea): AWF, with no FATAL or MAJOR findings and two MINOR ones, both repaired by the overlay. It accepted the reduction, D2/D2′/partial D3, the general rules and CAP at written scope. Its verdict: "a sound written bridge exists; no residual class is presently excluded".
- Claude written review: pending as of the last parent message.

### Exploratory computations (not accepted)

These were run with engine v1 (e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d). They are **not** accepted exclusions.

**Stage A** (receipt `evidence/stageA-RECEIPT.md` 90906aa60ac3026317af164069d2c0e22f825fc776cf789d4507d1445db4657c):
- X1: COMPLETE, 115 profiles, **0 survivors**. If confirmed, this removes K5.3, because every K5.3 configuration contains an X1 configuration.
- MSP45 and CORE5 controls: 0 survivors.
- Realisable controls: all survive.

**Stage B** (receipt `evidence/stageB-RECEIPT.md` e044a4eba6decd3c34222e577628993f762a51b67cc63e61853f97db7ca9e074):
- K52: COMPLETE, 171 profiles, **0 survivors**.
- KII: COMPLETE, 132 profiles, **0 survivors**; its 528 leaf orbits were all killed by RPLP.

**Pending:** the parent's separately authored independent checkers, writing `review/sun-coset7-stageA-independent-v1` and `review/sun-coset7-stageB-independent-v1`, and the reviews of both. A successful checker does not erase the late certificate format.

## 2. UNKNOWNs and NOT_STARTED items

- **Executed runs:** none is UNKNOWN; every Stage A and Stage B run was COMPLETE.
- **Stage C (K6.2\*, K6.3):** NOT_STARTED, on parent HOLD. The checkers own the slots, and a smoke run plus a separate GO are both required first.
- **K7 (Stage D):** not requested; not run.
- **Unexecuted files (NOT_STARTED, not scientific results):**
  - engine v2 (7ebb0bab…) and engine v3 (a26e6c68…) as Stage C engines;
  - admission_v1 (f58861d8…);
  - stageC_launch v1 (158c074d…), v2 (9955a8e0…, non-compliant: three processes) and v3 (4f00be28…);
  - smoke_v3_v1 (36ae890f…);
  - the current candidates, none executed: engine v4 41be7774aeb058ee02858a86a7c35799bee0ebdb8a465e90dd814feed18020b6, admission_v2 e0b6768aec643d160d4fb392b5598f6ada8ed47e22ab9ae2e469d1e4af0b52c0, stageC_launch_v4 a0d8369889213dc3f5cfc9fe3a798bf5d20cf0d8de3f0df7c50731be3adaedf4, smoke_v4_v2 9e862e76d2d03639bbab0d0e85c5690f44cb9193424006db3f7da91f1ee578f1 and terminal_probe_v1 cbefbdc42e448c9b4ab81fa54239b62ea710060b41f27d556998286d97449fe9.

## 3. Deviations (all disclosed earlier; none relabelled)

1. **Late certificate format.** CERT-FORMAT-k7-v1 (2c0e4830…1545) was frozen at 13:38:43. That is after Stage A (13:35:02–05) and after Stage B started (13:37:15). It is a late specification, never a retroactive preregistration.
2. **RPLP was not written down when it ran.** RPLP was absent from rules-k7-v1 when Stages A and B ran, and FINITE-COVERAGE §2.5 said it was "transcribed", which was false at freeze. It was written at 14:00:41 in rules-k7-addendum-v1 §A1.
3. **No per-node certificates.** Engine v1 stores no per-node certificates, contrary to the FINITE-COVERAGE §3 plan. A checker must re-walk the tree (CERT-FORMAT §2, §5).
4. **Wording errors.** README line 81 cites "§R" where it means §3. L5 omitted the condition 2 ≤ |T|, and the Farkas system was not specified (erratum W1, W2).
5. **Wrappers.** Stages A and B each ran one engine at a time, but inside the tool shell as `/usr/bin/time -l python3 … | grep …`. The receipts show those exact commands. Under the strict process count the parent applied later, the wrappers count as extra lane processes.
6. **Launch infrastructure went through several versions before any execution:**
   - engine v2 had no cooperative stop;
   - admission_v1 had a read-order race;
   - launcher v1 signalled a bare PID;
   - launcher v2 used three processes;
   - v3 left a terminal SIGTERM uncoerced and could wait forever after SIGTERM.

   The current versions are engine v4, admission_v2, stageC_launch_v4, smoke_v4_v2 and terminal_probe_v1. Engine v3/v4 is not a guard-only patch: the writer buffering and dual-key selection changed in v3 (`evidence/engine-v2-to-v3.diff`).
7. **Frontier wording.** My earlier phrase "exact frontier" is superseded. `profiles_done` with `profile_in_progress` is a completed-profile frontier, not an α-prefix frontier.
8. **Manifest self-entry.** In `evidence/lane-manifest-v1.sha256` (06648b07…4a08), line 34 is a self-entry hashed while the manifest was still being written; it is meaningless.
9. **Draft corrections.** Mis-targeted edits in unfrozen drafts were corrected before those drafts were frozen: in README-addendum-v2, CERT-FORMAT-k7-addendum-v1 and launchers v2/v3. No frozen or reported file was modified.
10. **Disk.** The parent relayed that its monitor recorded 11.985e9 free at 14:07:50, below the floor, recovering to 14.99e9 at 14:11:51. No lane computation was running then; no engine had run since 13:45:02.

## 4. Key hashes

- `evidence/freeze-v1.sha256`: c756076e34421b88d20b48d2a7f751a23a72fa966a2e3ca002611b2b032574b2
- `FINITE-COVERAGE-k7-v1.md`: cbad6fdd85d27181a235231f4219df059e7f41c653e0405b152a3b0b1843e0dc
- `README-addendum-v1.md`: 76056d8639f89b662f2014d5e199fe7c660bad4f3b305cb95ace3b5d1ae3193d
- `CERT-FORMAT-k7-addendum-v1.md`: e2b097be5a4f1eed35d8cdff93ea49b5b3a4f238fd674c80d2a27386f031a677
- Addenda v2, v3 and v4:
  - f7cd210f2c23f2c6207f39f5eb06e08a418f48bde46a4f34623520292c8f51f3
  - 8657c0d17d040a7403b19d7e4c367f5c91d18d42be77a7c576903b1ea319cfbc
  - 1ca4306caa770f4665168ec035440fab64d6fe2faecb04a9faf3f2bfff459ea3
- Every lane file: `evidence/lane-manifest-v1.sha256` 06648b07baa77f4a934e1c2f6f7b7af80df956d011638464d3e25d3cbae54a08. It has 68 file entries; ignore the self-entry on line 34.
