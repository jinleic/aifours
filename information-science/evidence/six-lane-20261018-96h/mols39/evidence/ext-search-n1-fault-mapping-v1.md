# MOLS39 beta N1 fault cases and capture-audit reject cases: source/plan/oracle mapping v1 (2026-10-19T11:25:57-0700)

Worker ContinueCFR21c. WRITTEN ONLY, NOEXEC: nothing below was executed, imported, compiled, parsed or tested. The two new
harness sources are frozen bytes for a later parent decision; every case needs its own exact parent GO. Plan v5, its 20 jobs,
the 2 calibrations and all older files are unchanged. No audit record, release ledger or validator is created here.

Authority: review 16e0683425aab039ee6eee079fe2369a1a082708e8070659b75d685d6efc522c prerequisites 2 (four N1 fault cases) and
3 (seven audit rejection cases), `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-beta-successor4-admission_gate-codex-v1.prompt.stdout.txt`;
parent readiness 46459dc4e94a78ad072552b2b85b280f590c39d3f28bbfc58dd482c7cb39e01f (SOURCE_READY_RUNTIME_HOLD, not GO); prose
erratum ecbe507934cae7ee9faa9056122f774ce6331a44162039332730c85085782e89; governing fabe57ab; e441d858 withdrawn.

## 1. Existing consumer: NOT IMPLEMENTED (located before planning)
- No code in /Users/jinleic/repos/aifours writes `<item>.audit.json`, AUDITED_PASS/AUDITED_FAIL or a release record (read-only
  scout over all *.py plus direct reads). No planned audit directory exists yet (plan v5 audit_dir `mols39/mols39-ext-search-v4-audits`).
- `code/ext4_gate.py` 8d04c5ce7b9fdf3f42c5537bdf32c892b6c1af09e3e31096e41b2506597624fa lines 285-292 only CONSUME a finished
  canonical audit record (format/verdict AUDITED_PASS/settled/exit_code/output digests/64-hex receipt syntax). It never reads a
  receipt, a stdout/stderr capture or an actual exit, so it cannot reject any of the cases below.
- Parent audits to date are hand-written JSON (e.g. review/mols39-ext1-parent-audit-v1.json).
- The parent-only five-part release transaction is defined, contract-only, in
  `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10/evidence/owned_supervisor_v15-qualification-package-v8-plan-v1.md`
  (31f91759213ffc4685c430719d60e7a867ef7087082270b84f48044b3f2865db) lines 87-97: part 2 requires separately captured actual exit
  and complete stdout AND stderr; part 3 an admitted fixed oracle with actual exit and exact cause; line 97 says the parent owns
  the implementation. Its implementation is a recorded prerequisite, not present.
- Consequence: the seven audit cases, and the audit-rejection half of the four N1 cases, have NO consumer coverage. Section 5
  records the exact missing API contract and section 6 the case mapping. Nothing here claims that coverage.

## 2. Sources under test (actual pinned bytes, never copied)
- Entrypoint `code/ext4_entry_beta.py` c6c21b83b3190685b3559c2ae08ba345ab3c931a986026d7fcab586909c656eb: GO 23-57; ALGO_PATH/ALGO_SHA256
  65-66; `_load` 200-217 (actual-byte digest check, exec with VERIFIED_SOURCE_SHA256); `_main` 223-238 (`status = mod.main(args)`
  232, escaping BaseException -> `os._exit(94)` 233-235, invalid status -> 94 at 236-237, `sys.exit(status)` 238).
- Algorithm `code/ext4_beta.py` a319a4be1cc219a2de4c53211ac61cabc42bdc19d000f8bc740c6e4bc262b978: pin site 287 (INPUT_PIN_MISMATCH,
  'raw hash'); file publication 349-363 (exclusive create 352); deadline checks 364-365; stdout `print(...,flush=True)` 368;
  caught OSError 369-371 -> `os._exit(5 if deadline expired else 2)`; normal returns 372 (late -> 5) and 373.
