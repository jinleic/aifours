# Parent GB replay — frozen implementation brief

## Goal and exact scope

Build a counted parent-owned replay for the 18 GB inputs required by the n8 contract: twelve direct templates P1-B4, P0-B4, P0-B5, P0-B6, P1-B6, P2-C4, P2-C3, P0-B1, P0-B2, P0-B3, P2-C2, P2-C1; then strengthened P1-B2.M2, P1-B2.M4, P1-B5.M2, P1-B5.M3, P1-B3.M2, P1-B1.M2. No other input or refinement is authorized. Native runs require a separate explicit parent GO; do not run the 18 science items during implementation.

Write exclusively under a NEW desk `institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-staged-replay-v1/` in `/Users/jinleic/repos/aifours`. Every file mode x, directories exist_ok=False. Correct by new versions. No deletion (spent FIFOs retained), /tmp writes, commits, pushes, global configuration, paid APIs or external contact. Each tool TMPDIR must be in the desk. Native work ends 17:57 PDT 2026-10-18; new native launch ends 17:29.

## Existing evidence to read

- `review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673 (relative to the run directory). All 22 exact formula identities, bytes and counts; use only the specified 18.
- Same desk `scripts/bind_gb_v2.py`: hash-pinned parent implementation already generated and decoded all22; its unchanged GB source loader and segmented in-memory sink can be reused. Do not call its `generate()` writer or overwrite any binding artifact. Recompute exact bytes in memory and demand the parent-bound SHA/bytes/header before launching.
- Lane `physics/evidence/six-lane-20261016/moqls8-problem16/code/gram_b_r2.py` SHA 4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0. GB flags: --order8 --quantum12345 --ngeneric0 --p4 1 --sb2 --g5. Own GB name table for each unit/tail; no GA integer IDs.
- Lane `review/GB_R6_PARENT_HANDOFF.r1.md`, SHA 0870f26c2a3713a0e520b7e92721888de9ff8d7edc5dfdaeb684c58d4d63dc1b: timing and API references only. Worker gb_direct_r6 deletes FIFO nodes, has weaker lifecycle/consumption guards, and is NOT the counted runtime. Do not import/run it. Do not copy its PASS summaries as proof.
- Parent GA runtime `review/moqls8-strengthened-parent-replay-v1/scripts/replay_v5d.py`, SHA ee52004ba7d12edd673a10bc4ed73005d6c56588697215c9b06cc1dbb846339e: reviewed resource/ownership/byte-accounting patterns. Reuse patterns instead of inventing a separate policy.
- `review/parent-rule-amendment-long-job-stability-v1.md`, SHA 0bbf4fdf6fd25e22e57b5c320262518dcf2df8a5a9e0a06c6b44b9afdac4ce87.
- `review/n8-replay-v5d-delta-codex-v1.note.md` and prior v5b/v5c findings: exception-safe ownership, failure latches, controls and identity timing.

## Runtime contract

Staged transport: one kissat process first (proof FIFO to a RAM collector with SHA256/count/actual EOF), fully reaped, then one parent drat-trim process fed the in-memory proof and a separately measured complete CNF. No CNF/proof regular file. Keep at most one collector chunk plus the RAM proof buffer; resource guard counts buffers in driver RSS. Emit ordinary receipts/logs only.

Pinned binaries: kissat4.0.4 `/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat`, SHA 05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848; parent checker `review/moqls7-parent-proofcheck-v1/drat-trim`, SHA a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37. Native limits3600/7200s. SIGTERM-only owned cleanup with bounded120s wait; no Popen.kill, SIGKILL, subprocess.run(timeout), subprocess wait(timeout), broad signals or setuid helpers inside a supervised group. An unsettled child/thread/FD or helper survivor stops the desk and vetoes qualification.

Admit only when the parent GA driver has exited and parent explicitly releases this desk; no GA/GB concurrency. One GB native at a time, pipeline RSS cap6GiB, lane busy<=4 and total<=11GiB, fresh free>=12.2e9 plus growth and in-flight floor12e9. Jobs>=60min require the unchanged monitor rule from `review/disk-monitor-v1-20261018T0722-to-1810.jsonl`: last sample age0..30s, >=25 ordered/tz-aware samples spanning>=290s in last300s, free>=13.5e9, max peak-to-later drop<=max(300e6,(lastfree-13.5e9)/12). Preserve restart events/gaps; do not reconstruct samples. Exact identities are re-hashed after admission immediately before native spawn.

PASS only with every conjunct: freshly regenerated formula matches bound SHA/bytes/header; BOTH measured CNF feeds complete/error-free matching that identity; solver self-exit20 and exact singleton `s UNSATISFIABLE`; checker self-exit0 and exact singleton `s VERIFIED` after stripping only CR; no NOT VERIFIED/TIMEOUT/early EOF/less-than-expected/header mismatch; recorded positive collected proof count/digest equals actually fed count/digest; checker-parsed consumed proof count equals fed bytes; observed EOF; all resources settled; no latched signal/guard/failure. Hash full raw logs at runtime; GB emits375334 duplicate-literal normalization lines, so count/filter ONLY that known class without weakening fatal/error parsing. Status and critical parser lines retained; record full raw stream hash/count separately from the filtered log hash.

Controls on THIS frozen runtime identity (exclusive separate outputs): genuine tiny UNSAT PASS; satisfiable checker CNF rejects the proof with proper NOT VERIFIED; intentionally short CNF delivery refuses even if checker prints VERIFIED; truncated proof rejects via byte equality; suffix proof rejects via byte equality while checking actual consumed count; deliberately altered recorded/transported digest fails; early checker close drains or stops cleanly without abandoning ownership. Each must prove the intended failure, not an unrelated exception. Pure-Python fixtures/smokes first; native controls only after the parent approves source.

## Delivery

Freeze source/diff/pins and control plan, with exact CLI commands and source SHA. Message the parent. No solver/control launch until explicit GO. After source review, run controls only; report measured receipts. Science execution is a separate GO, at most one item per run with newly named artifacts; no automatic retries, old UNKNOWNs retained. Scope stays exact-input proof certification, not n8 theorem or novelty.
