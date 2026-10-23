# Incident record: automatic deletion of lane-generated intermediate files (2026-10-17)

Recorded 2026-10-17 ≈03:53 PDT host clock by worker `MathMcDsqs38`, after the parent's
safety correction. **Deletion did occur** in the runs listed below; no "no deletion
performed" statement applies to them. Nothing was regenerated to conceal the loss; any future
regeneration will be labelled *regenerated*, never original. The frozen lane `../mcdsqs38/`
was only listed/hashed (read-only) for this inventory.

## 1. Causes (producer code)

| Script (lane, sha256 at the time) | Cleanup behaviour |
|---|---|
| `mcdsqs38/code/pipeline.py` (`d27e6fea…250e` for E1b/E4; `4dc82fb6…eabf` for E6, replay, and the copies used by F0/F1 here) | `os.remove(km_i.cnf)` for every KM sample i > 0 (right after solving); `os.remove(col_i.cnf)` for every colouring CNF whose status was not SAT |
| `mcdsqs38/code/mutation_controls.py` (`e2fa6511…c902ca`) | wrote each mutated certificate, ran both checkers, then `os.remove`d it (15 files per run) |
| `mcdsqs38/code/km_inventory.py` (`ce2a071e…2e292`) | wrote each KM CNF into a Python `tempfile.TemporaryDirectory` (system temp, **outside the repository**) that is deleted automatically on exit |
| `mcdsqs38/code/tanzhou_controls.py` (first run, double-translation bug) | not a delete call: the two invalid control certificates (sha256 `5b885f24…aa12cc` v=26, `48318a08…a054f9` v=32) and their check receipts were **overwritten in place** by the corrected run instead of being retired to `archive/` |

## 2. Inventory of pipeline runs (`runs/incident_inventory.json`, read-only comparison with each run's summary.json)

| Run directory | Samples | Files written | Not retained | Present files match recorded sha256 |
|---|---|---|---|---|
| `mcdsqs38/runs/e1b/v26_m7_r9` | 5 | 9 | km_1–km_4 (4) | yes |
| `mcdsqs38/runs/e1b/v26_m23_r9` | 8 | 16 | km_1–km_7; col_3–col_6 (UNSAT) (11) | yes |
| `mcdsqs38/runs/e1b/v26_m9_r9` | 8 | 16 | km_1–km_7 (7) | yes |
| `mcdsqs38/runs/e4/m7_r7_b1` | 12 | 24 | km_1–km_11; col_0–col_2 (UNKNOWN at 300 s) (14) | yes |
| `mcdsqs38/runs/e6/g3phi_r9_b1` (the 24-sample run of the verified mcDSQS(38)) | 24 | 48 | km_1–km_23 (23); all 24 colouring CNFs retained | yes |
| `mcdsqs38/runs/replay_e6_s0` | 1 | 2 | none | yes |
| `mcdsqs-twisted-family/runs/f0/p19_replay` | 1 | 2 | none | yes |
| `mcdsqs-twisted-family/runs/f1/p31` | 4 | 8 | km_1–km_3 (3) | yes |

For every file not retained, its sha256 (computed when it was written) survives in the run's
`summary.json` and in `runs/incident_inventory.json`. The pinned mcDSQS(38) evidence is
unaffected as a mathematical object (its certificate is checked directly); its producer
inputs for sample 0 (`e6/g3phi_r9_b1/km_0.cnf`, `col_0.cnf`) are retained and match, and the
parent's independent replay of sample 0 is separate. Certificate validity does **not** imply
that the other originals survived.

Other non-retained files:
* mutated certificates: 15 each in `mcdsqs38/controls/mutations_tanzhou26/`,
  `mcdsqs38/controls/mutations_tanzhou32/`, `mcdsqs38/evidence/mcdsqs38-g342/mutations/`
  (45 files; only `mutation-results.json` with both checkers' messages remains; mutated-file
  hashes were not recorded);
* 6 KM CNFs of E0 (`mcdsqs38/runs/e0/km_inventory_v38.json` records their sha256:
  `e64e7265…d46b`, `afe38554…5a4f`, `f0c51b2e…898f`, `14eb62da…464d`, `0d894ea2…8b68`,
  `aa99879d…2372`), written to and removed from the system temp directory.

## 3. Containment and fix

* The family-lane probe `runs/f1/p31` (old code already loaded) was cancelled gracefully
  (SIGTERM to its own pipeline process and its two kissat children) at 03:50:19 PDT, before
  any colouring of samples 1–3 finished, so no colouring CNF was removed there. Retained:
  km_0.cnf, col_0.cnf–col_3.cnf, col_0.cnf.log, mcdsqs62_sample0.txt, summary.json, p31.log.
* Fixed family-lane sources: `code/pipeline.py` sha256
  `95b5867348b868cf9686a5d105b88a68161355fce307bedddf4c81c910b5a749` and
  `code/mutation_controls.py` sha256
  `c14763f13e523ca3f6bbff765e6a7f7a75e906e147882763ad16fd8c6f9b24bc`: no cleanup branches;
  `os.remove/os.unlink/os.rmdir/os.removedirs` replaced by a raising guard at import; both
  refuse to write into a non-empty output directory (no overwrite). Mutated files are
  retained and their sha256 recorded. `km_inventory.py` and `tanzhou_controls.py` are not
  copied into this lane; nothing here uses `tempfile`.
