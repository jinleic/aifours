# Parent replay of two phys-2 K3 cube certificates (MOQLS(7), encoder A)

Desk: `review/moqls7-k3-cube-parent-replay-v1/`, run 2026-10-18 00:58-02:32 PDT. RESULT.json sha256 `8b6f57b7cc9f14071849d916fcfa5001ed7dac43e6d0b5d2673adefb1431ca9b`.

## Scope
This is per-instance verification evidence only. For C321 and C411, the parent regenerated the CNF from the pinned
lane code. The bytes matched the brief's SHA-256, and a freshly streamed CaDiCaL binary DRAT refutation was accepted
by the parent-built drat-trim. There is no K3, M(7), coverage, bridge or theorem verdict. AMENDMENT-2 makes
each cube claim conditional on whole-bridge review. C311 is outside this desk.

## Verdicts
| instance | verdict | regenerated CNF sha256 = brief | solver rc | checker rc | checker status | safety stop |
|---|---|---|---|---|---|---|
| A_C321 | **PASS** | `d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388` yes | 20 | 0 | `s VERIFIED` (exact, CR stripped) | none |
| A_C411 | **PASS** | `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2` yes | 20 | 0 | `s VERIFIED` (exact, CR stripped) | none |

Neither checker log contains `NOT VERIFIED` or `s TIMEOUT` anywhere. Both solver logs are exactly `s UNSATISFIABLE\n`
(sha256 `bde6e1ee...a162`), the same bytes as the producer's solver logs.

## Per-instance record
| | A_C321 | A_C411 |
|---|---|---|
| final receipt | `receipts/v1-A_C321.json` `cbd7f02f5b2850cae2814c641f283633abf5405b87035bac3043a1541502efa8` | `receipts/v1-A_C411.json` `308e255ee1ec4c687f1b79db4157a44c3c3ae9fc1b8cffa24b976f8690707442` |
| pre-execution receipt (script SHA-256s, written before any launch) | `62cebdf9e1ddf856c6e9fc393a790e647366c033a4fe51e1e4054c543d696588` | `2845fa27d1cffa82ca998451c285b09f1a2aadde61c342da8631d771bfd679d2` |
| launch receipt (binary SHA-256 at spawn, lane snapshot) | `231131d338b2f1ffee8b7f162f0d4cb40595037ee2363b66b856296b37c73897` | `25bcdf9bce0d179a94193146e40736f6eb6b7bf25fb6d8956e0dcab10ef9e3f5` |
| CNF bytes / header | 16,730,029 / `p cnf 96978 627486` | 16,730,836 / `p cnf 96978 627556` |
| base CNF sha256 (= brief) | `d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388` | `d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388` |
| regeneration (subprocess) | 1.182 s | 1.19 s |
| pipeline start / end | 2026-10-18T00:59:08-07:00 / 2026-10-18T01:34:46-07:00 | 2026-10-18T01:34:52-07:00 / 2026-10-18T02:32:52-07:00 |
| solver end (wall, user) | 2026-10-18T01:23:09-07:00 (1441.516 s, 1433.14 s) | 2026-10-18T02:07:12-07:00 (1939.366 s, 1925.42 s) |
| checker end (wall, user) | 2137.989 s, 705.697 s | 3479.385 s, 1551.671 s |
| sampled aggregate RSS peak (driver + children, 8,290 / 13,556 samples) | 1,360,969,728 B | 1,643,446,272 B |
| ru_maxrss solver / checker | 870,678,528 / 868,827,136 B | 859,340,800 / 1,261,944,832 B |
| free bytes: gate before drat-trim, before cadical | 15,985,811,456, 15,985,811,456 | 15,551,860,736, 15,551,860,736 |
| free bytes: in-flight minimum / at end | 15,528,595,456 / 15,551,807,488 | 14,359,072,768 / 14,750,056,448 |
| solver log | `logs/v1-A_C321.solver.log` `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162` | `logs/v1-A_C411.solver.log` `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162` |
| checker log | `logs/v1-A_C321.checker.log` `fb69d2b8449a0f36a9ee22837829239dabfcbc928a4d24e2432f15d1061ddc94` | `logs/v1-A_C411.checker.log` `a8a1b84169f53cca91d436d0ca0a5415e1e5eea157ec1284f0dfac4922a82dee` |
| proof bytes read by drat-trim (log) | 558,745,977 | 916,894,734 |
| core (log) | 350073/627486 clauses; 1656163/4846790 lemmas | 437328/627556 clauses; 2682948/6433957 lemmas |
| producer receipt: seconds, peak | 1906.802 s, 1,275,789,312 B | 3143.93 s, 1,899,347,968 B |

