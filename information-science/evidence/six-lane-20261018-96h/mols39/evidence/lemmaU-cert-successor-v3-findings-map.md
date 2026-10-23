# Lemma U certificate — successor package v3 and per-finding map (2026-10-19T07:45:07-0700, ContinueCFR21)

Answers the source review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-certificate-source-codex-v1.prompt.stdout.txt (sha256 ea5f29a7d48fbcfae81c8fb6c6ffc78d208234afd521755faa30e8291b8c2a10), verdict HOLD, and the parent's instructions of
2026-10-19 ~07:2x. Everything below is WRITTEN ONLY. No producer, checker, generator, expectation program, entrypoint
or config has been run, compiled or parsed by any tool. No launch is requested by this file.

## Package (one frozen set; every file pinned in run plan v3 or the format)
| role | path | sha256 | status |
|---|---|---|---|
| format v2 (normative contract) | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-format-v2.md | a36ce58f481a6a0b4bc62a121951331a4f98276a624d79ea2b488fcd608bf64e | new |
| run plan v3 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-cert-run-plan-v3.json | eb7c3001b60807aa4377a94c2ac680c4bd92437724b492ccb4cda3ed95d3a974 | new; supersedes plan v2 868a5b39... and plan v1 ee6312f7... (neither ever authorized or run) |
| producer v2 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/lemmaU_cert_producer_v2.py | 2a635bd8a9ceef2f74abf47638531b940945e0b9b845048fc77d8a257d0f841e | new; supersedes producer v1 52b8218e... (never run) |
| checker (independent) | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker.py | e7e849627865db5c592507563b482a62873bd21413e0f46d4fec8bb5429e99a0 | UNCHANGED, byte-identical; source accepted on inspection |
| checker README | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/README.md | 038e4db23c3b5bfb48dd5b523bc3bceb7777cb8927d2024dcc8541450ad3bb5f | unchanged |
| mutant generator v3 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/make_cert_mutants_v3.py | 9fe7841863b7120dcad4d0ee7858e76ba50d4d7192c96eb894b3aca93fbed7a2 | new; supersedes generator v2 35d08e6e... and v1 12d89e5c... (never run) |
| expectations v3 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/check_cert_runs_v3.py | 74d9d11736a7d34d864ebfbf6c227eb9a6185f666c443319eae5c5ecf4bde732 | new; supersedes check_cert_runs v2 d7be83ff... and v1 7ce2b4e0... (never run) |
| entrypoint producer v2 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_producer_v2.py | dd7c52dabba351a32a92309a49811638036efc87f39237ffc7e85f31efbbcc2d | new; supersedes go_entry_producer_v1 (never run) |
| entrypoint checker v2 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_checker_v2.py | b65f6cd2b7691bd1bcddfcafc1c98d05f8405400b80f924b8a4b623c427032a1 | new; supersedes go_entry_checker_v1 (never run) |
| entrypoint generator v2 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_mutants_v2.py | ab4872480a08777620eb7f3e8a7d6b7390434bff145edcbc001ef91da0691ca7 | new; supersedes go_entry_mutants_v1 (never run) |
| entrypoint expectations v2 | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/go_entry_expectations_v2.py | 87f9119d252ecadfdfd94ceac7626fbeb3539671a42e19ed034779988a8a286a | new; supersedes go_entry_expectations_v1 (never run) |
| nc9 control raw | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/cert-controls-v1/dm39_anchor_mut_r1c0.raw | c620c0f7663f04cf0b00c7824250effb5b5bac62e893627ad505475572a26d15 | unchanged control data |
| nc9 provenance | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/cert-controls-v1/provenance-v1.json | 3e37d17d7dc0f9b7b2e4ee2f12eb1ff27b2247e0c0f272d68060a952afe5b12d | unchanged |
| anchor input | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/controls-v1/dm39_six_anchor.raw | 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a | unchanged |
| DM21 input | /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/checker-controls-pass-v1/controls/pos_sage_dm21_k6.raw | 70c8c2e579961ead65bb2abf03cc2d86cc799d1976f31d5333b52b26a142e825 | unchanged |
The review covers source and plan only. Nothing executed, so readiness grants no launch permission.

