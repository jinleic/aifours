# phys-1 MOQLS(8) Problem 16 — frozen lane plan v1

Recorded 2026-10-18T23:16:41-0700 (/bin/date). Lane `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8`. Contract `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/contract-v1.json` (sha256 `55baff0cf1ac1a4b0ab38b0eb1b1fa5a35a47c890f352b79dae4dfea919ffcaa`). Deadline 2026-10-22T22:56:33-07:00; no native launch at or after 2026-10-22T20:56:33-07:00; owned compute settled by 21:56:33.

## Target (unchanged)
Every set of five MOQLS(8) is classical (M(8) ≤ 4), or one exact non-classical five-set verified by two independent exact checkers. A complete proof needs A1–A11 of assembly r3 (`N8_ASSEMBLY.r3.md` 64d5d06b…8710), including two independently written encodings (GA and GB) for every exhaustive step.

## Frozen baseline
`review/RECONCILIATION-v1.json` sha256 `48c69cde1495b7d1bea6452fdbcbbf6fa28aefe4ed4782e85610bdafbb915890`:
- GA 16/18 parent-qualified (A4 12/12 direct; A8 4/6). Open: P1-B2.M2 (UNKNOWN, external SIGTERM at 408.5 s), P1-B3.M2 (UNKNOWN, CaDiCaL 3600 s self-limit; 614,606,348 proof bytes, no conflict).
- GB 1/18 (P1-B4). Seventeen GB inputs have identity only (GBBINDING d917203d…c673).
- Templates closed: 14/16 by GA, 1/16 by GB. A11 not started. **OPEN.** There is no n=8 claim, and none from the restricted K4/K5 data or partial counts.
- Inherited stops: `review/STOP-REGISTRY-v1.json` sha256 `c76e5c3184b8487e096086e1687be818264fc369a1c2eec0bec103295a24fa26`.

## Two separate ledgers per counted replay
1. **Mathematical coverage.** Exactly which bound formula identity (SHA256 and bytes) has a qualifying UNSAT, and which template it closes under U/T16/NF (GA) or the genuine bridge (GB).
2. **Transport checks.** Measured solver and checker CNF feeds, each with its SHA256 and byte count equal to the bound identity. The proof stream: bytes read from the FIFO (GA) or collected (GB), bytes delivered or fed, and the checker's own `read N bytes`, with the proof SHA256. Exact raw status lines, self-exits, settlement, and the parent audit (GB also needs the parent release).

A native `s VERIFIED` alone never counts: the truncate control produced it on a truncated stream.

## Attack and order (one pipeline at a time; at most 2 busy natives; lane RSS at most 11 GiB)
0. **New runner identities.** Old desks and drivers are never reused (their deadlines are stale, the paths are old and parent-owned).
   - GA `code/replay_v6.py` = reviewed `replay_v5e.py` (a60a924b…dbcdb) plus a constants/path-only diff.
   - GB `code/gb_staged_v6.py` = reviewed `gb_staged_v5.py` (a0e59977…a353a) plus a constants/path-only diff.
   - Old inputs are read-only. The new monitor is observer v3 (addendum v2 6ddac862…2f65); the rule is addendum v1.
   - Each diff gets a hostile Codex delta review before any native use. Then each identity runs its own native control suite, followed by a parent audit.
1. **Decisive pilot: GA P1-B3.M2** (bound sha256 `e4b55555…428d`, 137,665,032 B). It is the only remaining input where a full attempt exhausted its solver budget, so its tractability decides whether the direct 36-input route can close this round.
   - Limits: CaDiCaL 3.0.1 `-t 6600`; parent drat-trim a46c0c71 `-t 10440` (wall time from checker start, concurrent stream); driver backstop 10,680 s. Plus a bounded 120 s SIGTERM reap, so the maximum is at most the 10,800 s chunk cap.
   - Memory: reservation 9 GiB, desk stop at 9.5 GiB, lane cap 11 GiB.
   - Expected proof is about 1.1 GB at the observed 0.17 MB/s; drat-trim about 2.5 GB, CaDiCaL about 4 GB.
   - **PASS** (after parent audit): GA 17/18 and template P1-B3 closed for GA.
   - **UNKNOWN by budget:** B3 is not closable directly within one chunk. The next step is a written case-split proposal (no retry without a new GO).
   - **SAT:** a Boolean model of a relaxation, not a non-classical witness. The desk stops and the template stays open.
2. **GA P1-B2.M2** (`3f65ad96…04b0`): same runner and limits. Its sibling P1-B2.M4 needed 2,232 s.
3. **GB direct, 11 inputs.** Order: P0-B4, P0-B5, P2-C3, P2-C4, P1-B6, P0-B6, P0-B3, then P0-B1, P0-B2, P2-C2, P2-C1.
   - Kissat 4.0.4 `--time=3600`; staged transport; drat-trim `-t 6840` (so 3,600 + 120 + 6,840 + 2×120 ≤ 10,800).
   - Reservation 6 GiB. One gb item per PRE-EXEC, a parent GO for each, then a parent audit and release.
   - Worker timings, which do not count: 3–12 min each.
4. **GB strengthened, 6 inputs.** Feasibility is analysed first, because kissat proofs are about 1.7–12 MB/s and staged transport holds the whole proof in RAM. Options are a larger GB reservation or a CaDiCaL GB variant; a separate proposal and GO are needed.
5. **A11 dossier.** Only after 36/36: parent regeneration and audit, then hostile Codex and Claude assembly reviews, then a parent final verdict.

## Stop and settlement
- Stops are SIGTERM-only, to recorded owned child PIDs, with a bounded 120 s reap. Never SIGKILL, ulimit, or tool/subprocess timeouts; the solver/checker `-t` limits are self-budgets.
- A latched driver SIGTERM, scanner failure, helper survivor, floor or RSS breach, or deadline means UNKNOWN and no further launch.
- FIFOs, logs and receipts are never deleted. Each run is followed by an owned-process census, then a parent audit (GB: also the parent release record).

## Disk and IO
CNF and proof bytes never touch disk. Retained growth per run is under 10 MiB (logs, receipts). Launch requires fresh free ≥ 12.2e9 + 10 MiB and the observer v3 rule (last free ≥ 13.5e9 + 10 MiB, ≥25 samples over ≥290 s within 300 s, age ≤ 30 s, drop allowance). The in-flight floor is 12e9.
