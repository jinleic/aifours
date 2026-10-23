# PA19 exposed-record native re-solve + parent drat-trim replay: frozen plan v1 (PA19StoredProofReplay)

Status: **PLAN ONLY. No re-solve child has been started.** Launch needs the parent source-review PASS of `resolve_v1.py`.
Kept separate from the retained-file route-a/E0 replay (`stored_replay_v2.py`). Not a theorem, gate, M1 or M2 verdict.

## Scope: exactly 737 chosen records (238 cases), nothing else
Source: the bridge census `pa19-final-bridge-v1/delivery-exposure-census-v1.json` (`baf3cee6…`), mapped onto the audit's chosen records (`pa19-final-receipts-v1/run-v1/cases-A2.jsonl` `d2471123…`, `split-index-map.jsonl.gz` `8812e2af…`). For split cases, only chosen records with rev 5 or rev 9 are selected. Their index sums must equal the census `indices_without_positive_evidence`, otherwise the plan aborts.

| Route | Records | Solver | Recorded limits |
|---|---|---|---|
| b rev5 (ms08 170, ms09 28) | 198 | kissat | `--time=600`, drat-trim `-t 1800` |
| c5 rev5 (ms06) | 37 | kissat | 32 at `--time=3600`/`-t 4800`; 5 at `--time=600`/`-t 1800` |
| d `ms01_s03171/f01788_r3` | 1 | cadical | `-t 600`, drat-trim `-t 1200` |
| e `ms06_s00150` rev9 batches (49,902 indices) | 500 | kissat | `--time=600`/`-t 1200` |
| e `ms09_s00010/batch_04300_04399_r3` (100 indices) | 1 | cadical | `-t 600`/`-t 1200` |

The batches are 500 runs, not 49,902.

## Priority order
1. **M2-open first.** These are the overlap entries whose m2 status starts with `OPEN` (`delivery-exposure-m2-overlap-v1.json` `007e417d…`): 545 records in 46 cases.
   - 25 b, 19 c5 (4 of them bigmem), 500 e rev9, 1 e r3.
   - Recorded solve time 3,464 s; recorded check time 4,522 s.
2. **Then the other exposed records:** 192.
   - 173 b, 18 c5 (3 bigmem), 1 d.
   - Recorded solve time 1,638 s; recorded check time 2,069 s.

Within each group the order is the audit case order, then the audit record order. Records whose recorded proof is over 300 MiB are moved to the end of their group. There are 7 such records: ms06_s00183 1.31 GB, s00182 1.06 GB, s00148 685 MB, s00187 579 MB (all M2-open), and s00062, s00040, s00091 (other).

The counts above are a preview. They come from the same pinned inputs, read in the agent kernel. The binding plan file is `resolve-plan-v1.jsonl`, written by `resolve_v1.py plan` under one token, with its sha reported.

## CNF bytes (in driver memory only; never written)
- **b and c5 (235 records).** The pass-1 file `cases19skel/cnf/<tag>.cnf` is read once, O_RDONLY. Its sha and length must equal:
  - the parent R5 rebuild (`pa19-cnf-binding-v1` `2a14a1dc…`, per_tag PASS);
  - the record's `cnf_sha256`/`cnf_bytes`;
  - and the stat must be unchanged across the read.

  c5 records rebuilt `encode_skel.build(spec)` in memory with `cnf_matches_pass1_sha` true, so they share this R5 binding.
- **Split records (502).** The CNF is built in memory with the sha-pinned lane encoders, executed from verified bytes: `encode_e1` `2a76e8bd…`, `encode_skel` `dd871522…`, `encode_full` `33a49879…`, `encode_partbatch` `ee4496cc…`.
  - Inputs:
    - the pinned spec (R5 `spec_sha256`: ms01_s03171 `db23f8d0…`, ms06_s00150 `ffef5575…`, ms09_s00010 `56a11899…`);
    - the pinned `ext.json` (audit split-map sha: `5a4f2b72…`, `9b794c0c…`, `5bd88696…`);
    - the record's exact index or indices. For the batch `_r3`, the indices must also equal the original record's.
  - Serialization uses `cnf_bytes_of`, which is checked at start to be text-identical to `stream_check5` (`3060a9c0…`) and `stream_check9` (`d3bcda4c…`).
  - The built sha and length must equal the record.
  - This is in-memory construction for delivery only. Parent formula binding of the 247 un-replayed ms06_s00150 batches and the two r3 leaves stays with the formula desk. The final receipts list the built sha so it can be cross-checked against that desk's parent hashes.

## Native transport and measured delivery
Anonymous pipes only; there are no FIFOs and no files.
- **Checker** (parent drat-trim `a46c0c71…`): `[DT, /dev/fd/3, -i, -t T]`. fd 3 is the CNF pipe; stdin is the proof pipe. This is the moqls8-tested binary stdin mode.
- **Solver**, exactly as recorded:
  - kissat (`05d6f3e9…`): `-q -f --seed=1 --time=L /dev/fd/3 /dev/fd/4`;
  - cadical (`601c9fa8…`): `-q -t L /dev/fd/3 /dev/fd/4`.
