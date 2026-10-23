# ame46-lower46-parent-binding-v1 — parent binding check of the LOWER46 computer cases

Created 2026-10-17 13:18:25 PDT (host clock). Parent-side binding verification for the candidate partial theorem
"every AME(4,6) state has at least 46 non-zero coefficients" (lane physics/evidence/six-lane-20261016/ame46-support).
This is NOT the frozen minimum-support gate, and nothing here accepts the theorem.

## Question
The parent already re-verified the 18 pinned CNFs UNSAT. This directory checks that those CNFs encode the claimed
mathematics: (1) the deficit-profile list is complete; (2) each final-enumeration CNF is exactly the pinned code's
N-only base CNF for its (t, e, profile) followed by blocking clauses; (3) the blocking clauses are exactly the H-orbits
of the listed representatives; (4) every representative and every orbit image satisfies an independently written
N-only predicate; (5) an independent exhaustive enumeration of all N-sets satisfying that predicate matches the
blocked sets; (6) the four completion CNFs are well formed.

## Inputs (read-only snapshot)
/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/ame46-lower46-parent-inputs-v1
Pins: parent-pin-receipt.json in that snapshot. Pinned engine code is copied to pinned_code/ (SHA-verified) and is
imported ONLY to regenerate base clauses via SmallGen.build_gen. No SAT solver, no engine run()/write()/group().

## Rules followed
Writes only inside this directory (created with exist_ok=False; files opened with mode "x", README appended).
<=1 CPU, <=4 GiB RSS (measured with /usr/bin/time -l), <=1 GiB new data; native limits via ulimit -t / ulimit -f;
no kill/timeout wrappers. Host-clock timestamps.

## Checkpoints (host clock)
- 2026-10-17 13:18:25 PDT — directory created; plan: copy+pin code, write binding_check.py (items 1-4, 6) and enum_nsets.c (item 5).
- 2026-10-17 13:28:07 PDT — enum_nsets.c written and smoke-tested (dev outputs in enum/dev/, not evidence): it reproduces 144, 78192, 21600, 16, 64800 and 0 for the other nine profiles in <2 s each; (2,2)^4 at e=0 gives the 10 OA sets. binding_check.py drafted; next: run_enum.py, controls.py, official runs.
- 2026-10-17 13:37:17 PDT — run_enum.py attempt 1 failed at start (enum/final etc. did not exist; logs kept as logs/run_enum.attempt1.*; no outputs written). Attempt 2 13:31:22-13:36:58 PDT: enum-runs.json verdict PASS - 14 final runs complete with counts equal to the orbit sums; 26 coordinate orderings, 14 reversed-part relabellings, (2,2)^4 brute force e=0..8, 3 no-orth negatives all match; 38/42 single-pruning ablations complete and equal, 4 --no-dist-prune runs UNKNOWN at the 2e8-node budget. Driver peak RSS 903 MB. Parent IRC 13:29 disk guard noted (24.4 GB free, binding dir ~50 MB); parent IRC: item 6 may be limited to headers. Next: controls.py, then binding_check.py.

## Result (2026-10-17 13:39:46 PDT, host clock)
**Outcome: PASS. No discrepancy found.** `binding-result.json` (SHA-256 6589167609d6478d300371e6de388adcabe3a8d6e053ab157388d1cb0b4febf9) has verdict PASS with an empty
fail list. This binds the pinned CNFs to the N-only mathematics only; it does NOT accept the theorem.

1. **Profiles.** Independent brute-force partitions: h=6 gives 4 partitions and 35 multisets, 2 kept by Lemma 12;
   h=7 gives 3 and 15, 1 kept; h=8 gives 6 and 126, 7 kept. These equal the JSON lists for all five cases
   (2+2+2+1+7 = 14 profiles). No profile is dropped, extra or duplicated.
2. **14 final-enumeration CNFs.** Each header equals `p cnf nv (base + sum of orbit sizes)`. Base lines are
   byte-identical to the `SmallGen.build_gen` regeneration (9898, 20365, 9898, 20365, 9898, 20365, 20245, 47590,
   99334, 20125, 34315, 58365, 99400, 169790 lines). Every blocking clause is all-negative with exactly 2h+e distinct,
   strictly increasing point variables. There is no trailing data. Clauses are cut in JSON representative order.
3. **28 representatives.** Each BFS orbit equals its segment as a set, with no duplicate clause. Orbit sizes match
   the JSON and the r1 proof table, and all divide |H|. |H| from the product formula equals the JSON group_order for
   all 14 profiles (2592, 31104, 384, 165888, 165888, 384, 1152, 9216, 165888, 7962624).