- Superseded, sensitivity only: `code/ext3_entry_beta.py` 94c60282c01135ca108d8a1a894e03ff76c3074e5aa2701435aee584ee51c4f3 and
  `code/ext3_beta.py` 33200e9d3e80ccb71b635bcd18ffe7082b2677f254ca182f99fa78a82d463873, whose 369-371 RETURN 5/2, so entry 238
  `sys.exit` runs CPython finalization and its stdout flush (the N1 mechanism of review aba8c5c3).
- Job modelled: plan v5 254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731 B-BAD_PIN, lines 598-629 (exit 2,
  INPUT_PIN_MISMATCH, 'raw hash', outputs [result.json], --raw-sha256 70c8c2e5..., --m 0, --budget-s 240). Its placeholders
  resolve to --chunk-lo 0 --chunk-hi 1 (DATA maker `code/ext2_controls_final.py` line 141, gate derivation `code/ext4_gate.py`
  line 195). The fixture is a case-local exclusive copy of the exact DATA `neg6.raw` bytes (ext4_gate line 174 definition):
  b"0 0 0 0 0 0\n0 1 2 3 4 5\n", 24 B, sha256 32ae7f1897aa091c68d97a731ad912d4c93acf07bb09e45302be2f4bda8c2209.
- Interpreter: `/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python`
  sha256 7ecc1ecbf9daa9303c4bf502ff62ffdd9010ed5c08729d470ae9380c10ce1211 (the lane's supervised-child executable; every path
  component checked as a real directory, metadata only), flags -I -B.

## 3. Frozen harness sources (NOEXEC, exclusive create)
- Child `code/n1_fault_child_v1.py` sha256 c47c23ab2ac99f73b8f604a1abd751fdccb3f8a60f32f54ca8e355096d111757 (9431 B, 233 lines).
  It is labelled INSTRUMENTED RawIO fault. `FaultRaw` (91-174) is an io.RawIOBase over the real fd 1, the driver's capture pipe.
  Its plan:
  - Optional strict prefix (140-152): the first write call emits min(K, requested-1) bytes and returns that count.
  - Would-block (154-162): an optional real `time.sleep`, then `return None`. None is the RawIOBase/FileIO result of a full
    non-blocking pipe, so CPython's own BufferedWriter raises BlockingIOError (an OSError subclass) and keeps every unwritten
    byte pending in its buffer.
  - Interrupt (163-171): a complete pass-through write, then `raise KeyboardInterrupt`.
  - Every call after the planned fault passes through (135-139), so a later flush retry would succeed and be captured.
  sys.stdout is a REAL `io.TextIOWrapper(io.BufferedWriter(FaultRaw, buffer_size=8192), encoding="utf-8", errors="strict",
  newline="\n", line_buffering=False, write_through=False)` (212-213, installed at 224). These are CPython's text-layer settings for
  a piped stdout; only the raw layer and the explicit 8192 buffer differ from production. The B-BAD_PIN line (<8192 B, checked
  as `result_json_fits_buffer`) is therefore wholly pending in BufferedWriter when the fault fires.
  The child reads the ACTUAL entrypoint bytes anchored (205), checks their sha256 (209), compiles and execs them as __main__
  (221-228). The entrypoint then digest-checks and execs the actual algorithm itself. No clock, /bin/date, exit code or return
  value is faked. Child-only exits: 82 argv, 83 trace create, 84 entry read, 85 entry digest, 86 compile, 87 entrypoint
  returned, 88 trace write. A per-call JSONL trace (`fault-trace.jsonl`, O_EXCL) records each raw call. Its
  time.monotonic() values are informational instrumentation, not /bin/date evidence.
