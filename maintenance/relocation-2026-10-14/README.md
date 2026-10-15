# AI4S relocation — 2026-10-14

The owner requested moving the research from
`/Users/jinleic/jinleic-workspace/ai4s` to `/Users/jinleic/repos/aifours` and organizing it.
The old project path is absent; there is no compatibility symlink or second active copy.

## Organization

| Destination | Ownership |
|---|---|
| [`../../information-science/`](../../information-science/README.md) | 12 dossiers and their round-level evidence |
| [`../../mathematics/`](../../mathematics/README.md) | 11 dossiers and their round-level evidence |
| [`../../physics/`](../../physics/README.md) | 13 dossiers, reselection and literature/significance audits |
| [`../../books/`](../../books/README.md) | Three original source-volume PDFs, kept local |
| This directory | Relocation provenance, old-to-new paths and verification outputs |

The domain indexes route to the dossier that owns each scientific statement, proof and verdict.
This relocation does not upgrade any novelty, correctness, HMZ or Lean claim.

## Conservation and provenance

- [`before.json`](before.json): per-path type, mode, byte count and SHA-256 before the move.
- [`move-receipt.json`](move-receipt.json): the initial move conserved 5,733 files,
  totaling 485,115,996 bytes, and preserved the existing destination Git directory.
- [`path-map.json`](path-map.json): current destinations for the original top-level entries
  and the five round-evidence directories. Apply the longest matching source prefix.
- [`original-index.md`](original-index.md): the pre-relocation combined index, preserved
  separately from the new repository and domain indexes.
- [`physics-scratch-move-receipt.json`](physics-scratch-move-receipt.json): five additional
  physics scratch trees moved into physics evidence; 387 files and 57,744,960 bytes conserved.
- `source-root/`: the preserved former project container after its contents were relocated.
- [`workspace-registry-entry-before.json`](workspace-registry-entry-before.json): the former
  workspace-root registry entry, retained because the project now lives outside that registry.
- [`edited-files.json`](edited-files.json): every preserved file whose bytes changed after the
  move, with SHA-256 before and after: 22 current research documents (21 dossier docs and one
  round-level README, all path translations), 10 runtime scripts (path fixes), the replaced root
  index and one concurrent physics-index edit. All other 5,699 preserved files still match `before.json`.

The move receipt describes conservation at cutover. Navigation and runtime-path edits made
subsequently are not claims of byte identity with the old tree. Historical prompts, run logs,
review outputs and receipts may still cite old paths or hashes; interpret them as the recorded
snapshots, using the path map rather than rewriting their provenance.

## Exercised relocation checks

Separate outputs are under [`parallel-smoke/`](parallel-smoke/); no smoke command below
writes into an original scientific receipt directory.

- Mathematics: the relocated trialgebra checker passed all 15 critical peaks, 75 trace steps,
  and its corrupted-coefficient and sign-mutation controls.
- Information science: the relocated exact array checker verified 19 decision cases,
  two counterexamples and 22 controls.
- Physics: the relocated lattice-universality checker passed four quadratic fixtures,
  12 convergent bases, 300 forward and 300 reverse patch checks, 36 phase windows and
  three negative-control families; run without its optional `--write` flag.
- Explorer: its default project path resolves here; all four dynamic-only information-science
  overlap guards find their relocated dossiers; local-lead lookup finds this repository;
  extraction renders one mathematics-volume page from `books/`. The old project path
  remains absent after the smoke.
- Workspace: `python3 -B research-institute/explorer/test_ri.py` passed 34 tests.
  `python3 scripts/workspace_audit.py` reported zero failures and zero warnings.
  The test run emitted a Python `ResourceWarning` for an unclosed test stream.
- Dossier checkers: 22 deterministic commands across all three domains exited 0 from the new
  paths, including Lean elaboration of the semifilter and Shor files through the shared cache
  (axioms `propext`, `Classical.choice`, `Quot.sound` only). Checkers that write into their own
  dossier ran on temporary copies. Record: [`dossier-smoke.json`](dossier-smoke.json).

[`parallel-path-review.json`](parallel-path-review.json) retains a bounded independent
Claude review of the initial path-risk excerpts. [`parallel-observations.json`](parallel-observations.json)
contains its parsed findings. Those are pre-fix observations, not a final review verdict;
the exercised checks above describe the observed post-cutover behavior.

The [final organization review](organization-review.json) used Codex `gpt-6.1-sol`, effort
`max`, read-only. It checked 43 claims and returned two documentation findings, both applied:
the root router now identifies the separate `institute/` workstream, and the translated-document
count distinguishes dossier documents from the round-level README. No scientific verdict changed.
[Final verification](final-verification.json) records preservation, navigation and verification
scope, including the post-review router hash.

## External resources intentionally not moved

Python environments, the dedicated mathematics HMZ working trees and Lean caches, the shared
`math/` corpus, HMZ wrapper/pairing and the delegate-model registry remain under
`/Users/jinleic/jinleic-workspace`. Their exact locations are in the
[repository reproduction section](../../README.md#reproduction) and dossier commands.
This is a research relocation, not a standalone environment export. Moving or rebuilding those
resources is not required to use the relocated dossier checkers on this machine.

The destination is outside the workspace Syncthing folder. Do not infer backup, peer replication
or publication from this relocation. No commit or push is authorized by this record.

## Reversing the relocation

Rollback is manual and must not overwrite an existing source path. The following **prints**
exact reverse commands from the recorded maps; it does not execute them. Review the output
before running any command. Current navigation edits move back with their dossier; the old
combined index is copied from its preserved snapshot.

```sh
python3 - <<'PY'
import json
import shlex
from pathlib import Path

repo = Path('/Users/jinleic/repos/aifours')
record = repo / 'maintenance/relocation-2026-10-14'
plan = json.loads((record / 'path-map.json').read_text())
source = Path(plan['source_root'])
for old, new in {**plan['entries'], **plan.get('evidence_rounds', {})}.items():
    original = record / 'original-index.md' if old == 'README.md' else repo / new
    target = source / old
    print('mkdir -p ' + shlex.quote(str(target.parent)))
    operation = 'cp -pn ' if old == 'README.md' else 'mv -n '
    print(operation + shlex.quote(str(original)) + ' ' + shlex.quote(str(target)))
PY
```

Supplemental physics-scratch reverse paths are recorded separately in
`physics-scratch-move-receipt.json`. Reversing the file moves also requires restoring the
workspace registry/routing and explorer paths; do not run the explorer against a half-moved tree.
