# Cleanup 2026-10-19: failed, stale and regenerable artifacts

Owner request (2026-10-18, about 23:12 PDT, verbatim): "clean up the ~/repos/aifours artifacts , so that the
stale and failed artifacts can get removed , just make sure that the scripts to create the artifacts are
preserved , then it is fine. also add these bulky artifcats file type or folder name into the .gitignore so
that they wont get uploaded into the github".
Owner choices, recorded before anything moved: include artifacts inherited by the live 96-hour run
("Everything now"), and rebuild the unpushed WIP commit without the bulky files ("Rewrite WIP commit").

## What moved

Between 2026-10-19T00:45:53 and 00:46:04 -0700, every selected entry was renamed (same APFS volume, no copy) to
`~/.Trash/aifours-cleanup-20261019/<same repository-relative path>`. Nothing was deleted. Disk space comes back
only when the Trash is emptied: about 90 GB, not the full 107.7 GB, because some copies are APFS clones that
share blocks with files that stay. At 00:56:42 two units (68 files, 30 MB) went back to their original paths; see
"What was kept". The table counts what is still in the Trash.

| Category | Units | Files | Bytes | FIFOs |
|---|---|---|---|---|
| FAILED: UNKNOWN, killed, capped or withdrawn runs | 39 | 3,057 | 58.51 GB | 125 |
| STALE: superseded versions, abandoned routes, duplicate copies, finished scratch | 90 | 13,450 | 28.85 GB | 196,320 |
| REGENERABLE-ENV: venvs, uv caches, Lean `.lake`/toolchains/builds, CLI caches | 90 | 288,618 | 20.38 GB | 0 |
| **Total** | **219** | **305,125** | **107.74 GB** | **196,445** |

About 56.3 GB of this sat in lanes that the live run `institute/runs/six-lane-2026-10-18-96h` inherits.

Largest units:
- `information-science/evidence/six-lane-20261016/packing-array19/m2q0b/proof` (21.8 GB, FAILED). The LRATs were accepted
  only by the unsound `lrat-check`, and the route was re-certified as `m2q0c` (486/486 drat-trim verified).
- `.../packing-array19/cases19q0/proof/*.lrat` (9.4 GB, STALE). drat-trim `-L` derived these from the `.drat` files,
  which stay and passed the final 2,976/2,976 replay.
- `.../packing-array19/cases19/proof` (9.1 GB, FAILED): four partial UNKNOWN streams of the abandoned M-class route.
- `physics/evidence/six-lane-20261016/ame46-support/explore/large_t_gen` (6.9 GB, FAILED): killed or UNKNOWN runs. The 18
  pinned pairs behind the s≥46 result stay.
- `physics/evidence/hard-continuation-20261015/formal/{lean/.lake, upstream/sat-upper-4268/lean/.lake, env}` (17.2 GB,
  REGENERABLE-ENV): Lean 4.24.0 toolchain, Mathlib f897ebcf packages and cache, comparator/lean4export/lean4checker builds.
  The formal README already called them non-deliverables, and the local tool patches are tracked as patch files.
- `information-science/evidence/six-lane-20261016/btd12-15/runs` (4.8 GB, FAILED): DRAT streams of UNKNOWN SAT runs on a
  route the verdict did not use.
- `institute/runs/six-lane-2026-10-16/review/moqls8-k2-parent-replay-v1` (4.3 GB, FAILED): its proof check failed on a
  parsing bug, and `-v2` superseded it.

Each unit's category, evidence (file:line), generator scripts and regeneration command are in
[units.json](units.json).

## What was kept

- **Every script, source and config.** Directory-wide selections moved only bulky types (`*.cnf *.drat* *.lrat* *.zst
  *.olean *.ilean *.ltar *.pbtxt`), FIFOs and files of 1 MB or more. Narrower selections moved exactly the files they
  name; outside whole third-party environment directories, that never included a source (`*.py *.sh *.lean *.c ...`),
  config, verdict or STOP marker. All 564 generator scripts that the units name still resolve in the repository.
  Narrower selections did move 1,091 small non-bulky files. 1,007 of them are duplicate copies (receipts, map files,
  logs) inside parent-replay input snapshots such as `review/moqls8-k2-parent-replay-v*/inputs/`, and a byte-identical
  copy of each still exists in the repository. The other 84 are dev or test outputs: `ame46-lower46-parent-binding-v1/enum/dev`,
  which its README calls "not evidence", the superseded `cdf211-k7/runs/xr1test` runs, the `k1_zst_test2` logs and one
  me3 calibration file.
- **Engine attack-epoch records.** The two hard-2026-10-15 units `problems/math-p0039/attack-e0/logs` and
  `.../attack-e1/{logs,selection-inputs}` held blob-identical copies of attack-e2 files. They were moved at 00:46 and
  restored unchanged (SHA-256 checked) at 00:56:42, because `attack-e*/` directories of institute engine runs are
  append-only records.
- **All load-bearing evidence of accepted results**, for example the retained PA19 DRATs and CNFs, the MOQLS(7) K2/K3/K4
  certificates, the K5 root proofs, the BTD(12,20) and CFR certificates, the colour cone trees and the me3 chart leaves.