- Driver `code/n1_fault_driver_v1.py` sha256 83aeb70e25a64670fd4ce16b77219da25057807b723d13d5a6c54321ea4ce76b (29511 B, 672 lines). One case per invocation.
  - GO protocol: lines 33-66, the same 3-byte protocol as the entrypoints, with silent exit 97.
  - Case table: lines 102-111.
  - Pins before and after the case: the child (bound constant), PYTHON_APP, and the case's entrypoint and algorithm.
  - Exclusive dirs/files: `evidence/n1-fault-v1/<CASE>/{input,job}` (mode 700) and the fixture.
  - Bounded owned /bin/date helpers: lines 312 and 506/625.
  - The fault child: one invocation, `PYTHON_APP -I -B` in a new session (line 518), GO relayed at 537.
  - `_supervise` (352-403): complete stdout/stderr capture to EOF (stored <= 1 MiB each, seen-count kept), a 45 s child wall,
    at most one SIGTERM to the owned unreaped group, a 10 s grace, never SIGKILL, and the actual Popen/waitpid return code.
  - Settlement evidence: group-closure probe (552); bounded ps + lsof-cwd census (321-349, called at 561).
  - Outputs: exclusive stdout.bin/stderr.bin/census files with readback digests; one canonical receipt.json (659); and one stdout
    summary line (receipt path, sha256, inode, nlink, child return code).
  - Mechanical byte relations only: `_relations` 423-452.
  - Receipt `judgement` (655) = NONE. Driver exits: 0 recorded, 1 recorded with anomaly, 2 refused before child, 97 no GO.
- Bounds per invocation: GO wait <=120 s; each helper <=10 s + 5 s grace; child <=45 s + 10 s grace. Worst case is ~235 s
  (<300 s); the expected wall is 1-6 s. Stored outputs are a few MiB at most (<16 MiB). No SIGKILL, ulimit, tool timeout,
  deletion, autochain or network.

## 4. Cases and oracle (expected receipt observations)
Common to every case, all from receipt.json fields:
- Preconditions: pins_before/pins_after all match; fixture sha256 32ae7f18...; exactly one child trace start record with
  ppid == driver pid (relations.trace_start_ppid_is_driver); result.json is the only job entry, nlink 1, mode 644, <=8192 B,
  INPUT_PIN_MISMATCH/'raw hash', all-null metadata, program_sha256 = the case algorithm digest.
- Streams: stderr capture complete (eof true, over_cap false, seen == stored) and EMPTY; stdout capture complete.
- Settlement: child reaped, group EMPTY, census complete with no hit, no SIGTERM sent, no anomaly.
For C3/C4/A5, result.json must show INPUT_PIN_MISMATCH. INCOMPLETE_BUDGET there means the 2 s budget lapsed BEFORE file
publication. That outcome is INCONCLUSIVE_PRECONDITION (rerun only under a new versioned root and a new GO), never PASS or FAIL
of N1. A driver exit 2, child exits 82-88, any anomaly or any pin change are harness failures, never case evidence.

| case | role | impl | K | fault | sleep s | budget s | expected child exit | expected stdout vs result.json | expected trace actions (calls after plan) |
|---|---|---|---|---|---|---|---|---|---|
| C1 | REQUIRED empty x unexpired | ext4 | 0 | wouldblock | 0 | 240 | 2 (371) | empty, 0 LF | [return_None_wouldblock] (0) |
| C2 | REQUIRED strict prefix x unexpired | ext4 | 64 | wouldblock | 0 | 240 | 2 (371) | exactly first 64 B, 0 LF | [strict_prefix, return_None_wouldblock] (0) |
| C3 | REQUIRED empty x expired | ext4 | 0 | wouldblock | 3 | 2 | 5 (371) | empty, 0 LF | [return_None_wouldblock], observed sleep >= 3 s (0) |
| C4 | REQUIRED strict prefix x expired | ext4 | 64 | wouldblock | 3 | 2 | 5 (371) | exactly first 64 B, 0 LF | [strict_prefix, return_None_wouldblock], sleep >= 3 s (0) |
| B0 | POSITIVE baseline | ext4 | 0 | none | 0 | 240 | 2 (373) | equal, 1 LF | [pass_planned] (0) |
| A5 | audit evidence | ext4 | 0 | none | 3 | 2 | 5 (372) | equal, 1 LF | [pass_planned], sleep >= 3 s (0) |
| A94 | audit evidence | ext4 | 0 | interrupt | 0 | 240 | 94 (entry 233-235) | equal, 1 LF | [pass_then_raise_KeyboardInterrupt] (0) |
| S1 | SENSITIVITY, superseded | ext3 | 64 | wouldblock | 0 | 240 | 2 (ext3 371 + entry 238) | equal, via the retry | [strict_prefix, return_None_wouldblock, pass_after_plan] (1, requested-64 B) |
| S2 | SENSITIVITY, superseded | ext3 | 64 | wouldblock | 3 | 2 | 5 (ext3 370 + entry 238) | equal, via the late retry | as S1 plus sleep >= 3 s (1) |

