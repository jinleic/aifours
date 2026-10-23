# Lemma U certificate — launch-contract addendum v1 (2026-10-19T07:11:34-0700, ContinueCFR21)

Written only; nothing is run under this file. Parent IRC 2026-10-19 ~07:0x: the four certificate programs lacked the
supervisor GO handshake, so a fast child could read, compute or exit before the supervisor published its launch
identity and wrote GO. This addendum adds versioned entrypoints that require exactly b"GO\n" on stdin before anything
else. It is a launch-contract fix; no scientific scope changes.

## 1. Unchanged
- Normative format and checks: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-format-v1.md (sha256 1b6537a42dd936a16337c58fd65039ece9e150099e2b8a297ab21d206dfd6ba0); spec /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1.md (b151a61f9f84ccf8a0b261bfeb056ff6a9db58fc99e516b7562e1cea98f57df2) with erratum /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1-erratum1.md (beca7d3330230672e19ea5561f1844e721496ec7283e07c69a76672d62fb9135).
- Producer algorithm /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/lemmaU_cert_producer_v1.py (sha256 52b8218e8a3f5fccc719d8c2b1c17a886f0cdaee67bebebe54f2a3f4dd00b8eb): unchanged.
- Independent checker algorithm /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py (sha256 e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0), README
  /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/README.md (sha256 038e4db23c3b5bfb48dd5b523bc3bceb7777cb8927d2024dcc8541450ad3bb5f): unchanged and still independently authored. It imports
  nothing from the lane, and its entrypoint (below) imports nothing from the producer.
- Expectation algorithm /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/check_cert_runs_v2.py (sha256 d7be83ffa375818f45efe6513a77990e36e5af504d6483a167ce679f1d3a5959): unchanged.
- Control data: anchor-mutation raw /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/cert-controls-v1/dm39_anchor_mut_r1c0.raw (sha256 c620c0f7663f04cf0b00c7824250effb5b5bac62e893627ad505475572a26d15), provenance sha256 3e37d17d7dc0f9b7b2e4ee2f12eb1ff27b2247e0c0f272d68060a952afe5b12d.

## 2. Changed
- Mutant generator: v2 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/make_cert_mutants_v2.py (sha256 35d08e6e093febf0c298a2b6c5decee3ce149806b3a2eba388dc1549ff8e2f24) supersedes v1 (12d89e5c..., never executed). Only change: --outdir must be
  an EXISTING directory (the supervisor's output root), and the ten mutants and manifest.json are written there as flat
  regular files, with no subdirectory. This is needed because the supervisor accepts only declared regular child
  outputs.
- Four entrypoints, from one template:
  | entrypoint | sha256 | algorithm | algorithm sha256 |
  |---|---|---|---|
  | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_producer_v1.py | 23f45634a436335570836d5ff600d92247213644a34cd07c352f81589c2d73f8 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/lemmaU_cert_producer_v1.py | 52b8218e8a3f5fccc719d8c2b1c17a886f0cdaee67bebebe54f2a3f4dd00b8eb |
  | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_checker_v1.py | e5328bfc4316deff3f63d539656d23cc3480b052c195e9fb84047fae9461a639 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py | e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0 |
  | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_mutants_v1.py | b058997abf093a3307d7499cdfac6f722457dac53e5a9f470b2292e237611c99 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/make_cert_mutants_v2.py | 35d08e6e093febf0c298a2b6c5decee3ce149806b3a2eba388dc1549ff8e2f24 |
  | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_expectations_v1.py | 8d14b50e9c3d43703c4ccc7cd137f6e59214fd457d4004394f3a7328e0d07cd0 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/check_cert_runs_v2.py | d7be83ffa375818f45efe6513a77990e36e5af504d6483a167ce679f1d3a5959 |
- Run plan v2 (below) supersedes run plan v1 (/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-run-plan-v1.json, sha256 ee6312f75f65338dca221cab9ed4d510337fb43096982c2e17fa6cc1dd645aac).
  v1 was never authorized or executed.

## 3. GO protocol (each entrypoint)
1. The first action after `import sys` reads exactly one line from stdin. Unless it is exactly b"GO\n", the
   entrypoint exits 97 at once, with no stdout, no stderr and no file created. EOF, other bytes and a missing newline
   all count as no GO. Exit code 97 is not used by any of the four algorithms (producer 0/2/3/4/5, checker 0/1/2,
   generator 0/2, expectations 0/1/2).
2. After GO, the entrypoint reads the algorithm file, checks its sha256 against the pinned constant, compiles the
   hashed bytes (so the file cannot change between check and use) and executes them as a fresh module. The module's
   __main__ block does not run. A pin mismatch prints {"status": "ALGORITHM_PIN_MISMATCH"} and exits 96. A load
   failure prints {"status": "ALGORITHM_LOAD_ERROR"} and exits 95. Note that the checker was never compiled before
   freezing, so a syntax error would show up here.
3. The entrypoint calls main(argv[1:]) and exits with its status. For the checker, any exception escaping main maps to
   its ERROR exit code (2), exactly as the checker's own __main__ block does.
Expected stdin contract: the supervisor writes b"GO\n", flushes and closes stdin after publishing the launch identity
(as in owned_supervisor v7: go_delivered = GO written and stdin closed). The entrypoints never read beyond the first line.

## 4. Supervisor integration requirements (for config generation at GO time)
- Child argv = [python3.14, -I, -B, ENTRYPOINT, args...]. No go_exec_shim is used, because the handshake is in the
  entrypoint.
- Child stdout sink = <base>/<item>/stdout.txt (the expectation algorithm reads exactly this path); stderr sink
  <base>/<item>/stderr.txt.
- The declared child outputs per job are listed in the run plan ("declared_outputs", relative to <base>/<item>).
- Run plan placeholders: @PROD_ANCHOR_CERT_SHA256@ (MUT, stage 2; from PROD-anchor's one-line stdout, only after EXP-B
  is AS_EXPECTED), @PLAN_PATH@ and @PLAN_SHA256@ (the EXP jobs; this plan v2 file and its sha256).
