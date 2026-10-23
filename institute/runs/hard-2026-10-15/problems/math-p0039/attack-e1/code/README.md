# Computations and replay

Run all commands from the workspace root. Every command listed in the current
`claims.json` uses Python; it never executes an attack-built binary.

* `recheck.py` is the snapshot-safe entry point for the main metadata, main
  arithmetic samples, shared C/Python arithmetic and Python-prefix samples.
  It first uses `recover_logs.py` to reconstruct the three oversized logs from
  the staged gzip parts and verify both supplied manifests. Each child has a
  timeout below 900 seconds.
* `check.py` independently recomputes recorded full residues and actual sieve
  factors by Python pow and trial division. Metadata checks establish block
  bookkeeping only. `compare_scans.py` checks aggregate totals and 6,032 shared
  full-residue/factor records; it does not compare every scan decision.
* `replay.py` produced the fresh ten contiguous 10-million-member prefix
  chunks. `check_interval.py CHUNK --backend pow|manual` recomputes every member
  of exactly that chunk and checks its full-residue hash. It imports no producer.
* `windows.py` is the preserved separated-window producer. `check_windows.py`
  reexecutes exactly the requested windows and enforces their fixed grid.
  Current claims split the 100 windows into five groups of 20. Use those
  individual commands; the old `--all` claim timed out in the previous review.
* `check_controls.py` and `check_family.py` verify the isolated small controls,
  exact difference collisions, proper factors and restricted power-of-two
  family. Their corresponding generators are preserved.
* `scan.c` and `independent_scan.py` are the original producing sources. The
  retained `scan` binary is provenance only. The C production scan was not
  rerun during recovery; its full range is not independently certified.
* `recovery_batch.py` is visit orchestration for bounded prefix/window jobs,
  not a claims replay entry point. Its child commands, outputs, return codes
  and timings are preserved in `evidence/recovery-*-runs.json` and chunk files.
* `recovery_quick_checks.py` exercises positive evidence and deliberately
  broken witnesses. `check_snapshot_recovery.py` tests a snapshot with all
  three oversized raw logs absent. `seal.py create|check` records/checks file
  integrity, restoring omitted raw logs before checking. Hashes do not prove
  mathematical scan correctness.
* `build_recovery_delivery.py --final` builds the current report and atomically
  rewrites claims only after all planned finite checks have outputs. It does
  not produce scan decisions. `start_recovery.py` was the one-time initialization.

The previous attempt's `finalize.py`, `fast_checks.py`, `progress.py` and related
orchestration are retained as historical source. They do not build the corrected
delivery. In particular, rerunning the legacy finalizer would restore the old
wording and unchunked replay commands. The previous report, claims, manifest and
status are archived in `evidence/previous-delivery/`.
