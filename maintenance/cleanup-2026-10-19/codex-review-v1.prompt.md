You are an independent, hostile reviewer of a planned cleanup of the research repository /Users/jinleic/repos/aifours. Static, read-only review: do not modify, move or create anything anywhere, and do not run solvers, builds, Lean, pip/uv or git write commands.

## Owner request (verbatim)
"clean up the ~/repos/aifours artifacts , so that the stale and failed artifacts can get removed , just make sure that the scripts to create the artifacts are preserved , then it is fine. also add these bulky artifcats file type or folder name into the .gitignore so that they wont get uploaded into the github"

## Plan under review
- Packet directory: /Users/jinleic/.omp/agent/sessions/-jinleic-workspace/2026-10-19T06-11-57-946Z_01a152c9-c77a-7030-a650-fcb212134bba/local/aifours-cleanup/review-packet-v1/
  - manifest-units.json: 227 candidate units (path, selector, category FAILED/STALE/REGENERABLE-ENV, evidence, generator, regeneration). Units with a non-null `excluded_by_parent` will NOT be moved.
  - moved-paths.txt: every entry that would be moved (kind f=file p=FIFO l=symlink, apparent bytes, repo-relative path). Large: use grep, never read whole.
  - keep-bulky.json: bulky artifacts that stay on disk (only git-ignored).
- Action: move (os.rename, same APFS volume) every listed entry into ~/.Trash/aifours-cleanup-20261019/<same relative path>, with a manifest; nothing is deleted.
- Preservation filter applied on top of each selector (except whole-directory REGENERABLE-ENV units such as venvs, uv caches, Lean .lake/toolchains): never move *.py *.sh *.lean *.c *.h *.cpp *.rs *.jl *.sage *.gp *.m *.ipynb *.toml *.cfg *.ini *.yaml *.yml *.md *.tex *.bib *.patch *.diff *.lock, Makefile, lakefile.*, lean-toolchain, lake-manifest.json, pyproject.toml, uv.lock, or names starting SHA256SUMS/MANIFEST/README/STATUS/RESULT/receipt/requirements or containing STOP; inside `selector: "all"` units only bulky types (*.cnf *.drat* *.lrat* *.zst *.xz *.olean *.ilean *.ltar *.pbtxt *.fifo), FIFOs and regular files >= 1 MB are moved, so small logs/receipts/JSON stay.
- A live 96-hour research run started 2026-10-18 22:59 PDT: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h (contract-v1.json) with lanes under */evidence/six-lane-20261018-96h/. Nothing under those paths is selected. Its lanes inherit older lanes (units flagged live_lane=true). Its contract (contract-v1.json:121) tells round workers to keep closed-run evidence, UNKNOWNs, FIFOs and intermediates; the owner's cleanup request is a separate direct instruction, and the owner will be asked whether to include live-inherited units.

## Authorities
Final report /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/final-report-v7.md, outcomes.md, transitions.json, parent verdicts in that review/ directory, lane README/LOG/STATUS files, and the live run's contract and lane code (read-only).

## Check, in priority order
1. Load-bearing evidence: does any unit move bytes that an accepted result (gate or accepted partial, per the final report) depends on and that is not retained elsewhere byte-identically or regenerable by a retained script? Priority: units >= 300 MB and all risk=medium units.
2. Live run: does any moved path appear in, or get read by, the live run's files/code (institute/runs/six-lane-2026-10-18-96h, */evidence/six-lane-20261018-96h/)? Note the live pa19 code lists STOP/HALT markers in .../packing-array19/cycle2 and hashes pinned files; the live moqls8 code reads scripts/BINDING from old review desks.
3. Script preservation: does any unit move an authored script/source/config (not a third-party env file), or a generator named by a unit? Is every unit's generator outside the moved set?
4. Category truth: spot-check at least 15 units across slices (S1..S5) that the cited evidence lines actually say failed/UNKNOWN/superseded/duplicate.

FIFO hazard: about 196,000 named pipes exist in the tree. Opening one blocks forever. Never cat/head/open a path unless it is a confirmed regular file; use rg (skips special files) or grep -D skip. Do not read or hash files > 1 MB.

## Output
Verdict line first: GO, GO-WITH-EXCLUSIONS, or HOLD. Then numbered findings, each with severity (BLOCKER/MAJOR/MINOR), the unit path, file:line evidence, and the exact change (e.g. "exclude unit X" or "narrow selector to Y"). Max 1500 words.
