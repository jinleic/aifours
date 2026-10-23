# Cleanup 2026-10-18: environments of dropped six-lane targets

Requested by the owner: for dropped targets, keep scripts, configs, receipts, verdicts and logs; remove bulk generated outputs.
No git-tracked file was changed. Every removed file is listed with size and SHA-256 in `removed-files.tsv`;
package versions of the removed virtualenvs are in `removed-env-packages.txt`.

Removed (untracked, regenerable):
- `information-science/evidence/six-lane-20261016/balanced242/.venv` (185 MiB; CPython 3.14.3 + ortools, scipy, highspy).
  The tracked symlink `guessing-number-r-minus/.venv -> ../balanced242/.venv` is kept and now dangles.
- `information-science/evidence/six-lane-20261016/cdf211-k7/venv` (218 MiB, including a 38 MiB pip download cache).
- `physics/evidence/six-lane-20261016/noncws-code/env/uv-cache` (155 MiB uv download cache; `env/venv` kept).
- `__pycache__` directories in seven of the dropped lanes.

Deliberately kept:
- `noncws-code/env/venv`: `matrix-weight-24-0-10/frozen-candidate-v1/MANIFEST.json` names it as the verification interpreter.
- `robust-spr/code/venv` and `env-cache`: used by the active `me3-minimum-scv` and the `phase-type-complex3` receipts; a run was live during cleanup.
- All `runs/` data (CNFs, solver outputs) in `cdf211-k7` and `mcdsqs-twisted-family`: git-tracked, and README tables and a pin receipt cite them.
- Source PDFs (repository policy keeps third-party PDFs local).

Note: the round contract (`institute/runs/six-lane-2026-10-16/contract.json`) forbids deletion by round workers; this cleanup was
an explicit owner instruction outside that round.