Binaries, hashed at spawn and again after each run (unchanged):
- cadical: `/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical`, sha256 `601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa`, equal to the producer's.
- drat-trim (parent-built): `review/moqls7-parent-proofcheck-v1/drat-trim`, sha256 `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`.

Commands: `cadical -q -t 5400 /dev/fd/<cnf-pipe> fifo/v1-A_<cube>.drat.fifo` and
`drat-trim /dev/fd/<cnf-pipe> -i -t 7200 < fifo/v1-A_<cube>.drat.fifo`. Both used cwd and TMPDIR set to desk `tmp/`.

Observation: each parent checker log matches the producer's lane checker log line for line, except the
`c verification time` line. That covers the same proof byte count and the same core and lemma statistics. Each
producer log's SHA-256 equals its receipt's value. The proofs themselves were streamed only and never hashed.
That CaDiCaL emitted the same proof bytes is therefore [INFERENCE], and the verdict does not depend on it.

At both launches the observational lane snapshot showed exactly two other lane natives: the phys-2 worker's kissat and
drat-trim on `explore/k3cubes/B_C321.cnf`. This desk itself ran at most two natives at any time, with instances in sequence.

## Inputs verified (SHA-256, at start and again at assembly)
- `code/k3_cubes.py` `70c79c62...0550` (wrapper pin); `code/gram_enc.py` `b2c206d8...8d38833` (encoder A pin).
- Producer receipts `A_C321.json` `c3a30df3...9314`, `A_C411.json` `5f117b60...23cf`. Metadata `A_C321.meta.json`
  `030cc5b8...dbda` and `A_C411.meta.json` `c180a573...9874` equal the receipts' `metadata_sha256`. Metadata CNF,
  base CNF, wrapper and encoder hashes all equal the brief's values.
- The lane CNF copies, hashed read-only only, equal the brief's values. They were never used.
- `review/AMENDMENT-2.r1.md` `82ee394e...14e0`, read for the composition rule.
All of these are unchanged at assembly (RESULT.json `lane_inputs_recheck`, `read_only_inputs_at_assembly`).

## Checks run before the instances (this desk)
- Regeneration-only precheck: both CNFs MATCH (`receipts/v1-regen-A_C321.json` `61746d59...e590`,
  `v1-regen-A_C411.json` `ad8bcb8d...09ef`). No native was launched.
- Transport self-checks of this desk's pipeline and verdict code (`receipts/v1-selfcheck-summary.json`
  `8b62446c...6171`):
  - X1 UNSAT4 gave PASS (solver 20, `s VERIFIED`).
  - X2 SAT3 gave FAIL (solver 10, `s NOT VERIFIED`).
  - X3, an UNSAT4 proof checked against the SAT3 CNF, gave FAIL (solver 20, checker 1, `s NOT VERIFIED`).
  - Six in-memory status-parser cases and two no-run verdict cases also passed.
  These test the desk's plumbing only.
- Parent checker controls are cited, not rerun: `review/moqls7-k2-parent-v1/RESULT.r2.json` (sha256
  `5362d6d2...8766`). T1-T5, Cb1, Cb2, Cc and the two Ca controls matched their stated expectations. The four Cd/Cd2
  mutation controls had no preset expectation and were recorded as observed.