4. **Independent predicate.** `failures()` returns [] on all 28 representatives and all 164,752 orbit images.
5. **Independent enumeration** (`enum_nsets.c`, no worker code). The set of all N satisfying the predicate equals the
   union of blocked orbits for every profile: 144, 78192, 21600, 16, 64800, and 0 for the other nine. Every
   enumerated set also passes `failures()`. All 14 final runs complete; none is UNKNOWN.
6. **Completion CNFs.** All four are well formed. Headers:
   - t30 (3,3) rep1: `p cnf 4062 10368`;
   - t28 (4,4) rep6: `p cnf 3080 7848`;
   - t28 (4,4) rep7: `p cnf 3080 7848`;
   - t28 (3,3,2)^4 rep0: `p cnf 3136 7992`.
   Independent allowed-point counts (606, 464, 464, 472) equal the JSON values. Encoding soundness is audited
   separately (parent completion binding).

**Controls.**
- `controls-result.json` (SHA-256 7b425d47bdeb7693789db7c92332cbd7bb5131e4b42945ac185c65a6fd04d3d7): PASS. 35 negatives are each rejected for the
  intended reason, and the 6 positive baselines pass.
  - The negatives cover JSON, profile and entry mutations, 14 single-edit CNF fixtures (kept with SHA-256 under
    controls/fixtures/), predicate inputs, non-H group maps, and completion fixtures.
- `enum-runs.json` (SHA-256 229f4d7edf8a121ce54879c04acd2a7cb39640c18ec1b48a48d97b772b469f4d): PASS.
  - The (2,2)^4 brute force for e=0..8 matches exactly: 10, 0, 0, 0, 116, 48, 120, 16, 1.
  - 26 coordinate reorderings and 14 reversed-part relabellings, mapped back, equal the final sets.
  - Of 42 single-pruning ablations, 38 complete and equal the final sets. 4 `--no-dist-prune` runs are UNKNOWN at
    the 2e8-node budget: (4,4), (4,2,2), (3,3,2)(2^4)^3 and (2^4)^4.
  - Without C4 there are extra sets: 60 for (3,3,2)^4, 48040 for (3,2,2)^4 at e=2, and 648 for (3,3)(2,2,2)^3 at e=2.
    Each extra set fails exactly ["orth"].

**Observation (not a defect).** Combinatorial orthogonality (L42-5) is load-bearing in the (28,0) (3,3,2)^4 profile
and in the (29,2) and (30,2) cases. Without it the N-only solution counts are 76 / 48040 / 648 instead of
16 / 0 / 0.

**Limits.**
- One process at a time, single-threaded.
- Peak RSS: run_enum driver 903,315,456 B; binding_check 477,872,128 B; controls 48,037,888 B; each enumerator
  process at most about 2.2 MB.
- CPU: run_enum 334 s user, binding_check 39 s, controls 2 s.
- Native limits: ulimit -t and ulimit -f for the drivers; RLIMIT_CPU 1800 s and RLIMIT_FSIZE 256 MiB for each
  enumerator process.
- New data is about 136 MB. Of that, 46 MB is development smoke output in enum/dev/, which is not evidence.
- Free disk stayed at or above 24.2 GB, above the parent's 12 GB floor.

**Scope and dependencies (not verified here).**
- Not verified here:
  - that the predicate's conditions follow from the written lemmas;
  - the normal-form and symmetry reduction, including transfer of exclusion along H;
  - the phase and completion exclusions;
  - the UNSAT proofs (parent replays).
- The independent enumeration establishes coverage without the CNF encoding or any solver: every N satisfying the
  predicate lies in an H-orbit of a listed representative. This holds subject to the enumerator's correctness, as
  supported by the controls above.

**Commands** (cwd = this directory; Python 3.13.9; Apple clang 17.0.0):
- `cc -O2 -Wall -Wextra -std=c11 -o enum_nsets enum_nsets.c`
- `ulimit -t 7200; ulimit -f 2097152; OMP_NUM_THREADS=1 /usr/bin/time -l python3.13 -B run_enum.py` → enum-runs.json
- the same wrapper with `controls.py` → controls-result.json, then with `binding_check.py` → binding-result.json.

**Files.**
- Code: binding_check.py, run_enum.py, controls.py, enum_nsets.c, enum_nsets.
- pinned_code/: SHA-verified copies, used only for base regeneration.
- Outputs: enum/final, orderings, reversed, ablations, bruteforce, no_orth; controls/fixtures/; logs/.
- 2026-10-17 13:39:46 PDT — binding-result.json PASS written 13:38:12; README result section added. Work complete.
