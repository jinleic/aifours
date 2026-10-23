# Lemma U certificate — format and launch contract v2 (2026-10-19T07:35:22-0700, ContinueCFR21)

Status: normative contract of the v3 successor package (written only; nothing has been run under it).
Supersedes, for that package, format v1 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-format-v1.md (sha256 1b6537a42dd936a16337c58fd65039ece9e150099e2b8a297ab21d206dfd6ba0). The certified claim, the certificate schema and
checks 0-6 are unchanged from format v1 and from the spec /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1.md (sha256 b151a61f9f84ccf8a0b261bfeb056ff6a9db58fc99e516b7562e1cea98f57df2) with its erratum
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1-erratum1.md (sha256 beca7d3330230672e19ea5561f1844e721496ec7283e07c69a76672d62fb9135). The independently written checker /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py
(sha256 e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0) implements checks 0-6 and is used unchanged (byte-identical).
Review answered: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-certificate-source-codex-v1.prompt.stdout.txt (sha256 ea5f29a7d48fbcfae81c8fb6c6ffc78d208234afd521755faa30e8291b8c2a10), verdict HOLD. The per-finding map is a separate file.

## 1. Raw grammar G1 (normative for the producer, the generator and the checker)
G1 equals the parse of the accepted checker (cert_checker.py, function parse_anchor), written out:
1. The raw file is read once. Its sha256 and its parse use the same bytes. Size cap: 1,048,576 bytes.
2. lines := raw.split(b"\n"). If the last element is b"", it is dropped (so at most one final newline is absorbed).
3. For each line: tokens := line.split() (Python bytes.split with no argument, i.e. runs of ASCII whitespace
   b" \t\n\r\x0b\x0c"; a trailing CR is therefore discarded). A line with no token is rejected (this rejects
   blank rows, including a second final newline).
4. A token is accepted iff, after removing ONE optional leading b"+" or b"-", the rest is non-empty and consists of
   ASCII digits 0-9 only (bytes.isdigit). Its value is int(token). Python's limit on integer string length rejects
   over-long tokens. Underscores, non-ASCII digits and empty tokens are rejected.
5. All rows must have the same length n, and the number of rows is k. Entries are reduced mod n.
The producer and the generator reject a G1 violation as BAD_INPUT. The checker reports it as check 1 (unchanged).

## 2. Limits
- Anchor raw <= 1,048,576 bytes and certificate <= 8,388,608 bytes. The entrypoints enforce these on their input
  flags (section 7). The producer and generator also enforce them on the bytes they read.
- Producer work limits: 2 <= k <= 12, n <= 120 with n = 3q and q % 3 != 0, gauged dimension dim <= 8.
  Beyond these the producer stops with WORK_LIMIT and writes no certificate.
- Every program has a finite positive self-budget: --budget-s must be finite with 0 < S <= 280 (default 240),
  except the checker, which keeps its accepted budget rule (finite, positive). Every supervisor additionally enforces
  its own wall limit.

## 3. Certificate (schema unchanged from format v1 section 3)
Canonical bytes are a producer obligation: json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n", ASCII. The
checker does not enforce canonical bytes; its cert_sha256 binds the exact bytes it read. The expectations program v3
verifies canonical bytes for every certificate artifact: both producer outputs and all mutants. (Review m2: the
"producer-only plus expectation verification" option.)

## 4. Checks 0-6: unchanged (format v1 section 4)
The checker reports reason strings as "check N: <text>". Its successful reason is "checks 0-6 passed". The exact
strings used by the preregistered controls are listed in the run plan v3 (exact strings or full-match regexes).

## 5. Program interfaces (each is run only through its entrypoint, section 7)
Outputs are plain file names created exclusively in the job root, which is the entrypoint's working directory.
Every program writes result.json, whose bytes equal its printed stdout line plus "\n". result.json is written last.
A. Producer v2 (code/lemmaU_cert_producer_v2.py)
   - Args (exactly these flags, each at most once, "--flag value" form only): --anchor RAW (required),
     --anchor-sha256 HEX (required), --budget-s S (optional).
   - Outputs: cert.json (only when status is OK) and result.json.
   - result.json keys (exactly): status, reason, n, q, k, U, J, rank, dim, rainbow_count, alpha_hat_idx,
     minus_alpha_hat_idx, cert_sha256, anchor_sha256, producer_sha256, wall_s.
   - Serialisation: canonical (sort_keys, separators (",", ":")). Fields that are not established are null.
   - Status and exit codes: OK 0; BAD_INPUT 2; INPUT_PIN_MISMATCH 2; IO_ERROR 2; NOT_DM 3; FIBRE_SIZE 3;
     SELF_CHECK 4; INTERNAL_ERROR 4; BUDGET_EXCEEDED 5; WORK_LIMIT 6.
B. Checker (review/cert_checker/cert_checker.py, unchanged)
   - Args: --anchor RAW --anchor-sha256 HEX --cert CERT --out result.json [--budget-s S].
   - Output result.json = json.dumps(obj, separators=(",", ":")) + "\n" with its fixed key order (OUT_KEYS).
   - Exit codes: VALID 0, INVALID 1, ERROR 2.