## Per-finding map
F1 (FATAL; expectations can pass without actual artifacts) -> check_cert_runs_v3.py:
  - Every artifact is read from <plan.base_dir>/<item>/<declared name>: an O_NOFOLLOW walk, a regular file with one
    link, a size cap. Hashes are computed from the bytes read.
  - Producer: cert_sha256 must equal the hash of the actual cert.json. The certificate must be canonical, with its
    header and sizes consistent with the report (check_producer).
  - Checker: cert_sha256 must equal the hash of the actual certificate artifact named in the plan, never another
    report (check_checker).
  - Generator: the reported manifest and source hashes are checked against the actual files. Every mutant file is
    hashed, parsed canonically, and compared with an independent re-application of its intended mutation to the
    actual producer certificate (apply_mutation). The manifest details are checked against the source. nc0 must be
    byte-identical to the source.
  - Parsing is strict: duplicate keys, NaN, Infinity and non-finite floats are rejected. Each report must be exactly
    one line in its producer's exact serialisation with the exact key set. Comparisons use typed equality (same()),
    so 7 != 7.0 and 1 != True. No .get() defaults are accepted for expected fields.
  - Launch evidence: each prefix item needs a parent audit record (format v2 section 8) with verdict AUDITED_PASS and
    the expected exit code. Its declared-output hashes must equal the hashes the program computes. Pins of all
    programs and inputs are re-verified.
  - The self-reported producer_sha256 and generator_sha256 are informational only.
F2 (FATAL; qualification ignores a false claim) -> check_cert_runs_v3.py main():
  - qualified = (self is the final item) AND everything as expected AND claim is true AND no pin mismatch.
  - The final item exits 0 only if qualified. Before CHK-anchor the claim is the explicit string "UNEVALUATED", and
    a non-final EXP exits 0 only in that state.
  - The CHK-anchor expected fields and the claim fields include anchor_sha256 = 3c8dbe62.... The claim also binds
    cert_sha256 to the actual PROD-anchor cert.json (format v2 section 6).
M1 (MAJOR; prior EXP gates and the parent-audit barrier) -> check_cert_runs_v3.py, plan v3:
  - --self ITEM replaces "upto". The evaluated prefix is every plan item strictly before ITEM, earlier EXP items
    included. Their result files are validated: same plan, same prefix, all_as_expected true, claim "UNEVALUATED",
    qualified false.
  - Parent audits are mandatory for every prefix item.
  - Plan P1: one exact parent GO per job, EXP jobs included, with no automatic continuation or polling.
  - Plan P3: CHK-anchor is admitted only after the parent's AUDITED_PASS record for EXP-D, cited in its GO.
M2 (MAJOR; unbounded pre-GO waits) -> go_entry_*_v2.py:
  - At most 3 bytes are consumed via os.read on fd 0, plus a zero-timeout probe for one extra byte, with a select()
    deadline of 120 s from entrypoint start.
  - EOF, timeout, wrong bytes, extra bytes or a select error -> os._exit(97), with nothing printed and no file.
  - The supervisor must own a finite startup deadline from spawn (format v2 section 9 S2). No supervisor version is
    assumed.
M3 (MAJOR; incomplete budgets):
  - Producer v2, generator v3 and expectations v3 accept only a finite budget with 0 < S <= 280 (default 240). They
    have cooperative checks in every substantial loop and a deadline check before each publication step.
  - The producer additionally has work limits k <= 12, n <= 120, dim <= 8 (WORK_LIMIT).
  - Input caps (raw 1 MiB, certificate 8 MiB, plan 4 MiB) are enforced by the entrypoints, before the algorithm
    reads anything, and again inside the programs.
  - The checker keeps its accepted budget rule (finite, positive); its inputs are capped by its entrypoint.
  - Supervisor wall, RSS and output caps remain independent (S5).
M4 (MAJOR; real-root containment):
  - Entrypoints v2 open --job-root component by component with O_DIRECTORY|O_NOFOLLOW, require the run user's
    ownership and no group/world write, then fchdir() into it.
  - Outputs are plain names created with O_CREAT|O_EXCL|O_NOFOLLOW in that directory. For the checker, the
    entrypoint requires exactly "--out result.json". The generator's --outdir is removed.
  - The expectations program uses only plan.base_dir and checks that its own working directory is
    <base_dir>/<self> (same device and inode). It reads only declared names through directory fds and never follows
    manifest or report paths.
  - It rebuilds the plan argv for every job and requires it to equal the plan's argv_tail.
