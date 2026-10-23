# Lemma U certificate package v5 — reader and final-publication overlay (2026-10-19T08:41:58-0700)

Written only. Supersedes v4 runtime overlay; old sources unchanged. Answers /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-certificate-v4-source-codex-v1.prompt.stdout.txt
SHA25640fcc2edee624615e3124f9244894d3b08b44ecf4a177d6211a2fd5eb3a50cbc, HOLD: one MAJOR reader-coverage issue plus one
remaining MINOR stdout-completion gap. Original scientific LemmaU scoped acceptance is unaffected.
Format-v2 schema, controls nc0..10, literal claim, audited prefix and CHK-anchor EXP-D parent barrier remain unchanged.
No execution/configs/control runs, source parsing or compilation. All textual inspections/hash comparisons only.

## Complete runtime-reader policy
File bytes are read only through descriptor-bound O_RDONLY|O_NONBLOCK|O_NOFOLLOW opens, descriptor regular fstat,
actual cap+1 bounded loops (blocks<=64KiB); reject overflow, including growth after stat. Error classes preserved.
A FIFO cannot block before fstat. Input path replacement after opening cannot redirect the descriptor.
- Expectation artifacts+audits: read_entry retains anchored directory fd, plain-name restriction, regular type,
  nlink==1, declared-name/path and size guards; now NONBLOCK plus min(65536,cap+1-total), not1MiB overflow probes.
- Expectation plan/source/input/documentary-pin and nc6 raw reads: read_pinned retains bounded same-fd reader.
- Checker raw/cert read_capped_input retains same-fd budget-aware bounded reader, cap1MiB/8MiB.
- Producer and generator raw/source-certificate reader retains same-fd bounded helper, cap1MiB/8MiB.
- Every entrypoint algorithm load NOW uses NONBLOCK|NOFOLLOW, descriptor regular fstat, bounded cap+1 reading,
  cap1MiB; protected exceptions stay ENTRY_ALGORITHM_LOAD_ERROR95, actual hash mismatch96.
- Producer/generator NEVER reopen __file__ for informational hashes. Wrapper injects VERIFIED_SOURCE_SHA256 from
  the SAME already-read/hash-checked/compiled source bytes. Informational only, not a substitute for artifact pins.
  Thus no unbudgeted source reread precedes algorithm Budget construction. Direct unwrapped invocation has no
  injected digest, but cannot qualify under the exact GO/argv/pin/audit contract.
- Directory walks use O_DIRECTORY|O_NOFOLLOW and pinned fds; they do not consume file data. GO stdin remains the
  independently bounded3byte protocol plus1byte probe with fresh cutoff checks.
Real regular-file I/O latency still needs the supervisor independent wall deadline; no OS hard real-time guarantee.
Transient block+joined input payload<=2*cap, as in v4; no snapshot files or additional declared outputs.

## Final stdout-completion policy
Each algorithm checks deadline AFTER print(line,flush=True) returns, not only before it.
- Producer/generator/expectations late => return5.
- Checker late => ERROR2, including if the emitted verdict was INVALID and would normally exit1.
The emitted line and retained evidence are immutable: no rewrite, no second JSON line. Printed status/wall_s may
precede completion; exact child exit and parent/supervisor endpoint timing govern release. Parent audit MUST reject
late/non-success exit even if line/file match and a result field says OK/VALID/INVALID. Scientific invalid1 controls
never count as passed when the completion exit isERROR2. I/O exceptions remain their original error mappings.
Pre/post file-publication and per-mutant/manifest clock checks from v4 stay in force.

## Sources and independence
Final scientific checker is /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v3.py (ed93f236c342925eded12b299b52cfb5f6fb5b7835d30833cb8ff0b22b759dcb).
Math block hash/bytes identical to original independent checker; only I/O boundary revisions by integration owner.
I/O contract /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/cert_checker/cert_checker_v3-io-contract-v1.md SHA2564f11fbf058a48f0cd8cd7d5be1c690345bed9116b1efe0f996801d402128768d.
No producer import or math/rank/basis/rainbow/coverage change. nc6 independently derived fix retained unchanged.

## Supervisor authority
Governing correction: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-supervisor-v10-scope-parent-correction-v1.json, SHA256fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2.
The old e441d858 scope decision supplies NO launch authority. Mandatory owned bounded /bin/date helper and complete
known ownership/unresolved-census obligations remain supervisor responsibilities. Science algorithms are still
single-process and launch no helper; that restriction DOES NOT discharge supervisor/helper settlement requirements.
Supervisor version qualification is pending, not presumed. Startup/loading/GO + algorithm + final flush all count
in total admission;120s child GO allowance plus240s self-budget is NOT automatically a300s whole job.
No automatic chaining. Every21 job has its own exact parent GO and parent post-exit audit. CHK-anchor GO must cite
completed AUDITED_PASS EXP-D audit (path+sha). Audit exact exit, actual artifacts and single emitted line before release.

## Pin inventory and states
Planv5 replaces every executable/entrypoint path+hash and I/O contract; explicitly inventories formatv2, THIS overlay,
nested nc9 provenance, originalspec/erratum/format and governing supervisor correction too. Gate verifies all entries.
New sources unexecuted/unqualified. GLOBAL HOLD persists. Beta-route source work remains PAUSED.
No mathematical status changes: exact-anchor LemmaU scoped acceptance intact, both extension questions UNKNOWN,
sixMOLS39/CFR6,39 OPEN. No further science or claim follows from readiness.