What the four required cases establish together, if observed:
- Actual exit 2 when the caught-error deadline observation is unexpired, 5 when expired.
- No shutdown retry and no additional bytes: trace_calls_after_plan == 0 and stdout_len equals the bytes written before
  the fault (0 or 64).
- No second line: 0 LF.
- Preserved file evidence: the intact intended result.json.
- A later retry was possible: every post-plan call passes through. In C3/C4 the fault itself happens after the deadline,
  so any retry would be after the deadline.
S1/S2 are the non-vacuity controls. With identical instrumentation, code that returns normally DOES retry at shutdown and
succeed. Missing bytes in C1-C4 are thus attributable to ext4 line 371, not to the harness. B0 shows that the instrumentation
alone does not disturb a normal publication. A5/A94 provide genuine (instrumented) evidence for audit cases 5 and 6.
Expiry is a REAL deadline crossing: the sleep inside the faulting raw call starts after the beta `start`, and its observed
duration (>= 3 s) exceeds the 2 s budget. No clock is patched.

## 5. Missing parent consumer: exact API contract (parent-owned; part 2 + part 3 of the five-part release)
Input, bound by the parent (absolute paths + parent-recorded sha256, anchored capped reads):
- plan v5 + erratum, the plan item and its job spec (args/outputs/exit/status/reason);
- the invocation evidence: resolved argv, GO record, entrypoint/algorithm/input pins;
- the parent-observed actual exit (int; negative = signal);
- stdout and stderr capture records {present, path, sha256, bytes_seen, bytes_stored, eof, overflow, error};
- declared-output artifacts {path, sha256, bytes, ino, nlink};
- settlement {reaped, group_empty, census_complete, unresolved identities, signals};
- the owned /bin/date start/end values;
- the receipt {path, sha256} that the parent binds to the actual settled run.
The source may be a supervisor v15 receipt and sinks, or this driver's receipt (streams.*, child.returncode, artifacts.*, census.*).
Output: one decision {verdict AUDITED_PASS|AUDITED_FAIL, exact causes[]}. Only an AUDITED_PASS for a real plan item may become
the canonical ext-search-job-audit-v1 record the gate consumes. Fixture/negative decisions must be written OUTSIDE the plan audit
dir, and never as AUDITED_PASS records in it.
Predicates; each failure adds its exact cause, and AUDITED_PASS requires none:
- X1 EXIT_MISMATCH: actual exit != plan exit (B-BAD_PIN 2).
- X2 STDOUT_CAPTURE_MISSING | STDOUT_CAPTURE_INCOMPLETE (eof false, overflow, error, seen != stored) |
  STDOUT_NOT_EXACT_RESULT_LINE (stdout != result.json bytes, or not exactly one final LF).
- X3 STDERR_CAPTURE_MISSING | STDERR_CAPTURE_INCOMPLETE (same tests) | STDERR_NONEMPTY (these producers expect empty stderr).
- X4 ARTIFACT_SET_OR_DIGEST: the declared output set is exact, digests match, one link.
- X5 RESULT_SCHEMA: successor4 contract v3 (ad5bb631...) per-status schema for the planned status/reason.
- X6 UNSETTLED: not reaped, group not empty, census incomplete/hit, unresolved identity, or any stop signal sent.
- X7 PROVENANCE: the receipt/argv/pins/dates are not bound to the actual run, or the source is not the plan v5 pin.
Test mode, required to test the seven cases by their exact cause:
- The parent supplies the bundle's own receipt digest as the binding.
- A fixture bundle is mapped onto the B-BAD_PIN job spec, with its case-local job root and fixture path substituted.
- The expected exact cause must be the only cause unless the table says otherwise.

