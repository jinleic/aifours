# Receipt: exact_rqls_checker_v2 controls (initial-scope stdlib probe; not load-bearing)

Recorded 2026-10-19T00:47:15-0700. Launch record evidence/exact-checker-v2-controls.launch.json sha256
45c54ca64c6c77eb6eace40c67218c1b770177492cc70af7f711bfad95927b5d. Checker code/exact_rqls_checker_v2.py sha256
5bcdd698e228264af0b814e47113fc796bf73c7106c5ecac1f2d03ff6d09e8f7 (independent of the old lane's v1: trace-form zero test with Ramanujan sums;
Cauchy-Schwarz equality for parallelism).
Inputs: the old lane's five control files (regular files, read-only; sha256 matched the old README pins).
Command: for each file, `env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/exact_rqls_checker_v2.py <file>
> evidence/exact-checker-v2-controls/<name>.report.json` (noclobber), tool timeout 0; START/END
2026-10-19T00:47:05-0700; all five processes exited (exit 0 for C1, 1 for C2-C5). Lane tmp/ empty. Reports frozen 0444:
- C1_ex24_positive.report.json: 0c13e012838f6a86eba1b666218e1dfb1648c3089a3069ee8366944b13e61164
- C2_classical_nonparallel_negative.report.json: bb266769258a31237a401cd367319a693b8489e3b26b69d429d2eaa6d9b19d02
- C3_phase_mutation_negative.report.json: 9df7444e5d5084c97020f6e4d99fbe8f0efb2d72a414ce48079a597048edfce2
- C4_latin_mutation_negative.report.json: 5833f5198de6655d4ba0630b7d02a1d4bfc4eb72cfaa4cb07326b932c0cc65a1
- C5_norm_mutation_negative.report.json: 6a0b3f187f5140a813620999181674e3ef843773e47fc75d7542ed483e95846d

Results (all as intended, matching the old checker's control receipt):
- C1 Example 2.4: ALL_PASS, 64 distinct rays, 0 parallel pairs, 0 nonorthogonal line pairs.
- C2 classical: fails P4 only (8 rays, 224 parallel pairs).
- C3 phase mutation: fails P3 only (5 nonorthogonal line pairs), 64 rays.
- C4 Latin mutation: fails P1 only.
- C5 norm mutation: fails P2 only.
Role: an independent second exact checker, ready for any future candidate over a cyclotomic field Q(zeta_N).