## Deviations (full text: `deviations-v1.json`)
1. D1: `k3_cubes.make()` was not run. It calls `os.makedirs(<lane>/explore/scratch)` and must write the CNF and
   metadata as files. `scripts/compose_v1.py` instead executes the hash-verified bytes of `gram_enc.py` and
   `k3_cubes.py` and calls the pinned `coverage()`, `variable_map()`, `build(3, None, True, True, None)` with the map
   identity check, and `cube_clauses()`. It restates only make's encoder-A composition (header, base body, extra
   clauses) and emits the CNF to a pipe. Byte identity is confirmed by SHA-256 for both cubes.
2. D2: the interpreter was CLT python3 3.9.6 with `-I -B` and a reset environment. The producer's interpreter is not recorded.
3. D3: limits were cadical `-t 5400` and drat-trim `-t 7200` (producer 3600/3600). No instance came near either.
4. D4: the CNF went from memory to both programs through anonymous pipes. The producer used the lane CNF file. The proof
   went through a desk FIFO with a driver-held keepalive. Proofs were neither retained nor hashed, and zero-length FIFO
   nodes remain in `fifo/`.
5. D5: the parent-built drat-trim was used, not the lane-built binary. The source hash is the same. Controls are cited.
6. D6: the extra prechecks above. The regen precheck's script hashes are in its post-run receipts, and they equal the
   pre-receipt hashes.
7. D7: launch gate before each native Popen was free bytes >= 12,200,262,144 (12.2e9 + 262,144 projected growth). The
   in-flight floor was 12e9 and the RSS stop 3.5 GiB, with SIGTERM and a 120 s bounded wait. No lane-capacity wait was used.
8. D8: the PASS rule is stricter than line matching. `NOT VERIFIED` and `s TIMEOUT` must be absent from the whole log.
9. D9: `assemble_v1.py` and `deviations-v1.json` were created after the runs. REPORT.md was written from RESULT.json.
10. D10: no reruns. No infrastructure fault occurred.

## Integrity
Every desk file was created exclusively; logs were opened O_EXCL|O_APPEND. Nothing was modified, deleted or renamed.
No lane file was written, and no `__pycache__` appeared in the lane `code/`. There were no /tmp writes, Git, network or
model CLIs. The desk holds about 0.25 MB of new data. Scripts (sha256):
`compose_v1.py` `079cc5f5...03f7`, `k3lib_v1.py` `69903789...a7bf`, `replay_v1.py` `df746c43...6bdb`,
`assemble_v1.py` `ef98bbe9...8afb`.