## 6. Case mapping to the missing consumer (expected: never AUDITED_PASS)
| audit case (review 16e) | bundle source | expected exact cause(s) |
|---|---|---|
| 1 missing stdout | GENUINE C1 (exit 2 = the intended exit; intended file) | X2 STDOUT_NOT_EXACT_RESULT_LINE only |
| 2 partial stdout | GENUINE C2 (exit 2; 64-byte strict prefix) | X2 STDOUT_NOT_EXACT_RESULT_LINE only |
| 3 missing stderr capture | DERIVED from genuine B0: stderr capture record and stderr.bin omitted in a new derived bundle dir | X3 STDERR_CAPTURE_MISSING only |
| 4 partial stderr capture | DERIVED from B0: stderr record eof=false, or bytes_seen > bytes_stored | X3 STDERR_CAPTURE_INCOMPLETE only |
| 5 intended-looking, actual exit 5 | GENUINE A5 (alternatively DERIVED B0 with actual exit 5) | X1 EXIT_MISMATCH only |
| 6 intended-looking, actual exit 94 | GENUINE A94 (alternatively DERIVED B0 with actual exit 94) | X1 EXIT_MISMATCH only |
| 7 intended-looking, actual exit 120 | DERIVED B0 with actual exit 120 | X1 EXIT_MISMATCH only |
| N1 C1/C2 | genuine | as audit cases 1/2 |
| N1 C3/C4 | genuine | X1 EXIT_MISMATCH + X2 STDOUT_NOT_EXACT_RESULT_LINE |
| B0 positive | genuine | no cause: the consumer must report all predicates satisfied (test mode only, no real audit record) |
| S1/S2 | genuine, superseded source | S1: X7 (ext3 program_sha256/pins), otherwise intended-looking; S2: X1 + X7 |

Derived bundles are new exclusive files built from copies of genuine B0 evidence. They are labelled SYNTHETIC NEGATIVE
FIXTURE, and originals are never edited. They are consumer tests, not run evidence.
No derivation tool is written here. The parent's consumer test owns their construction under the stated mutation.
[INFERENCE from source] The pinned ext4 B-BAD_PIN path cannot emit 120: after a successful line-368 flush, no stdout/stderr
bytes remain pending; the caught-OSError branch os._exits; every other escape is quiet 94. So case 7 is DERIVED only.
S1 shows why the source pin matters: superseded ext3 can produce a complete, intended-looking line and exit 2 by a shutdown retry.

## 7. Run plan (each line needs its own exact parent GO; no autochain, polling or retry)
Command, run by the parent, which also captures the DRIVER's actual exit and complete stdout/stderr (five-part part 2):
`printf 'GO\n' | /opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python -I -B /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/n1_fault_driver_v1.py --case CASE`
Suggested order: B0, C1, C2, C3, C4 (required), then S1, S2 (non-vacuity), then A5, A94 (optional). Each run writes only
`/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/n1-fault-v1/CASE/`. An existing CASE dir refuses (exit 2), so a rerun needs a new versioned driver/root.
Machine-readable copy: `evidence/ext-search-n1-fault-plan-v1.json`. Metadata check: `evidence/ext-search-n1-fault-metadata-v1.json`.

## 8. Claim boundary
- The fault is INSTRUMENTED at the RawIO API layer under the real CPython 3.14.3 BufferedWriter/TextIOWrapper. It is not a
  kernel-generated EAGAIN/EPIPE. It is one interpreter build, one input, and single runs.
- Observed C1-C4 would establish the ext4 line-371 behaviour for this fault class. They would not establish completion by the
  deadline, every OS failure mode, supervisor qualification (prerequisite 1), or any consumer coverage (sections 1, 5).
- No scientific status changes: exact-anchor Lemma U scoped acceptance and corrected R1 stand; both extension questions UNKNOWN;
  six MOLS(39) OPEN.