- Executables are invoked through an absolute path that contains the lane path (`L/../…/<real path>`), so watchdog4 counts them. Realpaths and shas are checked pre and post.

**Delivery is measured for both children:**
- **CNF.** Each writer thread counts bytes only after `write` returns, then closes its end.
- **Remainder.** The driver keeps a duplicate read end of each CNF pipe. After the child has exited and the writer is done, `FIONREAD` must be 0. Any bytes drained afterwards count as undelivered.
- **Proof.** A relay hashes and counts the solver's proof (read to EOF) and writes it to drat-trim's stdin, counting after each write returns.
- **Checker self-report.** drat-trim must print:
  - exactly one `c parsing input formula with V variables and C clauses`, equal to the CNF p-line;
  - exactly one `c reading proof from stdin`;
  - exactly one `c finished parsing, read N bytes from proof file`, with N equal to the relayed bytes. That line is unreachable on the early-EOF path.

## PASS predicate (fail-closed; anything else is UNKNOWN)
A record passes only if all of these hold:
- The built CNF equals the record (and R5).
- The solver exits by itself with rc 20. Its s-lines are a subset of `['s UNSATISFIABLE']`, at most one.
- Both CNF deliveries are complete.
- The relay reached EOF with bytes_in == bytes_out > 0, no error, and stdin closed.
- The checker exits by itself with rc 0, and its CR-stripped s-lines are exactly `['s VERIFIED']`.
- None of the fatal markers appears: NOT VERIFIED, TIMEOUT, MEMOUT, ERROR, early EOF, clauses less than expected, wrong binary prefix, trivial UNSAT, DERIVATION, conflict claimed, failed at proof line.
- The three self-report lines above match.
- Executable shas pre and post equal their pins.
- No guard fired.

Outcomes outside PASS:
- **rc 10 → SAT-CLAIM.** The model stays in the raw log and the chunk stops.
- **Proof determinism** (re-solve proof sha equal to the recorded `drat_sha256`) is reported but not required.
- **No retries.** Any index that already has a receipt line is never re-run.

## Guards and resources
- **Lane locks.**
  - One existing lane token per record, held from CNF build to post-hash. It is a read-only fd with flock; COUNT and token files are never written. The wait is bounded at ≤ 1800 s. One token covers the solver plus the checker, i.e. 2 busy processes, as in lane stage accounting.
  - Records over 300 MiB also take the lane `bigmem` lock, by read-only flock with a bounded wait.
- **Time.**
  - Hard wall T + 120 s.
  - On a guard: SIGTERM, a 30 s bounded wait, then quarantine with the token held. No SIGKILL.
  - The solver is SIGTERMed if the checker exits first.
- **Memory.** Solver + checker + driver resident < 3.5 GiB, sampled every 0.2 s. The 7 bigmem proofs may exceed this and end UNKNOWN. Reference point: the rev12 s00235 run, 622 MB DRAT → drat-trim 845 MB sampled.
- **Disk.** Free space ≥ 12e9 B continuously, and ≥ 12,334,217,728 + 20 MiB at admission.
- **Logs and desk.** Raw logs ≤ 2 MiB per child per record. Desk allocation ≤ 20e6 B, shared with the stored replay.
- **Schedule.** Chunks ≤ 10,800 s. Nothing is admitted that cannot finish by 18:00 PDT. `STOP-RESOLVE` stops a chunk between records.
- **Receipts.** Append-only gzip, with a sync flush + fsync per line and an intent line before each record. Checkpoints at least every 15 min.

## Controls (run once after review PASS, before production; same `resolve_one` path; in-memory CNFs)
- **RC1:** kissat on a tiny UNSAT formula → PASS.
- **RC2:** kissat on a tiny SAT formula → SAT-CLAIM.
- **RC3:** kissat on the tiny UNSAT formula, with the driver deliberately feeding the checker only half the CNF (the F-A early-EOF hazard) → must be rejected, with `checker CNF delivery incomplete` among the reasons.
- **RC4:** cadical on the tiny UNSAT formula → PASS.

## Time estimate
Recorded sums are 5,102 s solve and 6,591 s check. With streaming, the expected wall is about 2–2.5 h plus waits, for the M2-open group first. The c5 bigmem records dominate the tail.

## Not claimed / open for parent decision
- No mathematical acceptance and no M2 closure: replayed records only re-certify the exposed M1 leaves.
- **Parent decision 1:** acceptance of in-memory encoder construction for the 502 split records. Formula binding is the formula desk's job.
- **Parent decision 2:** use of the lane `bigmem` lock.
- **Parent decision 3:** the through-lane exec paths for watchdog visibility.