C. Mutant generator v3 (code/make_cert_mutants_v3.py)
   - Args: --cert CERT --cert-sha256 HEX --anchor RAW --anchor-sha256 HEX --other-sha256 HEX
     --mut-anchor-sha256 HEX [--budget-s S].
   - Outputs: nc0_identity ... nc10_basis_scale (".cert.json"), manifest.json and result.json, all canonical.
   - result.json keys: status, reason, mutants, manifest_sha256, source_cert_sha256, generator_sha256, wall_s.
   - Exit codes: OK 0; BAD_INPUT/INPUT_PIN_MISMATCH/IO_ERROR 2; INTERNAL_ERROR 4; BUDGET_EXCEEDED 5.
   - manifest.json keys: format ("lemmaU-cert-mutants-v2"), source_cert_sha256, anchor_sha256, generator_sha256,
     mutants. mutants is a list of objects with keys item, file, sha256, intended_verdict,
     intended_first_failed_check and detail (integers only, per mutant: see the generator docstring).
D. Expectations v3 (code/check_cert_runs_v3.py)
   - Args: --plan PLAN --plan-sha256 HEX --self ITEM [--budget-s S].
   - Output: result.json, canonical, with keys status, reason, self, plan_sha256, evaluated_prefix,
     all_as_expected, claim, qualified, pin_mismatches, items, wall_s.
   - Exit codes: 0 iff the evaluation succeeded and is as expected. For the final item this also requires
     qualified = true. 1 on any deviation; 2 on input or plan error; 5 on budget.

## 6. Claim predicate (exact; evaluated only once CHK-anchor is in the audited prefix, otherwise "UNEVALUATED")
The CHK-anchor result.json must equal, field by field with typed equality, verdict "VALID", first_failed_check
null, reason "checks 0-6 passed", anchor_sha256 = 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a, n 39,
q 13, k 6, U 190, J 195, dim 5, rank 185, rainbow_count 2, alpha_hat_listed true, minus_alpha_hat_listed true and
rainbow_is_pm_alpha_hat true. In addition, cert_sha256 must equal the sha256 of the actual bytes of PROD-anchor's
cert.json, read by the expectations program, and wall_s must be a finite non-negative float.
qualified = (self is the final EXP item) and every prefix item is as expected and the claim predicate is true and no
pin mismatch.

## 7. Entrypoint protocol v2 (code/go_entry_<role>_v2.py, one template)
1. Before GO, the entrypoint only imports os, sys, time and select, and reads stdin. It consumes at most 3 bytes with
   os.read on fd 0, waiting with select at most 120 s from entrypoint start. Unless those bytes are exactly
   b"GO\n", it exits at once with os._exit(97): no output and no file. EOF, other bytes, a timeout and a select
   error all count as no GO. After the 3 bytes, a zero-timeout probe that finds any further byte available also
   counts as no GO (EOF is fine).
2. After GO, argv must start with "--job-root", ABS. ABS must be absolute and normalised (no "", "." or ".."
   components). It is opened component by component with O_RDONLY|O_DIRECTORY|O_NOFOLLOW relative to the previous
   directory fd. The final directory must be owned by the current uid and must not be group- or world-writable. The
   entrypoint then fchdir()s into it. Failure: one JSON line {"status":"ENTRY_JOB_ROOT_REJECTED",...}, exit 93.
3. Argument rules per role. For the checker, the output flag must be exactly "--out" "result.json". The other roles
   have no output flags. Every input-path flag (--anchor, --cert, --plan) must name an absolute path to a regular
   file within the section 2 size caps; --plan has a 4,194,304-byte cap. Failure: ENTRY_ARGUMENT_REJECTED, exit 92.
4. Load. The algorithm file is read inside the error handler with a 1,048,576-byte cap and its sha256 is checked
   against the pinned constant. Mismatch: ENTRY_ALGORITHM_PIN_MISMATCH, exit 96. Read, compile or exec failure:
   ENTRY_ALGORITHM_LOAD_ERROR, exit 95. The hashed bytes are compiled and executed as a fresh module, so the
   module's __main__ block does not run.
5. Call main(remaining argv). Checker role: an exception escaping main maps to the checker's ERROR code (2), as its
   own __main__ does. Other roles: one JSON line {"status":"ENTRY_UNCAUGHT_EXCEPTION"}, exit 94. A
   non-integer status maps to the same code.
Exit codes 92-97 are used by no algorithm.

## 8. Audit record (written only by the parent; read by the expectations program)
Path: <audit_dir>/<item>.audit.json, where audit_dir is fixed in the run plan.
Exact keys: format ("mols39-cert-job-audit-v1"), item, plan_sha256, verdict ("AUDITED_PASS" or "AUDITED_FAIL"),
settled (true or false), exit_code (int), declared_output_sha256 (object: every declared output name to the sha256
the parent computed from the actual file), receipt_sha256 (string, informational), auditor (string), at (string),
notes (string).
The expectations program requires: verdict AUDITED_PASS; settled true; exit_code = the plan's expected exit; the key
set of declared_output_sha256 equal to the declared outputs; and every value equal to the sha256 it computes itself.

## 9. Supervisor interface requirements (generic; no particular supervisor version is assumed)
S1. Spawn argv = [python3.14, "-I", "-B", entrypoint, *argv_tail] exactly as in the run plan, with stdin a pipe.
S2. Publish the launch identity, then write b"GO\n", flush and close stdin. The supervisor owns a finite startup
    deadline from spawn that covers GO delivery and stalled stdin.
S3. The job root (<base_dir>/<item>) is created fresh for the job, owned by the run user, not group- or
    world-writable, with no symlink in its chain. The entrypoint verifies this independently.
S4. At settlement the job root holds only the declared outputs plus any supervisor-owned files, all regular files
    with one link. Their hashes are recorded in the supervisor's settlement evidence.
S5. Per-job caps: wall 300 s, RSS 256 MiB, output 16 MiB, reservation 100 MB.
S6. Settlement evidence is audited by the parent, who writes the section 8 record.
