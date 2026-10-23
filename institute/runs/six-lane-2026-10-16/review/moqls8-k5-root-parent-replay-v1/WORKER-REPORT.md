# K5RootProofReplay final report (parent-delegated task output; saved 2026-10-17 16:30:13 PDT)

I replayed all 122 retained K5 root proofs and all 122 passed (`PASS`). Every proof was checked against exactly the base CNF plus that root's 7 unit clauses, using the parent-pinned drat-trim (`a46c0c71…8e37`). There were no mapping or proof mismatches, no cap trips and no failed attempts, so I sent no notification. This covers C11 only; it is not acceptance of K5 as a whole.

**Final receipt:** `review/moqls8-k5-root-parent-replay-v1/final-a1/FINAL.json`, SHA `88cac421…2905`. Counts: 122 planned, 122 with receipt, 122 `PASS`, problems `[]`, `c11_passed_root_ids` lists all 122. The six UNKNOWN roots (c016, c032, c048, c064, c080, c096) are listed as excluded and were neither replayed nor accepted.

**Other files** (paths relative to `review/moqls8-k5-root-parent-replay-v1/`; every file and directory was created exclusively, total 2.39 MB):

| File | SHA-256 | Contents |
|---|---|---|
| `k5_root_replay_v1.py` | `03213e7d…b89c` | The frozen runner, standard library only, no lane imports |
| `pin-a1/PIN.json` | `f32de4f3…5db2` | Pinned metadata, base record, per-root plan |
| `controls-a1/CONTROLS.json` | `afcd7398…1748` | 20 smoke controls |
| `corpus-a1/` | META `42caa554…`, DONE `e2eb3710…` | Per root: `cNNN.json`, raw `cNNN.drat-trim.stdout` and `.stderr` (all stderr empty) |

**Inputs pinned before the replay:**
- `LEDGER.v003` `b9b3fc67…`, the manifest `65f6e0dd…` and its `.sha256` sidecar `4e109813…` matched their expected hashes.
- Strict `RESULTS.jsonl` (`1f70fc0e…`), strict `META`, and the old `all` and `pilot` receipts were pinned at their current hashes.
- Each root was cross-bound across ledger line hash ↔ strict receipt ↔ manifest row ↔ sidecar ↔ old receipt. The compressed proofs total exactly 444,419,127 bytes.
- The base CNF was hashed once (`6ecb77a7…`) and given a full structural check: exactly 5,740,230 canonical clause lines, every variable ≤ 509915, no comments.
- The four lane metadata files were unchanged after the run.

**What every `PASS` root required** (each condition stored per root in `checks`):
- The CNF stream was exactly the header with `5740237` clauses, the base body unchanged, then the ledger literals as `<lit> 0` lines. Its hash matched the strict leaf CNF hash.
- The compressed proof's hash and size matched the manifest.
- Decompression in-process with Python's built-in `compression.zstd` completed cleanly. The full decompressed stream matched the strict stream hash and byte count, both as produced and as delivered.
- drat-trim reported reading exactly that many proof bytes and parsing `509915/5740237`.
- drat-trim exited 0 with exactly one status line, `s VERIFIED`. There was no TIMEOUT, no fatal or unclassified warning, and no guard trip.

The command was `drat-trim /dev/fd/N -i -t 1500`: the leaf CNF arrives through an anonymous pipe and the proof on stdin.

**One finding the parent should note:** for 102 of the 122 roots, drat-trim refutes base plus cube by unit propagation alone, before using any lemma. Those proofs were fully read and hash-bound but did not affect the verdict. The other 20 roots needed real backward DRAT checking: c006, c008, c014, c022, c024, c030, c038, c040, c046, c054, c056, c070, c072, c078, c086, c088, c102, c104, c112, c120. The largest, c040, had 268,294 of 6,124,455 lemmas in the core.

**Controls (20 of 20 behaved as intended):**
- **Positives:** a tiny valid UNSAT proof, real root c004 (unit propagation) and real root c054 (backward check) were all accepted.
- **Checker rejections:** an empty-clause-only proof was rejected (`s NOT VERIFIED`, exit 1) on a SAT CNF, on an UNSAT CNF that unit propagation cannot refute, on the `p cnf 1 1` case that upstream lrat-check wrongly accepts, and on c054's real CNF.
- **Binding rejections:**
  - A flipped compressed byte was rejected.
  - A mutated decompressed byte, recompressed so the compressed hash was self-consistent, was rejected. drat-trim itself said `s VERIFIED` on that proof; only the runner's stream-hash check caught it.
  - c014's literals under c054's binding were rejected.
  - c014's proof under c054's mapping was rejected.
  - A truncated compressed file was rejected as a decompression error.
- **Feed errors fail closed:** a valid proof followed by a 1 MiB bad tail made drat-trim stop reading and print `s VERIFIED` after only 5 of 1,048,581 bytes. The runner still returned UNKNOWN.
- **Caps give UNKNOWN, not FAIL:** a 160 MiB memory guard and a 1 s watchdog each ended drat-trim with SIGTERM. The `-t 0` limit printed `s TIMEOUT` with exit 0 and was correctly treated as UNKNOWN.
- **Base-CNF rejections:** a wrong clause count in the header, an octal-looking literal, a comment line and an out-of-range variable were all rejected.

**Resources:**
- The pipeline is two processes by design: one Python feeder and one drat-trim. There are no helper processes and nothing was written to `/tmp`.
- Peak checker memory was 1,178,419,200 bytes on c040, measured exactly by the OS. The highest sampled combined total was 1,246,576,640 bytes and Python's own peak was 68 MB, so usage stayed under 1.17 GiB, below the 1.4 GiB guard and the 1.5 GiB cap.
- Host-clock wall times: corpus 16:18:24–16:28:38 PDT (614 s), longest single root 105 s; controls 26 s; pin 5 s.
- Free disk afterwards was 17.5e9 bytes.

**Not covered here:** the cover argument (K5RootCoverAudit's job), the encoders and the meaning of the base CNF (C1–C10), any review of drat-trim's source beyond these controls, and the six UNKNOWN roots. The pin step did confirm that all 128 ledger literal sets equal the canonical sign patterns of `chain[1]`, but that is only a binding check, not a cover audit.