M5 (MAJOR; grammar mismatch):
  - Grammar G1 is frozen normatively in format v2 section 1. It is the accepted checker's parse: split on "\n", at
    most one final newline absorbed, ASCII-whitespace tokens, blank rows rejected, one optional sign plus ASCII
    digits, Python int digit limit.
  - Producer v2 and generator v3 implement G1 on the same single raw read that is hashed. The checker is unchanged.
m1 (MINOR; error mappings):
  - Entrypoint _load() reads inside the handler: read, compile or exec failure -> 95; pin mismatch -> 96; an
    exception escaping main -> 94 (checker: its own ERROR code, 2).
  - Producer, generator and expectations map OSError to IO_ERROR/ERROR and other exceptions to
    INTERNAL_ERROR/ERROR, and always try to write result.json.
  - Distinct codes ensure that no abnormal outcome can look like an intended control rejection, whose exit is 1 with
    an INVALID report checked field by field.
m2 (MINOR; canonical bytes): option "producer-only plus verification" (format v2 section 3). The producer and
  generator write canonical bytes. The expectations program requires canonical bytes for the producer certificate,
  the source copy and all 11 mutants. The checker is unchanged.
m3 (MINOR; no check-3 control):
  - nc10_basis_scale (basis[0] times 2) is added, with intended INVALID at check 3 and exact reason
    "check 3: basis[0][free_columns[0]] != 1".
  - Stale v1 references are corrected: the plan and docstrings now name the v2/v3 files.
Parent items:
  - Actual artifacts, schemas, pins and audited prefix: F1 and M1 above.
  - CHK-anchor only after an explicit parent audit of EXP-D: plan P3. No auto-chaining: plan P1.
  - No v7 assumptions: format v2 section 9 is generic and the plan's "requires" names no version.
  - The independent checker is preserved byte-identical (math, rank, basis, rainbow and coverage logic untouched).
  - nc9 bytes for review: plan v3 field "nc9" carries the full mutated raw text, the provenance JSON text, the
    original and mutated row-1 lines, and the derivation of the exact DM rejection. Summary: D[1][0] goes 0 -> 1, so
    f = D0 - D1 changes only at column 0, from 0 to 38. 38 then occurs twice and 0 not at all, and the first failure
    is "check 1: D is not a difference matrix (rows 0, 1)".

## Preregistered control expectations (plan v3; checker source e7e84962...)
- Exact reason strings:
  - nc2 "check 4: R_0[pivot_0] != 1"
  - nc4 "check 6: 242 indices listed, 3^dim needed (dim = 5)"
  - nc5 "check 1: sha256 of the anchor bytes != certificate anchor_sha256"
  - nc8 "check 0: rank_witness is not a list of U - dim records"
  - nc9 "check 1: D is not a difference matrix (rows 0, 1)"
  - nc10 "check 3: basis[0][free_columns[0]] != 1"
- Full-match regexes, because the failing equation or pivot depends on the data:
  - nc1 "check 2: e_[0-9]+ \. basis\[0\] != 0 \(mod 3\)"
  - nc7 "check 4: R_0\[pivot_[0-9]+\] != [01]"
- Templates filled from the independently verified manifest details:
  - nc3 "check 5: listed point {failure_idx_moved} is not rainbow (fibre {failure_fibre_of_moved})"
  - nc6 "check 6: failure [{idx}, {new_fibre}]: the fibre carries three distinct values"
- nc0 must be VALID with the full anchor facts.
- The fields n, q, k, U and J are expected to be null for first failures at checks 0 and 1, and to equal the raw
  values from check 2 on. The facts are null for every INVALID.

## Scope
Lemma U stays CORRECTNESS_ACCEPTED_SCOPED_PARTIAL: computer-assisted, exact anchor only. This package is unexecuted
and unqualified. Both extension questions stay UNKNOWN. There is no claim about CFR(6,39), six MOLS(39), other
anchors, novelty or priority.