- **Six units excluded by the parent:**
  - the five parent-compiled Lean builds of accepted results, each the only compiled copy:
    `gcdcqs20-lean-parent-audit-v2/build`, `lkts-kernel-parent-replay-v1/build`, `mcdsqs38-kernel-parent-replay-v1/build`,
    `point-cyclic-table-kernel-parent-replay-v1/build` and `point-cyclic100-kernel-parent-replay-v2/build`;
  - `review/ame46-lower46-parent-inputs-v1`, a clone-only copy that frees nothing and is a path the LOWER46 drivers read.
- **Environments still in use:** `robust-spr/code/venv`, `depolarizing/env`, `noncws-code/env/venv`,
  `random5reg-colour/.venv` and `moqls8-problem16/env`.

## Live 96-hour run

Its contract (`contract-v1.json:121`) tells round workers to keep closed-run evidence, UNKNOWNs and FIFOs. This
cleanup is a separate, explicit owner instruction, the same as the [2026-10-18 cleanup](../cleanup-2026-10-18/README.md).
Checks made immediately before the move:
- lsof found no open file or cwd inside the moved set.
- All 9,696 live-run text files were scanned for path references. The only match is a FIFO path quoted inside a
  receipt snapshot.
- The live lanes' pinned inputs, the PA19 cycle2 STOP/HALT markers and the old desks' scripts and `BINDING.json`
  were not touched.

Nothing under `*/six-lane-20261018-96h/` was selected.

## Records

- [units.json](units.json): one record per unit, including the six kept ones and the two restored ones.
- [moved-files.tsv](moved-files.tsv): 16,507 moved science files with size, SHA-256 and git status. Spot checks match the
  hashes in `moqls7-problem16/evidence/final_v1/INSTANCES_RECEIPT.json` and in `packing-array19/cases19q0/results/*.check.json`.
- [moved-envs-and-fifos.tsv](moved-envs-and-fifos.tsv): file counts and bytes for each environment unit, and FIFO counts for each unit.
- [codex-review-v1.md](codex-review-v1.md): independent review (gpt-6.1-sol, read-only). It found no scientific blocker after
  checking all medium-risk units, the units of 300 MB or more and 15 spot checks. Its MAJOR finding (the WIP commit must be
  rebuilt) and its MINOR finding (the move alone frees no space) are both addressed here.
- `~/.Trash/aifours-cleanup-20261019/MOVE-JOURNAL.jsonl` lists all 53,954 rename operations and the 45 restore operations,
  with copies of the files above. 53,909 renames remain in effect.

Restore an entry with `mv ~/.Trash/aifours-cleanup-20261019/<path> ~/repos/aifours/<path>`.

## Git

- `.gitignore` now excludes the bulky artifact types and folders: SAT formulas, proofs and proof streams
  (`*.cnf`, `*.drat`, `*.lrat`, `*.zst`, ...), drat-trim logs, `*.pbtxt`, `*.npz`, Lean outputs (`.lake/`, `*.olean`, `*.ilean`, `*.ltar`),
  Python environments and caches (`.venv/`, `venv*/`, `.uv-cache/`, `.uvcache/`, `pydeps*/`, `env-cache/`) and CLI temporaries
  (`node-compile-cache/`, `tmp-codex*/`).
- A second block ignores retired outputs whose file types are not bulky in general, by name or location. Rerunning
  their scripts therefore cannot re-add them: Olson `census6_p*.txt` and `p7_N*_fam*.jsonl` (857, 827 and 599 MB examples,
  over GitHub's 100 MB limit), me3 `leaves.txt.gz`, the random5reg `work-dirs/`, the moqls8 parent-replay input copies and
  other dev/test outputs.
- `git check-ignore --no-index` matches every one of the 305,166 moved regular files and symlinks. The 196,442 FIFOs
  match no pattern, but git never adds FIFOs.
- The unpushed WIP commit `97567e6d` (48,433 files, 69.8 GB, 176 files over 50 MB) was rebuilt as `e201b3e8`, with the same
  message, author and parent `origin/main`:
  - 37,440 files, 1.20 GB, largest 42.8 MB;
  - 10,993 paths dropped: 3,266 moved to the Trash and 7,727 still on disk but ignored;
  - the only other change is `.gitignore`;
  - a push would upload 27,355 blobs (0.84 GB), none over 50 MB.

  An intermediate rebuild, `f86523eb`, came before the scoped patterns and the restore. Fifty-nine of the dropped paths
  were already on GitHub: 55 `*.pbtxt` models and 2 CNFs from failed Kirkman searches (moved), and 2 Kirkman `*.pbtxt`
  files (kept on disk). Nothing was pushed.
- `97567e6d` stays reachable through the reflog, so `.git` still holds its 19.7 GB pack. That space comes back only after
  `git reflog expire` and `git gc`, which removes the rollback path. Neither was run.

## Known consequences

- Some lane `MANIFEST*`/`SHA256SUMS*` files list moved files, and some lane READMEs and verdicts say those files are
  "retained" or "kept", for example `packing-array19/README.md:353-354`. They were left unchanged, because closed-run
  records are append-only. This record supersedes them.
- Rebuilding a six-lane Lean replay needs the Mathlib d13f23b closure at `/private/tmp/seymour-lean-20261014-68365`, which no
  longer exists. That was already true before this cleanup.
- About 1.9 GB of untracked, non-ignored files remain, in 121k files, the largest 48.8 MB. They are mostly text and JSON
  certificates, receipts and logs of accepted results, which neither the type patterns nor the scoped patterns cover.
- The random5reg `work-dirs/` pattern also stops tracking the 81 small superseded job JSONs that stayed on disk.
  `outer/evidence/SHA256SUMS` still lists them.
