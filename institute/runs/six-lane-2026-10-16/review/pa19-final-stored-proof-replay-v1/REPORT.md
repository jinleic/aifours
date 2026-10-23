# PA19StoredProofReplay (TaskB): native parent drat-trim replay of retained M1 proofs + exposed-record re-solve status

Recorded 2026-10-18 PDT (host clock). This is evidence only. It is **not** a PA(19,8,6) theorem, M1, M2 or gate verdict.

## 1. Retained-proof replay: COMPLETE, 2976/2976 PASS
`RESULT.json` sha256 `5b6593e69ccab5740ae930d3a7d610c8f53397e6911c269a39d781eb4b8132d2`.

| Set | Denominator (audit-frozen) | PASS | UNKNOWN | not attempted |
|---|---|---|---|---|
| A2 route a (`cases19skel`) | 2490 | 2490 | 0 | 0 |
| E0 (`cases19q0`) | 486 | 486 | 0 | 0 |

- **Freeze.** The 2976 pairs come from the audit's `M1-manifest-compact.tsv` (route a, in TSV order) plus `run-v1/cases-E0.jsonl`, with no file discovery.
  - Each source receipt was sha-checked against the audit pin. All 2976 were READY; 0 were UNKNOWN at freeze.
  - `manifest-v1.jsonl` `3175656454733c39e217ef89816c67b837dbb2465411312dfe5d1d7455c62d54`; `freeze-v1.json` `6359092d29bec390c163a6d4cc21e9415bfa783467702c88b56492976a00a57e`.
- **Checker.** Parent drat-trim `a46c0c71…8e37`, run as `[DT, CNF, PROOF, -t, 1200]` directly on the lane files. Nothing was copied.
  - The checker sha was taken before and after every case, and at chunk start and end.
- **Strict predicate.** A case passes only if all of these hold:
  - rc 0 with self-exit;
  - after removing only CR, the s-lines are exactly `['s VERIFIED']`;
  - no fatal marker, including early EOF and clauses-less-than-expected;
  - exactly one `c parsing input formula` line, equal to the CNF p-line and to the R5 (V, C) for route a;
  - exactly one `c finished parsing, read N bytes from proof file`, with N equal to the proof size;
  - one binary-mode line;
  - CNF and proof sha256 equal to the pins both before and after the check, with (dev, ino, size, mtime) unchanged;
  - no guard fired.
- **Runs.** Chunk c001 ran 03:13:48–03:42:17: 2560 PASS. It deferred cleanly on token refusal at COUNT=0, during the parent list window. Chunk c002 ran 05:18:39–05:29:10: 416 PASS.
  - Both chunks: token wait 0 s, no signals, no RSS probe failures, no WARNING lines in any log.
  - Max child maxrss 292,896,768 B; sum of native time 2319.5 s; min free disk seen 13.16e9 B.
- **Finalize.** All 2976 raw-log hashes were re-verified, with 0 duplicates and 0 partial receipt tails.
- **Bindings** (`CROSSREF-v1.json` `d0558d7fa0ff830c75da588ebf049c4ddfb9630849d488447b76c0585025bbd5`):
  - Route a, 2490/2490: the replayed CNF sha (pre = post) and the parsed (V, C) equal the parent R5 rebuild (`2a14a1dc…`), reused by hash.
  - E0, 486/486: the replayed CNF sha (pre = post) equals the formula desk's `encode_q0` rebuild and its in-place stored hash, and the parsed (V, C) equals the rebuild (`e0-v1.jsonl` `5cd5cb6c…`, `e0-result-v1.json` `660c74c6…`). This E0 formula binding comes from TaskA's receipt and was joined here, not recomputed.
- **Controls** (`controls-v1/RESULT-controls.json` `2c65318c9178b7b9655eb0de79e4053484c9554161f16d885419278abd3902bf`), using the same check code as production:
  - C1, a tiny UNSAT CNF with a valid binary DRAT: PASS.
  - C2, a SAT CNF with a forged binary empty clause: rejected (rc 1, `s NOT VERIFIED`).
- **Scripts.**
  - `stored_replay_v1.py` `3bea2d91…5be3`: freeze and controls.
  - `stored_replay_v2.py` `b5c22bbc…6b51`: run and finalize. It differs from v1 only in gzip receipt storage (AST-checked).
  - `crossref_v1.py` `6b8b54fb…ea86`.

## 2. Exposed-record re-solve (737 records): NOT RUN, blocked at the transport controls
- **Plan.** `PLAN-resolve-v1.md` `0e1701fe…`. `resolve_v1.py` `9c6f0a15…` was put on HOLD. `resolve_v2.py` `b5700af1…c97b` passed source review.
- **Frozen plan** `resolve-plan-v1.jsonl` `d51b5555b0ef2c8f6a4b86443cd83d70239fbee4cc47077ec3cdac9ef7ec5e23`:
  - 737 records over 238 cases; the 545 M2-open records (46 cases) come first.
  - 15 c5 entries are plan-UNKNOWN only because my predicate required R5 status PASS. They are R5 PENDING with reason `lrat_check_only_direct_records`, and their sha and bytes are equal. Main approved fix (b) for exactly these 15.
- **v2 controls: MISMATCH** (`resolve-controls-v1/RESULT-controls.json` `7fc14391…3ad6`; no confirming rerun).
  - kissat refuses the proof path `/dev/fd/4` ("can not write proof"), and cadical reports it "not writable". Both check that the proof directory is writable.
  - The harness failed closed: the solver-CNF FIONREAD remainder equalled the full length, the relay carried 0 B, and RC1, RC2 and RC4 all came out UNKNOWN.
  - **RC3 empirically confirms the F-A hazard.** Parent drat-trim, fed half the CNF and 0 proof bytes, printed `early EOF`, `formula contains empty clause`, `s VERIFIED` and returned rc 0. My predicate rejected it.
- **Next step, approved in principle by Main, not done here.** Write `resolve_v3` with:
  - solver CNF and proof through owned 0-byte FIFOs;
  - a retained read end for FIONREAD;
  - a dummy write end on the proof FIFO until the solver is reaped;
  - the exact 15-entry R5 plan fix, with a plan v2 file and a byte-diff against plan v1.

  Then a source review, all four controls rerun once, and only then production.
- **`resolve_v3.py` placeholder.** It currently exists only as a byte-identical copy of `resolve_v2.py` (sha `b5700af1…`), with no v3 changes. Do not run it.
- **No exposed record was touched.** There is no re-solve receipt, and no claim that any streamed route has been replayed.

## 3. Process
- One driver at a time. Each case held one existing token (read-only flock), released between cases; COUNT and the guards were never written.
- Every launch used absolute argv containing the lane path, plus the parent drat-trim on lane paths. Each driver was detached (start_new_session) with an owned TMPDIR and nice 10.
- No SIGKILL, no `/tmp`, no Git, no CNF or proof copies. Desk allocation is about 6.3 MB.
- `LOG.md` holds all pins, launch times and deferrals.