Desk files before this report (33 regular files; FIFO nodes: v1-A_C321.drat.fifo, v1-A_C411.drat.fifo, v1-X1-UNSAT4.drat.fifo, v1-X2-SAT3.drat.fifo, v1-X3-UNSAT4proof-vs-SAT3cnf.drat.fifo):
- `RESULT.json` 30,940 B `8b6f57b7cc9f14071849d916fcfa5001ed7dac43e6d0b5d2673adefb1431ca9b`
- `deviations-v1.json` 5,674 B `cc7bafbcae66317e04af650fec4b61c5687119ec2152a8ee2c9f1466c3ac6c0f`
- `logs/v1-A_C321.checker.log` 3,065 B `fb69d2b8449a0f36a9ee22837829239dabfcbc928a4d24e2432f15d1061ddc94`
- `logs/v1-A_C321.solver.log` 16 B `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162`
- `logs/v1-A_C411.checker.log` 4,721 B `a8a1b84169f53cca91d436d0ca0a5415e1e5eea157ec1284f0dfac4922a82dee`
- `logs/v1-A_C411.solver.log` 16 B `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162`
- `logs/v1-X1-UNSAT4.checker.log` 414 B `75c438dbdf3d735b8250897d72edd590edc61bbeb47978dbe1b1271f2f2882e2`
- `logs/v1-X1-UNSAT4.solver.log` 16 B `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162`
- `logs/v1-X2-SAT3.checker.log` 178 B `8264c752a67d292c6eff732b24163ac4cf5dfa68dffa989bce01993a9dacd929`
- `logs/v1-X2-SAT3.solver.log` 22 B `2217106c4668f1a7c1dc25daef5631b13f0f5c888c3838e65730cec29fffcd9b`
- `logs/v1-X3-UNSAT4proof-vs-SAT3cnf.checker.log` 224 B `dd56a5978d7b4e3ecbd40a2fa769a0de3f794e1109e6724372c3ba6690236f1b`
- `logs/v1-X3-UNSAT4proof-vs-SAT3cnf.solver.log` 16 B `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162`
- `logs/v1-driver-regen-C321-C411.log` 438 B `c489551514b42569d31ab391c5e5d056fc558bcf2d5680848bfbdbc175a8e765`
- `logs/v1-driver-run-C321.log` 1,346 B `8e94ad1d40799f6ec0261939fa610ba5bb619882605cf5646a605aa1d7a43c53`
- `logs/v1-driver-run-C411.log` 1,345 B `6cfe46e6ef0dd6145a6c71682f758abb568dfc912eee24e076c221f800e596bf`
- `logs/v1-driver-selfcheck.log` 1,254 B `1865d6d0f6689a8ab25282cd20a019ebcb4a6cb40e4d44ef578f8aa294dc6d5c`
- `receipts/v1-A_C321.json` 11,486 B `cbd7f02f5b2850cae2814c641f283633abf5405b87035bac3043a1541502efa8`
- `receipts/v1-A_C321.launch.json` 6,779 B `231131d338b2f1ffee8b7f162f0d4cb40595037ee2363b66b856296b37c73897`
- `receipts/v1-A_C321.pre.json` 6,123 B `62cebdf9e1ddf856c6e9fc393a790e647366c033a4fe51e1e4054c543d696588`
- `receipts/v1-A_C411.json` 11,719 B `308e255ee1ec4c687f1b79db4157a44c3c3ae9fc1b8cffa24b976f8690707442`
- `receipts/v1-A_C411.launch.json` 7,008 B `25bcdf9bce0d179a94193146e40736f6eb6b7bf25fb6d8956e0dcab10ef9e3f5`
- `receipts/v1-A_C411.pre.json` 6,284 B `2845fa27d1cffa82ca998451c285b09f1a2aadde61c342da8631d771bfd679d2`
- `receipts/v1-X1-UNSAT4.json` 3,685 B `1eca61f49e64e9b9751bdfb7f3e6bb4769585d2e6ac66a966fbaa3a8022f2362`
- `receipts/v1-X2-SAT3.json` 3,654 B `604f85e2c18cecdc9dee72f7c53e9e22ae1f108022ca56b7cfe9605cb42b0773`
- `receipts/v1-X3-UNSAT4proof-vs-SAT3cnf.json` 3,791 B `6a674dc48d49d13e225de4cd97a03641643be0ae5bfe72e848006147fb2ed2fb`
- `receipts/v1-regen-A_C321.json` 10,016 B `61746d599bd505ba42f18f3df8b1a70bb6eee5debd25dcfaf0b30f830bb6e590`
- `receipts/v1-regen-A_C411.json` 10,409 B `ad8bcb8d04d7779079782249d62ceececea3e80db25283fa61876a5aec5d09ef`
- `receipts/v1-selfcheck-summary.json` 3,818 B `8b62446cdb2dbce7d5312f1055f7c3680413ea0479b3149ae91189c5e68e6171`
- `receipts/v1-selfcheck.pre.json` 2,858 B `8bacfdb446a276b4c29949d191f2ce0bf456adc164cfd42f6d43a7363a6e821b`
- `scripts/assemble_v1.py` 12,143 B `ef98bbe9540641ad5a78cb9559936fc0499b8f8088bd5b2c8c93ef6776738afb`
- `scripts/compose_v1.py` 4,978 B `079cc5f5bf53e9b894881d743784c5a0083f5b061e447332fdc8d868131503f7`
- `scripts/k3lib_v1.py` 21,064 B `6990378933de8f4e0a568091b2bc17e8b8528a4b05112faa145d275a767ea7bf`
- `scripts/replay_v1.py` 13,269 B `df746c43f48c33717f52ad62a18a198d5c43952406349a4b898ab297fa196bdb`
